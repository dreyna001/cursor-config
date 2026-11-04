# Case analysis contract

Applies to on-prem, AWS GovCloud, AWS commercial, and Azure.

## New initial analysis

| Field | Required content |
| --- | --- |
| `alert_reconciliation.verdict` | `likely_benign`, `likely_malicious`, or `unknown` |
| `alert_reconciliation.one_sentence_summary` | Concise assessment |
| `alert_reconciliation.key_findings` | Distinct `{text, kind, evidence_fields}` records |
| `alert_reconciliation.evidence_gaps` | Missing evidence, scoped to supplied inputs |
| `alert_reconciliation.recommended_actions` | Proposed checks as `{action, reason}` |
| `competing_hypotheses` | Exactly three likelihood-ranked explanations; overlap and shared evidence allowed |
| `ttp_analysis` | Supported ATT&CK mappings with existing evidence fields and mapping scores |
| `ioc_extraction` | Existing typed indicator lists; current-alert literals only |

Finding kinds: `observation`, `reported_context`, `inference`, and
`historical_context`. Current-alert findings cite exact supplied field names.
Historical findings have an empty `evidence_fields` list and remain advisory;
they do not establish current indicators or activity. Field-reference validation
checks provenance, not general narrative truth. Findings written as `field=value`
use exact source literals without annotations; explanatory findings use ordinary
prose with the same source citations.

Hypotheses contain `hypothesis_type`, `hypothesis`, `evidence_support`, and
`evidence_gaps`. Order explanations by fit to the supplied evidence and context;
there is no distinctness or benign/adversary type quota. This is a reasoning
instruction and structural count contract, not a guarantee that a model finds
the true three most likely causes. Existing archives with zero through three
explanations remain readable. Use empty support/gap lists when no material
content is supported. Checks
are recommendations; the portal does not execute them.

The model does not produce an overall confidence, duplicate decision drivers,
separate evidence/inference summaries, pivots, or application IDs. Initial
analysis does not generate SPL/Query DSL, execute SIEM searches, or interpret
new SIEM search results. Assistant knowledge retrieval and approved ServiceNow creation
remain separate capabilities.

## Reasoning and recovery

Likely meanings, roles, protocols, mechanisms, benign explanations and candidate ATT&CK mappings can contribute to analysis when the evidence or context supports them. The analysis must explain the basis and material uncertainty, preserve raw facts and distinguish interpretation from observations, maliciousness, authorization and performed actions. A labeled hypothesis supplies qualification; every sentence need not repeat a particular hedge word. Relevant attributed historical precedent can affect relative plausibility without becoming a current event or approval.

Exact source values, source field references, IOC membership, valid technique IDs and action/approval boundaries remain enforced. Typed inferences no longer depend on a narrow list of qualifying phrases. Actual claims that the current logs record a value still require source support. These checks do not establish general semantic correctness or complete entity/event relationship correctness.

When optional analyzer review is unavailable or unresolved, an independently mechanically/source-valid candidate can survive with explicit `metadata.semantic_review` warnings. Bounded detail projection preserves that warning. A failed revision does not become approved. Analyzer review remains opt-in and defaults off; no additional model pass is introduced. Chat distinguishes approved, corrected, partial and unavailable verification; incomplete-review recovery retains source-bound information and a visible warning. Existing read-only retrieval, execution gates, source/context limits and spending controls remain in place.

Known JSON-encoded output containers can be decoded only to their declared exact container types, then pass the unchanged full native validation. Duplicate inner keys, malformed JSON and wrong types are rejected rather than silently coerced. After the existing single repair is exhausted, a non-TTP core can survive only if it independently passes the native schema/content/provenance checks; each surviving TTP and the final projection are checked again. Invalid mappings remain in the original raw attempts and the exclusion audit. No citation is fabricated and no additional model pass is added.

Structural exclusions set `metadata.structural_recovery.review_required`, independently of actual semantic-review receipts. The four bounded detail projections preserve that warning and an accepted review status even when large diagnostics are omitted. A successfully completed review is never relabeled incomplete merely because a mapping was excluded. The portals and Markdown reports display a distinct technique-mapping warning and keep valid sibling mappings visible, without exposing raw validator diagnostics.

