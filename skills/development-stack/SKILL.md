---
name: development-stack
description: "Choose or review application, data, LLM, frontend, deployment, and infrastructure technologies while preserving established project choices."
---
# Development Stack

For UI/UX work, start at the permanent local baseline:
`$HOME/.agents/ui-baseline/README.md` (Windows:
`%USERPROFILE%\.agents\ui-baseline\README.md`). On the current workstation,
open [Windows](C:/Users/Daniel.Reyna/.agents/ui-baseline/README.md) or
`$HOME/.agents/ui-baseline/README.md` (WSL).
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

Use the selection defaults only when the task requires a technology choice. Read [references/stack-boundaries.md](references/stack-boundaries.md) before introducing a central component into a project that does not already use it.

For routine work in a repository that already uses a listed technology, do not reconsider the stack. Load only the relevant implementation-practice reference routed from `stack-boundaries.md`, and follow the repository's established patterns first.

For production integration changes, read only the matching reference:

- [OpenSearch and FAISS](references/retrieval-search-production.md) for retrieval, indexing, or index lifecycle changes.
- [Local embeddings](references/local-embeddings-production.md) for Sentence Transformers or Transformers embedding and reranking changes.
- [Azure Functions and Storage](references/azure-functions-storage-production.md) for Functions, Blob Storage, or Storage Queue execution changes.
- [Cosmos DB and Azure AI Search](references/azure-cosmos-search-production.md) for the selected service's persistence or retrieval contracts.
- [Authlib](references/authlib-oidc-production.md) for OIDC login or JOSE/JWT bearer-token verification.
- [MSAL and Entra](references/msal-entra-production.md) for browser/backend authentication and authorization changes.

Pick **Shared** defaults first, then the **On-prem** or **Cloud** profile that matches the deployment target. Do not mix profiles without a concrete requirement.

## Precedence

1. Follow explicit task requirements.
2. Preserve the repository's established stack and valid project instructions.
3. Reuse existing dependencies, patterns, and deployment mechanisms.
4. Use the defaults below only when the choice remains open.

Do not replace, upgrade, or add technology merely to match these defaults. Add a dependency only when the current task requires it and existing mechanisms are insufficient; explain the need.

## Shared

Applies to on-prem and cloud unless a profile below overrides it.

### Python application base

- **Runtime and layout:** Python 3.12, `pyproject.toml`, `src/<package_name>/`, package imports.
- **Validation and contracts:** Pydantic v2 at API, config, and structured-output boundaries; `pydantic-settings` for environment configuration.
- **HTTP services:** FastAPI with Uvicorn when an HTTP API is required.
- **Sync HTTP clients:** `requests` for scripts and synchronous integrations.
- **Async HTTP clients:** `httpx` for async FastAPI paths and high-concurrency service code.
- **Tests:** pytest for deterministic behavior, contracts, and regressions.
- **LLM evaluation:** Pydantic Evals for probabilistic LLM or agent quality; keep deterministic assertions in pytest.

### Data (relational and ML)

- **Relational store:** PostgreSQL when durable relational state, transactions, or concurrent access are required (portal/worker apps such as ATO and threat hunting).
- **Semantic retrieval:** PostgreSQL full-text search plus pgvector hybrid retrieval when semantic retrieval is required and PostgreSQL is already an appropriate system of record; use self-managed PostgreSQL on-prem or provider-managed PostgreSQL in cloud.
- **ORM and migrations:** SQLAlchemy 2 with Alembic when PostgreSQL persistence needs schema evolution.
- **PostgreSQL driver:** psycopg 3 (sync or async); use `asyncpg` only for a demonstrated performance need.
- **Dataframes (traditional ML):** Polars first; pandas only at a narrow compatibility boundary.
- **ML modeling:** scikit-learn baselines first; no deep learning without a demonstrated requirement.
- **Small data interchange:** CSV by default; use Parquet or another format only with a concrete scale or integration reason.

### LLM platform (shared targets)

- **Model origin:** use only models made in the United States, including foundation, embedding, reranking, vision, OCR, speech, and externally developed ML models.
- **Bounded LLM steps:** PydanticAI for tool-using agents, dependency injection, and structured model output.
- **Multi-step workflows:** pydantic-graph only when explicit state, branching, loops, or resumability are required.
- **MCP:** FastMCP when exposing or consuming MCP tools or resources.
- **Policy enforcement:** OPA when authorization or execution policy must be externalized, shared, or independently audited.
- **Observability:** OpenTelemetry for production traces, metrics, and correlated logs.
- **Sandboxing:** gVisor when containers run untrusted or agent-generated workloads and the platform supports it.

### Frontend (when a web UI is required)

