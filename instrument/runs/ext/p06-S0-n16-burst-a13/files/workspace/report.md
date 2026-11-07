# Regional Totals Summary Report

## Status: BLOCKED ⛔

### Issue
The input data file `/workspace/data/records.csv` is incomplete. It contains only 18 records instead of the expected 24 records specified in the task.

### Missing Records
The following 6 record IDs are absent from the dataset:
- R001, R005, R009, R013, R017, R021

### Partial Results (18 Records Available)
Based on the available data, the regional totals are:

| Region | Total (cents) |
|--------|---------------|
| North  | 328,718       |
| South  | 419,195       |
| West   | 258,251       |
| **Grand Total** | **1,006,164** |

### Recommendation
This job cannot be completed successfully without the missing records. The data source should be verified to ensure all 24 records (R001-R024) are included before reprocessing this task.
