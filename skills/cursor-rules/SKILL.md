---
name: cursor-rules
description: "Use for code design, implementation, or review when this collection's Python, ML, API, cloud, security, LLM, frontend, or documentation standards apply; read only matching references."
---

# Engineering Guidance

For UI/UX work, start at the permanent local baseline:
`$HOME/.agents/ui-baseline/README.md` (Windows:
`%USERPROFILE%\.agents\ui-baseline\README.md`). On the current workstation,
open [Windows](C:/Users/Daniel.Reyna/.agents/ui-baseline/README.md) or
[WSL](/home/dreyna/.agents/ui-baseline/README.md).
If absent, install the versioned `ui-baseline/` bundle from `cursor-config`;
the app's `docs/suite-ui-standard.md` release copy is the fallback. No GitHub
sign-in is required to read the installed reference. This is the single entry
point for shared rules, adaptation, visual examples, exceptions and validation.
Preserve newer approved login/account, sidebar, typography, colors, layouts,
features and intended behavior; older HTML or guidance cannot override them.

Approved shared UI changes are not complete until the versioned baseline,
its visual companion, all three apps (six frontends), this configuration
repository's reference bundle, and the permanent local baseline are synchronized.
Follow the baseline's “Keeping one baseline” procedure, record app-specific
exceptions and validation, and preserve newer approved behavior and styling.
If any part cannot be updated or verified, report the remaining drift explicitly.

## Cloud IaC policy

Use Terraform exclusively for all new or modified cloud resources, across all
providers. Do not add or extend other IaC formats or provision resources through
console instructions or application scripts. Apply the Terraform cloud deployment
standard and the existing documented root; treat other checked-in templates as
legacy. Builds and artifact publication may use their existing tools.

For cloud development, apply the [Terraform cloud deployment standard](../terraform-cloud-deployment-standard/SKILL.md), including its create-or-reference contract for required deployable prerequisites. Preserve the established stack and customer ownership; document qualified platform exceptions.

Use this skill as a conditional router for the engineering standards in `references/`. Read only the reference files relevant to the requested change and the systems it touches. Do not turn the collection into a checklist for unrelated work. Subagent routing stays in the always-on delegation rule.

## Reference index

For general code changes, use the applicable parts of [core engineering](references/core-engineering.md), [correctness and testing](references/correctness-and-testing.md), [maintainability and architecture](references/maintainability-and-architecture.md), [reliability and performance](references/reliability-and-performance.md), and [requirements confidence](references/requirements-confidence.md). For interface layout, navigation, content hierarchy, or editing-state decisions across UI stacks, read [UI/UX organization](references/ui-ux-organization.md).

For user-facing wording and first-use task clarity, use [self-explanatory UI](../self-explanatory-ui/SKILL.md).

For APIs, persistence, queues, or distributed behavior, read [API, data, and distributed systems](references/api-data-and-distributed.md). For Python code, read [Python coding standards](references/python-coding-standards.md) after checking the target project's declared and deployed Python versions; preserve its established stack and conventions. For React, read [React](references/react.md). When frontend changes touch authentication, credential forwarding, browser persistence, uploads/previews or untrusted content rendering, also read [security](references/security.md) and its matching framework reference.

For traditional ML standards, read only the relevant parts of [ML foundations](references/01_ml_foundations.md), [data and validation](references/02_data_and_validation.md), [experiments and reproducibility](references/03_experiment_and_reproducibility.md), [delivery and reporting](references/04_delivery_and_reporting.md), and [scale and data handling](references/05_scale_and_data_handling.md).

For procedural ML work, use the matching dedicated skill: [problem framing](../ml-problem-framing/SKILL.md), [EDA](../ml-eda/SKILL.md), [preprocessing and features](../ml-preprocessing-and-features/SKILL.md), [baselines](../ml-baselines/SKILL.md), [model training](../ml-model-training/SKILL.md), [imbalance](../ml-imbalance/SKILL.md), [hyperparameter tuning](../ml-hyperparameter-tuning/SKILL.md), [evaluation](../ml-evaluation/SKILL.md), [error analysis](../ml-error-analysis/SKILL.md), [interpretability](../ml-interpretability/SKILL.md), [packaging and inference](../ml-packaging-and-inference/SKILL.md), or [monitoring and drift](../ml-monitoring-and-drift/SKILL.md). The references define shared standards; the dedicated skills define workflow steps.

