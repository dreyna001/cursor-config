# ML Foundations

- Treat this stack as **traditional ML** by default: tabular workflows and classical models, not deep learning unless explicitly requested.
- Prefer the **simplest production-ready solution** that can meet the need.
- Start with **baseline models** before introducing more complex candidates.
- Prefer **`scikit-learn` first** unless there is a clear reason to use another training library.
- Prefer the existing dependency set and the standard library; do not introduce novel ML dependencies without justification.
- Default dataframe engine is **`Polars`**.
- Keep examples **`Polars`-first**, not pandas-first.
- Avoid pandas unless a library forces it at a **narrow boundary**.
- Default input and output examples use **CSV** for simplicity and portability.
- If using Parquet, Delta, or another format, explain the concrete scale, performance, schema, or integration reason.
- Write code that is modular, documented, testable, and typed where practical.
- Prefer solutions that remain workable for **batch-oriented** and **streaming-friendly** processing as data volume grows.
