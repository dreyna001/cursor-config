## Regression obligations

When changing evidence, assistant review or exports, preserve these existing
contracts; they are not requests for new features:

- Adding, replacing or removing evidence has the documented effect on dependent
  facts, proposals and confirmations. Control source re-analysis stays scoped to
  the selected control; saving source links alone does not call a model.
- Private conversations do not change canonical SSP content without an approved
  proposal. Statement, status and responsibility changes require explicit review.
- Dirty or stale proposals cannot apply different content or overwrite human
  edits. Source/profile/evidence changes invalidate the appropriate decisions.
- JSON, DOCX and draft OSCAL export the exact saved revision with current
  provenance and limitations. Earlier exports and stored history remain intact;
  exporting does not require a separate SSP approval.
- Content completion and review do not establish control effectiveness,
  compliance or authorization. Synthetic checks do not replace independent SME
  or customer qualification, and do not close authority/release gates.

Current behavior is described in the current project-root `docs/APP_AI_WORKFLOW.md` and the
current project-root `docs/SSP_WORKSPACE_OPERATOR_GUIDE.md`.
