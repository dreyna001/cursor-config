---
description: Python 3.12 coding standards for Python source changes
globs: "**/*.py"
alwaysApply: true
---

# Python Coding Standards

- Target Python 3.12 unless explicitly instructed otherwise.
- Match existing module style: imports, naming, typing, logging, and error handling.
- Prefer explicit types on public APIs and non-obvious internals.
- Keep functions focused, cohesive, and testable.
- Use package imports; avoid root-relative import hacks.
- Prefer dataclasses or typed models for structured internal contracts.
- Avoid global mutable state.
- Avoid broad bare `except`; catch specific exceptions and handle or re-raise intentionally.
- Distinguish retryable failures from non-retryable failures.
- Use explicit timeouts for external calls.
- Keep docstrings proportional; avoid verbose comments for obvious code.
- Do not introduce metaprogramming, plugin registries, abstract factories, or generic frameworks unless required by the current task.