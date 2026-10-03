---
name: cybersecurity-approval-policy-gates
description: "Design policy gates, allowlists, approvals, and safe execution boundaries for cybersecurity workflows."
---
# Cybersecurity Approval And Policy Gates

Use this skill when a cybersecurity workflow may move from analysis into execution, writeback, state changes, or actions.

## Quick Start

Follow this sequence:

1. Classify each operation as read-only, writeback, or action-taking.
2. Define which operations are allowed, approval-gated, or prohibited.
3. Add policy validation before any generated query, update, or action executes.
4. Express allowlists, deny rules, budgets, and scope limits in code or versioned policy.
5. Return structured block reasons when policy denies execution.
6. Add audit-friendly logs and tests for allowed and denied cases.

## Core Rules

- Separate **policy logic** from orchestration, prompt construction, and adapters.
- Prefer **fail-closed** behavior when policy is uncertain.
- Require explicit approval boundaries for consequential writes or actions.
- Keep read-only execution distinct from writeback and action-taking behavior.
- Use policy checks even when a human eventually approves the result.
- Do not let prompt text be the only place where safety rules live.

## What To Define

For each risky capability, define:

- operation name
- risk class
- allowed conditions
- prohibited conditions
- approval requirement
- scope limits
- time or cost budget
- structured denial reason

## Typical Policy Controls

- command or API allowlists
- index, tenant, or system scope limits
- time bounds
- result count limits
- cost or complexity caps
- approval-required flags
- prohibited state transitions
- environment-specific restrictions

## Testing Guidance

- test explicitly allowed cases
- test explicitly denied cases
- test missing-approval cases
- test invalid combinations
- test structured denial output

## Preferred Outcome

Aim for **clear policy-gated automation** where operators can tell what is safe, what needs approval, and what is prohibited across domains.
