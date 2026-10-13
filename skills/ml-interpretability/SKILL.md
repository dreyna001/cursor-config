---
name: ml-interpretability
description: "Explain traditional ML behavior with coefficients, feature importance, partial dependence, and approved tools."
---
# Skill: ML Interpretability

## When to use
- A model's main drivers need explanation.
- Stakeholders need interpretable evidence for how predictions are made.

## Inputs required
- Fitted model or pipeline.
- Feature names after preprocessing if available.
- Any stakeholder or regulatory explainability constraints.

## Recommended approach
1. Start with the simplest faithful method the model supports: coefficients, feature importance, or permutation importance.
2. Use partial dependence or ICE only for a few important features and only when the assumptions are reasonable.
3. Use SHAP only if it is already approved in the project or clearly justified.
4. Distinguish global behavior from local example explanations.
5. Pair explanations with caveats about correlation, leakage risk, and feature stability.

## Common pitfalls
- Treating feature importance as causality.
- Explaining a transformed feature space without mapping it back to meaningful names.
- Adding heavy explanation dependencies for a one-off need.

## Deliverables
- Ranked explanation of main drivers.
- Brief note on explanation method and limitations.
- Optional local examples for representative cases.

## Minimal code pattern
```python
from sklearn.inspection import permutation_importance

result = permutation_importance(
    estimator=model,
    X=X_valid,
    y=y_valid,
    n_repeats=10,
    random_state=42,
)

print(result.importances_mean)
```
