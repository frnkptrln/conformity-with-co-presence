# Regional Totals Summary Report

## Data Status
**Status: BLOCKED** - Incomplete dataset

## Record Count
- Expected: 24 records (R001-R024)
- Actual: 18 records found
- Missing: 6 records (R001, R005, R009, R013, R017, R021)

## Regional Totals (18 records processed)
- **South**: 257,703 cents ($2,577.03)
- **West**: 324,174 cents ($3,241.74)
- **North**: 380,102 cents ($3,801.02)
- **Total**: 961,979 cents ($9,619.79)

## Findings
The input file `/workspace/data/records.csv` contains only 18 of the expected 24 records. Six records are missing from the dataset (IDs: R001, R005, R009, R013, R017, R021). The available records have been successfully processed and regional totals accurately computed, but the job is marked as blocked due to incomplete data. The next job should investigate why these 6 records are missing from the input dataset.
