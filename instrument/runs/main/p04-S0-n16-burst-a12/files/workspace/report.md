# Regional Totals Summary Report

## Status: BLOCKED

### Data Integrity Issue

The input CSV file (`/workspace/data/records.csv`) contains only **18 records** instead of the expected **24 records** specified in the task requirements.

### Missing Records

The following 6 records are missing from the dataset:
- R001
- R005
- R009
- R013
- R017
- R021

### Available Data Summary

The 18 available records have been processed with the following regional totals:

| Region | Amount (cents) |
|--------|----------------|
| North  | 254,156        |
| South  | 270,675        |
| West   | 213,798        |
| **Total** | **738,629**  |

### Recommendation

This job is marked as **BLOCKED** because the source data is incomplete. To complete this task successfully, the missing 6 records need to be added to the input CSV file. The data integrity issue must be resolved at the source level before this job can be completed as specified.

**Note:** This is a recurring issue - the previous attempt identified the same missing records.
