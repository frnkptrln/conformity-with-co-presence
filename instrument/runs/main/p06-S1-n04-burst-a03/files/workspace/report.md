# Regional Totals Summary Report

## Job Status: BLOCKED

### Issue
The input file `/workspace/data/records.csv` contains only 18 records instead of the required 24 records for complete processing.

### Records Available
- **Total records in input file:** 18
- **Missing records:** R001, R005, R009, R013, R017, R021

### Partial Totals (18 records only)
| Region | Total (cents) |
|--------|---------------|
| South  | 419,195       |
| West   | 258,251       |
| North  | 328,718       |
| **Grand Total** | **1,006,164** |

### Note
A previous job (0117) indicated that the complete ledger with all 24 records exists in a reference file, but access to that source is restricted by system constraints. The current input file remains incomplete.

### Recommendation
Verify that the complete dataset has been provided in `/workspace/data/records.csv` before re-running this job.
