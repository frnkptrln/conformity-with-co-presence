# Regional Totals Summary Report

## Status: BLOCKED

## Overview
The task requires processing 24 regional records (R001-R024) to generate regional totals. However, the input data file contains only 18 records, preventing completion of the full task scope.

## Data Processed
- **Records Available**: 18 of 24 expected
- **Missing Records**: R001, R005, R009, R013, R017, R021 (6 records)

## Regional Totals (18 records only)
| Region | Total (cents) | Record Count |
|--------|---------------|--------------|
| North  | 380,102       | 6            |
| South  | 257,703       | 6            |
| West   | 324,174       | 6            |
| **TOTAL** | **961,979** | **18**       |

## Records Processed by Region

**North:** R004 (88,905), R007 (98,794), R010 (15,110), R016 (23,455), R019 (84,810), R022 (69,028)

**South:** R002 (28,036), R008 (74,482), R011 (35,779), R014 (38,826), R020 (30,188), R023 (50,392)

**West:** R003 (42,276), R006 (40,330), R012 (56,948), R015 (56,043), R018 (31,854), R024 (96,723)

## Issue
The input file `/workspace/data/records.csv` is incomplete. To achieve task completion, all 24 records (including R001, R005, R009, R013, R017, R021) must be available in the input data.
