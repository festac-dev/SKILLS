# Professional Product Creation Toolkit

A local library for product design, application engineering, verification and operations. Start with [SKILL.md](SKILL.md), select [relevant routes](orchestrator/PROJECT_ROUTING.md), and consult [the catalogue](CATALOG.md) for specialist topics. Load only what the actual work needs.

## Install all skills

On Linux or macOS, install the complete library with one command:

```sh
curl -fsSL https://raw.githubusercontent.com/festac-dev/SKILLS/main/install.sh | sh
```

Or clone the full repository and install it directly:

```sh
git clone https://github.com/festac-dev/SKILLS.git
cd SKILLS
sh install.sh codex
```

The default installs **all 15,579 skills**, including the main toolkit,
Motion Studio and every imported collection, with their supporting files.
**Python and npm are not required for installation or skill discovery.**
There is no selection or Python search-helper step.

Codex CLI uses the native `complete-skills@festac-skills` bundle. Its manifest
registers each skill directory explicitly, so the complete library is
available despite limits on scanning one large directory. Skill names include
`$complete-skills:anthropic-pdf` and `$complete-skills:motion-studio`.
The same native setup can be run without the shell bootstrap:

```sh
codex plugin marketplace add .
codex plugin add complete-skills@festac-skills
```

Choose another agent by appending `claude-code` or `opencode`. Native skill
directories link to the complete checkout, retaining references, scripts,
assets, relative paths and license notices. Keep the checkout in place.
Existing unrelated skills are preserved, and repeat installations are safe.

```sh
sh install.sh opencode
sh install.sh claude-code
sh install.sh codex --dry-run
sh install.sh --list
```

Open a fresh agent session after installation. To update, run `git pull` in the
checkout and repeat the install command. Dependencies used by a particular
skill's scripts belong to that task, rather than to installing the library.

### Using the standard skills CLI

If you use [skills.sh](https://skills.sh), Node.js 22.20+ and Git, select individual skills with its normal installer:

```sh
npx skills add festac-dev/SKILLS --full-depth
```

Choose skills and agents in the prompts. Add `-g` for a user-wide installation or `-y -a opencode --skill motion-studio` for a specific agent and skill. `--full-depth` discovers the nested imported collections. Use the native installer above for the complete toolkit with a shared checkout. The standard CLI manages its own copies with `npx skills update` and `npx skills remove`.

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

The requested collections live directly under this directory; see [COLLECTIONS.md](COLLECTIONS.md). Their skill names are prefixed by collection, supporting files and notices are retained, and [COLLECTION_RULES.md](COLLECTION_RULES.md) reconciles their workflow conventions with current user instructions. Browse the native skill list, [the collection catalogue](COLLECTIONS.md), or `sh install.sh --list`. No Python discovery command is required. Run `python3 scripts/skill_collections.py validate` for supporting-file digests, namespaces and compatibility checks. Importing source code does not install or activate its external tools.

## License

Project-authored toolkit material and integration changes use [Apache-2.0](LICENSE). Imported material retains its upstream licenses and terms; see [NOTICE.md](NOTICE.md) and the license files within each collection.
