# AWS Decision Guidance

Use these prompts for AWS and AWS GovCloud architecture. They are not a fixed reference architecture.

## Platform Fit

- Confirm the target partition and region before selecting services or endpoints.
- Verify current AWS GovCloud service and feature availability from official AWS documentation.
- Prefer regional managed services that satisfy the workload's latency, scale, compliance, and recovery requirements.
- Select event-driven, synchronous, scheduled, streaming, or batch topology from actual workload behavior.
- Do not reproduce Azure or on-prem topology when AWS has a simpler native path.

## Identity And Network

- Prefer IAM roles and short-lived workload credentials over embedded or customer-managed static credentials.
- Scope resource policies, role trust, actions, resources, KMS use, and cross-account access explicitly.
- Treat partition-specific ARNs, service principals, STS behavior, endpoints, DNS, certificates, and audiences as runtime contracts.
- Use private networking where the threat model or customer boundary requires it; do not add VPC complexity without a concrete boundary.

## Data And Retrieval

- Choose S3, DynamoDB, relational storage, OpenSearch, or another service from access patterns and consistency needs, not cross-cloud naming symmetry.
- Define the authoritative record, immutable artifacts, mutable indexes, concurrency controls, replay behavior, and deletion/retention ownership.
- For small knowledge corpora, compare managed search, application-managed retrieval, and simpler indexed storage before accepting OpenSearch operational cost.
- If semantic retrieval is required, verify embedding-model and vector-search availability in the target partition and region.

## Reliability And Operations

- Define retry ownership across SDK, Lambda, queue, event source, workflow, and application layers.
- Require idempotency for duplicate-capable event delivery and side effects.
- Size queue visibility, function timeout, batch failure handling, concurrency, and dead-letter behavior together.
- Test locally with mocked clients and LocalStack where useful, then require real-account validation for IAM, KMS, networking, quotas, and managed-service behavior.

## Customer Boundary

Document customer-owned values such as account, region, KMS keys, retention, domains, identity providers, integration endpoints, capacity, model IDs, and feature profiles. Validate them without baking a specific customer's values into the architecture.
