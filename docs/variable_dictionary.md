# Variable dictionary: BRFSS 2023 working dataset

Owner: M2 · Source: CDC LLCP 2023 Codebook Report (Sep 10, 2024) and 2023 Calculated Variables (v12, May 23, 2024).
Values are **raw codes as released by CDC**. No recoding has been done (M3 owns cleaning). Counts below are from the codebook (n = 433,323).

**Special codes (general rule):** 7 / 77 / 777 = Don't know; 9 / 99 / 999 = Refused; BLANK = not asked or missing. Never recode these to "No".

## Summary

| Variable | Role | Label | Missing/unknown codes | % of records |
|---|---|---|---|---:|
| `CVDINFR4` | outcome | Ever Diagnosed with Heart Attack | 7, 9, BLANK | 0.59 |
| `CVDCRHD4` | outcome | Ever Diagnosed with Angina or Coronary Heart Disease | 7, 9, BLANK | 0.98 |
| `CVDSTRK3` | outcome | Ever Diagnosed with a Stroke | 7, 9, BLANK | 0.34 |
| `_MICHD` | outcome | Ever had CHD or MI | BLANK | 1.06 |
| `BPHIGH6` | risk_factor | Ever Told Blood Pressure High | 7, 9, BLANK | 0.44 |
| `_RFHYPE6` | risk_factor | High Blood Pressure Calculated Variable | 9 | 0.44 |
| `CHOLCHK3` | risk_factor | How Long since Cholesterol Checked | 7, 9, BLANK | 6.10 |
| `TOLDHI3` | risk_factor | Ever Told Cholesterol Is High | 7, 9, BLANK | 12.71 |
| `_RFCHOL3` | risk_factor | High Cholesterol Calculated Variable | 9, BLANK | 12.71 |
| `DIABETE4` | risk_factor | (Ever told) you had diabetes | 7, 9, BLANK | 0.23 |
| `_BMI5` | risk_factor | Computed body mass index | BLANK | 9.35 |
| `_BMI5CAT` | risk_factor | Computed body mass index categories | BLANK | 9.35 |
| `_RFBMI5` | risk_factor | Overweight or obese calculated variable | 9 | 9.35 |
| `_SMOKER3` | risk_factor | Computed Smoking Status | 9 | 5.32 |
| `_RFSMOK3` | risk_factor | Current Smoking Calculated Variable | 9 | 5.32 |
| `EXERANY2` | risk_factor | Exercise in Past 30 Days | 7, 9, BLANK | 0.29 |
| `_TOTINDA` | risk_factor | Leisure Time Physical Activity Calculated Variable | 9 | 0.29 |
| `_AGEG5YR` | demographic | Reported age in five-year age categories calculated variable | 14 | 1.80 |
| `_AGE80` | demographic | Imputed Age value collapsed above 80 | none | 0.00 |
| `_AGE_G` | demographic | Imputed age in six groups | none | 0.00 |
| `_SEX` | demographic | Calculated sex variable | none | 0.00 |
| `SEXVAR` | demographic | Sex of Respondent | none | 0.00 |
| `_INCOMG1` | demographic | Computed income categories | 9 | 19.99 |
| `_EDUCAG` | demographic | Computed level of education completed categories | 9 | 0.54 |
| `_RACE` | demographic | Computed Race-Ethnicity grouping | 9, BLANK | 2.21 |
| `_STATE` | demographic | State FIPS Code | none | 0.00 |
| `_LLCPWT` | survey_design | Final weight: Land-line and cell-phone data | none | 0.00 |
| `_STSTR` | survey_design | Sample Design Stratification Variable | none | 0.00 |
| `_PSU` | survey_design | Primary Sampling Unit | none | 0.00 |

## Outcome

### `CVDINFR4`: Ever Diagnosed with Heart Attack

- Codebook section: Chronic Health Conditions Core; column: 138
- Question: (Ever told) you had a heart attack, also called a myocardial infarction?
- **Missing / unknown codes:** 7, 9, BLANK (2,568 records, 0.59%). Keep as-is; M3 decides treatment.
- **Project note:** Outcome component (heart attack / MI).

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Yes | 23,451 | 5.41 | 4.16 |
| 2 | No | 407,304 | 94.00 | 95.17 |
| 7 | Don't know/Not sure | 2,314 | 0.53 | 0.61 |
| 9 | Refused | 251 | 0.06 | 0.05 |
| BLANK | Not asked or Missing | 3 | . | . |

### `CVDCRHD4`: Ever Diagnosed with Angina or Coronary Heart Disease

