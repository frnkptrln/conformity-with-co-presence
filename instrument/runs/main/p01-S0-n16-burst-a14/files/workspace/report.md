# Regional Totals Summary Report

## Status: BLOCKED

### Data Quality Issue

The input file `/workspace/data/records.csv` contains **18 records** instead of the expected **24 records** (R001-R024).

**Missing Records:** R001, R005, R009, R013, R017, R021 (6 records total)

### Available Data Summary

Analysis of the 18 available records:

| Region | Total (cents) | Record Count |
|--------|---------------|--------------|
| South  | 264,985       | 6            |
| West   | 248,208       | 6            |
| North  | 332,992       | 6            |
| **TOTAL** | **846,185** | **18**  |

### Records Processed

South: R002, R008, R011, R014, R020, R023
West: R003, R006, R012, R015, R018, R024
North: R004, R007, R010, R016, R019, R022

### Conclusion

The job is blocked due to incomplete input data. The dataset appears to be missing all odd-numbered records (except R001-R024 which should include R005, R009, R013, R017, R021). The totals shown represent only the 18 records present in the input file and cannot be validated against the expected 24-record dataset.
