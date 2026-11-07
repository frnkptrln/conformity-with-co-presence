# Regional Totals Summary - Status Report

## Status: BLOCKED ❌

## Summary
The regional totals summary job could not be completed due to incomplete input data.

### Data Quality Issue
- **Expected Records**: 24 (R001-R024)
- **Found Records**: 18
- **Missing Records**: R001, R005, R009, R013, R017, R021 (6 records)

### Processed Data
The job successfully processed the 18 available records and calculated the following regional totals:

| Region | Total Amount (cents) |
|--------|----------------------|
| North  | 332,992              |
| South  | 264,985              |
| West   | 248,208              |
| **GRAND TOTAL** | **846,185** |

### Issue Resolution Required
The input file `/workspace/data/records.csv` is missing 6 of 24 expected records. The data source must be verified and corrected to complete this job successfully. Without all 24 records, the totals cannot be validated against the reference dataset.
