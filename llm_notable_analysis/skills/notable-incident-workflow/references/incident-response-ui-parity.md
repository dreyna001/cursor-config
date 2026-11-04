# Incident Response UI parity

The four products remain independently buildable and deployable. Common source is
copied into each frontend; no product imports a sibling checkout at build or
runtime. The current approved redesign is an **on-prem-first presentation pilot**.
Its scoped layout changes do not roll out to the three cloud frontends.

`incident-response-ui-parity.json` identifies the files that must be byte-identical
across all four products, explains the native deployment adapters, and records the
limited on-prem presentation overrides with exact SHA-256 values and reasons.

## On-prem presentation pilot

The reviewed layout and component mapping are documented in
On-prem workspace layout pilot (current project-root `docs/ui-onprem-workspace-layout-20261030.md`). The
parity contract treats these three categories separately:

- `identical_files` remain byte-identical across all four frontends.
- `deployment_adapters` retain native authentication, API, upload, recovery, and
  provider behavior. A layout change is not a deployment adapter.
- `onprem_presentation_overrides` is an exact allowlist for the reviewed on-prem
  pilot. Existing overridden files must still match each other byte-for-byte in
  the three cloud products; the on-prem copy must match its pinned SHA-256.
  On-prem-only files must be absent from the cloud products and match their own
  pinned hashes. Every entry includes its reason.

This is a narrow pilot exception, not a broad `src/` exemption. New or modified
on-prem presentation sources must be individually listed with a reason and a new
reviewed hash. Unlisted on-prem changes and any cloud drift still fail the check.
When a change is later approved for all products, remove its override and restore
the shared-file requirement. Do not change native deployment adapters just to
make the layouts look alike.

## Checks

Run:

```bash
python3 scripts/check_ir_ui_parity.py
python3 scripts/check_suite_ui.py
python3 scripts/check_suite_foundation.py
```

The check rejects accidental edits to shared copies, changed cloud copies beneath
an on-prem override, an on-prem override that no longer matches its reviewed hash,
unlisted frontend sources, and stale adapter or override entries. Matching source
does not replace rendered checks.

Shared sources continue to govern the suite controls and styling, common
navigation and conversation primitives, empty/loading/error treatments, and
capacity colors/count formatting. The on-prem pilot has separately pinned
exceptions for sidebar arrangement, case analysis, evidence presentation, and
closed-ticket layout. The cloud three remain byte-identical across all shared
sources and among their copies of each source beneath an on-prem override. Native
callers inject their account controls into the common sidebar slots.

Keep authentication, API schemas, upload destinations, recovery and token provenance
native. On-prem inline images and server uploads, S3 uploads and Azure Blob uploads
retain their respective contracts and capability gates. Case-list controllers retain
native filtering, cursor ordering and refresh/scroll behavior; a page-local AWS filter
can have more results to check even when the current page has no matches. Azure can
show provider/cache usage details supplied only by its API. These differences must
not cause unrelated spacing, wording or control-layout differences.

Use the same layout for equivalent states. Show an optional field, action or detail
only when its native inputs/capabilities support it; do not fabricate parity by enabling
unsupported features or dropping supported evidence. Record a reason before adding a
new deployment adapter; do not move presentation into an adapter merely to pass the gate.

The on-prem pilot is scoped to that deployment; it does not update the suite
standard or the other products.

## Queue and evidence interaction contracts

Within an authenticated app session, Cases retains filters, draft filters and
pagination when opening a case and returning with Back or Return to results.
Cursor reuse is limited to 30 minutes. Expired cursors, invalid page responses
and restored terminal empty pages recover without discarding the filters;
ordinary empty pages with continuation cursors retain normal pagination.
Context remains in memory only, resets when the authenticated app unmounts,
and is not copied into URLs or browser storage. Reload starts a new context.

Failed reads retain filters and available rows, show an adjacent Retry action,
and preserve cancellation. Refresh bookkeeping records successful queries only,
so an interrupted StrictMode load cannot suppress recovery of that query.

Evidence inspection supports field/value/source search, 50-row display pages,
180-character previews and full-value expansion. Expansion uses plain text and
preserves literal values, including significant whitespace. Citation navigation
clears conflicting filters and opens the page containing the original field ID.
Full value means the complete loaded field; archive bounds and Technical details
paging still apply. Keep source and observation/inference labels intact.

Shared navigation and conversation components receive native account/logout
controls. Attachment presentation is shared, but upload protocols, validation,
retry, capacity and capability gates stay native. Optional report locations are
shown only when supplied; recovery links respect the deployment's base path.
Headerless card bodies retain a 16px inset, disclosures share their content
gutters, and metadata values can shrink and wrap without losing their labels.

## Focused regression coverage

For changes to these contracts, use each affected frontend's
`CasesQueue.test.tsx`, `EvidenceFields.test.tsx`, `caseAnalysisProjection.test.ts`
and `e2e/queue-evidence-recovery.spec.ts`. Cover same-query retry, retained rows,
StrictMode return, cursor expiry, literal values, and citation focus through
filtering/pagination. Preview data must keep archived cases separate from
synchronized ServiceNow tickets; see the on-prem `test_preview_fake_db.py` tests.

Rendered checks should include Cases, case details, Closed Tickets and Assistant
states at the affected desktop widths, including long values, unavailable data,
keyboard access, guarded dialogs, attachment limits and error recovery. Verify
native browser zoom separately from font resizing when zoom is in scope. Source
parity and geometry alone do not prove visual quality or screen-reader speech.
Use isolated synthetic API/identity fixtures; they do not qualify production
identity, live uploads, model reasoning or customer deployment. Preserve the
current on-prem pilot coverage and limits (current project-root `docs/ui-onprem-workspace-layout-20261030.md`).
