---
name: operator-documentation-journey
description: "Create or review operator and deployment documentation organized as a clear README-first journey."
---
# Operator Documentation Journey

Simplify and consolidate existing documentation. Do not add net documentation unless the requested behavior has no current home. Preserve executable commands, gates, contracts, and failure behavior.

## Ownership

| Owner | Responsibility |
| --- | --- |
| Root `README.md` | Product summary, boundaries, approval gate, Path A/B/C order, entry commands, validation terminus, rollback versus teardown |
| `docs/README.md` | Topic index that links back to the root journey |
| Configuration reference | Complete environment or parameter contract |
| Profile or capability guide | Profile mappings and exclusions |
| Deployment runbook | Build, deploy, rollback, and validation for one stack |
| Testing guide | Smoke, staging, and contract-test commands |

Keep one canonical document per topic; use short links elsewhere. Each runbook should cover one concern, state its purpose at the top, and include `## Next` when it belongs to a journey.

## Workflow

1. Trace every supported path from the root README through validation and identify duplicate or competing entry points.
2. Assign a canonical owner before editing.
3. Make the root README the journey, trim indexes and runbooks to their owned concerns, preserve copyable commands, and add clear `## Next` handoffs.
4. Check links and anchors, update existing documentation contract tests when required, run relevant validation, and confirm rollback is not confused with teardown.

Each root path should explain why each linked step exists and end at one validation destination.

## Preserve

- supported cloud, region, partition, or platform boundaries
- approval before live mutations
- deployment order and immutable release identifiers
- authentication, authorization, tenant isolation, network, and encryption contracts
- environment, profile, retry, replay, and dead-letter behavior
- destructive-operation gates and known platform limits

## Done When

A new operator can start at the root README, follow one path in order, and finish at validation without searching the repository. Duplicate journey prose is removed, navigation works, safety contracts remain, and relevant tests pass.

Report what changed, the ownership decisions, duplication removed, contracts preserved, verification performed, and any intentional exclusion.
