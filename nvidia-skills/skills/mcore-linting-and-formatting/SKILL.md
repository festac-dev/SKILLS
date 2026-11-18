---
name: nvidia-mcore-linting-and-formatting
description: Linting and formatting for Megatron-LM. Covers running autoformat.sh,
  tools (ruff, black, isort, pylint, mypy), and code style rules.
license: Apache-2.0
metadata:
  author: Philip Petrakian <ppetrakian@nvidia.com>
  upstream_headers:
    when_to_use: Running linting or autoformat; fixing style violations before a PR;
      'pre-commit fails', 'ruff error', 'isort', 'mypy', 'style violation', 'how do
      I format', 'autoformat.sh'.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Linting and Formatting

---

## Running the Formatter

Run before opening a PR:

```bash
# Check mode (no changes applied)
BASE_REF=main CHECK_ONLY=true SKIP_DOCS=false bash tools/autoformat.sh

# Fix mode
BASE_REF=main CHECK_ONLY=false bash tools/autoformat.sh
```

Tools invoked: `black`, `isort`, `pylint`, `ruff`, `mypy`.

---

## Import Ordering

After editing imports in any Python files, always run `uv run isort` on those
files before committing:

```bash
uv run isort <file1>.py <file2>.py
```

---

## Setting Up the Linting Group

Inside the container:

```bash
uv sync --locked --only-group linting
```

This installs `ruff`, `black`, `isort`, `pylint` — the same tools used by
`tools/autoformat.sh` and CI's `linting` job.

---

## Code Style Rules

- **Type hints**: required on all public API functions. Use `X | None`, not `Optional[X]`.
- **Docstrings**: Google-style on all public classes and functions.
- **Naming**: follow Python conventions — `snake_case` for functions and variables, `PascalCase` for classes.
- **Line length**: 119 characters (configured in `pyproject.toml`).
- **No bare `except`**: always catch specific exception types.
