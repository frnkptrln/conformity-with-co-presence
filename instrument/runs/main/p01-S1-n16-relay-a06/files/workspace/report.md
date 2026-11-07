# Regional Totals Summary Report

## Status: BLOCKED

The input data file `/workspace/data/records.csv` contains **18 records** instead of the expected **24 records** (R001-R024).

## Missing Records
The following 6 records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

## Regional Totals (from available 18 records)

| Region | Total (cents) |
|--------|--------------|
| South  | 264,985      |
| West   | 248,208      |
| North  | 332,992      |
| **TOTAL** | **846,185** |

## Notes
This job is marked as **blocked** because the complete dataset is not available. Processing proceeded with the available records, but full accuracy cannot be confirmed without all 24 expected records. The next job should investigate why 6 records (R001, R005, R009, R013, R017, R021) are missing from the input file.
