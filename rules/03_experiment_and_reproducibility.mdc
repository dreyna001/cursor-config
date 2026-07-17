---
description: Experiment hygiene, artifact tracking, and reproducibility expectations for ML work
alwaysApply: false
---

# Experiment And Reproducibility

- Set **fixed random seeds** where the library supports them.
- Keep parameters **config-driven** rather than scattered as hidden constants.
- Log or record the dataset version, feature set, split method, metrics, and produced artifacts for each meaningful run.
- Save the **trained model and preprocessing pipeline together** so reruns and inference use the same logic.
- Make reruns reproducible: the same code, config, data snapshot, and seed should reproduce materially similar results.
- Name artifacts clearly enough to recover the training inputs and evaluation context later.
- Prefer deterministic tests, fixtures, and sample data over ad hoc notebook-only experimentation.
