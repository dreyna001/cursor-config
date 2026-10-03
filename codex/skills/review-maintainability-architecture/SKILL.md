---
name: review-maintainability-architecture
description: "Review maintainability, architecture boundaries, stale code, observability, config hygiene, and docs gaps."
---
# Review Maintainability And Architecture

## Focus

- poor boundaries and hidden dependencies
- duplicated logic and fragile utilities
- god functions, deep nesting, magic values, and leaky abstractions
- dead or stale code, obsolete flags, zombie tests, and deprecated wrappers
- weak observability, unsafe defaults, and missing docs for non-obvious systems
- wrong abstraction boundaries and hard-to-replace bottlenecks

## Output

Return:
1. High-value refactors only
2. Dead or stale code to delete
3. Architecture concerns
4. Missing docs or operational needs
5. What to fix now vs later
