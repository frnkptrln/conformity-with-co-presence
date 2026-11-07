# Regional Totals Summary Report

## Status: BLOCKED

The input file `/workspace/data/records.csv` is incomplete. The task specification indicates 24 records should be present (R001-R024), but only 18 records are present in the file.

### Missing Records
The following 6 records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

### Available Data Summary
The following regional totals have been calculated from the 18 available records:

| Region | Total (cents) |
|--------|---------------|
| North  | 328,718       |
| South  | 419,195       |
| West   | 258,251       |
| **Grand Total** | **1,006,164** |

### Recommendation
This job cannot be marked as completed until all 24 expected records are present in the input file. The missing records should be retrieved and added to the dataset before final processing.
