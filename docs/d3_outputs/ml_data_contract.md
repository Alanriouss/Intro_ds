# ML data contract

File: `data/processed/brfss2023_ml_frozen.parquet` (git-ignored, shared through the team drive) | Rows: 321,978 | Columns: 13 | SHA-256: `90f7fac9e1a57e2ed0dd89878a476b51056af2dc79996408e6de2ddc751b881d`

## Target
`CVD_ANY`: 1 = ever told they had a heart attack, angina/coronary heart disease or stroke; 0 = none of the three (self-reported).
Positive share (unweighted): 12.35%, so the classes are imbalanced: report precision, recall, F1 and ROC-AUC, not accuracy alone.

## Allowed features
- `HTN_FLAG`
- `CHOL_FLAG`
- `DIABETES_FLAG`
- `OBESITY_FLAG`
- `SMOKING_FLAG`
- `INACTIVE_FLAG`
- `_AGE80`
- `_SEX`

## Never use as features (leakage)
- `MI_FLAG`
- `CHD_FLAG`
- `STROKE_FLAG`
- `_MICHD`
- `CVDINFR4`
- `CVDCRHD4`
- `CVDSTRK3`

## Other columns (not features)
`RiskCount` (sum of the six flags, redundant with them); `_LLCPWT`, `_STSTR`, `_PSU` (survey weight and design).

## Missing values
Complete-case sample from D2: no missing values, no imputation. Unknown answers were never coded as "No".
