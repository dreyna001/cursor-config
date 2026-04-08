---
name: implement-python-feature
description: Implements or extends Python functionality with minimal production-ready changes in this repository. Use when adding features in onprem_service, onprem_rag, or onprem-llm-sdk, or when changing behavior tied to config.env, LLM_API_URL, LLM_MODEL_NAME, model identifiers, ports, paths, payload fields, or runtime contracts.
---

# Implement Python Feature

## Use This When
- Adding a new Python feature.
- Extending existing Python modules or services.
- Introducing or changing runtime contract values.

## Out of Scope
- Broad architecture redesign without explicit user request.
- Infra-only changes with no Python behavior impact.

## Workflow
1. Read relevant files first and identify the smallest correct implementation.
2. Preserve existing conventions unless improvement is necessary and scoped.
3. Add type hints to all new or modified functions and methods.
4. Add Google-style docstrings for all public modules, classes, functions, and methods.
5. Prefer Python standard library first; if adding a dependency, justify why stdlib is insufficient.
6. Use structured logging in production paths; avoid print statements.
7. Use specific exceptions and actionable error messages.
8. For LLM-driven analysis or output paths:
   - validate and normalize output into an explicit contract
   - separate direct evidence from inference
   - keep unknown values explicitly as "unknown"
   - reject unsupported IDs or values via allowlist or validator
   - use bounded retries with backoff for model or API calls
   - handle parse failures explicitly
   - preserve raw model response only for debugging or evidence workflows
   - never log secrets, tokens, or credentials
   - fail loudly on contract or configuration errors (no silent fallback)
9. If contract values change, update all linked artifacts in the same change:
   - runtime code
   - README and deployment docs
   - `.env.example` or `config.env.example`
   - compose files or systemd units
   - SAM, CloudFormation, or other infra templates
   - smoke-test instructions or scripts
   - tests that assert the contract
10. Add or update tests for non-trivial logic and cover normal, edge, and failure paths.

## Output
- What changed.
- Why.
- Dependencies added (if any) and why they were needed.
- Verification steps and results.
