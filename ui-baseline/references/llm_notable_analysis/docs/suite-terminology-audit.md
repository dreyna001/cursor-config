# Incident Response terminology audit

Date: 2026-10-19 | Shared vocabulary: 1.0.0

## Applied

- All four frontends (on-premises, AWS GovCloud, commercial AWS, and Azure) use
  **Incident Response Workspace** in sidebar branding, sign-in identity, and browser titles.
- Replaced AI Case Assistant with **Incident Response Assistant**, including
  navigation, assistant headings, advisory copy, and accessibility labels.
- Replaced Chatbot readiness with **Assistant readiness**, including loading
  skeletons and case metadata. Retrieval descriptions name the assistant.
- Retained exchanges are **Conversations** with **New conversation**, **Delete
  conversation**, and **Conversation history** labels. Empty-state copy uses
  conversation instead of investigation thread. Existing New chat title sentinels
  are translated only for display; stored records and draft logic remain unchanged.
- Current UI navigation, capability/error messages, and authentication copy use
  workspace instead of portal. Account copy uses Signed in as and Sign out.
- Added the shared vocabulary, root README/agent entry points, and local check.

## Reviewed and retained

- Alerts and source-specific notables are not renamed incidents. Cases remain
  case records. Closed Tickets represents synchronized external tickets, not
  closed cases, so its name remains correct.
- Evidence, citations, findings, recommendations, run/review states, severity,
  priority, and confidence retain their actual domain contracts. No response
  execution or incident classification capability is implied by the new app name.
- Chat remains valid as an interaction mode; Conversations names retained exchanges.
- Routes, API fields (including chatbot readiness fields), OpenAPI titles,
  package/component identifiers, authentication events, storage keys, and saved
  titles retain compatibility. Platform-specific deployments remain separate.
- Historical plans, frozen schemas, dated release evidence, design mockups, and
  operator-tool identifiers keep their original names. Revisit terminology when
  they become active user-facing product content.

## Verification

Run `python3 scripts/check_suite_terminology.py` from the repo root. Each frontend
uses its existing affected unit tests, TypeScript checks, and production build;
desktop browser checks inspect real branding/navigation layouts. The terminology
check does not validate source truth, model quality, or live integrations.

## Recorded local results — 2026-10-19

- 320 affected unit tests passed: on-premises 87, AWS GovCloud 69, commercial AWS 91, Azure 73.
- All four TypeScript checks and production builds passed.
- On-premises sign-in/workspace, both AWS workspaces, and Azure sign-in passed in Chromium, Firefox, and WebKit (15 desktop surface checks).
- Browser checks used isolated local previews and mocked application APIs. Azure sign-in used a separate build with synthetic public OIDC identifiers; it did not exercise a real identity provider or authenticated Azure workspace.
- Terminology check passed, including a separate negative control that rejects a retired product name. Shared guide and checker hashes match across all three repositories.
- Changed-file whitespace review passed. Existing unrelated work was preserved.
- Verification was performed locally before publication; no services or deployments were restarted or updated.

## Remote-main candidate verification — 2026-10-19

- 320 frontend unit tests passed on the isolated remote-main candidate.
- All applicable frontend TypeScript checks and production builds passed.
- Known terminology checks and changed-file whitespace checks passed.
- Only terminology changes and their documentation/tests are included; unrelated primary-checkout edits remain excluded.

## Workflow usability follow-up — 2026-10-19

See [context, evidence and recovery fixes](ui-context-evidence-recovery-20261019.md)
for the scoped interaction changes and local verification. The shared vocabulary
and domain-specific review/approval contracts remain unchanged.

## Brand package and app placement — 2026-10-19

The selected mark and versioned [brand package](../brand/README.md) are now
included in this repository. Each app variant uses the same master mark in its
sidebar and sign-in screen and serves the matching favicon. The package's
outlined wordmarks support document and marketing production. The mark is a
visual identity and does not imply automatic containment or remediation.
