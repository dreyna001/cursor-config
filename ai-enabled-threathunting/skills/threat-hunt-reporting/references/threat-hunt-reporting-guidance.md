# Threat-hunt report guidance

This is the browser/PDF presentation contract. Preserve canonical saved content,
analyst edits, evidence identity, schema, validation, approvals, editing, saving,
finalization and immutable historical PDFs. Presentation never authorizes searches,
model calls or changes to factual reasoning.

## Reading order and hierarchy

Lead with the saved assessment, full question answers and essential limits, with
hypothesis/scope context nearby. Do not invent an overall assessment when the saved
conclusion is already the question-answer projection. Put inventories, raw dumps,
diagnostics and repeated observations in available supporting detail. Legacy reports
without explicit observation provenance retain their narratives and reading order.

Use one title, no repeated generic running-header label, and restrained
section/subsection hierarchy with real headings and spacing for background,
objective, UTC window, focus and planned telemetry. Use Public Sans / Source Sans
Pro / system-ui; monospace for atomic IDs, queries and code. PDF sizes: title 20 pt,
section 14 pt, subsection 11 pt, body 9.2 pt. Keep headings with content, tables/links
inside page edges, and space between a table's final border and its note.

State the hypothesis once without a redundant “working assumption” label. Omit
only the exact terminal display clause “; treat the assumption itself as unverified”
(with optional final period); preserve internal/quoted occurrences, other qualifiers
and saved text. New reports use the reviewed hypothesis; saved edits remain canonical.

Introduce the reported concern, recorded trigger, relevant assets/behavior, window
and question for a first-time reader. Label missing background rather than inventing
an alert, impact or causal story. Keep intake reports separate from findings.
“Additional cited source observation” identifies a selected supporting record, not
necessarily the initiating event. Examples retain time/citation, selected-versus-raw
field distinctions, conflicts and multivalues. Network endpoints do not prove process
attribution; Zeek responders remain responders, not relabeled destinations.

## Approved scope and executed coverage

Retain the approved objective, terrain, behavior, questions and exact UTC start/end.
Distinguish planned sources/targets from those actually searched and from unavailable,
failed, partial, truncated, unqueried or out-of-retention coverage. Identify affected
scope/time when known. Zero matches differ from no search or missing data; isolated
observations do not prove continuous telemetry.

## Event chronology and analyst activity

**Event timeline** is a chronological table of environmental observations: UTC time,
behavior, host/terrain and source citation, with uncertain times/order explicit.
Point events do not establish continuity, causation or a common process.
**Hunt timeline** records investigation actions (searches, pivots, decisions, edits)
separately. These are local labels, not universal source-mandated vocabulary.
The browser table may collapse as a whole; PDF prints it fully with repeated table
headers on continuation pages.

## Findings, assessment, and caveats

Separate observation, interpretation and uncertainty. Hosts/IPs/hashes/dates are
neutral observed values unless evidence supports an IOC/malicious label. Answer what
supports, contradicts or leaves the hypothesis unresolved; coverage boilerplate
cannot replace the conclusion. Model confidence is not attack probability, severity
or a likelihood badge. Do not invent numeric scores.

Keep every distinct limitation, count, scope and uncertainty attached to its owning
answer/finding/source/time. New evidence does not automatically resolve earlier
limits; earlier candidate limits do not apply to all later evidence. Retain conflicts.
For identical whole-string question limits, show the first wording and numbered
**Same wording as** links at later questions; identical text does not mean identical
source scope. Coverage links to those notes. Retain explicit report-wide references;
changed wording/source suffixes stay separate. Browser links focus the exact note;
PDF uses static references/internal navigation.

Compact explicitly empty saved field lists only when roles and missing/multivalue/
non-scalar/omitted counts match. Keep each field/count and say **no listed values**;
unknown, null and zero differ. Preserve populated typed values and bindings.

## Citations and evidence identity

Use stable, readable numbered citations shared by browser and PDF. Separate sequences
need explicit type labels. Reuse numbers only for the same immutable record; similar
text with different IDs stays distinct. Labels never replace canonical IDs/UUIDs.
Browser links target the correct available source and show unavailable states instead
of dead/misleading links. Retain raw detail with its citation. Number ranges may open
the first source. Do not substitute current records for missing saved snapshots or
extend approved source scope.

## Browser and PDF details

