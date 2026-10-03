# Central Stack Boundaries

These are preferred technologies when their capability is required, not dependencies to install in every project.

## Shared

- **Model origin:** use only United States-made models for any model capability.
- **FastAPI / Uvicorn:** HTTP API or service boundary only.
- **Pydantic v2:** boundary validation, serialization, structured LLM output, and config contracts—not a substitute for SQLAlchemy persistence models.
- **PydanticAI:** LLM agents with tools, dependencies, or structured output; use a direct SDK call for a single simple model step.
- **pydantic-graph:** explicit state, branching, loops, or resumability; keep linear flows as functions or a simple agent.
- **FastMCP:** MCP exposure or consumption; not an internal module abstraction.
- **OPA:** shared, externalized, or independently audited policy; keep simple local checks in application code when sufficient.
- **OpenTelemetry:** production cross-service observability; not for small local utilities.
- **gVisor:** untrusted or agent-generated container workloads with platform support.
- **PostgreSQL / SQLAlchemy / Alembic / psycopg:** durable relational state for portal/worker apps.
- **pgvector + PostgreSQL FTS:** hybrid semantic retrieval when PostgreSQL is an appropriate system of record; self-managed on-prem or provider-managed in cloud.
- **React / Vite / TypeScript / Tailwind / Radix:** web UI when required.
- **Federal SOC Dark theme:** default cybersecurity portal visual language when theming is open.
- **pytest / Pydantic Evals:** deterministic tests vs probabilistic LLM evaluation.
- **Per-format doc intake:** default bounded extraction; not every app needs file intake.
- **jsonschema:** external JSON or schema validation only.
- **Auth (authlib, MSAL, PyJWT, managed identity):** customer-dependent; choose from established project or customer requirements.

## On-prem

- **systemd / Docker:** deployment options for owned infrastructure.
- **vLLM + direct OpenAI-compatible HTTP client:** self-hosted inference only.
- **LiteLLM:** multi-provider or multi-model routing only.
- **sentence-transformers + pinned HF models:** local embeddings and rerank only.
- **Docling:** layout-heavy RAG upgrade only; not a replacement for governed per-format intake.

## Cloud

- **Provider-managed services only:** native compute, storage, database, search, AI, and identity from the chosen cloud provider; no VM lift-and-shift or on-prem runtime patterns.
- **Terraform:** the only cloud IaC default.
- **AWS pipeline (Lambda, S3, SQS, DynamoDB, Bedrock, Titan embed, OpenSearch, Textract):** notable pipeline shape.
- **Azure pipeline (Functions, Blob/Queue Storage, Cosmos DB, Azure OpenAI, Azure AI Search, Document Intelligence):** notable pipeline shape.
- **GCP pipeline (Cloud Run, Cloud Storage, Pub/Sub or Cloud Tasks, Firestore, Vertex AI, Vertex AI Vector Search, Document AI):** notable pipeline shape.
- **Cloud portal/worker apps:** managed compute plus managed PostgreSQL (RDS, Azure Database, Cloud SQL, or AlloyDB), including managed pgvector when appropriate; not VMs.
- **Splunk / ServiceNow / Elasticsearch:** integration adapters only; not stack defaults.

Before implementation, inspect installed versions, lockfiles, and current project usage. Add only the components required by the current task.

For implementation guidance, load only the relevant reference:

- [application-and-llm.md](application-and-llm.md) for APIs, validation, LLM workflows, MCP, evaluation, and document intake.
- [data-and-retrieval.md](data-and-retrieval.md) for PostgreSQL, migrations, pgvector, embeddings, and dataframes.
- [platform-and-operations.md](platform-and-operations.md) for policy, observability, sandboxing, deployment, inference, routing, and IaC.