- Codebook section: Chronic Health Conditions Core; column: 139
- Question: (Ever told) (you had) angina or coronary heart disease?
- **Missing / unknown codes:** 7, 9, BLANK (4,231 records, 0.98%). Keep as-is; M3 decides treatment.
- **Project note:** Outcome component. Label covers angina OR coronary heart disease: use this wording in the report.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Yes | 23,454 | 5.41 | 4.03 |
| 2 | No | 405,638 | 93.61 | 95.15 |
| 7 | Don't know/Not sure | 3,936 | 0.91 | 0.76 |
| 9 | Refused | 292 | 0.07 | 0.06 |
| BLANK | Not asked or Missing | 3 | . | . |

### `CVDSTRK3`: Ever Diagnosed with a Stroke

- Codebook section: Chronic Health Conditions Core; column: 140
- Question: (Ever told) (you had) a stroke.
- **Missing / unknown codes:** 7, 9, BLANK (1,474 records, 0.34%). Keep as-is; M3 decides treatment.
- **Project note:** Outcome component (stroke). Not part of _MICHD.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Yes | 18,350 | 4.23 | 3.37 |
| 2 | No | 413,499 | 95.43 | 96.30 |
| 7 | Don't know/Not sure | 1,212 | 0.28 | 0.26 |
| 9 | Refused | 258 | 0.06 | 0.06 |
| BLANK | Not asked or Missing | 4 | . | . |

### `_MICHD`: Ever had CHD or MI

- Codebook section: Calculated Variables; column: 1994
- Question: Respondents that have ever reported having coronary heart disease (CHD) or myocardial infarction (MI)
- **Missing / unknown codes:** BLANK (4,585 records, 1.06%). Keep as-is; M3 decides treatment.
- **Project note:** MI or CHD only. Does NOT include stroke, so CVD_ANY must be built from the three CVD* variables.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Reported having MI or CHD Notes: CVDINFR4=1 OR CVDCRHD4=1 | 36,311 | 8.47 | 6.47 |
| 2 | Did not report having MI or CHD Notes: CVDINFR4=2 AND CVDCRHD4=2 | 392,427 | 91.53 | 93.53 |
| BLANK | Not asked or Missing Notes: CVDINFR4=7, 9 or Missing OR CVDCRHD4=7, 9, or Missing | 4,585 | . | . |

## Risk Factor

### `BPHIGH6`: Ever Told Blood Pressure High

- Codebook section: Hypertension Awareness Core; column: 133
- Question: Have you ever been told by a doctor, nurse or other health professional that you have high blood pressure? (If Yes - and respondent is female, ask Was this only when you were pregnant?.)
- **Missing / unknown codes:** 7, 9, BLANK (1,919 records, 0.44%). Keep as-is; M3 decides treatment.
- **Project note:** Raw item. 1 = yes; 2 = yes but only during pregnancy; 3 = no; 4 = told borderline/pre-hypertensive. Codes 2, 3 and 4 all become "No" (1) in _RFHYPE6.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Yes | 176,222 | 40.67 | 34.28 |
| 2 | Yes, but female told only during pregnancy - Go to Section 06.01 CHOLCHK3 | 3,280 | 0.76 | 0.90 |
| 3 | No - Go to Section 06.01 CHOLCHK3 | 247,855 | 57.20 | 63.46 |
| 4 | Told borderline high or pre-hypertensive or elevated blood pressure - Go to Section 06.01 CHOLCHK3 | 4,047 | 0.93 | 0.84 |
| 7 | Don't know/Not Sure - Go to Section 06.01 CHOLCHK3 | 1,312 | 0.30 | 0.36 |
| 9 | Refused - Go to Section 06.01 CHOLCHK3 | 604 | 0.14 | 0.15 |
| BLANK | Not asked or Missing | 3 | . | . |

### `_RFHYPE6`: High Blood Pressure Calculated Variable

- Codebook section: Calculated Variables; column: 1991
- Question: Adults who have been told they have high blood pressure by a doctor, nurse, or other health professional
- **Missing / unknown codes:** 9 (1,919 records, 0.44%). Keep as-is; M3 decides treatment.
- **Project note:** 1 = No, 2 = Yes (note the 1/2 coding), 9 = unknown. Group "No" includes pregnancy-only and borderline.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | No Notes: BPHIGH6 = 2 or 3 or 4 | 255,182 | 58.89 | 65.20 |
| 2 | Yes Notes: BPHIGH6 = 1 | 176,222 | 40.67 | 34.28 |
| 9 | Don't know/Not Sure/Refused/Missing Notes: BPHIGH6 = 7 or 9 or Missing | 1,919 | 0.44 | 0.52 |

