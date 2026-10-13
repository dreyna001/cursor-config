---
name: ml-hyperparameter-tuning
description: "Tune traditional ML models with bounded search spaces, correct CV boundaries, and baseline-aware selection."
---
# Skill: ML Hyperparameter Tuning

## When to use
- A baseline is established and targeted tuning is justified.
- You need a repeatable search space and CV strategy.

## Inputs required
- Candidate model or pipeline.
- Training-only split or CV plan.
- Primary metric and runtime budget.

## Recommended approach
1. Tune only after baseline performance is understood.
2. Search a small, justified parameter space before expanding it.
3. Keep CV entirely inside the training split.
4. Prefer randomized search when the space is moderate or large.
5. Use early stopping only when the chosen library supports it and the validation boundary is clear.

## Common pitfalls
- Tuning against the final holdout test set.
- Searching wide spaces without a runtime budget or rationale.
- Treating tiny metric gains as meaningful without checking variance and complexity cost.

## Deliverables
- Search space and CV design.
- Best parameter set and corresponding validation score.
- Clear note on whether tuning materially beat the baseline.

## Minimal code pattern
```python
from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

pipeline = Pipeline([("model", RandomForestClassifier(random_state=42))])

search = RandomizedSearchCV(
    estimator=pipeline,
    param_distributions={
        "model__n_estimators": [100, 200, 400],
        "model__max_depth": [None, 5, 10, 20],
        "model__min_samples_leaf": [1, 2, 5],
    },
    n_iter=10,
    scoring="average_precision",
    cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
    random_state=42,
)
```