- **App stack:** React, TypeScript, and Vite.
- **UI:** Tailwind CSS for styling; Radix UI for accessible interaction primitives.
- **Visual theme:** Follow the permanent local UI/UX baseline and its visual adaptation rules. Preserve the destination app's approved behavior and styling; use the HTML as a companion, not an override.
- **Unit tests:** Vitest.
- **Browser E2E:** Playwright only when end-to-end coverage is justified.
- **Portal extras (conditional):** `zod`, version-appropriate `react-router` imports, Testing Library/jsdom, and OpenAPI client codegen when the UI is tightly bound to a typed API contract.

### Auth (customer-dependent)

Authentication is chosen per customer and project requirements. Do not impose one global auth mechanism.

Common options when the choice is open:

- **OIDC/OAuth2 enterprise SSO:** `authlib` or the customer's IdP SDK.
- **Azure AD / Entra ID:** `@azure/msal-browser` on the frontend and the matching backend validation pattern when the customer uses Microsoft identity.
- **JWT or API tokens:** `PyJWT` or provider token validation for service, pipeline, or machine-to-machine boundaries.
- **Cloud managed identity:** AWS IAM roles, Azure managed identity, or equivalent provider-native service auth instead of long-lived shared secrets when running in cloud.

Follow the customer's IdP, compliance constraints, and any auth pattern already established in the repository.

### Document intake default (both profiles)

Use bounded, deterministic extraction with explicit size, page, and output limits.

- **Per-format extractors:** `pypdf`, `pypdfium2`, `python-docx`, `docx2txt`, `openpyxl`, `Pillow`, `defusedxml`, `lxml`.
- **Schema validation (conditional):** `jsonschema` when validating external JSON/OSCAL or similar contracts.
- **Governed app intake:** keep per-format extractors with audit trail and structured segments; do not replace with Docling.

### Packaging

- **Container option:** Docker/OCI images with minimal non-root images and immutable tags (GHCR when using the established release workflow).

## On-prem

Use when the deployment target is customer-controlled infrastructure, airgapped, or systemd/Docker on owned hosts.

### Deployment

- **Single-host services:** systemd when direct host deployment fits better than containers.
- **Containers:** Docker/OCI when packaging is required.

### Inference and routing

- **Self-hosted inference:** vLLM as the default OpenAI-compatible inference server.
- **LLM client:** direct OpenAI-compatible HTTP calls via `httpx` or `requests` unless PydanticAI or another agent framework is required.
- **Multi-model routing:** LiteLLM only when multiple providers or models need one routing boundary.

### Retrieval and embeddings

- **PostgreSQL deployment:** run the shared PostgreSQL full-text search and pgvector stack on customer-controlled infrastructure.
- **Local embeddings:** `sentence-transformers` with pinned Hugging Face models; default embed/rerank family is IBM Granite English r2 unless the project already pins another model.
- **Token counting (optional):** `tiktoken` for portal or context budgeting.

### Document intake

- **RAG/plain-text ingest:** start with the shared per-format stack.
- **Upgrade path:** Docling only when real documents need layout, tables, reading order, or scan/OCR fidelity and the default stack is insufficient.

## Cloud

Use when the deployment target is AWS, Azure, GCP, or another managed cloud. Pick **one** cloud path; do not combine provider defaults in one project.

**Cloud means provider-managed services only.** Use the cloud provider's native compute, storage, database, search, AI, identity, and networking services. Do not lift-and-shift onto self-managed VMs, pet servers, or on-prem runtime patterns such as systemd, vLLM, or Docker-on-a-host you operate like on-prem.

Pipeline apps (notable analysis) and portal/worker apps use different durable stores. Do not assume one cloud database shape for every project.

### Deployment and IaC

- **Cloud IaC:** Terraform only.

### AWS path (notable pipeline shape)

- **Runtime:** Lambda and other AWS-managed compute — not EC2 VM deployments.
- **SDK:** `boto3`.
- **Object and queue storage:** S3 and SQS when the pipeline shape requires them.
- **App state:** DynamoDB for pipeline metadata, idempotency, and portal chat state.
- **Analysis LLM:** Bedrock approved model IDs for the customer account.
- **Embeddings:** Bedrock Titan embed (`amazon.titan-embed-text-v2:0` or customer-approved equivalent).
- **Vector retrieval:** OpenSearch Service.
- **Document OCR:** Textract for scanned PDFs and images when OCR is required beyond digital PDF/DOCX text layers.
- **Local testing:** mocked clients for unit tests; LocalStack for integration when useful.

### Azure path (notable pipeline shape)