### `CHOLCHK3`: How Long since Cholesterol Checked

- Codebook section: Cholesterol Awareness Core; column: 135
- Question: About how long has it been since you last had your cholesterol checked?
- **Missing / unknown codes:** 7, 9, BLANK (26,449 records, 6.10%). Keep as-is; M3 decides treatment.
- **Project note:** Raw item: time since last cholesterol check.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Never - Go to Section 07.01 CVDINFR4 | 25,362 | 5.85 | 8.14 |
| 2 | Within the past year (anytime less than one year ago) | 307,737 | 71.02 | 65.62 |
| 3 | Within the past 2 years (1 year but less than 2 years ago) | 38,772 | 8.95 | 9.61 |
| 4 | Within the past 3 years (2 years but less than 3 years ago) | 12,240 | 2.82 | 3.22 |
| 5 | Within the past 4 years (3 years but less than 4 years ago) | 5,495 | 1.27 | 1.43 |
| 6 | Within the past 5 years (4 years but less than 5 years ago) | 4,378 | 1.01 | 1.10 |
| 7 | Don't know/Not Sure - Go to Section 07.01 CVDINFR4 | 25,705 | 5.93 | 7.38 |
| 8 | 5 or more years ago | 12,890 | 2.97 | 3.29 |
| 9 | Refused - Go to Section 07.01 CVDINFR4 | 741 | 0.17 | 0.20 |
| BLANK | Not asked or Missing | 3 | . | . |

### `TOLDHI3`: Ever Told Cholesterol Is High

- Codebook section: Cholesterol Awareness Core; column: 136
- Question: Have you ever been told by a doctor, nurse or other health professional that your cholesterol is high?
- **Missing / unknown codes:** 7, 9, BLANK (55,084 records, 12.71%). Keep as-is; M3 decides treatment.
- **Project note:** Raw item: ever told cholesterol high (only asked if checked).

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Yes | 158,906 | 41.65 | 37.20 |
| 2 | No | 219,333 | 57.49 | 61.96 |
| 7 | Don't know/Not Sure | 2,868 | 0.75 | 0.71 |
| 9 | Refused | 404 | 0.11 | 0.12 |
| BLANK | Not asked or Missing Notes: Section 06.01, CHOLCHK3, is coded 1, 7, 9, or Missing | 51,812 | . | . |

### `_RFCHOL3`: High Cholesterol Calculated Variable

- Codebook section: Calculated Variables; column: 1993
- Question: Adults who have had their cholesterol checked and have been told by a doctor, nurse, or other health professional that it was high
- **Missing / unknown codes:** 9, BLANK (55,084 records, 12.71%). Keep as-is; M3 decides treatment.
- **Project note:** BLANK when never checked / unknown (not code 9). Decide how to treat "not checked".

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | No Notes: CHOLCHK3 = 2,3,4,5,6 or 8 and TOLDHI3 = 2 | 219,333 | 57.49 | 61.96 |
| 2 | Yes Notes: CHOLCHK3 = 2,3,4,5,6 or 8 and TOLDHI3 = 1 | 158,906 | 41.65 | 37.20 |
| 9 | Don't know/Not Sure Or Refused/Missing Notes: CHOLCHK3 = 2,3,4,5,6 or 8 and TOLDHI3 = 7 or 9 or Missing | 3,273 | 0.86 | 0.83 |
| BLANK | Missing Notes: CHOLCHK3 = 1 or 7 or 9 or Missing | 51,811 | . | . |

### `DIABETE4`: (Ever told) you had diabetes

- Codebook section: Chronic Health Conditions Core; column: 149
- Question: (Ever told) (you had) diabetes? (If Yes - and respondent is female, ask Was this only when you were pregnant? If Respondent says pre-diabetes or borderline diabetes, use response code 4.)
- **Missing / unknown codes:** 7, 9, BLANK (984 records, 0.23%). Keep as-is; M3 decides treatment.
- **Project note:** No calculated variable. 1 = yes; 2 = pregnancy only; 3 = no; 4 = pre-diabetes/borderline; 7/9 = unknown.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Yes | 59,786 | 13.80 | 12.04 |
| 2 | Yes, but female told only during pregnancy - Go to Section 08.01 AGE | 3,253 | 0.75 | 0.93 |
| 3 | No - Go to Section 08.01 AGE | 358,706 | 82.78 | 84.16 |
| 4 | No, pre-diabetes or borderline diabetes - Go to Section 08.01 AGE | 10,594 | 2.44 | 2.58 |
| 7 | Don't know/Not Sure - Go to Section 08.01 AGE | 683 | 0.16 | 0.21 |
| 9 | Refused - Go to Section 08.01 AGE | 296 | 0.07 | 0.08 |
| BLANK | Not asked or Missing | 5 | . | . |

