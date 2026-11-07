# Regional Totals Summary Report

## Status: BLOCKED

### Issue Identified
The input CSV file `/workspace/data/records.csv` contains a data integrity issue:
- **Expected records:** 24 (R001-R024)
- **Actual records found:** 18
- **Missing records:** R001, R005, R009, R013, R017, R021

### Data Available
Of the 18 records present in the CSV, the following regional totals were calculated:

| Region | Total (cents) |
|--------|---------------|
| North  | 342,270       |
| South  | 423,723       |
| West   | 265,276       |

### Records Found
Present records: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Recommendation
Complete data integrity validation is required before this job can be processed successfully. The 6 missing records (33% of expected data) must be supplied to achieve "completed" status.
