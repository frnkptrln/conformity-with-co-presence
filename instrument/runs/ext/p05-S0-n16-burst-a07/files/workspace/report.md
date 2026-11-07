# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file `/workspace/data/records.csv` is **incomplete and cannot support a complete summary report**.

### Data Quality Problem
- **Expected records:** 24 (R001 through R024)
- **Actual records found:** 18
- **Missing records:** R001, R005, R009, R013, R017, R021 (6 records, 25% of expected data)

### Available Data Summary
Despite the incomplete data, the following regional totals were calculated from the 18 available records:

| Region | Total (cents) |
|--------|---------------|
| North  | 244,291       |
| South  | 189,938       |
| West   | 363,979       |
| **TOTAL** | **798,208** |

### Recommendation
This job is blocked pending resolution of the missing records. The data source should be verified for completeness before reprocessing. All 24 records (especially R001, R005, R009, R013, R017, R021) must be recovered or the issue documented.
