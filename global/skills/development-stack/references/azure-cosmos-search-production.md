# Azure Cosmos DB and Azure AI Search

Apply only the service sections a project uses. Treat Cosmos DB and Azure AI Search as separate managed data services with separate identities, limits, and derived-data contracts. Preserve an existing API, SDK, index layout, and deployment workflow unless the task requires a change.

## Azure Cosmos DB

- Confirm the Cosmos API in use before applying NoSQL-specific guidance. Cosmos DB for NoSQL supports native data-plane role assignments; these are distinct from Azure control-plane roles, and API support differs. Prefer managed identity and the narrowest database/container scope supported by the chosen API. Do not assume a resource-management role grants item access.
- Choose an immutable partition key from real read/write and transaction patterns. It determines the logical transaction boundary and request distribution. Check current service limits for the API, account/throughput mode, and full partition-key shape; for hierarchical keys, distinguish full-key limits from prefix behavior. Include the required key components in point operations, and check for hot keys and query fan-out before increasing overall throughput.
- Treat request units (RUs) as the cost/throughput budget of operations and queries. Record request charge where the SDK exposes it. Cosmos SDKs retry rate-limit responses (`429`) automatically within configured retry behavior; keep those retries inside the caller's deadline and monitor normalized RU consumption, throttling, and end-to-end latency. A 429 count alone does not prove that users saw a failed operation.
- Transactions and transactional batches are scoped to one logical partition. For read-modify-write paths, use `_etag`/`If-Match` conditional writes when concurrent updates must not overwrite each other; handle a precondition conflict as a state reread/reconciliation, not an unconditional retry of stale data.
- Make IDs, partition key, tenant/owner fields, and serialization shape explicit application contracts. Do not infer authorization from partitioning; enforce the caller's tenant and object permissions in the service boundary.

## Azure AI Search

- Treat the index as derived data. Version the document key, source/version provenance, filterable authorization metadata, searchable/retrievable fields, vector dimensions, embedding model/version, and similarity metric together with the producer and query code. Deploy schema changes that require recreation as a rebuild/migration with a rollback path; many field attribute or analyzer changes cannot be applied in place.
- A successful indexing HTTP response does not mean every document succeeded. Inspect each returned indexing result (`key`, `status`, `statusCode`, and `errorMessage`); fix malformed or unauthorized input, retry only transient failures with bounded backoff, and retain a reconciliation record for items that remain failed. Stable document keys make replay and source-to-index reconciliation tractable.
- Enforce document access on the server for every query. Prefer Entra data-plane roles for the application's index access. For document-level permissions, either use a supported Search permission-filter feature with the required permission metadata and caller token, or build a server-side security filter from trusted, validated identity claims. Never accept an untrusted browser-supplied filter as the authorization decision, and never query an ACL-protected index without the user identity the access design requires.
- Keep authorization metadata in step with source ACL changes. Search returns the permissions represented by the indexed document state; delayed or failed reindexing can leave access stale. Some built-in ACL/RBAC ingestion and query paths are preview features, and support depends on API/SDK version, source, region, and cloud. Check the current support matrix and obtain an explicit production qualification before relying on a preview path.
- Bound retrieval cost and payload size: request only fields the caller needs, cap result counts and vector/query dimensions to the product contract, and constrain user-generated filters and query input. Search APIs impose request, filter-clause, result-page, and vector-field limits; check current quotas instead of copying old numeric limits into application logic.
- Keep Search administration credentials server-side. Separate provisioning/index-writer privileges from query-only access where the identity model allows it, and avoid sending index admin keys or service-wide roles to browser code.

## Azure cloud and validation boundary

Use the endpoint and token audience for the selected Azure cloud, not a public-cloud string copied from an example. For example, Azure AI Search uses a `search.windows.net` endpoint and `https://search.azure.com/.default` audience in Azure public, while Azure Government uses a `search.azure.us` endpoint and `https://search.azure.us/.default`. Confirm the exact resource endpoint in deployment configuration. Verify service availability, tier, region, and feature support for the target cloud; a feature listed for commercial Azure is not evidence that it is available in Azure Government.

Emulators and mocks can verify application contracts and retry handling. They do not qualify RU distribution, regional failover, managed identity/RBAC, private networking, or cloud-specific Search features; record which of those require deployment-level evidence for the actual target.

## Official references

- [Cosmos DB partitioning overview](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview)
- [Monitor normalized request units and throttling](https://learn.microsoft.com/en-us/azure/cosmos-db/monitor-normalized-request-units)
- [Cosmos DB transactions and optimistic concurrency](https://learn.microsoft.com/en-us/azure/cosmos-db/database-transactions-optimistic-concurrency)
- [Cosmos DB for NoSQL data-plane RBAC](https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-connect-role-based-access-control)
- [Azure AI Search Entra authentication and roles](https://learn.microsoft.com/en-us/azure/search/search-security-rbac)
- [Azure AI Search document-level access control](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview)
- [Azure AI Search ACL and RBAC push indexing](https://learn.microsoft.com/en-us/azure/search/search-index-access-control-lists-and-rbac-push-api)
- [Azure AI Search partial indexing result contract](https://learn.microsoft.com/en-us/rest/api/searchservice/documents/?view=rest-searchservice-2026-04-01)
- [Create and update an Azure AI Search vector index](https://learn.microsoft.com/en-us/azure/search/vector-search-how-to-create-index)
- [Azure AI Search service limits](https://learn.microsoft.com/en-us/azure/search/search-limits-quotas-capacity)
- [Azure AI Search region and feature support](https://learn.microsoft.com/en-us/azure/search/search-region-support)
- [Azure AI Search keyless connections, including Azure Government endpoints](https://learn.microsoft.com/en-us/azure/search/keyless-connections)
