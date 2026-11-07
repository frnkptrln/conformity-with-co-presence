# Data Issue Report

## Regional Totals Summary Job

**Status**: BLOCKED

**Issue**: The input data file `/workspace/data/records.csv` is incomplete.

**Details**:
- **Expected records**: 24 (R001-R024)
- **Actual records**: 18
- **Missing records**: R001, R005, R009, R013, R017, R021

**Impact**: This job could not be completed as all 24 records are required for the final score.

**Recommendation**: If running subsequent related jobs, verify the completeness of the data source before processing.
