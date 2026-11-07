# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input file `/workspace/data/records.csv` contains incomplete data:
- **Records present:** 18 of 24 expected
- **Missing record IDs:** R001, R005, R009, R013, R017, R021
- **Data completeness:** 75%

### Available Data Summary
Partial regional totals from 18 records:

| Region | Amount (cents) | Records |
|--------|-----------------|---------|
| South  | 423,723        | 7       |
| West   | 265,276        | 6       |
| North  | 342,270        | 5       |
| **Total** | **1,031,269** | **18** |

### Constraints
The complete reference data required to fulfill this task is not accessible within current system constraints. Task completion requires all 24 records to match reference totals.

### Recommendation
Provide complete input data in `/workspace/data/records.csv` with all 24 records (R001-R024) to enable task completion.
