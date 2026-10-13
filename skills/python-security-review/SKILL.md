---
name: python-security-review
description: "Review Python changes for security risks around input, subprocesses, secrets, auth, file I/O, APIs, and deployment."
---
# Python Security Review

For web/API boundaries, apply [application security](../cursor-rules/references/security.md) and the matching installed-framework reference. Include authorization for indirect file/export access, sensitive response/cache behavior, parser bounds, and approved outbound destinations; inspect the frontend when it controls the sink or credential flow.

## Use This When
- Reviewing Python code or pull requests for security risk.
- Validating safe handling of untrusted input, secrets, and external calls.
- Assessing deployment or runtime contract changes that can impact security.

## Review Principles
- Prioritize realistic, evidence-backed findings over speculative risks.
- Keep direct evidence separate from inference.
- Mark unknown data explicitly as `unknown`.
- Do not overstate exploitability beyond observed evidence.

For production HTTP security exposure review, read [API abuse and exposure](../cursor-rules/references/api-abuse-and-exposure.md) and, only for its named repositories, [project HTTP security checkpoints](../cursor-rules/references/api-project-checkpoints.md). Apply their production scope and distinguish source/template findings from live deployment evidence.

## Workflow
1. Identify trust boundaries and untrusted entry points.
2. Check for unsafe execution patterns:
   - `eval` or `exec`
   - `shell=True`
   - unsafe deserialization
   - unsafe temporary file handling
3. Check for secrets exposure:
   - hardcoded credentials or tokens
   - sensitive values in logs, docs, or examples
4. Validate input handling for paths, args, HTTP payloads, and IDs (allowlist or validator pattern).
5. Verify retry, timeout, and failure behavior for network, API, or model calls.
6. Confirm authentication and authorization assumptions where applicable. For production HTTP routes, apply the API abuse and exposure reference, including anonymous routes, login, health, docs/schema, and static serving. Preserve local protections without retrofitting production deployment controls into developer/test instances unless requested.
7. Separate direct evidence from inference; mark unknowns as `unknown`.
8. Do not overstate exploitability beyond evidence.
9. If the change includes a model or tool call, apply [LLM boundaries](../cursor-rules/references/llm-boundaries.md). Do not restate its checks.
10. If a scanner is already installed or configured in CI, run it and record ran, failed, skipped, or not installed. Do not install one for the review. Judge hits using the application security rule.

## Output Format
For each finding, provide:
- Finding
- Why it matters
- Direct evidence
- Recommended fix
- Confidence level
