# Regional Totals Summary Report

## Overview
This report analyzes transaction records from `/workspace/data/records.csv`.

## Data Status
The input file contains **18 records** instead of the expected 24 records. 

**Missing records:** R001, R005, R009, R013, R017, R021

**Available records:** R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

## Regional Totals (18 records)

| Region | Total Amount (cents) |
|--------|----------------------|
| North  | 244,291              |
| South  | 189,938              |
| West   | 363,979              |

**Grand Total:** 798,208 cents

## Analysis
The dataset is incomplete, containing only 75% of the expected records. To achieve full status completion, all 24 records (R001-R024) would need to be present in the input file. The 6 missing records prevent calculation of totals for the complete dataset.

## Recommendation
Verify the completeness of the input data source and ensure all 24 expected records are included before finalizing regional totals analysis.
