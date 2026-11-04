# Durable Admission and Recovery

Read this reference when a LangGraph path admits database-backed work, tracks paid provider usage, or retries/reconciles external actions. Keep the workflow's existing contracts and permissions authoritative.

## Preserve one admission boundary

Treat a capacity decision as a transaction over the current execution fence, resource usage, reservations, and durable action identity. Acquire locks in a stable order, revalidate the worker generation after lock waits, calculate against both settled usage and outstanding reservations, and write the batch, actions, and reservations in the same transaction. A failure partway through a multi-member admission must roll back the entire admission unless partial grants are an explicit contract.

Pure validation, grant calculation, replay mapping, and persistence mapping can be extracted when they have clear inputs and outputs. Keep the connection, transaction, fence checks, and lock order owned by the admission operation; a helper must not introduce an independently committed half-state. Check all callers, including legacy or single-action paths, before changing a shared adapter.

## Treat uncertain external outcomes as unresolved

Give each external action a stable identity bound to its canonical request. If submission may have reached the provider but its acknowledgment was lost, reconcile by the exact action identity and provider metadata before retrying. Do not submit again merely because the local result is missing. Keep the action and its reservations/usage accounting unresolved until authoritative evidence establishes whether it ran and what it cost; release or charge only under the documented accounting rule.

Fence every artifact, action, and checkpoint mutation at the mutation boundary against the current execution generation. An earlier lease check does not prevent a stale worker from writing after replacement. For multi-table state, apply the fence and related writes atomically or use the storage system's established equivalent.

## Verify the claim against the right storage

Use focused synthetic tests for route selection and pure policy. When a claim depends on database locking, rollback, concurrent admission, stale generations, or persisted replay, qualify it with the actual supported database backend and representative failure path. A fake store cannot establish transaction isolation or database lock behavior. Choose the relevant cases for the change rather than running an unrelated full matrix.

Measure runtime performance directly with representative workloads. Function length can reveal mixed responsibilities, but it is not evidence of latency or throughput. Extract a helper when it improves a real responsibility boundary or enables meaningful focused verification, and preserve observable behavior and transaction boundaries.
