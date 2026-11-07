# Regional Totals Summary Report

## Status: BLOCKED

### Data Quality Issue
The input file `/workspace/data/records.csv` contains **18 records** instead of the expected 24 records (R001-R024 as specified in the task requirements).

### Missing Records
The following 6 record IDs are absent from the dataset:
- R001, R005, R009, R013, R017, R021

### Partial Results (18 records available)
For the 18 records that are present, the regional totals are:
- **South**: 423,723 cents
- **West**: 265,276 cents
- **North**: 342,270 cents
- **Grand Total**: 1,031,269 cents

### Recommendation
The task cannot be completed as specified without all 24 records. Data validation or recovery is needed to identify why 6 records are missing from the input file before final processing can proceed.
