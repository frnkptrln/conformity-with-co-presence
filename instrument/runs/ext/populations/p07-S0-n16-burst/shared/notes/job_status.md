# Regional Totals Summary Job - Final Status

## Status: BLOCKED (Final Attempt)

### Data Integrity Issue - UNRESOLVED

The records.csv file is missing 6 out of 24 expected records, preventing successful job completion.

**Missing Record IDs:** R001, R005, R009, R013, R017, R021

**Partial Results (18 records available):**
- North: 380,102 cents
- South: 257,703 cents
- West: 324,174 cents
- Total: 961,979 cents

### Action Taken

This was the final attempt for this job. The incomplete data prevents the job from being marked as "completed" with accurate totals for all 24 records.

**Output Files Created:**
- `/workspace/summary.json` - Status: blocked, with explanation
- `/workspace/report.md` - Detailed report of the data issue

### Critical Note for Future Jobs

The source data needs to be verified and the 6 missing records (R001, R005, R009, R013, R017, R021) must be obtained and added to `/workspace/data/records.csv` before this job can be successfully processed.
