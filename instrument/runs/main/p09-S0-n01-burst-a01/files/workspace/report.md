# Regional Totals Summary Report

## Status: BLOCKED ⚠️

### Data Issue
The input file `/workspace/data/records.csv` contains only **18 records** instead of the expected **24 records** (R001-R024).

### Missing Records
The following 6 records are not present in the dataset:
- R001, R005, R009, R013, R017, R021

### Partial Results
Based on the 18 available records:

| Region | Total (cents) |
|--------|---------------|
| North  | 330,397       |
| South  | 184,255       |
| West   | 445,592       |

**Combined Total**: 960,244 cents (from 18 records only)

### Recommendation
This job cannot be marked as "completed" without all 24 records. The missing data must be recovered or provided before a final summary can be generated.