- **Runtime:** Azure Functions and other Azure-managed compute — not Azure VM deployments.
- **SDK:** `azure-*` SDKs.
- **Object and queue storage:** Blob Storage and Queue Storage when the pipeline shape requires them.
- **App state:** Cosmos DB for transactional application state.
- **Analysis and embeddings:** Azure OpenAI deployments for chat and 1024-dimensional embeddings.
- **Vector retrieval:** Azure AI Search.
- **Document OCR:** Azure Document Intelligence when scan/OCR is required.
- **Local testing:** mocked clients for unit tests; Azurite and the Cosmos DB emulator for integration when useful.

### GCP path (notable pipeline shape)

- **Runtime:** Cloud Run services, jobs, or functions and other GCP-managed compute — not Compute Engine VM deployments.
- **SDK:** `google-cloud-*` client libraries.
- **Object and queue storage:** Cloud Storage with Pub/Sub or Cloud Tasks when the pipeline shape requires them.
- **App state:** Firestore for pipeline metadata, idempotency, and portal chat state when a document store fits the access pattern.
- **Analysis and embeddings:** customer-approved Vertex AI deployments that satisfy the shared model-origin policy.
- **Vector retrieval:** Vertex AI Vector Search for a dedicated managed vector index; prefer Cloud SQL or AlloyDB PostgreSQL with pgvector when PostgreSQL is already the appropriate system of record.
- **Document OCR:** Document AI when scan or layout extraction is required.
- **Local testing:** mocked clients and provider emulators where maintained and useful; require live validation for identity, networking, quotas, and managed-service behavior.

### Cloud portal/worker apps

When a portal or worker app is deployed to cloud, keep the app cloud-native:

- **Compute:** provider-managed services such as Lambda, Fargate, Azure Functions, App Service, or Cloud Run — not self-managed VMs.
- **Relational state:** provider-managed PostgreSQL such as RDS, Azure Database for PostgreSQL, Cloud SQL, or AlloyDB when relational storage is required, including managed pgvector when the shared retrieval default fits the workload — not PostgreSQL on a VM you operate.
- **Auth:** follow the shared auth options and the customer's IdP requirements.

### Cloud integrations (not global defaults)

- **Splunk, ServiceNow, Elasticsearch, and similar systems:** thin integration adapters only; customer- and profile-specific, not personal stack defaults.

## Handoff

When a new stack choice was necessary, state the deployment profile (shared, on-prem, or cloud path), what was selected, why existing mechanisms were insufficient, and how the choice was verified. Do not produce a stack recommendation for routine changes that introduced no technology decision.

## Shared UI change completion

Approved shared UI changes are not complete until the versioned baseline,
its visual companion, all three apps (six frontends), this configuration
repository's reference bundle, and the permanent local baseline are synchronized.
Follow the baseline's “Keeping one baseline” procedure, record app-specific
exceptions and validation, and preserve newer approved behavior and styling.
If any part cannot be updated or verified, report the remaining drift explicitly.

For shared UI work, complete the central baseline's **Interaction and accessibility**
checks and its role/state coverage record. Exercise keyboard focus and bypass,
modal/popup semantics, disabled/readonly/validation, loading/error announcements,
loading-to-content consistency, field-boundary contrast, and scrolling/enlarged
content in the affected apps. Preserve app-specific guards and layouts. Record
actual browser/route/state evidence and any unverified areas; source parity alone
is not interaction or accessibility sign-off.

For desktop zoom and assistant-feedback work, follow the central baseline's
**Desktop zoom and conversational feedback** section. Verify actual browser zoom
separately from root-font resizing, preserve the requested desktop/mobile scope,
and test waiting/error/completion announcements, required states and guarded flows.
Distinguish accessibility-tree evidence from actual screen-reader speech; record
excluded apps and unavailable checks rather than claiming whole-suite coverage.

For every UI/UX change, use Playwright to verify the affected surface and follow the central baseline's **Workflow and popup regression coverage**.
Verify every dialog's accessible name, all constrained desktop confirmation actions,
popup viewport fit, and relevant delayed/failed-request, retry, duplicate-submit and
unsaved-navigation paths. Preserve each app's guards and desktop/mobile scope;
record actual browser/role/state evidence and synthetic-versus-live test boundaries.

## Reviewing an existing frontend foundation

When the user requests standardization or architecture review, preservation of
an existing stack is not evidence that it is the best choice. Compare current
implementations with credible alternatives against the actual workflows,
security boundaries, complexity, performance evidence and migration cost.
Record the decision, uncertainty and conditions that would justify revisiting it.
Do not infer quality from one app's incumbent implementation or from popularity.
For the workspace suite, follow the permanent UI/UX baseline's **Foundation
decision review** and shared-foundation contract. Keep apps independently
buildable; cross-repository comparisons are development checks only.
Use the existing source-driven, maintainability, reliability/performance and
testing guidance for relevant concerns; do not create parallel policy skills.
