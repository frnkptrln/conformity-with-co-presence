# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input file `/workspace/data/records.csv` is incomplete and cannot be processed to full specifications.

**Expected**: 24 records (R001-R024)  
**Received**: 18 records  
**Missing**: 6 records (R001, R005, R009, R013, R017, R021)

### Partial Results (18 Available Records)
The following regional totals were calculated from the available 18 records:

| Region | Total (cents) |
|--------|---------------|
| North  | 273,324       |
| South  | 240,720       |
| West   | 197,094       |

**Grand Total**: 711,138 cents (18 records)

### Records Available
R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Impact
The job cannot be marked as "completed" because 25% of the expected data is missing. To achieve full completion, the missing 6 records must be located and integrated into the dataset.

### Recommendation
- Verify the source data system for the missing record IDs
- Obtain records R001, R005, R009, R013, R017, and R021 to complete the dataset
- Re-run this job once all 24 records are available
