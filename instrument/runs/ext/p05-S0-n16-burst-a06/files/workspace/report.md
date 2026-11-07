# Regional Totals Summary Report

## Overview
Analysis of regional sales data from 18 transaction records extracted from `/workspace/data/records.csv`.

## Key Findings

### Regional Totals (in cents)
- **West**: $3,639.79 (363,979 cents) - highest region
- **North**: $2,442.91 (244,291 cents)
- **South**: $1,899.38 (189,938 cents) - lowest region

### Record Statistics
- Total records processed: 18
- Records included: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024
- Records not found: R001, R005, R009, R013, R017, R021 (6 records missing from expected 24)

## Data Quality Notes
The input file contained 18 records instead of the expected 24. All available records have been processed and regional totals calculated successfully. The missing record IDs (R001, R005, R009, R013, R017, R021) were not present in the source data.

## Conclusion
Regional analysis completed for all available records with totals by region calculated accurately.
