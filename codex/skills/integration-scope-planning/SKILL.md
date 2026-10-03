---
name: integration-scope-planning
description: "Decide which external integrations are required now, later, or not at all for the current block."
---
# Integration Scope Planning

Use this skill when:
- deciding whether to integrate with external systems
- planning AWS vs on-prem edges
- preventing premature platform coupling

## Objective

Select only the external integrations that are necessary for the current block.
Do not add integrations for completeness or future-proofing.

## Process

1. List the current workflow step being implemented.
2. Identify which external systems are authoritative.
3. For each possible integration, classify it as:
   - required now
   - optional now
   - later phase
   - out of scope
4. Identify whether the integration is read-only, write-only, or bidirectional.
5. Identify any customer-specific assumptions.
6. Recommend the smallest workable integration path.
7. Note a fallback path such as CSV, local file input, or manual export/import when appropriate.

## Output format

Return these sections:
- Current block
- Candidate integrations
- Required now
- Optional now
- Later phase
- Out of scope
- Minimum viable integration plan
- Risks

## Constraints

- Do not recommend deep bidirectional sync unless the block truly needs it.
- Do not replace existing systems of record.
- Do not add vendor-specific complexity without a current operational need.
- Prefer thin, explicit integrations over broad platform entanglement.
