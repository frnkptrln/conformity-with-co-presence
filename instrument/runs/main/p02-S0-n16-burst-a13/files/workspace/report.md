# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input file `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records (R001-R024).

### Missing Records
- R001
- R005
- R009
- R013
- R017
- R021

### Data Available (18 records)
The following totals were calculated for the 18 available records:

| Region | Total Amount (cents) |
|--------|----------------------|
| South  | 368,067              |
| West   | 374,056              |
| North  | 377,979              |

### Summary
Due to the missing 6 records, this job cannot be completed successfully. Approximately 25% of the expected data is missing from the input file. The calculations shown above are valid only for the records that are present.

### Recommendation
Please verify the source data and ensure all 24 records (R001-R024) are included in the input file before attempting to complete this job.
