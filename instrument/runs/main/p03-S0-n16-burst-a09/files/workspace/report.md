# Regional Totals Summary Report

## Overview
This report summarizes regional financial data from the available records in the input dataset.

## Data Summary
- **Records Processed**: 18 records
- **Expected Records**: 24 (R001-R024)
- **Data Quality Issue**: 6 records are missing from the input file (R001, R005, R009, R013, R017, R021)

## Regional Totals (in cents)
| Region | Total Amount |
|--------|-------------|
| South  | 439,870     |
| West   | 285,519     |
| North  | 157,857     |
| **Grand Total** | **883,246** |

## Findings
The analysis processed 18 records from the input CSV file. The data shows:
- **South region** has the largest total at 439,870 cents
- **West region** totals 285,519 cents
- **North region** totals 157,857 cents

## Data Quality Note
⚠️ **Important**: The input file contains incomplete data. While the specification indicates 24 records should be present (R001-R024), only 18 records were found in the actual CSV file. This discrepancy should be investigated for upstream data integrity issues.
