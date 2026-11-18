---
name: alireza-wiki-init
description: Bootstrap a fresh LLM Wiki vault with the three-layer structure, schema files, and starter templates. Usage /wiki-init <path> --topic "<topic>" [--tool all|claude-code|codex|cursor|antigravity]
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

<!-- canonical copy: engineering/llm-wiki/commands/wiki-init.md — keep in sync -->

# /wiki-init

Bootstrap a new LLM Wiki vault. Creates `raw/`, `wiki/{entities,concepts,sources,comparisons,synthesis}`, the index and log, and installs the schema file(s) for your LLM CLI of choice.

## Usage

```
/wiki-init <path> --topic "<one-line topic>"
/wiki-init <path> --topic "<topic>" --tool <claude-code|codex|cursor|antigravity|opencode|gemini-cli|all>
/wiki-init <path> --topic "<topic>" --force    # overwrite non-empty dir
```

## Examples

```
/wiki-init ~/vaults/research --topic "LLM interpretability"
/wiki-init ./book-wiki --topic "The Power Broker — Robert Caro" --tool all
/wiki-init ~/vaults/founders --topic "SaaS founder playbook" --tool codex
```

## What it creates

```
<path>/
├── raw/
│   └── assets/
├── wiki/
│   ├── index.md              # from template
│   ├── log.md                # from template
│   ├── entities/
│   ├── concepts/
│   ├── sources/
│   ├── comparisons/
│   ├── synthesis/
│   └── .templates/           # page templates for reference
├── CLAUDE.md                 # if --tool claude-code or all
├── AGENTS.md                 # if --tool codex|cursor|antigravity|opencode|gemini-cli|all
├── .cursorrules              # if --tool cursor or all
└── .gitignore
```

## Next steps

After init:
1. Open the vault in Obsidian
2. Drop a source into `raw/`
3. Run `/wiki-ingest raw/<your-file>`

## Script

- `engineering/llm-wiki/skills/llm-wiki/scripts/init_vault.py`

## Skill Reference

→ `engineering/llm-wiki/skills/llm-wiki/SKILL.md`
