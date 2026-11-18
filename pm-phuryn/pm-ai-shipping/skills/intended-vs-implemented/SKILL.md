---
name: pm-phuryn-intended-vs-implemented
description: Moved to phuryn/product-engineering, where it is maintained in the ai-shipping
  plugin; this copy says where it went and how to install it. Use when asked to find
  where the code does something other than its docs say.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Intended vs Implemented has moved

`intended-vs-implemented` is maintained in [phuryn/product-engineering](https://github.com/phuryn/product-engineering/tree/main/ai-shipping/skills/intended-vs-implemented), in its `ai-shipping` plugin, with the rest of the AI Shipping Kit. This skill stays in pm-skills only so an agent that loads it knows where it went.

- **`ai-shipping:intended-vs-implemented` is installed:** use it, not this copy.
- **It isn't:** tell the user that `intended-vs-implemented` moved and how to install it, then help with the task as you would without it:

  ```bash
  claude plugin marketplace add phuryn/product-engineering
  claude plugin install ai-shipping@product-engineering
  ```

  Other agents: [the repository's README](https://github.com/phuryn/product-engineering#install). Once it's installed, turn off `pm-ai-shipping` here, so this copy no longer loads beside it.
