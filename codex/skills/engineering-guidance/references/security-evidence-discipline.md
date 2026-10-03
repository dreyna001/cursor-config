---
description: Security posture, evidence handling, and safe handling of untrusted input
alwaysApply: false
---

# Security and Evidence Discipline

- **Do not fabricate** IOCs, events, IDs, or findings. Mark unsupported factual claims as `unknown` or omit per contract.
- **Evidence vs inference:** label or separate analyst conclusions from raw source material; do not present inference as ground truth.
- Preserve raw evidence or diagnostic metadata when humans must review failures.
- Fail closed for policy or action paths. Non-consequential analysis may degrade only with an explicit, observable reason.
