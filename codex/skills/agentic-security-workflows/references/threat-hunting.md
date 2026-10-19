# Threat hunting

## Decision and loop

Decide whether a hypothesis has supporting or refuting evidence in an approved
environment/time window, what remains uncertain, and which leads need review.

`intent -> discover -> readable plan/scope -> analyst approval -> bounded searches
-> assess -> justified pivots -> scoped assessment/evidence -> continuation/handoff`

## Required behaviors

- Support advisory-led and hypothesis-led intake without duplicate mandatory intent
  fields. Derive missing intent for review rather than silently expanding scope.
- Discover the actual source schemas before generating query syntax. Distinguish
  multiple sources inside one SIEM from native cross-tool federation.
- Define answer requirements for each approved question. Track unsearched,
  partially answered, supported, refuted, and visibility-limited outcomes without
  treating those planning labels as facts about compromise.
- Follow entities observed in returned evidence. Carry source/query/job/time lineage
  through every pivot and preserve contradictory searches and alternative entities.
- Show a concise assessment, material attack-sequence observations, affected or
  candidate entities with their actual support, next useful actions, and gaps.
  Make source records and executed queries inspectable from the assessment.
- Keep exact raw observations in evidence storage. Rank/group them by their
  contribution to approved questions; do not inflate threat findings with every row.
- Support continuation within the approved boundary; changed scope or limits need
  the existing reapproval flow. Keep normal editing out of raw JSON.
- Preserve read-only search and immutable approval/configuration bindings. An
  optional Approve and run control must approve the exact saved/displayed plan.

## Conditional capabilities

- Recurring hunts need approved templates, relative-window semantics, ownership,
  budget per run and period, expiry, schema/scope drift handling, deduplication,
  new-versus-existing findings, and a way to stop or revoke recurrence.
- Baselines need a documented population, period, source quality, and freshness.
  Common process names, domains, successful logins, or familiar ports are not a
  benign baseline. Query-role labels are not substantive evidence.
- Add a connector when it closes a measured visibility gap. Qualify supported
  hunt operations and authorization rather than counting integrations or MCP tools.
- Detection drafts and case handoff are separate outputs; creating a draft never
  means a detection was deployed or a response action executed.

## Acceptance examples

- Failed logins followed by success and MFA change: identify supported account/IP
  relationships and ordering, show the cited events, preserve benign alternatives.
- Missing MFA telemetry: report a visibility gap rather than no MFA change.
- Reused process ID or conflicting host/boot identity: retain observations without
  falsely joining them into one execution chain.
- Truncated results or omitted context: expose the bound and retain responsive
  evidence through targeted retrieval rather than increasing every limit.
- A passing schema with an unresolved central question remains analytically partial.
- Unsaved or stale plan edits cannot result in approving a different version.

## Scope preservation

Use the active engine. Existing code for an optional or parked engine is not
permission to activate it. Do not claim full threat absence or estate coverage
from a bounded hunt. Do not add autonomous containment to a hunting workspace.
