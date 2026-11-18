# Professional Product Creation Toolkit

A local library for product design, application engineering, verification and operations. Start with [SKILL.md](SKILL.md), select [relevant routes](orchestrator/PROJECT_ROUTING.md), and consult [the catalogue](CATALOG.md) for specialist topics. Load only what the actual work needs.

## Install for your AI app

These public commands work for anyone. Choose the app you use. `-g` makes the entrypoint available across projects; the second command registers the MCP server in that app's user configuration. Node.js 22.20+ and Git are required.

### Codex

```sh
npx skills add festac-dev/SKILLS --full-depth --skill skills-library --agent codex -g -y --copy
node "$HOME/.agents/skills/skills-library/scripts/setup-mcp.mjs" --codex
```

### Claude Code

```sh
npx skills add festac-dev/SKILLS --full-depth --skill skills-library --agent claude-code -g -y --copy
node "$HOME/.claude/skills/skills-library/scripts/setup-mcp.mjs" --claude-code
```

### OpenCode

```sh
npx skills add festac-dev/SKILLS --full-depth --skill skills-library --agent opencode -g -y --copy
node "$HOME/.agents/skills/skills-library/scripts/setup-mcp.mjs" --opencode
```

### All three apps

```sh
npx skills add festac-dev/SKILLS --full-depth --skill skills-library --agent codex claude-code opencode -g -y --copy
node "$HOME/.agents/skills/skills-library/scripts/setup-mcp.mjs" --all
```

The installer uses each person's home directory. MCP registration preserves other servers and backs up changed configuration files. Open a fresh agent session after setup.

## Read skills through MCP

The AI's skill folders contain only a small entrypoint and its runtime scripts. The dataset and index stay outside those folders. MCP `find` returns a few IDs and short descriptions; `read` loads a selected skill, section, or supporting file in bounded pages. Default: 80 lines, with at most 10,000 UTF-8 content bytes; maximum: 160 lines. Follow the returned `next.offset` and `next.column` to continue.

On first search, the index is cached under `~/.cache/festac-skills/` (or `XDG_CACHE_HOME`). Selected skills and files are cached there on demand. The full catalogue is never inserted into AI context automatically.

For offline use, clone the repository outside your agent's skills folder. Register MCP from the checkout:

```sh
git clone https://github.com/festac-dev/SKILLS.git
cd SKILLS
node scripts/setup-mcp.mjs --all
```

The setup script finds the checkout on the current machine. `SKILLS_LIBRARY_SOURCE` can also select a complete local dataset. Supporting scripts may require neighbouring resources before execution.

The shell installer also installs one entrypoint from a complete checkout. Maintainers use [the index builder](scripts/build_library.py), [MCP server](scripts/mcp-server.mjs), [reader](scripts/skills.mjs), and [setup helper](scripts/setup-mcp.mjs). The Codex plugin exposes the same single entrypoint.

## Working with the library

For substantial projects, use [the master workflow](orchestrator/MASTER_ORCHESTRATOR_PROMPT.md). For narrow changes, go directly to the owning resource. Preserve the user’s requirements and project conventions; the catalogue is not a feature checklist.

The specialist guides include concrete domain checks. References explain reusable decisions, templates capture useful evidence, playbooks connect the work, and quality gates assess the result. Apply only relevant sections and remove unused template fields.

## Optional repository maintenance

These commands are for maintainers changing the repository, rather than for installing or using skills. Run from this directory with Python 3.10+; the helper uses the standard library:

```sh
python scripts/toolkit.py route 'Make distinct logos and visual identities'
python scripts/toolkit.py search 'offline synchronization'
python scripts/toolkit.py index
python scripts/toolkit.py validate
python scripts/toolkit.py dry-run
python scripts/toolkit.py audit
python -m unittest discover -s tests -v
```

`index` regenerates the catalogue, routing guide and [machine manifest](manifest.json) from the current sources and route registry. `validate` checks links, route/schema integrity, discoverability, duplicate content/titles, retired paths, deterministic routing cases and behavioral-result records. `audit` emits a read-only inventory with SHA-256 fingerprints and recorded evaluation statuses.

The historical [merge baseline](reports/MERGE_BASELINE.json) records the original imported material. Authorized revisions may update that material. `validate --preserve-baseline` is an optional check of the old append-only merge contract and can fail intentionally after a revision. Missing original resources are still flagged by ordinary validation.

## Backend and operations

