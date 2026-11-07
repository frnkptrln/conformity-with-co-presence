# Regional Totals Summary Report

## Status: BLOCKED

### Data Quality Issue
The input file `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records (R001-R024).

### Missing Records
The following records are absent from the input file:
- R001, R005, R009, R013, R017, R021

### Totals for Available Records
Based on the 18 records that could be processed:

| Region | Total (cents) |
|--------|---------------|
| North  | 380,102       |
| South  | 257,703       |
| West   | 324,174       |
| **TOTAL** | **961,979** |

### Recommendation
The input data file needs to be corrected to include all 24 expected records before this job can be marked as completed. The complete reference data source should be verified and the input file should be updated accordingly.
