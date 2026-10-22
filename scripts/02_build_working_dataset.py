#!/usr/bin/env python3
"""
02_build_working_dataset.py  --  M2 (Data Engineer), Step 2.

Reads ONLY the variables the project needs from the raw BRFSS 2023 XPT file and saves them as
data/processed/brfss2023_working.parquet (about 30 columns instead of 350).

Rules (agreed boundary with M3):
  * Values stay as the RAW CDC codes. No recoding, no dropping rows. M3 owns cleaning.
  * Row order is unchanged. Whole-number columns become nullable integers (Int64);
    BLANK/'.' becomes <NA>. Weights stay float.
  * The saved file is re-loaded and checked against the CDC codebook frequencies.

Also writes:
  docs/data_profile.csv               per-variable dtype, missing count, min/max, value counts
  docs/working_dataset_manifest.json  rows, columns, SHA-256, versions (for M5's reproducibility audit)

Usage (project root):
  python -m pip install pyarrow
  python scripts/02_build_working_dataset.py
"""
import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent


def load_step1():
    """Reuse constants and the XPT reader from 01_verify_source.py."""
    spec = importlib.util.spec_from_file_location("step1", HERE / "01_verify_source.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def tally(series) -> dict:
    out = {}
    for v, n in series.value_counts(dropna=False).items():
        out["missing" if pd.isna(v) else int(v)] = int(n)
    return out


def to_nullable_int(df: pd.DataFrame) -> pd.DataFrame:
    """Whole-number numeric columns -> Int64 (keeps NA); everything else unchanged."""
    out = df.copy()
    for c in out.columns:
        s = out[c]
        if pd.api.types.is_numeric_dtype(s):
            nn = s.dropna()
            if len(nn) and (nn % 1 == 0).all() and c != "_LLCPWT":
                out[c] = s.astype("Int64")
    return out


def check_against_codebook(step1, df: pd.DataFrame) -> dict:
    res = {"rows_ok": len(df) == step1.EXPECTED_ROWS}
    res["value_counts_ok"] = {
        v: step1.compare(exp, tally(df[v]))["ok"]
        for v, exp in step1.EXPECTED_VALUE_COUNTS.items()}
    exp_state = {k: n for k, (_, n) in step1.EXPECTED_STATES.items()}
    res["state_counts_ok"] = step1.compare(exp_state, tally(df["_STATE"]))["ok"]
    w = df["_LLCPWT"]
    res["weight_ok"] = bool(w.notna().all() and (w > 0).all())
    res["all_ok"] = bool(res["rows_ok"] and all(res["value_counts_ok"].values())
                         and res["state_counts_ok"] and res["weight_ok"])
    return res


def profile(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for c in df.columns:
        s = df[c]
        n_unique = int(s.nunique(dropna=True))
        top = ""
        if n_unique <= 20:
            top = "; ".join(f"{k}:{v}" for k, v in sorted(tally(s).items(), key=lambda kv: str(kv[0])))
        rows.append({"variable": c, "dtype": str(s.dtype), "n_rows": len(s),
                     "n_missing": int(s.isna().sum()),
                     "pct_missing": round(100 * s.isna().mean(), 2),
                     "n_unique": n_unique,
                     "min": s.min(), "max": s.max(), "value_counts": top})
    return pd.DataFrame(rows)


def sha256_of(path: Path, block: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(block):
            h.update(chunk)
    return h.hexdigest()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--xpt", type=Path, default=Path("data/raw/LLCP2023.XPT"))
    ap.add_argument("--out", type=Path, default=Path("data/processed/brfss2023_working.parquet"))
    ap.add_argument("--docs", type=Path, default=Path("docs"))
    a = ap.parse_args(argv)

    step1 = load_step1()
    wanted = [c for g in step1.REQUIRED_VARS.values() for c in g]

    print(f"Reading {len(wanted)} columns from {a.xpt} ...")
    df, all_cols = step1.read_needed(a.xpt, wanted)
    missing = [c for c in wanted if c not in df.columns]
    if missing:
        sys.exit(f"Variables not found in XPT: {missing}")
    df = to_nullable_int(df[wanted])

    pre = check_against_codebook(step1, df)
    if not pre["all_ok"]:
        sys.exit(f"Checks failed BEFORE saving: {pre}")

    a.out.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(a.out, index=False)
    back = pd.read_parquet(a.out)
    post = check_against_codebook(step1, back)
    same = back.shape == df.shape and list(back.columns) == list(df.columns)
    if not (post["all_ok"] and same):
        sys.exit(f"Checks failed AFTER reloading parquet: {post}")

    a.docs.mkdir(parents=True, exist_ok=True)
    profile(back).to_csv(a.docs / "data_profile.csv", index=False, encoding="utf-8-sig")

    src = a.docs / "source_verification.json"
    xpt_sha = None
    if src.exists():
        xpt_sha = json.loads(src.read_text(encoding="utf-8")).get("files", {}).get("xpt", {}).get("sha256")
    try:
        import pyarrow
        pa_ver = pyarrow.__version__
    except Exception:
        pa_ver = None
    manifest = {
        "created_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "source_xpt": str(a.xpt), "source_xpt_sha256": xpt_sha,
        "output": str(a.out), "output_bytes": a.out.stat().st_size, "output_sha256": sha256_of(a.out),
        "rows": int(back.shape[0]), "columns": int(back.shape[1]), "column_names": list(back.columns),
        "all_columns_in_source": len(all_cols),
        "recoding": "none (raw CDC codes)",
        "checks_after_reload": post,
        "versions": {"python": sys.version.split()[0], "pandas": pd.__version__, "pyarrow": pa_ver},
    }
    (a.docs / "working_dataset_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Saved {a.out}  ({back.shape[0]:,} rows x {back.shape[1]} columns, {manifest['output_bytes']/1e6:.1f} MB)")
    print(f"Parquet SHA-256: {manifest['output_sha256']}")
    print("Reload check vs codebook:", "OK" if post["all_ok"] else post)
    print("Wrote docs/data_profile.csv and docs/working_dataset_manifest.json")
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
