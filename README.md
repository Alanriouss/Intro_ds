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

## Data

CDC Behavioral Risk Factor Surveillance System (BRFSS) 2023, combined landline and cell phone file: 433,323 adult respondents, 350 columns, of which 29 are kept.
The raw file (1.2 GB) and the processed files are **not stored in this repository**; `data/README.md` records the source, checksums, terms of use and how to rebuild them.

> Data source: Centers for Disease Control and Prevention (CDC), Behavioral Risk Factor Surveillance System (BRFSS) 2023.
> This analysis was produced by students of International University, VNU-HCM and has not been reviewed or endorsed by CDC, HHS or the U.S. Government.

## Deliverable status

| Step | Content | Where |
|---|---|---|
| D1 | Proposal | submitted on Blackboard |
| D2 | Data and profiling: load and merge, data profile, cleaning log, five data manipulations | `notebooks/02_d2_data_profiling_cleaning.ipynb`, outputs in `docs/d2_outputs/` |
| D3 | Statistical relationship, charts, reproducibility package | in progress |

## Repository layout

```
data/README.md              source, retrieval record, checksums, terms of use, decisions handed to analysis
data/lookup/                state_lookup.csv: state FIPS -> name, USPS code, Census region (used in the D2 merge)
data/processed/             working and clean datasets (not tracked; see data/README.md)
docs/                       variable dictionary, source verification, manifest, CDC documentation
docs/d2_outputs/            D2 tables: data profile, cleaning log, sample flow, prevalence tables, integrity checks
notebooks/01_...ipynb       builds the working dataset from the CDC file (M2)
notebooks/02_...ipynb       D2: profiling, cleaning log and five data manipulations
scripts/                    verification, build and packaging scripts
```

## Reproduce D2

1. Create a Python 3.12+ environment and run `python -m pip install -r requirements.txt`.
2. Put `brfss2023_working.parquet` in `data/processed/` (build it with `notebooks/01_data_preparation.ipynb`, or copy the team-drive file and compare its SHA-256 with `data/README.md`, section 8).
3. Open `notebooks/02_d2_data_profiling_cleaning.ipynb`, choose **Restart kernel → Run All**. The seed is fixed at 42 (D2 uses no randomness).

## What D2 found (descriptive, not causal)

* Working file 433,323 respondents; 8,217 from Guam, Puerto Rico and the U.S. Virgin Islands are removed, leaving 425,106 in 48 states and DC (Kentucky and Pennsylvania were not released by CDC for 2023).
* Unknown answers are never coded as "No". Requiring all six risk factors and the outcome to be known leaves an analysis sample of 321,978 (74.3% of the working file); the loss is driven by unknown cholesterol, BMI and smoking status (notebook section 5.2 compares those dropped with those kept).
* Respondents dropped by that rule are younger (mean age 40.4 against 51.0) and have lower reported CVD (5.7% against 9.9%, weighted), so the sample level overstates the adult-population level; D3 compares groups within age bands.
* Weighted reported cardiovascular disease rises from 2.2% among adults with no risk factor to 39.7% among adults with all six, and also rises with age in every risk band. Age is therefore a major confounder to handle in D3.

## Limitations

Self-reported telephone survey; "reported CVD" means already diagnosed, so it does not measure undiagnosed disease; complete-case selection; results describe adults in the 48 states and DC of the 2023 public file only.
