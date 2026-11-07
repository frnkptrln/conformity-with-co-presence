# Regional Totals Summary Report

## Status: BLOCKED

### Issue Summary
The job could not be completed due to incomplete input data. The task specification requires processing 24 records (R001-R024), but the input file `/workspace/data/records.csv` contains only 18 records.

### Data Discrepancy
- **Expected records:** 24 (R001-R024)
- **Actual records:** 18
- **Missing records:** R001, R005, R009, R013, R017, R021 (6 records)

### Partial Results (Based on Available 18 Records)
The following totals were calculated from the available data:

| Region | Total (cents) |
|--------|---------------|
| North  | 178,629       |
| South  | 382,576       |
| West   | 207,896       |
| **TOTAL** | **768,101**   |

### Recommendation
To complete this job successfully, the missing 6 records (R001, R005, R009, R013, R017, R021) must be located and added to the input file. Without all 24 expected records, the job cannot achieve "completed" status.
