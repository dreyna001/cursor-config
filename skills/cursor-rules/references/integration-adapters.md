---
description: Use for external APIs, cybersecurity integrations, data boundaries, distributed systems, adapters, retries, pagination, and vendor normalization
alwaysApply: false
---

# Integration Adapter Rules

## Adapter Boundaries

- Keep external systems behind thin adapter boundaries.
- Treat adapters as transport and normalization layers, not workflow or policy layers.
- Prefer one adapter per system or API surface.
- Do not scatter vendor calls throughout business logic.
- Keep environment-specific URLs, tenants, field mappings, credentials, auth, retries, rate limits, and error translation out of workflow code.

## Normalization

- Normalize external request and response shapes into stable internal objects before business logic uses them.
- Expose typed failures so orchestration can distinguish retryable, validation, auth, rate-limit, not-found, and policy errors.
- Separate read, writeback, and action-taking operations even when they hit the same vendor system.

## API And Data Contracts

- Require explicit schemas and consistent response/error shapes at boundaries.
- Plan versioning or migration when changes can break clients or stored data.
- Review pagination, filtering, request growth, serialization, and request-size limits.
- Avoid duplicate sources of truth and weak constraints.
- Review transaction boundaries, orphaned records, soft-delete correctness, and unsafe migrations where applicable.

## Distributed Behavior

- Assume retries, duplicate delivery, imperfect clocks, partial failure, and out-of-order events.
- Require idempotency for replay-prone writes and consumers.
- Flag lost updates, double processing, ordering assumptions, deadlocks, retry amplification, and duplicate side effects.
- Define retry ownership explicitly.
- Add adapter tests with fake responses or fixtures; do not rely on live vendor systems for basic contract coverage.