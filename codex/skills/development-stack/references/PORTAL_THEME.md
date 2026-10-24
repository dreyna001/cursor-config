# Historical theme reference

For UI/UX work, start at the permanent local baseline:
`$HOME/.agents/ui-baseline/README.md` (Windows:
`%USERPROFILE%\.agents\ui-baseline\README.md`). On the current workstation,
open [Windows](C:/Users/Daniel.Reyna/.agents/ui-baseline/README.md) or
[WSL](/home/dreyna/.agents/ui-baseline/README.md).
If absent, install the versioned `ui-baseline/` bundle from `cursor-config`;
the app's `docs/suite-ui-standard.md` release copy is the fallback. No GitHub
sign-in is required to read the installed reference. This is the single entry
point for shared rules, adaptation, visual examples, exceptions and validation.
Preserve newer approved login/account, sidebar, typography, colors, layouts,
features and intended behavior; older HTML or guidance cannot override them.

Approved shared UI changes are not complete until the versioned baseline,
its visual companion, all three apps (six frontends), this configuration
repository's reference bundle, and the permanent local baseline are synchronized.
Follow the baseline's “Keeping one baseline” procedure, record app-specific
exceptions and validation, and preserve newer approved behavior and styling.
If any part cannot be updated or verified, report the remaining drift explicitly.

The following is retained historical evidence. Its palette, typography and
geometry do not override the current baseline.

# Portal Theme — "Federal SOC Dark"

Chosen theme for the ATO Evidence Analysis Portal (July 2026 design pass).
It blends two directions that were prototyped in canvas mockups:

- **Palette**: SOC dark console — near-black blue-gray surfaces with a
  saturated blue accent and high-contrast status colors. Matches the
  Splunk/Grafana/SIEM tooling cyber analysts already use.
- **Edges and type**: USWDS conventions — square 2px corner radius and
  Public Sans for UI text with Roboto Mono for identifiers (run IDs,
  digests, blocker codes).

Implemented in `portal/src/index.css` (`.dark` block; the portal runs
dark-only via `<html class="dark">` in `portal/index.html`). No new
libraries — this is CSS variables plus two Google Fonts imports.

**Visual reference (open in any browser):**
[`federal-soc-dark-reference.html`](federal-soc-dark-reference.html)
— workflow mockup, palette swatches, CSS variable table, and accessibility
contrast ratios.

Canonical copy lives in the personal `development-stack` skill under
`references/`. Projects may also keep copies under `docs/` when useful.

## Palette

| Role (shadcn variable)   | Hex       | Usage                                    |
| ------------------------ | --------- | ---------------------------------------- |
| `--background`           | `#0d1117` | Page background                          |
| `--card` / `--popover`   | `#161b22` | Cards, panels, popovers                  |
| `--secondary` / `--muted`| `#1c2129` | Muted fills, selected rows, secondary buttons |
| `--border` / `--input`   | `#30363d` | Borders, input outlines                  |
| `--foreground`           | `#e6edf3` | Primary text                             |
| `--muted-foreground`     | `#8b949e` | Secondary/muted text                     |
| `--primary`              | `#1f6feb` | Primary buttons, focus ring (WCAG AA 4.6:1 with white text) |
| `--primary-foreground`   | `#ffffff` | Text on primary                          |
| `--destructive`          | `#f85149` | Errors, blockers, failed states          |
| `--sidebar`              | `#10141a` | Sidebar background                       |

Status colors: `Badge` variants in `portal/src/components/ui/badge.tsx` use
Tailwind `emerald-400` / `amber-400` text on 15%-tinted fills — the dark-mode
readable steps of those hues (the previous `*-700` steps were tuned for light
backgrounds).

## Accessibility

- Primary buttons: white on `#1f6feb` = 4.6:1, passes WCAG AA. The brighter
  `#2f81f7` from the original SOC mockup fails at 3.7:1 with white text and
  is not used for filled buttons.
- Body text `#e6edf3` on `#0d1117` ≈ 15:1; muted text `#8b949e` ≈ 6.2:1;
  destructive `#f85149` ≈ 5.6:1 — all pass AA on the page background.

## Shape and type

- `--radius: 0.125rem` (2px). shadcn's derived `--radius-sm`/`--radius-md`
  clamp to 0, so small controls render fully square — intentional, per the
  USWDS look.
- UI text: `Public Sans` (fallback: Source Sans Pro, system stack).
- Identifiers/code: `Roboto Mono`, applied to `code`, `kbd`, `pre`, `samp`,
  and Tailwind's `.font-mono`.
- Fonts load from Google Fonts in `index.css`; system fallbacks keep the
  portal usable offline.

## Provenance

Explored in canvas mockups (maintained outside this repository):
`portal-style-directions.canvas.tsx` (USWDS Federal / SOC Dark Console /
Civic Light / Federal Dark blend) and `federal-dark-contenders.canvas.tsx`
(six background-and-accent variations). This document is the durable
record; the canvases are exploratory only.
