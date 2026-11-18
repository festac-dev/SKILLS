# Language and Framework Profiles (backend and general)

Use to *recommend*, never to impose. Existing project language wins unless a measured problem justifies change. Versions and ecosystem health move; mark claims "verify current".

## How to choose
Team skill and hiring pool > ecosystem fit for the problem > runtime characteristics > fashion. A team shipping in a language it knows beats a "better" language it does not.

## Profiles
| Language | Strong fit | Watch out for | Common stacks |
|---|---|---|---|
| **TypeScript / Node.js (also Bun, Deno)** | Full-stack teams sharing types, I/O-bound APIs, real-time (WebSocket), BFFs, serverless | CPU-bound work blocks the event loop (use workers/queues); dependency sprawl and supply-chain risk; unhandled promise rejections; type-safety ends at the network boundary (validate with a schema library) | Express, Fastify, Hono, NestJS; Next.js/Remix/SvelteKit server routes; Prisma, Drizzle, Kysely |
| **Python** | Data/ML/AI products, scripting, rapid APIs, admin-heavy apps, scientific work | GIL limits CPU parallelism (use processes, native extensions or queues); packaging/env discipline; async/sync mixing; type hints are optional (use mypy/pyright) | Django (batteries, admin, ORM), FastAPI (typed async APIs), Flask, Celery/RQ/Dramatiq; SQLAlchemy, Alembic |
| **Go** | Network services, CLIs, infrastructure tools, high-concurrency APIs, small static binaries | Verbose error handling; less expressive domain modeling; generics are newer; ORMs less central (sqlc, pgx, ent) | net/http, chi, gin, echo; cobra; Bubble Tea for TUIs |
| **Rust** | Performance- and safety-critical components, WASM, CLI tools, embedded, parsers, proxies | Steeper learning curve; slower iteration for CRUD; async ecosystem choices | axum, actix-web, tokio, sqlx, diesel; tauri |
| **Java / Kotlin (JVM)** | Large enterprise systems, mature ecosystem, strong typing, long-lived teams, Android (Kotlin) | Startup/memory (mitigate with GraalVM native or CRaC where appropriate); framework magic; configuration weight | Spring Boot, Quarkus, Micronaut, Ktor; Hibernate, jOOQ, Flyway/Liquibase |
| **C# / .NET** | Enterprise and Windows-adjacent shops, high-performance APIs, game dev (Unity), desktop | Ecosystem assumptions around Microsoft tooling (though cross-platform) | ASP.NET Core minimal APIs/MVC, Entity Framework, Dapper; Blazor, MAUI |
| **PHP** | Content sites, e-commerce, mature hosting everywhere, rapid CRUD | Legacy patterns in older code; strict typing and static analysis must be adopted deliberately | Laravel, Symfony, WordPress (as CMS), Filament |
| **Ruby** | Product-led CRUD apps, startups, convention-over-configuration speed | Throughput per core; scaling discipline needed; shrinking but loyal talent pool | Rails (Hotwire), Sidekiq, Sinatra |
| **Elixir / Erlang** | Real-time, presence, chat, fault-tolerant soft-real-time systems, IoT backends | Smaller hiring pool; different mental model (OTP) | Phoenix (LiveView), Oban, Broadway |
| **Swift / Kotlin / Dart** | Native or cross-platform mobile clients; Swift and Kotlin also server-side | Platform release cadence, store review | SwiftUI, Jetpack Compose, Flutter |
| **C / C++** | Engines, drivers, codecs, embedded, high-performance libraries | Memory safety; build complexity | CMake, vcpkg/conan |
| **SQL** | The database is part of your language set: constraints, views, windows, CTEs, RLS | Treating the DB as a dumb store | PostgreSQL, MySQL/MariaDB, SQLite, SQL Server |

## Framework style choices
- **Batteries-included (Django, Rails, Laravel, Spring, ASP.NET)**: fastest for conventional CRUD/admin/auth products; consistent structure; larger surface to learn.
- **Micro/minimal (Express, Fastify, Hono, Flask, FastAPI, Gin, axum)**: freedom and low overhead; you must assemble validation, auth, migrations, jobs and structure deliberately.
- **Full-stack meta-frameworks (Next.js, Remix/React Router, SvelteKit, Nuxt, Astro)**: one deploy unit for UI plus server routes; great for product sites and apps; check lock-in to a hosting platform and cache semantics.
- **Serverless functions**: spiky/low traffic, event glue; watch cold starts, connection limits (use pooling/proxy), vendor-specific runtimes and local-dev parity.
- **Modular monolith**: default recommendation for most new products; extract services only for a named reason (independent scaling, team boundaries, different runtime, blast-radius isolation).

## Recommendation heuristics
- Greenfield CRUD + admin, small team → Django, Rails, Laravel or a TypeScript full-stack framework with a typed ORM, PostgreSQL, a managed queue or a Postgres-backed job runner.
- Real-time collaborative or chat → Node/TypeScript or Elixir for the socket tier; Postgres for state; Redis/NATS for fan-out if scaling beyond one node; CRDT/OT library if concurrent editing.
- Data/AI-heavy → Python services around the model/data tooling; keep the public API thin and typed; isolate long jobs in workers.
- Infra tools, agents, CLIs → Go or Rust for single static binaries; TypeScript where plugin ecosystems matter.
- Hard latency/throughput budgets or memory-safety needs → Rust/Go/JVM/.NET after profiling shows the bottleneck.
- Content-heavy marketing/docs → static or hybrid rendering (Astro, Next.js, Eleventy, Hugo) with a headless CMS only if editors need it.

## Anti-patterns
Choosing by benchmark headlines; polyglot sprawl for a 3-person team; rewriting to chase a framework; ORM everywhere with no SQL fluency; no schema validation at boundaries; ignoring the language's concurrency model.

## Evidence to collect
Language/runtime versions and EOL dates, framework release support windows, dependency audit results, build/test times, p95 latency under realistic load.
