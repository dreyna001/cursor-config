# LLM efficiency with preserved analysis

Apply when adding, changing or reviewing model calls, their input/output contracts,
or embedding/indexing pipelines. Preserve the task's analytical purpose and
existing execution, evidence, access and deployment boundaries. Do not add a
standalone optimization project to unrelated work.

## Identify redundant model work

Inspect assembled provider requests and completed workflow stages, rather than
only individual prompt templates. Account for system instructions, framework
schemas, retained evidence, retrieved context, history, repair and review calls.
Identify repeated copies and transformations. Keep complete evidence and any
repetition shown necessary for quality; removing duplicate data is not permission
to summarize, truncate, select fewer sources, lower output limits, skip review or
switch models. An earlier request is not implicit memory for a later request.

Let application code copy existing data exactly. An approving review can return
its explicit decision and issues while the application retains the original
answer; a correction still returns the complete corrected content. Align prompts,
schemas, parsers, budgets, repair and failure handling when changing that contract.
Do not substitute deterministic copying for model reasoning or semantic review.

## Reuse only demonstrably compatible results

Prefer bounded request-scoped reuse when identical transformations repeat. Use
persistent reuse only when its measured benefit justifies lifecycle complexity
and compatible storage already exists or new infrastructure is separately scoped.
Do not cache whole answers, searches or authorization decisions merely because
the question or document ID matches.

For embeddings, compare the exact effective input and complete embedding contract:
provider/endpoint and immutable model or deployment revision, query/document mode,
prompt/preprocessing/tokenizer configuration where applicable, dimensions,
normalization, precision and other generation settings. A mutable alias alone
cannot establish compatibility. Invalidate on any relevant change; ambiguous,
legacy, missing or malformed entries are misses. Validate vector shape and finite
values before reuse. Do not modify inputs just to increase cache hits.

Enforce the original tenant/access scope and retention/deletion boundaries.
Reusing a vector must not skip metadata, ACL, expiration, reconciliation or delete
updates. Preserve every intended retrieval lane, filter, reranking step and failure
state. Test changed inputs and model settings, scope boundaries, invalid vectors,
failures and cleanup alongside actual reuse through the native call sites.

## Demonstrate savings and retained behavior

For affected paths, capture a reproducible before/after comparison of provider
call counts and input, output, cache-read/write and embedding tokens separately.
Distinguish actual provider usage from tokenizer estimates and input-byte counts.
Prompt caching may lower cost without removing logical context tokens; batch
requests may lower request overhead without reducing embedding tokens. Report
those effects accurately, using the same fixtures and settings.

Pair savings with preserved source content and bindings, analytical conclusions,
hypotheses, counterevidence, uncertainty, recommendations and relevant review/error
behavior. Schema acceptance and unchanged inputs alone do not establish semantic
quality after changing a model contract or prompt. Use the existing evidence-
regression and benchmark workflows for those changes. Start with local captured
requests and deterministic controls; use bounded live comparisons when authorized
and relevant, with synthetic evidence and explicit coverage limits. Do not impose
paid runs on every routine change or infer permission for deployments or recurring
model calls. Retain failed attempts and investigate regressions before promotion.
