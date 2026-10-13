---
name: react
description: "Create or review React interfaces, components, hooks, and explicit UI states."
---
# React Skill

Use when creating, editing, or reviewing React frontend code.

Follow these rules:

* Use functional components, hooks, and composition.
* Keep components small and focused.
* Separate UI, state, API calls, and business logic.
* Prefer derived state over unnecessary `useEffect`.
* Handle loading, error, empty, and success states.
* Use stable keys; never use array index when an ID exists.
* Keep forms accessible and predictable.
* Avoid unnecessary `useMemo`, `useCallback`, and abstraction.
* Do not introduce new UI/state libraries unless required.
* For cybersecurity portals, follow **Federal SOC Dark**: read `development-stack/references/PORTAL_THEME.md` and open `development-stack/references/federal-soc-dark-reference.html` from the installed skill folder.
* Keep frontend types aligned with backend API schemas.
* Remove dead code, unused imports, console logs, and duplicate logic.
* Prefer simple, readable, production-ready code.
* For layout, navigation, form-state, and scroll-area decisions, follow the shared [UI/UX organization](../engineering-guidance/references/ui-ux-organization.md) guidance. In the ATO portal, use the matching `.portal-scroll-*` utilities in `portal/src/index.css` to implement its scroll-area recommendations.

## Component styling and visual systems

* Before styling a component, inspect the app's theme, shared UI primitives, design tokens, and nearby screens. Follow the established system instead of introducing a competing look.
* Prefer existing primitives and semantic theme tokens/utilities for colors, surfaces, borders, spacing, typography, and focus states. Avoid hard-coded colors, one-off CSS, or duplicate buttons, badges, cards, and help controls when the shared component can express the need.
* Keep hover, focus, active, disabled, loading, success, and error states consistent with the shared component patterns. Preserve readable contrast, visible focus, and responsive behavior.
* Make local presentation changes locally. Change shared primitives or theme tokens only when the intended effect is shared across the app.
* For cybersecurity portals, use the Federal SOC Dark reference linked above for the palette, typography, corner treatment, and status colors; keep its detailed values in that reference rather than creating local variants.
* Keep expandable cards visually continuous: the trigger, single section title, status, and expanded content share one card outline. Avoid a separate bordered trigger followed by a second card that repeats the same title. When correcting one expandable section, check its sibling sections for the same pattern.

## Icons: Lucide React

* Preserve an application's established icon library. For apps already using Lucide, including the ATO portal, use `lucide-react` consistently; do not add a second icon library or replace it during unrelated UI work. Other existing icon systems do not need migration.
* Import named icons directly, for example `import { FileText, Sparkles } from "lucide-react"`. Keep icons bundled with the application; do not introduce an icon CDN, remote kit, icon font, or a dynamic whole-catalog lookup for a known icon.
* Preserve Lucide's outline style and default stroke width unless an existing local pattern calls for a change. Let icons inherit `currentColor`; use the application's semantic color utilities for intentional status/accent colors.
* Follow shared component sizing. The ATO portal's Button primitive sizes descendant SVGs to `size-4` (16 px), prevents shrinking, and supplies the icon/text gap; standalone help icons also use `size-4`, while compact navigation/status icons use `size-3` (12 px). Inspect the shared primitive before overriding those styles.
* Hide decorative icons from assistive technology with `aria-hidden="true"`; let visible text name the action. Give icon-only buttons an accessible action name on the button, and preserve keyboard focus and tooltips where useful. Never communicate an essential state through the icon alone.
* Choose icons for the actual action and reuse the same meaning consistently. The ATO portal's document-generation and SSP Assistant actions reuse the shared `ssp-workspace/AiDocumentIcon.tsx`: `FileText` with a small `Sparkles` overlay, indicating AI document work. Its wrapper is `h-4 w-5`, with a `size-2.5!` overlay to override Button's descendant sizing. Generation progress uses `LoaderCircle` with `animate-spin`, and Stop uses `Square`; do not replace these during an unrelated change.
* Keep icon combinations local until actual reuse warrants sharing. Check the rendered composition at its real button size, including clipping, spacing, inherited color, and loading/disabled states; do not add a general icon framework for one combination.

## UI clarity and contextual help

* Make hierarchy and grouping visible: keep a value, its label, status, and help affordance visually together. Do not leave a help icon looking like an unrelated item in a neighboring row.
* Use direct labels that state what a value or status means. Prefer plain states such as “Not approved” over workflow jargon whose meaning is not obvious from the screen.
* Keep essential instructions visible near the field or action. Use a tooltip or small help popover for secondary explanation, definitions, provenance, or details that users may need occasionally; do not hide required steps only in a tooltip.
* Anchor contextual help to the specific label or control it explains, using the app's established tooltip or popover primitive. Give its trigger an accessible name, support keyboard and touch without relying on hover, preserve visible focus, and ensure the content stays readable on narrow screens and near viewport edges.
* When help explains a title or metric, place its trigger inline with that title or label, not beside the value it describes. Match the surrounding title-row pattern.
* Tailor help content to the user's likely decision: define the current value; include possible values with short meanings when they help compare or choose; explain status/provenance and the next step when relevant. Combine these only as needed, and avoid dumping unrelated or exhaustive options into every tooltip.
* Explain values concretely: say what the value represents and, when useful, what changes it. Avoid repeating the label or using vague copy such as “more information.”
* Before finishing a UI change, inspect the rendered layout at the relevant screen size and verify that labels, help, status, and actions remain associated and readable.

### Resizable sidebars

* When a sidebar takes space from the main workspace, provide a visible resize handle and a practical minimum width so users can reclaim content space without making navigation unusable.
* Keep navigation labels and utility actions anchored to stable padding during resizing. Size compact controls to their contents when stretching or centering them would cause unnecessary movement. Keep the navigation start stable when a header wraps; if truncation is appropriate, preserve the full accessible label.
* Support pointer dragging and keyboard resizing with an accessible separator, announced current/minimum/maximum widths, and enforced bounds. Preserve the main content's ability to shrink or scroll without overlap.
* Persist a user's width when that matches the application's navigation behavior. Match the product's existing visual system; examples may guide spacing and interaction without becoming styling references.

## Security boundaries

When touching authentication, API credentials, browser persistence, uploads/previews or untrusted content rendering, read [application security](../engineering-guidance/references/security.md) and the matching framework reference it routes to. Preserve the selected auth SDK and approved serving architecture. Layout-only changes do not require an audit or production retrofit.

## Tool references

- When building or deploying a Vite app, read [Vite production practices](references/vite-production.md).
- When adding or maintaining Vitest unit/component tests, read [Vitest practices](references/vitest-production.md).
- When adding or maintaining Playwright browser tests, read [Playwright practices](references/playwright-production.md).
