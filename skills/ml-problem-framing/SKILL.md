---
name: ml-problem-framing
description: Frame traditional ML tasks by defining target, prediction unit, constraints, and success metrics.
---

# Skill: ML Problem Framing

## When to use
- A new ML use case needs to be framed before EDA or modeling.
- The task type, target, constraints, or success metric is still ambiguous.

## Inputs required
- Problem statement and business outcome.
- Available data sources and likely prediction unit.
- Key constraints such as latency, throughput, label quality, and explainability needs.

## Recommended approach
1. Name the task type: classification, regression, clustering, ranking, or anomaly detection.
2. Define the target and the exact unit of prediction.
3. Clarify the decision the model will support and the cost of false positives vs false negatives.
4. Lock primary and secondary metrics that match that decision.
5. Record operational constraints such as data freshness, inference shape, and deployment environment.
6. State what is out of scope before moving into EDA.

## Common pitfalls
- Starting feature work before the target and prediction unit are stable.
- Choosing metrics that do not match the business decision.
- Framing a problem as supervised learning when labels are weak or unavailable.

## Deliverables
- Problem type and target definition.
- Unit of prediction and label window.
- Success metrics, constraints, and explicit assumptions.

## Minimal code pattern
```python
problem = {
    "task_type": "classification",
    "prediction_unit": "customer-month",
    "target": "churned_within_30_days",
    "primary_metric": "average_precision",
    "secondary_metrics": ["recall_at_threshold", "roc_auc"],
    "constraints": {
        "batch_or_realtime": "batch",
        "max_scoring_latency_s": 300,
        "explainability_required": True,
    },
}
```
