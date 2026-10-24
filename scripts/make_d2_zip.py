#!/usr/bin/env python3
"""Pack the D2 submission for Blackboard (M5 / whoever uploads).

Usage (from the project root, after running the notebook and exporting its PDF):
  python scripts/make_d2_zip.py --pdf path/to/exported.pdf
Optional: --notebook (default notebooks/02_d2_data_profiling_cleaning.ipynb), --repo (default below).

Creates D2_Topic15_Phuong_Chinh_Dung_Loc_Dung_Bao.zip containing, at the top level of the zip:
  <name>.ipynb   the executed notebook
  <name>.pdf     its PDF export
  <name>.txt     the repository link
"""
import argparse, json, sys, zipfile
from pathlib import Path

NAME = "D2_Topic15_Phuong_Chinh_Dung_Loc_Dung_Bao"
DEFAULT_REPO = "https://github.com/Alanriouss/Intro_ds"

ap = argparse.ArgumentParser()
ap.add_argument("--pdf", required=True)
ap.add_argument("--notebook", default="notebooks/02_d2_data_profiling_cleaning.ipynb")
ap.add_argument("--repo", default=DEFAULT_REPO)
ap.add_argument("--out", default=".")
a = ap.parse_args()

nb_path, pdf_path = Path(a.notebook), Path(a.pdf)
for p in (nb_path, pdf_path):
    if not p.exists():
        sys.exit(f"Missing file: {p}")
if pdf_path.suffix.lower() != ".pdf":
    sys.exit("--pdf must be a .pdf file")
if not a.repo.startswith("https://github.com/"):
    sys.exit("Repository link must start with https://github.com/")

nb = json.loads(nb_path.read_text(encoding="utf-8"))
code = [c for c in nb["cells"] if c["cell_type"] == "code"]
with_out = [c for c in code if c.get("outputs")]
errors = [o for c in code for o in c.get("outputs", []) if o.get("output_type") == "error"]
print(f"code cells: {len(code)} | with saved output: {len(with_out)} | errors: {len(errors)}")
if len(with_out) < len(code) - 2:
    sys.exit("The notebook has not been run (most cells have no output). Restart kernel -> Run All, save, then retry.")
if errors:
    sys.exit("The notebook contains error outputs. Fix them and run all cells again.")
if pdf_path.stat().st_size < 50_000:
    print("WARNING: the PDF is very small. Check that it shows the tables and outputs.")

out = Path(a.out) / f"{NAME}.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(nb_path, f"{NAME}.ipynb")
    z.write(pdf_path, f"{NAME}.pdf")
    z.writestr(f"{NAME}.txt", a.repo + "\n")
print("Created", out.resolve(), f"({out.stat().st_size / 1e6:.1f} MB)")
with zipfile.ZipFile(out) as z:
    for i in z.infolist():
        print("  ", i.filename, i.file_size)
