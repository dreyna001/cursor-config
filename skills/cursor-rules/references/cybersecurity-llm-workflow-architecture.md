---
description: Architecture pattern for cybersecurity LLM workflows and bounded automation
alwaysApply: false
---

# Cybersecurity LLM Workflow Architecture

- Plan **by backend capability**, not by abstract "agent" labels. Use autonomy levels only as a secondary control and risk label.
- Prefer the bounded workflow shape: **normalize input -> grounded context/prompt -> structured output -> validate/policy-check -> optional bounded tool execution -> summarize/write back**.
- Separate **direct evidence**, **advisory context** (RAG, SOPs, KB), and **inference**. Advisory context must not be claimed as case evidence.
- Use **RAG for environment grounding**, such as schema, indexes, fields, macros, query patterns, and runbooks, not for current-alert facts.
- Prefer explicit **output contracts** with required keys, enums, `unknown` behavior, and machine-safe parsing.
- Always design **validators and policy gates** for generated queries or actions: allowlists, time bounds, cost caps, read-only enforcement, and approval checks where needed.
- If the workflow is single-call, keep intermediate context deterministic and in-memory; do not add persistence unless multi-step execution, replay, or audit needs it.
- Keep **tool adapters** and **policy/validation** as separate concerns from prompt construction and orchestration.
- Prefer **incremental capability delivery**: grounded generation first, then validation, then read-only execution, then summarization, then approval-gated writeback/action.
- Default target for current cybersecurity workflows is a **bounded investigative system with human approval for consequential actions**, not open-ended autonomy.