The [backend delivery playbook](playbooks/BACKEND_DELIVERY_PLAYBOOK.md) connects architecture, API contracts, databases, identity, queues, realtime, release, host operations, observability and recovery. Dedicated database, queue and server guides deepen the existing backend coverage. Start from a real operation and the installed stack; these capabilities are available when needed, not prescribed infrastructure.

## Visual references and identity

Use [reference analysis](references/visual-reference-analysis.md) for supplied videos, carousels, profiles and repositories. It covers retrieval, sampling, observed versus inferred behavior, licensing, cleanup and transfer into an actual project. The [direction brief](templates/VISUAL_DIRECTION_AND_MOTION_BRIEF.md) is optional for substantial design work. Brand, motion, UX and video owners define the implementation and its verification.

## Demo-video production

The [video workflow](playbooks/PRODUCT_DEMO_VIDEO_PLAYBOOK.md) covers product evidence, story, capture, narration, timing, captions, rendering and audio/visual QA. Styles and tools are recommendations governed by the actual brief. The optional [media checker](scripts/media_audit.py) inspects local exports with FFmpeg/ffprobe; it uses no paid services and creates no reports by default.

## Evidence and limits

[Routing cases](evals/ROUTING_EVALS.json) execute the helper. [Behavioral cases](evals/SKILL_EVALS.json) describe agent outcomes and remain `not_run` until executed with evidence. Static validation does not prove agent quality, live integrations, accessibility conformance or production readiness.

The [current upgrade report](reports/UPGRADE_VERIFICATION.md) records this revision and its applied project checks. Earlier [inventory](reports/INVENTORY.md), [gap analysis](reports/GAP_ANALYSIS.md) and [merge verification](reports/VERIFICATION.md) are historical records, not current runtime evidence.

## Consolidated archive and examples

The CLAUDE archive is merged into this library. [The merge map](reports/CLAUDE_MERGE_MAP.json) records the source fingerprints and canonical destinations of imported resources. Overlapping guides have one owner; callers use that owner's path instead of a second toolkit or redirect copy. [Archive history](reports/CLAUDE_IMPORT_HISTORY.md) is retained as historical context.

[Examples](examples/README.md) include interactive graphics and a local backend reference. Their dependencies, data and limits are illustrative, not project defaults. [AGENTS.md](AGENTS.md) and [CLAUDE.md](CLAUDE.md) both point to the shared skill instructions.

Imported resources have provenance and static checks; importing them does not establish behavioral evaluation. Existing agent scenarios remain unexecuted unless their records include actual evidence. New authored guidance still requires scenario coverage; template and reference imports are tracked separately from executed agent tests.

## Imported GitHub collections

The requested collections live directly under this directory; see [COLLECTIONS.md](COLLECTIONS.md). Their skill names are prefixed by collection, supporting files and notices are retained, and [COLLECTION_RULES.md](COLLECTION_RULES.md) reconciles their workflow conventions with current user instructions. Find relevant guides through MCP, or inspect [the collection catalogue](COLLECTIONS.md) while maintaining the dataset. Run `python3 scripts/skill_collections.py validate` for supporting-file digests, namespaces and compatibility checks. Importing source code does not install or activate its external tools.

## License

Project-authored toolkit material and integration changes use [Apache-2.0](LICENSE). Imported material retains its upstream licenses and terms; see [NOTICE.md](NOTICE.md) and the license files within each collection.

## Skills.sh imports

SKILLS contains **18029 skills**: 18027 imported skills and two core skills. The catalogue imports have added **2450 skills** in completed batches, including **2261 in the latest batch. Skills use names such as `skills-azure-deploy`, `skills-playwright-cli`, and `skills-apple-design`.

See [collections](COLLECTIONS.md), [the batch record](reports/SKILLS_SH_IMPORT.json), and [the snapshot inventory](reports/SKILLS_SH_CATALOGUE.json) for source revisions, results and pending listings. Licences and required supporting resources are preserved. Repeated source bytes are skipped instead of counted as additions.

Maintainers continue batches with [the source fetcher](scripts/fetch_skills_sh.py) and [the importer](scripts/import_skills_sh.py). Set `SKILLS_IMPORT_WORK` to an external work directory holding `curation.json` (`sources`: repository-to-skill-name lists; `*` selects every missing skill). Import maintenance uses PyYAML; MCP has no package dependencies. After a batch, regenerate the index and run collection validation. Archives, staging files and logs stay in the external work directory.
