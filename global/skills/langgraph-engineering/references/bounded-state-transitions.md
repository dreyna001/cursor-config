# Bounded State Transitions

Read this reference when a workflow updates bounded durable snapshots, queue lineage, retained history, or overflow receipts. Use the project's current contracts and limits; this guidance does not set universal field sizes or byte caps.

## Keep projections authoritative

When a transition admits, defers, drops, or otherwise omits an item, update the authoritative lineage/projection on every path. Do not rely on a transient queue to stand in for persisted provenance if later validators, resume paths, or reports read a separate projection. Validate that new dependencies refer to known, completed or otherwise contract-authorized identities; reject unknown and future IDs.

If a transition is split into helpers, keep one final validation and commit boundary for the coherent state change. Track the source-of-truth fields alongside the derived queue, answer/history references, active members, and overflow summary so they cannot drift on only one branch.

## Bound the serialized state, including recovery metadata

Measure the complete serialized model that will be constructed and stored, including digests, omission counts, newly defaulted fields, and references. Checking only the incoming payload can miss a failure when overflow metadata itself pushes a previously valid object over its contract limit.

At a size boundary, preserve the prior valid state and its provenance. If the full new state cannot fit, use the contract's explicit omission/overflow receipt. If that receipt also cannot fit in the bounded projection, record it in an existing durable terminal or transition record, or another established bounded metadata surface; do not silently drop it, double-count it on replay, or raise the cap just to admit the transition. Preserve compatibility with historical payloads that omit fields added later by using the established defaults and migration behavior.

## Verify the transitions that can drift

Choose focused cases that follow the authoritative data across boundaries: a multi-hop dependency from a generated item to its follow-up, rejection of an unknown dependency, queue admission followed by cap-driven omission, and a prior state just below its size limit whose new receipt would exceed it. Where replay is supported, repeat the same transition and check that lineage and omission counts remain stable. Also check the downstream report or projection when it consumes the bounded history. Test only the limits and branches relevant to the change; do not hard-code another project's cap values or require an unrelated full suite.

When a test double participates in staged planning, preserve the required scope,
application-assigned identities and other bindings supplied with the next request.
Generate new timestamps or identities only where the real contract permits it.
Keep deliberately invalid responses explicit, and check initial drafts and valid
follow-up drafts without depending on both calls occurring in the same clock tick.
