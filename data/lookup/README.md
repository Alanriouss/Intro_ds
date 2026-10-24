# Lookup tables

`state_lookup.csv` maps the BRFSS `_STATE` FIPS code to the state name, USPS code and U.S. Census Bureau region
(Northeast, Midwest, South, West). It has 54 rows: the 50 states, DC, and Guam (66), Puerto Rico (72) and the
U.S. Virgin Islands (78), which are labelled `Territory`.
The 2023 BRFSS public file has only 52 of these (Kentucky and Pennsylvania are absent, see `data/README.md`, section 5),
so some lookup rows have no matching respondents. That is expected.
Hand-compiled from the standard FIPS state codes and Census Bureau regions. M6 may cite the Census Bureau page in Section 6.