### `_BMI5`: Computed body mass index

- Codebook section: Calculated Variables; column: 2082-2085
- Question: Body Mass Index (BMI)
- **Missing / unknown codes:** BLANK (40,535 records, 9.35%). Keep as-is; M3 decides treatment.
- **Project note:** Stored with 2 implied decimals: divide by 100. Missing if height/weight unknown or pregnant.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 - 9999 | 1 or greater Notes: WTKG3/(HTM4*HTM4) (Has 2 implied decimal places) | 392,788 | 100.00 | 100.00 |
| BLANK | Don't know/Refused/Missing Notes: WTKG3 = 777 or 999 or HTM4 = 777 or 999 | 40,535 | . | . |

### `_BMI5CAT`: Computed body mass index categories

- Codebook section: Calculated Variables; column: 2086
- Question: Four-categories of Body Mass Index (BMI)
- **Missing / unknown codes:** BLANK (40,535 records, 9.35%). Keep as-is; M3 decides treatment.
- **Project note:** Proposal "obesity" = 4. Underweight=1, Normal=2, Overweight=3, Obese=4.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Underweight Notes: _BMI5 < 1850 (_BMI5 has 2 implied decimal places) | 6,767 | 1.72 | 1.96 |
| 2 | Normal Weight Notes: 1850 <= _BMI5 < 2500 | 116,500 | 29.66 | 30.50 |
| 3 | Overweight Notes: 2500 <= _BMI5 < 3000 | 139,615 | 35.54 | 34.73 |
| 4 | Obese Notes: 3000 <= _BMI5 < 9999 | 129,906 | 33.07 | 32.80 |
| BLANK | Don't know/Refused/Missing Notes: _BMI5 = 9999 | 40,535 | . | . |

### `_RFBMI5`: Overweight or obese calculated variable

- Codebook section: Calculated Variables; column: 2087
- Question: Adults who have a body mass index greater than 25.00 (Overweight or Obese)
- **Missing / unknown codes:** 9 (40,535 records, 9.35%). Keep as-is; M3 decides treatment.
- **Project note:** Overweight OR obese (BMI >= 25). Not the same as obesity.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | No Notes: 1200 <= _BMI5 < 2500 (_BMI5 has 2 implied decimal places) | 123,267 | 28.45 | 28.92 |
| 2 | Yes Notes: 2500 <= _BMI5 < 9999 | 269,521 | 62.20 | 60.15 |
| 9 | Don't know/Refused/Missing Notes: _BMI5 = 9999 | 40,535 | 9.35 | 10.93 |

### `_SMOKER3`: Computed Smoking Status

- Codebook section: Calculated Variables; column: 2091
- Question: Four-level smoker status: Everyday smoker, Someday smoker, Former smoker, Non-smoker
- **Missing / unknown codes:** 9 (23,062 records, 5.32%). Keep as-is; M3 decides treatment.
- **Project note:** Current smoker = 1 or 2; former = 3; never = 4; 9 = unknown.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Current smoker - now smokes every day Notes: SMOKE100 = 1 and SMOKEDAY = 1 | 31,770 | 7.33 | 7.24 |
| 2 | Current smoker - now smokes some days Notes: SMOKE100 = 1 and SMOKEDAY = 2 | 13,376 | 3.09 | 3.44 |
| 3 | Former smoker Notes: SMOKE100 = 1 and SMOKEDAY = 3 | 113,134 | 26.11 | 22.15 |
| 4 | Never smoked Notes: SMOKE100 = 2 | 251,981 | 58.15 | 60.93 |
| 9 | Don't know/Refused/Missing Notes: SMOKE100 = 1 and SMOKEDAY = 9 or SMOKE100 = 7 or 9 or Missing | 23,062 | 5.32 | 6.25 |

### `_RFSMOK3`: Current Smoking Calculated Variable

- Codebook section: Calculated Variables; column: 2092
- Question: Adults who are current smokers
- **Missing / unknown codes:** 9 (23,062 records, 5.32%). Keep as-is; M3 decides treatment.
- **Project note:** 1 = No, 2 = Yes (current smoker), 9 = unknown.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | No Notes: _SMOKER3 = 3 or 4 | 365,115 | 84.26 | 83.08 |
| 2 | Yes Notes: _SMOKER3 = 1 or 2 | 45,146 | 10.42 | 10.68 |
| 9 | Don't know/Refused/Missing Notes: _SMOKER3 = 9 | 23,062 | 5.32 | 6.25 |

