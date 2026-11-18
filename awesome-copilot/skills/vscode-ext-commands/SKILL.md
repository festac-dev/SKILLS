---
name: copilot-vscode-ext-commands
description: 'Guidelines for contributing commands in VS Code extensions. Indicates naming convention, visibility, localization and other relevant attributes, following VS Code extension development guidelines, libraries and good practices'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# VS Code extension command contribution

This skill helps you to contribute commands in VS Code extensions

## When to use this skill

Use this skill when you need to:
- Add or update commands to your VS Code extension

# Instructions

VS Code commands must always define a `title`, independent of its category, visibility or location. We use a few patterns for each "kind" of command, with some characteristics, described below:

* Regular commands: By default, all commands should be accessible in the Command Palette, must define a `category`, and don't need an `icon`, unless the command will be used in the Side Bar.

* Side Bar commands: Its name follows a special pattern, starting with underscore (`_`) and suffixed with `#sideBar`, like `_extensionId.someCommand#sideBar` for instance. Must define an `icon`, and may or may not have some rule for `enablement`. Side Bar exclusive commands should not be visible in the Command Palette. Contributing it to the `view/title` or `view/item/context`, we must inform _order/position_ that it will be displayed, and we can use terms "relative to other command/button" in order to you identify the correct `group` to be used. Also, it's a good practice to define the condition (`when`) for the new command is visible.
