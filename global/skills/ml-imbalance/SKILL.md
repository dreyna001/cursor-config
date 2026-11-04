---
name: ml-imbalance
description: "Handle traditional ML class imbalance with correct training boundaries, class weights, thresholds, PR tradeoffs, and resampling."
---
# Skill: ML Imbalance

## When to use
- Positive labels are rare or cost asymmetry is high.
- The task requires explicit recall, precision, or threshold tradeoffs.

## Inputs required
- Label distribution and task metric.
- Training-only split or CV plan.
- Business cost preference for false positives vs false negatives.

## Recommended approach
1. Measure the imbalance first and set metrics that reflect the actual decision.
2. Try class weighting before more invasive methods.
3. Tune thresholds on validation data rather than assuming `0.5` is correct.
4. If resampling is needed, apply it only inside training folds.
5. Recheck calibration and subgroup behavior after any imbalance treatment.

## Common pitfalls
- Reporting ROC AUC alone on highly imbalanced data.
- Resampling before the split and leaking duplicated examples.
- Optimizing recall without quantifying the operational false-positive cost.

## Deliverables
- Chosen imbalance strategy and rationale.
- Threshold recommendation tied to a validation metric.
- Precision-recall tradeoff summary for stakeholders.

## Minimal code pattern
```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve

model = LogisticRegression(max_iter=1000, class_weight="balanced")
model.fit(X_train, y_train)

scores = model.predict_proba(X_valid)[:, 1]
precision, recall, thresholds = precision_recall_curve(y_valid, scores)
```
