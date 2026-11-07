# Regional Totals Summary Report

## Status: BLOCKED

## Issue
The input data file contains only 18 records instead of the expected 24 records (R001-R024). The following 6 records are missing:
- R001, R005, R009, R013, R017, R021

## Data Available
Successfully processed 18 records from `/workspace/data/records.csv`

## Regional Totals (18 records only)
- **South**: $4,237.23 (423,723 cents)
- **West**: $2,652.76 (265,276 cents)
- **North**: $3,422.70 (342,270 cents)

**Total Across All Regions**: $10,312.69 (1,031,269 cents)

## Recommendation
The job cannot be completed as specified due to missing input data. Recommend:
1. Verify data extraction/export process
2. Check if records R001, R005, R009, R013, R017, R021 should be recovered from backup
3. Re-run job once complete dataset is available
