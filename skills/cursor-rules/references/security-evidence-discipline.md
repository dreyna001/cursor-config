---
description: Security posture, evidence handling, and safe handling of untrusted input
alwaysApply: false
---

# Security and Evidence Discipline

- Treat **untrusted input** (alerts, uploads, API bodies, model output) as untrusted: validate, normalize, and avoid dangerous patterns (injection, path traversal, unsafe `eval` / `literal_eval` except on strictly bounded model-output paths as already documented in code).
- **Do not fabricate** IOCs, events, IDs, or findings. Mark unsupported factual claims as `unknown` or omit per contract.
- **Evidence vs inference:** label or separate analyst conclusions from raw source material; do not present inference as ground truth.
- **Secrets:** never log tokens, API keys, session cookies, or raw auth headers. Redact in examples and test fixtures.
- Prefer **fail-closed** behavior for security-sensitive branches; document intentional fail-open paths (e.g. optional RAG) and add observability where degradation occurs.
