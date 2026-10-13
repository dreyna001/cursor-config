---
name: ml-packaging-and-inference
description: "Package traditional ML pipelines for deterministic inference, input validation, serialization, and batch scoring."
---
# Skill: ML Packaging And Inference

## When to use
- A trained model needs to be shipped into batch or real-time inference.
- Training-time feature logic must be preserved for production scoring.

## Inputs required
- Serialized model or pipeline artifact.
- Required input schema and output contract.
- Expected inference shape, volume, and throughput.

## Recommended approach
1. Package preprocessing and the model together so inference uses the same learned logic as training.
2. Validate the input schema before scoring and fail clearly on missing fields.
3. Keep batch scoring partition-friendly for large daily volumes.
4. Prefer partitioned CSV input and output for simple, portable batch paths unless another format is justified.
5. Separate raw input, prepared features, and scoring output artifacts so each stage is debuggable.

## Common pitfalls
- Re-implementing feature logic in a different inference code path.
- Scoring a huge daily dataset as one full in-memory job.
- Accepting malformed inference inputs and producing silent garbage output.

## Deliverables
- Inference entry point and schema contract.
- Batch or real-time scoring plan with volume assumptions.
- Stable output shape for downstream consumers.

## Minimal code pattern
```python
import pickle
import polars as pl

FEATURE_COLUMNS = ["f1", "f2", "f3"]
REQUIRED_COLUMNS = set(FEATURE_COLUMNS)

def score_partition(input_csv: str, output_csv: str, model_path: str) -> None:
    df = pl.read_csv(input_csv)
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"missing required columns: {sorted(missing)}")

    with open(model_path, "rb") as f:
        pipeline = pickle.load(f)

    features = df.select(FEATURE_COLUMNS).to_numpy()
    scores = pipeline.predict_proba(features)[:, 1]
    df.select(FEATURE_COLUMNS).with_columns(pl.Series("score", scores)).write_csv(output_csv)
```
