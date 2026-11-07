# Regional Totals Summary Report

## Status: BLOCKED

### Data Integrity Issue
The input file `/workspace/data/records.csv` contains only **18 records** instead of the expected **24 records** (R001-R024) as specified in the job requirements.

### Missing Records
The following 6 records are not present in the dataset:
- R001, R005, R009, R013, R017, R021

### Available Data Summary
The 18 records that are present in the file have been processed with the following regional totals:

| Region | Total (cents) |
|--------|---------------|
| North  | 332,992       |
| South  | 264,985       |
| West   | 248,208       |

### Records Analyzed
R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Conclusion
This job cannot be marked as completed due to incomplete input data. The dataset is missing 25% of the expected records. Please verify the data source and provide all 24 records to complete this task.
