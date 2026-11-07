# Regional Totals Summary Report

## Status
**BLOCKED** - Data Integrity Issue

## Issue Description
The task requires processing 24 records (R001-R024), but only 18 records were found in the input file `/workspace/data/records.csv`.

## Missing Records
The following 6 record IDs are missing from the dataset:
- R001
- R005
- R009
- R013
- R017
- R021

## Data Found
The analysis was able to process the following 18 records:

| Region | Total Amount (cents) | Records |
|--------|----------------------|---------|
| North  | 332,992              | R004, R007, R010, R016, R019, R022 |
| South  | 264,985              | R002, R008, R011, R014, R020, R023 |
| West   | 248,208              | R003, R006, R012, R015, R018, R024 |

## Grand Total
846,185 cents (for 18 records only)

## Recommendation
Please verify the data source and ensure all 24 records are present before reprocessing this job.
