# Regional Totals Summary Report

## Status: BLOCKED

## Issue
The input file at `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records (R001-R024).

### Missing Records
The following record IDs are absent from the input file:
- R001, R005, R009, R013, R017, R021

## Available Data Summary
Analysis of the 18 available records:

| Region | Total Amount (cents) | Total Amount (dollars) |
|--------|---------------------|------------------------|
| South  | 189,938              | $1,899.38              |
| West   | 363,979              | $3,639.79              |
| North  | 244,291              | $2,442.91              |
| **Total** | **798,208**        | **$7,982.08**          |

## Records Processed
South: R002, R008, R011, R014, R020, R023
West: R003, R006, R012, R015, R018, R024
North: R004, R007, R010, R016, R019, R022

## Recommendation
The job cannot be completed as specified without all 24 records. Please verify the input data source and provide the missing records before final processing.
