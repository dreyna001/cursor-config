---
description: Core engineering expectations for all changes in this repository
alwaysApply: false
---

# Core Engineering Standards

- **Scope:** implement what was asked; avoid expanding into unrelated files, “cleanup” passes, or new docs unless requested or required by the change.
- **Consistency:** follow conventions already present in the codebase and keep configuration, code, and docs aligned when behavior or contracts shift.
- **Reviewability:** small logical commits or clear separation of concerns; each line in a diff should support the stated goal.
- **Honesty about uncertainty:** if something is unknown or environment-dependent, say so and prefer configurable or documented behavior over guessing.
