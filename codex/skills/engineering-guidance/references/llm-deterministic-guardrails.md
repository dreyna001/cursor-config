---
description: Deterministic guardrails for LLM analysis, structured output, and parsing
alwaysApply: false
---

# LLM Analysis and Output Guardrails

- Separate **direct evidence** (case/alert/artifact data), **advisory context** (KB, RAG, runbooks, doctrine), and **inference**. Do not let retrieved or instructional text become claimed observations unless the case data supports it.
- Prefer explicit **output contracts** (required keys, allowed values, `unknown` for missing facts). Downstream automation must not rely on prose outside the contract.
- **Parse → validate → repair (optional) → fail or degrade explicitly.** Do not silently accept malformed JSON or policy violations for automated paths.
- Prefer **low temperature** and schema-oriented instructions where repeatability matters; document when free-form output is intentional.
- **Allowlists and validators** (e.g. technique IDs, enums) belong in code or versioned data, not only in prompt prose.
- Preserve **raw model output** or clear metadata when humans must review failures; avoid dropping diagnostic text without a structured reason field.
- When the selected provider supports strict structured outputs, send the supported response schema through the API rather than relying on prompt text or JSON mode alone. Derive it from the application contract, constrain context-specific choices where useful, and retain semantic validation plus explicit refusal/truncation handling. A valid schema or citation does not establish factual correctness.
- Project cross-field invariants into supported native schema variants where feasible, such as requiring nonempty evidence for positive claims. Test generated schemas against valid and invalid combinations, and run bounded provider contract checks before claiming provider compatibility; keep application validation authoritative.
- Let application code own durable identifiers and derivable relationships. Models may select bounded context-local labels resolved through an immutable request mapping; reject unknown or out-of-context labels. Preserve query references for zero-result searches and scoped negative findings.
- Pass relevant prior structured assessments with their supporting records when a downstream step depends on earlier investigation work. Label assessments as interpretations, preserve provenance and limitations, and fit the whole handoff within existing evidence and context budgets.
- Measure first-pass schema and grounding validity separately from eventual repair success and analytical quality. Use observed workflow outputs for evaluations; scripted fixtures test deterministic behavior and cannot establish live-model quality. Record provider/model settings, precision/recall where labels support them, unsupported claims, repair rate, and cost within an explicitly bounded evaluation.
- Compute counts and observed time bounds in application code when they are derivable from retained evidence. Distinguish the approved search interval, point-event timestamps, sample completeness, and demonstrated telemetry continuity; endpoint timestamps alone never establish continuous coverage. Reproduce observed factual overclaims with bounded live evaluations and keep general analytical quality unproven until representative judgments support it.
