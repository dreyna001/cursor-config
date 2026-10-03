---
name: cybersecurity-prompt-engineering
description: "Design cybersecurity LLM prompts, schemas, repair prompts, and RAG-grounded analyst workflows."
---
# Cybersecurity Prompt Engineering

Use this skill when designing, editing, or reviewing cybersecurity-oriented LLM prompts that feed structured analysis, reporting, enrichment, or automation.

## Quick Start

Follow this sequence:

1. Define the operational task in plain terms.
2. Define the output contract before writing the prompt.
3. Separate direct evidence, advisory context, and inference.
4. Add explicit rules for what the model must not claim.
5. Constrain enums, IDs, formats, and platform-specific fields.
6. Specify strict response-shape rules.
7. Add repair behavior for parse, schema, or policy failures.
8. Define when to stop and escalate to human review.

If the prompt output is consumed by downstream code, keep the prompt, parser, validator, repair prompt, examples, tests, and docs in sync in the same change.

Apply the shared [LLM deterministic guardrails](../engineering-guidance/references/llm-deterministic-guardrails.md) at the actual provider request and downstream context, not only in prompt wording.

## Core Principles

- Keep `direct evidence`, `advisory context`, and `inference` separate.
- Treat KB text, runbooks, retrieved context, and analyst doctrine as guidance unless case evidence confirms them.
- Prefer deterministic, schema-oriented instructions over open-ended prose.
- Preserve provenance for grounded context when available.
- Use `unknown` for unsupported factual fields.
- Reject or suppress unsupported IDs, enum values, and schema fields.
- Fail loudly on parse, contract, or configuration errors.
- Do not silently degrade malformed output into downstream automation.

## Required Workflow

### 1. Define the task

State exactly what the model is being asked to do, such as:

- summarize incident triage findings
- normalize scanner output into a contract
- produce hunt pivots from observed artifacts
- generate detection content for a specific platform

Avoid vague task statements like "analyze this" when the output will drive decisions or automation.

### 2. Define the output contract first

Before writing or editing prompt text, specify:

- required fields
- optional fields
- allowed enum values
- allowed identifier formats
- `unknown` behavior
- empty-list behavior
- whether explanations are allowed
- whether citations or provenance are required

If the output is machine-consumed, instruct the model to emit only the contract shape.

### 3. Separate inputs by evidence class

Classify prompt inputs as:

- `Direct evidence`: alert payloads, logs, scan results, case artifacts, raw telemetry, supplied files
- `Advisory context`: KB entries, RAG snippets, runbooks, SOPs, ATT&CK notes, analyst doctrine
- `Inference`: conclusions derived from direct evidence

Advisory context may guide reasoning, but it must not be copied into evidence fields unless direct evidence supports it.

### 4. Add explicit non-fabrication rules

The prompt should explicitly forbid invention of:

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

Unsupported values must be dropped or marked `unknown` according to the contract.

### 5. Add validators and allowlists when applicable

When the domain supports it, constrain outputs with:

- enum allowlists
- platform field allowlists
- identifier regexes
- severity mappings
- supported CVE or CWE formats
- platform-specific query or rule schemas

Do not let the model emit "close enough" values that downstream systems cannot safely consume.

### 6. Define repair behavior

Use repair prompts only after:

- parse failures
- schema validation failures
- policy violations
- unsupported value emission

Repair instructions must correct structure or policy violations without adding unsupported facts.

### 7. Define fallback behavior

If validation cannot be satisfied, prefer explicit failure or human review over silent fallback.

## Structured Output Template

Use a section like this when strict output is required:

```text
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
```

## Evidence Separation Pattern

Prompt rules should explicitly state:

```text
Treat the inputs as three distinct classes:
- Direct evidence: facts present in the provided case data or artifacts
- Advisory context: retrieved or reference material that may guide reasoning
- Inference: conclusions derived from direct evidence

Advisory context may inform reasoning, but it must not be presented as direct evidence.
Do not copy retrieved or doctrinal claims into evidence fields unless the case data supports them.
If a conclusion cannot be supported by direct evidence, set the relevant field to "unknown" or omit it when the contract requires omission.
```

## Grounded Context Pattern

When using RAG, KB, or runbook context:

- label it as advisory context
- preserve provenance when available
- keep it tightly bounded to the task
- prefer small, high-signal context over large dumps
- instruct the model not to treat it as observed environment truth

Example instruction:

```text
You may use the retrieved operational context as guidance only.
Do not treat retrieved context as direct evidence from the case.
Do not copy retrieved claims into evidence fields unless the case data itself supports them.
```

## Repair Prompt Pattern

Use a repair prompt only after a concrete validation failure.

```text
Your previous response violated the required output contract.

Validation error:
<error here>

Rewrite the response so it matches the contract exactly.
Do not add new facts not supported by the provided evidence.
If a field cannot be supported, set it to "unknown" or an empty list as required.
Return valid JSON only.
```

Repair prompts should include:

- the invalid prior response
- the validation error
- the original contract
- an instruction to preserve evidence discipline

Repair prompts must not ask for a better guess.

## Domain Guidance

### Threat Hunting

- prioritize observable entities, pivots, hypotheses, and confidence
- separate hunt leads from confirmed findings
- avoid claiming host, user, or process activity not present in evidence
- constrain generated queries to the target platform schema

### Vulnerability Assessment

- separate observed scanner output from analyst interpretation
- constrain CVE, CWE, and severity fields to supported values
- avoid inventing exploitability, exposure, compensating controls, or asset context
- mark missing environmental details as `unknown`

### Incident Triage

- preserve the chain from evidence to conclusion
- separate facts, hypotheses, and recommended next steps
- avoid overstating attribution, impact, or scope
- clearly mark recommendations as recommendations, not findings

### Detection Engineering

- separate detection logic from threat narrative
- constrain query or rule output to the destination platform schema
- reject placeholders, fake field names, and invented telemetry sources
- suppress invalid query content instead of emitting partial nonsense

## Review Checklist

When reviewing a cybersecurity prompt, verify:

- the task is operationally clear
- the output contract is explicit
- evidence and advisory context are separated
- unsupported values are dropped or marked `unknown`
- grounded context is labeled and bounded
- repair behavior is explicit
- downstream consumers can safely parse the output
- the prompt does not encourage fabricated certainty

## Preferred Defaults

- prefer low-temperature or structured-output prompting for automation paths
- prefer concise instructions with explicit constraints
- prefer allowlists and validators for IDs and enums
- prefer human-review fallback over silent degradation
- prefer explicit parse and contract errors over best-effort coercion

## Avoid

- "use your best judgment" for required factual fields
- mixing evidence and runbook text in the same output section
- asking for confidence without defining what it applies to
- allowing free-form prose when a contract is required
- accepting malformed but "close enough" structured output
- silent fallback that hides validation failure
