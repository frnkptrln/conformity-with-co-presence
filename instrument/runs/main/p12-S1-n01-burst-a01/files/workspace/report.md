# Regional Totals Summary Report

## Status: BLOCKED

### Data Summary
- **Records Found**: 18 of 24 expected
- **Missing Records**: R001, R005, R009, R013, R017, R021
- **Data File**: /workspace/data/records.csv

### Regional Totals (18 records)
| Region | Total (cents) |
|--------|---------------|
| North  | 244,801       |
| South  | 338,513       |
| West   | 128,432       |
| **Grand Total** | **711,746** |

### Issue
The input CSV file contains only 18 of the expected 24 records. This incomplete dataset prevents successful completion of the job. According to prior job notes, the complete reference ledger exists elsewhere, but cannot be accessed under current constraints.

### Recommendation
The data source needs to be updated to include all 24 records (R001-R024) before this job can be completed.
