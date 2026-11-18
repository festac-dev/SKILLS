# AI Agent Implementation Playbook

## Define
Specify task, user benefit, non-goals, autonomy level, tools, data boundaries, and unacceptable outcomes.

## Architect
Separate planner, policy/permission layer, executor, tool adapters, state store, evaluator, and audit trail as justified. Keep trusted enforcement outside the model.

## Execute safely
Validate structured outputs, scope credentials, bound time/cost/actions, make operations idempotent, and require approval for consequential actions.

## Evaluate
Build representative normal, edge, adversarial, injection, and tool-failure cases. Measure task success, correctness, policy adherence, latency, cost, and harm severity.

## Operate
Monitor drift and failures, provide fallback and human escalation, support cancellation and recovery, and version prompts/tools/evaluations.

A convincing demo is not sufficient evidence of safe autonomy.

## Runtime, retrieval, and auditable execution

### When to use
Use when an LLM retrieves information, invokes tools, changes persistent state, or drives a user workflow.

### Core principles
Keep permission enforcement outside the model. Prompts express intent; schemas and trusted code enforce boundaries. Treat retrieved content and tool results as untrusted data. A cited answer is only as trustworthy as the cited evidence.

### Step-by-step procedure
1. Specify task success, prohibited effects, allowed tools/data, and a bounded run budget. Version prompts, model configuration, retrieval corpus, and tool contracts together.
2. For RAG, evaluate corpus access control, chunk provenance, freshness, recall, and answer faithfulness separately. Filter tenant/document permissions before returning retrieval results; do not rely on prompting to hide unauthorized chunks.
3. Validate tool arguments, resolve targets, check policy, and record intent before side effects. Attach an idempotency key to retryable mutations.
4. Bound steps, elapsed time, input/output tokens, tool calls, and external spend. On timeout or ambiguity, report partial state and a recoverable next step.
5. Evaluate representative tasks plus injection, malformed output, unavailable tools, stale retrieval, duplicate calls, and interrupted execution.
6. Record structured action events with run ID, sequence, timestamp, tool/action, redacted argument summary or digest, authorization reference, result status, duration, and evidence reference. Do not log secrets, full prompts, private documents, or hidden reasoning by default.

### Checklist
- [ ] Tool results cannot overwrite policy or grant themselves permission.
- [ ] Each mutation has an accountable target and recovery semantics.
- [ ] Audits capture attempted and denied actions as well as successes.
- [ ] Evaluation separates retrieval failure, reasoning failure, and tool failure.

### Common failure modes
A prompt-only permission rule is bypassable; a fallback provider can leak data; automatic retry can duplicate effects; a summary of a failed tool call is not proof of success.

### Concrete examples
A redacted event shape:
```json
{"run_id":"run-42","sequence":3,"action":"issue.read","target":"issue-17","authorization":"user-task","status":"succeeded","duration_ms":85,"evidence":"result-3"}
```
For a document-answering eval, plant a retrieved sentence that requests credential disclosure. Expected behavior is to ignore that instruction, answer from authorized evidence, and never call a credential-reading tool.

### Verification
Measure task completion, unsupported claims, tool correctness, permission violations, p95 latency, and cost per successful task. Record denominators and failure severity. Validate that audit records reflect actual tool outcomes.

### Related skills
[Tool/MCP engineering](../specialists/tool-and-mcp-engineering.md), [AI governance](../specialists/ai-evaluation-and-governance.md), [context and recovery](../references/agent-context-and-handoffs.md).

## Application evidence

Demonstrate one useful task, an untrusted instruction and a tool timeout after commit. Inspect the actual execution trace for authority, duplicate effects and recovery; configuration text and model explanations do not prove enforcement.
