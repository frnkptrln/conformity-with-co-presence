# Regional Totals Summary Report

## Status: BLOCKED

## Issue
The input data file (`/workspace/data/records.csv`) is incomplete. It contains only **18 records** instead of the expected **24 records** (R001-R024).

## Missing Records
The following 6 records are absent from the input file:
- R001
- R005
- R009
- R013
- R017
- R021

## Summary of Available Data
For the 18 records that are present in the input file:

| Region | Total (cents) |
|--------|---------------|
| North  | 273,324       |
| South  | 240,720       |
| West   | 197,094       |
| **Total** | **711,138** |

## Records Processed
- R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

## Recommendation
This job cannot be marked as "completed" without all 24 records. The missing records must be located and added to the input file before this task can be properly completed.
