# Regional Totals Summary Report

## Status: BLOCKED

## Data Availability Issue

The task requires processing 24 records (R001-R024) from the input file `/workspace/data/records.csv`. However, the actual input file contains only **18 records**, missing 6 records:
- Missing: R001, R005, R009, R013, R017, R021

## Records Processed

Successfully summarized the 18 available records:

| Region | Total (cents) | Count |
|--------|---------------|-------|
| North  | 445,994       | 6     |
| South  | 167,478       | 5     |
| West   | 337,092       | 7     |
| **TOTAL** | **950,564** | **18** |

## Reason for Blocked Status

To complete this job with all 24 records as specified in the requirements, access to the complete ledger data is required. The available input file is incomplete, preventing validation against the reference dataset needed for automatic scoring.

## Deliverables

- ✅ summary.json: Generated with status "blocked" and available data
- ✅ report.md: This report
