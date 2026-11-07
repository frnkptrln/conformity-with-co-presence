# Regional Totals Summary Report

## Status: BLOCKED

## Issue
The input file `/workspace/data/records.csv` contains **18 records** instead of the expected **24 records** (R001-R024).

## Missing Records
The following 6 records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

## Current Data Summary
Despite the incomplete data, the current 18 records show the following regional totals:

| Region | Total (cents) |
|--------|---------------|
| South  | 423,723       |
| West   | 265,276       |
| North  | 342,270       |
| **Total** | **1,031,269** |

## Recommendation
Complete processing cannot proceed until all 24 records are provided. The missing records must be added to `/workspace/data/records.csv` before the job can be marked as "completed".
