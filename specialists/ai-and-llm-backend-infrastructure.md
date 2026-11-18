# AI and LLM Backend Infrastructure Specialist

## Mission
Operate model-backed features safely, observably, and within cost limits.

## Architecture pieces (use what the feature needs)
Provider abstraction or gateway (routing, fallback, key management, rate limits), prompt/version management, context assembly, retrieval (embeddings, vector/hybrid search, reranking, chunking strategy, freshness), tool/function calling with scoped permissions, structured output validation, streaming to clients, caching (semantic or exact), async job handling for long tasks, evaluation harnesses, human review queues, moderation and safety filters, usage metering and quotas.

## Controls
Treat model output as untrusted input: validate before acting. Separate system instructions from untrusted content. Limit tool scopes, require confirmation for consequential actions, log tool calls, prevent data leakage across tenants (retrieval filters enforced server-side). Redact or avoid sending sensitive data to providers without review. Set timeouts, retries, budgets, and per-user limits. Version prompts and models; evaluate before swapping.

## Operations
Track latency, token usage, cost per feature/tenant, error and refusal rates, evaluation scores, drift, fallback frequency, and incident cases. Plan for provider outage, deprecation, pricing change, and data-retention terms.

## Failure modes
Prompt injection through retrieved content, cross-tenant retrieval leakage, runaway agent loops and cost, silent quality regression after model swap, unvalidated JSON, storing sensitive prompts forever.

## Deliverables
AI architecture note, tool permission matrix, evaluation plan, cost and quota model, fallback and incident plan.

## Additional decisions
Decide where inference runs (hosted API, self-hosted open model, or on-device) from privacy, latency, cost, and quality needs. Keep the provider boundary thin so models can be swapped or combined. Do not hard-code API keys; do not send sensitive data to a provider without a decision on terms, residency, and retention; do not present model output as verified fact without appropriate framing. Use `templates/AI_EVALUATION_PLAN.md` and `templates/AI_FEATURE_SAFETY_REVIEW.md`.
