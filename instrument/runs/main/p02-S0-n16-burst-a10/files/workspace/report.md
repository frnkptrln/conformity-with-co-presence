# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input CSV file `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records (R001-R024).

### Missing Records
The following 6 records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

### Available Data Summary
The 18 available records have been processed and show the following totals by region:

| Region | Total (cents) |
|--------|---------------|
| North  | 377,979       |
| South  | 368,067       |
| West   | 374,056       |
| **Total** | **1,120,102** |

### Recommendation
The data file appears to be incomplete or corrupted. Please verify the source data and ensure all 24 records (R001-R024) are present in the input file before reprocessing.
