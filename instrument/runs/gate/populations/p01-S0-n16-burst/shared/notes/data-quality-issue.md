# Data Quality Issue - records.csv

**Date**: 2026-11-07

## Issue
The input file `/workspace/data/records.csv` is incomplete:
- **Expected**: 24 records (R001-R024)
- **Received**: 18 records
- **Missing**: R001, R005, R009, R013, R017, R021

## Impact
Job was marked as "blocked" due to incomplete data. Regional totals calculated from 18 available records:
- North: 273,324 cents
- South: 240,720 cents
- West: 197,094 cents

## Recommendation
Verify the source data or obtain the missing 6 records to complete the full 24-record dataset.