The browser Report is a continuous document; six supporting sections use native
disclosures with chevrons and View/Hide details cues. Preserve section hashes/history,
all saved detail and approval/editing guards. At wide desktop sizes, a scope/coverage
rail can be replaced by the source inspector without shifting the document; with
constrained space/enlarged text, show inspection inline at its owning answer/section.
Preserve keyboard focus, Escape return and explicit saved/unavailable/separately
requested current-record states.

Completed hunts open Investigation Desk's Findings first, with Report in its own tab.
Keep setup, plan approval, search activity and evidence library in their named
workflow destinations. Retain bounded source reads, complete exports, visible load
failures and unsaved-edit status beside save/finalize even with the JSON editor shut.

Supporting source observations start collapsed with observation and unavailable-detail
counts; citations reveal their section/record. Preserve saved statement, interpretation,
action, event/collection time and bindings; PDF observations are static. Group only
explicitly identified, untouched application observations, never by title/prose/confidence.
Edited observations remain primary findings; save/finalize recomputes membership.
Missing detail stays counted with retained-finding access. One-record timestamp caveats
may share a warning only when identical and their timestamps remain in verified rows;
distinct wording, intervals and analyst caveats remain.

Preserve disposition, selected metadata, timeline search coverage, all distinct notes
and edits across both surfaces. Missing saved observations stay unavailable with links
to separately loaded results; current prose cannot fill them. Show exact inventory
entity/DNS values, types, roles and raw-event versus result origins without implying
affected assets, relationships or unique processes. PDF prints entity literals;
full exports retain action/time catalogs alongside timeline/observation tables.
Omitted values/references remain limits. Application coverage and the assistant's
requirement self-assessment remain distinct; valid structure is not semantic completeness.

Omit **Query Appendix** and **Reference Key** in browser/new PDFs while retaining
canonical queries, evidence, validation and editor. PDFs show citations without the
full ID-to-label index. Hide only exact allowlisted benchmark title suffixes in display;
never trim ordinary text/punctuation or stored titles. Classification/confidence badges
are omitted only from the readable overview.

## Preserve report content and editing behavior

Keep every supported answer, finding, observation, caveat, query and binding accessible.
Never replace a custom analyst conclusion with a generated summary. Remove duplicate
question/answer framing only for an exact known paired projection; familiar `Question:`
or `Answer:` prefixes alone do not justify slicing. Preserve standalone answers and
analyst-authored Q/A conclusions.

New PDFs retain the eight-section order, Event timeline before Search summary, with
static scope/coverage replacing the rail and all supporting sections printed. Keep one
complete saved-report PDF, clickable contents, question bookmarks and internal citations.
Move detailed requirement coverage/process comparisons into supporting detail with
bidirectional links. Keep short answers with limits when they fit; let long answers
continue without truncation. Apply layout changes only through normal new finalization;
never rewrite historical exports.

## Paired browser/PDF review gate

For changes to report content, headings, ordering, labels, coverage, citations,
projections or rendering:

- State **Browser impact** and **PDF impact** in the PR: changed, unchanged with
  reason, or deferred with a link to README current status. Unverified/deferred
  surfaces are not complete parity.
- Apply shared meaning/design to both, preserving intentional differences such as
  interactive panels versus static print. Do not restore omitted appendices.
- Check the same representative saved fixtures for answers, edits, distinct limits,
  scope, event times, labels, exact IDs, snapshot/current provenance and unavailable
  states. Retain parity tests and add focused regressions for changed behavior.
- For PDF changes, use the `pdf` skill, generate/render actual PDFs and inspect every
  page for headings, legibility, long values, continued tables, links and clipping.
  Extraction/tests alone do not prove visual correctness. Verify download/finalization
  with isolated data; use desktop Playwright for affected browser behavior.
- Record fixture/source versions, commands/results and rendered checks in the handoff;
  distinguish synthetic/live and unavailable checks. Complete required checks before merge.

Documentation compression alone does not change either renderer. This gate changes
neither suite standards nor schemas, prompts, approval rules or historical files.

## Basis and local conventions

[NIST SP 800-61 Rev. 3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf),
§3 RS.AN-03/06/07/08, informs event sequence/assets, recorded actions, provenance and
validated magnitude. [MITRE TTP-Based Hunting](https://www.mitre.org/sites/default/files/2021-11/prs-19-3892-ttp-based-hunting.pdf),
§§1.2, 2.3, 2.5, informs time/terrain/behavior scope, hunt timeline, affected systems,
risk/facts and avoiding speculation. Layout, ordering, display omissions and citation
style are local conventions, not certification or source-mandated templates. MITRE's
behavior-prioritization likelihood does not turn LLM confidence into report probability.
