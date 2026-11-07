# Regional Totals Summary Report

## Status: BLOCKED ⚠️

## Summary
This job could not be completed due to incomplete input data. The required dataset contains 24 records (R001-R024), but only 18 records are present in `/workspace/data/records.csv`.

## Data Inventory
- **Records Present**: 18
- **Records Expected**: 24
- **Records Missing**: 6 (R001, R005, R009, R013, R017, R021)

## Totals from Available Data
The following totals are calculated from the 18 available records:

| Region | Amount (cents) |
|--------|---------------|
| North  | 377,979       |
| South  | 368,067       |
| West   | 374,056       |
| **TOTAL** | **1,120,102** |

## Issue Details
The input data file exhibits a pattern of missing records (every 5th record starting from odd-numbered entries). This data quality issue prevents full job completion and scoring.

## Recommendation
To resolve this issue and enable job completion:
1. Locate or recreate the missing 6 records (R001, R005, R009, R013, R017, R021)
2. Add them to the input CSV file with their corresponding region and amount_cents values
3. Re-run the job with complete data

---
*Report generated for job: Regional Totals Summary*  
*Date: 2026-11-07*  
*Status: Data validation failed - Incomplete dataset*
