# Regional Totals Summary Report

## Status: BLOCKED

### Data Integrity Issue

The regional totals summary job encountered a critical data integrity issue that prevents completion.

**Expected:** 24 records (R001-R024)  
**Found:** 18 records  
**Missing Records:** R001, R005, R009, R013, R017, R021

### Available Data

Despite the missing records, the following regional totals were calculated from the 18 available records:

| Region | Total (cents) |
|--------|---------------|
| North  | 328,718       |
| South  | 419,195       |
| West   | 258,251       |

### Records Processed

R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Action Required

The input data file is missing 6 records (25% of expected data). These records must be located and added to the input file before the job can be marked as completed.
