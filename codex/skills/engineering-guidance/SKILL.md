---
name: engineering-guidance
description: Use for code design, implementation, or review when this collection's Python, ML, API, cloud, security, LLM, frontend, or documentation standards apply; read only matching references.
---

# Engineering Guidance

Use this skill as a conditional router for the user's migrated engineering standards. Read only the reference files relevant to the requested change and the systems it touches. Do not turn the collection into a checklist for unrelated work. Follow the current global `AGENTS.md` for universal behavior and model routing.

## Reference index

For general code changes, use the applicable parts of [core engineering](references/core-engineering.md), [correctness and testing](references/correctness-and-testing.md), [maintainability and architecture](references/maintainability-and-architecture.md), [reliability and performance](references/reliability-and-performance.md), and [requirements confidence](references/requirements-confidence.md).

For APIs, persistence, queues, or distributed behavior, read [API, data, and distributed systems](references/api-data-and-distributed.md). For Python code, read [Python coding standards](references/python-coding-standards.md) after checking the target project's declared and deployed Python versions; preserve its established stack and conventions. For React, read [React](references/react.md).

For traditional ML work, read only the relevant parts of [ML foundations](references/01_ml_foundations.md), [data and validation](references/02_data_and_validation.md), [experiments and reproducibility](references/03_experiment_and_reproducibility.md), [delivery and reporting](references/04_delivery_and_reporting.md), and [scale and data handling](references/05_scale_and_data_handling.md).

For AWS work, read [local AWS testing](references/aws-local-testing.md) and/or [Lambda least privilege](references/aws-lambda-least-privilege.md). For containers or runtime changes, use [Docker and GHCR release workflow](references/docker-ghcr-release-workflow.md), [deployment runtime contract](references/deployment-runtime-contract.md), and [secure infrastructure operations](references/secure-infra-ops.md) as applicable. Use [environment awareness](references/environment-awareness.md) when deployment boundaries matter.

For cybersecurity workflows, use the relevant references for [approval and policy gates](references/cybersecurity-approval-policy-gates.md), [integration adapters](references/cybersecurity-integration-adapters.md), [LLM workflow architecture](references/cybersecurity-llm-workflow-architecture.md), and [security evidence](references/security-evidence-discipline.md). For general security-sensitive changes, read [security](references/security.md) and add [LLM boundaries](references/llm-boundaries.md) or [deterministic LLM guardrails](references/llm-deterministic-guardrails.md) only when those systems are involved.

For production tool integrations, load only the matching reference: [Splunk SDK/SPL](../cybersecurity-integration-adapters/references/splunk-production.md), [OpenSearch/FAISS](../development-stack/references/retrieval-search-production.md), [local embeddings](../development-stack/references/local-embeddings-production.md), [Azure Functions/Storage](../development-stack/references/azure-functions-storage-production.md), [Cosmos DB/Azure AI Search](../development-stack/references/azure-cosmos-search-production.md), [Authlib OIDC/JWT](../development-stack/references/authlib-oidc-production.md), or [MSAL/Entra](../development-stack/references/msal-entra-production.md). For Vite builds, Vitest tests, or Playwright browser flows, use the matching reference in the [React skill](../react/SKILL.md). These references qualify existing integrations; they do not require choosing a new stack.

For product architecture or project structure, consult [capability profile architecture](references/capability-profile-architecture.md) and/or [project layout standards](references/project-layout-standards.md) when relevant. Use [technology selection](references/technology-selection.mdc) only for greenfield work or when the project has no established stack; preserve explicit user choices and existing project evidence.

For documentation work, read [documentation layout and bootstrap](references/docs-layout-and-bootstrap.md) and [testing and documentation standards](references/testing-documentation-standards.md) when the changed contract or behavior calls for them.

## Scope boundaries

- For LangGraph workflow engineering, use the separate `$langgraph-engineering` skill as the primary workflow guide; read this collection only for an additional, directly relevant standard.
- The original `subagent-delegation.mdc` rule is intentionally superseded: Codex model and delegation routing belongs to the current global `AGENTS.md`.
- Do not use Cursor-only actions or assume Cursor tools are available in Codex.
