# Gap Analysis and Merge Map

Historical merge record. See [the current upgrade verification](UPGRADE_VERIFICATION.md) for this revision.

The initial assessment grouped subtopics exactly as the user's topic groups: 64 groups, 18 MISSING (28.1%), 38 PARTIAL, 8 COVERED. The user's rule permitted continuing without a go confirmation. Status describes the pre-merge state; links identify the existing or newly added owner. Covered topics were reused; a file may be extended for a different partial topic without rewriting its covered content.

| Topic | Initial status | Target file |
|---|---|---|
| A Testing, properties, flakes | PARTIAL | [specialists/quality-engineering-and-test-strategy.md](../specialists/quality-engineering-and-test-strategy.md) |
| A Debugging and incident triage | PARTIAL | [playbooks/INCIDENT_RESPONSE_PLAYBOOK.md](../playbooks/INCIDENT_RESPONSE_PLAYBOOK.md) |
| A Code review and refactoring | PARTIAL | [specialists/technical-debt-and-modernization.md](../specialists/technical-debt-and-modernization.md) |
| A Git, PRs, semver, releases | PARTIAL | [references/release-and-change-management.md](../references/release-and-change-management.md) |
| A Frontend fundamentals | PARTIAL | [specialists/frontend-engineering.md](../specialists/frontend-engineering.md) |
| A Profiling and load testing | PARTIAL | [playbooks/PERFORMANCE_INVESTIGATION_PLAYBOOK.md](../playbooks/PERFORMANCE_INVESTIGATION_PLAYBOOK.md) |
| A README, ADRs, runbooks | COVERED | [specialists/technical-documentation.md](../specialists/technical-documentation.md) |
| B LLMs, RAG, agents, evals | PARTIAL | [playbooks/AI_AGENT_IMPLEMENTATION_PLAYBOOK.md](../playbooks/AI_AGENT_IMPLEMENTATION_PLAYBOOK.md) |
| B Prompt-injection defense | PARTIAL | [specialists/ai-evaluation-and-governance.md](../specialists/ai-evaluation-and-governance.md) |
| B Tool/MCP engineering | MISSING | [specialists/tool-and-mcp-engineering.md](../specialists/tool-and-mcp-engineering.md) |
| B Multi-agent coordination | MISSING | [specialists/multi-agent-coordination.md](../specialists/multi-agent-coordination.md) |
| B Context engineering | MISSING | [references/agent-context-and-handoffs.md](../references/agent-context-and-handoffs.md) |
| B Skill routing | PARTIAL | [orchestrator/PROJECT_ROUTING.md](../orchestrator/PROJECT_ROUTING.md) |
| B Skills evaluation harness | MISSING | [playbooks/SKILL_EVALUATION_PLAYBOOK.md](../playbooks/SKILL_EVALUATION_PLAYBOOK.md) |
| C Data and ML pipelines | PARTIAL | [specialists/data-platform-and-pipelines.md](../specialists/data-platform-and-pipelines.md) |
| C Search and reindexing | PARTIAL | [specialists/search-relevance-and-recommendations.md](../specialists/search-relevance-and-recommendations.md) |
| C Distributed systems | PARTIAL | [specialists/edge-and-distributed-systems.md](../specialists/edge-and-distributed-systems.md) |
| C SRE | PARTIAL | [references/reliability-engineering-patterns.md](../references/reliability-engineering-patterns.md) |
| C Kubernetes and cloud | PARTIAL | [specialists/devops-and-release.md](../specialists/devops-and-release.md) |
| C Systems languages, FFI, WASM | MISSING | [specialists/systems-languages-and-interop.md](../specialists/systems-languages-and-interop.md) |
| C Mobile engineering | PARTIAL | [specialists/mobile-and-device-experiences.md](../specialists/mobile-and-device-experiences.md) |
| D Supply-chain protection | PARTIAL | [specialists/supply-chain-and-build-security.md](../specialists/supply-chain-and-build-security.md) |
| D STRIDE and attack trees | PARTIAL | [specialists/security-architecture-and-red-teaming.md](../specialists/security-architecture-and-red-teaming.md) |
| D OWASP and ASVS | PARTIAL | [references/security-control-catalogue.md](../references/security-control-catalogue.md) |
| D Pentest procedure | PARTIAL | [specialists/security-architecture-and-red-teaming.md](../specialists/security-architecture-and-red-teaming.md) |
| D Secrets rotation | PARTIAL | [specialists/identity-and-access-management.md](../specialists/identity-and-access-management.md) |
| D GDPR, SOC 2, PII, retention | PARTIAL | [specialists/data-governance-and-compliance.md](../specialists/data-governance-and-compliance.md) |
| E Payments and billing | COVERED | [specialists/billing-and-entitlements.md](../specialists/billing-and-entitlements.md) |
| E EVM transaction safety | MISSING | [specialists/evm-transaction-engineering.md](../specialists/evm-transaction-engineering.md) |
| E Solidity and Foundry | MISSING | [specialists/solidity-contract-engineering.md](../specialists/solidity-contract-engineering.md) |
| E NEAR and cross-chain | MISSING | [specialists/near-and-cross-chain-engineering.md](../specialists/near-and-cross-chain-engineering.md) |
| E Browser/desktop automation | MISSING | [specialists/browser-and-desktop-automation.md](../specialists/browser-and-desktop-automation.md) |
| E Wine, Proton, Box64, DXVK | MISSING | [specialists/compatibility-runtime-engineering.md](../specialists/compatibility-runtime-engineering.md) |
| E Design systems and graphics | PARTIAL | [specialists/motion-3d-and-immersive.md](../specialists/motion-3d-and-immersive.md) |
| E Product, events, experiments | COVERED | [specialists/product-strategy.md](../specialists/product-strategy.md) |
| F Termux, offline, low RAM, patches | MISSING | [references/termux-and-constrained-environments.md](../references/termux-and-constrained-environments.md) |
| G Hackathon delivery | MISSING | [playbooks/HACKATHON_DELIVERY_PLAYBOOK.md](../playbooks/HACKATHON_DELIVERY_PLAYBOOK.md) |
| H Plan-execute-verify | COVERED | [orchestrator/MASTER_ORCHESTRATOR_PROMPT.md](../orchestrator/MASTER_ORCHESTRATOR_PROMPT.md) |
| H Repository reconnaissance | COVERED | [playbooks/EXISTING_REPOSITORY_AUDIT_PLAYBOOK.md](../playbooks/EXISTING_REPOSITORY_AUDIT_PLAYBOOK.md) |
| H Self-review and production failures | PARTIAL | [orchestrator/ENGINEERING_JUDGMENT_AND_EVIDENCE.md](../orchestrator/ENGINEERING_JUDGMENT_AND_EVIDENCE.md) |
| H Verify APIs, flags, versions | PARTIAL | [orchestrator/TECHNOLOGY_SELECTION.md](../orchestrator/TECHNOLOGY_SELECTION.md) |
| H Blast radius and authorization | PARTIAL | [orchestrator/MASTER_ORCHESTRATOR_PROMPT.md](../orchestrator/MASTER_ORCHESTRATOR_PROMPT.md) |
| H Reversibility | PARTIAL | [references/release-and-change-management.md](../references/release-and-change-management.md) |
| H Root-cause discipline | PARTIAL | [playbooks/INCIDENT_RESPONSE_PLAYBOOK.md](../playbooks/INCIDENT_RESPONSE_PLAYBOOK.md) |
| H Agent failure patterns | PARTIAL | [quality-gates/ANTI-BLOAT-AND-ANTI-GENERIC-AI.md](../quality-gates/ANTI-BLOAT-AND-ANTI-GENERIC-AI.md) |
| H Cost, latency, token budgets | PARTIAL | [specialists/cost-and-capacity-engineering.md](../specialists/cost-and-capacity-engineering.md) |
| H Build-versus-buy and judgment | PARTIAL | [orchestrator/TECHNOLOGY_SELECTION.md](../orchestrator/TECHNOLOGY_SELECTION.md) |
| I Evidence-based skill improvement | MISSING | [references/skill-lifecycle-and-improvement.md](../references/skill-lifecycle-and-improvement.md) |
| I Resumable long-horizon work | MISSING | [references/agent-context-and-handoffs.md](../references/agent-context-and-handoffs.md) |
| I Formal methods | MISSING | [specialists/formal-methods-and-invariants.md](../specialists/formal-methods-and-invariants.md) |
| I Differential/metamorphic testing | MISSING | [references/differential-and-metamorphic-testing.md](../references/differential-and-metamorphic-testing.md) |
| I Simulation, faults, replay | PARTIAL | [specialists/game-and-interactive-systems.md](../specialists/game-and-interactive-systems.md) |
| I Autonomous security review | PARTIAL | [specialists/security-architecture-and-red-teaming.md](../specialists/security-architecture-and-red-teaming.md) |
| I Adversarial self-review | PARTIAL | [orchestrator/ENGINEERING_JUDGMENT_AND_EVIDENCE.md](../orchestrator/ENGINEERING_JUDGMENT_AND_EVIDENCE.md) |
| I Calibrated uncertainty | COVERED | [orchestrator/ENGINEERING_JUDGMENT_AND_EVIDENCE.md](../orchestrator/ENGINEERING_JUDGMENT_AND_EVIDENCE.md) |
| I Cross-repo analysis and codemods | MISSING | [specialists/monorepo-and-cross-repo-engineering.md](../specialists/monorepo-and-cross-repo-engineering.md) |
| I Legacy migrations | PARTIAL | [specialists/migration-and-compatibility.md](../specialists/migration-and-compatibility.md) |
| I Unit economics and cost of delay | PARTIAL | [specialists/financial-planning-and-unit-economics.md](../specialists/financial-planning-and-unit-economics.md) |
| J Skill standards and lifecycle | MISSING | [references/skill-lifecycle-and-improvement.md](../references/skill-lifecycle-and-improvement.md) |
| J Human factors | PARTIAL | [orchestrator/MASTER_ORCHESTRATOR_PROMPT.md](../orchestrator/MASTER_ORCHESTRATOR_PROMPT.md) |
| J Ethics, licensing, privacy | PARTIAL | [specialists/legal-policy-and-regulatory-coordination.md](../specialists/legal-policy-and-regulatory-coordination.md) |
| J Accessibility and i18n | COVERED | [specialists/accessibility-and-internationalization.md](../specialists/accessibility-and-internationalization.md) |
| J Quality gates and done criteria | COVERED | [quality-gates/DEFINITION_OF_DONE.md](../quality-gates/DEFINITION_OF_DONE.md) |
| J Auditable agent actions | PARTIAL | [playbooks/AI_AGENT_IMPLEMENTATION_PLAYBOOK.md](../playbooks/AI_AGENT_IMPLEMENTATION_PLAYBOOK.md) |

