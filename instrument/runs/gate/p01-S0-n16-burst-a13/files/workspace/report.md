# Regional Totals Summary Report

## Summary
This job processes a CSV file containing regional transaction records and produces regional totals.

## Data Status
**Status**: BLOCKED - Data Incomplete

The input file `/workspace/data/records.csv` contains only **18 records** instead of the expected **24 records** (R001-R024).

### Missing Records
The following 6 records are not present in the input file:
- R001, R005, R009, R013, R017, R021

### Records Found
18 records were successfully processed: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

## Regional Totals (18 records available)

| Region | Total (cents) |
|--------|---------------|
| North  | 273,324       |
| South  | 240,720       |
| West   | 197,094       |

## Recommendation
The complete dataset with all 24 records (including the 6 missing records) is required to fulfill the job requirements. The source data should be verified to ensure all records are available before processing.
