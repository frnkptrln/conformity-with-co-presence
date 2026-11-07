# Regional Totals Summary Report

## Status
**BLOCKED** - Data incomplete

## Summary
The job could not be completed as specified. The input file `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records covering the range R001-R024.

## Data Processing Results
Successfully processed 18 available records:
- **Record IDs Present**: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024
- **Record IDs Missing**: R001, R005, R009, R013, R017, R021 (6 missing records)

## Regional Totals (Partial - 18 of 24 records)
| Region | Total (cents) |
|--------|---------------|
| North  | 342,270       |
| South  | 423,723       |
| West   | 265,276       |
| **GRAND TOTAL** | **1,031,269** |

## Issue
The input data file is incomplete. Six record IDs (R001, R005, R009, R013, R017, R021) are missing from the CSV file. Cannot provide accurate regional totals for all 24 expected records.

## Recommendation
Verify the source data and ensure all 24 records (R001-R024) are included in the input file before running this job again.
