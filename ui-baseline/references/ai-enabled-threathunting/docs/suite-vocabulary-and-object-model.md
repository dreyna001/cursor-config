# Suite Vocabulary and Object Model

Version: 1.0.0 | Agreed: 2026-10-19

This is the shared product-language contract for the three workspaces. Identical
copies live at `docs/suite-vocabulary-and-object-model.md` in
`ai-enabled-threathunting`, `llm_notable_analysis`, and `ai-enabled-ato`.
It governs new and changed user-facing language. It does not introduce features,
change operational authority, or rename existing technical contracts.

## Product identity

- **Incident Response Workspace** (`llm_notable_analysis`): short name **Incident
  Response**; assistant **Incident Response Assistant**. Alert analysis, case
  investigation, and source-specific notable processing are capabilities within
  this product. The name does not imply automated containment or remediation.
- **Threat Hunting Workspace** (`ai-enabled-threathunting`): short name **Threat
  Hunting**; assistant **Threat Hunting Assistant**, if an interactive assistant
  is exposed. Hunts, hypothesis development, planning, and reporting remain
  capabilities within this product.
- **ATO Workspace** (`ai-enabled-ato`): short name **ATO**; assistant **ATO
  Assistant**. SSP drafting is the current capability; other authorization work
  may be introduced through separately scoped changes. Content approval is not
  a system authorization decision.

Use the full name in app branding, sign-in identity, and the HTML browser title.
Use short names in a suite app switcher or breadcrumb with clear product context.
Deployment platform, model provider, AI/LLM implementation, and user role do not
change product identity. All four Incident Response delivery variants use the
same name. Describe the actual available capabilities beside the name.

Retire these product aliases from current UI: Alert Analysis Portal, Notable
Analyst Portal, Threat Hunt Console, Analyst workspace as product branding,
SSP Drafting Portal, and ATO Evidence Analysis Portal.

## Product structure

- **Suite**: the collection of operational apps. No suite brand is selected yet.
- **App**: one operational product in the suite.
- **Workspace**: an interactive working environment in an app. Qualify scoped
  environments as **Hunt workspace** or **SSP workspace**. A scoped workspace is
  not another app, an authorization boundary, or a tenant by implication.
- **Portal**: reserve for a shared suite entry point if one is built. Do not use
  portal, console, and workspace interchangeably for an app.
- **Dashboard**: a summary page containing activity, status, or metrics.
- **Assistant**: the interactive AI capability. Use its product-specific name
  for headings and navigation; **Assistant** is sufficient in local descriptions.
- **Conversation**: an exchange of messages with an assistant. Use
  **Conversations**, **New conversation**, and **Conversation history** for
  navigation and retained exchanges. **Chat** may describe an interaction mode;
  it is not an alternative name for the assistant or the retained object.

## Shared objects and relationships

- **Source**: the originating system, document, record, or supplied material.
  Preserve source identity and provenance.
- **Evidence**: retained material used to support an assessment. Its presence
  alone does not imply validation, completeness, or human approval.
- **Citation**: a reference to a specific supporting record or passage. A valid
  citation does not by itself establish that the conclusion is correct.
- **Analysis**: examination and reasoning over information. Keep observation,
  inference, hypothesis, and proposed investigation distinguishable.
- **Finding**: a documented conclusion supported by evidence. It may be a draft
  or require review; the word does not imply an incident or a control deficiency.
- **Recommendation**: a proposed next step. It is not an executed action.
- **Workflow**: a defined process or sequence of steps.
- **Run**: one execution of a workflow. A retry or rerun is another execution
  only where the application's existing execution model establishes that fact.
- **Task**: an individual unit of work, with assignment or status only where
  those features exist.
- **Report**: a presentation of analysis, findings, evidence references, and
  recommendations. An SSP remains an SSP; not every document is a report.

Relationship rules:

1. A suite contains apps; an app exposes capabilities and working environments.
2. A workflow has runs; runs perform steps and may produce analysis and findings.
3. Findings cite supporting evidence; evidence retains its source provenance.
4. Recommendations may lead to tasks or approved actions; they do not execute
   themselves.
5. Conversations contain messages and may reference domain objects and sources.
6. Reviews and approvals apply to explicit objects or versions. A review of one
   artifact does not transfer approval to another artifact or a later version.

These are conceptual relationships, not a mandate for shared databases, parent
classes, identifiers, endpoints, or a new cross-app case-management layer.

