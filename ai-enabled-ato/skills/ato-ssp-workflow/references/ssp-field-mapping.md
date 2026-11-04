## SSP field mapping

- Component **name** identifies it; **purpose** describes its function;
  **placement** describes its relationship to the authorization boundary.
- Do not copy a complete inventory row into purpose. Preserve the original source
  and citation, including accountability details, in supported records or control text.
- Do not invent a component owner field. Names remain valid in component identities
  and responsible-actor statements; this rule is not a blanket name filter.
- Fixes to prompts or synthetic inputs do not authorize rewriting saved workspaces.
  Existing values need a reviewed edit.

Relevant coverage lives in the SSP generation, system-definition and vision tests,
`tests/test_fgrs_runner_helpers.py`, and the component-mapping browser fixture.
