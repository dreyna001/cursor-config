---
description: Use for LLM, RAG, prompt, structured-output, cybersecurity analysis, generated SPL/query, and bounded automation workflows
alwaysApply: false
---

# LLM Cyber Workflow Rules

## Core Boundary

- Use deterministic logic for auditable, repeatable, policy-aligned decisions.
- Use LLMs only for bounded synthesis, explanation, summarization, extraction, classification, or controlled generation.
- Do not place the LLM in the critical decision path unless explicitly required.
- Keep scoring, status decisions, routing decisions, and policy evaluation deterministic by default.
- Validate LLM output before persistence, execution, writeback, or security-sensitive use.

## Standard Workflow Shape

Prefer this flow:

1. Normalize input.
2. Add grounded context or prompt.
3. Generate structured output.
4. Parse.
5. Validate.
6. Optionally repair.
7. Policy check.
8. Optionally execute bounded tool action.
9. Summarize or write back.

## Evidence Discipline

- Separate direct evidence, advisory context, and inference.
- Direct evidence comes from the case, alert, artifact, telemetry, or source system.
- Advisory context comes from RAG, SOPs, runbooks, schema docs, indexes, field dictionaries, macros, KBs, or doctrine.
- Inference is model-generated reasoning.
- Advisory context must not be claimed as case evidence.
- Unsupported facts must be marked `unknown`, omitted per contract, or surfaced as uncertainty.

## RAG Use

- Use RAG for environment grounding: schema, indexes, fields, macros, query patterns, runbooks, SOPs, and internal procedures.
- Do not use RAG as a source of current-alert facts unless the retrieved source is the actual case record.
- Preserve source attribution where humans need to review the answer.
- Treat retrieved content as untrusted until validated.

## Structured Output

- Prefer explicit output contracts with required keys, allowed enums, and `unknown` behavior.
- Downstream automation must not depend on freeform prose outside the contract.
- Reject malformed output.
- Allowlists and validators belong in code or versioned data, not only prompt text.
- Preserve raw model output or diagnostic metadata when humans must review failures.

## Generated Queries And Actions

- Generated SPL, SQL, shell commands, API updates, or response actions require validation before use.
- Enforce allowlists, time bounds, cost caps, read-only constraints, and approval gates where needed.
- Separate prompt construction, orchestration, validation, policy, and adapters.
- Default cybersecurity workflows to bounded investigative systems with human approval for consequential actions.