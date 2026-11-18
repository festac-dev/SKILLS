---
name: agentic-awesome-app-builder-a7d7d79c
description: Main application building orchestrator. Creates full-stack applications
  from natural language requests. Determines project type, selects tech stack, coordinates
  agents.
metadata:
  upstream_headers:
    risk: critical
    source: community
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# App Builder - Application Building Orchestrator

> Analyzes user's requests, determines tech stack, plans structure, and coordinates agents.

## 🎯 Selective Reading Rule

**Read ONLY files relevant to the request!** Check the content map, find what you need.

| File | Description | When to Read |
|------|-------------|--------------|
| `project-detection.md` | Keyword matrix, project type detection | Starting new project |
| `tech-stack.md` | 2025 default stack, alternatives | Choosing technologies |
| `agent-coordination.md` | Agent pipeline, execution order | Coordinating multi-agent work |
| `scaffolding.md` | Directory structure, core files | Creating project structure |
| `feature-building.md` | Feature analysis, error handling | Adding features to existing project |
| `templates/SKILL.md` | **Project templates** | Scaffolding new project |

---

## Scope and template prerequisites

These13 Markdown templates describe layouts, not complete generated projects. Preserve an existing application's framework, package manager and lockfile; keywords alone do not justify replacing its stack. Template versions are historical baselines and scaffold @latest can produce incompatible layouts/APIs. Check current primary framework docs and host constraints before selecting exact versions. Named agents/tools are optional environment-specific roles, not bundled capabilities or authority to delegate. Honor existing plans rather than requiring a new conflicting filename or three redundant questions. Confirm data/tenant authorization and acceptance examples; keep secrets server-side, review migration effects and use local previews before authorized deployment/publication/payments/messages. Report actual tests, not production-ready guarantees.

## 📦 Templates (13)

Quick-start scaffolding for new projects. **Read the matching template only!**

| Template | Tech Stack | When to Use |
|----------|------------|-------------|
| [nextjs-fullstack](templates/nextjs-fullstack/TEMPLATE.md) | Next.js + Prisma | Full-stack web app |
| [nextjs-saas](templates/nextjs-saas/TEMPLATE.md) | Next.js + Stripe | SaaS product |
| [nextjs-static](templates/nextjs-static/TEMPLATE.md) | Next.js + Framer | Landing page |
| [nuxt-app](templates/nuxt-app/TEMPLATE.md) | Nuxt 3 + Pinia | Vue full-stack app |
| [express-api](templates/express-api/TEMPLATE.md) | Express + JWT | REST API |
| [python-fastapi](templates/python-fastapi/TEMPLATE.md) | FastAPI | Python API |
| [react-native-app](templates/react-native-app/TEMPLATE.md) | Expo + Zustand | Mobile app |
| [flutter-app](templates/flutter-app/TEMPLATE.md) | Flutter + Riverpod | Cross-platform mobile |
| [electron-desktop](templates/electron-desktop/TEMPLATE.md) | Electron + React | Desktop app |
| [chrome-extension](templates/chrome-extension/TEMPLATE.md) | Chrome MV3 | Browser extension |
| [cli-tool](templates/cli-tool/TEMPLATE.md) | Node.js + Commander | CLI app |
| [monorepo-turborepo](templates/monorepo-turborepo/TEMPLATE.md) | Turborepo + pnpm | Monorepo |

---

## 🔗 Related Agents

| Agent | Role |
|-------|------|
| `project-planner` | Task breakdown, dependency graph |
| `frontend-specialist` | UI components, pages |
| `backend-specialist` | API, business logic |
| `database-architect` | Schema, migrations |
| `devops-engineer` | Deployment, preview |

---

## Usage Example

```
User: "Make an Instagram clone with photo sharing and likes"

App Builder Process:
1. Project type: Social Media App
2. Tech stack: Next.js + Prisma + Cloudinary + Clerk
3. Create plan:
   ├─ Database schema (users, posts, likes, follows)
   ├─ API routes (12 endpoints)
   ├─ Pages (feed, profile, upload)
   └─ Components (PostCard, Feed, LikeButton)
4. Coordinate agents
5. Report progress
6. Start preview
```

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
