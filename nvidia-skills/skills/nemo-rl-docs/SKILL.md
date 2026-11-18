---
name: nvidia-nemo-rl-docs
description: 'Documentation conventions for NeMo-RL. Covers docs/index.md updates
  and docstring format. Do NOT use for: bug fixes, test fixes, dependency bumps, refactoring,
  CI/CD changes, performance tuning, or any task that does not involve writing or
  updating documentation.'
license: Apache-2.0
metadata:
  upstream_headers:
    when_to_use: Adding or updating documentation; adding a new markdown file; reviewing
      docstrings; 'docs/index.md', 'docstring format', 'Sphinx', 'where do I add docs',
      during code review.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Documentation Conventions

## Keep docs/index.md Up to Date

When a new markdown doc is added under `docs/**/*.md` or a markdown file is renamed, ensure that @docs/index.md is updated and the document appears in the most appropriate section.

## Docstring Format

Use [Google style](https://google.github.io/styleguide/pyguide.html) docstrings for classes and functions. These are parseable by Sphinx.

For interfaces that may be used outside a file, prefer docstrings over comments. Comments should be reserved for code within a function or interfaces local to a file.

## Document New Features

When a new feature is added, update or create documentation in the `docs/` directory that most closely matches the feature. Look at existing docs to find the best fit — if none exists, create a new doc and add it to @docs/index.md.

Documentation changes are **not required** for bug fixes or CI-related changes.
