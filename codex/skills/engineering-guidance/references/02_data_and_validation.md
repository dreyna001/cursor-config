# Data And Validation

- Never fit preprocessors, encoders, imputers, selectors, or resamplers on the **full dataset before the split**.
- Prevent **target leakage**, temporal leakage, and train-test contamination at every stage.
- Choose the split strategy to match the problem type and data-generating process.
- Use **time-aware splits** for temporal data; do not shuffle away ordering that matters.
- Use **stratification** for classification when it is valid and materially improves split quality.
- Run cross-validation only on the **training portion** of the data.
- Keep the final **holdout test set untouched** until final evaluation.
- Apply resampling, threshold tuning, and feature selection only inside the correct training or CV boundary.
- When data is grouped by user, device, account, or case, split in a way that prevents entity leakage across folds.
