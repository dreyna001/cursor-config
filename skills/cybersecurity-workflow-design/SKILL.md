---
name: cybersecurity-workflow-design
description: "Design bounded cybersecurity LLM workflow orchestration, validation, adapters, policy gates, approvals, and execution sequencing; use for multi-step workflow architecture, not standalone prompt authoring."
---
# Cybersecurity Workflow Design

Use this skill when designing, editing, or reviewing a cybersecurity workflow that may call an LLM, validate structured analysis, call tools, generate queries, or write back to downstream systems.

For prompt text, output schemas, RAG instructions, evidence wording, and repair prompts, use [Cybersecurity Prompt Engineering](../cybersecurity-prompt-engineering/SKILL.md). That skill owns the model-call contract; do not duplicate its prompt patterns here.

For agentic threat hunting, incident investigation, or SSP authoring, also use
[Agentic Security Workflows](../agentic-security-workflows/SKILL.md) and only its
matching use-case reference. It owns decision completeness, evidence review,
version-bound analyst UX, and source-backed capability/backlog reviews.

## Default Pattern

Use this bounded flow unless the use case clearly requires another shape:

    normalize input
    -> grounded context / prompt
    -> structured output
    -> parse
    -> validate
    -> optional repair
    -> policy check
    -> optional bounded tool execution
    -> summarize / write back

## Workflow

1. Define the operational task or backend capability.
2. Define direct evidence sources.
3. Define advisory context sources.
4. Define the structured output contract through the prompt-engineering skill.
5. Decide deterministic code vs LLM responsibility.
6. Define validators, allowlists, enum limits, ID formats, and `unknown` handling.
7. Define required tool adapters.
8. Define approval boundary and failure behavior.
9. Define repair behavior for parse, schema, or policy failures.
10. Add tests for prompt output, parsing, validation, policy, repair, and fallback behavior.

## Capability Scope And Delivery

- Plan by the backend capability being delivered; use autonomy levels only as a secondary label for control, risk, and governance.
- Deliver capabilities incrementally: grounded generation, validation, bounded read-only execution, summarization, then approval-gated writeback or actions.
- For a single-call workflow, keep intermediate context deterministic and in memory. Add persistence only when multi-step execution, replay, or audit requires it.
- Keep the default bounded and investigative, with human approval for consequential actions.

## LLM Call Boundary

- Use the prompt-engineering skill for every LLM step's task, evidence classes, output schema, prompt, and repair prompt.
- Apply [LLM boundaries](../cursor-rules/references/llm-boundaries.md) to user text, retrieved content, tool results, and model output.
- Keep prompts, parsers, validators, examples, tests, and documentation synchronized when a model-call contract changes.
- Keep authorization, budgets, policy decisions, and tool permissions outside the model.

## Validators And Allowlists

When applicable, constrain outputs with:

- enum allowlists
- platform field allowlists
- identifier regexes
- severity mappings
- supported CVE, CWE, ATT&CK, IOC, or asset formats
- platform-specific query or rule schemas
- destination-system schema validators
- policy allowlists and deny rules

Do not let the model emit “close enough” values that downstream systems cannot safely consume.

## Repair Boundary

- Trigger repair only after a concrete parse, schema, policy, or allowlist failure.
- Build repair prompts with the prompt-engineering skill.
- Re-run deterministic parsing, validation, and policy checks after repair.
- Limit repair attempts and preserve the failure reason for review.

## Fallback Behavior

- Prefer explicit failure or human review over silent fallback.
- Fail loudly on parse, contract, policy, or configuration errors.
- Do not silently degrade malformed output into downstream automation.
- Surface uncertainty clearly.
- Preserve invalid output or diagnostic metadata only when useful for debugging or review.

## Query And Tooling Rules

When the workflow generates queries, rules, commands, or tool inputs:

- tie each generated query or action to a specific hypothesis, unknown, or contradiction
- validate syntax and platform-specific policy before execution
- enforce read-only behavior unless writes are explicitly approved
- cap time range, cost, result count, and execution time
- reject placeholders, fake field names, and invented telemetry sources
- suppress invalid query content instead of emitting partial nonsense
- log enough metadata for audit and debugging

## Approval And Automation Rules

- Add approval gates before consequential writes or actions.
- Keep read-only, writeback, and action-taking behavior separate.
- Keep orchestration, prompt construction, validation, policy, and adapters distinct.
- Use deterministic policy checks before generated queries, updates, or actions execute.
- Return structured block reasons when policy denies execution.

## Review Checklist

When reviewing a cybersecurity workflow, verify:

- the operational task is clear
- each model call has an explicit contract owned by the prompt-engineering skill
- validators and allowlists exist outside the prompt
- repair behavior is explicit
- downstream consumers can safely parse the output
- adapters contain transport concerns only
- generated queries or actions are policy checked
- consequential actions have an explicit approval boundary
- fallback behavior is explicit and safe

## Preferred Defaults

- Prefer deterministic orchestration and explicit state transitions.
- Prefer allowlists and validators outside the model.
- Prefer human-review fallback over silent degradation.
- Prefer explicit parse and contract errors over best-effort coercion.
- Prefer one bounded LLM call over agentic multi-step behavior unless required.
- Prefer deterministic extraction and normalization in code when practical.

## Avoid

- “use your best judgment” for required factual fields
- accepting malformed but “close enough” structured output
- silent fallback that hides validation failure
- using the LLM for policy enforcement
- using the LLM to compensate for missing domain rules

## Autonomy Guidance

- grounded structured output only: Level 3
- validated read-only tool execution: entering Level 4
- bounded multi-step investigation: Level 4
- structured recommendations with approval-gated consequential actions: Level 5

Default cybersecurity target: Level 5, not Level 6.
