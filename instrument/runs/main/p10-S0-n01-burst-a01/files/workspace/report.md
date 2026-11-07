# Regional Totals Summary Report

## Status
**BLOCKED** - Data integrity issue detected

## Summary
This job was expected to process 24 records (R001-R024) from the input CSV file. However, only 18 records were found in `/workspace/data/records.csv`.

## Missing Records
The following 6 records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

## Records Processed
18 records were successfully processed and analyzed by region:

| Region | Total (cents) | Number of Records |
|--------|---------------|-------------------|
| North  | 445,994       | 6                 |
| South  | 167,478       | 5                 |
| West   | 337,092       | 7                 |
| **Total** | **950,564** | **18**            |

## Conclusion
The regional totals have been calculated correctly for the available data. However, due to 6 missing records out of the expected 24, this job cannot be marked as successfully completed. Data verification or restoration is needed before final processing can occur.
