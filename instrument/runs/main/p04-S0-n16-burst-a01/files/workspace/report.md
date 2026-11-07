# Regional Totals Summary Report

## Status
**BLOCKED** - Data Integrity Issue

## Summary
The input file `/workspace/data/records.csv` was expected to contain 24 records (R001-R024) but only contains 18 records.

## Missing Records
The following 6 records are missing from the dataset:
- R001
- R005
- R009
- R013
- R017
- R021

## Available Data Summary
Of the 18 records present in the file:

| Region | Total (cents) |
|--------|---------------|
| North  | 254,156       |
| South  | 270,675       |
| West   | 213,798       |
| **TOTAL** | **738,629** |

## Recommendation
Please verify the source data and provide the complete dataset with all 24 records before this job can be marked as completed.
