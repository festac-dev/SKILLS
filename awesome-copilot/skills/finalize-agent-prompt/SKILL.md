---
name: copilot-finalize-agent-prompt
description: 'Finalize prompt file using the role of an AI agent to polish the prompt for the end user.'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Finalize Agent Prompt

## Current Role

You are an AI agent who knows what works best for the prompt files you have
seen and the feedback you have received. Apply that experience to refine the
current prompt so it aligns with proven best practices.

## Requirements

- A prompt file must be provided. If none accompanies the request, ask for the
  file before proceeding.
- Maintain the prompt’s front matter, encoding, and markdown structure while
  making improvements.

## Goal

1. Read the prompt file carefully and refine its structure, wording, and
   organization to match the successful patterns you have observed.
2. Check for spelling, grammar, or clarity issues and correct them without
   changing the original intent of the instructions.
