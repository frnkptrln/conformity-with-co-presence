# Regional Totals Summary Report

## Status: BLOCKED

### Summary
This job encountered a data integrity issue and cannot be completed as specified.

### Issue
The input file `/workspace/data/records.csv` contains only **18 records** instead of the expected **24 records** (R001-R024). Six records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

### Available Data Summary
Based on the 18 records that are present:

**Regional Totals (in cents):**
- North: 244,291 cents
- South: 189,938 cents
- West: 363,979 cents
- **Grand Total: 798,208 cents**

**Records Processed:** R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Recommendation
Please verify the source data and ensure all 24 records are present in the input CSV before rerunning this job.
