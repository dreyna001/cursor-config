---
name: ml-model-training
description: "Train traditional ML models with Polars-first prep, proper evaluation, and saved classification or regression artifacts."
---
# Skill: ML Model Training

## When to use
- A traditional ML pipeline needs to be fit, evaluated, and saved.
- Data preparation and model training need a clean boundary.

## Inputs required
- Training dataset and target column.
- Split strategy and chosen baseline or candidate model.
- Artifact path for the fitted pipeline.

## Recommended approach
1. Use `Polars` for data preparation and feature shaping.
2. Convert to `NumPy`, Arrow, or pandas only when the training library requires it.
3. Keep the conversion late and narrow: features, target, and only the needed columns.
4. Fit preprocessing and model steps inside one pipeline when possible.
5. Save the fitted pipeline artifact immediately after evaluation.

## Common pitfalls
- Training on data that was transformed outside the fitted pipeline.
- Converting large datasets too early and losing scale headroom.
- Saving only the model weights and not the preprocessing logic.

## Deliverables
- Fitted training pipeline.
- Validation metrics on the agreed split.
- Serialized artifact that includes learned preprocessing and model state.

## Minimal code pattern
```python
import pickle
import polars as pl
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import average_precision_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

df = pl.read_csv("train.csv")
X = df.select(["f1", "f2", "f3"]).to_numpy()
y = df["target"].to_numpy()

X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

pipeline = Pipeline([("model", RandomForestClassifier(random_state=42))])
pipeline.fit(X_train, y_train)

scores = pipeline.predict_proba(X_valid)[:, 1]
print(average_precision_score(y_valid, scores))

with open("artifacts/model.pkl", "wb") as f:
    pickle.dump(pipeline, f)
```
