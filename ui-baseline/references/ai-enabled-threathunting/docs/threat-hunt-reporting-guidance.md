# Threat-hunt report guidance

This guidance defines the local presentation conventions for an editable threat-hunt report and its finalized PDF. It makes the saved assessment and recorded event timeline easy to find while retaining the approved scope, supported findings, distinct caveats, source bindings, and analyst edits. It is a presentation contract; it does not change the report schema, evidence validation, hunt approval, editing, save, or finalization behavior.

## Reading order and hierarchy

Use one clear report title, followed by a restrained heading hierarchy: major sections at one level, with a second level only when it helps navigation. Apply a consistent title > section > subsection > body-text hierarchy across browser and PDF. Use the application's prose font stack (`Public Sans`, `Source Sans Pro`, `system-ui`, sans-serif) where available; use monospace for atomic identifiers, queries and raw code. Keep body text and table labels comfortably readable, use emphasis sparingly, and avoid styling that makes a merely observed artifact look malicious. In PDFs, keep headings with their content and prevent tables, citations, or links from clipping at page boundaries.

Lead with the saved assessment, analytical findings and important coverage limits. Keep hypothesis and approved-scope context available near that assessment. Repeated source observations, full inventories and the event timeline are supporting material, rather than additional conclusions. For now, omit Query Appendix and Reference Key from the readable report. Long raw statements, dumps, and diagnostics belong in supporting detail rather than the opening narrative; keep them available for review instead of dropping them. Legacy reports without explicit source-observation provenance retain their saved narratives and reading order.

The PDF uses a 20 pt report title, 14 pt section headings, 11 pt subsection headings and 9.2 pt body text. Give sections and subsections distinct spacing; keep headings with the text that follows them. Browser headings follow the same visual ordering within their existing semantic nesting.

State the hypothesis once and plainly. Do not add a redundant “working assumption” label when the hypothesis already expresses the assumption. In the report display, omit the exact terminal clause “; treat the assumption itself as unverified” with its optional final period. The hypothesis heading already conveys that status. Preserve other uncertainty qualifiers, quoted/internal occurrences and canonical saved text. The report should answer what the evidence establishes about that hypothesis. Explain the supporting, conflicting, or unresolved evidence and why. Coverage boilerplate may qualify the result, but it must not replace the analytical conclusion.

Assume the reader has never heard about the hunt or the underlying event. Introduce the reported concern, the recorded reason for investigating it, the relevant assets/behavior and time window, and the question being tested before referring to “the observed activity.” Name a particular event, connection, alert or record when the supplied context identifies it. Preserve reported background as reported information, separate from findings. If the intake narrative does not explain the trigger, say that the background was not recorded; do not invent an alert, business impact, attack story or causal relationship to make the opening sound complete. New reports use the reviewed plan's hypothesis, while saved report edits remain canonical. Selected supporting records in the introduction are labeled “Additional cited source observation.” Their selection does not identify the initiating event; keep that role separate from reported intake background and from the findings’ assessment of relationships.

Where helpful, introduce a bounded example from a cited, selected record. Preserve its timestamp and source reference, distinguish selected fields from raw source fields, retain conflicts and multivalue data, and do not infer process attribution from a network endpoint. Zeek responder fields retain their responder role rather than being relabeled as destinations. Keep raw field paths and dumps in supporting evidence.

Give background, objective, approved investigation window, investigation focus and planned telemetry real subsections with their own heading level and spacing. Labels embedded in body sentences are not a substitute for a readable hierarchy. Keep one main report title; omit the repeated generic running-header label. Leave visible space between the final table border and its qualifying note.

## Approved scope and executed coverage

Preserve the reviewed plan’s objective, target terrain, behavior of interest, questions, and exact UTC start/end window. Identify the plan as approved scope, rather than implying that every planned source or target was searched. Distinguish:

- **Planned sources and targets:** what the approved plan intended to inspect.
- **Searched sources and targets:** what the retained search and result records show was actually queried.
- **Coverage limits:** unavailable, failed, partial, truncated, unqueried, or out-of-retention data, with the affected source, terrain, or time span when known.

Do not convert a planned source into a searched source because it appears in the plan. Distinguish a successful search with zero matching events from a source that was not queried, failed, lacked coverage, or has no retained data. State time ranges in UTC and avoid implying continuous telemetry from isolated observations.

## Event chronology and analyst activity

Present the **event timeline** as a chronological table of recorded observations. Include the event time in UTC, a concise description of the observed behavior, the relevant host or other terrain, and a citation to its source. Keep uncertain timestamps or ordering explicit. A point observation establishes that event at that point; it does not by itself establish continuous activity, causation, or a common process across events.