### `EXERANY2`: Exercise in Past 30 Days

- Codebook section: Exercise (Physical Activity) Core; column: 113
- Question: During the past month, other than your regular job, did you participate in any physical activities or exercises such as running, calisthenics, golf, gardening, or walking for exercise?
- **Missing / unknown codes:** 7, 9, BLANK (1,251 records, 0.29%). Keep as-is; M3 decides treatment.
- **Project note:** Raw item: any physical activity in past 30 days (outside regular job).

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Yes | 325,227 | 75.05 | 75.03 |
| 2 | No - Go to Section 04.08 STRENGTH | 106,845 | 24.66 | 24.71 |
| 7 | Don't know/Not Sure - Go to Section 04.08 STRENGTH | 927 | 0.21 | 0.19 |
| 9 | Refused - Go to Section 04.08 STRENGTH | 322 | 0.07 | 0.07 |
| BLANK | Not asked or Missing | 2 | . | . |

### `_TOTINDA`: Leisure Time Physical Activity Calculated Variable

- Codebook section: Calculated Variables; column: 1902
- Question: Adults who reported doing physical activity or exercise during the past 30 days other than their regular job
- **Missing / unknown codes:** 9 (1,251 records, 0.29%). Keep as-is; M3 decides treatment.
- **Project note:** 1 = had activity, 2 = no activity (physical inactivity = 2), 9 = unknown.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Had physical activity or exercise Notes: EXERANY2 = 1 | 325,227 | 75.05 | 75.03 |
| 2 | No physical activity or exercise in last 30 days Notes: EXERANY2 = 2 | 106,845 | 24.66 | 24.71 |
| 9 | Don't know/Refused/Missing Notes: EXERANY2 = 7 or 9 or Missing | 1,251 | 0.29 | 0.26 |

## Demographic

### `_AGEG5YR`: Reported age in five-year age categories calculated variable

- Codebook section: Calculated Variables; column: 2065-2066
- Question: Fourteen-level age category
- **Missing / unknown codes:** 14 (7,779 records, 1.80%). Keep as-is; M3 decides treatment.
- **Project note:** 14 levels; 14 = don't know/refused/missing.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Age 18 to 24 Notes: 18 <= AGE <= 24 | 26,280 | 6.06 | 12.37 |
| 2 | Age 25 to 29 Notes: 25 <= AGE <= 29 | 21,247 | 4.90 | 7.38 |
| 3 | Age 30 to 34 Notes: 30 <= AGE <= 34 | 24,803 | 5.72 | 9.11 |
| 4 | Age 35 to 39 Notes: 35 <= AGE <= 39 | 27,153 | 6.27 | 7.62 |
| 5 | Age 40 to 44 Notes: 40 <= AGE <= 44 | 28,463 | 6.57 | 8.47 |
| 6 | Age 45 to 49 Notes: 45 <= AGE <= 49 | 27,070 | 6.25 | 6.45 |
| 7 | Age 50 to 54 Notes: 50 <= AGE <= 54 | 31,291 | 7.22 | 7.83 |
| 8 | Age 55 to 59 Notes: 55 <= AGE <= 59 | 34,219 | 7.90 | 7.11 |
| 9 | Age 60 to 64 Notes: 60 <= AGE <= 64 | 41,974 | 9.69 | 8.60 |
| 10 | Age 65 to 69 Notes: 65 <= AGE <= 69 | 46,099 | 10.64 | 6.94 |
| 11 | Age 70 to 74 Notes: 70 <= AGE <= 74 | 43,533 | 10.05 | 6.48 |
| 12 | Age 75 to 79 Notes: 75 <= AGE <= 79 | 34,543 | 7.97 | 4.55 |
| 13 | Age 80 or older Notes: 80 <= AGE <= 99 | 38,869 | 8.97 | 5.24 |
| 14 | Don't know/Refused/Missing Notes: 7 <= AGE <= 9 | 7,779 | 1.80 | 1.84 |

### `_AGE80`: Imputed Age value collapsed above 80