Recovery does not regenerate summaries or prove general semantic independence. The retained core passes the existing full checks, including paired rejection of a summary repeating a fabricated process fact; those finite checks cannot detect every dependent prose claim. Original output and a visible partial-result warning remain necessary.

## Existing records and links

Azure reuses completed analysis only when the stored prompt, source and model
fingerprints match the current runtime. Removing obsolete analyzer code changes
the source fingerprint: existing archives remain readable, while a later replay
with the old fingerprint requires fresh analysis. The upgrade does not rewrite
stored reports or bypass fingerprint validation.

Original alerts and archived analysis remain intact. The UI projects both
formats without migrating stored cases. Legacy drivers appear as neutral notes;
saved hypotheses, drafts, search results, and interpretation links remain readable.
Old tab aliases and query references continue to resolve. Unmatched records stay
accessible in Technical details; missing evidence is never shown as a zero-result
search. Bounded display views disclose truncation and offer complete source access.

Loading remaining archived fields replaces the original-record JSON panels with
the saved values, without the initial display shortening. It does not rerun
analysis or retrieve new source evidence.

Historical search outcomes remain separate from the current assessment. The
Assessment tab exposes saved search limitations and links to the retained query
records. A section with only status or summary metadata remains visible even
when individual records are unavailable. Disabled, denied, failed, timed-out,
partial and unknown outcomes do not establish a completed search with zero
matches. Only a saved successful/executed result with an explicit valid count
establishes that count; absent or invalid counts remain unavailable.

Original query text, references and any additional saved metadata remain
inspectable. The retired normalizer did not record a search source or execution
timestamp. Neither the case processing time nor the report generation time
supplies that missing provenance. Original-record disclosures reflect the
returned archive view; use the existing complete-source controls in Technical
details when the archive view is shortened.

Evidence-gap checks are prospective suggestions tied to the saved limitation in
the same row. Saved search leads show their recorded purpose when available;
an absent purpose remains explicit. Neither following a source reference nor
opening a saved search record executes a check. The verdict is a saved AI
assessment, any legacy model estimate is uncalibrated, and ATT&CK confidence is
confidence in a technique mapping. The current initial-analysis contract has no
dedicated human analyst disposition, technical-severity or sourced business-impact
field; do not infer those dimensions from the verdict, model estimate or names.

The closed-ticket view shows mapped core fields separately from Additional
ServiceNow fields. The latter contains source fields outside the configured core
mapping and journal entries not already represented in core Notes. Filtering
this view does not change the stored original ticket or retrieval content.

Saved search leads render as separate entries with their recorded description,
source and field names. The known saved `description: log_source=...;
key_fields=[...]` form remains readable. Unknown or malformed entries stay visible
intact; arbitrary evidence values are not split on punctuation, and repeated
leads remain separate.

Legacy decision, evidence and inference notes appear with Key findings while
retaining their distinct roles. Only exact repeats within one role collapse;
malformed structured siblings cannot suppress independent saved notes. A saved
model confidence, including zero, stays visible with its uncalibrated-probability
qualification and remains separate from technique-mapping confidence. Complete
original records stay available through the existing inspection controls.

The findings list has a separately named, keyboard-accessible scroll region
capped at `min(24rem, 45dvh)`. Its heading, count, explanation and show-all/fewer
control remain outside that region. Source links, collapse/re-expansion and
natural page scrolling remain available without changing saved content.

## Implementation locations

- On-prem: `llm_notable_analysis_onprem_systemd/src/llm_notable_analysis_onprem_systemd/onprem_service/`.
- GovCloud: `s3_notable_pipeline/src/s3_notable_pipeline/`.
- Commercial: `s3_notable_pipeline_commercial/src/s3_notable_pipeline/`.
- Azure: `azure_notable_pipeline/src/azure_notable_pipeline/`.

Each backend has `analysis_provenance.py` and `analysis_summary.py`. GovCloud
provider types are in `analysis_models.py`; other native provider schemas and
readers are in `ttp_analyzer.py` or on-prem `local_llm_client*.py`.
Each portal uses `src/utils/caseAnalysisProjection.ts` and
`src/components/case-detail/CaseAnalysisView.tsx`.

For upgrades, remove retired investigation profiles and flags as described in
each product's `docs/operations/investigation/SPL_OPERATIONS.md`. No case-data
migration is required.
