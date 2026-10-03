---
name: cybersecurity-workflow-design
description: "Design cybersecurity LLM workflows and prompts with grounded context, structured contracts, validation, adapters, and approval gates."
---
# Cybersecurity Workflow Design

Use this skill when designing, editing, or reviewing a cybersecurity workflow that may use an LLM, generate structured analysis, produce prompts, call tools, generate queries, or write back to downstream systems.

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
4. Define the structured output contract before writing prompts.
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

## LLM Step Design

For each LLM step, define:

- purpose
- upstream deterministic facts
- what the model may produce
- what the model must not decide or invent
- output schema
- validation rules
- fallback behavior
- prompt draft

## Prompt Engineering Rules

- State the task operationally; avoid vague instructions like “analyze this” when output drives decisions or automation.
- Define the output contract before prompt text.
- Prefer deterministic, schema-oriented instructions over open-ended prose.
- If output is machine-consumed, require only the contract shape.
- Constrain enums, IDs, formats, platform fields, and allowed values.
- Require strict response-shape rules.
- Do not rely on prompt text alone for safety; use validators and policy gates in code.
- Keep prompt, parser, validator, repair prompt, examples, tests, and docs synchronized when output contracts change.

## Structured Output Contract

Before prompt implementation, define:

- required fields
- optional fields
- allowed enum values
- allowed identifier formats
- `unknown` behavior
- empty-list behavior
- whether explanations are allowed
- whether citations or provenance are required
- whether markdown is allowed
- whether freeform text outside the contract is allowed

## Structured Output Template

Use this pattern when strict output is required:

    Return valid JSON only.

    Follow this contract exactly:
    - required fields: <list>
    - optional fields: <list>
    - allowed values: <list>
    - allowed identifier formats: <list>
    - if evidence is missing, use "unknown"
    - if no items are supported, return an empty list where required
    - do not invent IDs, entities, timestamps, hosts, users, tools, or findings
    - do not include markdown
    - do not include explanatory text outside the JSON object

## Evidence Discipline

- Separate direct evidence, advisory context, and inference.
- Direct evidence comes from the case, alert, artifact, telemetry, source system, supplied file, scanner output, or raw log.
- Advisory context comes from RAG, SOPs, runbooks, schemas, indexes, field dictionaries, macros, KBs, ATT&CK notes, analyst doctrine, or reference material.
- Inference is model-generated reasoning derived from direct evidence.
- Advisory context may guide reasoning, but it must not be presented as direct evidence.
- Do not copy retrieved or doctrinal claims into evidence fields unless case data supports them.
- Unsupported facts must be `unknown`, omitted per contract, or surfaced as uncertainty.

## Explicit Non-Fabrication Rules

Prompts must forbid invention of:

- IDs
- hosts
- users
- timestamps
- tools
- processes
- findings
- severities
- asset context
- exploitability claims
- telemetry sources
- ATT&CK mappings
- CVEs, CWEs, IOCs, or vulnerabilities
- source evidence

Unsupported values must be dropped or marked `unknown` according to the contract.

## RAG And Grounded Context Rules

- Use RAG for environment grounding: schemas, fields, indexes, macros, SOPs, runbooks, query patterns, and internal procedures.
- Do not use RAG as current-case facts unless the retrieved source is the actual case record.
- Label RAG, KB, and runbook content as advisory context.
- Preserve provenance when available.
- Prefer small, high-signal context over large dumps.
- Treat retrieved content as untrusted until validated.
- Instruct the model not to treat retrieved context as observed environment truth.

## Grounded Context Prompt Pattern

Use this pattern when retrieved context is included:

    You may use the retrieved operational context as guidance only.
    Do not treat retrieved context as direct evidence from the case.
    Do not copy retrieved claims into evidence fields unless the case data itself supports them.

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

## Repair Behavior

Use repair prompts only after concrete failures:

- parse failure
- schema validation failure
- policy violation
- unsupported value emission
- invalid enum, ID, field, or platform syntax

Repair instructions must correct structure or policy violations without adding unsupported facts.

## Repair Prompt Pattern

Use this pattern only after validation failure:

    Your previous response violated the required output contract.

    Validation error:
    <error here>

    Rewrite the response so it matches the contract exactly.
    Do not add new facts not supported by the provided evidence.
    If a field cannot be supported, set it to "unknown" or an empty list as required.
    Return valid JSON only.

Repair prompts should include:

- invalid prior response
- validation error
- original contract
- evidence-discipline instruction

Repair prompts must not ask for a better guess.

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

## Domain Guidance

### Threat Hunting

- Prioritize observable entities, pivots, hypotheses, and confidence.
- Separate hunt leads from confirmed findings.
- Avoid claiming host, user, process, or network activity not present in evidence.
- Constrain generated queries to the target platform schema.
- Tie each pivot to evidence or an explicit hypothesis.

### Vulnerability Assessment And Management

- Separate observed scanner output from analyst interpretation.
- Constrain CVE, CWE, package, version, severity, and exploitability fields to supported values.
- Avoid inventing exploitability, exposure, compensating controls, affected assets, or environmental context.
- Mark missing environmental details as `unknown`.

### Incident Triage

- Preserve the chain from evidence to conclusion.
- Separate facts, hypotheses, and recommended next steps.
- Avoid overstating attribution, impact, blast radius, or scope.
- Clearly mark recommendations as recommendations, not findings.

### Detection Engineering

- Separate detection logic from threat narrative.
- Constrain query or rule output to the destination platform schema.
- Reject placeholders, fake field names, invented telemetry sources, and unsupported macros.
- Validate generated SPL, SQL, Sigma, YARA, or platform-specific rules before use.

### Security Reporting

- Separate evidence-backed findings from interpretation.
- Avoid overstating confidence.
- Preserve source traceability where humans need review.
- Use `unknown` for unsupported factual fields.

## Review Checklist

When reviewing a cybersecurity workflow or prompt, verify:

- the operational task is clear
- the output contract is explicit
- evidence and advisory context are separated
- unsupported values are dropped or marked `unknown`
- grounded context is labeled and bounded
- validators and allowlists exist outside the prompt
- repair behavior is explicit
- downstream consumers can safely parse the output
- generated queries or actions are policy checked
- the workflow does not encourage fabricated certainty
- fallback behavior is explicit and safe

## Preferred Defaults

- Prefer low-temperature or structured-output prompting for automation paths.
- Prefer concise instructions with explicit constraints.
- Prefer allowlists and validators for IDs and enums.
- Prefer human-review fallback over silent degradation.
- Prefer explicit parse and contract errors over best-effort coercion.
- Prefer one bounded LLM call over agentic multi-step behavior unless required.
- Prefer deterministic extraction and normalization in code when practical.

## Avoid

- “use your best judgment” for required factual fields
- mixing evidence and runbook text in the same output section
- asking for confidence without defining what it applies to
- allowing freeform prose when a contract is required
- accepting malformed but “close enough” structured output
- silent fallback that hides validation failure
- using RAG as proof of current-case facts
- using the LLM for policy enforcement
- using the LLM to compensate for missing domain rules

## Autonomy Guidance

- grounded structured output only: Level 3
- validated read-only tool execution: entering Level 4
- bounded multi-step investigation: Level 4
- structured recommendations with approval-gated consequential actions: Level 5

Default cybersecurity target: Level 5, not Level 6.
