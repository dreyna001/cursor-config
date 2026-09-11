---
description: AWS Lambda and serverless least-privilege and consistency
alwaysApply: false
---

# AWS / Lambda Least Privilege and Consistency

- Grant IAM permissions **narrowly** to what the function needs (specific actions, resources, and conditions). Avoid `*` on resources unless justified and documented.
- Do not commit **secrets**; use environment variables from secure config, Secrets Manager, or SSM as appropriate—not plaintext in repo or in Lambda env in source control.
- Keep **handler contract, env var names, and event shapes** aligned across code, Terraform, and README or runbooks.
- Use **structured logging** with correlation where useful; avoid logging full payloads that may contain secrets or PII.
- **Timeouts, memory, and retry semantics** should match downstream limits; document partial-failure behavior for async or fan-out patterns.