For AWS work, read [local AWS testing](references/aws-local-testing.md) and/or [Lambda least privilege](references/aws-lambda-least-privilege.md). For containers or runtime changes, use [Docker and GHCR release workflow](references/docker-ghcr-release-workflow.md), [deployment runtime contract](references/deployment-runtime-contract.md), and [secure infrastructure operations](references/secure-infra-ops.md) as applicable. Use [environment awareness](references/environment-awareness.md) when deployment boundaries matter.

For implementation or deployment work in `ai-enabled-ato`, also read the scoped [ATO runtime and deployment contract](references/ato-runtime-deployment-contract.md). It applies only to that repository.

For cybersecurity workflows, route orchestration to [cybersecurity workflow design](../cybersecurity-workflow-design/SKILL.md), model-call contracts to [cybersecurity prompt engineering](../cybersecurity-prompt-engineering/SKILL.md), external systems to [cybersecurity integration adapters](../cybersecurity-integration-adapters/SKILL.md), and consequential operations to [cybersecurity approval and policy gates](../cybersecurity-approval-policy-gates/SKILL.md). Add [security evidence](references/security-evidence-discipline.md) when findings or reports depend on evidence classification. For general security-sensitive changes, read [security](references/security.md) and add [LLM boundaries](references/llm-boundaries.md) or [deterministic LLM guardrails](references/llm-deterministic-guardrails.md) only when those systems are involved. For a service, API, or public endpoint, read [authorization-ready applications](references/authorization-ready-apps.md). For production HTTP APIs, edge exposure, quotas, authentication entry points, or health checks, also read [API abuse and exposure](references/api-abuse-and-exposure.md). Load [project HTTP security checkpoints](references/api-project-checkpoints.md) only for `ai-enabled-ato`, `ai-enabled-threathunting`, or `llm_notable_analysis`. Do not retrofit these production controls into developer/test instances unless requested; preserve existing protections.

For corrections to LLM evidence handling, output contracts, grounding guards or
quality evaluations, use [llm-evidence-regression](../llm-evidence-regression/SKILL.md)
to check rejection and supported-fact/decision retention together. This routing
does not apply to unrelated LLM work or ordinary writing.

For production tool integrations, load only the matching reference: [Splunk SDK/SPL](../cybersecurity-integration-adapters/references/splunk-production.md), [OpenSearch/FAISS](../development-stack/references/retrieval-search-production.md), [local embeddings](../development-stack/references/local-embeddings-production.md), [Azure Functions/Storage](../development-stack/references/azure-functions-storage-production.md), [Cosmos DB/Azure AI Search](../development-stack/references/azure-cosmos-search-production.md), [Authlib OIDC/JWT](../development-stack/references/authlib-oidc-production.md), or [MSAL/Entra](../development-stack/references/msal-entra-production.md). For Vite builds, Vitest tests, or Playwright browser flows, use the matching reference in the [React skill](../react/SKILL.md). These references qualify existing integrations; they do not require choosing a new stack.

For product architecture or project structure, consult [capability profile architecture](references/capability-profile-architecture.md) and/or [project layout standards](references/project-layout-standards.md) when relevant. Use [technology selection](references/technology-selection.md) only for greenfield work or when the project has no established stack; preserve explicit user choices and existing project evidence.

For documentation work, read [documentation layout and bootstrap](references/docs-layout-and-bootstrap.md) and [testing and documentation standards](references/testing-documentation-standards.md) when the changed contract or behavior calls for them.

## Scope boundaries

- For LangGraph workflow engineering, use the separate `langgraph-engineering` skill as the primary workflow guide; read this collection only for an additional, directly relevant standard.
- For reproduced parser, API, timeout, cancellation, or durable-state regressions, use `boundary-failure-regressions`.

For shared UI work, complete the central baseline's **Interaction and accessibility**
checks and its role/state coverage record. Exercise keyboard focus and bypass,
modal/popup semantics, disabled/readonly/validation, loading/error announcements,
loading-to-content consistency, field-boundary contrast, and scrolling/enlarged
content in the affected apps. Preserve app-specific guards and layouts. Record
actual browser/route/state evidence and any unverified areas; source parity alone
is not interaction or accessibility sign-off.
