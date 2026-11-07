# Regional Totals Summary Report

## Data Quality Issue

This job encountered an incomplete dataset. The task specification expected 24 records (R001-R024), but only 18 records were present in the input file.

## Missing Records

The following 6 records were not found in the dataset:
- R001, R005, R009, R013, R017, R021

## Available Data Summary

### Records Processed
- **Total Records:** 18 out of 24 expected
- **Record IDs:** R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Regional Totals (in cents)
- **South:** 419,195 cents
- **West:** 258,251 cents
- **North:** 328,718 cents
- **Grand Total:** 1,006,164 cents (all 18 records)

## Status

**Job Status: BLOCKED**

The job cannot be marked as "completed" because the input data is incomplete. The automatic scoring requires all 24 records to match the reference totals. With only 18 records available, it is impossible to verify the complete and correct totals.

## Recommendation

The data source should be verified to ensure all 24 records (R001-R024) are included in the input file before this job can be successfully completed.
