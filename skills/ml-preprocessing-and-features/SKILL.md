---
name: ml-preprocessing-and-features
description: Build Polars-first preprocessing and feature flows for imputation, encoding, scaling, selection, and sklearn handoff.
---

# Skill: ML Preprocessing And Features

## When to use
- Raw data needs cleanup, feature generation, or model-ready transforms.
- You need a clear boundary between `Polars` preparation and sklearn modeling.

## Inputs required
- Raw feature columns and target column.
- Known numeric, categorical, text, or temporal fields.
- Any leakage-sensitive columns that must be excluded.

## Recommended approach
1. Do dataset shaping and feature generation in `Polars`.
2. Keep transforms batch-friendly and avoid row-wise Python loops.
3. Separate reversible cleanup from learned preprocessing such as imputation or scaling.
4. Hand off to sklearn only at the model boundary and keep that conversion late and narrow.
5. Put learned preprocessing inside a pipeline so training and inference stay aligned.

## Common pitfalls
- Fitting imputers or encoders before the train split.
- Mixing feature engineering logic across notebooks, training code, and inference code.
- Converting to pandas too early and losing the scale benefits of `Polars`.

## Deliverables
- Clean feature list and dropped-column list.
- Reusable feature engineering logic.
- A pipeline-ready handoff into sklearn preprocessing and modeling.

## Minimal code pattern
```python
import polars as pl
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

lf = pl.scan_csv("train.csv").with_columns(
    (pl.col("amount") / pl.col("tenure_days").clip(lower_bound=1)).alias("amount_per_day")
)

feature_df = lf.select(["amount_per_day", "age", "segment"]).collect()
X = feature_df.to_numpy()

preprocessor = ColumnTransformer(
    transformers=[
        ("num", Pipeline([("imputer", SimpleImputer()), ("scaler", StandardScaler())]), [0, 1]),
        ("cat", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("ohe", OneHotEncoder(handle_unknown="ignore"))]), [2]),
    ]
)
```
