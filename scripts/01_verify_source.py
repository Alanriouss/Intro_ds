#!/usr/bin/env python3
"""
01_verify_source.py  --  M2 (Data Engineer), Step 1: verify the BRFSS 2023 download.

What it does (all local; the raw file never leaves your machine):
  1. Records file size + SHA-256 of the ZIP and/or XPT (and of the documentation files).
  2. Confirms the XPT has the expected number of records and lists its columns.
  3. Confirms every variable the project needs exists in the file.
  4. Compares value counts of the 3 CVD outcome variables, _MICHD and _STATE against
     the frequencies printed in the CDC codebook (LLCP 2023 Codebook Report).
  5. Writes docs/source_verification.json  -> paste the key numbers into data/README.md.

Usage (from the project root):
  python scripts/01_verify_source.py --zip data/raw/LLCP2023XPT.zip --docs docs/cdc
  python scripts/01_verify_source.py --xpt data/raw/LLCP2023.XPT

Requires: pandas (always) and, optionally, pyreadstat (faster, reads only the needed columns).
Raw data is read-only here: nothing in data/raw is modified.
"""
import argparse
import datetime as dt
import hashlib
import json
import sys
import zipfile
from pathlib import Path

# ----------------------------------------------------------------------------
# Expected values, copied from the CDC 2023 codebook (Codebook Report dated Sep 10, 2024)
# ----------------------------------------------------------------------------
EXPECTED_ROWS = 433_323
EXPECTED_GEOGRAPHIES = 52            # 48 states + DC + Guam + Puerto Rico + Virgin Islands
ABSENT_FIPS = {21: "Kentucky", 42: "Pennsylvania"}   # not in the 2023 public file

REQUIRED_VARS = {
    "outcome":      ["CVDINFR4", "CVDCRHD4", "CVDSTRK3", "_MICHD"],
    "risk_factors": ["BPHIGH6", "_RFHYPE6", "CHOLCHK3", "TOLDHI3", "_RFCHOL3", "DIABETE4",
                     "_BMI5", "_BMI5CAT", "_RFBMI5", "_SMOKER3", "_RFSMOK3", "EXERANY2", "_TOTINDA"],
    "demographic":  ["_AGEG5YR", "_AGE80", "_AGE_G", "_SEX", "SEXVAR", "_INCOMG1", "_EDUCAG", "_RACE", "_STATE"],
    "survey_design": ["_LLCPWT", "_STSTR", "_PSU"],
}

# value -> frequency ("missing" = BLANK / '.' in the codebook)
EXPECTED_VALUE_COUNTS = {
    "CVDINFR4": {1: 23451, 2: 407304, 7: 2314, 9: 251, "missing": 3},
    "CVDCRHD4": {1: 23454, 2: 405638, 7: 3936, 9: 292, "missing": 3},
    "CVDSTRK3": {1: 18350, 2: 413499, 7: 1212, 9: 258, "missing": 4},
    "_MICHD":   {1: 36311, 2: 392427, "missing": 4585},
}

# FIPS -> [name, frequency] from the _STATE table of the codebook
EXPECTED_STATES = {
    1: ["Alabama", 4362],
    2: ["Alaska", 5525],
    4: ["Arizona", 12036],
    5: ["Arkansas", 5351],
    6: ["California", 11976],
    8: ["Colorado", 8783],
    9: ["Connecticut", 9501],
    10: ["Delaware", 4282],
    11: ["District of Columbia", 3207],
    12: ["Florida", 13255],
    13: ["Georgia", 8227],
    15: ["Hawaii", 7832],
    16: ["Idaho", 6895],
    17: ["Illinois", 5279],
    18: ["Indiana", 10993],
    19: ["Iowa", 8876],
    20: ["Kansas", 9884],
    22: ["Louisiana", 5388],
    23: ["Maine", 12255],
    24: ["Maryland", 17255],
    25: ["Massachusetts", 9528],
    26: ["Michigan", 9978],
    27: ["Minnesota", 16170],
    28: ["Mississippi", 4069],
    29: ["Missouri", 7219],
    30: ["Montana", 7143],
    31: ["Nebraska", 12886],
    32: ["Nevada", 2650],
    33: ["New Hampshire", 6960],
    34: ["New Jersey", 9328],
    35: ["New Mexico", 3220],
    36: ["New York", 17349],
    37: ["North Carolina", 4088],
    38: ["North Dakota", 5745],
    39: ["Ohio", 13384],
    40: ["Oklahoma", 6727],
    41: ["Oregon", 6234],
    44: ["Rhode Island", 5781],
    45: ["South Carolina", 10038],
    46: ["South Dakota", 5886],
    47: ["Tennessee", 5645],
    48: ["Texas", 10059],
    49: ["Utah", 11154],
    50: ["Vermont", 7636],
    51: ["Virginia", 6981],
    53: ["Washington", 26444],
    54: ["West Virginia", 4339],
    55: ["Wisconsin", 12819],
    56: ["Wyoming", 4484],
    66: ["Guam", 1559],
    72: ["Puerto Rico", 4594],
    78: ["Virgin Islands", 2064],
}


