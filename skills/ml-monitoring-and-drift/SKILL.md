---
name: ml-monitoring-and-drift
description: Monitor traditional ML production quality, data drift, prediction drift, label lag, and retraining signals.
---

# Skill: ML Monitoring And Drift

## When to use
- A model is moving into production or already serving predictions.
- You need monitoring for data quality, prediction behavior, or retraining triggers.

## Inputs required
- Reference training summary or baseline production window.
- Current production inputs and predictions.
- Any available delayed labels and alert thresholds.

## Recommended approach
1. Track input health, score distributions, and business outcome metrics separately.
2. Monitor data drift, prediction drift, and label lag as distinct signals.
3. Define thresholds and retraining triggers before incidents happen.
4. Compare current slices against a stable reference window, not just yesterday.
5. Keep monitoring lightweight enough to run on schedule and easy to audit.

## Common pitfalls
- Treating drift as a single number without checking which features moved.
- Waiting for labels before monitoring anything.
- Triggering retraining without checking whether the drift is operationally meaningful.

## Deliverables
- Monitoring metric set and cadence.
- Drift checks with thresholds and alert conditions.
- Explicit retraining triggers and ownership notes.

## Minimal code pattern
```python
import polars as pl

reference = pl.read_csv("reference_summary.csv")
current = pl.read_csv("current_summary.csv")

drift = current.join(reference, on="feature", suffix="_ref").with_columns(
    (pl.col("null_rate") - pl.col("null_rate_ref")).abs().alias("null_rate_shift"),
    (pl.col("mean") - pl.col("mean_ref")).abs().alias("mean_shift"),
)

print(drift.filter((pl.col("null_rate_shift") > 0.05) | (pl.col("mean_shift") > 1.0)))
```
