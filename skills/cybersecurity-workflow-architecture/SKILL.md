---
name: cybersecurity-workflow-architecture
description: Design bounded cybersecurity LLM workflows with schemas, grounding, validators, adapters, and approval gates.
---

# Cybersecurity Workflow Architecture

Use this skill when designing, reviewing, or implementing a cybersecurity LLM workflow that may produce structured analysis, generate queries, call tools, or write back to downstream systems.

## Quick Start

Follow this sequence:

1. Define the backend capability being added.
2. Define the structured output contract before editing prompts.
3. Separate direct evidence, advisory context, and inference.
4. Decide what belongs in deterministic code vs the LLM.
5. Add validators and policy gates before any generated query or action can run.
6. Keep integrations behind tool adapters.
7. Add approval gates before consequential writes or actions.
8. Deliver incrementally and map the result to an autonomy level only after the capability is defined.

## Preferred Architecture Pattern

Default to this bounded flow:

`normalize input -> grounded context/prompt -> structured output -> validate/policy-check -> optional bounded tool execution -> summarize/write back`

Use this pattern unless the use case clearly requires a different shape.

## Required Design Rules

- Plan **by backend capability**, not by abstract "agent" labels.
- Use autonomy levels as a **secondary** label for control, risk, and governance.
- Keep **orchestration**, **LLM contract/prompt building**, **tool adapters**, and **policy/validation** as distinct concerns.
- Prefer deterministic extraction and normalization in code when possible.
- Use **RAG for environment grounding** such as schema, fields, indexes, macros, SOPs, and query patterns, not for current-case facts.
- Keep current-case facts grounded in the alert, artifacts, or other direct evidence.
- Prefer explicit output schemas, enums, allowlists, and `unknown` handling over free-form prose.
- Use repair prompts only after concrete parse, schema, or policy failures.

## Capability Design Checklist

For each new workflow or enhancement, define:

- the exact backend capability being added
- the input evidence sources
- the structured output contract
- the validators and allowlists
- the tool adapters required
- the approval boundary
- the failure and fallback behavior
- the tests needed for the change

## Query And Tooling Guidance

When the workflow generates queries or tool inputs:

- tie each query or action to a specific hypothesis, unknown, or contradiction
- validate syntax and platform-specific policy before execution
- enforce read-only behavior unless writes are explicitly approved
- cap time range, cost, result count, and execution time
- log enough metadata for audit and debugging

## Single-Call Guidance

If the workflow is a single bounded LLM call:

- keep any intermediate case context in memory
- parse the LLM JSON response in code
- do not add persistence unless multi-step execution, replay, or audit requires it

## Maturity Overlay

Use this rough mapping:

- grounded structured output only: Level 3
- validated read-only tool execution: entering Level 4
- bounded multi-step investigation: Level 4
- structured recommendations with approval-gated consequential actions: Level 5

Default target for current cybersecurity workflows: **Level 5**, not Level 6.
