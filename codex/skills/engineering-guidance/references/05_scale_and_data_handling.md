---
description: Large-scale data handling defaults for traditional ML pipelines and inference workloads
alwaysApply: false
---

# Scale And Data Handling

- Follow `01_ml_foundations` for dataframe and file-format defaults.
- Prefer **lazy execution** where appropriate, especially for large file scans and derived feature pipelines.
- Prefer **column pruning** and **early filtering** to reduce memory and I/O pressure.
- Avoid row-wise Python loops when vectorized, expression-based, or batch operations are available.
- Avoid designs that require the entire daily dataset to fit comfortably in memory.
- Prefer **incremental scoring**, **batch scoring**, and **windowed feature generation** when scale demands it.
- Explicitly separate **raw ingestion**, **feature generation**, **model input dataset**, and **scoring output** stages.
- Surface likely **compute**, **memory**, and **I/O bottlenecks** early in the design.
- Call out full-materialization steps and justify them when they cannot be avoided.
