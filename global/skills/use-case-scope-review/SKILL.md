---
name: use-case-scope-review
description: "Clarify a greenfield or new-use-case idea into a bounded MVP without forcing a shared architecture; not for existing-repo requirement shaping or 2-week implementation-block planning."
---
# Use Case Scope Review

Use this skill when:
- starting a new use case
- turning a vague idea into a bounded MVP without imposing a shared architecture
- checking whether a greenfield scope is too broad

For a 2-week implementation-block plan on an existing direction, use [scope and diff planning](../scope-and-diff-planning/SKILL.md). For unresolved correctness, compatibility, security, or safety choices, use [requirements shaping](../requirements-shaping-and-diff-planning/SKILL.md).

## Objective

Produce a scoped implementation plan for the current block only.
Do not impose a reusable framework, shared library, or generic architecture unless the prompt explicitly asks for one.

## Process

1. Define the exact problem being solved.
2. Name the primary user or operator.
3. Define the operational input.
4. Define the operational output.
5. List the minimum deterministic logic required.
6. Determine whether an LLM step is needed.
7. If yes, define the narrow purpose of the LLM step.
8. State what is explicitly out of scope.
9. Identify the smallest end-to-end demo slice.
10. List the main risks and unknowns.

## Output format

Return these sections:
- Goal
- In scope
- Out of scope
- Inputs
- Outputs
- Deterministic logic
- LLM use, if any
- External dependencies
- Risks
- Proposed 2-week slice

## Constraints

- Do not widen the scope to cover future roadmap items.
- Do not force cross-use-case reuse.
- Do not recommend shared code unless the user explicitly asks.
- Favor direct solutions over generalized platforms.
