---
name: agentic-security-workflows
description: "Design or review agentic threat hunting, incident investigation, or evidence-grounded SSP authoring; apply shared evidence, scope, approval, completeness, and analyst UX rules with the matching use-case reference."
---

# Agentic Security Workflows

Use for capability reviews, implementation requirements, and workflow changes in
threat hunting, incident investigation, and SSP authoring. These are engineering
instructions, not prompts to insert wholesale into an application's model.
Do not use for ordinary chat, unrelated security review, or authority decisions.

## Route first

1. Read repository instructions and identify the active product, configuration,
   execution path, human decision, and current delivery scope.
2. Load only the matching reference:
   - [Threat hunting](references/threat-hunting.md): proactive hypothesis testing.
   - [Incident response](references/incident-response.md): alert/case investigation.
   - [SSP authoring](references/ssp-authoring.md): system documentation and review.
3. Reuse [workflow design](../cybersecurity-workflow-design/SKILL.md) for execution
   architecture, [prompt engineering](../cybersecurity-prompt-engineering/SKILL.md)
   for model contracts, and [approval policy](../cybersecurity-approval-policy-gates/SKILL.md)
   for consequential actions. Do not duplicate their implementations.
4. Verify current source. Distinguish implemented, optional/configuration-gated,
   parked, not found in reviewed sources, intentional boundary, and unknown.
   Record installed and live behavior only when actually observed.

## Core rules

- Start with the user's decision and a bounded question. Define the evidence
  required to answer it before adding models, agents, tools, or UI steps.
- Discover actual schemas and source capabilities. Track available time windows,
  usable fields, permissions, retrieval outcomes, truncation, and context omission.
  A configured connector or a successful query is not complete coverage.
- Give every material conclusion resolvable, authorized source references. Keep
  source observations, interpretation, hypotheses, proposed actions, and human
  decisions distinct. Advisory knowledge and prior chat are not new case facts.
- Correlate with source-supported identity, scope, and time keys. Record ambiguous
  identifiers, conflicts, event time versus collection time, and alternatives.
  Shared names or overlapping timestamps do not establish attribution or cause.
- Distinguish no matching activity in a completed bounded search from missing
  telemetry, a failed search, and evidence that was not reviewed. For documents,
  distinguish absent documentation from a control not being implemented.
- Measure semantic completeness independently of schema/citation validation.
  Preserve responsive supported facts and counterevidence through selection,
  compression, repair, synthesis, and export. An empty but valid answer can fail.
- Keep full evidence inspectable while grouping material observations into useful
  answers. More records, findings, citations, calls, or agents are not quality.
- Select the next action by the unresolved question and expected information gain.
  Stop on answered scope, exhausted useful leads, missing prerequisites, cancellation,
  or approved bounds. Do not generate arbitrary queries to appear thorough.
- Enforce identity, tenancy/ownership, allowed tools, scope, time, rows, bytes,
  concurrency, cost, and cancellation outside the model. Do not reset accounting
  on recovery or silently replay work whose external outcome is unknown.
- Bind approvals to the exact displayed, saved version and relevant configuration.
  Resolve unsaved edits and stale revisions before approval. A conversational
  instruction does not grant broader scope or authorize a consequential action.
- Preserve existing product approval gates. Fewer UI actions may combine existing
  transitions only when exact-version checks and server enforcement remain.
- Make intake short, show a readable scope/change preview, and provide one clear
  next action. Use ordinary controls for ordinary edits; JSON and engine metadata
  belong in advanced inspection. Keep consequential coverage gaps visible.
- Continue conversations with the same authorized object and source versions.
  Scope expansion, changed evidence, or stale proposals require the existing
  refresh/review boundary; prior assistant assertions never become evidence.
- Reuse existing adapters, profiles, provenance, and state. Do not replace a working
  orchestrator or activate parked paths merely to call the product agentic.
- Add recurrence, persistent baselines, new connectors, or writeback only when the
  use case needs them. Define ownership, expiry, scope, drift checks, failure
  handling, and cost limits before enabling automation.

## Review artifact

When asked for an applied review without a prose report, write a repository-native
JSON implementation backlog. Preserve existing queues and link the artifact once
from the repository entrypoint. Use these fields:

- `schema_version`: `1`; `use_case`: `threat_hunting`, `incident_response`, or
  `ssp_authoring`; `review_date`: ISO date; `source_revision`: reviewed Git HEAD;
  `review_level`: `source_only`, `synthetic`, or `live`; `objective`: decision served.
- `variants`: `{id, root}` for each separately reviewed product. Readiness and
  configuration do not transfer between variants.
- `boundaries`: preserved scope and authorization constraints.
- `evidence`: `{id, variant, kind, path, anchor}`, with repository-relative paths
  and an exact source substring. `kind` is `source` or `recorded_evaluation`.
- `capabilities`: `{id, status, assessment, evidence_ids}`. Status is `implemented`,
  `partial`, `configuration_gated`, `parked`, `intentional_boundary`, `not_found`,
  or `unknown`. Qualify `not_found` to the actual reviewed surface.
- `work_items`: `{id, priority, type, status, capability_id, problem, recommendation,
  acceptance, evidence_ids, depends_on}`. Priority is `P1`, `P2`, or `P3`; type is
  `defect`, `ux`, `capability`, or `verification`; status is `proposed`,
  `requires_scope_decision`, or `verification_required`. Keep scope extensions
  separate from demonstrated defects. Acceptance must describe observable behavior.
- `limits`: unverified runtime, visual, model-quality, and deployment claims.

Validate with the packaged source-reference checker:

```bash
python3 <skill-root>/scripts/validate_review.py --repo <repository> <review.json>
```

The checker establishes artifact structure, source-anchor resolution, references,
and dependency consistency. It does not establish semantic accuracy or implemented
behavior. Never mark proposed acceptance criteria as passing tests.

## Verification

- For evidence/contract changes use [LLM evidence regressions](../llm-evidence-regression/SKILL.md):
  pair unsupported-claim rejection with supported-fact and decision retention.
- Check source-to-UI/export fidelity, partial/failure outcomes, stale approvals,
  dirty edits, recovery, and cancellation where the changed boundary requires it.
- Browser evidence is required for visual/interaction findings. If unavailable,
  label conclusions source-based and leave visual/accessibility behavior unverified.
- Report executed checks and their limits. A prior evaluation is historical
  evidence, not a newly executed test or a general accuracy estimate.
