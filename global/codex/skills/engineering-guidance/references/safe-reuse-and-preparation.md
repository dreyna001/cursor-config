# Safe reuse and shared preparation

Apply when changing caches, refresh coordination, extraction or repeated input
preparation. Preserve the product's evidence, uncertainty, citation/provenance,
workflow limits, authorization and approval boundaries. This is conditional
engineering guidance, not permission to add an optimization project.

## Bound and validate reuse

- Prefer small memory-only, request/session-scoped caches. Bound entries, bytes
  and lifetime; clear affected sensitive entries on sign-out, account/access
  changes, access failures, mutations and relevant configuration changes.
  Existing approved persistent caches need explicit scope, retention/deletion,
  compatibility and measured benefit; do not replace them merely for uniformity.
- Authorize access in the current security scope and validate the current source
  version before reuse. Use an appropriate authoritative revision, conditional
  read or generation check; a document ID or TTL alone is insufficient. Never
  convert a failed/denied current read into a successful response from an old
  copy. If the product retains displayed content during failure, mark it stale
  or unavailable, do not treat it as current evidence, and retain access controls.
- Coalesce equivalent overlapping refreshes only for matching identity, scope,
  object and freshness generation. A change invalidates the old generation;
  post-change reads and explicit retries must obtain the required fresh result,
  not attach to an older failed or superseded attempt. Reject late completions
  from old generations instead of overwriting newer state. Do not collapse distinct
  operations, swallow errors or let one consumer cancel work other callers need.
- Reuse extraction only when source content/integrity, parser and dependency
  versions, transformation settings (including OCR/layout and output contract),
  format/conversion policy, preprocessing, limits and security scope
  match. Missing or ambiguous compatibility metadata is a miss. Apply the complete
  [embedding contract](llm-efficiency.md#reuse-only-demonstrably-compatible-results)
  to vectors, including provider/model settings; a mutable alias is insufficient.
- Scan and validate each upload at its existing approved admission boundary before
  reusing extraction. Preserve actual-byte/type/path/integrity checks and required
  malware/content scanning; a cache hit does not establish that the current upload
  is safe. Bind current upload-specific identity and citations outside shared
  transformed content. Retain the safe parser, isolation and resource limits.
- Prepare identical parsing and exact byte counts once per compatible immutable
  input/serializer contract when useful. Keep workflow-specific truncation, caps,
  field selection and citations/provenance at their own boundaries. Shared
  preparation must not pre-truncate evidence for another consumer or relax its
  limits; use the [byte accounting contract](api-data-and-distributed.md#byte-bounded-serialization-and-backing-reads).
- Account for documented format conversions through an explicit, versioned
  normalization/projection contract. Preserve saved bytes and content, immutable
  source identity and original integrity checks; a legitimate representation
  difference is not authority to rewrite saved material or weaken a checksum.

## Verify work reduction and retained behavior

Measure actual work before/after under comparable inputs: reads/bytes, parsing,
preparation, refreshes and provider calls as relevant. Pair savings with stale
versions, account/scope changes, denied/failed reads, post-change and explicit
retry reads, incompatible transform settings, safe/unsafe uploads, and supported
results with retained evidence and citations. For model/retrieval changes compare
answer quality, total cost and end-to-end latency as well as ranking/call counts;
use [LLM efficiency](llm-efficiency.md) and the existing benchmark workflow.
Do not claim unmeasured production savings or run paid/live evaluations implicitly.
