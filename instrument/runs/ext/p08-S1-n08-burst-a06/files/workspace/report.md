# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file at `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records. The following record IDs are missing from the input file:
- R001, R005, R009, R013, R017, R021

### Data Summary (18 Available Records)
Based on the records present in the input file:

| Region | Total (cents) |
|--------|---------------|
| South  | 423,723       |
| West   | 265,276       |
| North  | 342,270       |

**Total Records Processed:** 18 of 24 expected

### Conclusion
The job cannot be completed as specified because the input file is incomplete. All 24 records (R001-R024) are required to generate accurate regional totals. The missing 6 records (25% of the dataset) represent a significant data quality issue that prevents successful job completion.
