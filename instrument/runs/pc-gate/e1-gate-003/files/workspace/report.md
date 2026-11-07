# Regional Totals Summary Report

## Status: BLOCKED

## Summary
This job attempted to summarize regional transaction totals from the input ledger. However, the data is incomplete.

## Data Availability
- **Expected records:** 24 (R001-R024)
- **Available records:** 18
- **Missing records:** R001, R005, R009, R013, R017, R021 (6 records)

## Results (Partial)
Based on the 18 available records, the totals by region are:

| Region | Total (cents) |
|--------|---------------|
| South  | 367,576       |
| North  | 368,475       |
| West   | 272,493       |
| **TOTAL** | **1,008,544** |

## Reason for Blocked Status
The input file /workspace/data/records.csv is missing 6 of the 24 expected records. The job cannot be completed as specified without access to the complete dataset containing all 24 records.
