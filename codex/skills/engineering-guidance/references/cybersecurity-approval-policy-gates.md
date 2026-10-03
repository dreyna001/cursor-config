---
description: Approval boundaries and policy gates for cybersecurity analysis, writeback, and actions
alwaysApply: false
---

# Cybersecurity Approval And Policy Gates

- Separate **read-only retrieval**, **writeback**, and **action-taking** behavior as different risk classes.
- Put **policy validation** before any generated query, update, or action reaches an external system.
- Prefer **fail-closed** behavior for risky operations; do not silently continue on policy uncertainty.
- Require explicit approval boundaries for consequential writes, state changes, escalations, suppressions, or response actions.
- Keep **allowlists, deny rules, budgets, time bounds, scope caps, and approval requirements** in code or versioned policy, not only in prompt text.
- Make it clear which operations are safe to automate, which require approval, and which are prohibited.
- Log enough metadata for auditability without exposing secrets or sensitive payloads unnecessarily.
- Treat policy checks as a distinct layer from adapters and orchestration.
- If policy blocks execution, return a structured reason instead of degrading into ambiguous behavior.
- Design the same policy-gate pattern across domains such as incident triage, threat hunting, vulnerability workflows, threat intelligence, ATO, and ConMon.
