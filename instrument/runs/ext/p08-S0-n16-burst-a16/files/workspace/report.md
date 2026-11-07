# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input file `/workspace/data/records.csv` is incomplete and cannot be processed as requested.

**Expected:** 24 records (R001-R024)  
**Actual:** 18 records found  
**Missing:** 6 records (R001, R005, R009, R013, R017, R021)

### Available Data
The 18 available records were successfully processed with the following regional totals:

| Region | Amount (cents) |
|--------|-----------------|
| North  | 342,270         |
| South  | 423,723         |
| West   | 265,276         |
| **Total** | **1,031,269** |

### Recommendation
The data source must be corrected to include all 24 required records. Once the missing records are added to the input file, this job can be completed successfully.
