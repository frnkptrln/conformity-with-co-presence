# Regional Totals Summary Report

## Status: BLOCKED

### Data Quality Issue

The regional totals summary job cannot be completed as specified due to incomplete input data.

**Expected:** 24 records (R001-R024)  
**Received:** 18 records  
**Missing:** R001, R005, R009, R013, R017, R021

### Available Data Summary

Analysis was performed on the 18 available records in `/workspace/data/records.csv`:

| Region | Total Amount (cents) |
|--------|----------------------|
| North  | 244,291              |
| South  | 189,938              |
| West   | 363,979              |

**Total across all regions:** 798,208 cents

### Recommendation

The data source should be verified and the missing records located before this job can be completed. This is a data quality issue that requires investigation upstream of this job.

---
*This job was unable to process all 24 expected records due to missing input data.*
