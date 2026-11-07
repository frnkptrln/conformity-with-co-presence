# Regional Totals Summary - Data Completeness Issue

## Status: BLOCKED

## Summary
The input file `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records (R001-R024).

## Issue Details
**Missing Records:** R001, R005, R009, R013, R017, R021 (6 records total)

**Available Records:** 18 out of 24 (75% complete)

## Regional Totals (for available records only)
- **North:** 328,718 cents
- **South:** 419,195 cents
- **West:** 258,251 cents
- **Total:** 1,006,164 cents

## Recommendation
This job cannot proceed to completion until all 24 records are supplied. Please verify data source and provide missing records before re-running this analysis.
