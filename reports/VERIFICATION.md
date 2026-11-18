# Merge Verification and Change Inventory

Historical merge record. See [the current upgrade verification](UPGRADE_VERIFICATION.md) for this revision.

Directory-only delivery completed on 2026-11-06 UTC. No ZIP, commit, deployment, external message, or package installation was performed.

## Result

- 184 maintained source files: 34 added, 35 original files extended, 115 original files untouched.
- All 150 original file prefixes are preserved byte-for-byte against [the merge baseline](MERGE_BASELINE.json); no original file was removed.
- 39 task routes include trigger keywords, ordered resources, skip rules, overlap ownership, and applicable gates. Every source is reachable through [the catalogue](../CATALOG.md).
- 23 new guidance resources each have three behavioral cases: 69 total. These cases are defined but **not executed** by a live agent.
- The machine-counted initial gap table is 18 MISSING (28.1%), 38 PARTIAL, and 8 COVERED across 64 groups. An earlier progress-message arithmetic total of 19/37 was corrected; the continuation decision remains unchanged.

## Checks executed

| Check | Observed result | Limit |
|---|---|---|
| `python scripts/toolkit.py validate` | Passed source naming, headings, local links, entrypoint reachability, routes, eval coverage, and original-content preservation | Static validation; external URLs and semantic correctness are not proved |
| Skill creator `quick_validate.py` on this directory | Passed root skill metadata validation | Does not evaluate live agent behavior |
| `python -m unittest discover -s tests -v` | 11 tests passed | Tests the maintenance helper, not all product frameworks |
| Python AST parsing | Both new Python files parsed successfully | Runtime behavior covered separately by the helper tests |
| Embedded Python examples | 4 examples executed successfully: conditional stock update, deterministic replay, JSON normalization, terminal capability detection | These are bounded local examples, not production integration evidence |
| Extension structure review | All extended resources contain the eight requested procedure sections | Original content and headings retained |
| Five routing dry-runs | All selected the expected primary route and existing ordered resources | Deterministic keyword simulation, not semantic model evaluation |
| Manual overlap/example review | Consolidated the duplicate session-added decision template; removed a placeholder path; improved the formal model example | Semantic review cannot guarantee no future overlap |

Regression checks exercise broken links, traversal targets, original-content loss, duplicate headings, missing evaluations, symlinks, code-fence handling, environment supplements, and ordinary use of “near.”

## Five routing dry-runs

