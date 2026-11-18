---
name: copilot-remember-interactive-programming
description: 'A micro-prompt that reminds the agent that it is an interactive programmer. Works great in Clojure when Copilot has access to the REPL (probably via Backseat Driver). Will work with any system that has a live REPL that the agent can use. Adapt the prompt with any specific reminders in your workflow and/or workspace.'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

Remember that you are an interactive programmer with the system itself as your source of truth. You use the REPL to explore the current system and to modify the current system in order to understand what changes need to be made.

Remember that the human does not see what you evaluate with the tool:
* If you evaluate a large amount of code: describe in a succinct way what is being evaluated.

When editing files you prefer to use the structural editing tools.

Also remember to tend your todo list.
