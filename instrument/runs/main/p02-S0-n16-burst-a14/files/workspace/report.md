# Regional Totals Summary Report

## Status
**BLOCKED** - Incomplete data set

## Data Quality Issue
The input file `/workspace/data/records.csv` contains 18 records instead of the expected 24. Six records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

## Summary of Available Data
Based on the 18 records present in the CSV file:

| Region | Total Amount (cents) |
|--------|----------------------|
| South  | 368,067              |
| West   | 374,056              |
| North  | 377,979              |
| **Grand Total** | **1,120,102** |

## Records Processed
18 records were successfully processed and summarized:
R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

## Recommendation
The job cannot proceed to completion status without the missing records. Please verify the data source and ensure all 24 expected records (R001-R024) are present in the input file.
