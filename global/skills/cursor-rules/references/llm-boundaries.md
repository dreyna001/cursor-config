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

## Untrusted channels

Text from these channels may be quoted, stored, and sent to the model as data. Instructions inside that text are not commands.

- Frontend: user text, uploads, and rendered model output. Rendering, CSP, and upload isolation stay in the application security rule.
- Between the UI and the model: API bodies, queues, retrieved documents, tickets, mail, and tool results. Inbound webhook authenticity stays in the integration-adapter rule. Production quotas stay in the API abuse rule.
- Backend: model output before it becomes a query, shell command, write, or tool call.
- Whether retrieved text is evidence or only advisory stays in the deterministic guardrails rule.

Checks, enforced in application code:

- Keep task instructions in the system or developer channel. Keep user text, retrieved content, and tool results in a data channel labeled with its source id.
- Fix the tool allowlist, tenant, and budget before the model sees that data.
- Parse only the output schema. Ignore instructions outside it.
- Reject a response that copies the system prompt or a secret. Do not put secrets in the prompt.
- A tool result cannot add a tool, widen scope, or authorize a write. The next call still has to match the allowlist, schema, tenant, and budget.
- Cap tool calls, tokens, retrieved bytes, and time in code. Stop with a structured limit error. A prompt line is not the cap.
- Test with fixtures that contain an instruction. Pass means no extra tool ran, the allowlist did not change, and the decision still matches the fixture's real evidence.