- Codebook section: Calculated Variables; column: 2068-2069
- Question: Imputed Age value collapsed above 80
- **Missing / unknown codes:** none (0 records, 0.00%). Keep as-is; M3 decides treatment.
- **Project note:** Age capped at 80. _IMPAGE is not in the codebook.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 18 - 24 | Imputed Age 18 to 24 | 26,281 | 6.06 | 12.37 |
| 25 - 29 | Imputed Age 25 to 29 | 21,255 | 4.91 | 7.38 |
| 30 - 34 | Imputed Age 30 to 34 | 24,822 | 5.73 | 9.12 |
| 35 - 39 | Imputed Age 35 to 39 | 27,332 | 6.31 | 7.71 |
| 40 - 44 | Imputed Age 40 to 44 | 28,892 | 6.67 | 8.73 |
| 45 - 49 | Imputed Age 45 to 49 | 27,789 | 6.41 | 6.71 |
| 50 - 54 | Imputed Age 50 to 54 | 34,059 | 7.86 | 8.50 |
| 55 - 59 | Imputed Age 55 to 59 | 35,772 | 8.26 | 7.29 |
| 60 - 64 | Imputed Age 60 to 64 | 42,166 | 9.73 | 8.64 |
| 65 - 69 | Imputed Age 65 to 69 | 46,398 | 10.71 | 7.00 |
| 70 - 74 | Imputed Age 70 to 74 | 44,992 | 10.38 | 6.71 |
| 75 - 79 | Imputed Age 75 to 79 | 34,681 | 8.00 | 4.58 |
| 80 - 99 | Imputed Age 80 or older | 38,884 | 8.97 | 5.25 |

### `_AGE_G`: Imputed age in six groups

- Codebook section: Calculated Variables; column: 2070
- Question: Six-level imputed age category
- **Missing / unknown codes:** none (0 records, 0.00%). Keep as-is; M3 decides treatment.
- **Project note:** Six-level age group from imputed age.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Age 18 to 24 Notes: 18 <= _IMPAGE <= 24 | 26,281 | 6.06 | 12.37 |
| 2 | Age 25 to 34 Notes: 25 <= _IMPAGE <= 34 | 46,077 | 10.63 | 16.50 |
| 3 | Age 35 to 44 Notes: 35 <= _IMPAGE <= 44 | 56,224 | 12.98 | 16.44 |
| 4 | Age 45 to 54 Notes: 45 <= _IMPAGE <= 54 | 61,848 | 14.27 | 15.21 |
| 5 | Age 55 to 64 Notes: 55 <= _IMPAGE <= 64 | 77,938 | 17.99 | 15.93 |
| 6 | Age 65 or older Notes: _IMPAGE => 65 | 164,955 | 38.07 | 23.54 |

### `_SEX`: Calculated sex variable

- Codebook section: Calculated Variables; column: 2064
- Question: Calculated sex variable
- **Missing / unknown codes:** none (0 records, 0.00%). Keep as-is; M3 decides treatment.
- **Project note:** Calculated sex (1 male, 2 female), derived from SEXVAR (counts differ by 18 records).

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Male Notes: SEXVAR=1 | 203,800 | 47.03 | 48.50 |
| 2 | Female Notes: SEXVAR=2 | 229,523 | 52.97 | 51.50 |

### `SEXVAR`: Sex of Respondent

- Codebook section: Respondent Sex; column: 88
- Question: Sex of Respondent
- **Missing / unknown codes:** none (0 records, 0.00%). Keep as-is; M3 decides treatment.
- **Project note:** Sex of respondent (raw).

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Male - Code=1 if LANDSEX2=1 or CELLSEX2=1 | 203,782 | 47.03 | 48.50 |
| 2 | Female - Code=2 if LANDSEX2=2 or CELLSEX2=2 | 229,541 | 52.97 | 51.50 |

### `_INCOMG1`: Computed income categories

- Codebook section: Calculated Variables; column: 2090
- Question: Income categories
- **Missing / unknown codes:** 9 (86,623 records, 19.99%). Keep as-is; M3 decides treatment.
- **Project note:** 9 = unknown/refused (about 20% of records).

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Less than $15,000 Notes: INCOME3=1,2 | 19,187 | 4.43 | 4.88 |
| 2 | $15,000 to < $25,000 Notes: INCOME3=3,4 | 31,069 | 7.17 | 7.53 |
| 3 | $25,000 to < $35,000 Notes: INCOME3=5 | 38,508 | 8.89 | 8.88 |
| 4 | $35,000 to < $50,000 Notes: INCOME3=6 | 47,502 | 10.96 | 10.42 |
| 5 | $50,000 to < $100,000 Notes: INCOME3=7,8 | 107,027 | 24.70 | 22.29 |
| 6 | $100,000 to < $200,000 Notes: INCOME3=9,10 | 76,637 | 17.69 | 17.49 |
| 7 | $200,000 or more Notes: INCOME3=11 | 26,770 | 6.18 | 6.78 |
| 9 | Don't know/Not sure/Missing Notes: INCOME3=77, 99, or Missing | 86,623 | 19.99 | 21.73 |

