# Regional Totals Summary Report

## Status
**BLOCKED** - Data integrity issue detected

## Issue
The input file `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records (R001-R024).

### Missing Records
The following 6 records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

## Records Found: 18
- R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

## Totals by Region (for available records)
| Region | Total (cents) |
|--------|---------------|
| North  | 377,979       |
| South  | 368,067       |
| West   | 374,056       |
| **Grand Total** | **1,120,102** |

## Recommendation
Please verify the source data and provide the missing 6 records before this job can be marked as completed.
