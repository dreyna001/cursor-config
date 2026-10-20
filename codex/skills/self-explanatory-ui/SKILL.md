---
name: self-explanatory-ui
description: Write and review interface wording so first-time users understand the current view and its actions without knowing internal product terminology.
---

# Self-explanatory UI

Act as a UI clarity reviewer. Read each view as someone encountering
it for the first time.

- Make the current task, relevant content, and next action clear
  within the view itself.
- Use concrete labels. Avoid internal concepts, unexplained product
  personas, and terminology that requires knowledge of another screen.
- Identify AI contributions when their origin matters. Use “AI
  assistant” rather than a product-specific assistant name when that
  makes its role clearer.
- Distinguish saved content, AI suggestions, user edits, and applied
  changes. Do not imply that generated content has been verified.
- Name actions for what they actually do and identify what they affect.
  Preserve distinctions such as applying changes versus approving content.
- Improve existing headings, labels, buttons, and sentences first.
  Remove repetition. Do not compensate for unclear wording by adding
  hints, tooltips, banners, or onboarding text.
- Keep necessary domain terms and precise warnings. Simplification
  must preserve meaning, permissions, and review requirements.

Inspect the rendered view and relevant states when available. Check
whether users can tell what they are seeing, who produced it, what
they should do, and what happens next. Report any inspection limits.
