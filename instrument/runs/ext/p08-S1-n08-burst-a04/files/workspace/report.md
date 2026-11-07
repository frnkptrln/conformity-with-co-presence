# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records spanning R001 to R024.

### Missing Records
The following record IDs are missing from the dataset:
- R001, R005, R009, R013, R017, R021

### Data Summary (18 records available)
The 18 available records were processed and summarized by region:

| Region | Total (cents) |
|--------|---------------|
| North  | 342,270       |
| South  | 423,723       |
| West   | 265,276       |

### Conclusion
The job cannot be completed as specified because the input dataset is incomplete. All 24 records (R001-R024) are required to produce a valid summary. Six records are missing from the provided data file.
