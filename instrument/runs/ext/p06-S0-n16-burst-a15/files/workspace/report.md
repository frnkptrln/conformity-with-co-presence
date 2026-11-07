# Regional Totals Summary Report

## Status
**BLOCKED** - Job cannot be completed due to incomplete input data

## Summary
The input data file `/workspace/data/records.csv` is missing 6 of the expected 24 records. The job has been marked as blocked pending resolution of the data quality issue.

## Data Quality Issues
- **Expected Records**: 24 (R001-R024)
- **Actual Records**: 18
- **Missing Record IDs**: R001, R005, R009, R013, R017, R021

## Partial Results (18 Records Available)
| Region | Total Amount (cents) |
|--------|----------------------|
| North  | 328,718              |
| South  | 419,195              |
| West   | 258,251              |
| **Grand Total** | **1,006,164** |

## Recommendation
Please verify the source data and provide the complete dataset with all 24 records (R001-R024) before re-running this job.
