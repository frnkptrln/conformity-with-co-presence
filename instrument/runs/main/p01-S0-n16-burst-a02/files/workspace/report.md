# Regional Totals Summary Report

## Overview
This report summarizes financial transactions across three regions based on the records in `/workspace/data/records.csv`.

## Data Summary
- **Total Records Processed**: 18
- **Record IDs**: R002-R024 (with gaps at R001, R005, R009, R013, R017, R021)

## Regional Totals (in cents)
| Region | Total Amount (cents) |
|--------|----------------------|
| North  | 332,992              |
| South  | 264,985              |
| West   | 248,208              |
| **Grand Total** | **846,185**  |

## Findings
- The North region has the highest total transactions at $3,329.92
- The South region follows with $2,649.85
- The West region has $2,482.08

## Data Quality Note
Six record IDs were missing from the input dataset (R001, R005, R009, R013, R017, R021), resulting in 18 records processed instead of the expected 24.
