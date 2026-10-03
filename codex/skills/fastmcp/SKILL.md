---
name: fastmcp
description: "Build or review Python FastMCP tools, resources, clients, and deployments; use for MCP integration work."
---
# FastMCP

## Workflow

1. Inspect the installed FastMCP version and existing project patterns; verify version-specific APIs from authoritative documentation.
2. Confirm MCP is a justified interoperability boundary, not an internal abstraction.
3. Define the smallest typed tool/resource contracts required.
4. Implement authentication, authorization, validation, limits, and auditability.
5. Test contracts, failures, cancellation, and deployment transport.

## Design rules

- Keep business policy and orchestration in the application; MCP handles protocol, authorization, transport, and normalization.
- Prefer a few capability-oriented tools over CRUD wrappers or one tool per query permutation.
- Use explicit Pydantic-compatible inputs and structured outputs with stable error contracts.
- Treat tool descriptions as model guidance, never as security enforcement.
- Validate every argument; bound time, concurrency, rows, bytes, and response size.
- Keep credentials server-side. Redact secrets and sensitive payloads from errors, logs, and traces.
- Make read-only, write, and consequential tools distinct. Require approval for consequential actions and fail closed on uncertain authorization.
- Preserve source identity, provenance, truncation, and limitations in returned evidence.
- Use dependency/lifespan-managed shared clients; do not create external clients per invocation.
- Avoid hidden state. If sessions are required, define ownership, expiry, replay, and recovery explicitly.
- Use stdio for local process integrations and streamable HTTP for remote services unless the deployment requires otherwise.
- Add no framework, proxy, gateway, or distributed service without a demonstrated requirement.

## Verification

- Test tool discovery and schemas.
- Test valid, malformed, unauthorized, oversized, timed-out, cancelled, and upstream-failure calls.
- Use fakes for external systems; keep live tests explicitly integration-scoped.
- Verify transport, TLS, authentication, health, and shutdown behavior in the target deployment.
- Confirm MCP cannot bypass application policy, approval gates, budgets, tenancy, or audit records.
