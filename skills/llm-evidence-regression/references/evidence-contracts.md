# Evidence contracts that preserve useful output

Read the sections relevant to the changed boundary. These are implementation and
review principles, not text to paste wholesale into every model prompt. The
application's actual contract and the user's task determine the schema and scope.

## Structure, normalization and repair

- Keep initial prompts, repair prompts, examples, parser, native provider schema
  and downstream validator aligned, including nested required fields and types.
  A prompt's strict-format request does not prove provider schema enforcement.
- Normalize only declared structural aliases or other demonstrated lossless
  transformations. When canonical and alias fields coexist, preserve both sets
  of supplied values. Preserve malformed or unknown nonempty values for diagnosis
  and repair; do not infer an indicator category from its spelling or silently
  erase wrapper metadata. An unknown empty collection can be omitted only if the
  contract distinguishes neither its presence nor its meaning.
- Distinguish a valid observation from a valid category assignment. An observed
  value in an unsupported category may belong in a supported evidence field, but
  relocation needs its original field/source binding. Prefer bounded repair or
  explicit failure when that mapping is unresolved. Never erase an observation
  merely because it is not an IOC.
- A source reference is request-derived and may be incomplete. Preserve array
  record grouping, delimiters and escaping; signal omissions. A value omitted
  from a shortened reference is not absent from the full supplied evidence.
- Honor the configured output budget and provider truncation/refusal signals.
  Keep the invalid prior output, validation error and original evidence/contract
  in an existing bounded repair path. Do not add unlimited retries or fabricate
  repairs. Expose failure when the bound is exhausted.

## Exact evidence versus interpretation

- If the contract requires exact evidence, compare a copied string to the
  corresponding source scalar after removing only syntactic quote/escape wrappers.
  Preserve its case and significant whitespace. Keep typed JSON scalars distinct
  from literal strings. A field/value pair must match that field in a real source
  record; a compound pair must not join values from different events.
- Contiguous short quotes may be supported by a source value where the contract
  permits excerpts. A field/value assertion requires its full field value, not a
  matching substring elsewhere. Do not assemble an observed URL/path/identity
  from separate fields unless the contract defines a deterministic derivation and
  labels it accordingly.
- Apply exactness to the contract's evidence and identifier fields, not to all
  interpretation. An explicit hypothesis or prospective investigation can mention
  an unobserved target without claiming it was observed. Keep its qualification
  scoped to that claim so it cannot excuse a separate unsupported assertion.
- Clearly prospective investigation/tool examples are not observed case facts.
  Apply the task's actual advice policy: a source-only workflow needs advisory
  support, while a workflow permitting general advice need not find every example
  in case records. Do not infer a source-only ban when that policy is unspecified;
  state the uncertainty and qualify availability/access/approval where needed.
  A suggested product does not establish its presence, a deployed integration,
  available telemetry or an asset role.

## Claim identity, source and polarity

- An identifier's words do not prove a role, protocol, purpose or behavior. A
  product/tool mention also does not assign an asset role. Conversely, explicit
  role statements and structured role fields must remain usable when supported.
- Bind a property to its entity, source lane, event and time. Current observations,
  historical records, advisory guidance and generated interpretations are distinct.
  A supported predicate on one host cannot validate the same predicate on another.
- Keep explicit occurrence, explicit non-occurrence, missing records and lack of
  established proof distinct using the supplied state contract. An incomplete
  record cannot establish an unlimited "never" claim. Advisory absence-of-proof
  language concerns that document; it is not evidence of a current completed action.
- Parse subjects and modifiers as grammatical relationships rather than adding
  every observed adverb or preposition to a special-case list. Test evidence-defined
  short identifiers that resemble ordinary words. Document the finite grammar's
  unresolved forms instead of claiming full language understanding.

## Partial output and capability status

- Separately supported facts and cited advisory references can survive removal of
  a bad claim only when the resulting unit is self-contained and still source-bound.
  Do not strand pronouns, targets, chronology, causal links or source references.
  A safe fallback that discards an expected independent fact is a retention failure.
- Require affirmative support for projected factual content; absence of a guard
  complaint does not establish correctness. Revalidate the projection. A complete
  authoritative source clause can be safer than an unverified rewritten fragment.
- Preserve supported SOP identifiers and advice as advisory, without implying the
  advised action occurred. Keep an explicit application capability refusal separate
  from factual uncertainty. A refusal's self/portal attribution must survive; a
  quotation, retrieved statement, hypothesis or third-party refusal does not prove
  the assistant refused. Canonical capability text must reflect the actual
  application's capabilities, not an invented universal read-only policy.