| Task | Resources in load order | Gates |
|---|---|---|
| Build a keyboard-driven TUI on Termux with no mouse. | [termux-and-constrained-environments.md](../references/termux-and-constrained-environments.md) → [cli-and-tui-engineering.md](../specialists/cli-and-tui-engineering.md) → [platform-compatibility-matrix.md](../references/platform-compatibility-matrix.md) → [quality-engineering-and-test-strategy.md](../specialists/quality-engineering-and-test-strategy.md) | [USER_EXPERIENCE_AND_CONTENT_GATE.md](../quality-gates/USER_EXPERIENCE_AND_CONTENT_GATE.md), [TESTING_AND_EVIDENCE_GATE.md](../quality-gates/TESTING_AND_EVIDENCE_GATE.md) |
| Fix duplicate webhook processing in the backend API. | [backend-and-data-engineering.md](../specialists/backend-and-data-engineering.md) → [edge-and-distributed-systems.md](../specialists/edge-and-distributed-systems.md) → [quality-engineering-and-test-strategy.md](../specialists/quality-engineering-and-test-strategy.md) | [ARCHITECTURE_AND_DATA_GATE.md](../quality-gates/ARCHITECTURE_AND_DATA_GATE.md), [TESTING_AND_EVIDENCE_GATE.md](../quality-gates/TESTING_AND_EVIDENCE_GATE.md) |
| Review Foundry proxy storage and Solidity reentrancy before a testnet release. | [solidity-contract-engineering.md](../specialists/solidity-contract-engineering.md) → [formal-methods-and-invariants.md](../specialists/formal-methods-and-invariants.md) → [security-architecture-and-red-teaming.md](../specialists/security-architecture-and-red-teaming.md) | [ARCHITECTURE_AND_DATA_GATE.md](../quality-gates/ARCHITECTURE_AND_DATA_GATE.md), [TESTING_AND_EVIDENCE_GATE.md](../quality-gates/TESTING_AND_EVIDENCE_GATE.md) |
| Repair a responsive form and frontend focus at high zoom. | [frontend-engineering.md](../specialists/frontend-engineering.md) → [platform-compatibility-matrix.md](../references/platform-compatibility-matrix.md) → [SCREEN_AND_STATE_INVENTORY.md](../templates/SCREEN_AND_STATE_INVENTORY.md) → [accessibility-and-internationalization.md](../specialists/accessibility-and-internationalization.md) | [USER_EXPERIENCE_AND_CONTENT_GATE.md](../quality-gates/USER_EXPERIENCE_AND_CONTENT_GATE.md), [TESTING_AND_EVIDENCE_GATE.md](../quality-gates/TESTING_AND_EVIDENCE_GATE.md) |
| Migrate a shared package through a monorepo codemod. | [monorepo-and-cross-repo-engineering.md](../specialists/monorepo-and-cross-repo-engineering.md) → [migration-and-compatibility.md](../specialists/migration-and-compatibility.md) → [quality-engineering-and-test-strategy.md](../specialists/quality-engineering-and-test-strategy.md) | [ARCHITECTURE_AND_DATA_GATE.md](../quality-gates/ARCHITECTURE_AND_DATA_GATE.md), [TESTING_AND_EVIDENCE_GATE.md](../quality-gates/TESTING_AND_EVIDENCE_GATE.md) |

## Preservation and corrections

The first request led to two replacements before the staged merge instruction arrived. The original README and master orchestrator were restored at their original sizes (3,863 and 9,574 bytes), then extended only under new headings. The original baseline is 150 files and 128,081 bytes.

Only a file created during this session, `templates/TECHNOLOGY_DECISION_RECORD.md`, was removed: its fields were merged into the original technical-decision-records reference to avoid duplication. Unfinished routing rows created in the first pass were replaced because they pointed to resources that had not been created. Two new examples were corrected: a placeholder refactoring path became a real README command, and an Alloy example that assumed its conclusion became a transfer-preservation model with a separate TLA+ reservation sketch. No original project content was deleted for these corrections.

## Remaining limits and uncertainty

Every requested topic group has an owning resource and practical guidance. Coverage is deliberately consolidated; the toolkit does not recreate historical file-count targets by duplicating resources.

- Live agent evaluations remain unverified; all 69 cases retain `not_run` status in the evaluation file.
- Actual devices, assistive technologies, PTYs/SSH/tmux, GPUs, cloud deployments, Kubernetes, native/mobile toolchains, and blockchain environments were not integration-tested in this documentation task.
- Alloy/TLA+ examples were not run in a model checker. They are bounded sketches with explicit assumptions, not proofs of a deployed implementation.
- Version-sensitive commands require the installed version/help and current authoritative docs. No vendor price, regulatory certification, model superiority, or production-readiness guarantee is asserted.
- Keyword routing demonstrates deterministic selection and exclusions; agents must still interpret intent and select relevant catalogue resources. Static duplicate-title checks do not prove semantic uniqueness.
- The local source tree had no Git repository. Change accounting uses the preserved baseline, not a claimed Git diff or staged review.

## Files added

