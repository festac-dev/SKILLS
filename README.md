# Professional Product Creation Toolkit

A local library for product design, application engineering, verification and operations. Start with [SKILL.md](SKILL.md), select [relevant routes](orchestrator/PROJECT_ROUTING.md), and consult [the catalogue](CATALOG.md) for specialist topics. Load only what the actual work needs. For instant search across all 19,573 imported and core skills without reading entire directories, run `python scripts/search.py "<topic>"` or consult `SKILLS_GUIDE.md` at the workspace root.

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

## Fast skill search and AI model discovery

With **19,573 skills** across 115 collections, reading or scanning whole directories will exhaust an AI model's context window. The repository provides a lightweight search CLI, an indexed SQLite FTS5 database, a single-line TSV quickref, and 20 domain-specific index files to find and preview skills in under 50ms without context bloat.

### Instant CLI search

Run `scripts/search.py` (zero external dependencies) to search all skills with BM25 relevance ranking:

```sh
# General topic search across all 19,573 skills
python3 scripts/search.py "docker deployment"

# Filter by domain category or collection
python3 scripts/search.py --category cloud-devops "terraform"
python3 scripts/search.py --collection aws-agent-toolkit-for-aws "lambda"

# Preview a skill's instructions in-terminal without loading the full file
python3 scripts/search.py --info <skill-id>

# Machine-readable JSON output for automated agents
python3 scripts/search.py --json --limit 5 "react tailwind"

# List all 20 categories and skill counts
python3 scripts/search.py --categories
```

### Full-text search and quickref data

- **SQLite Database (`runtime/indexes/skills.db`)**: 17 MB standalone SQLite database with an FTS5 full-text search table across all skills, categories, collections, and descriptions.
- **Single-Line TSV Quickref (`runtime/indexes/skills_quickref.tsv`)**: Grep-friendly plain-text file (`id`, `name`, `category`, `collection`, `path`, `summary`) for shell pipelines:
  ```sh
  grep -i "fastapi" runtime/indexes/skills_quickref.tsv | head -n 10
  ```
- **Master Navigation Guide**: `runtime/indexes/SKILLS_GUIDE.md` provides complete usage instructions, querying tips, and skill execution protocols for AI agents.

### Domain categories

Skills are categorized into 20 bounded Markdown files under `runtime/indexes/categories/`:

| Domain Category | Skills | Focus Areas |
|---|---|---|
| `ai-agents` | 2,056 | Multi-agent swarms, autonomous workflows, tool calling, memory |
| `ai-prompts-llms` | 3,365 | Prompt engineering, system prompts, OpenAI/Anthropic APIs, RAG |
| `cloud-devops` | 1,401 | AWS, GCP, Azure, Terraform, CloudFormation, CI/CD pipelines |
| `containers-kubernetes` | 232 | Dockerfiles, container builds, Kubernetes pods, Helm, Ingress |
| `security-appsec` | 1,165 | AppSec, CVE vulnerability research, exploits, payloads, fuzzing |
| `security-auditing` | 588 | RedHat ProdSec, SlowMist, Trail of Bits, IAM, compliance, hardening |
| `web-frontend` | 447 | React, Vue, Svelte, Next.js, Nuxt, DOM manipulation, state |
| `web-styling-ui` | 285 | Tailwind CSS, Shadcn UI, design systems, responsive UI, motion |
| `backend-apis` | 285 | FastAPI, Express, Django, Flask, REST APIs, GraphQL, microservices |
| `databases-storage` | 472 | PostgreSQL, Supabase, Neon, Prisma, MySQL, SQLite, Redis caching |
| `testing-qa` | 235 | Playwright, Cypress, Jest, pytest, end-to-end testing, visual QA |
| `graphics-3d-motion` | 500 | Three.js, Blender, WebGL shaders, 3D meshes, spatial rendering |
| `media-video-audio` | 451 | Video editing, Remotion, FFmpeg, TTS, audio ducking, ElevenLabs |
| `mobile-apps` | 230 | React Native, Expo, Flutter, iOS (Swift), Android (Kotlin) |
| `product-management` | 322 | PRDs, user stories, feature specifications, roadmaps, OKRs |
| `marketing-growth` | 1,084 | SEO, copywriting, content marketing, growth campaigns, analytics |
| `blockchain-web3` | 220 | Solana, Ethereum, Solidity smart contracts, DeFi, Web3 protocols |
| `data-science-scientific` | 270 | Bioinformatics, NCBI datasets, genomics, chemistry, scientific computing |
| `software-architecture` | 345 | Clean code, architectural patterns, refactoring, Git, monorepos |
| `programming-languages` | 5,620 | Python, TypeScript, Go, Rust, C++, CLI utilities, algorithms |

### Regenerating the AI search index

Whenever new skill collections are imported, rebuild the SQLite database, TSV quickref, and category indexes:

```sh
python3 scripts/build_ai_index.py
```

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

SKILLS contains **19,341 skills**: 19,339 imported skills and two core skills. Completed skills.sh batches have added **3,762 skills**. The latest batch added **1,312 skills**. Skills use names such as `skills-azure-deploy`, `skills-playwright-cli`, and `skills-apple-design`.

See [collections](COLLECTIONS.md), [the batch record](reports/SKILLS_SH_IMPORT.json), and [the snapshot inventory](reports/SKILLS_SH_CATALOGUE.json) for source revisions, results and pending listings. Licences and required supporting resources are preserved. Repeated source bytes are skipped instead of counted as additions.

Maintainers continue batches with [the source fetcher](scripts/fetch_skills_sh.py) and [the importer](scripts/import_skills_sh.py). Set `SKILLS_IMPORT_WORK` to an external work directory holding `curation.json` (`sources`: repository-to-skill-name lists; `*` selects every missing skill). Import maintenance uses PyYAML; MCP has no package dependencies. After a batch, regenerate the index and run collection validation. Archives, staging files and logs stay in the external work directory.
