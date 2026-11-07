# Regional Totals Summary Report

## Status: BLOCKED

### Data Quality Issue

The input CSV file at `/workspace/data/records.csv` is incomplete and cannot support successful job completion.

**Expected Dataset:**
- 24 records (R001 through R024)
- Columns: record_id, region, amount_cents

**Actual Dataset:**
- 18 records only
- Missing: R001, R005, R009, R013, R017, R021 (6 records)

### Partial Results (18 records only)

For the 18 records available in the CSV file, the regional totals are:

| Region | Total (cents) |
|--------|---------------|
| North  | 380,102       |
| South  | 257,703       |
| West   | 324,174       |
| **TOTAL** | **961,979**   |

### Recommendation

This job cannot be completed successfully without the complete dataset. The missing 6 records must be sourced and added to the input CSV file to allow for accurate regional totals calculation and job completion.
