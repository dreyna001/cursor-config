---
name: cursor-cloud-config
description: "Maintain Cursor-specific configuration in this repository when requested; inspect the actual files and scripts and verify feature availability."
---

# Cursor Configuration Maintenance

Use this skill only when the user asks to maintain the Cursor configuration or cloud workflow represented by this repository. It describes Cursor artifacts; it does not make Cursor CLI, cloud-agent, hook, or settings capabilities available inside Codex.

## Workflow

1. Inspect the current repository tree, its instructions, scripts, and documentation before choosing a workflow.
2. Identify whether the request concerns skills, project rules, hooks, MCP configuration, or project installation. These are separate Cursor surfaces with different locations and formats.
3. Use only scripts and integrations that actually exist in the checkout or are exposed in the current environment. Do not assume a Windows path, Cursor cloud sync, private remote, slash command, or external service is configured.
4. Preserve the distinction between source configuration and a project copy. Explain which repository or files the requested change affects.
5. Validate the edited files with the repository's documented checks. If a Cursor-specific operation is unavailable, provide the local artifact or exact manual next step instead of simulating it.
6. Do not commit, push, install into another project, or change hosted settings unless the user authorized that operation.

## Portability Notes

- Cursor skills, project rules, hooks, MCP settings, and cloud-agent settings are Cursor-specific. Do not translate their file formats into Codex formats unless the user asks for a migration; use Codex's own skills and project instructions for Codex behavior.
- Paths vary by operating system and user configuration. Resolve them from the current checkout or official Cursor documentation rather than relying on historical personal paths.
- Cloud availability and supported configuration surfaces can change. Verify them from current official Cursor documentation when the request depends on hosted behavior.
