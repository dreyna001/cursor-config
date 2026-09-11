---
description: Architecture pattern for cybersecurity LLM workflows and bounded automation
alwaysApply: false
---

# Cybersecurity LLM Workflow Architecture

- Plan **by backend capability**, not by abstract "agent" labels. Use autonomy levels only as a secondary control and risk label.
- Prefer the bounded workflow shape: **normalize input -> grounded context/prompt -> structured output -> validate/policy-check -> optional bounded tool execution -> summarize/write back**.
- Use **RAG for environment grounding**, such as schema, indexes, fields, macros, query patterns, and runbooks, not for current-alert facts.
- Apply `security-evidence-discipline`, `llm-deterministic-guardrails`, and `cybersecurity-approval-policy-gates` to evidence, model output, and generated actions.
- If the workflow is single-call, keep intermediate context deterministic and in-memory; do not add persistence unless multi-step execution, replay, or audit needs it.
- Keep tool adapters and policy validation separate from prompt construction and orchestration.
- Prefer **incremental capability delivery**: grounded generation first, then validation, then read-only execution, then summarization, then approval-gated writeback/action.
- Default target for current cybersecurity workflows is a **bounded investigative system with human approval for consequential actions**, not open-ended autonomy.
