---
name: python-security-review
description: "Review Python changes for security risks around input, subprocesses, secrets, auth, file I/O, APIs, and deployment."
---
# Python Security Review

## Use This When
- Reviewing Python code or pull requests for security risk.
- Validating safe handling of untrusted input, secrets, and external calls.
- Assessing deployment or runtime contract changes that can impact security.

## Review Principles
- Prioritize realistic, evidence-backed findings over speculative risks.
- Keep direct evidence separate from inference.
- Mark unknown data explicitly as `unknown`.
- Do not overstate exploitability beyond observed evidence.

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
6. Confirm authentication and authorization assumptions where applicable.
7. Separate direct evidence from inference; mark unknowns as `unknown`.
8. Do not overstate exploitability beyond evidence.

## Output Format
For each finding, provide:
- Finding
- Why it matters
- Direct evidence
- Recommended fix
- Confidence level
