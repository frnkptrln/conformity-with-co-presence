# Final Attempt Result - Regional Totals Summary Job

**Date**: 2026-11-07  
**Attempt**: FINAL

## Summary
This was the final attempt for the Regional Totals Summary job. The job has been marked as **BLOCKED** due to incomplete input data.

## Key Findings
- **Input Records**: 18 out of 24 expected (75% complete)
- **Missing Records**: R001, R005, R009, R013, R017, R021
- **Status**: BLOCKED (cannot proceed)
- **Score**: 0 (incomplete data)

## Totals from Available 18 Records
- North: 377,979 cents
- South: 368,067 cents
- West: 374,056 cents

## Root Cause
The source data file `/workspace/data/records.csv` is missing 6 records following a pattern (every 5th record starting from odd numbers).

## Next Steps
If this job is assigned again:
1. Verify data completeness BEFORE processing
2. Ensure all 24 records (R001-R024) are present
3. Check for data integrity and consistency
4. Only then proceed with summary generation

## Job Closure
This is the final attempt. The job is closed with score 0 due to incomplete data.
