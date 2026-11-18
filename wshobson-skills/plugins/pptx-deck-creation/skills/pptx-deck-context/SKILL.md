---
name: wshobson-pptx-deck-context
description: Use when preparing the narrative, sources, and design context for a new
  editable PPTX deck.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# PPTX Deck Context

Prepare the deck before coordinates or PPTX objects are authored. This skill owns the business narrative, source lineage, and design lock.

## Decision sequence

1. Confirm audience, decision, slide count, language, sources, and brand requirements.
2. Use the user-selected narrative framework. If none is specified, offer `mckinsey`, `scqa`, `pyramid`, `mece`, `action-title`, `assertion-evidence`, `exec-summary-first`, or `custom`; do not choose silently.
3. Assign stable source IDs and plan a `source_ref` for every metric, quotation, chart value, and factual claim.
4. Choose a documented design direction. Prefer a user brand guide, then read-only reference-deck evidence, then a reusable profile from `references/design-profiles.md`.
5. Record the framework, assumptions, source manifest, palette, typography, spacing, and signature elements in `summary` before authoring slides.

## Rules

- One slide should communicate one message, with an action-style title where the framework calls for it.
- Treat design references as design evidence, not content or asset sources.
- Do not copy external fonts, images, icons, or logos without recorded licensing evidence.
- Translate design signals into explicit fills, typography, spacing, and bboxes; do not rely on an automatic layout engine.
- Keep long source material concise. Ask for a summary or decision-relevant excerpt instead of turning a deck spec into a document dump.

See `references/design-profiles.md` for reusable profile guidance.
