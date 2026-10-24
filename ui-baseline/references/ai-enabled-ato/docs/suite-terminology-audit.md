# ATO terminology audit

Date: 2026-10-19 | Shared vocabulary: 1.0.0

## Applied

- Sidebar, sign-in identity, and browser title use **ATO Workspace** instead of
  SSP Drafting Portal or ATO Evidence Analysis Portal.
- The interactive capability is **ATO Assistant** in navigation, headings, and
  accessibility text. Send to assistant replaces Send to agent in the UI fallback.
- The primary navigation groups **Capabilities** and names the current capability
  **SSP Drafting**. This distinguishes the app from the current workflow.
- **SSP Workspace Inventory** qualifies the scoped records listed by management;
  internal routes and identifiers remain unchanged.
- Conversation history and Private conversation consistently name retained
  assistant exchanges. Error and navigation copy uses workspace instead of portal.
- Added the shared vocabulary, README/agent entry points, and local check.

## Reviewed and retained

- SSP workspace names a scoped working environment for an SSP inside ATO Workspace.
  It is not a second app. Profiles remain SSP requirement profiles, not user profiles.
- Systems, controls, SSPs, evidence, extracted facts, citations, and shared proposals
  remain distinct. Source review, SSP approval, and system authorization remain
  different actions; none is relabeled to imply a broader capability.
- Existing state machines, permissions, retention statements, evidence provenance,
  approval gates, and supported exports remain unchanged.
- API paths/fields, storage, component names, CSS classes, and historical contract
  documents retain their technical/original names. No database migration is needed.
- The broader ATO name does not enable unimplemented authorization workflows.

## Verification

Run `python3 scripts/check_suite_terminology.py` from the repo root. Verification
uses local frontend tests, TypeScript checks, build, and desktop browser checks.
GitHub Actions remains disabled under repository guidance. The terminology check
detects known naming drift and does not prove semantic correctness.

## Recorded local results — 2026-10-19

- 44 affected frontend unit tests passed.
- TypeScript checks and production build passed.
- Sign-in and authenticated branding/navigation passed in Chromium, Firefox, and WebKit (6 desktop surface checks).
- Terminology check passed, including a separate negative control that rejects a retired product name. Shared guide and checker hashes match across all three repositories.
- Changed-file whitespace review passed. Existing unrelated work was preserved.
- Verification was performed locally before publication; no services or deployments were restarted or updated.
- Browser checks used mocked application APIs in isolated local previews; they do not qualify live integrations or identity providers.

## Remote-main candidate verification — 2026-10-19

- 44 frontend unit tests passed on the isolated remote-main candidate.
- All applicable frontend TypeScript checks and production builds passed.
- Known terminology checks and changed-file whitespace checks passed.
- Only terminology changes and their documentation/tests are included; unrelated primary-checkout edits remain excluded.

## Workflow usability follow-up — 2026-10-19

See [context, evidence and recovery fixes](ui-context-evidence-recovery-20261019.md)
for the scoped interaction changes and local verification. The shared vocabulary
and domain-specific review/approval contracts remain unchanged.

## User-requested assistant label exception — 2026-10-20

- Use **AI assistant** in ATO navigation, assistant headings, accessible names,
  and Changes instructions. The user requested a literal role that first-time
  users can understand without knowing the product-specific persona.
- **ATO Workspace** remains the product name. Shared vocabulary version 1.0.0
  remains unchanged; this is an ATO display-language exception, not a rename
  of other suite assistants or API/storage objects.
- The ATO branch of the terminology checker expects the requested local label.

### Verification of the wording follow-up

- 42 focused component tests passed, including source display, revision checks,
  selected decisions, edited text preservation, and assistant navigation.
- Nine browser scenarios passed across Chromium, Firefox, and WebKit: evidence
  handoff and combined Apply, navigation and empty Changes, and preserving edits
  through filtering, sibling decisions, and older revisions at desktop widths.
  One Chromium run encountered a page reload during concurrent verification;
  its trace shows a second document load. The unchanged-source rerun passed.
  The reload trigger was not established as an application defect.
- These populated browser scenarios intercept application APIs with synthetic
  records. They do not mutate installed workspaces or qualify backend persistence.
- Live sign-in, the actual empty Changes view, the AI assistant label, and API
  readiness were verified against the installed stack. No evidence-change
  proposals were returned by the live workspace listing for this user.
- TypeScript, production build, public-bundle, terminology, and whitespace checks
  passed. The existing large-chunk build warning remains.
- Local screenshots and traces are under
  `/home/dreyna/.cache/ato-changes-wording-20261020/`; final populated screenshots
  are in `final-browser/playwright-results/`, and the Chromium confirmation is
  in `chromium-focus-confirmed/playwright-results/`. No paid model calls were made.

## First-use wording across SSP views — 2026-10-20

The [remaining-view wording review](evaluations/workspace-wording-review-20261020.md)
applies the approved self-explanatory UI skill to Controls, Evidence, SSP
Document, Overview, System Setup and its tabs, and Review & Export. Existing
labels and instructions identify AI actions, saved drafts, human confirmation,
and exact-revision approval more directly. The shared approval badge names the
SSP; the actual ISSO role and authorization boundary are unchanged. These are
local display-language refinements, with no shared vocabulary version change.
