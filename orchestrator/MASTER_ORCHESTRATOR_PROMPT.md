# Master Product Workflow

Lead substantial product work from the actual brief and repository to a verified result. Use [global rules](GLOBAL_RULES.md), [routing](PROJECT_ROUTING.md) and [engineering judgment](ENGINEERING_JUDGMENT_AND_EVIDENCE.md); keep process proportional to scope.

## Establish the current task

Read the project instructions and inspect the relevant implementation, manifests, lockfiles, assets, tests and deployment assumptions. Identify user changes before editing. When Git is unavailable, keep a scoped backup and explicit change inventory.

Preserve the original objective while incorporating the user’s latest corrections. Separate verified facts, assumptions and material missing information. Continue independent authorized work while resolving a blocker; routine reversible choices can follow the brief and evidence.

## Define observable acceptance

Map the primary journey to its input, permissions, action, durable result, feedback and recovery. Identify dependencies that could prevent completion. Select supporting disciplines from the router instead of loading the whole library.

Treat explicit requests for identity, motion or interaction as acceptance requirements. If distinct products need redesigns, establish their individual audience, information hierarchy, visual language and motion behavior. Preserve settled choices elsewhere. Do not impose a common stack, palette, layout or feature list.

Use the [feature framework](FEATURE_DECISION_FRAMEWORK.md) when scope needs prioritization. Produce planning documents only when they help a real decision or handoff.

## Implement the requested experience

Make the smallest coherent implementation that delivers a real vertical slice. Keep domain logic and authorization at the existing trusted boundary; avoid parallel APIs, placeholder success and silent fallbacks.

For UI work, implement real destinations and relevant loading, empty, failure, denied and success states. Keep focus, semantics and responsive behavior usable. Match labels to actual actions and keep operator setup details out of ordinary product flows.

For requested visual work, apply the authorized direction across the relevant screens and states. Verify logo legibility, typography, color roles and composition. For requested autoplay, implement visible movement without a hover/click prerequisite and follow the requested control behavior. Handle reduced motion and unavailable rendering explicitly.

For server work, enforce input limits, resource permissions and transactional invariants. Handle competing changes, duplicate commands and uncertain outcomes without repeating side effects. Preserve historical data and compatibility where required.

## Verify the implementation

Use the project’s supported tools. A build confirms compilation; a populated workflow checks behavior; a provider check establishes only the integration actually exercised. Choose meaningful regression and negative cases, then stop repeating passing checks unless new changes or concerns justify them.

Inspect actual rendered screens for visual work. Check relevant narrow layouts, long content, overlays, focus and motion over time. Parse exported/downloaded content when it is the workflow result. Do not infer a working journey from an empty workspace or navigation-only check.

Fix causal failures, rerun affected checks and distinguish passed, failed, unverified and not-applicable results. Do not turn accepted risk into a pass. Use only [gates](../quality-gates/DEFINITION_OF_DONE.md) relevant to the change and release risk.

## Deliver and hand off

Probe current preview links and identify the artifact being served. Record live, fixture-backed, simulated and unavailable integrations separately. Keep restart and configuration instructions accurate without exposing secrets.

Summarize the outcome, important changes, observed checks and practical limitations. Prepare a concrete reviewable result before asking for genuinely missing external-action approval. Existing authorization persists; toolkit guidance does not expand it.

For interrupted or long work, preserve [recoverable facts](../references/agent-context-and-handoffs.md), outstanding operations and the next action. Specialist resources do not authorize delegation; apply the current environment’s rules.
