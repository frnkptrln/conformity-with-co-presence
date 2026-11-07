# Regional Totals Summary Report

## Overview
This report summarizes the regional distribution of amounts from the records dataset.

## Data Summary
- **Records Processed**: 18 out of expected 24
- **Missing Records**: R001, R005, R009, R013, R017, R021 (6 records not found in source file)
- **Processing Date**: 2026-11-07

## Regional Breakdown

| Region | Total Amount (cents) | Record Count |
|--------|----------------------|--------------|
| South  | 423,723              | 6            |
| West   | 265,276              | 6            |
| North  | 342,270              | 6            |
| **TOTAL** | **1,031,269**      | **18**       |

## Key Findings
- The South region has the highest total amount (423,723 cents)
- The North region has the second highest (342,270 cents)
- The West region has the lowest total (265,276 cents)
- All three regions are evenly represented with 6 records each

## Data Quality Notes
The input CSV file at `/workspace/data/records.csv` contains 18 records instead of the expected 24. Six records (IDs: R001, R005, R009, R013, R017, R021) are missing from the dataset. This analysis is based on the records that were available in the source file.
