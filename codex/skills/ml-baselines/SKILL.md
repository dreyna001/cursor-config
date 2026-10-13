---
name: ml-baselines
description: "Establish dummy, linear, and lightweight tree baselines before complex traditional ML models."
---
# Skill: ML Baselines

## When to use
- Modeling has started but no trustworthy baseline exists yet.
- A candidate model needs comparison against simple, deployable alternatives.

## Inputs required
- Problem type and primary metric.
- Training and validation split or CV plan.
- Preprocessed feature matrix or pipeline-ready feature definition.

## Recommended approach
1. Start with a dummy baseline tied to the task.
2. Add a simple linear baseline such as logistic or linear regression.
3. Add one lightweight nonlinear baseline such as random forest when appropriate.
4. Compare all baselines on the same validation protocol.
5. Escalate to heavier libraries only if the baseline gap justifies it and the project allows it.

## Common pitfalls
- Comparing models across different splits or metrics.
- Skipping dummy baselines and overstating model value.
- Introducing gradient boosting libraries before proving simpler options are insufficient.

## Deliverables
- Baseline table with metric values and notes.
- Chosen candidate for deeper tuning or rejection.
- Clear evidence that the candidate beats trivial alternatives.

## Minimal code pattern
```python
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

models = {
    "dummy": DummyClassifier(strategy="prior"),
    "logistic": LogisticRegression(max_iter=1000),
    "random_forest": RandomForestClassifier(n_estimators=200, random_state=42),
}
```
