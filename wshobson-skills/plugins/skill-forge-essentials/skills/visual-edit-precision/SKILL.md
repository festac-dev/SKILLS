---
name: wshobson-visual-edit-precision
description: Use when making UI/frontend changes guided by visual context, when the
  user selects elements visually, draws annotations, or provides screenshots alongside
  change requests. Also use when editing components where spatial context (element
  identity, DOM references, layout data) supplements text instructions.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Visual Edit Precision

## Overview

When visual context accompanies a change request (element selections, annotations, screenshots), make targeted, minimal edits. Precision over ambition: change exactly what was indicated, preserve everything else.

## Process

When visual context is provided:

1. **IDENTIFY** - What exact element(s) were indicated? Which component file owns them?
2. **SCOPE** - Change ONLY what was pointed at. Don't refactor surrounding code.
3. **PRESERVE** - Keep existing styles, classes, and behavior. Only modify what was asked.
4. **TARGETED** - Make the minimal CSS/markup change that achieves the visual result.
5. **VERIFY** - Confirm the change renders correctly without side effects.

## Key Principles

### Precision Over Ambition

Visual context gives a SPECIFIC element. Don't:
- Refactor the entire component when only one style was requested
- Change the component's API when only its appearance was pointed at
- Touch logic when only visuals were selected

Do:
- Find the exact file and line for the selected element
- Make the minimal edit that achieves the described visual change
- Preserve all existing behavior, event handlers, accessibility

### Multiple Edits

When multiple visual edits arrive:
- Each targets its own element independently
- Don't wait for one to finish before processing another
- If two edits conflict (same element, different requests), handle the most recent

## Common Mistakes

- Rewriting an entire component when the user pointed at one button
- Changing global config when only one element's color needs adjusting
- Breaking responsive behavior by adding fixed widths to match a selection
- Ignoring specificity (user indicated ONE card, agent changed ALL cards)
- Removing accessibility attributes (aria-*, role, tabindex) during visual edits
