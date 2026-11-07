# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file `/workspace/data/records.csv` contains only 18 records, but the task specification indicates 24 records (R001-R024) should be present.

### Missing Records
The following 6 records are absent from the dataset:
- R001
- R005
- R009
- R013
- R017
- R021

### Data Found (18 records)
The available records have been analyzed with the following regional totals:

| Region | Total (cents) |
|--------|---------------|
| South  | 240,720       |
| North  | 273,324       |
| West   | 197,094       |

**Grand Total: 711,138 cents**

### Recommendation
The job cannot be completed until all 24 expected records are provided in the input file. Please verify the data source and ensure all records are present before processing can resume.
