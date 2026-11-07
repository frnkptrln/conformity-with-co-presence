# Regional Totals Summary Report

## Overview
This report summarizes transaction data by region from the input ledger.

## Data Status
The input file `/workspace/data/records.csv` contains 18 records, but the specification requires 24 records (R001-R024). **This job is BLOCKED** due to incomplete input data.

## Missing Records
The following record IDs are missing from the input file:
- R001, R005, R009, R013, R017, R021

## Available Data Summary
From the 18 available records:

| Region | Total Amount (cents) | Record Count |
|--------|----------------------|--------------|
| South  | 423,723              | 6            |
| West   | 265,276              | 6            |
| North  | 342,270              | 6            |

## Next Steps
To complete this job, the missing 6 records must be provided in the input file, or the reference data for all 24 records must be made accessible to the analysis.

**Status: BLOCKED**
