# cursor-config

This repository is the canonical source for global Cursor rules/skills and Codex instructions/skills. It is not an application product.

- Cursor loads `rules/*.mdc` from `~/.cursor/rules/` after install. Use the `cursor-rules` skill as the router.
- Codex loads `codex/global-instructions.md` as `~/.codex/AGENTS.md`. Use the `engineering-guidance` skill as the router.
- Install steps and harness details are in [README.md](README.md).
- Keep standing policies aligned in `rules/` and `codex/global-instructions.md` when both harnesses should follow them.
