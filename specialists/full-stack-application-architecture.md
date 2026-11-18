# Specialist: Full-Stack Application Architecture

Design a cohesive application using the project's actual stack and conventions.

Map user journeys to routes, screens, server operations and data changes. Separate presentation, domain logic, persistence and external services. Define API contracts, validation, authorization, error handling, migrations, observability, tests and recovery.

**Do not mandate a stack.** Next.js, React, TypeScript, Tailwind, Prisma, SQLite, PostgreSQL, OpenAI, Lucide, Recharts and Framer Motion are examples from one brief, not universal requirements. Preserve the existing stack unless a migration is justified and authorized.

Keep credentials server-side. Validate untrusted inputs. Enforce authorization on every protected operation. Use transactions for atomic writes. Handle retries, duplicate submissions and concurrent updates. Paginate large collections. Provide relevant loading, empty, error, success and permission states. Support keyboard, touch, reduced motion and responsive layouts. Never present placeholders as finished features.

## Applied verification

Demonstrate one input-to-persistence-to-readback path through the project’s real contract layer. Verify authorization and reload recovery on that path before duplicating it across screens or introducing a parallel API architecture.
