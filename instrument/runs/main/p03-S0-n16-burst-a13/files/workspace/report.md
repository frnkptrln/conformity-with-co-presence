# Regional Totals Summary Report

## Status
**BLOCKED** - Incomplete Data

## Summary
The input CSV file (`/workspace/data/records.csv`) contains only 18 records instead of the expected 24 records spanning the range R001 through R024.

## Missing Records
The following 6 record IDs are missing from the dataset:
- R001, R005, R009, R013, R017, R021

## Available Data Analysis
Of the 18 records present in the file, the regional totals are:

| Region | Total (cents) | Records |
|--------|---------------|---------|
| North  | 157,857       | 6       |
| South  | 439,870       | 6       |
| West   | 285,519       | 6       |
| **TOTAL** | **883,246** | **18** |

## Conclusion
The job cannot be marked as "completed" because the required 24 records are not present in the input file. The missing data prevents accurate validation against the reference dataset. The available 18 records have been processed and summarized above, but completion requires the 6 missing records.

### Records Present
R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024
