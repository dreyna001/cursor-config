---
name: implement-python-feature
description: Implement Python 3.12 features or runtime contract changes with minimal production-ready diffs.
---

# Implement Python Feature

Use this skill when adding or changing Python behavior.

## Out Of Scope

- Broad architecture redesign without explicit request.
- Infra-only changes with no Python behavior impact.

## Workflow

1. Read relevant files first.
2. Identify the smallest correct implementation.
3. Preserve existing conventions unless improvement is necessary and scoped.
4. Target Python 3.12 unless explicitly told otherwise.
5. Add type hints to new or modified functions and methods.
6. Add proportional docstrings for public modules, classes, functions, and methods.
7. Prefer stdlib and existing dependencies first.
8. If adding a dependency, justify why existing tools are insufficient.
9. Use structured logging in production paths.
10. Avoid print statements in production paths.
11. Use specific exceptions and actionable error messages.
12. Add or update tests for normal, edge, and failure paths.

## LLM Or External Call Paths

For LLM-driven or external-output paths:
- validate and normalize output into an explicit contract
- separate evidence from inference
- keep unknown values explicitly as `unknown`
- reject unsupported IDs or values via allowlist or validator
- use bounded retries with backoff
- handle parse failures explicitly
- preserve raw model response only for debugging or evidence workflows
- never log secrets, tokens, or credentials
- fail loudly on contract or configuration errors

## Runtime Contract Changes

If contract values change, update linked artifacts in the same change:
- runtime code
- tests
- README and deployment docs
- `.env.example` or `config.env.example`
- compose files or systemd units
- SAM, CloudFormation, or other infra templates
- smoke-test instructions or scripts

## Output

Return:
- what changed
- why
- dependencies added, if any
- verification steps and results