- [.gitignore](../.gitignore)
- [CATALOG.md](../CATALOG.md)
- [SKILL.md](../SKILL.md)
- [evals/SKILL_EVALS.json](../evals/SKILL_EVALS.json)
- [orchestrator/ENGINEERING_JUDGMENT_AND_EVIDENCE.md](../orchestrator/ENGINEERING_JUDGMENT_AND_EVIDENCE.md)
- [orchestrator/GLOBAL_RULES.md](../orchestrator/GLOBAL_RULES.md)
- [orchestrator/PROJECT_ROUTING.md](../orchestrator/PROJECT_ROUTING.md)
- [orchestrator/ROUTES.json](../orchestrator/ROUTES.json)
- [orchestrator/TECHNOLOGY_SELECTION.md](../orchestrator/TECHNOLOGY_SELECTION.md)
- [playbooks/HACKATHON_DELIVERY_PLAYBOOK.md](../playbooks/HACKATHON_DELIVERY_PLAYBOOK.md)
- [playbooks/SKILL_EVALUATION_PLAYBOOK.md](../playbooks/SKILL_EVALUATION_PLAYBOOK.md)
- [quality-gates/GATE_PROTOCOL.md](../quality-gates/GATE_PROTOCOL.md)
- [references/agent-context-and-handoffs.md](../references/agent-context-and-handoffs.md)
- [references/differential-and-metamorphic-testing.md](../references/differential-and-metamorphic-testing.md)
- [references/skill-lifecycle-and-improvement.md](../references/skill-lifecycle-and-improvement.md)
- [references/termux-and-constrained-environments.md](../references/termux-and-constrained-environments.md)
- [reports/GAP_ANALYSIS.md](../reports/GAP_ANALYSIS.md)
- [reports/INVENTORY.md](../reports/INVENTORY.md)
- [reports/MERGE_BASELINE.json](../reports/MERGE_BASELINE.json)
- [reports/VERIFICATION.md](../reports/VERIFICATION.md)
- [scripts/toolkit.py](../scripts/toolkit.py)
- [specialists/browser-and-desktop-automation.md](../specialists/browser-and-desktop-automation.md)
- [specialists/cli-and-tui-engineering.md](../specialists/cli-and-tui-engineering.md)
- [specialists/compatibility-runtime-engineering.md](../specialists/compatibility-runtime-engineering.md)
- [specialists/evm-transaction-engineering.md](../specialists/evm-transaction-engineering.md)
- [specialists/formal-methods-and-invariants.md](../specialists/formal-methods-and-invariants.md)
- [specialists/monorepo-and-cross-repo-engineering.md](../specialists/monorepo-and-cross-repo-engineering.md)
- [specialists/multi-agent-coordination.md](../specialists/multi-agent-coordination.md)
- [specialists/near-and-cross-chain-engineering.md](../specialists/near-and-cross-chain-engineering.md)
- [specialists/solidity-contract-engineering.md](../specialists/solidity-contract-engineering.md)
- [specialists/systems-languages-and-interop.md](../specialists/systems-languages-and-interop.md)
- [specialists/tool-and-mcp-engineering.md](../specialists/tool-and-mcp-engineering.md)
- [templates/REPOSITORY_HYGIENE.gitignore](../templates/REPOSITORY_HYGIENE.gitignore)
- [tests/test_toolkit.py](../tests/test_toolkit.py)

## Files extended

