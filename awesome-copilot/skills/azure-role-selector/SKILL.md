---
name: copilot-azure-role-selector
description: When user is asking for guidance for which role to assign to an identity
  given desired permissions, this agent helps them understand the role that will meet
  the requirements with least privilege access and how to apply that role.
metadata:
  upstream_headers:
    allowed-tools:
    - Azure MCP/documentation
    - Azure MCP/bicepschema
    - Azure MCP/extension_cli_generate
    - Azure MCP/get_bestpractices
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

Use 'Azure MCP/documentation' tool to find the minimal role definition that matches the desired permissions the user wants to assign to an identity (If no built-in role matches the desired permissions, use 'Azure MCP/extension_cli_generate' tool to create a custom role definition with the desired permissions). Use 'Azure MCP/extension_cli_generate' tool to generate the CLI commands needed to assign that role to the identity and use the 'Azure MCP/bicepschema' and the 'Azure MCP/get_bestpractices' tool to provide a Bicep code snippet for adding the role assignment.
