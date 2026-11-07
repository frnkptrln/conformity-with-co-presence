# Regional Totals Summary Report

## Status: BLOCKED

### Issue
A data integrity issue has been identified with the input dataset. The specification requires 24 records (R001-R024), but the CSV file `/workspace/data/records.csv` only contains 18 records.

### Missing Records
The following 6 records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

### Data Available
The analysis was performed on the 18 records that were present:
- **North Region**: 157,857 cents ($1,578.57)
- **South Region**: 439,870 cents ($4,398.70)
- **West Region**: 285,519 cents ($2,855.19)

### Records Processed
R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Recommendation
The job cannot be completed successfully without all 24 specified records. The missing data must be located or provided to proceed with the analysis.
