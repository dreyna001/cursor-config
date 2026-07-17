---
name: llm-step-design
description: Design one bounded LLM step with clear responsibilities, guardrails, and validation.
---

# LLM Step Design

Use this skill when:
- adding a single LLM step to a workflow
- refining prompts and guardrails
- deciding whether the LLM belongs in the design at all

## Objective

Design an LLM step that adds value without taking ownership of deterministic decisions.

## Process

1. State why an LLM is needed.
2. Identify the exact upstream deterministic facts available.
3. Decide what the LLM is allowed to produce.
4. Decide what the LLM must never decide or invent.
5. Define a structured output shape.
6. Define validation rules.
7. Define failure handling and fallback behavior.
8. Keep the prompt constrained to provided facts.
9. Keep the scope narrow enough to explain in one sentence.

## Output format

Return these sections:
- Purpose of the LLM step
- Upstream facts provided to the model
- Model is allowed to do
- Model is not allowed to do
- Output schema
- Validation rules
- Fallback behavior
- Prompt draft

## Constraints

- Do not let the model override deterministic status or scoring logic unless explicitly required.
- Do not use the LLM to compensate for missing domain rules.
- Do not produce free-form output when structured output is appropriate.
- Prefer a single bounded call over agentic multi-step behavior unless the prompt explicitly asks otherwise.
