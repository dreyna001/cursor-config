---
name: engineering-guidance
description: "Find shared engineering standards for architecture, production boundaries, security, or cross-cutting behavior changes."
---

# Engineering Guidance

For UI/UX work, use the global `AGENTS.md` UI/UX route to the permanent baseline and its browser verification and shared rollout requirements.

## Cloud IaC policy

Use Terraform exclusively for all new or modified cloud resources, across all
providers. Do not add or extend other IaC formats or provision resources through
console instructions or application scripts. Apply the Terraform cloud deployment
standard and the existing documented root; treat other checked-in templates as
legacy. Builds and artifact publication may use their existing tools.

For cloud development, apply the [Terraform cloud deployment standard](../terraform-cloud-deployment-standard/SKILL.md), including its create-or-reference contract for required deployable prerequisites. Preserve the established stack and customer ownership; document qualified platform exceptions.

Use this skill as a conditional router for the user's migrated engineering standards. Read only the reference files relevant to the requested change and the systems it touches. Do not turn the collection into a checklist for unrelated work. Follow the current global `AGENTS.md` for universal behavior and model routing.

For backup/recovery design or review of technologies actually used by the project, read [conditional backup and recovery decisions](../cloud-native-platform-architecture/references/data-protection.md).

## Reference index

For local tool/provider installation, Terraform cache use, or cache cleanup, read [local tool and Terraform caches](references/local-tool-and-terraform-caches.md). Before post-merge worktree cleanup, read [worktree verification and removal](references/post-merge-worktree-cleanup.md). For WSL configuration, model routing, AI COE checkout hygiene or command waiting, read the applicable section of [WSL Codex operations](references/wsl-codex-operations.md).

For cache, overlapping refresh, extraction reuse or repeated parsing/byte preparation changes, read [safe reuse and preparation](references/safe-reuse-and-preparation.md). Use the reliability reference for late cancellation/cleanup and the API reference for retry/save identity.

For model-call, prompt/output-contract or embedding/indexing changes, apply [LLM efficiency with preserved analysis](references/llm-efficiency.md) alongside the relevant engineering references.


For frontend routes, browser history, deep links, or frontend/backend URL
boundaries, read [URL routing](references/url-routing.md). For compact portals
with peer workspaces, also use the scoped [small portal routing](references/small-portal-routing.md).

For general code changes, use the applicable parts of [core engineering](references/core-engineering.md), [correctness and testing](references/correctness-and-testing.md), [maintainability and architecture](references/maintainability-and-architecture.md), [reliability and performance](references/reliability-and-performance.md), and [requirements confidence](references/requirements-confidence.md). For interface layout, navigation, content hierarchy, or editing-state decisions across UI stacks, read [UI/UX organization](references/ui-ux-organization.md).

For user-facing wording and first-use task clarity, use [self-explanatory UI](../self-explanatory-ui/SKILL.md).

For APIs, persistence, queues, or distributed behavior, read [API, data, and distributed systems](references/api-data-and-distributed.md). For Python code, read [Python coding standards](references/python-coding-standards.md) after checking the target project's declared and deployed Python versions; preserve its established stack and conventions. For React, read [React](references/react.md). When frontend changes touch authentication, credential forwarding, browser persistence, uploads/previews or untrusted content rendering, also read [security](references/security.md) and its matching framework reference.

For traditional ML standards, read only the relevant parts of [ML foundations](references/01_ml_foundations.md), [data and validation](references/02_data_and_validation.md), [experiments and reproducibility](references/03_experiment_and_reproducibility.md), [delivery and reporting](references/04_delivery_and_reporting.md), and [scale and data handling](references/05_scale_and_data_handling.md).

For procedural ML work, use the matching dedicated skill: [problem framing](../ml-problem-framing/SKILL.md), [EDA](../ml-eda/SKILL.md), [preprocessing and features](../ml-preprocessing-and-features/SKILL.md), [baselines](../ml-baselines/SKILL.md), [model training](../ml-model-training/SKILL.md), [imbalance](../ml-imbalance/SKILL.md), [hyperparameter tuning](../ml-hyperparameter-tuning/SKILL.md), [evaluation](../ml-evaluation/SKILL.md), [error analysis](../ml-error-analysis/SKILL.md), [interpretability](../ml-interpretability/SKILL.md), [packaging and inference](../ml-packaging-and-inference/SKILL.md), or [monitoring and drift](../ml-monitoring-and-drift/SKILL.md). The references define shared standards; the dedicated skills define workflow steps.

