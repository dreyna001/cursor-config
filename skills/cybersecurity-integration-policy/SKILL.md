---
name: cybersecurity-integration-policy
description: "Legacy manual alias for combined cybersecurity integration and policy requests; routes explicitly invoked work to separate adapter and policy skills."
disable-model-invocation: true
---
# Cybersecurity Integration And Policy

This compatibility entrypoint is manual-only.

- Use [Cybersecurity Integration Adapters](../cybersecurity-integration-adapters/SKILL.md) for transport, normalization, authentication, retries, rate limits, typed failures, fixtures, and inbound webhook verification.
- Use [Cybersecurity Approval Policy Gates](../cybersecurity-approval-policy-gates/SKILL.md) for risk classes, allowlists, budgets, approval requirements, structured denials, and policy tests.
- Use [Cybersecurity Workflow Design](../cybersecurity-workflow-design/SKILL.md) when orchestration coordinates either boundary.

Keep adapter behavior and policy decisions separate. Do not maintain a combined checklist in this alias.
