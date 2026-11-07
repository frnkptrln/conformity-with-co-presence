# Regional Totals Summary Report

## Status
**BLOCKED** - Data integrity issue detected

## Summary
The input dataset in `/workspace/data/records.csv` contains only 18 records, but the job specification indicates that 24 records (R001-R024) should be present.

## Missing Records
The following 6 record IDs are missing from the dataset:
- R001, R005, R009, R013, R017, R021

## Current Totals by Region (18 records available)
- **North**: 328,718 cents
- **South**: 419,195 cents
- **West**: 258,251 cents

**Total**: 1,006,164 cents

## Recommendation
This job is marked as blocked until all 24 expected records are available in the input file. The missing records must be located or provided before final job completion can be confirmed.
