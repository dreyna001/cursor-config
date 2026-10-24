# Optional UI pattern catalog

This catalog collects selected interaction approaches from approved previews and
suite products. It is a **choice aid**, not an extension of the shared UI
standard. Pick a pattern only when it fits the destination app, preserve that
app's current behavior and contracts, and adapt its existing components and
tokens. Do not copy a preview's styling, mock data, or interactions as production
requirements.

The evidence labels distinguish a synthetic preview check from review of
application source. A preview can establish that its own interaction works; it
does not establish production integration, live data behavior, or export parity.

## Quick selection

| Pattern | Consider it when | Evidence status |
| --- | --- | --- |
| Peer tabs inside a workspace | People move among several named, equally important sections in one task. | Approved and browser-checked in the synthetic Report preview. |
| Nonmodal source inspector | A citation should be inspected without losing the current report context. | Approved and browser-checked in the synthetic Report preview. |
| Flat source details | People need to scan source metadata without guessing which fields are hidden under a generic disclosure. | Approved and browser-checked in the synthetic Report preview. |
| Answer-first report reading | Readers need a conclusion, its limits, and its supporting sources together. | Source reviewed; preview content is synthetic. |
| Draft guard with separate export | Editing, review/finalization, and document output have different consequences. | Preview interactions checked with local mock actions; app export contract was not tested by that preview. |

## Patterns

### Peer tabs within a workspace

**Use when:** A bounded set of peer sections belongs to one workspace and users
need to move directly among them. This can reduce repeated scrolling through a
long report or opening many independent disclosures.

**Avoid when:** Sections form a required sequence, when users must compare many
panels at once, or when nested tabs would hide a larger information-architecture
problem. Keep each tab label short and distinct; do not add a tab just to move a
rare detail that is better in its existing destination.

**Interaction and accessibility:** Keep the nested navigation visibly scoped to
its parent workspace. Expose a named `tablist`, selected state, and one active
panel; provide arrow-key navigation and a visible focus indicator. If direct
section links are useful, synchronize the URL and browser history, restore the
selected section on Back/Forward, and ensure the active panel is reachable after
navigation. Do not discard edits, reset filters, or change workflow permissions
when a section changes.

**Preserve:** Existing section content and labels, persistent report identity and
actions, keyboard access, saved draft state, deep-link behavior, and the full
print/export document. Screen tabs must not turn into a print pagination rule.

**Provenance and decision:** The Threat Hunt Report preview at
`ai-enabled-threathunting/design-previews/20261024/report-redesign/` contains the
proposal, implementation, and section-tab checks. On October 24, the user
approved nested tabs under Report, with one tab for each Report section, and
asked that the rest of the approved appearance stay the same.

**Verification:** The standalone synthetic preview was checked in Chromium,
Firefox, and WebKit at desktop widths 1280, 1440, and 1920px. Its checks cover
tab keyboard behavior, active-panel focus, URL/history navigation, source-panel
closure on section change, long text, and 200% text enlargement. See
`design-proposal.md`, `verification.json`, and `accessibility-verification.json`
in the preview directory. This is not a production-app sign-off.

### Nonmodal source or query inspector

**Use when:** A reader needs source context while keeping the originating
question, search, or report visible. Place the inspector alongside the content
when space allows and below it at constrained desktop widths; do not force a
modal for ordinary evidence browsing.

**Avoid when:** The content is a task that requires a modal decision, or when a
full record viewer, document viewer, or editor already fits the source type
better. A summary inspector must not replace the destination's complete record
view.

**Interaction and accessibility:** Keep the selected source and its owning
question/search explicit. Allow normal navigation while the inspector is open;
do not add a backdrop, focus trap, or extra dismissal step. Close it when the
user leaves its owning section, and leave it closed on return. Escape may close
it while focus is inside; return focus to the source link or selected section.
Keep source links, section navigation, and the close control keyboard reachable.
Represent missing or unavailable source data as such; do not substitute a
different record.

**Preserve:** Exact evidence/query identifiers, citation context, source
provenance, loading/error/empty states, and all existing navigation and
authorization boundaries. A panel opening must not trigger a new query or imply
that evidence was retrieved when it was not.

**Provenance and decision:** The same Threat Hunt Report preview implements this
pattern in `report-preview.js` and `index.html`; the user approved a side panel
for evidence/query links, then specified that it must close when leaving
Questions & conclusions and must be scoped to whichever report section owns it.
Application source counterparts include
`ai-enabled-threathunting/frontend/src/ThreatHuntApp.tsx` and
`ai-enabled-threathunting/frontend/src/EvidenceInspector.tsx`.

**Verification:** The synthetic preview checks nonmodal behavior, source focus,
Escape, focus return, ownership across Questions & conclusions, Search summary,
Timeline, Observations, and Source values, and inline/docked placement at the
desktop widths above. It makes no API requests. The app-specific integration
status must be checked in the current app checkout; preview results do not
establish live source retrieval or full application behavior.

### Flat, labeled source details

