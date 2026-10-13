---
name: capability-profile-architecture
description: "Design capability flags, feature profiles, rollout controls, and validation for modular products."
---
# Capability Profile Architecture

Use this skill when optional capabilities may vary by customer, environment, or rollout stage.

## Workflow

1. Define the capability in plain language.
2. Classify it as read-only, writeback, or action-taking.
3. Add an explicit flag or profile entry.
4. Define dependencies and incompatible combinations.
5. Default risky capabilities to off.
6. Add startup validation for invalid combinations.
7. Update env examples, docs, and tests.
8. Express customer-specific behavior as a named supported profile or bundle.

## Rules

- Treat capabilities as first-class product configuration.
- Prefer explicit flags over hidden behavior or customer-name conditionals.
- Separate coarse enablement from policy and approval logic.
- Keep read-only, writeback, and action-taking capabilities distinct.
- Fail fast on unsupported combinations.
- Prefer a small set of documented profiles over unlimited config variation.

## Define For Each Capability

- name
- purpose
- default state
- dependencies
- incompatible combinations
- approval boundary
- operator-visible config name
- docs and example config updates
- tests for enabled, disabled, and invalid combinations

## Good Profile Examples

- `analysis-only`
- `analysis-plus-rag`
- `analysis-plus-readonly-spl`
- `analysis-plus-ticket-draft`

## Avoid

- one-off undocumented env combinations
- customer-name-specific logic
- flags whose names do not describe behavior
- silent degradation into unknown states

## Preferred Outcome

Modular capabilities with validated per-customer profiles, not config sprawl.