### `_EDUCAG`: Computed level of education completed categories

- Codebook section: Calculated Variables; column: 2089
- Question: Level of education completed
- **Missing / unknown codes:** 9 (2,325 records, 0.54%). Keep as-is; M3 decides treatment.
- **Project note:** 9 = unknown/refused.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Did not graduate High School Notes: EDUCA = 1 or 2 or 3 | 25,172 | 5.81 | 11.57 |
| 2 | Graduated High School Notes: EDUCA = 4 | 106,613 | 24.60 | 27.04 |
| 3 | Attended College or Technical School Notes: EDUCA = 5 | 114,346 | 26.39 | 29.90 |
| 4 | Graduated from College or Technical School Notes: EDUCA = 6 | 184,867 | 42.66 | 30.90 |
| 9 | Don't know/Not sure/Missing Notes: EDUCA = 9 or Missing | 2,325 | 0.54 | 0.59 |

### `_RACE`: Computed Race-Ethnicity grouping

- Codebook section: Calculated Race Variables; column: 2060
- Question: Race/ethnicity categories
- **Missing / unknown codes:** 9, BLANK (9,570 records, 2.21%). Keep as-is; M3 decides treatment.
- **Project note:** Race/ethnicity, 9 = unknown. Optional for equity checks.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | White only, non-Hispanic Notes: _HISPANC = 2 and _MRACE1 = 10 | 313,067 | 72.26 | 55.63 |
| 2 | Black only, non-Hispanic Notes: _HISPANC = 2 and _MRACE1 = 20 | 32,919 | 7.60 | 11.69 |
| 3 | American Indian or Alaskan Native only, Non-Hispanic Notes: _HISPANC = 2 and _MRACE1 = 30 | 6,795 | 1.57 | 0.99 |
| 4 | Asian only, non-Hispanic Notes: _HISPANC = 2 and _MRACE1 = 40,41,42,43,44,45,46,47 | 12,105 | 2.79 | 6.00 |
| 5 | Native Hawaiian or other Pacific Islander only, Non-Hispanic Notes: _HISPANC = 2 and _MRACE1 = 50,51,52,53,54 | 2,097 | 0.48 | 0.33 |
| 6 | Other race only, non-Hispanic Notes: _HISPANC = 2 and _MRACE1 = 60 | 3,359 | 0.78 | 1.03 |
| 7 | Multiracial, non-Hispanic Notes: _HISPANC = 2 and _MRACE1 = 77 | 10,125 | 2.34 | 2.68 |
| 8 | Hispanic Notes: _HISPANC = 1 | 43,286 | 9.99 | 19.34 |
| 9 | Don't know/Not sure/Refused Notes: _HISPANC = 7 or 9 or _MRACE1 = 77 or 99 and _HISPANC = 2 | 9,484 | 2.19 | 2.31 |
| BLANK | Missing Notes: _HISPANC = Missing or _MRACE1 = Missing | 86 | . | . |

### `_STATE`: State FIPS Code

