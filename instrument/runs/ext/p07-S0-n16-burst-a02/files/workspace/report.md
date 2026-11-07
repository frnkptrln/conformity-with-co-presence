# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file (`/workspace/data/records.csv`) contains incomplete data. Only 18 of 24 expected records were found in the file.

### Data Found
- **Records present**: 18 total (R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024)
- **Records missing**: 6 (R001, R005, R009, R013, R017, R021)

### Regional Totals (Based on Available Data)
| Region | Total (cents) |
|--------|--------------|
| North  | 380,102      |
| South  | 257,703      |
| West   | 324,174      |
| **TOTAL** | **961,979** |

### Recommendation
This job requires all 24 records (R001-R024) to complete successfully. The missing 6 records must be located or provided before processing can be marked as complete. The current status is "blocked" pending resolution of the missing data.
