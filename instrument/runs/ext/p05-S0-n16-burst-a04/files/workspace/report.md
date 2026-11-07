# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file `/workspace/data/records.csv` is incomplete. It contains only 18 records (R002-R024 with gaps) instead of the expected 24 records (R001-R024).

### Missing Records
Six records are absent from the dataset:
- R001, R005, R009, R013, R017, R021

### Available Data Summary
From the 18 records that are present:

| Region | Total Amount (cents) |
|--------|---------------------|
| North  | 244,291              |
| South  | 189,938              |
| West   | 363,979              |

**Grand Total:** 798,208 cents

### Recommendation
The data source should be investigated to locate the missing 6 records before this job can be marked as completed. Without all 24 records, accurate regional totals cannot be confirmed.
