# Application And LLM Practices

Apply only the sections for technologies the project actually uses. Inspect installed versions and current project patterns first; verify version-specific APIs from authoritative documentation rather than model memory.

## FastAPI And Pydantic

- Keep route handlers thin: validate input, authorize, call application logic, and map the result to an explicit response contract.
- Use Pydantic models at trust boundaries and SQLAlchemy models for persistence. Do not make one model serve every layer when their contracts differ.
- Decide `extra`, strictness, aliases, and serialization deliberately for each external contract. Keep validators deterministic and free of I/O.
- Use dependency injection for request-scoped dependencies and lifespan hooks for shared resources. Do not create clients or pools per request. Keep shared services scoped to the application instance; lifecycle changes warrant checks that two applications remain isolated and resources close on shutdown.
- Avoid blocking calls in async paths. Inspect the entire called path for synchronous database, parsing, and filesystem work; offload it through the established bounded execution mechanism. Bound request bodies, outbound calls, concurrency, and timeouts.
- Return stable error contracts without leaking secrets or internal exception details.

## Structured Model Boundaries

Apply to direct model calls as well as agent frameworks. Follow the shared [LLM deterministic guardrails](../../engineering-guidance/references/llm-deterministic-guardrails.md) for API-enforced schemas, deterministic identity mapping, bounded context handoffs, and evaluation evidence. Preserve each supported provider's actual capabilities; do not silently downgrade a requested strict contract.

## PydanticAI And Pydantic Graph

- Use a direct model call for one simple step; add PydanticAI when tools, dependencies, or structured output materially help.
- Define explicit input, dependency, tool, and output contracts. Validate model output before persistence, execution, or security-sensitive use.
- Keep tools narrow, authorized, observable, and bounded by timeout and result size. Require approval for consequential actions.
- Use pydantic-graph only for current branching, loops, resumability, or explicit state. Keep linear workflows as functions or a single agent.
- Make resumable nodes idempotent and persist only the state needed to continue safely.
- Test deterministic contracts with pytest and probabilistic behavior with bounded Pydantic Evals datasets and acceptance thresholds.

## FastMCP

- Expose the smallest useful tool or resource contract with clear schemas and descriptions.
- Authenticate and authorize at the server boundary; do not assume tool discovery grants execution rights.
- Validate all tool arguments, bound outputs, redact secrets, and record security-relevant calls.
- Keep business policy in the application or policy layer rather than duplicating it in MCP transport adapters.

## Document Intake

- Enforce file type, size, page, decompression, and processing-time limits before parsing untrusted documents.
- Use the narrow per-format extractor needed by the current input. Add OCR or layout tooling only when actual documents require it.
- Preserve source location and provenance for extracted segments; never treat model interpretation as direct document evidence.
