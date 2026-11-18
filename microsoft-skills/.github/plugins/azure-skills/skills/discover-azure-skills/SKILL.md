---
name: microsoft-discover-azure-skills
description: 'Searches the Azure skills catalog and recommends installable agent skills
  by matching an Azure task to skill metadata and plugin installation guidance. WHEN:
  before starting any task that involves an Azure or Microsoft-cloud service, product,
  or data source, when no currently loaded skill or tool already covers it.'
license: MIT
metadata:
  author: Microsoft
  version: 1.0.2
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

Follow these steps to discover the available azure skill matching the given task description.

1. List plugins

List Azure plugin directories from the GitHub Contents API: https://api.github.com/repos/microsoft/azure-skills/contents/.github/plugins?ref=main

In the result, each entry whose `type` is `dir` is a plugin directory. Skills are organized by plugins.

2. List skills

For each plugin, list their skills from the GitHub Contents API: https://api.github.com/repos/microsoft/azure-skills/contents/.github/plugins/{plugin-dirname}/skills?ref=main

In the result, each entry whose `type` is `dir` is a skill directory. Each skill has a SKILL.md file that explains what this skill should be used for.

3. Discover relevant skills

Eliminate the skills that obviously aren't relevant by their names. Then for each remaining skill, read their description from the API: https://raw.githubusercontent.com/microsoft/azure-skills/main/.github/plugins/{plugin-dirname}/skills/{skill-name}/SKILL.md

Use the descriptions to further eliminate skills that aren't relevant.

4. Discover the plugin name of the relevant skills

For each relevant skill, discover their plugin name by reading the `plugin.json` from the GitHub Contents API: https://raw.githubusercontent.com/microsoft/azure-skills/main/.github/plugins/{plugin-dirname}/.plugin/plugin.json

This is important because a plugin's name may be different from its directory name. The installation commands depend on the plugin's name.

5. Report the matched skills

Report the matched skills and offer instructions to install them. Skills can be installed by installing their plugin. Read the installation instructions matching the agent client to offer the installation instructions.

- [Copilot CLI](./references/install/copilot-cli.md)
- [Claude Code](./references/install/claude-code.md)
- [Other](./references/install/other.md)