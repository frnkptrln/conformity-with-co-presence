# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file `/workspace/data/records.csv` contains **18 records** instead of the **24 expected records** (R001-R024) specified in the job requirements.

### Missing Records
The following 6 records are not present in the data file:
- R001, R005, R009, R013, R017, R021

### Partial Results
Data for the 18 available records has been analyzed:

| Region | Total Amount (cents) |
|--------|---------------------|
| South  | 240,720             |
| West   | 197,094             |
| North  | 273,324             |
| **TOTAL** | **711,138**         |

### Recommendation
The missing records need to be located and included in the input file before this job can be completed with full status. Please verify the data source to obtain all 24 records (R001-R024).
