# Regional Totals Summary Report

## Status
**BLOCKED** - Data quality issue detected

## Summary
The analysis of `/workspace/data/records.csv` identified a significant data completeness problem that prevents successful completion of this job.

### Data Quality Issue
- **Expected Records**: 24 (R001-R024)
- **Records Found**: 18
- **Missing Records**: R001, R005, R009, R013, R017, R021 (6 records missing)

### Partial Results (18 Records Only)
The following totals were calculated from the available records:

| Region | Total (cents) |
|--------|---------------|
| North  | 342,270       |
| South  | 423,723       |
| West   | 265,276       |
| **TOTAL** | **1,031,269** |

### Records Processed
R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Recommendation
The input data file appears to be incomplete or corrupted. To complete this job successfully, please:
1. Verify the completeness of the source data
2. Locate and include the missing 6 records (R001, R005, R009, R013, R017, R021)
3. Re-run the analysis with the complete dataset
