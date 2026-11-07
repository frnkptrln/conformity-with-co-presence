# Regional Totals Summary Report

## Status: BLOCKED

### Summary
The job was unable to complete as specified due to incomplete input data. The records.csv file contains only 18 records instead of the expected 24 records (R001-R024).

### Data Found
- **Total Records Processed:** 18 of 24 expected
- **Missing Records:** R001, R005, R009, R013, R017, R021 (6 records)

### Regional Totals (for 18 available records)
| Region | Total (cents) |
|--------|---------------|
| South  | 270,675       |
| West   | 213,798       |
| North  | 254,156       |
| **TOTAL** | **738,629** |

### Recommendation
The input data file is missing 25% of the expected records. To complete this job successfully, all 24 records (R001-R024) must be present in the input file. The job cannot proceed to "completed" status without the missing records.