For provider-dependent cloud work, start with the matching [AWS, Azure or Google Cloud architecture reference](../cloud-native-platform-architecture/SKILL.md#load-provider-guidance). For AWS local tests or Lambda permissions, use [local AWS testing](references/aws-local-testing.md) or [Lambda least privilege](references/aws-lambda-least-privilege.md), respectively. For built-image or runtime dependency changes, read [container and cloud security scans](references/security.md#container-and-cloud-security-scans). For containers or runtime changes, use [Docker and GHCR release workflow](references/docker-ghcr-release-workflow.md), [deployment runtime contract](references/deployment-runtime-contract.md), and [secure infrastructure operations](references/secure-infra-ops.md) as applicable. Use [environment awareness](references/environment-awareness.md) when deployment boundaries matter.

For application-specific implementation and deployment requirements, read that application's local instructions and project-only rule package.

For cybersecurity workflows, route orchestration to [cybersecurity workflow design](../cybersecurity-workflow-design/SKILL.md), model-call contracts to [cybersecurity prompt engineering](../cybersecurity-prompt-engineering/SKILL.md), external systems to [cybersecurity integration adapters](../cybersecurity-integration-adapters/SKILL.md), and consequential operations to [cybersecurity approval and policy gates](../cybersecurity-approval-policy-gates/SKILL.md). Add [security evidence](references/security-evidence-discipline.md) when findings or reports depend on evidence classification. For general security-sensitive changes, read [security](references/security.md) and add [LLM boundaries](references/llm-boundaries.md) or [deterministic LLM guardrails](references/llm-deterministic-guardrails.md) only when those systems are involved. For a service, API, or public endpoint, read [authorization-ready applications](references/authorization-ready-apps.md). For production HTTP APIs, edge exposure, quotas, authentication entry points, or health checks, also read [API abuse and exposure](references/api-abuse-and-exposure.md); app-specific checkpoints belong in the matching project-only package. Do not retrofit these production controls into developer/test instances unless requested; preserve existing protections.

For corrections to LLM evidence handling, output contracts, grounding guards or
quality evaluations, use [llm-evidence-regression](../llm-evidence-regression/SKILL.md)
to check rejection and supported-fact/decision retention together. This routing
does not apply to unrelated LLM work or ordinary writing.

For production tool integrations, load only the matching reference: [Splunk SDK/SPL](../cybersecurity-integration-adapters/references/splunk-production.md), [OpenSearch/FAISS](../development-stack/references/retrieval-search-production.md), [local embeddings](../development-stack/references/local-embeddings-production.md), [Azure Functions/Storage](../development-stack/references/azure-functions-storage-production.md), [Cosmos DB/Azure AI Search](../development-stack/references/azure-cosmos-search-production.md), [Authlib OIDC/JWT](../development-stack/references/authlib-oidc-production.md), or [MSAL/Entra](../development-stack/references/msal-entra-production.md). For Vite builds, Vitest tests, or Playwright browser flows, use the matching reference in the [React skill](../react/SKILL.md). These references qualify existing integrations; they do not require choosing a new stack.

For product architecture or project structure, consult [capability profile architecture](references/capability-profile-architecture.md) and/or [project layout standards](references/project-layout-standards.md) when relevant. Use [technology selection](references/technology-selection.md) for greenfield choices or an explicitly requested stack review/standardization; preserve explicit user choices and existing project evidence.

For documentation work, read [documentation layout and bootstrap](references/docs-layout-and-bootstrap.md) and [testing and documentation standards](references/testing-documentation-standards.md) when the changed contract or behavior calls for them.

## Scope boundaries

- For LangGraph workflow engineering, use the separate `$langgraph-engineering` skill as the primary workflow guide; read this collection only for an additional, directly relevant standard.
- The original `subagent-delegation.mdc` rule is intentionally superseded: Codex model and delegation routing follows the [WSL operating guidance](references/wsl-codex-operations.md#codex-model-and-subagent-routing).
- Do not use Cursor-only actions or assume Cursor tools are available in Codex.

## Shared frontend and report contracts

For report projection changes, use [report and export parity](../report-export-parity/SKILL.md). For evidence assignment, use [evidence field mapping](../evidence-field-mapping/SKILL.md). For shared frontend foundations, read [the independent deployment contract](references/shared-frontend-foundations.md). Reuse [LLM evidence regression](../llm-evidence-regression/SKILL.md) for generalizable analysis fixes; do not add fixture-specific reasoning exceptions.
