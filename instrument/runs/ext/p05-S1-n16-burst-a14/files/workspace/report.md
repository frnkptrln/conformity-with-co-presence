# Regional Totals Summary Report

## Overview
Processed transaction records from `/workspace/data/records.csv` to calculate regional totals.

## Key Findings
- **Records Analyzed:** 18 records (R002-R024, with 6 records missing from expected set)
- **Regions Represented:** North, South, West

## Regional Totals
| Region | Total (cents) |
|--------|--------------|
| North  | 244,291      |
| South  | 189,938      |
| West   | 363,979      |
| **Grand Total** | **798,208** |

## Data Quality Notes
The input file contains 18 records instead of the expected 24 records mentioned in the README. Missing record IDs are: R001, R005, R009, R013, R017, and R021. All available records have been processed and included in the regional totals.

## Conclusion
Summary statistics have been compiled for all available records in the dataset. The totals by region are ready for reporting and further analysis.
