# Prioritizing Cardiovascular Screening Outreach (CDC BRFSS 2023)

IT135IU Introduction to Data Science · Course project · Topic 15 (own topic) · International University, VNU-HCM

**Decision question.** Which adult population groups should a public-health program prioritize for cardiovascular screening and prevention outreach,
based on combinations of major cardiovascular risk factors and reported cardiovascular disease burden?

## Team

| Member | Student ID | Role |
|---|---|---|
| Vũ Tiến Dũng | ITDSIU25011 | Product Owner |
| Mai Hoàng Gia Bảo | ITDSIU25005 | Data Engineer |
| Lê Nguyễn Trúc Phương | ITDSIU25029 | Data Analyst |
| Nguyễn Trần Phước Lộc | ITDSIU25020 | Visualisation Lead |
| Huỳnh Bá Dũng | ITDSIU25012 | Reproducibility Lead |
| Dương Minh Chính | ITDSIU25007 | Ethics and Privacy Officer |

Some scripts and notebooks refer to roles by the proposal's codes: M1 Product Owner, M2 Data Engineer, M3 Data Analyst, M4 Visualisation Lead, M5 Reproducibility Lead, M6 Ethics and Privacy Officer (same order as the table above).

## Data

CDC Behavioral Risk Factor Surveillance System (BRFSS) 2023, combined landline and cell phone file: 433,323 adult respondents, 350 columns, of which 29 are kept.

| File | In the repository? | Why |
|---|---|---|
| Raw CDC file `LLCP2023.XPT` (1.2 GB) | No | Too large and public; download it and check the SHA-256 in `data/README.md` |
| `brfss2023_working.parquet` (8 MB, 433,323 × 29, raw CDC codes) | No | Rebuilt from the raw file by notebook 01 or `scripts/` |
| `brfss2023_clean.parquet` (9 MB, 425,106 × 47, written by notebook 02) | **Yes** | Input of notebook 03, so D3 and the charts run without the 1.2 GB download; SHA-256 in `data/README.md`, section 8 |
| `brfss2023_ml_frozen.parquet` (321,978 × 13) | No | Written by notebook 03 for the later machine-learning step; contract in `docs/d3_outputs/ml_data_contract.md` |

> Data source: Centers for Disease Control and Prevention (CDC), Behavioral Risk Factor Surveillance System (BRFSS) 2023.
> This analysis was produced by students of International University, VNU-HCM and has not been reviewed or endorsed by CDC, HHS or the U.S. Government.

## Deliverable status

| Step | Content | Where | Status |
|---|---|---|---|
| D1 | Proposal | Blackboard | submitted |
| D2 | Data and profiling: load and merge, data profile, cleaning log, five data manipulations | `notebooks/02_d2_data_profiling_cleaning.ipynb`, outputs in `docs/d2_outputs/` | submitted |
| D3 | Statistical relationship (risk factors and reported CVD), priority-group candidates, at least three charts, reproducibility package | `notebooks/03_priority_analysis.ipynb`, outputs in `docs/d3_outputs/` | analysis done; charts, final README and environment file pending |
| D4 | Report and slides | not in this repository | due 22 Nov 2026 |

## Repository layout

```
README.md                    this file
requirements.txt             Python packages used (see the header of the file for the Python versions)
data/README.md               source, retrieval record, checksums, terms of use, decisions handed to analysis
data/lookup/                 state_lookup.csv: state FIPS -> name, USPS code, Census region (used in the D2 merge)
data/processed/              brfss2023_clean.parquet (tracked); other generated files are git-ignored
docs/                        variable dictionary, source verification, manifest, data profile
docs/cdc/                    CDC calculated-variable documentation (PDF)
docs/d2_outputs/             D2 tables: data profile, cleaning log, sample flow, prevalence tables, integrity checks
docs/d3_outputs/             D3 tables: prevalence by risk count, logistic models, candidate table, sensitivity, ML data contract
docs/ai_use_note.md          how AI assistance was used (draft, to be confirmed by the Ethics and Privacy Officer)
notebooks/01_data_preparation.ipynb       builds the working dataset from the CDC file (Data Engineer)
notebooks/02_d2_data_profiling_cleaning.ipynb   D2: profiling, cleaning log and five data manipulations; writes the clean dataset
notebooks/03_priority_analysis.ipynb      D3: survey-weighted prevalence, models, priority-group candidates
scripts/                     01_verify_source.py, 02_build_working_dataset.py (used by notebook 01); make_d2_zip.py (packs the D2 submission)
```

