---
name: ml-eda
description: Perform Polars-first EDA for schema, missingness, cardinality, distributions, balance, time patterns, and split mismatch.
---

# Skill: ML EDA

## When to use
- A dataset needs first-pass exploration before preprocessing or modeling.
- You need to inspect schema quality, missingness, drift, or target balance.

## Inputs required
- Dataset path or table source.
- Candidate target column and key identifiers if known.
- Any temporal column, split boundary, or expected cohorts.

## Recommended approach
1. Start with `Polars` and use lazy scans for large CSV inputs.
2. Inspect schema, row counts, null rates, cardinality, and basic ranges before plotting anything.
3. Check target balance, temporal coverage, and entity duplication early.
4. Compare train and test slices for obvious distribution mismatch.
5. Collect only compact summaries first; do not materialize the full dataset without need.

## Common pitfalls
- Doing EDA on the full dataset after labels or future information have already leaked in.
- Missing train-test mismatch because only aggregate summaries were reviewed.
- Falling back to pandas for routine inspection instead of keeping the workflow `Polars`-first.

## Deliverables
- Dataset summary with schema, nulls, cardinality, and target balance.
- Noted data quality issues, leakage risks, and likely preprocessing needs.
- A short list of train-test mismatch or temporal risk checks.

## Minimal code pattern
```python
import polars as pl

lf = pl.scan_csv("train.csv")

schema = lf.collect_schema()
row_count = lf.select(pl.len().alias("rows")).collect()
null_counts = lf.null_count().collect()
distinct_counts = lf.select(pl.all().n_unique()).collect()
target_balance = lf.group_by("target").len().collect()

print(schema)
print(row_count)
print(null_counts)
print(distinct_counts)
print(target_balance)
```