- Codebook section: Record Identification; column: 1-2
- Question: State FIPS Code
- **Missing / unknown codes:** none (0 records, 0.00%). Keep as-is; M3 decides treatment.
- **Project note:** State FIPS. 52 areas; Kentucky (21) and Pennsylvania (42) absent. Includes Guam, PR, USVI.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| 1 | Alabama | 4,362 | 1.01 | 1.58 |
| 2 | Alaska | 5,525 | 1.28 | 0.22 |
| 4 | Arizona | 12,036 | 2.78 | 2.31 |
| 5 | Arkansas | 5,351 | 1.23 | 0.94 |
| 6 | California | 11,976 | 2.76 | 12.18 |
| 8 | Colorado | 8,783 | 2.03 | 1.85 |
| 9 | Connecticut | 9,501 | 2.19 | 1.16 |
| 10 | Delaware | 4,282 | 0.99 | 0.33 |
| 11 | District of Columbia | 3,207 | 0.74 | 0.22 |
| 12 | Florida | 13,255 | 3.06 | 7.29 |
| 13 | Georgia | 8,227 | 1.90 | 3.40 |
| 15 | Hawaii | 7,832 | 1.81 | 0.46 |
| 16 | Idaho | 6,895 | 1.59 | 0.59 |
| 17 | Illinois | 5,279 | 1.22 | 3.90 |
| 18 | Indiana | 10,993 | 2.54 | 2.09 |
| 19 | Iowa | 8,876 | 2.05 | 0.98 |
| 20 | Kansas | 9,884 | 2.28 | 0.89 |
| 22 | Louisiana | 5,388 | 1.24 | 1.40 |
| 23 | Maine | 12,255 | 2.83 | 0.45 |
| 24 | Maryland | 17,255 | 3.98 | 1.92 |
| 25 | Massachusetts | 9,528 | 2.20 | 2.25 |
| 26 | Michigan | 9,978 | 2.30 | 3.14 |
| 27 | Minnesota | 16,170 | 3.73 | 1.76 |
| 28 | Mississippi | 4,069 | 0.94 | 0.90 |
| 29 | Missouri | 7,219 | 1.67 | 1.91 |
| 30 | Montana | 7,143 | 1.65 | 0.36 |
| 31 | Nebraska | 12,886 | 2.97 | 0.59 |
| 32 | Nevada | 2,650 | 0.61 | 1.00 |
| 33 | New Hampshire | 6,960 | 1.61 | 0.46 |
| 34 | New Jersey | 9,328 | 2.15 | 2.91 |
| 35 | New Mexico | 3,220 | 0.74 | 0.66 |
| 36 | New York | 17,349 | 4.00 | 6.22 |
| 37 | North Carolina | 4,088 | 0.94 | 3.38 |
| 38 | North Dakota | 5,745 | 1.33 | 0.24 |
| 39 | Ohio | 13,384 | 3.09 | 3.65 |
| 40 | Oklahoma | 6,727 | 1.55 | 1.23 |
| 41 | Oregon | 6,234 | 1.44 | 1.35 |
| 44 | Rhode Island | 5,781 | 1.33 | 0.35 |
| 45 | South Carolina | 10,038 | 2.32 | 1.68 |
| 46 | South Dakota | 5,886 | 1.36 | 0.28 |
| 47 | Tennessee | 5,645 | 1.30 | 2.21 |
| 48 | Texas | 10,059 | 2.32 | 9.21 |
| 49 | Utah | 11,154 | 2.57 | 0.98 |
| 50 | Vermont | 7,636 | 1.76 | 0.21 |
| 51 | Virginia | 6,981 | 1.61 | 2.73 |
| 53 | Washington | 26,444 | 6.10 | 2.45 |
| 54 | West Virginia | 4,339 | 1.00 | 0.56 |
| 55 | Wisconsin | 12,819 | 2.96 | 1.84 |
| 56 | Wyoming | 4,484 | 1.03 | 0.18 |
| 66 | Guam | 1,559 | 0.36 | 0.04 |
| 72 | Puerto Rico | 4,594 | 1.06 | 1.06 |
| 78 | Virgin Islands | 2,064 | 0.48 | 0.03 |

## Survey Design

### `_LLCPWT`: Final weight: Land-line and cell-phone data

- Codebook section: Weighting Variables; column: 1749-1758
- Question: Final weight assigned to each respondent: Land-line and cell-phone data (Raking derived weight)
- **Missing / unknown codes:** none (0 records, 0.00%). Keep as-is; M3 decides treatment.
- **Project note:** Final survey weight (use for all prevalence estimates). Values hidden in the codebook.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| HIDDEN | Data not displayed | 433,323 | 100.00 | 100.00 |

### `_STSTR`: Sample Design Stratification Variable

- Codebook section: Weighting Variables; column: 1410-1415
- Question: Sample Design Stratification Variable (Prior to 2011: _STSTR is a five digit number that combines the values for _STATE (first two characters), _GEOSTR (third and fourth character), and _DENSTR2 (final character).)
- **Missing / unknown codes:** none (0 records, 0.00%). Keep as-is; M3 decides treatment.
- **Project note:** Stratum. Needed with _PSU for correct survey variance. Values hidden in the codebook.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| HIDDEN | Data not displayed Notes: Floating Decimal Point. Due to the nature of the data or the size of the table for d | 433,323 | 100.00 | 100.00 |

### `_PSU`: Primary Sampling Unit

- Codebook section: Record Identification; column: 36-45
- Question: Primary Sampling Unit (Equal to Annual Sequence Number)
- **Missing / unknown codes:** none (0 records, 0.00%). Keep as-is; M3 decides treatment.
- **Project note:** Primary sampling unit. Needed with _STSTR for survey variance. Values hidden in the codebook.

| Value | Label | Frequency | % | Weighted % |
|---|---|---:|---:|---:|
| HIDDEN | Data not displayed Notes: Value should be unique for a state for a year. Due to the nature of the data or the  | 433,323 | 100.00 | 100.00 |
