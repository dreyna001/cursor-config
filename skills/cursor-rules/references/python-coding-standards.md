---
description: Python 3.12 style and conventions for this repository
globs: "**/*.py"
alwaysApply: true
---

# Python Coding Standards

- Target **Python 3.12** syntax, typing behavior, stdlib APIs, tests, and commands unless the user explicitly asks for another version.
- Match **existing module style**: imports, naming, typing, and error-handling patterns in the touched package (`onprem_service`, `onprem_rag`, `onprem_llm_sdk`, etc.).
- Prefer **explicit types** on public APIs and non-obvious internals; keep helpers focused and testable.
- Use package imports; avoid root-relative import hacks.
- Prefer dataclasses or typed models for structured internal contracts.
- Avoid global mutable state.
- **Dependencies:** add or pin only what the change needs; prefer stdlib or existing stack choices.
- **No broad bare `except`:** catch specific exceptions; log and re-raise or handle with a documented outcome.
- Distinguish retryable failures from non-retryable failures.
- Use explicit timeouts for external calls.
- Keep **docstrings** proportional to project norms—avoid verbose commentary on obvious code; preserve useful existing comments.
- Do not introduce metaprogramming, plugin registries, abstract factories, or generic frameworks unless required by the current task.
