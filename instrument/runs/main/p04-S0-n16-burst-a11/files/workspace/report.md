# Regional Totals Summary Report

## Status
**BLOCKED** - Data integrity issue detected

## Issue Description
The input dataset in `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records specified in the task requirements. The following records are missing:
- R001, R005, R009, R013, R017, R021

## Available Data Summary
Despite the incomplete dataset, the available 18 records have been processed and summarized:

| Region | Total (cents) |
|--------|---------------|
| North  | 254,156       |
| South  | 270,675       |
| West   | 213,798       |
| **Total** | **738,629** |

## Recommendation
The job cannot be marked as "completed" because the source data is incomplete. To resolve this issue:
1. Verify and provide all 24 records (R001-R024) in the input CSV
2. Ensure data integrity before reprocessing
3. Confirm that the missing records are not intentionally excluded

## Records Processed
18 records successfully analyzed: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024