**Use when:** A selected source has a manageable set of useful metadata fields
that people should scan together. Present clear labels next to values and keep
the record's source identity visible.

**Avoid when:** The record is very large, deeply nested, or better understood in
a table, document, or structured viewer. Do not silently truncate values or
collapse fields behind an all-purpose “Technical details” heading.

**Interaction and accessibility:** Keep label/value relationships clear in the
reading order and at enlarged text sizes. Wrap long values without clipping;
preserve copyable identifiers and code-like values. If the display has a size
limit, say what was omitted and provide a real path to the complete record.

**Preserve:** Original fields and values, data types where meaningful, exact
source IDs, and explicit unavailable/omitted states. A readable subset is not
the canonical record and must not be exported as if complete.

**Provenance and decision:** In the Report preview, the source panel lists
available fields without a second nested “Technical details” disclosure. The
user explicitly asked to un-nest the panel and make all its content visible.
Related application source for record-field presentation is
`ai-enabled-threathunting/frontend/src/EvidenceInspector.tsx`.

**Verification:** The preview's source-panel checks cover source identity,
visible fields, long text, missing-source behavior, and unchanged canonical
report content across Chromium, Firefox, and WebKit. The synthetic fixture does
not prove that every production record type can be represented as a flat list.
Use the full record viewer/export for large or nested data.

### Answer-first report reading with visible limits and sources

**Use when:** Readers need to understand the saved conclusion before exploring
the supporting detail. Present the question, its saved answer, its recorded
coverage/limitations, and relevant citations as a connected reading unit.

**Avoid when:** Reordering would obscure chronology, source-level comparison, or
the user's primary investigative task. Do not shorten or paraphrase saved
content merely to fit a card.

**Interaction and accessibility:** Use descriptive headings and plain status
labels. Keep material uncertainty near the answer; citations should identify
what they open. Make source inspection optional and reversible. Summary-first
presentation is not a content-generation instruction: prompt/output contracts
must separately define answer length, coverage reasoning, and evidence grounding.

**Preserve:** The saved answer, distinct application/model coverage meanings,
unresolved requirements, limitations, evidence references, and source
attribution. Do not imply that a concise answer is complete or that a citation
proves more than its retained source.

**Provenance and decision:** The Threat Hunt Report preview and
`ai-enabled-threathunting/frontend/src/ReportOverview.tsx` inform the answer and
coverage grouping. The design proposal also reviewed Incident Response
`frontend/analyst-portal/src/components/case-detail/CaseAnalysisView.tsx` and
`CaseDetailUi.tsx`, plus ATO
`portal/src/components/ssp-workspace/WorkspaceRecord.tsx`. These sibling-app
sources informed hierarchy only; the Threat Hunt user approved the Report
content and section layout in the preview.

**Verification:** The preview uses synthetic answers. Its rendered comparison
checks that answers, coverage, limitations, and citations remain present; it
does not verify prompt behavior or production answer quality. The sibling app
files were reviewed as source examples, not browser-tested in this catalog work.

### Draft guard with separate export action

**Use when:** A report can be edited, saved, reviewed/finalized, and exported,
and those actions carry different meaning or consequences.

**Avoid when:** A destination has no draft lifecycle or its existing workflow
intentionally combines those actions. Do not introduce a finalization step just
because a preview has one.

**Interaction and accessibility:** Keep unsaved-change feedback persistent and
clear. Preserve existing leave/discard, save, and finalization guards; make the
destructive or consequential decision understandable and operable by keyboard.
Keep download/export a separate, clearly named action and communicate which
saved version it represents. Handle validation, delayed response, failure, and
duplicate activation using the app's existing workflow.

**Preserve:** Backend lifecycle, approval requirements, immutable saved versions,
report content, full evidence/citations, print/PDF layout and filenames. A screen
preview does not redefine the generated document or authorize finalization.

**Provenance and decision:** The Report preview includes local mock editing and
finalization interactions, while its proposal says the application's saved
report and print/PDF remain unchanged. Inspiration also came from ATO
`portal/src/components/ssp-workspace/ReviewExportPanel.tsx` and
`WorkspaceRecord.tsx`, where review/export are distinct from record context.
These are source references, not a request to copy the ATO workflow into Hunt.

**Verification:** The synthetic preview checks draft feedback, validation,
finalization acknowledgement, and duplicate activation using local-only mock
actions. Its print sample is not the application export. Verify the destination
app's delayed/failed requests, retry behavior, dirty-navigation guard, final
artifact content, and PDF pagination before claiming production parity.

## Reuse record

When adopting one of these patterns, record only what is needed for review:

- selected pattern and destination screen;
- source app/files and the approved user decision that applies;
- adaptation made to fit the destination's current components and workflow;
- browser/route/role/state verification completed and any unverified areas;
- content, permission, data, and print/export contracts checked.

Keep the shared standard authoritative. If adoption changes a shared rule or
visual contract, follow its “Keeping one baseline” release procedure; adding an
app-only interaction does not by itself change the suite baseline.
