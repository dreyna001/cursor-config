---
description: Security review baseline
alwaysApply: false
---

# Security

- Treat all external input as untrusted and validate at boundaries.
- Never build queries or shell commands from untrusted input.
- Validate and normalize file paths, URLs, identifiers, and model output before use.
- Prevent injection, unsafe deserialization, SSRF, path traversal, and regex DoS where applicable.
- Enforce authentication, authorization, least privilege, and tenant or ownership isolation server-side.
- Never hardcode secrets or log tokens, credentials, or sensitive data.
- Use approved crypto and secure randomness only.
- Require schema validation and request-size limits where payload abuse is plausible.
- Avoid overly permissive exposure, verbose internal errors, and insecure defaults.
- Do not trust LLM output without validation before persistence, execution, or security-sensitive use.
