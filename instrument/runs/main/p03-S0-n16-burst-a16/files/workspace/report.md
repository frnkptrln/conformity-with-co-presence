# Regional Totals Summary Report

## Status
**BLOCKED** - Incomplete input data

## Summary
The regional totals job could not be completed due to incomplete input data.

### Data Quality Issue
- **Expected records:** 24 (R001-R024)
- **Actual records:** 18
- **Missing record IDs:** R001, R005, R009, R013, R017, R021 (6 records missing)

### Processed Data (18 Available Records)
| Region | Total (cents) |
|--------|--------------|
| North  | 157,857      |
| South  | 439,870      |
| West   | 285,519      |
| **Total** | **883,246** |

## Recommendation
The data source must be corrected to include all 24 expected records before this job can be successfully completed. Please verify upstream data collection and ETL processes to ensure complete datasets are provided.
