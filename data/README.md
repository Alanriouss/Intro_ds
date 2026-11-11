# Data provenance: BRFSS 2023

Owner: Mai Hoàng Gia Bảo (Data Engineer) · Reviewer: Dương Minh Chính (Ethics and Privacy Officer) · Status: source verified, working dataset built (D2), clean dataset added for D3

## 1. Source

| Item | Value |
|---|---|
| Dataset | Behavioral Risk Factor Surveillance System (BRFSS), 2023, Combined Landline and Cell Phone data (`LLCP2023`) |
| Publisher | U.S. Centers for Disease Control and Prevention (CDC) |
| Landing page | https://www.cdc.gov/brfss/annual_data/annual_2023.html |
| Data file | `LLCP2023XPT.zip` (SAS Transport format). 93,237,818 bytes as downloaded |
| Records | 433,323 (stated by CDC, and confirmed by the codebook frequencies) |
| Unit | Adult (18+) respondents, noninstitutionalized, telephone survey, cross-sectional |

## 2. Retrieval record

| Item | Value |
|---|---|
| Retrieval date | 20 Oct 2026 (file timestamp; confirmed with Bảo on 24 Oct 2026). The 13 Sep 2026 in the proposal was the planned date, not the download date |
| Retrieved by | Mai Hoàng Gia Bảo (Data Engineer) |
| ZIP size / SHA-256 | 93,237,818 bytes / `d1ab80e4806a1d07bd3e40ec78c971ad9ff920f3ea5f6049780aeaa41ff31f43` |
| XPT size / SHA-256 | 1,205,554,400 bytes / `3d3bf8ef5195bde227828ddc4c90745b76e8b304f8f5b9a043b6d99895fd1615` |
| Columns observed in XPT | 350 (proposal says 350; codebook documents 344, see section 5) |
| All checks passed | Yes (`docs/source_verification.json`) |

Raw files stay in `data/raw/` untouched and are git-ignored. Anyone can re-download from the landing page and compare the SHA-256.

## 3. Documentation used

| File | Version / date |
|---|---|
| `USCODE23_LLCP_021924.HTML` (codebook) | Report header: "LLCP 2023 Codebook Report, September 10, 2024", data weighted with `_LLCPWT`. The file name suggests Feb 2024, so cite the header date |
| `2023-calculated-variables-version4-508.pdf` | Cover: Version #12, revised May 23, 2024 |
| `2023-Child-Weighting-Calculated-Variables-508.pdf` | Version #3, revised May 23, 2024. Concerns the Random Child Selection module only, **not used** in this project |

## 4. Terms of use and attribution

Under CDC's "Use of Agency Materials" page (https://www.cdc.gov/other/agencymaterials.html), public-domain CDC content requires:

1. **Attribution** to the developing agency, for example "Source: CDC / BRFSS 2023".
2. A **disclaimer** that use of the material does not imply endorsement by CDC, HHS or the U.S. Government.

Suggested wording for the report and slides:

> Data source: Centers for Disease Control and Prevention (CDC), Behavioral Risk Factor Surveillance System (BRFSS) 2023. This analysis was produced by students of International University, VNU-HCM and has not been reviewed or endorsed by CDC, HHS or the U.S. Government.

Do not use CDC/HHS logos. Only analysis-necessary fields are kept, and no attempt is made to identify respondents (proposal Section 8). Wording confirmed by the Product Owner (Vũ Tiến Dũng) on 12 Nov 2026, on behalf of the Ethics and Privacy Officer; the Officer may still amend it before the report.

## 5. Verification log (codebook cross-check)

| Check | Result |
|---|---|
| Record count | Frequencies in `_STATE`, `CVDINFR4`, `CVDCRHD4`, `CVDSTRK3`, `_MICHD` each sum to 433,323 |
| Geography | 52 areas: 48 states, DC, Guam, Puerto Rico, US Virgin Islands. **Kentucky and Pennsylvania are absent** from the 2023 public file (CDC comparability document) |
| Survey-design variables | `_LLCPWT`, `_STSTR`, `_PSU` are documented (values hidden in the codebook report, so check them in the XPT) |
| Needed variables | All variables in `REQUIRED_VARS` of the script are documented in the codebook |
| Not documented | `_IMPAGE`, `_DENSTR2`, `_GEOSTR` are not in the codebook. Use `_AGE80` / `_AGEG5YR` rather than `_IMPAGE` |
| Variable count | The XPT has **350** columns, matching the proposal. The codebook documents only **344**, so 6 columns are undocumented (three known: `_IMPAGE`, `_DENSTR2`, `_GEOSTR`) |
| Executive-order modification | The calculated-variables PDF states the file was modified to comply with executive orders, so some values may be missing. The codebook still has `SOMALE`/`SOFEMALE` (sexual orientation) but no gender-identity variable was found. Not used in this project, but record it as a limitation |

## 6. Findings handed off to analysis, and how D2 resolved them

