---
name: pm-phuryn-code-review
description: Moved to phuryn/product-engineering, where it is maintained in the ai-shipping
  plugin; this copy says where it went and how to install it. Use when asked to review
  changes, find bugs, audit a codebase, or check whether a fix is safe.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Code Review has moved

`code-review` is maintained in [phuryn/product-engineering](https://github.com/phuryn/product-engineering/tree/main/ai-shipping/skills/code-review), in its `ai-shipping` plugin, with the rest of the AI Shipping Kit. This skill stays in pm-skills only so an agent that loads it knows where it went.

- **`ai-shipping:code-review` is installed:** use it, not this copy.
- **It isn't:** tell the user that `code-review` moved and how to install it, then help with the task as you would without it:

  ```bash
  claude plugin marketplace add phuryn/product-engineering
  claude plugin install ai-shipping@product-engineering
  ```

  Other agents: [the repository's README](https://github.com/phuryn/product-engineering#install). Once it's installed, turn off `pm-ai-shipping` here, so this copy no longer loads beside it.