## Domain objects

- **Alert**: a signal requiring examination. **Notable** remains appropriate for
  a source-specific notable record, such as a Splunk notable.
- **Case**: a bounded investigation record. An alert can be associated with a
  case; a case is not automatically an incident.
- **Incident**: an occurrence classified as an incident through the operational
  process. Do not relabel every alert or case as an incident because the app is
  named Incident Response Workspace.
- **Ticket**: a work-tracking record in an external or explicitly implemented
  ticketing system. **Closed Tickets** stays correct for synchronized closed
  tickets; do not rename it Closed Cases.
- **Hunt**: a scoped proactive investigation, with a hypothesis or intelligence
  input, plan, searches, evidence, and findings as supported by the product.
- **Hypothesis**: a proposition to investigate, not a supported conclusion.
- **Hunt plan**: proposed hunt questions, scope, and investigative steps. Plan
  approval authorizes only the defined actions and scope.
- **System**, **Control**, **SSP**, and **Authorization package**: distinct ATO
  domain concepts. An SSP describes a system and its control implementation;
  it is not an authorization decision or a complete authorization package.
- **Profile**: a named, versioned set of requirements or configuration. Qualify
  it where needed (for example, **SSP profile** or **deployment profile**).

## Actions, states, and dimensions

Use **Create**, **Save draft**, **Run**, **Cancel**, **Review**, **Approve**,
**Finalize**, **Export**, and **Archive** where the actual behavior matches.
Do not substitute Archive for Delete or Finalize for Export.

- **Review**: examine content or a proposed action. State what is reviewed.
- **Approve**: authorize a defined action or accept a specific result/version.
  Name the object: Approve plan, Approve SSP. Preserve permission and scope gates.
- **Finalize**: lock a specific version under the product's finalization rules.
  It does not imply external acceptance or system authorization.
- **Execution status**: progress of processing, such as Queued, Running,
  Completed, Failed, or Cancelled, only where supported.
- **Review status**: disposition of a particular review, such as Draft,
  Awaiting review, Approved, or Rejected, only where supported.
- **Severity**: assessed impact or seriousness.
- **Priority**: urgency or ordering of work.
- **Confidence**: certainty of an assessment, with its basis identified. Model
  confidence is not evidence strength, severity, priority, or human approval.

Completed does not mean Approved; Approved does not mean Authorized. A low
confidence result is not automatically a low severity result. Preserve existing
state machines, domain scales, and raw source values; document mappings before
harmonizing them. Never invent unavailable statuses for visual consistency.

## Configuration and records

- **Connection**: configured access to an external system, including applicable
  authentication and connectivity settings.
- **Data source**: a supplier of information, accessed through a connection,
  upload, or another supported ingestion path. One connection may serve multiple
  sources. Connectivity does not establish evidence quality or completeness.
- **Settings**: application behavior or preferences.
- **History**: revisions or previous activity for a named object.
- **Audit log**: attributable actions recorded for accountability. Conversation
  history and diagnostic logs do not become audit logs by relabeling them.

## Maintenance and compatibility

1. Read this guide before changing UI copy, assistant labels, help, report
   presentation, or user documentation. Use one term per meaning and one meaning
   per term. Qualify terms when their scopes differ.
2. Check the actual object and behavior before renaming it. Preserve evidence
   semantics, operational gates, domain distinctions, and supported capabilities.
3. Run `python3 scripts/check_suite_terminology.py` from the repository root after
   UI wording changes, plus the relevant frontend checks. The check detects known
   retired phrases and identity drift; it cannot prove semantic correctness.
4. For a shared vocabulary change, update this file in all three repositories
   with the same version and content in the same coordinated change. Record
   intentional local exceptions in `docs/suite-terminology-audit.md`, not by
   silently changing a shared definition. Compare file hashes to verify parity.
5. Existing API fields, schema enums, routes, storage keys, persisted titles,
   package names, deployment identifiers, and external source terminology are
   compatibility contracts. Change display text independently. Technical
   renaming requires explicit migration and compatibility planning.
6. Preserve historical design previews, dated evidence, frozen contracts, and
   old release records. They describe their original version. Apply the guide
   when those surfaces become active product content again.

## Change record

- **1.0.0 — 2026-10-19:** Established operational-function workspace names,
  product assistants, shared definitions, domain boundaries, state distinctions,
  compatibility rules, and the terminology-review workflow.