- [README.md](../README.md)
- [orchestrator/MASTER_ORCHESTRATOR_PROMPT.md](../orchestrator/MASTER_ORCHESTRATOR_PROMPT.md)
- [playbooks/AI_AGENT_IMPLEMENTATION_PLAYBOOK.md](../playbooks/AI_AGENT_IMPLEMENTATION_PLAYBOOK.md)
- [playbooks/EXISTING_REPOSITORY_AUDIT_PLAYBOOK.md](../playbooks/EXISTING_REPOSITORY_AUDIT_PLAYBOOK.md)
- [playbooks/INCIDENT_RESPONSE_PLAYBOOK.md](../playbooks/INCIDENT_RESPONSE_PLAYBOOK.md)
- [playbooks/PERFORMANCE_INVESTIGATION_PLAYBOOK.md](../playbooks/PERFORMANCE_INVESTIGATION_PLAYBOOK.md)
- [quality-gates/ANTI-BLOAT-AND-ANTI-GENERIC-AI.md](../quality-gates/ANTI-BLOAT-AND-ANTI-GENERIC-AI.md)
- [quality-gates/USER_EXPERIENCE_AND_CONTENT_GATE.md](../quality-gates/USER_EXPERIENCE_AND_CONTENT_GATE.md)
- [references/platform-compatibility-matrix.md](../references/platform-compatibility-matrix.md)
- [references/release-and-change-management.md](../references/release-and-change-management.md)
- [references/reliability-engineering-patterns.md](../references/reliability-engineering-patterns.md)
- [references/security-control-catalogue.md](../references/security-control-catalogue.md)
- [references/technical-decision-records.md](../references/technical-decision-records.md)
- [specialists/ai-evaluation-and-governance.md](../specialists/ai-evaluation-and-governance.md)
- [specialists/backend-and-data-engineering.md](../specialists/backend-and-data-engineering.md)
- [specialists/backup-and-disaster-recovery.md](../specialists/backup-and-disaster-recovery.md)
- [specialists/cost-and-capacity-engineering.md](../specialists/cost-and-capacity-engineering.md)
- [specialists/data-governance-and-compliance.md](../specialists/data-governance-and-compliance.md)
- [specialists/data-platform-and-pipelines.md](../specialists/data-platform-and-pipelines.md)
- [specialists/devops-and-release.md](../specialists/devops-and-release.md)
- [specialists/edge-and-distributed-systems.md](../specialists/edge-and-distributed-systems.md)
- [specialists/financial-planning-and-unit-economics.md](../specialists/financial-planning-and-unit-economics.md)
- [specialists/frontend-engineering.md](../specialists/frontend-engineering.md)
- [specialists/game-and-interactive-systems.md](../specialists/game-and-interactive-systems.md)
- [specialists/identity-and-access-management.md](../specialists/identity-and-access-management.md)
- [specialists/legal-policy-and-regulatory-coordination.md](../specialists/legal-policy-and-regulatory-coordination.md)
- [specialists/migration-and-compatibility.md](../specialists/migration-and-compatibility.md)
- [specialists/mobile-and-device-experiences.md](../specialists/mobile-and-device-experiences.md)
- [specialists/motion-3d-and-immersive.md](../specialists/motion-3d-and-immersive.md)
- [specialists/quality-engineering-and-test-strategy.md](../specialists/quality-engineering-and-test-strategy.md)
- [specialists/search-relevance-and-recommendations.md](../specialists/search-relevance-and-recommendations.md)
- [specialists/security-architecture-and-red-teaming.md](../specialists/security-architecture-and-red-teaming.md)
- [specialists/supply-chain-and-build-security.md](../specialists/supply-chain-and-build-security.md)
- [specialists/technical-debt-and-modernization.md](../specialists/technical-debt-and-modernization.md)
- [templates/SCREEN_AND_STATE_INVENTORY.md](../templates/SCREEN_AND_STATE_INVENTORY.md)

## Files untouched

