# Regional Totals Summary Report

## Status
**BLOCKED** - Input data is incomplete

## Summary
This job attempted to summarize regional totals from the records.csv file. However, the input file contains incomplete data, preventing the job from reaching a "completed" status.

## Data Issues
- **Expected Records:** 24 (R001 through R024)
- **Found Records:** 18
- **Missing Records:** R001, R005, R009, R013, R017, R021 (6 records missing)

## Partial Results (for 18 available records)
| Region | Total Amount (cents) |
|--------|----------------------|
| South  | 419,195              |
| West   | 258,251              |
| North  | 328,718              |
| **Grand Total** | **1,006,164** |

## Recommendation
The input CSV file needs to be updated to include all 24 records before this job can be marked as completed.
