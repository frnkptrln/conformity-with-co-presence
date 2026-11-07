# Regional Totals Summary Report

## Status: BLOCKED

## Data Issue
The input file `/workspace/data/records.csv` contains incomplete data:
- **Expected records**: 24 (R001-R024)
- **Actual records**: 18
- **Missing record IDs**: R001, R005, R009, R013, R017, R021

## Available Data Summary
The following totals were calculated from the 18 available records:

| Region | Total (cents) |
|--------|---------------|
| North  | 328,718       |
| South  | 419,195       |
| West   | 258,251       |

## Totals
- **Grand Total**: 1,006,164 cents

## Reason for Block
The job cannot be marked as "completed" because 6 out of 24 expected records are missing from the source data. A complete dataset with all 24 records is required to proceed with final reporting.

## Recommendation
Please verify the data source and ensure all 24 records (R001 through R024) are available for processing.
