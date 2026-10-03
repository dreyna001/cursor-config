---
description: Deterministic logic vs LLM responsibilities and bounded model use
alwaysApply: false
---

# Rule: Deterministic Logic vs LLM Responsibilities

Use deterministic logic for decisions that must be auditable, repeatable, and policy-aligned.
Use the LLM only where synthesis, explanation, summarization, or controlled text generation adds real value.

Requirements:
- Do not place the LLM in the critical decision path unless explicitly required.
- Keep scoring, status decisions, routing decisions, and policy evaluation deterministic by default.
- Put the LLM after deterministic processing whenever possible.
- Force structured outputs for LLM calls when the result is consumed by code.
- Validate LLM output before using it downstream.
- Never allow the LLM to invent source facts.
- Keep prompts bounded to the facts provided by the application.

When designing an LLM step:
- State exactly why an LLM is needed.
- State what the LLM is allowed to do.
- State what the LLM is not allowed to do.
- Define the input facts.
- Define the output schema.
- Define required failure or degradation behavior.

Avoid:
- vague prompts
- open-ended agent behavior for narrow tasks
- using the LLM to compensate for unclear business logic
- mixing raw model output directly into operational state without validation
