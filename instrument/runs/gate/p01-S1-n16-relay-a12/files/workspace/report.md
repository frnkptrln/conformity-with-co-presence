# Regional Totals Summary Report

## Status: BLOCKED

## Data Integrity Issue

The regional totals summary task could not be completed as specified. An analysis of the input data revealed a critical data integrity issue.

### Findings

- **Records Found**: 18 records
- **Records Expected**: 24 records (R001-R024)
- **Missing Records**: R001, R005, R009, R013, R017, R021 (6 records)

### Partial Results (18 Records Available)

The available records were analyzed and the following regional totals were calculated from the 18 records present:

| Region | Total Amount (cents) |
|--------|----------------------|
| South  | 240,720              |
| West   | 197,094              |
| North  | 273,324              |
| **Grand Total** | **711,138** |

### Recommendations

1. Verify the source data and locate the missing records
2. Confirm data extraction/export process is functioning correctly
3. Re-run this job once all 24 records are available
4. Validate that records R001, R005, R009, R013, R017, R021 are accessible in the source system
