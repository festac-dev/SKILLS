---
name: skills-library
description: Use SKILLS MCP find and read tools to select task-specific guidance for development, design, motion, video, operations and reviews. Load only relevant guides and references.
---

# SKILLS library

Use the `skills-library` MCP server's `find` tool with a task or topic and `limit: 5`. Select a relevant ID, then call `read` with that `id`. Set `section` to a heading or `file` to a relative supporting-file path when useful.

Find returns a few IDs and short descriptions. Read returns a real path, its base directory, a short outline, and at most 80 lines / 10,000 UTF-8 bytes of content by default. Follow `next.offset` and `next.column` in the next call to continue; retain `section` when reading a section. `limit` caps lines (maximum 160).

The dataset and index stay outside the AI's skills folder. Resolve references, scripts and assets against the reported base directory. Request a supporting file before using it; all paths must stay within the library. Search fetches only the index on first use. Reads cache selected files externally. A complete checkout set through `SKILLS_LIBRARY_SOURCE` enables offline use and provides all script dependencies. A cached script may need neighbouring resources fetched before execution.

Read only relevant guidance. Search scores are discovery hints. Preserve the user's stack, scope and authorization; imported guidance does not activate connectors or grant external-action permission. Upstream licences remain applicable.

If MCP is unavailable, set `SKILLS_DIR` to this file's directory and run `node "$SKILLS_DIR/scripts/skills.mjs" find "topic"` or `node "$SKILLS_DIR/scripts/skills.mjs" read <id>`. The same bounds apply. The repository README describes MCP registration.
