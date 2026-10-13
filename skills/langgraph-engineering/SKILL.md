---
name: langgraph-engineering
description: "Design, implement, migrate, or review LangGraph applications with explicit state, durable execution, model/tool boundaries, and recovery. Use for LangGraph workflow engineering and migration reviews, not unrelated application changes or general framework comparisons."
---

# LangGraph Engineering

When this skill is invoked for LangGraph work, read and apply [Original Conditional LangGraph Guidance](references/original-langgraph-guidance.md) together with the workflow below.

## Establish the contract

Read the user's requested outcome and relevant project architecture documents. Inspect the implementation and dependency lock before assuming a framework version, persistence backend, provider, or migration stage. Keep confirmed behavior, proposed design, and completed qualification distinct.

Check the project's Python requirement and actual local, CI and deployment interpreters against package compatibility metadata. Record the exact interpreter and package versions used for qualification. Keep project pins in dependency files and design records; do not prescribe one Python or LangGraph version globally.

Check version-sensitive APIs against primary sources:

- [Graph versus Functional API](https://docs.langchain.com/oss/python/langgraph/choosing-apis): choose the representation that makes the actual workflow understandable. Explicit graphs often suit branching stateful workflows; do not mandate them for every task.
- [Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api) and [usage](https://docs.langchain.com/oss/python/langgraph/use-graph-api): state updates, reducers, routing and validation limitations.
- [Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers), [interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts), and [compatibility](https://docs.langchain.com/oss/python/langgraph/backward-compatibility): recovery and upgrade behavior.
- [Maintainer advisories](https://github.com/langchain-ai/langgraph/security/advisories): inspect the relevant core, serializer, saver/store and optional SDK packages when selecting or upgrading dependencies.

Read only the references needed for the task. Use the installed version's behavior when moving documentation and examples differ. Do not introduce a hosted platform, agent factory, provider wrapper, or extra service solely because a tutorial uses it.

## Design or implement a complete slice

Identify the affected path's:

- Domain completion criteria, separately from node execution status.
- State fields, writers, reducers, routes and joins; explicit validation of outputs.
- External effects, stable action IDs, admission limits, uncertain outcomes and restart points.
- Persistence ownership and transaction boundaries between application artifacts, usage and graph checkpoints/pending writes.
- Model context, tool/proposal contracts, usage normalization and provider-specific failure behavior.

Reuse application services that meet the target behavior. Redesign incompatible orchestration instead of wrapping a whole existing loop in a node. Preserve one authority for external-call accounting and retries. Keep runtime clients and credentials out of persisted state, and avoid growing checkpoints with every raw result when references suffice.

For concurrency, cover both graph merges and database admission; graph-local concurrency does not enforce a deployment-wide limit. For interrupts, distinguish a paused graph from a failed job and preserve the application's approval contract. For memory and context, preserve provenance and uncertainty through summaries, and separate retrieval completeness from evidence supplied to a model.

## Review and verification

Select checks for the requested change and existing project guarantees. When verification is requested, use offline/synthetic adapters first, then the actual persistence backend for transaction and recovery claims. Use live external systems only within the user's authorized scope.

For database-backed action admission, provider usage accounting, or replay/reconciliation changes, also read [Durable admission and recovery](references/durable-admission-and-recovery.md). It focuses on transaction and fencing boundaries that must survive helper extraction.

For bounded scheduler snapshots, lineage projections, or history/overflow logic, read [Bounded state transitions](references/bounded-state-transitions.md). It focuses on source-of-truth updates and serialized-size recovery at contract boundaries.

Relevant failure cases include invalid node output, unintended duplicate routes, conflicting parallel updates, stale workers, lost acknowledgments, partial branch success, interrupted-node replay, exhausted retries, cancellation during synchronous calls, incompatible checkpoints, and private state exposed by streaming. Choose applicable cases; do not turn every change into a universal checklist or require new approvals for already authorized work.

Report changes, observed results, failures/skips and remaining qualification gaps. Update project implementation status only when the behavior is implemented and verified. Maintain general guidance globally; keep dated project findings in project documents. Add repository rules only for necessary project-specific constraints.
