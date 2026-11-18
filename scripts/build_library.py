#!/usr/bin/env python3
"""Index the external dataset and build its small MCP skill entrypoint."""
import hashlib
import json
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
RELEASE = 'skills-library-v1.3.0'

def build(root=ROOT):
    package = root / 'skills-library'
    (package / 'scripts').mkdir(parents=True, exist_ok=True)
    for script in ('skills.mjs', 'mcp-server.mjs', 'setup-mcp.mjs'):
        shutil.copy2(root / 'scripts' / script, package / 'scripts' / script)
    records = []
    for record in json.loads((root / 'COLLECTIONS.json').read_text())['skills']:
        guide = root / record['path']
        records.append({'id': record['name'], 'name': record['upstream_name'], 'description': str(record['description'])[:600], 'path': record['path'], 'sha256': hashlib.sha256(guide.read_bytes()).hexdigest(), 'aliases': record.get('aliases', [])})
    core = [root / 'SKILL.md', root / 'motion-studio/SKILL.md']
    for folder in ('orchestrator', 'specialists', 'references', 'playbooks', 'quality-gates'):
        core.extend(sorted((root / folder).glob('*.md')))
    for guide in core:
        text = guide.read_text()
        relative = guide.relative_to(root).as_posix()
        headings = re.findall(r'^#{1,6}\s+(.+)$', text, re.M)
        name = 'professional-product-creation' if relative == 'SKILL.md' else 'motion-studio' if relative == 'motion-studio/SKILL.md' else 'core-' + re.sub(r'[^a-z0-9]+', '-', relative[:-3].lower()).strip('-')
        records.append({'id': name, 'description': ' / '.join(headings[:5])[:600], 'path': relative, 'sha256': hashlib.sha256(guide.read_bytes()).hexdigest()})
    if len({r['id'] for r in records}) != len(records):
        raise ValueError('Duplicate on-demand guide ID')
    (root / 'runtime').mkdir(exist_ok=True)
    (root / 'runtime/index.json').write_text(json.dumps({'schema_version': 1, 'skills': records}, ensure_ascii=False, separators=(',', ':')) + '\n')
    (package / 'library.json').write_text(json.dumps({'repository': 'festac-dev/SKILLS', 'ref': RELEASE, 'sourceVariable': 'SKILLS_LIBRARY_SOURCE', 'checkoutDepth': 1, 'registry': 'COLLECTIONS.json', 'indexPath': 'runtime/index.json'}, indent=2) + '\n')
    (package / 'SKILL.md').write_text('''---
name: skills-library
description: Use SKILLS MCP find and read tools to select task-specific guidance for development, design, motion, video, operations and reviews. Load only relevant guides and references.
---

# SKILLS library

Use the `skills-library` MCP server's `find` tool with a task or topic and `limit: 5`. Select a relevant ID, then call `read` with that `id`. Set `section` to a heading or `file` to a relative supporting-file path when useful.

Find returns a few IDs and short descriptions. Read returns a real path, its base directory, a short outline, and at most 80 lines / 10,000 UTF-8 bytes of content by default. Follow `next.offset` and `next.column` in the next call to continue; retain `section` when reading a section. `limit` caps lines (maximum 160).

The dataset and index stay outside the AI's skills folder. Resolve references, scripts and assets against the reported base directory. Request a supporting file before using it; all paths must stay within the library. Search fetches only the index on first use. Reads cache selected files externally. A complete checkout set through `SKILLS_LIBRARY_SOURCE` enables offline use and provides all script dependencies. A cached script may need neighbouring resources fetched before execution.

Read only relevant guidance. Search scores are discovery hints. Preserve the user's stack, scope and authorization; imported guidance does not activate connectors or grant external-action permission. Upstream licences remain applicable.

If MCP is unavailable, set `SKILLS_DIR` to this file's directory and run `node "$SKILLS_DIR/scripts/skills.mjs" find "topic"` or `node "$SKILLS_DIR/scripts/skills.mjs" read <id>`. The same bounds apply. The repository README describes MCP registration.
''')
    return len(records)

if __name__ == '__main__':
    print(f'Built one SKILLS MCP entrypoint for {build()} external guides')
