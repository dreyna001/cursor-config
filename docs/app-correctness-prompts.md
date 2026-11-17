# App correctness audit prompts

Run a selected prompt in the app's repository. Each prompt authorizes analysis and targeted fixes. Follow the app's instructions and existing security, test, browser, and deployment boundaries. Use local or isolated fixtures for failures and consequential effects.

The existing skills own these topics. The additional guidance extends their references and routing. Skill names remain unchanged.

## Coverage and maintenance

- Implicit state machines extend the existing correctness reference and review skill with diagnosis, authoritative transitions, minimal representations, and event-order verification.
- Concurrency reuses late-result ownership and cancellation guidance, with explicit operation-ordering expectations.
- Idempotency reuses the existing logical-operation key, payload/scope binding, atomic deduplication, and unknown-outcome recovery contract.
- Invariants and atomicity extend the API/data reference with concurrent enforcement and partial-failure recovery.
- Timeouts, retries, and cancellation reuse the existing reliability and boundary-regression guidance.
- Authorization reuses the existing security guidance for server-derived identity, resource substitution, field access, and valid authorized controls.
- Optimistic UI extends the API/data reference with mutation-aware rollback, authoritative reconciliation, and fresh-read verification. React guidance routes to that owner.
- Resource lifecycle extends the reliability reference with ownership, partial initialization, shared consumers, and repeated teardown verification.
- Compatibility extends the API/data reference with supported version combinations, rollout sequencing, and representative old/new records.
- Observability and isolation extend the reliability reference with correlated outcomes, safe diagnostics, dependency recovery, and required-versus-optional failure handling.

Cursor rules remain activation stubs. Detailed contracts live in the existing shared references, mirrored for Codex and Cursor packaging. Application-specific permissions, data semantics, and deployment decisions stay in each app.

## 1. Implicit state machines

```text
Use $review-correctness and the implicit-state-machine guidance to inspect this app's important workflows. Find reachable contradictory states, invalid transitions, and missing recovery paths across UI, async work, and persisted state. Fix demonstrated bugs with the smallest suitable state representation and guards. Preserve independent state dimensions and supported flows. Add focused regression tests for the triggering event order and recovery. Report evidence, fixes, verification, and unresolved hypotheses.
```

## 2. Concurrency and stale results

```text
Use $review-reliability-performance to inspect overlapping requests, streaming updates, navigation, and concurrent edits in this app. Find stale completions, lost updates, and races between cancellation and completion. Establish the intended ordering and ownership rules, then fix demonstrated failures using existing request identity, versioning, or synchronization mechanisms. Preserve legitimate parallel work. Add deterministic tests for adverse completion orders and report verified outcomes and remaining gaps.
```

## 3. Idempotency and duplicate actions

```text
Use $review-api-data-distributed to trace replay-prone mutations, retries, and message consumers. Check logical-operation identity, authorized scope, payload conflicts, atomic claims, and recovery after an unknown outcome. Fix demonstrated duplicate side effects with the existing persistence and deduplication mechanisms. Preserve valid repeated business actions. Test concurrent duplicates and retries around the commit boundary. Report confirmed defects, minimal fixes, and verification.
```

## 4. Invariants and atomic updates

```text
Use $review-api-data-distributed to identify important relationships that must remain true across this app's records and side effects. Trace their authoritative write boundaries and find reachable partial updates or concurrent violations. Fix demonstrated failures with existing transactions, constraints, conditional writes, or recovery paths. Preserve valid workflows and data. Test competing requests and injected partial failures against an appropriate isolated dependency. Report the invariant, fix, and verification limits.
```

## 5. Timeouts, retries, and cancellation

```text
Use $review-reliability-performance and the boundary-failure guidance where applicable to inspect external calls and long-running work. Trace deadlines, layered retries, cancellation propagation, unknown outcomes, and work that continues after the caller returns. Fix demonstrated hangs, retry amplification, late effects, or leaked capacity with minimal changes. Preserve legitimate recovery. Test actual underlying completion and cleanup using controlled failures. Report evidence, verification, and remaining uncertainty.
```

## 6. Authorization and ownership boundaries

```text
Use $review-security to trace this app's real routes, resource lookup, storage access, background jobs, and mutations. Find demonstrated gaps in server-derived identity, permissions, tenant or ownership scope, and field-level access. Preserve intentionally shared access and the established authentication architecture. Fix confirmed issues locally. Add denied-substitution tests paired with valid authorized controls and verify persisted effects. Report affected boundaries, evidence, fixes, and remaining gaps.
```

## 7. Data consistency and optimistic UI

```text
Use $review-api-data-distributed and the app's framework guidance to trace optimistic mutations across detail views, lists, caches, and saved state. Find rollback that erases newer edits, stale refreshes, and success displays unsupported by persistence. Fix demonstrated inconsistencies through existing mutation, invalidation, and reconciliation mechanisms. Preserve current interaction behavior. Test overlapping success/failure orders and a fresh authorized reload. Report evidence, fixes, and verification.
```

## 8. Resource lifecycle and cleanup

```text
Use $review-reliability-performance to trace ownership of this app's subscriptions, timers, connections, streams, tasks, temporary resources, and database sessions. Find leaks, duplicate registration, cleanup races, and premature release of shared resources. Fix demonstrated problems with existing lifecycle mechanisms. Test repeated setup/teardown, partial initialization failure, cancellation, and late completion using observable effects or resource counts. Report minimal fixes and remaining verification gaps.
```

## 9. Contracts and compatibility

```text
Use $review-api-data-distributed to inspect contracts between this app's clients, APIs, queued work, and stored records. Identify supported version combinations and find demonstrated breakage in validation, defaults, nulls, enums, error shapes, or migrations. Fix affected readers, writers, or migration steps using the established rollout strategy. Preserve supported existing data and rollback paths. Test representative old/new payloads and records. Report compatibility boundaries, fixes, and verification.
```

## 10. Observability and failure isolation

```text
Use $review-reliability-performance to trace representative failures across this app's request, job, and dependency boundaries. Find missing operation correlation, misleading success, swallowed failures, and optional dependency failures that break unrelated work. Fix demonstrated diagnostic or isolation gaps through existing logging, error handling, and resource controls. Preserve privacy and fail-closed authorization and integrity checks. Test failure, recovery, and unaffected workflows. Report evidence, minimal fixes, and verification.
```
