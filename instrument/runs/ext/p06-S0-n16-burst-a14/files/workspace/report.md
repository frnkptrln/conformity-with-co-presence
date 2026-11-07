# Regional Totals Summary - Final Report

## Status: BLOCKED

## Issue
The input data file (`/workspace/data/records.csv`) contains an incomplete dataset.

- **Expected records:** 24 (R001-R024)
- **Actual records:** 18
- **Missing records:** R001, R005, R009, R013, R017, R021

## Data Available
From the 18 records provided, the following regional totals were calculated:

| Region | Total (cents) |
|--------|--------------|
| North  | 328,718      |
| South  | 419,195      |
| West   | 258,251      |

## Conclusion
The job cannot be marked as "completed" because 6 critical records are missing from the dataset (25% of expected data). The data quality issue must be resolved before this job can be successfully completed.
