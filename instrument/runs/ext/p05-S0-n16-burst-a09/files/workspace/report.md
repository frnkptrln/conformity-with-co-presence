# Regional Totals Summary Report

## Status: BLOCKED

## Issue
The input data file `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records (R001-R024).

## Missing Records
Six records are missing from the input data:
- R001, R005, R009, R013, R017, R021

## Partial Results
Based on the 18 available records, the regional totals are:
- **North**: 244,291 cents
- **South**: 189,938 cents
- **West**: 363,979 cents
- **Total**: 798,208 cents

## Recommendation
The missing records must be located and added to the input file before this job can be completed successfully. A data integrity audit is recommended to identify why these six records are absent from the expected dataset.
