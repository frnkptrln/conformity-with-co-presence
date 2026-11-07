# Regional Totals Summary Report

## Status: BLOCKED

### Data Integrity Issue
The input file `/workspace/data/records.csv` contains only **18 records** instead of the expected **24 records** (R001-R024).

### Missing Records
The following 6 records are missing from the dataset:
- R001
- R005
- R009
- R013
- R017
- R021

### Available Data Summary
Of the 18 records present in the file:

| Region | Total (cents) |
|--------|---------------|
| North  | 332,992       |
| South  | 264,985       |
| West   | 248,208       |
| **TOTAL** | **846,185** |

### Records by Region
- **North (6 records)**: R004, R007, R010, R016, R019, R022
- **South (6 records)**: R002, R008, R011, R014, R020, R023
- **West (6 records)**: R003, R006, R012, R015, R018, R024

### Recommendation
The job cannot be completed as specified. The data file is incomplete and missing 25% of the expected records. Please provide the missing records to proceed with completion.
