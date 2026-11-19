# SKILLS Index & Fast Lookup Guide for AI Models

> **IMPORTANT NOTICE FOR AI MODELS**:
> **DO NOT** attempt to scan all directories or parse `COLLECTIONS.json` (83MB) or `runtime/index.json` (9.2MB). Doing so will exhaust your context window.
> This repository contains **19,573 skills**. Use one of the fast, targeted methods below to find and load only the specific skill you need.

## 1. Instant CLI Search (Recommended)

Run the search tool from your shell / command execution tool. It searches all 19,573 skills in milliseconds and returns exact paths and summaries:

```bash
# 1. Keyword search (fast full-text ranking):
python3 /data/home/SKILLS/scripts/search.py 'kubernetes ingress deploy'

# 2. Search filtered by domain category:
python3 /data/home/SKILLS/scripts/search.py --category cloud-devops 'terraform aws'

# 3. Inspect a skill and view its instructions without reading the entire file:
python3 /data/home/SKILLS/scripts/search.py --info <skill-id>

# 4. Machine-readable JSON output (for automated parsing):
python3 /data/home/SKILLS/scripts/search.py --json --limit 5 'react tailwind'
```

## 2. Instant Grep Quickref (Zero Dependencies)

A single-line TSV index of all 19,573 skills (`id`, `name`, `category`, `collection`, `path`, `summary`):

```bash
grep -i 'fastapi' /data/home/SKILLS/runtime/indexes/skills_quickref.tsv | head -n 10
```

## 3. SQLite Full-Text Search (FTS5)

The database `/data/home/SKILLS/runtime/indexes/skills.db` is indexed with SQLite FTS5 for sub-millisecond queries:

```bash
sqlite3 /data/home/SKILLS/runtime/indexes/skills.db \
  "SELECT id, category, path, description FROM skills_fts WHERE skills_fts MATCH 'postgres' LIMIT 5;"
```

## 4. Browse by Domain Categories

If you need to explore available skills for a specific domain, read ONLY the corresponding category index file:

| Category | Skills | Description | Category File |
|---|---|---|---|
| **Programming Languages, CLI Tools, Compilers & Utilities** | 5620 | Python, TypeScript, Go, Rust, C++, shell scripting, CLI tools, algorithms, and developer utilities. | [categories/programming-languages.md](categories/programming-languages.md) |
| **Prompt Engineering, LLM Interfaces & Fine-Tuning** | 3365 | System prompts, task prompting, persona prompts, OpenAI/Anthropic APIs, RAG, and embeddings. | [categories/ai-prompts-llms.md](categories/ai-prompts-llms.md) |
| **AI Agents, Autonomous Workflows & Orchestration** | 2056 | Autonomous agents, subagents, multi-agent swarms, tool calling, memory, and orchestration. | [categories/ai-agents.md](categories/ai-agents.md) |
| **Cloud Platforms, Infrastructure as Code & DevOps** | 1401 | AWS, GCP, Azure, Terraform, CloudFormation, Ansible, CI/CD pipelines, and cloud operations. | [categories/cloud-devops.md](categories/cloud-devops.md) |
| **Application Security, Vulnerability Analysis & Exploits** | 1165 | AppSec, CVE vulnerability analysis, penetration testing, exploit detection, fuzzing, and secure coding. | [categories/security-appsec.md](categories/security-appsec.md) |
| **Marketing, SEO, Copywriting & Content Growth** | 1084 | Content marketing, copywriting, SEO optimization, growth tactics, email campaigns, and analytics. | [categories/marketing-growth.md](categories/marketing-growth.md) |
| **Security Audits, Hardening, Compliance & Threat Modeling** | 588 | RedHat ProdSec, SlowMist, Trail of Bits, IAM policies, compliance (SOC2/HIPAA), hardening, and firewall rules. | [categories/security-auditing.md](categories/security-auditing.md) |
| **3D Modeling, Blender, Three.js, WebGL & Canvas** | 500 | Three.js scenes, Blender scripting, WebGL shaders, 3D meshes, procedural graphics, and spatial rendering. | [categories/graphics-3d-motion.md](categories/graphics-3d-motion.md) |
| **Databases, SQL, PostgreSQL, Supabase, Prisma & Caching** | 472 | PostgreSQL, MySQL, SQLite, Supabase, Neon, Prisma ORM, Redis caching, migrations, and query tuning. | [categories/databases-storage.md](categories/databases-storage.md) |
| **Video Production, Audio Processing, TTS & Media Generation** | 451 | Motion Studio, Remotion, FFmpeg video editing, ElevenLabs TTS, audio ducking, subtitles, and media pipelines. | [categories/media-video-audio.md](categories/media-video-audio.md) |
| **Frontend Development, React, Vue, Next.js & Frameworks** | 447 | React, Vue, Svelte, Next.js, Nuxt, Angular, Astro, TypeScript frontend, DOM, and client state. | [categories/web-frontend.md](categories/web-frontend.md) |
| **Software Architecture, Clean Code, Git & Monorepos** | 345 | Architectural design patterns, clean code principles, refactoring, Git workflows, and monorepo management. | [categories/software-architecture.md](categories/software-architecture.md) |
| **Product Strategy, PRDs, Roadmaps & Feature Specs** | 322 | Product requirements documents (PRDs), user journeys, feature roadmaps, OKRs, and discovery protocols. | [categories/product-management.md](categories/product-management.md) |
| **UI/UX Design Systems, Tailwind, CSS & Components** | 285 | Tailwind CSS, design systems, Shadcn UI, CSS animations, responsive layouts, icons, and UX patterns. | [categories/web-styling-ui.md](categories/web-styling-ui.md) |
| **Backend Development, REST APIs, GraphQL & Microservices** | 285 | FastAPI, Express, Django, Flask, Spring, REST endpoints, GraphQL schemas, gRPC, and webhooks. | [categories/backend-apis.md](categories/backend-apis.md) |
| **Data Science, Scientific Computing, Bioinformatics & NCBI** | 270 | Scientific computing, bioinformatics, NCBI datasets, genomics, chemistry modeling, pandas, and data analytics. | [categories/data-science-scientific.md](categories/data-science-scientific.md) |
| **Testing, QA, Automation, Playwright, Jest & Cypress** | 235 | End-to-end testing, Playwright CLI, Cypress, unit tests (pytest/Jest), test mocks, and QA verification. | [categories/testing-qa.md](categories/testing-qa.md) |
| **Docker, Containers, Kubernetes & Orchestration** | 232 | Dockerfiles, container builds, Kubernetes pods/deployments/ingress, Helm charts, and container runtimes. | [categories/containers-kubernetes.md](categories/containers-kubernetes.md) |
| **Mobile App Development, React Native, Flutter, iOS & Android** | 230 | React Native, Expo, Flutter, Swift, SwiftUI, Kotlin, Android SDK, and cross-platform mobile patterns. | [categories/mobile-apps.md](categories/mobile-apps.md) |
| **Smart Contracts, Solana, Ethereum & Web3** | 220 | Solana development, Ethereum Solidity contracts, DeFi protocols, token standards, and Web3 SDKs. | [categories/blockchain-web3.md](categories/blockchain-web3.md) |

## 5. Collections Directory

To see all 115 imported upstream collections and which domains they cover, consult [collections.md](collections.md).

## 6. How to Load and Apply a Skill

Once you identify the relevant skill path (e.g. `openai-plugins/plugins/adobe/skills/adobe-create-mockups/SKILL.md`):
1. Read **only** that specific `SKILL.md` file using your file read tool.
2. Apply the instructions to the user's project.
3. Never read entire collection folders or unneeded files.