Pipeline: `LLCP2023.XPT` → notebook 01 → `brfss2023_working.parquet` → notebook 02 → `brfss2023_clean.parquet` → notebook 03 → `docs/d3_outputs/*.csv` → charts.

## Reproduce

Python 3.12 or newer. Run every command from the project root.

1. `python -m pip install -r requirements.txt`
2. **Fastest route (D3 only).** `data/processed/brfss2023_clean.parquet` is already in the repository. Open `notebooks/03_priority_analysis.ipynb` and choose **Restart kernel → Run All**. It rewrites `docs/d3_outputs/` and creates the git-ignored ML file.
3. **Full route.** Download the CDC file as described in `data/README.md` (sections 2 and 7), run `notebooks/01_data_preparation.ipynb` (about 1.2 GB read), then notebook 02, then notebook 03.
4. Check any rebuilt file against the SHA-256 values in `data/README.md`. A different pyarrow version can change the hash without changing the data; compare the shape and the key totals in `docs/d2_outputs/d2_sample_flow.csv` in that case.

The seed is fixed at 42 in every notebook; D2 and D3 use no randomness except the 1,000-row sample written by notebook 01.

## What the analysis found (descriptive, not causal)

**D2 (data).**

* The working file has 433,323 respondents; 8,217 from Guam, Puerto Rico and the U.S. Virgin Islands are removed, leaving 425,106 in 48 states and DC (Kentucky and Pennsylvania were not released by CDC for 2023).
* Unknown answers are never coded as "No". Requiring all six risk factors and the outcome to be known leaves an analysis sample of 321,978 (74.3% of the working file); the loss is driven by unknown cholesterol, BMI and smoking status.
* Respondents dropped by that rule are younger (mean age 40.4 against 51.0) and report less CVD (5.7% against 9.9%, weighted), so results describe the complete-case population, and D3 compares groups within age bands.

**D3 (analysis).** Reported CVD means a heart attack, angina or coronary heart disease, or stroke, ever diagnosed; risk factors are hypertension, high cholesterol, diabetes, obesity, smoking and physical inactivity.

* Weighted prevalence of reported CVD rises with the number of risk factors: 2.2%, 5.4%, 10.9%, 18.6%, 25.6%, 33.3% and 39.7% for 0 to 6 factors; overall 9.90% (95% CI 9.68–10.12).
* Each additional risk factor multiplies the odds of reported CVD by 1.84 (crude) and 1.61 after adjusting for age band and sex.
* The candidate table cuts the sample into 15 groups (5 age bands × 3 risk bands) and marks a group as a priority candidate when it has at least 100 respondents with reported CVD, a confidence-interval half-width of at most 25% of its own prevalence, a lower confidence limit above the overall prevalence, and at least 5% of the total weighted CVD burden. Five groups qualify: age 65+ with 2–3 factors, 65+ with 4–6, 65+ with 0–1, 55–64 with 2–3 and 55–64 with 4–6. Together they are 37.5% of the weighted population and 76.4% of the reported CVD burden. The list does not change when the case minimum (50, 100, 200) and the interval-width limit (20%, 25%, 30%) are varied (`d3_sensitivity_priority_groups.csv`); the 5% burden floor was not varied.
* The thresholds are the analyst's proposal. The product owner owns the final rule, including whether the 65+ group with only 0–1 factors should stay on the list.

## Limitations

Self-reported telephone survey; cross-sectional, so associations are not causes; "reported CVD" means already diagnosed, so it does not measure undiagnosed disease; complete-case selection; results describe adults in the 48 states and DC of the 2023 public file only.
