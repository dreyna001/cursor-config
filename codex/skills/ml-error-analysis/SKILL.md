---
name: ml-error-analysis
description: "Diagnose traditional ML mistakes with false-positive, false-negative, cohort, label, and feature analysis."
---
# Skill: ML Error Analysis

## When to use
- Overall metrics are acceptable but mistakes still need explanation.
- You need to understand false positives, false negatives, or cohort-specific failures.

## Inputs required
- Validation or test predictions with scores.
- Ground-truth labels.
- Useful slice columns such as cohort, time bucket, or source system.

## Recommended approach
1. Build a row-level error table with labels, predictions, scores, and slice keys.
2. Separate false positives and false negatives before looking at broad aggregates.
3. Group by cohort, source, feature ranges, and time windows to find concentrated failures.
4. Flag suspicious labels and upstream data quality issues separately from model limitations.
5. Turn recurring error patterns into actionable next steps for feature, label, or threshold changes.

## Common pitfalls
- Looking only at aggregate metrics and not at concrete failure slices.
- Treating mislabeled examples as model errors without evidence.
- Mixing threshold problems with representation problems.

## Deliverables
- Ranked list of failure slices and representative examples.
- Assessment of likely causes: threshold, features, labels, or data coverage.
- Recommended follow-up changes with expected impact.

## Minimal code pattern
```python
import polars as pl

errors = pl.DataFrame(
    {
        "y_true": y_valid,
        "y_pred": y_pred,
        "score": scores,
        "segment": segment_valid,
    }
).with_columns(
    ((pl.col("y_true") == 0) & (pl.col("y_pred") == 1)).alias("false_positive"),
    ((pl.col("y_true") == 1) & (pl.col("y_pred") == 0)).alias("false_negative"),
)

print(errors.group_by("segment").agg(pl.col("false_positive").sum(), pl.col("false_negative").sum()))
```
