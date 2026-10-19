# Incident investigation and response support

## Decision and loop

Decide what an alert/case establishes, what needs investigation, the supported
impact/scope, and the next justified analyst action. An analyst recommendation,
an approved response action, and a completed response action are different states.

`alert/case -> normalize -> evidence/retrieval -> assess alternatives -> optional
approved investigation -> reconcile -> analyst decision -> authorized handoff`

## Required behaviors

- Inventory the analyzer worker, case archive, portal Q&A, investigation adapters,
  and writeback separately. A worker's optional query capability does not mean
  chat can execute queries. Multi-turn synthesis is not a tool-execution loop.
- Preserve alert input, query results, external intelligence, past-case similarity,
  analyst assertions, and business context as distinct evidence classes.
- Lead the case view with a bounded assessment, supporting and conflicting evidence,
  unresolved questions, affected entities, and justified next steps. Separate model
  confidence from severity, asset impact, and analyst disposition.
- Make material case statements traceable to authorized retained sources. Existing
  citation-stripping contracts require a deliberate API/UI provenance change;
  simply displaying model-generated source numbers is not a safe fix.
- Retain current-case scope through history, attachments, retrieval, and follow-ups.
  A similar historical case is advisory context, not evidence of the current event.
- For optional searches, discover real fields, validate syntax and read-only policy,
  enforce budgets, preserve result provenance, and report disabled/failed/partial
  execution independently from no matching activity.
- Reconcile fresh evidence with previous assessments. Preserve old conclusions and
  their source versions, explain what changed, and invalidate stale action proposals.
- Define blast radius with measured identities and bounded coverage. Do not infer
  affected systems from indicator presence or a model confidence score alone.
- Keep actual business criticality, maintenance/authorization context, and ownership
  as sourced/configured inputs. Names such as admin or dc do not establish roles.
- Draft ticket/response packages with evidence, timeline, uncertainty, owner, and
  the proposed decision. Ticket creation, comments, containment, eradication,
  recovery, and external communication retain their respective explicit gates.

## Conditional capabilities

- A future agent loop needs a case-bound plan/action ledger, expected information
  gain, stop reasons, durable budgets, exact action approval, and cancellation.
  Do not enable execution inside an intentionally read-only chat endpoint.
- Case grouping needs evidence-backed relationships and analyst review; do not
  silently merge cases because embeddings or indicator values are similar.
- Analyst dispositions and feedback should record actor, source version, reason,
  and supersession; feedback never silently modifies global prompts or thresholds.
- Recurrence usually means reassessment on new case evidence or an approved
  monitoring policy, not copying the threat-hunting scheduler into alert triage.

## Acceptance examples

- New contradictory evidence changes the recommendation with an inspectable delta;
  old confidence is not presented as a current incident decision.
- Search unavailable versus complete search with zero matches remain distinguishable.
- Prior turns or attachments from another case cannot support this case's facts.
- Draft isolation commands cannot be presented as completed containment.
- Read-only chat refuses execution while retaining supported investigative guidance.
- Supported facts survive repair and normalization across each native product.

## Scope preservation

Review on-prem, AWS GovCloud, commercial AWS, and Azure in their own native
contexts. Preserve independent packages, partitions, identity, schemas, budgets,
and deployment gates. A shared principle is not permission to import production
code or state across products. First-pass analysis is not the full IR lifecycle.
