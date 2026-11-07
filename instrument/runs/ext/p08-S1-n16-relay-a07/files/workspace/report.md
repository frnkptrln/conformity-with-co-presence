# Regional Totals Summary Report

## Status: BLOCKED

### Data Completeness Issue

The task requires analysis of 24 records (R001-R024), but the input file `/workspace/data/records.csv` contains only 18 records.

**Missing Records:** R001, R005, R009, R013, R017, R021 (6 records, 25% of required data)

### Analysis of Available Data

For the 18 available records, the regional totals are:

| Region | Total (cents) |
|--------|---------------|
| South  | 423,723       |
| West   | 265,276       |
| North  | 342,270       |
| **TOTAL** | **1,031,269** |

### Impact

- Cannot provide totals for all 24 records as required
- Cannot achieve "completed" status with complete accuracy
- Previous attempts have encountered the same data incompleteness issue

### Recommendation for Next Job

If this job is re-attempted, the input file must be complete with all 24 records in `/workspace/data/records.csv` to enable successful completion.
