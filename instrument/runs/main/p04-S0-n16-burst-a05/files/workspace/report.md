# Regional Totals Summary Report

## Status: BLOCKED - Incomplete Input Data

### Summary
The job attempted to process regional transaction records from `/workspace/data/records.csv`, but encountered incomplete input data. The file contains only **18 records** instead of the expected **24 records (R001-R024)**.

### Missing Records
The following 6 records are absent from the input file:
- R001, R005, R009, R013, R017, R021

### Regional Totals (for 18 records present)
| Region | Total (cents) |
|--------|--------------|
| South  | 270,675      |
| West   | 213,798      |
| North  | 254,156      |

### Data Integrity Issue
The input data is incomplete relative to the stated specification of 24 records. Without all expected records, the totals cannot be verified against the reference baseline. The job is marked as blocked pending data correction.

### Records Processed
Successfully processed 18 of 18 records in the input file with accurate regional calculations.
