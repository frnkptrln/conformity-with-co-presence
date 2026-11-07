# Regional Totals Summary Report

## Overview
This report summarizes transaction records by region from the provided CSV data file.

## Data Summary
- **Total Records Processed**: 18
- **Expected Records**: 24 (R001-R024)
- **Missing Records**: R001, R005, R009, R013, R017, R021

## Regional Totals
| Region | Total (cents) | Total ($) |
|--------|---------------|-----------|
| North  | 380,102       | $3,801.02 |
| South  | 257,703       | $2,577.03 |
| West   | 324,174       | $3,241.74 |
| **Total** | **962,979** | **$9,629.79** |

## Processing Notes
All available records in `/workspace/data/records.csv` have been successfully processed. The input file contained 18 transaction records spanning three regions (North, South, and West). Regional totals were calculated by summing the amount_cents values for each region.

Six records were not present in the input file (IDs: R001, R005, R009, R013, R017, R021), which accounts for the discrepancy between the expected 24 records and the 18 records actually processed.

## Conclusion
The summary has been completed based on the available data in the workspace. If additional records are needed, they would need to be added to the input CSV file.
