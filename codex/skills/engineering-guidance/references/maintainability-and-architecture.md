# Maintainability And Architecture

- Keep boundaries clear, contracts strong, and dependencies explicit.
- Flag inconsistent patterns, fragile shared utilities, and weak sources of truth.

# Code Smells

- Flag god classes or functions, long methods, deep nesting, duplicated logic, magic values, leaky abstractions, boolean parameter explosion, hidden side effects, misleading comments, and overengineering.

- Assess responsibility boundaries and testability rather than imposing a fixed line-count limit. A small diff does not justify accumulating unrelated responsibilities in one module; extract a cohesive responsibility only when needed by the current change.

# Dead And Stale Code

- Flag unused functions, classes, imports, variables, unreachable branches, obsolete configs, stale feature flags, deprecated wrappers, zombie tests, and commented-out legacy logic.
- Prefer deleting dead code when it is proven unused and safe to remove.

# Operations And Architecture

- Review observability, config safety, deployment rollback hygiene, and documentation for non-obvious systems.
- Flag wrong abstraction boundaries, poor domain modeling, unclear trust boundaries, and hard-to-replace bottlenecks.
