# Regional Totals Summary Report

## Status: BLOCKED - Data Integrity Issue

### Issue
The input file `/workspace/data/records.csv` contains an incomplete dataset with only 18 records instead of the expected 24 records (R001-R024).

### Missing Records
The following records are missing from the data:
- R001, R005, R009, R013, R017, R021 (6 records total)

### Processed Records
The 18 available records (R002-R024, excluding the above) have been summarized as follows:

| Region | Total Amount (cents) |
|--------|----------------------|
| South  | 423,723              |
| West   | 265,276              |
| North  | 342,270              |
| **TOTAL** | **1,031,269**      |

### Recommendation
This job requires completion with all 24 records to achieve the reference match required for scoring. The data should be verified and the missing records located before reprocessing.
