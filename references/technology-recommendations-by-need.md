# Technology Recommendations by Need

**How to use:** these are conditional starting candidates, not mandates. First inspect the project. Preserve its existing stack. Only recommend a change when a requirement is unmet, risk is real, or the cost of staying is documented. Always state *why* and *what you gave up*. Verify current versions, licensing, pricing, and support before committing; technology moves faster than this file.

## Backend runtimes and frameworks
| Situation | Candidates | Why / trade-off |
|---|---|---|
| Team already knows a language | Stay in it | Skill and ecosystem beat marginal technical gains |
| Rapid CRUD + admin, batteries included | Django, Rails, Laravel, ASP.NET Core, Spring Boot | Mature auth, ORM, migrations; heavier than micro-frameworks |
| Typed APIs, JS/TS across stack | Node.js with Fastify/Express/Nest/Hono, Deno, Bun | Shared types and talent pool; mind CPU-bound work |
| High-concurrency network services | Go, Rust (Axum/Actix), Java/Kotlin, Elixir/Phoenix | Efficiency and concurrency; steeper hiring or learning curve in some cases |
| Data/AI-heavy services | Python (FastAPI, Django), plus workers | Ecosystem; watch GIL and async design |
| Real-time at scale | Elixir/Phoenix, Go, Node with a pub/sub backplane, managed realtime | Connection handling model |
| Tiny services/glue | Serverless functions, Hono/Workers-style edge runtimes | Limits and cold starts |

## Databases
| Need | Candidates |
|---|---|
| General transactional | PostgreSQL (rich features, extensions), MySQL/MariaDB |
| Embedded/edge/single-node | SQLite (with WAL; Litestream/LiteFS-style replication if needed), libSQL/Turso-type offerings |
| Massive key-value scale | DynamoDB, Cassandra/Scylla, Redis/Valkey for hot data |
| Flexible documents | MongoDB, Firestore, PostgreSQL JSONB |
| Analytics | ClickHouse, BigQuery, Snowflake, DuckDB, TimescaleDB |
| Search | Postgres FTS → Meilisearch/Typesense → OpenSearch/Elasticsearch |
| Vectors | pgvector first for modest scale; dedicated engines when scale or features require |
| Queues | Postgres-backed, Redis, RabbitMQ, SQS, Kafka/Redpanda (streams) |

## Hosting
| Situation | Candidates |
|---|---|
| One app, small team, limited ops | PaaS (Render, Railway, Fly.io, Heroku-style) or a well-managed VPS |
| Static/Jamstack + functions | Vercel, Netlify, Cloudflare Pages/Workers |
| Cost-sensitive steady workload | VPS/bare metal (Hetzner, OVH, DigitalOcean, Linode) with solid automation and backups |
| Enterprise integration/compliance | AWS, Azure, Google Cloud with IaC and landing zone |
| Container workloads without cluster ops | Cloud Run, ECS/Fargate, Azure Container Apps |
| Many services, platform team | Kubernetes (managed) with GitOps |

## Auth
Managed IdP (Auth0, Clerk, Cognito, Firebase Auth, Supabase Auth, WorkOS, Keycloak self-hosted, Ory) when speed and enterprise features matter; framework-native sessions for simple first-party apps; passkeys as primary or additional factor when the audience supports them.

## Observability
OpenTelemetry for instrumentation; Grafana stack or a hosted vendor for storage/visualization; Sentry-style error tracking; uptime probes from outside.

## IaC and config management
Terraform/OpenTofu or Pulumi for cloud resources; Ansible or cloud-init for host configuration; Helm/Kustomize for Kubernetes; Docker Compose for single-host stacks.

## Frontend graphics and motion
| Need | Candidates |
|---|---|
| UI transitions | CSS, View Transitions API, Motion/Framer Motion, GSAP |
| Complex timelines/scroll | GSAP (+ScrollTrigger), CSS scroll-driven animations |
| Authored animation | Lottie/dotLottie, Rive |
| 2D canvas/game-like | PixiJS, Canvas 2D, Phaser |
| 3D | Three.js (+React Three Fiber), Babylon.js, PlayCanvas, model-viewer |
| Data visualization | D3, Observable Plot, Vega-Lite, ECharts, deck.gl/MapLibre for maps |
| Shaders | GLSL/WGSL, OGL, regl; WebGPU with fallback |
| Physics | Rapier, Matter.js, springs |

## Recommendation format (use in reports)
**Context → Options considered → Recommendation → Why → What it costs/risks → Exit/rollback → Evidence to validate.**

## Language notes (verify currency)
C#/.NET: productive, strong tooling, good performance, cross-platform. PHP: pragmatic hosting and CMS ecosystems with capable modern frameworks. Ruby: productivity for product-centric web apps. Rust: safety and performance for latency-critical parts, steeper learning curve. Java/Kotlin: mature enterprise ecosystem, heavier footprint. Elixir/Erlang: massive concurrency and fault tolerance.

## Selection criteria
Team skill, hiring pool, ecosystem for the domain, operational familiarity, hosting constraints, performance need, security track record, licensing, long-term maintenance, exit cost. Record decisions with `references/technical-decision-records.md` or `templates/TECHNOLOGY_RECOMMENDATION_RECORD.md`.

## See also
`references/api-style-selection-guide.md`, `references/deployment-topology-options.md`, `orchestrator/PROJECT_ROUTING.md`.