Use **Event timeline** for that table and reserve **Hunt timeline** for investigation activity. These are clear local labels for the event sequence discussed by NIST and the hunt timeline discussed by MITRE; the sources do not impose a shared section title or a universal reporting vocabulary. Allow the whole browser event table to collapse. Keep the full static table in the PDF, including repeated headers on continued pages; do not promise interactive folding across PDF readers.

Keep an **analyst work timeline** separate if the report includes one. It records investigation actions such as searches, pivots, decisions, or report edits; it is not the chronology of events in the environment. Never interleave those action timestamps with event times without clearly labeling the two timelines.

## Findings, assessment, and caveats

Describe what was observed before stating what it means. Separate source facts from analyst interpretation. A host name, IP address, hash, date, or other entity may be emphasized as an observed value, but is not automatically an IOC or proof of malicious activity. Use an IOC or malicious label only when the retained evidence and context support that characterization.

Give a direct, evidence-backed assessment of the hypothesis, including what remains unknown. Do not translate model/provider confidence into attack likelihood, incident severity, or a numeric probability. Do not force a numeric score when the approved report contract does not contain one. If the source records a confidence value, keep its meaning distinct from the report’s factual conclusion; do not display it as a likelihood badge.

Consolidate repeated caveats for readability while preserving every distinct limitation, count, affected scope, and uncertainty. Exact repeated caveat text may be grouped only if its source bindings remain available. Keep a caveat attached to the answer, finding, source, or time range it qualifies; do not broaden an earlier candidate’s limitation into a statement about all later evidence, or mark a limitation resolved merely because newer evidence exists. Preserve contradictory or unresolved caveats and explain their scope rather than silently choosing one.

## Citations and evidence identity

Use concise, readable numbered citations in narrative and table cells. Keep one stable numbering map for the rendered report. If separate number sequences are needed, label their types explicitly so the same visible citation cannot point to different evidence, observation, or search targets. Repeated references to the same immutable record may reuse its number; records with different IDs remain distinct even when their text is similar.

Each browser citation must navigate to the intended available record and preserve the original evidence key or UUID as its target. Display labels are presentation aids, never replacements for canonical IDs or stored bindings. Do not renumber one class independently in a way that makes an existing label navigate to another class’s record. Keep unavailable-target states visible rather than rendering dead or misleading links. Raw evidence remains in the supporting detail associated with its citation.

## Browser and PDF details

Start the application report's Supporting source observations section collapsed, with
its observation count and unavailable-detail count visible. Observation citations
open that section and the relevant observation. Keep the complete saved statement,
interpretation and source bindings available; the PDF retains static observations.

The application report and PDF use the same saved report fields and data. Apply
the same citation ordering in both views; layouts and disclosure controls may
differ. Retain disposition, selected evidence metadata, timeline search coverage,
all distinct coverage notes and analyst edits. Do not import current result prose
to fill a missing saved observation; identify the unavailable saved detail and
keep links to separately loaded results. A shared presentation fixture checks
both renderers against the same values and citation identities.

Group only explicitly identified, untouched application source observations.
Never infer that status from a title, prose pattern or model confidence. Edited
titles, statements or interpretations remain primary findings; saving or
finalizing recomputes the application-owned group membership. Missing report
detail remains explicitly counted, with access to the retained findings.
Keep every grouped observation's action, event/collection time and citations.
Exact repeated one-record timestamp caveats may share one warning only when
the corresponding timestamp remains in that verified source-observation row;
distinct wording, intervals and analyst caveats remain intact.

List exact entity and DNS values from the application inventory, preserving
numeric/string representations, field roles and raw-event versus search-result
origins. These lists do not establish affected assets, relationships or unique
process counts. The static PDF prints entity literals; action/time catalogs
remain in the full results export alongside contextual timeline and supporting
observation tables. Explicit value/reference omissions remain coverage limits.
Show application coverage separately from the assistant's requirement
self-assessment; a structurally valid answer is not proof of semantic completeness.

For completed hunts, open Investigation Desk’s Findings tab first. Keep the full saved report in a separate Report tab. Keep earlier setup, plan
approval, search activity and the evidence library in their named workflow
navigation destinations. Open source citations in the persistent side-by-side
inspector; retain canonical IDs, bounded reads and complete evidence exports.
Keep load failures visible, existing action gates intact, and unsaved report edits
visible beside save/finalize controls even when the JSON editor is collapsed.

By current user decision, omit Query Appendix and Reference Key from the browser report and newly generated PDFs. Retain canonical query metadata, evidence identifiers, validation and the report editor. Browser citations navigate to available hunt-result records; unavailable targets remain explicit. The PDF keeps readable numbered citations but does not print the full ID-to-label index. This is a presentation change, not deletion of stored provenance.

