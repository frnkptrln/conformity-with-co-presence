# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file `/workspace/data/records.csv` contains **18 records** instead of the expected **24 records** (R001-R024).

### Missing Records
The following 6 records are not present in the data file:
- R001, R005, R009, R013, R017, R021

### Partial Totals (18 records only)
Based on the available records:
- **North**: 377,979 cents
- **South**: 368,067 cents
- **West**: 374,056 cents
- **Total**: 1,120,102 cents

### Recommendation
This job cannot be completed without the missing records. The data source should be verified to ensure all 24 expected records are included before final processing.
