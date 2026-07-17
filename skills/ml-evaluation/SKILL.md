---
name: ml-evaluation
description: Evaluate traditional ML with business metrics, thresholds, calibration, and cohort breakdowns.
---

# Skill: ML Evaluation

## When to use
- A model needs formal evaluation beyond raw accuracy.
- Thresholds, calibration, or subgroup behavior matter to the decision.

## Inputs required
- Validation or test predictions.
- Primary business objective and cost tradeoffs.
- Any important cohorts, segments, or protected groups to review.

## Recommended approach
1. Choose metrics that match the decision, not just the model type.
2. Evaluate ranking quality, thresholded behavior, and calibration separately when needed.
3. Compare baseline and candidate under the same split and threshold policy.
4. Slice results by meaningful cohorts to catch uneven behavior.
5. Keep the final test set for the end and document what changed between validation and test.

## Common pitfalls
- Using accuracy on skewed datasets.
- Selecting thresholds on the test set.
- Ignoring subgroup failures because overall metrics look good.

## Deliverables
- Evaluation summary with primary and secondary metrics.
- Threshold recommendation and calibration notes when relevant.
- Subgroup or cohort breakdown for key populations.

## Minimal code pattern
```python
from sklearn.metrics import average_precision_score, brier_score_loss, roc_auc_score

roc_auc = roc_auc_score(y_valid, scores)
pr_auc = average_precision_score(y_valid, scores)
brier = brier_score_loss(y_valid, scores)

print({"roc_auc": roc_auc, "pr_auc": pr_auc, "brier": brier})
```
