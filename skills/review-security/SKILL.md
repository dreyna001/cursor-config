---
name: review-security
description: Review security-sensitive code for risks in input, secrets, auth, APIs, dependencies, infra, deployment, and LLM boundaries.
---

# Review Security

Use this skill for security-focused review.

For browser/backend trust boundaries, apply [application security](../cursor-rules/references/security.md) and its matching installed-framework guidance. Trace content rendering, credential forwarding, sensitive caches, resource authorization, files, and outbound requests together; preserve the approved authentication and private-integration architecture.

For production HTTP security exposure review, read [API abuse and exposure](../cursor-rules/references/api-abuse-and-exposure.md) for the applicable controls and project checkpoints. Apply its production scope and distinguish source/template findings from live deployment evidence.

## Focus

- injection
- path traversal
- unsafe deserialization
- SSRF
- regex DoS
- unsafe dynamic execution
- authn/authz flaws
- IDOR or BOLA
- tenant isolation
- secret exposure
- weak crypto
- poor key handling
- missing schema validation
- missing size limits
- missing production request quota on a served route, including health, readiness, liveness, metrics, docs/schema, login, and static files; preserve local protections without retrofitting production deployment controls unless requested
- missing replay protection
- risky dependency or platform defaults
- LLM output used without validation

## Review Rules

- Prioritize realistic, evidence-backed findings.
- Separate direct evidence from inference.
- Mark unknowns as `unknown`.
- Do not overstate exploitability beyond observed evidence.
- Identify the affected trust boundary.
- State whether the issue should block merge.

## Output

For each finding, return:
- severity
- finding
- why it matters
- direct evidence
- affected trust boundary
- attack path or exploitability
- recommended mitigation
- confidence
- block merge: yes/no
