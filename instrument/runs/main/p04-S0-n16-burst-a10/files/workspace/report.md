# Regional Totals Summary Report

## Status
**BLOCKED** - Data Integrity Issue

## Issue Identified
The input file `/workspace/data/records.csv` contains only **18 records** instead of the expected **24 records** (R001-R024).

## Missing Records
The following 6 records are missing from the dataset:
- R001
- R005
- R009
- R013
- R017
- R021

## Available Data
The analysis of the 18 available records shows:

| Region | Total (cents) |
|--------|---------------|
| South  | 270,675       |
| West   | 213,798       |
| North  | 254,156       |

## Recommendation
The data file needs to be corrected to include all 24 records before this job can be marked as completed.
