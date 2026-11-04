---
name: cybersecurity-workflow-architecture
description: "Legacy manual alias for cybersecurity workflow architecture; routes explicitly invoked requests to the authoritative workflow and prompt skills."
disable-model-invocation: true
---
# Cybersecurity Workflow Architecture

This compatibility entrypoint is manual-only.

- Use [Cybersecurity Workflow Design](../cybersecurity-workflow-design/SKILL.md) for orchestration, validation, adapters, policy gates, approvals, and bounded execution.
- Use [Cybersecurity Prompt Engineering](../cybersecurity-prompt-engineering/SKILL.md) for prompt text, output schemas, evidence wording, RAG instructions, and repair prompts.
- Use [Cybersecurity Integration Adapters](../cybersecurity-integration-adapters/SKILL.md) for vendor boundaries and inbound webhooks.
- Use [Cybersecurity Approval Policy Gates](../cybersecurity-approval-policy-gates/SKILL.md) for allowlists, denials, approvals, and consequential actions.

Do not maintain a second workflow checklist in this alias.
