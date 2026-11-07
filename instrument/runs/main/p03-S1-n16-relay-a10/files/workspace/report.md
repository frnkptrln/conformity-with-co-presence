# Regional Totals Summary Report

## Executive Summary
Analysis of regional transaction data from the provided ledger has been completed for 18 available records (R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024).

## Data Findings

### Record Count
- **Available Records:** 18
- **Expected Records:** 24
- **Missing Records:** 6 (R001, R005, R009, R013, R017, R021)

### Regional Totals (in cents)
| Region | Total Amount (¢) | USD Equivalent |
|--------|------------------|-----------------|
| South  | 439,870          | $4,398.70       |
| West   | 285,519          | $2,855.19       |
| North  | 157,857          | $1,578.57       |
| **TOTAL** | **883,246**    | **$8,832.46**   |

## Analysis Details
- The South region represents the largest share at 49.8% of available transactions
- The West region accounts for 32.3% of available transactions  
- The North region accounts for 17.9% of available transactions

## Data Quality Note
The source file `/workspace/data/records.csv` is missing 6 records (25% of the expected dataset). Regional totals are calculated only from verified records present in the source file. Previous jobs noted this same data constraint. The complete reference dataset may exist in a protected location not accessible under current security restrictions.

## Conclusion
All available records have been processed and verified. Regional totals are accurate for the 18 records provided. For a complete analysis including all 24 expected records, the missing 6 records would need to be provided in the source data file.
