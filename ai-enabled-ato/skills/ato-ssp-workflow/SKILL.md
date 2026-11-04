---
name: ato-ssp-workflow
description: "Apply ai-enabled-ato SSP evidence, field mapping, approval, runtime and export contracts when changing that app; not for other SSP products."
---

# ATO SSP workflow

Use only in `ai-enabled-ato`. Read current root `AGENTS.md` and the actual
mounted SSP workflow. Shared instructions remain in installed global skills:
`agentic-security-workflows` (SSP-authoring reference), `evidence-field-mapping`,
`report-export-parity`, and `llm-evidence-regression` when their boundaries change.

## Local contracts

- For evidence, proposals, review and exports, read current
  `docs/SSP_ROADMAP_AND_BACKLOG.md#regression-obligations`,
  `docs/APP_AI_WORKFLOW.md` and `docs/SSP_WORKSPACE_OPERATOR_GUIDE.md`.
  [Packaged regression obligations](references/ssp-regression-obligations.md)
  preserve the exact local safeguards without copying the future-work backlog.
- For generation, imports and synthetic setup, apply current
  `docs/PROJECT_CONTEXT.md#ssp-field-mapping` and the
  [field mapping snapshot](references/ssp-field-mapping.md). Component name
  identifies it, purpose describes function, placement describes its relationship
  to the authorization boundary. Preserve source/citation and accountability in
  supported fields/control text; invent no owner field and apply no blanket name
  filter. Prompt/input fixes do not authorize rewriting saved workspaces.
- For runtime/deployment changes, use the local runtime rule and
  [contract](references/runtime-deployment-contract.md). Keep schema-validated
  JSON configuration, secret references, explicit capability dependencies and
  inactive deployment placeholders; do not overwrite live customer settings.
- For production HTTP changes, read the
  [dated checkpoint](references/production-http-checkpoint.md) and reverify it.

Keep current-profile scope and existing authority/release gates. JSON, DOCX and
draft OSCAL carry saved revision/provenance/limits; no generic browser/PDF pattern
may impose a new SSP approval or unsupported format. Local checks do not establish
live RHEL, identity, database, TLS, backup/recovery or SME qualification.
The [full AGENTS snapshot](references/repository-agents.md) is historical context;
current app instructions and source remain authoritative.
