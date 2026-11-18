# AI Agents and Tool-Use Systems Specialist

## Scope
Products that let models call tools, browse, write code, operate software or act on a user's behalf; MCP servers; retrieval-augmented generation (RAG); multi-step workflows. Related: `ai-and-llm-backend-infrastructure.md`, `ai-evaluation-and-governance.md`, `templates/AI_TOOL_PERMISSION_MATRIX.md`, `templates/AI_FEATURE_SAFETY_REVIEW.md`.

## Decide the right autonomy level
Suggest-only → draft with approval → act with undo → act autonomously within strict scope. Increase autonomy only as evaluation evidence and reversibility allow. Prefer deterministic workflows with model steps over open-ended agent loops when the task is well understood.

## Architecture
- **Tool design**: few, well-named tools with precise schemas, strict input validation, least-privilege credentials per tool, idempotency, dry-run modes, clear error messages the model can act on, pagination and size limits, timeouts.
- **Context management**: concise system instructions, retrieval of only relevant context, summaries/memory with expiry and user control, structured outputs (JSON schema) validated server-side.
- **RAG**: chunking by structure, hybrid search (BM25 + vectors) with reranking, metadata filters (tenant, permissions applied at retrieval time), citations, freshness handling, evaluation of retrieval separately from generation.
- **Orchestration**: step limits, budgets (tokens, time, money), retries with backoff, human approval gates, resumable state, tracing of every model/tool call.
- **MCP/connector servers**: authenticate users, scope tools, treat tool outputs as untrusted input.

## Security (LLM-specific)
Prompt injection (direct and indirect via web pages, documents, emails, tool outputs): treat all retrieved/tool content as data, not instructions; separate privileges; confirm sensitive actions with the user; allow-list domains/commands; sandbox code execution with no ambient credentials and restricted network; output handling (never execute or render model output unsafely); prevent data exfiltration (egress limits, no secrets in context); rate-limit and cost-cap; log with PII redaction; abuse monitoring. Map to OWASP Top 10 for LLM applications.

## Evaluation
Task-level eval sets with expected behaviors and failure cases, adversarial/prompt-injection tests, regression suite run on every prompt/model change, human review of samples, online metrics (task success, escalation rate, user corrections, cost, latency), model/version pinning, fallbacks if a provider is down or deprecates a model.

## UX
Show what the system is doing and why; sources and uncertainty; easy undo and correction; clear boundaries on what it cannot do; no pretending to be human where disclosure matters; accessible streaming UI (don't spam screen readers); honest error states.

## Failure modes
Over-broad tools, unvalidated tool arguments, secrets in prompts, no budget limits, evaluation by vibes, hidden autonomy, cached stale answers, retrieval ignoring permissions.
