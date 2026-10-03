---
name: cybersecurity-integration-policy
description: "Design cybersecurity integrations with explicit policy validation, approvals, and safe execution boundaries."
---
# Cybersecurity Integration And Policy

Use this skill when connecting cybersecurity workflows to external systems or adding execution/writeback/action gates.

## Adapter Workflow

1. Define what the workflow needs from the external system.
2. Split operations into read-only, writeback, and action-taking.
3. Create a thin adapter for the system or API surface.
4. Normalize vendor request and response shapes into stable internal objects.
5. Keep auth, config, retries, rate limits, and error translation inside the adapter.
6. Keep workflow logic, policy checks, approvals, and prompts outside the adapter.
7. Add fake-response or fixture tests for the adapter contract.

## Adapter Rules

- Treat adapters as transport and normalization layers, not orchestration layers.
- Do not scatter vendor API calls throughout business logic.
- Keep environment-specific details out of workflow code.
- Expose typed errors for retryable, auth, validation, rate-limit, not-found, and policy failures.
- Separate operations when risk differs.

## Define For Each Adapter

- external system name
- supported operations
- auth/config inputs
- normalized request shape
- normalized response shape
- timeout behavior
- retry behavior
- error taxonomy
- rate-limit behavior

## Policy Workflow

1. Classify each operation as read-only, writeback, or action-taking.
2. Define allowed, approval-gated, and prohibited operations.
3. Add policy validation before generated queries, updates, or actions execute.
4. Express allowlists, deny rules, budgets, and scope limits in code or versioned policy.
5. Return structured block reasons when policy denies execution.
6. Add audit-friendly logs and tests for allowed and denied cases.

## Policy Controls

- command or API allowlists
- index, tenant, or system scope limits
- time bounds
- result count limits
- cost or complexity caps
- approval-required flags
- prohibited state transitions
- environment-specific restrictions

## Testing

Cover:
- success
- auth failure
- transient failure
- validation failure
- malformed response
- explicitly allowed policy case
- explicitly denied policy case
- missing approval case

## Preferred Outcome

Clean integration boundaries with policy-gated automation where operators can tell what is safe, what requires approval, and what is prohibited.