- **`_MICHD` excludes stroke.** It covers only MI or CHD. `CVD_ANY` needs `CVDINFR4`, `CVDCRHD4` **and** `CVDSTRK3`. Observed codebook counts: `_MICHD` has 4,585 missing records.
- **`CVDCRHD4` = "angina or coronary heart disease"**. Wording matters for the ethics review.
- **Special codes.** 7 = Don't know, 9 = Refused, blank = not asked/missing. Do not recode to "No".
- **`_RFCHOL3`** is blank (51,811 records) when cholesterol was never checked or unknown, separate from code 9. Decide how to treat "not checked".
- **`_RFHYPE6`** code 1 ("No") includes `BPHIGH6` = 2 (told only during pregnancy), 3 (no) and 4 (told borderline/pre-hypertensive). Decide whether that fits the "risk factor" definition.
- **Diabetes** has no calculated variable. Use `DIABETE4` (1 = yes; 2 = pregnancy only; 3 = no; 4 = pre-diabetes; 7/9 = unknown).
- **`_BMI5`** is stored with 2 implied decimals (divide by 100). `_RFBMI5` means overweight **or** obese; the proposal's "obesity" corresponds to `_BMI5CAT` = 4. `_BMI5CAT` is missing for 40,535 records (9.35%).
- **`_AGEG5YR` = 14** (don't know / refused / missing) has 7,779 records (1.80%). `_INCOMG1` = 9 has 86,623 records (19.99%).
- **Weights.** Use `_LLCPWT` with `_STSTR` and `_PSU`. Decide whether to restrict to the 50 states + DC (excluding Guam, PR, USVI) before describing results as "U.S. adults".

How these were resolved in D2 (details in `docs/d2_outputs/d2_cleaning_log.csv`):

| Hand-off | Decision |
|---|---|
| Territories | Guam, Puerto Rico and USVI removed (8,217 rows, C1); results cover the 48 states and DC in the file (Kentucky and Pennsylvania are absent) |
| `CVD_ANY` | 1 if MI, CHD or stroke is "Yes", even when another answer is unknown; 0 only when all three are "No"; otherwise unknown (C13) |
| Unknown answers | Kept as `<NA>`, never coded as "No" (C4-C12) |
| Hypertension, cholesterol | CDC definitions kept as they are: `_RFHYPE6` code 1 (includes borderline) is 0 (C4); blank `_RFCHOL3` (cholesterol never checked) is unknown, not "normal" (C5) |
| Diabetes, obesity | Pregnancy-only and pre-diabetes coded 0 (C6); obesity is `_BMI5CAT` = 4, BMI of 30 or more (C7) |
| `RiskCount` | Sum of the six flags, only when all six are known (C14); `IN_SAMPLE` also needs known `CVD_ANY` and age: 321,978 rows (C16) |

## 7. Reproduce (from the project root)

Windows PowerShell:

```powershell
python -m pip install -r requirements.txt
Expand-Archive -Path data\raw\LLCP2023XPT.zip -DestinationPath data\raw
python scripts\01_verify_source.py --xpt data\raw\LLCP2023.XPT --docs docs\cdc
python scripts\02_build_working_dataset.py
```

macOS / Linux:

```bash
python -m pip install -r requirements.txt
unzip data/raw/LLCP2023XPT.zip -d data/raw
python scripts/01_verify_source.py --xpt data/raw/LLCP2023.XPT --docs docs/cdc
python scripts/02_build_working_dataset.py
```

Or run `notebooks/01_data_preparation.ipynb` top to bottom. Script 01 prints a pass/fail summary and writes `docs/source_verification.json`. Script 02 writes the parquet file, `docs/data_profile.csv` and `docs/working_dataset_manifest.json`.

## 8. Working dataset

`data/processed/brfss2023_working.parquet`: 433,323 rows × 29 columns, raw CDC codes (no recoding), row order as in the XPT.
SHA-256: `89a9229dc02692ff8c1766228de9ca9b00ed1e9b09e65c5527f3f4b36e5911b0`
Dictionary: `docs/variable_dictionary.md` (and `.csv`) · Profile: `docs/data_profile.csv` · Manifest: `docs/working_dataset_manifest.json`

The working file is git-ignored and shared through the team drive. Compare its SHA-256 with the value above before use. If it is rebuilt (for example with another pyarrow version) the hash may change while the data stay the same; check the row count and column list, then update this section and the manifest.

### Clean dataset (tracked)

`data/processed/brfss2023_clean.parquet`: 425,106 rows × 47 columns (the working file without the 8,217 territory rows, plus the derived 0/1 flags, `CVD_ANY`, `RiskCount`, `AGE_BAND` and `IN_SAMPLE`). Written by `notebooks/02_d2_data_profiling_cleaning.ipynb`; 9,414,730 bytes.
SHA-256: `5415732cfd26e14f0a701faa644f9174a60e9715714c05370892356d104414ea`

It is committed (9 MB) so that notebook 03 and the charts run without the 1.2 GB download. It holds the 29 CDC fields of the working file (listed in `docs/variable_dictionary.md`) plus the derived columns; the public BRFSS file has no names or direct identifiers. Treat it as derived from CDC public data under section 4. Do not edit it by hand: change the notebook and regenerate.

The other generated files (`brfss2023_ml_frozen.parquet`, `sample_1000.csv`) stay git-ignored.

## 9. Tools and AI use

Python 3.12 or newer; package versions are pinned in `requirements.txt`, which also records the Python version of each notebook run (3.12 on Windows for notebook 01 and the scripts; 3.13.5 for D2 and 3.14.2 for D3, both on macOS). Notebooks 02 and 03 need `jinja2` for table styling. Variable definitions come from CDC's codebook and calculated-variable documentation; the CDC SAS logic is not re-implemented here.
AI assistance (Claude) was used to draft the scripts and the dictionary. Results were checked against the CDC codebook and by running the scripts locally (`docs/source_verification.json`). The Ethics and Privacy Officer confirms the wording in `docs/ai_use_note.md`.
