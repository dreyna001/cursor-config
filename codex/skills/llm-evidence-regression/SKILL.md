---
name: llm-evidence-regression
description: "Implement or review corrections to LLM evidence handling, output schemas, grounding guards, or quality evaluations while preserving supported facts and decisions. Use for these behavior changes and regressions, not unrelated LLM work or ordinary writing."
---

# Llm Evidence Regression

Correct a demonstrated failure class without hiding lost evidence, missed threats,
false alarms, or unavailable outputs. This workflow complements existing engineering
and domain guidance; it does not establish a new verdict policy or authorize model
calls, deployments, integrations, or external publication.

## Establish the boundary

Identify the actual source records, evidence roles, output contract, native consumer,
and expected behavior. Separate a bad model response from a parser/normalizer error,
a grounding error, and an evaluation error. Fix the responsible boundary rather
than relaxing the entire pipeline. Use runtime captures when available; keep the
raw failure and the prior baseline.

For schema, coercion, quoting, truncation or repair changes, read the corresponding
sections of [evidence contracts](references/evidence-contracts.md). For claims,
action states, source binding or partial-answer handling, read its claim/projection
sections. Read [balanced regression checks](references/balanced-regressions.md)
when choosing controls or reporting results.

## Make a bounded correction

- Express the fix through supplied schemas, values, records, relationships or a
  documented grammar. Fixture names and phrases are examples, not exceptions.
- Preserve supported information through parsing and repair. Known aliases may
  normalize losslessly; unresolved nonempty metadata needs visible validation or
  bounded repair, not deletion to obtain a pass.
- Keep factual uncertainty separate from an explicit capability refusal. Keep a
  source's missing record separate from proof that an action did not happen.
- Apply source-copy requirements to observations. Clearly prospective advice or
  investigation examples follow the task's advice policy; do not add a universal
  source-only advice rule or imply that a suggested tool is available or was used.
- For partial answers, retain a fact only if its source/entity/event/time binding
  survives. Revalidate the result; otherwise return the contract's visible fallback
  and preserve the raw response for review. Do not retain unchecked factual prose
  or invent a blanket prohibition on permitted nonfactual advice.
- Apply shared principles to affected implementations, checking each native
  boundary separately. Preserve intentional product differences and isolated
  dependency environments; do not require identical code across unrelated systems.

## Prove both rejection and retention

Pair the failing class with supported controls and varied examples. Include the
disposition classes relevant to the task, such as malicious, benign and unknown,
and check actual final decisions and retained evidence rather than scorer flags
alone. Rejection/unavailability is a separate outcome, never an implicit benign
decision. Preserve existing expected results; change an expectation only when the
supplied evidence or contract justifies it, with an explicit explanation.

Run focused checks and required native validation. Broaden only for affected
boundaries or unresolved risks. For complex binding changes, use an independent
bounded review when available and authorized. Stop grammar expansion when the
demonstrated class is corrected; record unresolved language limits and follow-ups.

## Report the result

State the reusable change, supported information retained, rejected controls,
remaining unavailable outputs and known limits. Distinguish raw proposals,
application acceptance, full schema/grounding validity, analytical quality and
provider failures. Label scripted repair, actual captured replay and new live
execution separately. A finite passing corpus does not establish general reasoning
correctness, production sensitivity, false-positive rates or prompt effectiveness.
