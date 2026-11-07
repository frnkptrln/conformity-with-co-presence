# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input file `/workspace/data/records.csv` contains only **18 records** instead of the expected **24 records**. Six records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

### Data Found
The 18 available records were successfully processed with the following regional totals:

| Region | Total (cents) |
|--------|---------------|
| South  | 439,870       |
| West   | 285,519       |
| North  | 157,857       |

**Total across all regions: 883,246 cents**

### Recommendation
To complete this job, all 24 records (R001-R024) must be provided in the input CSV file. Please check the data source and ensure all records are present before resubmitting.
