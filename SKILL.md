---
name: professional-product-creation
description: Build, improve, and verify products that need coordinated design, application engineering, or operating work. Use the relevant route for focused changes, and the orchestrator for substantial builds or upgrades.
---

# Professional Product Creation

Deliver the user’s requested product behavior in the existing project, with evidence from the actual implementation. This library supplies domain guidance; its breadth does not make every capability part of the task.

## Start from the brief

Inspect the project’s instructions, runtime, working changes, assets and relevant implementation. Preserve the original objective and incorporate the latest user corrections. If recovering interrupted work, reconcile [checkpoint evidence](references/agent-context-and-handoffs.md) with current files and processes before retrying operations.

For a substantial build, use [the orchestrator](orchestrator/MASTER_ORCHESTRATOR_PROMPT.md). For a focused change, select [a route](orchestrator/PROJECT_ROUTING.md) and read only its needed resources. The [catalogue](CATALOG.md) and `python scripts/toolkit.py search 'subject'` cover less common domains.

## Imported collections

The user-requested [GitHub collections](COLLECTIONS.md) are stored directly under this SKILLS directory in separate folders. Find their skills with `python3 scripts/skill_collections.py search 'task'`, then read the returned path directly. Do not route these collections through core capability owners. Follow [collection rules](COLLECTION_RULES.md) to reconcile source workflow preferences with current user scope and authorization.

## Apply the right guidance

- **Visual references:** use [reference analysis](references/visual-reference-analysis.md) for supplied videos, carousels, websites or collections; transfer principles without treating sample claims as product facts.
- **Identity, templates or UI redesign:** use [brand](specialists/brand-and-art-direction.md), [design systems](specialists/design-systems-and-ui.md) and [UX](specialists/ux-and-information-architecture.md). Implement an authorized direction; when sibling products need distinct templates, differentiate composition and task hierarchy while preserving functional journeys.
- **Moving graphics:** use [Motion Studio](motion-studio/SKILL.md), then [spatial runtime guidance](specialists/motion-3d-and-immersive.md) for advanced geometry. Translate the requested movement and control behavior into visible acceptance criteria; for advanced scenes, coordinate a readable sequence and inspect its phases, loop and fallback.
- **Demo videos:** use [Motion Studio](motion-studio/SKILL.md) and [product evidence guidance](specialists/product-demo-video-production.md) for truthful capture, narration, editorial timing and export QA. Sample prompts supply optional techniques; the current brief selects style, tools and deliverables.
- **Backend and operations:** use the [backend delivery playbook](playbooks/BACKEND_DELIVERY_PLAYBOOK.md) for a complete service journey; load database, API, identity, queue, realtime, server and recovery guidance only where required.
- **Working features:** follow the existing server/data contracts and verify one complete input-to-result path before broadening the implementation.
- **Documentation:** use [technical documentation](specialists/technical-documentation.md#documentation-audience-and-evidence) for READMEs, setup/operator guides, API examples and verification summaries. Match the reader's task and the project's actual behavior; keep private delivery notes outside published content and preserve required disclosures.
- **Cleanup and Git handoff:** use [repository hygiene](references/repository-hygiene-and-ai-artifact-policy.md). Keep development prompts, transcripts, caches, render intermediates and unrelated working files out of Git; inspect tracked files as well as ignore rules. Keep runtime state and final deliverables separate from removable caches.
- **Library upgrades:** use [lifecycle guidance](references/skill-lifecycle-and-improvement.md) and [skill evaluation](playbooks/SKILL_EVALUATION_PLAYBOOK.md). Review coverage, correct demonstrated gaps and preserve useful topic ownership.

## Verify and deliver

Use [engineering judgment](orchestrator/ENGINEERING_JUDGMENT_AND_EVIDENCE.md) to select checks proportional to the change. Test populated journeys, meaningful failures and resulting artifacts where applicable. Distinguish a build, a fixture-backed browser check and a real-provider check. Report passed, failed, unverified and not-applicable results accurately through the [gate protocol](quality-gates/GATE_PROTOCOL.md).

Before handing over a local preview, probe the running artifact and current links. Keep the final report concise: outcome, important changes, observed checks and practical limitations.

For questions about whether an integration or account feature is enabled, use the configuration layers in [engineering evidence](orchestrator/ENGINEERING_JUDGMENT_AND_EVIDENCE.md#configuration-and-external-account-state). Building an integration, configuring it, enabling a provider setting and observing a live result establish different facts.

## Boundaries

Preserve the user’s stack, scope, assets and existing work. Explicitly requested identity and motion are requirements, while unrelated catalogue features remain optional. Use authorization already supplied; these documents do not grant new external-action permissions or require repeated approval for routine local work.

Specialist briefs are viewpoints, not instructions to spawn agents. Follow the environment’s delegation rules. Keep secrets, private transcripts and irrelevant assistant narration out of product files. Preserve required notices and attribution. Claims of readiness, compliance, performance or model quality require evidence within the stated scope.
