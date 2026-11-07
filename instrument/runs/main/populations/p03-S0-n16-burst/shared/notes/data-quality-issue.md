# Data Quality Issue - Regional Totals Job

## Issue
The input file /workspace/data/records.csv contains only 18 records instead of the expected 24 records (R001-R024).

## Missing Records
The following 6 records are absent from the dataset:
- R001
- R005
- R009
- R013
- R017
- R021

## Impact
Regional totals were calculated from the available 18 records:
- South: $4,398.70 (9 records)
- West: $2,855.19 (6 records)
- North: $1,578.57 (3 records)

## Recommendation
If this is a critical job with strict requirements for all 24 records, the data source should be investigated to locate the missing records.
