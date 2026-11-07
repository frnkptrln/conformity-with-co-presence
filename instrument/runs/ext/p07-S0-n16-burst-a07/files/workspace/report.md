# Regional Totals Summary Report

## Status
**BLOCKED** - Data integrity issue detected

## Summary
The task requested analysis of 24 records (R001-R024), but the input file `/workspace/data/records.csv` contains only 18 records. 

## Analysis of Available Data

### Records Processed
Successfully processed 18 records from the CSV file.

### Regional Totals (18 records)
- **North**: 380,102 cents ($3,801.02)
- **South**: 257,703 cents ($2,577.03)
- **West**: 324,174 cents ($3,241.74)

**Grand Total**: 961,979 cents ($9,619.79)

### Missing Records
The following 6 records referenced in the task are not present in the data file:
- R001, R005, R009, R013, R017, R021

## Recommendation
The missing records should be verified and provided before this job can be marked as complete. The totals shown are accurate for the 18 available records but do not represent the full expected dataset of 24 records.
