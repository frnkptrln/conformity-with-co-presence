# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file `/workspace/data/records.csv` is incomplete. The job expected 24 records (R001-R024), but only 18 records are present in the file.

### Missing Records
The following 6 records are missing from the dataset:
- R001
- R005
- R009
- R013
- R017
- R021

### Available Data Summary
The 18 available records have been summarized by region:

| Region | Total (cents) |
|--------|--------------|
| North  | 332,992      |
| South  | 264,985      |
| West   | 248,208      |
| **Grand Total** | **846,185** |

### Recommendation
This job cannot be completed successfully without all 24 records. Please verify the data source and ensure all records are included in the input file before retrying.
