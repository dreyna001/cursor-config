# Azure Decision Guidance

Use these prompts for Azure and Azure Government architecture. They are not a fixed reference architecture.

## Platform Fit

- Confirm the target cloud, subscription boundary, and region before selecting services or endpoints.
- Verify current Azure Government service, SKU, model, feature, and regional availability from official Microsoft documentation.
- Prefer Azure-native managed services when they meet the application's requirements and reduce customer operations.
- Do not reproduce AWS or on-prem topology when Azure offers a simpler native path.

## Identity And Network

- Prefer managed identities and Entra authorization over account keys, connection strings, or application secrets where supported.
- Scope role assignments to the narrowest practical resource and data-plane role.
- Treat cloud-specific authorities, token audiences, resource-manager endpoints, DNS zones, suffixes, certificates, and SDK cloud configuration as runtime contracts.
- Use private endpoints, network ACLs, and private DNS from the threat model and customer boundary; validate name resolution and deployment-plane access explicitly.

## Data And Retrieval

- Choose Blob Storage, Cosmos DB, relational storage, Azure AI Search, or another service from access patterns, consistency, filtering, retrieval, and operational needs.
- Define the authoritative record, immutable artifacts, mutable indexes, ETag or concurrency behavior, replay semantics, and deletion/retention ownership.
- For small knowledge corpora, compare Azure AI Search with simpler application-managed or database retrieval before accepting additional service cost.
- If semantic retrieval is required, verify embedding-model and vector or hybrid search availability in the target cloud and region.

## Reliability And Operations

- Define retry ownership across SDK, Functions triggers, queues, workflows, and application code.
- Require idempotency and side-effect fencing for duplicate-capable delivery.
- Size visibility or lock duration, function timeout, poison handling, concurrency, and scaling together.
- Use emulators and mocked clients for local confidence, then require live Azure validation for managed identity, RBAC, private networking, DNS, Key Vault, quotas, and service-specific behavior.

## Customer Boundary

Document customer-owned values such as tenant, subscription, resource groups, region, keys, retention, domains, identity providers, integration endpoints, capacity, model deployments, and feature profiles. Validate them without baking a specific customer's values into the architecture.
