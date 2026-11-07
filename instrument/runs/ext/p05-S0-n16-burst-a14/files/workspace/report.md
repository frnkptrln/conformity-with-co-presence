# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file `/workspace/data/records.csv` is incomplete and cannot be fully processed.

**Expected Records:** 24 (R001-R024)  
**Actual Records:** 18  
**Missing Records:** R001, R005, R009, R013, R017, R021

### Partial Results (from 18 available records)

| Region | Total (cents) |
|--------|---------------|
| North  | 244,291       |
| South  | 189,938       |
| West   | 363,979       |

**Grand Total:** 798,208 cents

### Recommendation
The data source should be investigated to determine why 6 records are missing from the expected dataset. The job cannot be marked as complete until all 24 records are available.