Hide only an exact, recognized benchmark suffix from the displayed title when the local implementation has a known suffix allowlist. Do not trim ordinary title text, treat punctuation (including a middle dot) as a suffix by itself, or change the stored hunt/report title. Classification and model-confidence badges are omitted from the readable overview; their omission is display-only and does not authorize schema or data changes.

## Preserve report content and editing behavior

Treat saved report data as canonical. Keep every supported answer, finding, observation, caveat, query, citation binding, and analyst-edited conclusion available through the report and its supporting detail. Do not overwrite a distinct custom conclusion with a generated or reconstructed summary. When a saved summary is derived from structured answers, remove duplicated question/answer framing only when the exact paired wrapper is known to be the same projection; a familiar `Question:` or `Answer:` prefix is not enough to slice text safely. Preserve standalone answer text and analyst-authored Q/A-form conclusions.

Presentation changes must preserve the existing schema, validation, draft-edit surface, save behavior, finalization gate, and immutable finalized artifacts. Apply a new PDF layout to a newly finalized report according to the application’s existing lifecycle; do not silently rewrite previously finalized files.

## Paired browser/PDF review gate

Treat the browser Report and exportable PDF as two presentations of the same
saved report. At planning and PR review, any change to report content, headings,
ordering, labels, coverage, citations, supporting detail, shared projections or
export rendering must prompt an explicit assessment of the other surface.
The repository PR template carries this reminder; `AGENTS.md` routes report
work here. This is a review requirement, not an automated parity guarantee.

- State **Browser impact** and **PDF impact** in the PR: changed, unchanged with
  a reason, or deferred with a linked item in `docs/remaining-work.md`. An
  unverified or deferred surface is not complete parity.
- Update both surfaces when the same saved meaning or approved design applies.
  Record intentional medium differences: browser tabs/panels become static print
  sections, while typography and pagination follow the PDF contract. Preserve
  existing omission decisions; presentation parity does not require copying
  interactive controls or restoring omitted appendices.
- Check the same representative saved-report fixtures in both views for answers,
  analyst edits, distinct limits, scope, event times, coverage labels and exact
  source identities. Preserve complete canonical data, snapshot/current provenance,
  unavailable states and immutable finalized artifacts. Add focused regression
  coverage for changed behavior; retain the existing parity/presentation checks.
- Before merging PDF changes, use the `pdf` skill to generate and render actual
  PDFs and visually inspect every page. Check heading/content separation, readable
  text, long values, table continuations, citations/links and page-edge clipping.
  Text extraction and passing tests alone do not establish visual correctness.
  Verify the affected download/finalization journey with isolated local data;
  use Playwright for affected browser behavior per the desktop baseline.
- Record fixture/source versions, test commands/results and rendered PDF evidence
  in the implementation handoff. State synthetic-versus-live boundaries and
  unavailable checks explicitly. Resolve required checks before merge.

This gate is app-specific and does not change the shared suite baseline, report
schema, model prompts, approval rules or historical finalized files.

## Basis and local conventions

The following sources inform the evidence and hunt-analysis principles. The visual hierarchy, exact report ordering, title-suffix display rule, numbered-link presentation, and browser/PDF appendix behavior above are **local presentation conventions**, not requirements imposed by these sources.

