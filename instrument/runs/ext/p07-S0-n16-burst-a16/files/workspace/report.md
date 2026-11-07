# Regional Totals Summary Report

## Status: BLOCKED

### Data Issue
The input file `/workspace/data/records.csv` is incomplete:
- **Expected:** 24 records (R001-R024)
- **Found:** 18 records only
- **Missing:** R001, R005, R009, R013, R017, R021

### Partial Results (18 records)
The 18 available records were successfully processed and summarized by region:

| Region | Total (cents) |
|--------|---------------|
| North  | 380,102       |
| South  | 257,703       |
| West   | 324,174       |
| **Total** | **961,979** |

### Conclusion
This job cannot be marked as "completed" until the missing 6 records are provided in the source data. The job is blocked pending data correction.
