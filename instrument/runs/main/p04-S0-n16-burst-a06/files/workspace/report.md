# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input dataset is incomplete. The file `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records (R001-R024).

### Missing Records
The following 6 records are absent from the dataset:
- R001, R005, R009, R013, R017, R021

### Available Data Summary
Despite the incomplete dataset, here are the totals calculated from the 18 available records:

| Region | Total (cents) |
|--------|---------------|
| North  | 254,156       |
| South  | 270,675       |
| West   | 213,798       |
| **Total** | **738,629** |

### Recommendation
To complete this job successfully, the source data must be verified and all 24 records provided. The missing records should be investigated to ensure they exist in the original data source and are included in the input file.

---

**Report generated**: 2026-11-07  
**Record count**: 18 of 24  
**Status**: Cannot proceed to completion without full dataset
