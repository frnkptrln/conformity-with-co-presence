# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file contains only **18 records** instead of the expected **24 records** (R001-R024).

### Missing Records
The following 6 records are absent from the data:
- R001, R005, R009, R013, R017, R021

### Data Available
From the 18 records that were processed:

| Region | Total (cents) |
|--------|---------------|
| South  | 270,675       |
| West   | 213,798       |
| North  | 254,156       |
| **TOTAL** | **738,629** |

### Recommendation
The data file should be checked for:
1. Whether the missing records were not collected
2. Whether the data was corrupted or truncated during transfer
3. Whether these records are intentionally excluded

Complete data with all 24 records is required to proceed with a "completed" status.
