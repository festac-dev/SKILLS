# Professional Product Creation Toolkit

A local library for product design, application engineering, verification and operations. Start with [SKILL.md](SKILL.md), select [relevant routes](orchestrator/PROJECT_ROUTING.md), and consult [the catalogue](CATALOG.md) for specialist topics. Load only what the actual work needs.

## Install the entrypoint and MCP tools

Install one small skill globally for Codex, Claude Code and OpenCode:

```sh
npx skills add festac-dev/SKILLS --full-depth --skill skills-library --agent codex claude-code opencode -g -y --copy
```

The dataset and search index stay outside agent skill folders. The MCP server exposes **find** (a few IDs and short descriptions) and **read** (a selected guide or supporting file, with bounded pages and continuation positions). First search downloads the pinned index into `~/.cache/festac-skills/`; reads download selected files there on demand. No guide catalogue is added to the AI context automatically.

For a complete local dataset and offline MCP use:

```sh
git clone https://github.com/festac-dev/SKILLS.git
cd SKILLS
sh install.sh all
node scripts/setup-mcp.mjs --all
```

The checkout holds the dataset and `runtime/index.json`. Installation copies only [the entrypoint](https://github.com/festac-dev/SKILLS/tree/main/skills-library) into global agent skill directories. MCP registration preserves other servers and backs up changed configuration files. Node.js 22.20+ runs the server; Python is only needed to maintain the repository.

The shell bootstrap also downloads a complete checkout outside the agent folders:

```sh
curl -fsSL https://raw.githubusercontent.com/festac-dev/SKILLS/main/install.sh | sh -s -- all
```

Register MCP from that checkout using `node ~/.local/share/SKILLS/scripts/setup-mcp.mjs --all`. Choose `--codex`, `--claude-code` or `--opencode` for one agent. Existing unrelated skills are preserved. Open a fresh agent session after installation and MCP registration.

For an entrypoint installed through npx, add the following MCP command to your agent's global configuration: `node ~/.agents/skills/skills-library/scripts/mcp-server.mjs`. Claude's copied entrypoint is at `~/.claude/skills/skills-library/`. Codex uses `[mcp_servers.skills-library]` in `~/.codex/config.toml`, Claude uses `mcpServers` in `~/.claude.json`, and OpenCode uses a local server in the `mcp` object in `~/.config/opencode/opencode.json`. The setup script above registers these automatically from a checkout.

The same bounded engine is available from the CLI:

```sh
node skills-library/scripts/skills.mjs find "motion video" --limit 3
node skills-library/scripts/skills.mjs read motion-studio --limit 80
```

Use `section` / `--section` for a heading, `file` / `--file` for a relative resource, and `offset` and `column` from the returned `next` position to continue. Read returns at most 10,000 UTF-8 content bytes and 160 lines; default is 80 lines. Supporting scripts may need neighbouring files fetched before execution. `SKILLS_LIBRARY_SOURCE` selects a complete checkout for offline use.

Update the source checkout and reinstall the entrypoint after imports. Maintainers run [the index builder](scripts/build_library.py) through `python3 scripts/toolkit.py index`; [the MCP adapter](scripts/mcp-server.mjs), [reader](scripts/skills.mjs) and [registration helper](scripts/setup-mcp.mjs) implement the runtime. The Codex plugin also registers only the single entrypoint.

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

Missing, licensed source skills are added in batches from the skills.sh catalogue. See [collections](COLLECTIONS.md) for the direct skill folders and [the import record](reports/SKILLS_SH_IMPORT.json) for the enumerated snapshot and current batch. Upstream licences remain applicable.

The completed batches add **189 missing guides**. [Snapshot inventory](reports/SKILLS_SH_CATALOGUE.json) records present and pending listings for continuation. Licence-review and unavailable sources remain in the import record.

Maintainers can continue in batches using [the source fetcher](scripts/fetch_skills_sh.py) and [the importer](scripts/import_skills_sh.py). Set `SKILLS_IMPORT_WORK` to an external work directory holding `curation.json` (`sources`: repository-to-skill-name lists; `*` selects every missing guide). The fetcher records pinned revisions and archive digests; the importer skips duplicates and requires an applicable redistribution licence for each guide. Import maintenance needs PyYAML, while the runtime MCP tools have no package dependencies. Run the index builder and collection validation after each batch. Archives, staging files and fetch logs remain in the external work directory.
