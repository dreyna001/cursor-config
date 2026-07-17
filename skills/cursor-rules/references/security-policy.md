---
description: Use for security-sensitive changes: auth, IAM, secrets, input validation, infra, writeback, actions, approval gates, or policy enforcement
alwaysApply: false
---

# Security And Policy Rules

## Security Baseline

- Treat all external input as untrusted.
- Validate schema, type, format, size, path, URL, identifiers, and model output before use.
- Never build queries, shell commands, file paths, or execution plans directly from untrusted input.
- Prevent injection, unsafe deserialization, SSRF, path traversal, regex DoS, and unsafe dynamic execution.
- Enforce authentication, authorization, least privilege, and tenant or ownership isolation server-side.
- Use approved crypto and secure randomness only.
- Avoid insecure defaults, overly permissive exposure, and verbose internal errors.

## Secrets

- Never commit secrets, tokens, API keys, session cookies, or plaintext credentials.
- Use secure config, env injection, Secrets Manager, SSM, or equivalent secret stores.
- Redact secrets in logs, examples, fixtures, and error messages.
- Do not place long-lived credentials in images, unit files, compose files, scripts, or committed config.

## Least Privilege

- Grant minimum required permissions.
- Avoid wildcard IAM actions/resources unless justified and documented.
- Scope credentials and policies to specific actions, resources, and conditions.
- Separate read-only, writeback, and action-taking permissions.

## Infra Security

- Bind sensitive inference/admin APIs to loopback unless a documented authenticated edge listener is required.
- Run services as dedicated unprivileged users where supported.
- Use minimal filesystem permissions consistent with the stack.
- Prefer explicit restart behavior, health checks, and idempotent installers.
- Verify TLS by default; disabling verification is only allowed for documented lab paths.

## Approval And Policy Gates

- Separate read-only retrieval, writeback, and action-taking behavior as distinct risk classes.
- Put deterministic policy validation before generated queries, updates, or actions reach external systems.
- Keep allowlists, deny rules, budgets, time bounds, scope caps, and approval requirements in code or versioned policy, not only prompt text.
- Require explicit approval boundaries for consequential writes, state changes, escalations, suppressions, or response actions.
- If policy blocks execution, return a structured reason.
- Log enough metadata for auditability without exposing secrets or sensitive payloads.