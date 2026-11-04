---
name: boundary-failure-regressions
description: "Use for reproduced software-boundary or durable-state regressions involving parsing, API errors, timeouts, or cancellation. Apply llm-evidence-regression to LLM evidence and output-contract aspects when relevant."
---

# Boundary Failure Regressions

Use this for a concrete failure or contract violation at an application boundary or in durable state. For LLM evidence, output-contract, grounding, or quality-evaluation changes, also apply `llm-evidence-regression`; when a failure spans both areas, use each skill only for its relevant part. Routine feature work and documentation do not need this workflow.

- Establish the failing request or operation from its real input, transport, and contract. Separate product behavior from guessed routes, client-side sanitization, fixture mistakes, or aggregate scores.
- Trace where invalid state first appears and fix that boundary. Validate decoded or normalized input before side effects, preserve meaningful error classes, and avoid broad catches or relaxed checks that hide the cause.
- Put timeout and cancellation bounds on the operation that waits. A caller timeout alone does not prove the work stopped. Settle or track in-flight work before releasing its transaction, session, or lock; check for late or duplicate effects and durable-state damage.
- When request semantics matter, exercise the registered route and the payload received by the server. If a client rejects or sanitizes input, use a suitable transport-level fixture to test server behavior.
- Choose the narrowest existing test layer: unit tests for deterministic parsing, existing auth/database/storage integration for durable behavior, and in-process service doubles with production-shaped protocols for outbound calls. Check the response and reload state when it persists.
- Pair failures with valid controls nearby: supported defaults and omitted optional fields, representative records, ordinary Unicode and whitespace, valid retries, and existing user edits. Confirm the fix preserves those paths.
- Keep fixes and seeded corpora bounded. Fuzz or load results cover included scenarios; they do not establish exhaustive safety, general correctness, or production capacity.
- Reuse existing boundaries and harnesses. Do not expand one regression into an unrelated migration, policy change, or architecture rewrite. Prefer isolated fixtures; use live services or production/customer data only within the user's existing explicit scope and authorization, following applicable review gates without adding a new confirmation step.
