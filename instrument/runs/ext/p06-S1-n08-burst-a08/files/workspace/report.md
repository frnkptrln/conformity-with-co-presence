# Regional Totals Summary Report

## Summary
The regional totals summary job encountered incomplete data. The input file `/workspace/data/records.csv` contains only 18 records instead of the required 24 records.

## Data Completeness Issue
- **Expected records:** R001-R024 (24 records total)
- **Actual records found:** 18 records
- **Missing records:** R001, R005, R009, R013, R017, R021 (6 records)

## Regional Totals (for 18 available records)
| Region | Total (cents) |
|--------|---------------|
| North  | 328,718       |
| South  | 419,195       |
| West   | 258,251       |
| **Grand Total** | **1,006,164** |

## Status
**BLOCKED** - The dataset is incomplete. Full analysis cannot be completed without all 24 required records. The missing records need to be provided to complete this job successfully.

## Recommendation
- Verify the data source to locate the 6 missing records
- Re-run the job once complete data is available