# ----------------------------------------------------------------------------
def sha256_of(path: Path, block: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(block):
            h.update(chunk)
    return h.hexdigest()


def file_record(path: Path) -> dict:
    return {"path": str(path), "bytes": path.stat().st_size, "sha256": sha256_of(path)}


def tally(series) -> dict:
    """Value counts with NaN reported as 'missing' and numeric codes as int."""
    out = {}
    for v, n in series.value_counts(dropna=False).items():
        out["missing" if v != v else int(v)] = int(n)
    return out


def compare(expected: dict, observed: dict) -> dict:
    keys = set(expected) | set(observed)
    diff = {str(k): {"expected": expected.get(k, 0), "observed": observed.get(k, 0)}
            for k in keys if expected.get(k, 0) != observed.get(k, 0)}
    return {"ok": not diff, "differences": diff}


def check_loaded(df, columns: list) -> dict:
    """Pure function: all content checks on a DataFrame holding the needed columns."""
    res = {"rows": {"expected": EXPECTED_ROWS, "observed": len(df), "ok": len(df) == EXPECTED_ROWS}}
    res["value_counts"] = {v: compare(e, tally(df[v]))
                           for v, e in EXPECTED_VALUE_COUNTS.items() if v in df.columns}
    if "_STATE" in df.columns:
        obs = tally(df["_STATE"])
        exp = {fips: n for fips, (_, n) in EXPECTED_STATES.items()}
        res["state_counts"] = compare(exp, obs)
        res["geographies"] = {"expected": EXPECTED_GEOGRAPHIES, "observed": len(obs),
                              "ok": len(obs) == EXPECTED_GEOGRAPHIES}
        res["kentucky_pennsylvania_absent"] = not (set(obs) & set(ABSENT_FIPS))
    if "_LLCPWT" in df.columns:
        w = df["_LLCPWT"]
        res["weight"] = {"missing": int(w.isna().sum()), "non_positive": int((w <= 0).sum()),
                         "sum_of_weights": float(w.sum())}   # logged for the record only
    needed = [c for g in REQUIRED_VARS.values() for c in g]
    res["required_vars_missing"] = [c for c in needed if c not in columns]
    return res


def read_needed(xpt: Path, wanted: list):
    """Return (DataFrame with wanted columns, list of all column names)."""
    try:
        import pyreadstat
        _, meta = pyreadstat.read_xport(str(xpt), metadataonly=True, encoding="ISO-8859-1")
        cols = list(meta.column_names)
        use = [c for c in wanted if c in cols]
        df, _ = pyreadstat.read_xport(str(xpt), usecols=use, encoding="ISO-8859-1")
        return df, cols
    except ImportError:
        import pandas as pd
        parts, cols = [], None
        for chunk in pd.read_sas(str(xpt), format="xport", chunksize=50_000, encoding="latin-1"):
            if cols is None:
                cols = list(chunk.columns)
            parts.append(chunk[[c for c in wanted if c in chunk.columns]])
        return pd.concat(parts, ignore_index=True), cols


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--zip", type=Path, help="Downloaded LLCP2023XPT.zip")
    ap.add_argument("--xpt", type=Path, help="Extracted LLCP2023.XPT (if no --zip)")
    ap.add_argument("--docs", type=Path, help="Folder with codebook/PDF documentation to hash")
    ap.add_argument("--out", type=Path, default=Path("docs/source_verification.json"))
    a = ap.parse_args(argv)
    if not (a.zip or a.xpt):
        ap.error("give --zip or --xpt")

    report = {"verified_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
              "files": {}}
    xpt = a.xpt
    if a.zip:
        report["files"]["zip"] = file_record(a.zip)
        with zipfile.ZipFile(a.zip) as z:
            members = [m for m in z.namelist() if m.lower().endswith(".xpt")]
            if not members:
                sys.exit("No .XPT inside the zip")
            xpt = a.zip.parent / Path(members[0]).name
            if not xpt.exists():
                z.extract(members[0], a.zip.parent)
                if Path(a.zip.parent / members[0]) != xpt:
                    (a.zip.parent / members[0]).replace(xpt)
    report["files"]["xpt"] = file_record(xpt)
    if a.docs:
        report["files"]["docs"] = [file_record(p) for p in sorted(a.docs.rglob("*")) if p.is_file()]

    wanted = sorted({c for g in REQUIRED_VARS.values() for c in g})
    df, cols = read_needed(xpt, wanted)
    report["n_columns"] = {"observed": len(cols), "proposal_says": 350, "codebook_documents": 344}
    report["checks"] = check_loaded(df, cols)

    c = report["checks"]
    ok = (c["rows"]["ok"] and not c["required_vars_missing"]
          and all(v["ok"] for v in c["value_counts"].values())
          and c.get("state_counts", {"ok": True})["ok"] and c.get("kentucky_pennsylvania_absent", True))
    report["all_checks_passed"] = bool(ok)

    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"XPT: {xpt}  ({report['files']['xpt']['bytes']:,} bytes)")
    print(f"SHA-256: {report['files']['xpt']['sha256']}")
    print(f"Rows: {c['rows']['observed']:,} (expected {EXPECTED_ROWS:,})   Columns: {len(cols)} (proposal says 350)")
    print(f"Missing required variables: {c['required_vars_missing'] or 'none'}")
    for v, r in c["value_counts"].items():
        print(f"  {v}: {'OK' if r['ok'] else 'MISMATCH ' + str(r['differences'])}")
    if "state_counts" in c:
        print(f"  _STATE counts vs codebook: {'OK' if c['state_counts']['ok'] else 'MISMATCH'}; "
              f"geographies={c['geographies']['observed']}; KY/PA absent={c['kentucky_pennsylvania_absent']}")
    print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED -> see " + str(a.out))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())



