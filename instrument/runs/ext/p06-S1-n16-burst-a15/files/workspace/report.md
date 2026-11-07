# Regional Totals Summary Report

## Overview
This report summarizes the regional distribution of 18 transaction records from the input CSV file.

## Data Processing
The input file `/workspace/data/records.csv` was processed to extract and aggregate financial records by region. 

**Note:** The dataset contained 18 records (IDs: R002-R024 with gaps) rather than the expected 24 records. Records R001, R005, R009, R013, R017, and R021 were not found in the input data.

## Regional Totals

| Region | Amount (cents) | Amount (dollars) |
|--------|----------------|------------------|
| North  | 328,718        | $3,287.18        |
| South  | 419,195        | $4,191.95        |
| West   | 258,251        | $2,582.51        |
| **Total** | **1,006,164** | **$10,061.64**   |

## Summary
- **Total Records Processed:** 18
- **Regions Covered:** North, South, West
- **Largest Region:** South with $4,191.95
- **Smallest Region:** West with $2,582.51

All available records have been successfully processed and aggregated by region.