- [NIST SP 800-61 Rev. 3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf), §3, outcomes RS.AN-03, RS.AN-06, RS.AN-07, and RS.AN-08: establish what happened and the sequence/assets involved; record investigation actions; preserve incident-data provenance; and estimate and validate incident magnitude.
- [MITRE, *TTP-Based Hunting*](https://www.mitre.org/sites/default/files/2021-11/prs-19-3892-ttp-based-hunting.pdf), §1.2, §2.3, and §2.5: frame analysis around time, terrain, and behavior; constrain hunt scope by those dimensions; and report the hunt timeline, confirmed presence, affected systems, risk, and facts while avoiding excessive speculation.

These cited sections do not prescribe this report template, a particular visual design, or a numeric likelihood score. MITRE §2.3 discusses likelihood as one possible filter for prioritizing behaviors; it does not require turning an LLM confidence value into a report probability. Use the sources to support the reasoning above, not to claim certification or broader requirements they do not state.

## Review checklist

- Is the saved assessment easy to find near the opening, and does it state a supported conclusion rather than only caveats?
- Can a first-time reader identify the reported concern, recorded trigger or explicit background gap, assets, time window and hypothesis without prior conversation?
- Are the approved hypothesis, objective, terrain, behavior, questions, and exact UTC window retained?
- Can a reader distinguish planned coverage from sources actually searched and from gaps?
- Does the event table contain only environment events, separate from analyst actions?
- Are observed entities neutral unless evidence supports an IOC/malicious characterization?
- Do numbered citations resolve to the correct immutable record and preserve its original ID?
- Are all distinct caveats and edited conclusions retained while repeated caveats are grouped?
- Are raw details available below the narrative, and are Query Appendix and Reference Key omitted while canonical records remain intact?
- Are schema, validation, editing, saving, finalization, and previously finalized artifacts unchanged?

### Desktop source-review destination

The October 15 central-workspace refinement supersedes the earlier persistent
side inspector. Keep saved questions/conclusions and supporting observations in
aligned report tables; retain complete saved detail behind chevrons. Citations
open the same canonical record in Source Records, with bounded retrieval and
an explicit complete export. Returning to Findings & report preserves unsaved
report edits. Missing saved coverage stays visibly unknown; planned source counts
are not completed search coverage.

### Investigation Desk navigation (October 16)

The approved Investigation Desk concept supersedes the older combined Findings &
report destination. Completed hunts open a question/finding table with selected
analysis beside it. Report remains the complete canonical reading/editing/export
surface. Source records remain a central workspace with bounded tables and
selected-record detail. Scope & plan opens the retained context and Plan & approval workspace;
execution, diagnostics and coverage stay in Activity. Do not delete saved
content to simplify the default screen.


The corrected full Investigation Desk shell has persistent **Hunt queue** and
**Current review** destinations and four review tabs: Findings, Evidence,
Activity and Report. Visiting the queue keeps the selected review and drafts;
opening a different hunt or leaving still uses the dirty-change guard. Use the
app-themed report reading view and adjacent editing rail as views of the same
saved content. The shared reference-number function is used by the Findings desk and
complete report; canonical citation IDs remain unchanged.


### Approved workflow simplification (later October 16)

Hunt titles in the queue open the review directly, without a selected-hunt preview.
Scope & plan now opens Plan review directly; original supplied context remains
separate from the revised/approved plan. Report starts in reading mode and offers
Edit report inside its own tab for drafts. Finalized reports hide editing controls.
Report citations retain contextual return to the report and preserve drafts.
Evidence owns the regular full-results export; exact source and recovery access
remain. The browser report and Event timeline use dark app surfaces with readable light
text and source links, as selected by the user after the white-preview iteration.
Reading width is bounded and coverage fields stay grouped. The static PDF
renderer retains its separate print styling. See [dark report qualification](report-dark-layout-20261016.md).

### Manual hunt workflow (October 21)

The current workspace order is **Plan → Searches → Evidence → Findings →
Report**. This supersedes the earlier visible Activity/Investigation labels;
existing route identifiers remain stable. Completed hunts still open Findings.
Keep the saved assessment and full-width question answers easy to read, with
direct citations. Put scope, search metrics and supporting technical detail in
clearly labeled disclosures. Consolidate general coverage notes into one
Coverage and limits disclosure while keeping question-specific uncertainty and
partial or blocked states visible. Preserve every distinct note and source
binding. Total data scanned and completed-search counts remain visible in the
Search summary heading. The PDF retains its static print layout.

### Report section tabs and source review (October 24)

The approved Report design uses eight peer sections: Assessment, Questions &
conclusions, Coverage & limits, Approved scope, Search summary, Timeline,
Observations, and Source values. A tab selects one section directly; it does not
require expanding that same section again. Preserve complete saved content,
question-specific limits and meaningful empty/unavailable states. Supporting
record fields may remain in the existing advanced/saved-data views.

The approved document hierarchy uses 18px section/source-panel titles and 16px
question titles, while retaining semantic h3/h4 nesting below Hunt report. This
Report-only typography adaptation uses `vs-report-section-title` and
`vs-report-question-title`; it does not redefine global heading sizes. Use the
baseline's stacked layout for constrained desktop zoom while Report is visible.

A normal report citation opens a non-modal source panel inside Report. The panel
belongs to its originating section and closes on section or workspace exit;
returning does not reopen it. Show available record fields in one flat detail
view, with natural scrolling for long content, explicit snapshot/current-source
identity, and a separate Open in Evidence action. Missing saved snapshots must
not silently acquire current values. Keep bounded retrieval, revision checks,
errors/retry and complete exports. Preserve canonical citation IDs and all
report edits when navigating. Modified-link/open-in-new-tab behavior retains the
existing canonical source destination.

The Evidence workspace can display saved evidence snapshots. Its query and
finding views display current retained records, so their report-panel action is
explicitly labeled **Open current record in Evidence** and carries current-source
provenance. Opening a current record inside the report panel also preserves that
choice when moving to Evidence. Keep the saved report version and return path
attached to either navigation mode.

This is an app-specific reading/navigation decision, not a new default for other
suite apps. Browser section navigation does not change the saved report schema,
model output contract or immutable PDF lifecycle. Static exports continue to
include the complete saved report, independent of the currently selected tab.
