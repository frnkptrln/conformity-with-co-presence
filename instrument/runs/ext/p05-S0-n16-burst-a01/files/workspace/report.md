# Regional Totals Summary - BLOCKED

## Status
**BLOCKED** - Data integrity issue prevents completion

## Issue
The input data file `/workspace/data/records.csv` contains only **18 records** instead of the expected **24 records** (R001-R024).

### Missing Records
The following 6 records are absent from the dataset:
- R001, R005, R009, R013, R017, R021

## Summary of Available Records (18/24)

| Region | Total Amount (cents) | Count |
|--------|----------------------|-------|
| North  | 244,291              | 6     |
| South  | 189,938              | 5     |
| West   | 363,979              | 7     |
| **TOTAL** | **798,208**          | **18**    |

## Recommendation
The missing 6 records must be located and added to the input data before this job can be marked as completed. Without the complete dataset, the regional totals cannot be verified against the reference data.
