# Data And Retrieval Practices

Apply only the sections for technologies the project actually uses. Inspect installed versions, schemas, migrations, and existing access patterns before changing the data layer.

## PostgreSQL, SQLAlchemy, Alembic, And psycopg

- Put durable invariants in database constraints as well as application validation. Define ownership, transactions, concurrency, and deletion behavior explicitly.
- Keep transaction scopes short and visible. Do not hold transactions open across model calls, network calls, or user interaction.
- Use one session per request or unit of work; do not share SQLAlchemy sessions across concurrent tasks.
- Parameterize SQL and use psycopg pools deliberately. Bound pool size, acquisition time, statement time, and idle transactions.
- Make Alembic migrations reviewable and safe for the current data volume. Separate destructive or long-running backfills when operationally necessary.
- Add indexes from real query patterns and verify material changes with query plans rather than intuition.

## pgvector And Hybrid Retrieval

- Use pgvector when PostgreSQL is already the appropriate system of record and semantic retrieval is required. Do not add a second vector store without demonstrated scale or query needs.
- Pin the embedding model, revision, vector dimension, normalization, and distance metric as one versioned contract.
- Store source identity, chunk provenance, model version, and filterable metadata beside embeddings.
- Start with exact search for small corpora. Add HNSW or IVFFlat only after measuring latency and recall on representative data.
- Combine vector similarity with PostgreSQL full-text search when hybrid retrieval improves measured relevance; keep ranking logic explicit and tested.
- Treat embedding changes as data migrations with coexistence or rebuild plans, not silent in-place replacements.
- Evaluate retrieval with representative queries, relevance judgments, filters, empty results, and provenance checks.

## Local Embeddings And Reranking

- Use only United States-made models. Pin model IDs and immutable revisions; record license, dimensions, normalization, and maximum input length.
- Batch and cache only when it reduces measured cost or latency without weakening freshness or tenant isolation.
- Add a reranker only when evaluation shows retrieval quality needs it.

## Polars And Interchange

- Prefer lazy scans and expression-based transformations for larger data; collect only when the result is needed.
- Define schema, null, timezone, and categorical behavior explicitly at ingestion boundaries.
- Keep pandas conversion narrow and documented at compatibility boundaries.
- Use CSV for simple interchange and Parquet when typed columnar storage or demonstrated scale justifies it.