- [orchestrator/FEATURE_DECISION_FRAMEWORK.md](../orchestrator/FEATURE_DECISION_FRAMEWORK.md)
- [orchestrator/PROJECT_DISCOVERY_PROTOCOL.md](../orchestrator/PROJECT_DISCOVERY_PROTOCOL.md)
- [playbooks/ACCESSIBILITY_REMEDIATION_PLAYBOOK.md](../playbooks/ACCESSIBILITY_REMEDIATION_PLAYBOOK.md)
- [playbooks/DATA_MIGRATION_PLAYBOOK.md](../playbooks/DATA_MIGRATION_PLAYBOOK.md)
- [playbooks/DESIGN_SYSTEM_IMPLEMENTATION_PLAYBOOK.md](../playbooks/DESIGN_SYSTEM_IMPLEMENTATION_PLAYBOOK.md)
- [playbooks/END_TO_END_PRODUCT_BUILD_PLAYBOOK.md](../playbooks/END_TO_END_PRODUCT_BUILD_PLAYBOOK.md)
- [playbooks/PRODUCTION_READINESS_PLAYBOOK.md](../playbooks/PRODUCTION_READINESS_PLAYBOOK.md)
- [playbooks/RESEARCH_TO_ROADMAP_PLAYBOOK.md](../playbooks/RESEARCH_TO_ROADMAP_PLAYBOOK.md)
- [playbooks/THIRD_PARTY_INTEGRATION_PLAYBOOK.md](../playbooks/THIRD_PARTY_INTEGRATION_PLAYBOOK.md)
- [quality-gates/AI_AND_AUTOMATION_RELEASE_GATE.md](../quality-gates/AI_AND_AUTOMATION_RELEASE_GATE.md)
- [quality-gates/ARCHITECTURE_AND_DATA_GATE.md](../quality-gates/ARCHITECTURE_AND_DATA_GATE.md)
- [quality-gates/COMMERCIAL_AND_OPERATIONS_GATE.md](../quality-gates/COMMERCIAL_AND_OPERATIONS_GATE.md)
- [quality-gates/DEFINITION_OF_DONE.md](../quality-gates/DEFINITION_OF_DONE.md)
- [quality-gates/DOMAIN_AND_INTEGRATION_GATE.md](../quality-gates/DOMAIN_AND_INTEGRATION_GATE.md)
- [quality-gates/INTEGRATION_AND_OPERATIONS_GATE.md](../quality-gates/INTEGRATION_AND_OPERATIONS_GATE.md)
- [quality-gates/MAINTAINABILITY_AND_HANDOFF_GATE.md](../quality-gates/MAINTAINABILITY_AND_HANDOFF_GATE.md)
- [quality-gates/PROJECT_DISCOVERY_AND_SCOPE_GATE.md](../quality-gates/PROJECT_DISCOVERY_AND_SCOPE_GATE.md)
- [quality-gates/TESTING_AND_EVIDENCE_GATE.md](../quality-gates/TESTING_AND_EVIDENCE_GATE.md)
- [references/architecture-decision-records.md](../references/architecture-decision-records.md)
- [references/architecture-pattern-selection-guide.md](../references/architecture-pattern-selection-guide.md)
- [references/capability-catalogue.md](../references/capability-catalogue.md)
- [references/complete-product-capability-map.md](../references/complete-product-capability-map.md)
- [references/content-design-and-voice-guide.md](../references/content-design-and-voice-guide.md)
- [references/data-modeling-and-integrity-guide.md](../references/data-modeling-and-integrity-guide.md)
- [references/design-and-content-principles.md](../references/design-and-content-principles.md)
- [references/design-system-governance.md](../references/design-system-governance.md)
- [references/full-stack-product-patterns.md](../references/full-stack-product-patterns.md)
- [references/integration-patterns-and-failure-modes.md](../references/integration-patterns-and-failure-modes.md)
- [references/interaction-and-state-pattern-library.md](../references/interaction-and-state-pattern-library.md)
- [references/metrics-and-experimentation-guide.md](../references/metrics-and-experimentation-guide.md)
- [references/operational-excellence-guide.md](../references/operational-excellence-guide.md)
- [references/platform-and-operational-capabilities.md](../references/platform-and-operational-capabilities.md)
- [references/product-domain-patterns.md](../references/product-domain-patterns.md)
- [references/research-and-validation-methods.md](../references/research-and-validation-methods.md)
- [specialists/3d-spatial-and-immersive-experiences.md](../specialists/3d-spatial-and-immersive-experiences.md)
- [specialists/accessibility-and-inclusive-research.md](../specialists/accessibility-and-inclusive-research.md)
- [specialists/accessibility-and-internationalization.md](../specialists/accessibility-and-internationalization.md)
- [specialists/api-and-developer-experience.md](../specialists/api-and-developer-experience.md)
- [specialists/architecture-and-systems-design.md](../specialists/architecture-and-systems-design.md)
- [specialists/billing-and-entitlements.md](../specialists/billing-and-entitlements.md)
- [specialists/brand-and-art-direction.md](../specialists/brand-and-art-direction.md)
- [specialists/commerce-and-checkout.md](../specialists/commerce-and-checkout.md)
- [specialists/content-platform-and-cms.md](../specialists/content-platform-and-cms.md)
- [specialists/customer-support-and-success.md](../specialists/customer-support-and-success.md)
- [specialists/design-systems-and-ui.md](../specialists/design-systems-and-ui.md)
- [specialists/desktop-and-cross-platform.md](../specialists/desktop-and-cross-platform.md)
- [specialists/education-and-learning-products.md](../specialists/education-and-learning-products.md)
- [specialists/experimentation-and-growth.md](../specialists/experimentation-and-growth.md)
- [specialists/finops-and-cloud-economics.md](../specialists/finops-and-cloud-economics.md)
- [specialists/fintech-and-ledger-systems.md](../specialists/fintech-and-ledger-systems.md)
- [specialists/full-stack-application-architecture.md](../specialists/full-stack-application-architecture.md)
- [specialists/hardware-and-iot-systems.md](../specialists/hardware-and-iot-systems.md)
- [specialists/healthcare-product-safety.md](../specialists/healthcare-product-safety.md)
- [specialists/human-content-and-ux-writing.md](../specialists/human-content-and-ux-writing.md)
- [specialists/import-export-and-data-portability.md](../specialists/import-export-and-data-portability.md)
- [specialists/marketplace-and-reputation.md](../specialists/marketplace-and-reputation.md)
- [specialists/monetization-and-growth.md](../specialists/monetization-and-growth.md)
- [specialists/multi-tenancy-and-enterprise-governance.md](../specialists/multi-tenancy-and-enterprise-governance.md)
- [specialists/notifications-and-messaging.md](../specialists/notifications-and-messaging.md)
- [specialists/observability-and-incident-response.md](../specialists/observability-and-incident-response.md)
- [specialists/offline-and-resilient-experiences.md](../specialists/offline-and-resilient-experiences.md)
- [specialists/performance-and-reliability.md](../specialists/performance-and-reliability.md)
- [specialists/portfolio-and-program-management.md](../specialists/portfolio-and-program-management.md)
- [specialists/privacy-engineering.md](../specialists/privacy-engineering.md)
- [specialists/product-strategy.md](../specialists/product-strategy.md)
- [specialists/qa-and-verification.md](../specialists/qa-and-verification.md)
- [specialists/real-time-media-and-streaming.md](../specialists/real-time-media-and-streaming.md)
- [specialists/realtime-and-collaboration.md](../specialists/realtime-and-collaboration.md)
- [specialists/research-and-discovery.md](../specialists/research-and-discovery.md)
- [specialists/robotics-and-autonomous-systems.md](../specialists/robotics-and-autonomous-systems.md)
- [specialists/search-and-information-retrieval.md](../specialists/search-and-information-retrieval.md)
- [specialists/security-and-privacy.md](../specialists/security-and-privacy.md)
- [specialists/seo-and-discoverability.md](../specialists/seo-and-discoverability.md)
- [specialists/technical-documentation.md](../specialists/technical-documentation.md)
- [specialists/technical-writing-and-knowledge-management.md](../specialists/technical-writing-and-knowledge-management.md)
- [specialists/trust-safety-and-moderation.md](../specialists/trust-safety-and-moderation.md)
- [specialists/ux-and-information-architecture.md](../specialists/ux-and-information-architecture.md)
- [specialists/visualization-and-information-design.md](../specialists/visualization-and-information-design.md)
- [specialists/voice-and-conversational-experiences.md](../specialists/voice-and-conversational-experiences.md)
- [specialists/workflow-automation-and-integrations.md](../specialists/workflow-automation-and-integrations.md)
- [templates/ACCESSIBILITY_AND_LOCALIZATION_REVIEW.md](../templates/ACCESSIBILITY_AND_LOCALIZATION_REVIEW.md)
- [templates/ACCESSIBILITY_CONFORMANCE_REPORT.md](../templates/ACCESSIBILITY_CONFORMANCE_REPORT.md)
- [templates/ACCESSIBILITY_TEST_PLAN.md](../templates/ACCESSIBILITY_TEST_PLAN.md)
- [templates/AI_EVALUATION_PLAN.md](../templates/AI_EVALUATION_PLAN.md)
- [templates/AI_FEATURE_SAFETY_REVIEW.md](../templates/AI_FEATURE_SAFETY_REVIEW.md)
- [templates/AI_TOOL_PERMISSION_MATRIX.md](../templates/AI_TOOL_PERMISSION_MATRIX.md)
- [templates/ANALYTICS_METRIC_SPEC.md](../templates/ANALYTICS_METRIC_SPEC.md)
- [templates/API_CONTRACT_REVIEW.md](../templates/API_CONTRACT_REVIEW.md)
- [templates/COST_MODEL_AND_CAPACITY_PLAN.md](../templates/COST_MODEL_AND_CAPACITY_PLAN.md)
- [templates/DATA_LIFECYCLE_AND_RETENTION.md](../templates/DATA_LIFECYCLE_AND_RETENTION.md)
- [templates/DEPRECATION_AND_END_OF_LIFE_PLAN.md](../templates/DEPRECATION_AND_END_OF_LIFE_PLAN.md)
- [templates/DOMAIN_MODEL_AND_STATE_MACHINE.md](../templates/DOMAIN_MODEL_AND_STATE_MACHINE.md)
- [templates/FEATURE_DECISION_REGISTER.md](../templates/FEATURE_DECISION_REGISTER.md)
- [templates/FULL_STACK_APPLICATION_BLUEPRINT.md](../templates/FULL_STACK_APPLICATION_BLUEPRINT.md)
- [templates/INCIDENT_POSTMORTEM.md](../templates/INCIDENT_POSTMORTEM.md)
- [templates/INTEGRATION_REGISTER.md](../templates/INTEGRATION_REGISTER.md)
- [templates/LOCALIZATION_READINESS.md](../templates/LOCALIZATION_READINESS.md)
- [templates/MIGRATION_RUNBOOK.md](../templates/MIGRATION_RUNBOOK.md)
- [templates/OBSERVABILITY_SPEC.md](../templates/OBSERVABILITY_SPEC.md)
- [templates/OPERATIONAL_READINESS_REVIEW.md](../templates/OPERATIONAL_READINESS_REVIEW.md)
- [templates/PERFORMANCE_BUDGET.md](../templates/PERFORMANCE_BUDGET.md)
- [templates/POST_LAUNCH_REVIEW.md](../templates/POST_LAUNCH_REVIEW.md)
- [templates/PRODUCT_RISK_REGISTER.md](../templates/PRODUCT_RISK_REGISTER.md)
- [templates/PROJECT_BRIEF.md](../templates/PROJECT_BRIEF.md)
- [templates/PROJECT_CHARTER_AND_OUTCOME_MAP.md](../templates/PROJECT_CHARTER_AND_OUTCOME_MAP.md)
- [templates/RELEASE_AND_EVIDENCE_REPORT.md](../templates/RELEASE_AND_EVIDENCE_REPORT.md)
- [templates/RELEASE_PLAN_AND_ROLLBACK.md](../templates/RELEASE_PLAN_AND_ROLLBACK.md)
- [templates/RESEARCH_PLAN_AND_FINDINGS.md](../templates/RESEARCH_PLAN_AND_FINDINGS.md)
- [templates/SECURITY_THREAT_REGISTER.md](../templates/SECURITY_THREAT_REGISTER.md)
- [templates/THIRD_PARTY_DUE_DILIGENCE.md](../templates/THIRD_PARTY_DUE_DILIGENCE.md)
- [templates/THREAT_MODEL_WORKSHEET.md](../templates/THREAT_MODEL_WORKSHEET.md)
- [templates/USER_FEEDBACK_AND_SUPPORT_TAXONOMY.md](../templates/USER_FEEDBACK_AND_SUPPORT_TAXONOMY.md)
- [templates/USER_JOURNEY_AND_FAILURE_MAP.md](../templates/USER_JOURNEY_AND_FAILURE_MAP.md)
- [templates/USER_STORY_AND_ACCEPTANCE_CRITERIA.md](../templates/USER_STORY_AND_ACCEPTANCE_CRITERIA.md)
- [templates/VENDOR_AND_EXIT_PLAN.md](../templates/VENDOR_AND_EXIT_PLAN.md)
