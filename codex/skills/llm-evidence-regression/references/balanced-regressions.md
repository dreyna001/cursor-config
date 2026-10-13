# Balanced regression checks

Select the rows relevant to the correction; this table is not a mandatory test
count or a requirement to build every case for a small change. Use new entities
and event structures as well as captured examples. Do not encode these example
values into production behavior.

| Changed boundary | Supported information that must survive | Unsupported or invalid control |
| --- | --- | --- |
| Alias/coercion | Canonical plus declared alias values, including a meaningful non-IOC observation | Unknown nonempty category, unresolved wrapper metadata or an ambiguous flat list remains visible and fails/repairs |
| Exact source copying | Quoted/escaped strings, paths with spaces, typed booleans/numbers/null, literal strings resembling those types | Case-only/value changes, annotation added to a copied fact, paraphrase in an exact field, values joined across records |
| Evidence roles | A supported observation and an explicitly qualified hypothesis or future pivot | The same unobserved hypothesis target asserted as a present observation; qualification in another clause |
| Advice policy | A clearly prospective tool/investigation example when the task permits general advice | A suggestion asserted as an installed tool, completed action or available telemetry; violation of an explicit source-only advice contract |
| Role/property binding | Explicit structured/text role on its actual entity, tool mention without a role assertion | Role inferred from a name or tool word; correct property assigned to a different host/event |
| Action polarity | Missing-record wording, explicit performed/not-performed facts, qualified advisory provenance | Missing record promoted to non-occurrence, advisory promoted to completed action, borrowed historical state |
| Partial answer | Independent host/activity facts and a supported advisory reference | Stranded pronoun, rebound target/time/source, unsupported causal fragment or unchecked prose surviving deletion |
| Capability refusal | Actual self-attributed refusal in supported direct or adjacent-clause forms | Quoted/retrieved/third-party, hypothetical, negated or uncertain refusal masquerading as actual response status |
| Truncation/repair | Retained raw failure and original evidence in the configured bounded repair path | Truncated JSON accepted as valid, fabricated repair, unsupported values deleted to make a green result |

## Measure decisions and evidence separately

For fixture labels that support it, record an expected-versus-final decision
matrix. Keep invalid/unavailable outputs in their own column. Include supported
malicious cases to detect lost threat detection, benign cases to detect false
alarms, and unknown cases to detect unjustified certainty. Count each case using
the actual completed application output, not only a raw model label or a grading
flag. Preserve all required supported facts and source bindings independently of
the disposition score.

A guard improvement that blocks more unsupported claims can still regress if it
turns supported threats or benign outputs into unavailable results, changes a
benign/unknown decision to malicious, or removes independently supported evidence.
Investigate those changes rather than treating increased rejection as success.
Do not freeze an incorrect verdict simply because it used to pass; justified
changes need evidence-backed expected behavior and an explicit baseline comparison.

## Keep evaluation layers distinct

1. Raw proposed model response and first-pass validity.
2. Parsing/normalization and application acceptance.
3. Full schema and source/grounding validation.
4. Final disposition and supported-fact retention.
5. Analytical rubric/human review and provider execution failures.

Report partial passes at their actual layer. The same response can have a correct
proposed verdict but no usable validated final decision. Separate technical
provider failures from analytical failures and semantic relevance from format.

Preserve capture order and actual repair responses. A scripted repair proves
deterministic recovery for that script. Replaying real captured outputs proves
handling of those captures, including missing repairs. Neither changes an earlier
live score or demonstrates that a revised prompt will produce good future output.

Compare equivalent inputs, labels and application boundaries before interpreting
before/after changes. Record revision, source/input hashes and whether source
changed during replay. Keep historical reports intact. For authorized live work,
state the model/provider, settings, case/call/time/cost limits and deployment scope;
do not infer permission for repeated runs from a skill or a prior single pass.

Finite controls bound demonstrated behavior. Production precision/recall or
false-positive rates require representative labels, explicit denominators and
appropriate review; a small all-green corpus is not that evidence.