## Earlier requirements retained

| Requirement | Initial coverage | Merged owner |
|---|---|---|
| Backend, APIs, auth, databases, queues, realtime | PARTIAL | [Backend](../specialists/backend-and-data-engineering.md), existing identity/distributed/realtime resources |
| Cloud, VPS, Linux, Docker, networks, CI/IaC, observability | PARTIAL | [DevOps](../specialists/devops-and-release.md), existing reliability and backup resources |
| Screens, inputs, zoom, orientation, specialized displays | PARTIAL | [Platform matrix](../references/platform-compatibility-matrix.md), existing mobile/frontend/screen inventory and UX gate |
| CLI/TUI, registries, terminal compatibility | MISSING | [CLI/TUI](../specialists/cli-and-tui-engineering.md) |
| Repository hygiene and AI residue | PARTIAL | [Repository audit](../playbooks/EXISTING_REPOSITORY_AUDIT_PLAYBOOK.md), [optional ignore template](../templates/REPOSITORY_HYGIENE.gitignore) |
| Animated graphics | PARTIAL | [Motion and graphics](../specialists/motion-3d-and-immersive.md) |

## Remaining limits

All requested topic groups now have an owning resource and practical guidance; this is not a claim that every platform or procedure has been executed. Device/terminal integration, cloud deployments, formal model checking, blockchain toolchains, and live model-based skill evaluations require their actual environments. Version-sensitive examples instruct installed-version inspection. No claim of model superiority or universal future completeness is made. See [verification](VERIFICATION.md).
