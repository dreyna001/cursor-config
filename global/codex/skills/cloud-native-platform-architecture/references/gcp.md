# GCP Decision Guidance

Use these prompts for Google Cloud architecture. They are not a fixed reference architecture or one-to-one mapping from another provider.

## Platform Fit

- Confirm the organization, project, region, and data-residency boundary before selecting services.
- Verify current regional service, model, feature, and quota availability from official Google Cloud documentation.
- Prefer GCP-managed services when they satisfy the workload and reduce customer operations.
- Select Cloud Run services, jobs, worker pools, or functions from the workload lifecycle; do not reproduce AWS, Azure, or on-prem topology by default.

## Identity And Network

- Prefer attached service accounts, Workload Identity Federation, and short-lived credentials over service-account keys.
- Scope IAM roles to the narrowest practical project, resource, and operation.
- Treat project IDs, service accounts, token audiences, endpoints, DNS, certificates, and organization policies as runtime contracts.
- Use private connectivity and network controls when the threat model requires them; do not add VPC complexity without a concrete boundary.

## Data And Retrieval

- Choose Cloud Storage, Firestore, Cloud SQL, AlloyDB, Vertex AI Vector Search, or another service from access patterns, consistency, filtering, retrieval, and operational needs.
- Define the authoritative record, immutable artifacts, mutable indexes, concurrency controls, replay behavior, and deletion or retention ownership.
- Prefer Cloud SQL or AlloyDB PostgreSQL with pgvector when relational data and semantic retrieval belong together; add a dedicated vector service only when scale or query behavior requires it.
- Verify the selected embedding model and retrieval capability in the target region and against the model-origin policy.

## Reliability And Operations

- Define retry ownership across client libraries, Cloud Run, Eventarc, Pub/Sub, Cloud Tasks, and application code.
- Require idempotency and side-effect fencing for duplicate-capable delivery.
- Size acknowledgement deadlines, task timeouts, concurrency, retry policy, and dead-letter handling together.
- Use mocked clients and maintained emulators where useful, then require live GCP validation for IAM, networking, encryption, quotas, and managed-service behavior.

## Customer Boundary

Document customer-owned values such as organization, project, region, service accounts, encryption keys, retention, domains, identity providers, integration endpoints, capacity, model IDs, and feature profiles. Validate them without baking a specific customer's values into the architecture.
