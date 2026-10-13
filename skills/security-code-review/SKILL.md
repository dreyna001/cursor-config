---
name: security-code-review
description: "Review security-sensitive code for risks in input, secrets, auth, APIs, dependencies, infrastructure, deployment, and LLM boundaries; not the built-in Security Review subagent."
---
# Security Code Review

Use this skill for a focused security review performed in the current agent. Use the built-in `review-security` skill only when the user explicitly asks for the Security Review subagent.

For browser/backend trust boundaries, apply [application security](../cursor-rules/references/security.md) and its matching installed-framework guidance. Trace content rendering, credential forwarding, sensitive caches, resource authorization, files, and outbound requests together; preserve the approved authentication and private-integration architecture.

For production HTTP security exposure review, read [API abuse and exposure](../cursor-rules/references/api-abuse-and-exposure.md) and, only for its named repositories, [project HTTP security checkpoints](../cursor-rules/references/api-project-checkpoints.md). Apply their production scope and distinguish source/template findings from live deployment evidence.

For an LLM or tool boundary, apply [LLM boundaries](../cursor-rules/references/llm-boundaries.md). Do not restate its channel or injection checks.

Run a scanner only when it is already installed or already configured in CI: secret scan, `pip-audit` or `npm audit`, Bandit or Semgrep, Checkov, or Trivy. Report ran, failed, skipped, or not installed. Do not install one to finish the review. Judge hits using the application security rule's scanner qualification.

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
- LLM or tool boundary that skips the LLM boundaries rule

## Review Rules

- Prioritize realistic, evidence-backed findings.
- Separate direct evidence from inference.
- Mark unknowns as `unknown`.
- Do not overstate exploitability beyond observed evidence.
- Treat scanner severity, similarity matches, and route status codes as triage signals. Trace the relevant request through routing, authentication, authorization, and the sensitive operation before reporting an exploitable issue; a method mismatch or status code alone does not establish an access-control flaw.
- Analyze credential mechanisms separately. Cookie-backed sessions and other ambient browser credentials need CSRF analysis; explicit bearer headers have different attachment behavior, so assess their storage, theft, and forwarding risks on their own. Do not infer one mechanism's protections from another's.
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
