# LLM Analysis and Output Guardrails

- Separate **direct evidence** (case/alert/artifact data), **advisory context** (KB, RAG, runbooks, doctrine), and **inference**. Do not let retrieved or instructional text become claimed observations unless the case data supports it.
- Prefer explicit **output contracts** (required keys, allowed values, `unknown` for missing facts). Downstream automation must not rely on prose outside the contract.
- **Parse → validate → repair (optional) → fail or degrade explicitly.** Do not silently accept malformed JSON or policy violations for automated paths.
- Prefer **low temperature** and schema-oriented instructions where repeatability matters; document when free-form output is intentional.
- **Allowlists and validators** (e.g. technique IDs, enums) belong in code or versioned data, not only in prompt prose.
- Preserve **raw model output** or clear metadata when humans must review failures; avoid dropping diagnostic text without a structured reason field.
- When the selected provider supports strict structured outputs, send the supported response schema through the API rather than relying on prompt text or JSON mode alone. Derive it from the application contract, constrain context-specific choices where useful, and retain semantic validation plus explicit refusal/truncation handling. A valid schema or citation does not establish factual correctness.
- Project cross-field invariants into supported native schema variants where feasible, such as requiring nonempty evidence for positive claims. Test generated schemas against valid and invalid combinations, and run bounded provider contract checks before claiming provider compatibility; keep application validation authoritative.
- Let application code own durable identifiers and derivable relationships. Models may select bounded context-local labels resolved through an immutable request mapping; reject unknown or out-of-context labels. Preserve query references for zero-result searches and scoped negative findings.
- Pass relevant prior structured assessments with their supporting records when a downstream step depends on earlier investigation work. Label assessments as interpretations, preserve provenance and limitations, and fit the whole handoff within existing evidence and context budgets.
- Measure first-pass schema and grounding validity separately from eventual repair success and analytical quality. Use observed workflow outputs for evaluations; scripted fixtures test deterministic behavior and cannot establish live-model quality. Record provider/model settings, precision/recall where labels support them, unsupported claims, repair rate, and cost within an explicitly bounded evaluation.
- Compute counts and observed time bounds in application code when they are derivable from retained evidence. Distinguish the approved search interval, point-event timestamps, sample completeness, and demonstrated telemetry continuity; endpoint timestamps alone never establish continuous coverage. Reproduce observed factual overclaims with bounded live evaluations and keep general analytical quality unproven until representative judgments support it.

## Corrections must preserve supported results

- For evidence, schema or grounding corrections, test unsupported rejection and
  supported retention together. Include the analytical outcome classes relevant
  to the task and compare actual final decisions. Rejection/unavailability is a
  separate outcome, not a benign result or a confirmed correct negative.
- Keep exact source strings and same-record field/value bindings where the
  contract requires exact evidence; preserve JSON scalar types and escaping.
  Do not impose literal-copy constraints on qualified analytical hypotheses or
  prospective investigations. Permitted prospective tool/investigation advice
  follows the actual advice policy; it need not be an observed case fact, and must
  not imply tool availability, telemetry access or a completed action.
- Normalize declared aliases losslessly. Unknown nonempty metadata, unresolved
  wrappers and ambiguous categories remain visible for bounded repair/failure.
  An empty extra collection may be omitted only when that loses no contract
  meaning. Do not erase a valid observation merely because it is not an IOC.
- Missing records do not establish non-occurrence; identifier words and tool
  mentions do not establish entity properties. Bind claims to their actual
  entity/source/event/time and distinguish advisory/current/historical roles.
- Partial-answer retention needs affirmative support and intact bindings, followed
  by revalidation. Keep supported independent facts and actual capability refusals;
  do not strand dependencies or preserve arbitrary unchecked prose.
- Correct a reusable supplied-contract or grammatical relationship rather than
  adding exceptions for fixture values or phrasing. Preserve evidence-defined
  identifiers that resemble function words; document unresolved language limits.
- Keep nested prompts/provider schemas/parsers/validators aligned and use the
  existing bounded repair path with raw prior output retained. Technical validity,
  grounding and analytical quality are separate checks.
- Preserve old cases and baselines. Report first-pass response, actual accepted
  output, full validation, decision/fact retention and provider failures separately.
  Scripted recovery or captured replay is not a new live pass. Check sensitivity
  and false alarms together when labels support them; finite controls do not
  establish production rates. This guidance grants no additional execution scope.
