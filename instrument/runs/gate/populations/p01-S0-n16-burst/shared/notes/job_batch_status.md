# Batch Status Note

## Job: Regional Totals Summary

**Status**: BLOCKED

**Issue**: Input data file contains incomplete records.
- Expected: 24 records (R001-R024)
- Actual: 18 records
- Missing: R001, R005, R009, R013, R017, R021

**Action Taken**: Job blocked with data quality explanation provided in summary.json and report.md.

**For Next Job**: If this batch continues, please verify the source data and ensure all 24 records are present before retrying.
