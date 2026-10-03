# OpenSearch And FAISS Retrieval Practices

Apply the relevant section only when the project already uses OpenSearch or FAISS. Keep the embedding contract aligned with [local embeddings guidance](local-embeddings-production.md); neither engine defines the model, text preprocessing, or tenant policy for the application.

## OpenSearch

- Create an explicit vector mapping before ingestion. Fix the dimension, distance space, engine, method, and index settings as a versioned contract; validate vector shape and numeric values at the write boundary. Do not rely on dynamic mapping or assume vector mapping changes can be applied in place. Check method/metric support for the deployed OpenSearch version and engine.
- Enforce tenant and document access through authenticated server-side policy: index permissions plus a non-removable tenant/document filter or supported document-level security. A tenant value supplied by the caller is an input, not authorization. OpenSearch DLS limits reads but does not limit writes; grant write permissions separately and test cross-tenant reads, updates, and deletes. When combining DLS and field-level security, keep the fields used by DLS visible to its filter.
- Use a hybrid lexical/vector query and score normalization or rank fusion only when relevance evaluation supports it. OpenSearch combines different score distributions through a search pipeline; verify the selected query and pipeline combination is supported by the deployed version and avoid assuming that lexical and vector scores are directly comparable.
- Make ingestion replay-safe with stable source-derived document IDs and an explicit update/version policy. Bound bulk request size and concurrency. Inspect both the top-level bulk error flag and each item result: retry only failed transient items, with bounded backoff; route mapping, validation, authorization, and version conflicts to correction or reconciliation instead of retrying the whole batch blindly.
- Treat mapping or embedding-contract changes as a new index generation. Build and validate the new index, including document counts, representative relevance queries, tenant filters, and freshness, then switch the read alias with one atomic aliases request. Keep the prior index available through the rollback window.
- For Amazon OpenSearch Service, qualify the exact service variant, region, partition, engine version, authentication path, and required features before design or deployment. Commercial and GovCloud support can differ; check the current AWS service and regional support matrices instead of inferring managed-service parity from upstream OpenSearch documentation.

## FAISS

- Keep the index rebuildable from a durable corpus snapshot and store a manifest beside it: FAISS build/version, CPU or GPU path, index type and training configuration, dimension/metric, stable ID mapping, corpus snapshot, and embedding model/preprocessing revision. Validate manifest compatibility and a trusted checksum/signature before loading. FAISS warns that malformed or malicious index files can cause resource exhaustion or code execution; never load an index from an untrusted or user-writable source.
- Write rebuilt indexes to a staged artifact and promote only after load and representative-query checks succeed. GPU indexes must be copied to CPU before `write_index`; verify the exact library/runtime and hardware path used for restore.
- Coordinate access explicitly. CPU indexes support concurrent read-only searches, but mutation must be synchronized with search and other mutations. GPU indexes are not thread-safe even for reads; serialize access or give each active calling thread its own `StandardGpuResources`.
- Use deterministic integer IDs and a separately persisted mapping to source records; FAISS index IDs are 64-bit integers, not application string keys. Keep document authorization and tenant filtering in a trusted layer that cannot be bypassed by the caller.

## Sources

- [OpenSearch `knn_vector` mappings](https://docs.opensearch.org/latest/mappings/supported-field-types/knn-vector/)
- [OpenSearch k-NN methods and engines](https://docs.opensearch.org/latest/mappings/supported-field-types/knn-methods-engines/)
- [OpenSearch hybrid search](https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/)
- [OpenSearch Bulk API and item-level failures](https://docs.opensearch.org/latest/api-reference/document-apis/bulk/)
- [OpenSearch atomic aliases API](https://docs.opensearch.org/latest/api-reference/alias/aliases-api/)
- [OpenSearch document-level security](https://docs.opensearch.org/latest/security/access-control/document-level-security/)
- [OpenSearch field-level security](https://docs.opensearch.org/latest/security/access-control/field-level-security/)
- [Amazon OpenSearch Service in AWS GovCloud](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-opensearch.html)
- [Amazon OpenSearch Service supported versions](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)
- [FAISS index I/O and serialization warning](https://github.com/facebookresearch/faiss/wiki/Index-IO%2C-cloning-and-hyper-parameter-tuning)
- [FAISS thread safety and asynchronous calls](https://github.com/facebookresearch/faiss/wiki/Threads-and-asynchronous-calls)
- [FAISS FAQ, including ID limits](https://github.com/facebookresearch/faiss/wiki/FAQ)
