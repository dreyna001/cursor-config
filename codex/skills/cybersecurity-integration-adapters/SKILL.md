---
name: cybersecurity-integration-adapters
description: "Design thin adapters for cybersecurity systems such as SIEM, SOAR, ticketing, GRC, scanners, cloud APIs, and identity platforms."
---
# Cybersecurity Integration Adapters

Use this skill when connecting a cybersecurity workflow to an external system such as Splunk, ServiceNow, Archer, a scanner, a CMDB, a cloud API, or a threat-intel platform.

## Quick Start

Follow this sequence:

1. Define what the workflow needs from the external system.
2. Split the integration into read, writeback, and action-taking operations.
3. Create a thin adapter for the system or API surface.
4. Normalize vendor-specific request and response shapes into stable internal objects.
5. Keep auth, config, retries, and error translation inside the adapter.
6. Keep workflow logic, policy checks, and approvals outside the adapter.
7. Add fake-response or fixture tests for the adapter contract.

For policy classification, allowlists, and approval boundaries, use [cybersecurity-approval-policy-gates](../cybersecurity-approval-policy-gates/SKILL.md). Keep those decisions outside the adapter.

For Splunk SDK use, SPL search construction, or search-job lifecycle work, read [Splunk SDK and SPL production guidance](references/splunk-production.md).

## Core Rules

- Treat adapters as **transport and normalization layers**, not orchestration layers.
- Do not scatter vendor API calls throughout business logic.
- Keep environment-specific details out of workflow code.
- Expose typed errors so orchestration can distinguish retryable, authentication, validation, rate-limit, and not-found failures. Keep policy denials in the policy layer.
- Separate one vendor integration into distinct operations when risk differs, such as read-only search vs writeback vs action.

## What To Define

For each adapter, define:

- external system name
- supported operations
- auth/config inputs
- normalized internal request shape
- normalized internal response shape
- retry and timeout behavior
- error taxonomy
- rate-limit behavior

## Good Boundaries

Keep in the adapter:

- HTTP or SDK calls
- auth and credential handling
- request construction
- response parsing
- rate-limit handling
- timeout and retry behavior

Keep out of the adapter:

- case reasoning
- approval decisions
- policy allow or deny logic
- workflow branching
- prompt construction

## Testing Guidance

- use stubs, fixtures, or fake responses
- cover success, authentication failure, transient and rate-limit failures, validation failure, not-found responses, and malformed responses
- avoid live-system dependence for basic contract tests

## Preferred Outcome

Aim for **one clean integration boundary per system**, reusable across multiple cybersecurity workflows and domains.
