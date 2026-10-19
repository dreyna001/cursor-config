# Evidence-grounded SSP authoring

## Decision and loop

Help an ISSO document how a defined system implements the requirements of its
pinned profile, identify evidence gaps, review proposed changes, and export the
approved working revision. SSP content approval is not an authorization to operate.

`system/profile -> evidence -> reviewed facts -> scoped drafting -> questions/
proposals -> human review -> saved-revision approval -> version-bound export`

## Required behaviors

- Verify the mounted SSP workflow and implemented profiles. Do not copy hunting
  concepts such as verdicts, attack timelines, query execution, or recurring hunts
  into the authoring workflow.
- Keep pinned authority/profile/version/baseline, system scope, approved facts,
  source documents, generated drafts, review decisions, and exports distinct.
  Requirements describe obligations, not evidence of implementation.
- Preserve source artifact identity/hash and page/section/image locators through
  extraction, fact review, control mapping, proposals, saved content, and export.
- Select evidence against the actual requirement clauses, parameters, roles,
  implementation responsibility, and system boundary. Include contradictory facts;
  lexical similarity or a control ID match is not evidence sufficiency.
- Track missing evidence, unreviewed facts, unanswered required questions, stale
  confirmations, incomplete drafting, human review, and approval separately.
  A completion percentage is not an effectiveness, compliance, or authorization score.
- Keep useful supported statements even when another clause remains unknown. Do
  not erase correct content to satisfy a validator or invent a complete statement.
- Treat common-provider links as relationships needing evidence and responsibility
  review; they do not prove inheritance, implementation, or effectiveness.
- Use contextual conversation for explanation and proposed changes. Changes remain
  explicit previews/diffs requiring an authorized user's decision; private chat
  and previous model answers do not silently become canonical facts.
- Bind proposed patches, confirmations, approval, and exports to the actual saved
  revision and evidence/profile context. Resolve dirty edits and reject stale work.
- Make new evidence produce an inspectable impact view and scoped draft proposals.
  Preserve prior human edits/reviews and the existing invalidation semantics.
- Provide one canonical editor per item and direct links from blockers/questions
  to the relevant source or edit control. Keep structured JSON as an export or
  advanced inspection format, not a required everyday authoring surface.

## Conditional capabilities

- Improve ongoing evidence maintenance through the existing review/proposal flow;
  scheduled activity must not approve content or imply continuous monitoring.
- Retrieval improvements must preserve provenance, contradictions, human decisions,
  profile pins, and budget behavior; don't add a second evidence registry.
- New profiles require reviewed authority bundles and explicit baseline semantics.
  Reuse the implemented developer profile workflow rather than creating global
  defaults or silently changing an existing workspace's profile.

## Acceptance examples

- A document describing planned MFA cannot establish deployed MFA implementation.
- A screenshot supports only visible details, not system-wide control effectiveness.
- Evidence removal/replacement makes dependent proposals/review state stale through
  existing revision rules; it never rewrites an already approved export.
- An edited or concurrent revision cannot receive approval for different content.
- Unknown responsibility/parameters remain explicit and linked to actionable work.
- JSON/DOCX/draft OSCAL retain source/version bindings and documented export limits.
- Multi-turn assistance retains supported facts while declining authority decisions.

## Scope preservation

Honor current authority and release gates. Do not add assessment, SAP, SAR,
POA&M management, authorization decisions, FedRAMP support, OSCAL conformance,
or continuous monitoring based on a generic agentic checklist. Record these as
intentional boundaries unless the user explicitly scopes a separate capability.
