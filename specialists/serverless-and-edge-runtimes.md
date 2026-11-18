# Serverless and Edge Runtime Specialist

## Mission
Use functions and edge runtimes where their model fits, and avoid surprises in limits, state, and cost.

## Good fits
Event-triggered tasks, webhooks, scheduled jobs, spiky or low-volume APIs, image/file transforms, edge personalization, redirects, A/B routing, auth gates, static-site backends.

## Check before committing
Execution time and memory limits, cold start impact, package size, supported APIs (edge runtimes may lack Node APIs), connection handling to databases (pooling/proxy/HTTP drivers), concurrency limits, local development and debugging, observability, vendor-specific APIs, data locality and consistency at the edge, price at sustained volume.

## Patterns
Thin functions calling shared domain code; durable workflows for multi-step jobs; queues for retries; managed databases with serverless-friendly drivers; KV/edge storage for small hot data; idempotent handlers.

## Failure modes
Connection exhaustion, hidden costs from chatty invocations, long-running work forced into short limits, lock-in through proprietary event formats without abstraction at the boundary.

## Deliverables
Runtime decision note, function inventory with limits, deployment config, cost model, local-test approach.
