# Read-Only Reconnaissance Inventory

Historical merge record. See [the current upgrade verification](UPGRADE_VERIFICATION.md) for this revision.

Snapshot taken after the first request and before further edits under the staged merge instructions. The directory then contained 157 files: 150 original resources plus seven session additions. The README and master orchestrator had already been replaced in that first pass; their exact original text was subsequently restored before additive merging. No archive or Git metadata was present.

Original conventions: lowercase kebab-case specialists/references; uppercase underscore orchestration, templates, gates, and playbooks; one H1 with optional H2 sections; no original YAML frontmatter. Only the new root SKILL.md uses name/description frontmatter. Filesystem mtimes are observed metadata, not reliable authorship dates.

| Path | Title / initial topics | Bytes | Observed modified UTC |
|---|---|---:|---|
| `.gitignore` | Toolkit build products and Python caches only. | 94 | 2026-11-06T15:00:11.074Z |
| `README.md` | Universal Professional Product Creation System; Start here; Choose a workflow | 6988 | 2026-11-06T15:00:54.226Z |
| `SKILL.md` | Professional Product Creation; Workflow; Constraints | 2988 | 2026-11-06T15:00:11.010Z |
| `orchestrator/ENGINEERING_JUDGMENT_AND_EVIDENCE.md` | Engineering Judgment and Evidence; Improve decisions; Evidence ledger | 2646 | 2026-11-06T15:00:11.054Z |
| `orchestrator/FEATURE_DECISION_FRAMEWORK.md` | Feature Decision Framework; Decision labels; Anti-bloat test | 1339 | 2026-11-06T12:29:16.989Z |
| `orchestrator/MASTER_ORCHESTRATOR_PROMPT.md` | Master Orchestrator — Professional Product Creation; Establish context and authority; Define the outcome | 5314 | 2026-11-06T15:00:54.226Z |
| `orchestrator/PROJECT_DISCOVERY_PROTOCOL.md` | Project Discovery Protocol; Inspection order; Record | 1329 | 2026-11-06T12:29:16.993Z |
| `orchestrator/PROJECT_ROUTING.md` | Project Routing; Compose without duplicate process; Routing examples | 3954 | 2026-11-06T15:00:11.026Z |
| `orchestrator/TECHNOLOGY_SELECTION.md` | Technology Selection and Evolution; Hard constraints; Compare a credible shortlist | 2468 | 2026-11-06T15:00:11.050Z |
| `playbooks/ACCESSIBILITY_REMEDIATION_PLAYBOOK.md` | Accessibility Remediation Playbook | 548 | 2026-11-06T12:29:17.437Z |
| `playbooks/AI_AGENT_IMPLEMENTATION_PLAYBOOK.md` | AI Agent Implementation Playbook; Define; Architect | 900 | 2026-11-06T12:29:17.425Z |
| `playbooks/DATA_MIGRATION_PLAYBOOK.md` | Data Migration Playbook; Plan; Prepare | 666 | 2026-11-06T12:29:17.437Z |
| `playbooks/DESIGN_SYSTEM_IMPLEMENTATION_PLAYBOOK.md` | Design System Implementation Playbook; Discover; Establish foundations | 763 | 2026-11-06T12:29:17.429Z |
| `playbooks/END_TO_END_PRODUCT_BUILD_PLAYBOOK.md` | End-to-End Product Build Playbook; Phase 1 — Understand; Phase 2 — Discover | 1318 | 2026-11-06T12:29:17.417Z |
| `playbooks/EXISTING_REPOSITORY_AUDIT_PLAYBOOK.md` | Existing Repository Audit Playbook; Inspect before changing; Establish baseline | 977 | 2026-11-06T12:29:17.421Z |
| `playbooks/INCIDENT_RESPONSE_PLAYBOOK.md` | Incident Response Playbook; Prepare; Detect and assess | 687 | 2026-11-06T12:29:17.433Z |
| `playbooks/PERFORMANCE_INVESTIGATION_PLAYBOOK.md` | Performance Investigation Playbook | 540 | 2026-11-06T12:29:17.441Z |
| `playbooks/PRODUCTION_READINESS_PLAYBOOK.md` | Production Readiness Playbook; Product; Engineering | 772 | 2026-11-06T12:29:17.425Z |
| `playbooks/RESEARCH_TO_ROADMAP_PLAYBOOK.md` | Research to Roadmap Playbook | 556 | 2026-11-06T12:29:17.449Z |
| `playbooks/THIRD_PARTY_INTEGRATION_PLAYBOOK.md` | Third-Party Integration Playbook | 577 | 2026-11-06T12:29:17.445Z |
| `quality-gates/AI_AND_AUTOMATION_RELEASE_GATE.md` | AI and Automation Release Gate | 833 | 2026-11-06T12:29:17.009Z |
| `quality-gates/ANTI-BLOAT-AND-ANTI-GENERIC-AI.md` | Anti-Bloat and Anti-Generic-AI Gate | 880 | 2026-11-06T12:29:17.001Z |
| `quality-gates/ARCHITECTURE_AND_DATA_GATE.md` | Architecture and Data Gate | 525 | 2026-11-06T12:29:17.017Z |
| `quality-gates/COMMERCIAL_AND_OPERATIONS_GATE.md` | Commercial and Operations Gate | 665 | 2026-11-06T12:29:17.013Z |
| `quality-gates/DEFINITION_OF_DONE.md` | Definition of Done; Product; Design and content | 1400 | 2026-11-06T12:29:17.005Z |
| `quality-gates/DOMAIN_AND_INTEGRATION_GATE.md` | Domain and Integration Gate | 799 | 2026-11-06T12:29:17.009Z |
| `quality-gates/GATE_PROTOCOL.md` | Evidence-Based Gate Protocol; Decision rules | 1290 | 2026-11-06T15:00:11.070Z |
| `quality-gates/INTEGRATION_AND_OPERATIONS_GATE.md` | Integration and Operations Gate | 702 | 2026-11-06T12:29:17.005Z |
| `quality-gates/MAINTAINABILITY_AND_HANDOFF_GATE.md` | Maintainability and Handoff Gate | 590 | 2026-11-06T12:29:17.025Z |
| `quality-gates/PROJECT_DISCOVERY_AND_SCOPE_GATE.md` | Project Discovery and Scope Gate | 617 | 2026-11-06T12:29:17.017Z |
| `quality-gates/TESTING_AND_EVIDENCE_GATE.md` | Testing and Evidence Gate | 573 | 2026-11-06T12:29:17.021Z |
| `quality-gates/USER_EXPERIENCE_AND_CONTENT_GATE.md` | User Experience and Content Gate | 570 | 2026-11-06T12:29:17.021Z |
| `references/architecture-decision-records.md` | Architecture Decision Records; Template | 547 | 2026-11-06T12:29:17.045Z |
| `references/architecture-pattern-selection-guide.md` | Architecture Pattern Selection Guide; Candidate styles; Compare on | 1253 | 2026-11-06T12:29:17.061Z |
| `references/capability-catalogue.md` | Product Capability Catalogue; Product foundations; SaaS and enterprise | 2770 | 2026-11-06T12:29:17.033Z |
| `references/complete-product-capability-map.md` | Complete Product Capability Map; Strategy and evidence; Experience and interface | 2253 | 2026-11-06T12:29:17.057Z |
| `references/content-design-and-voice-guide.md` | Content Design and Voice Guide; Principles; Error writing | 788 | 2026-11-06T12:29:17.069Z |
| `references/data-modeling-and-integrity-guide.md` | Data Modeling and Integrity Guide; Model around domain meaning; Integrity | 929 | 2026-11-06T12:29:17.073Z |
| `references/design-and-content-principles.md` | Design and Content Principles; Design for the problem, not the trend; Neutrality and user ownership | 2054 | 2026-11-06T12:29:17.037Z |
| `references/design-system-governance.md` | Design System Governance; Foundations; Components | 765 | 2026-11-06T12:29:17.065Z |
| `references/full-stack-product-patterns.md` | Full-Stack Product Patterns; Application shell; Workflow boards | 2313 | 2026-11-06T12:29:17.037Z |
| `references/integration-patterns-and-failure-modes.md` | Integration Patterns and Failure Modes; Integration approaches; Failure modes | 733 | 2026-11-06T12:29:17.077Z |
| `references/interaction-and-state-pattern-library.md` | Interaction and State Pattern Library; Global patterns; Data patterns | 1383 | 2026-11-06T12:29:17.057Z |
| `references/metrics-and-experimentation-guide.md` | Metrics and Experimentation Guide; Metric contract; Metric hierarchy | 764 | 2026-11-06T12:29:17.077Z |
| `references/operational-excellence-guide.md` | Operational Excellence Guide; Operability; Change safety | 757 | 2026-11-06T12:29:17.081Z |
| `references/platform-and-operational-capabilities.md` | Platform and Operational Capability Catalogue; Platform foundations; Collaboration and communication | 2110 | 2026-11-06T12:29:17.041Z |
| `references/platform-compatibility-matrix.md` | Platform Compatibility Matrix | 557 | 2026-11-06T12:29:17.073Z |
| `references/product-domain-patterns.md` | Product Domain Patterns; Common product domains; Cross-domain capabilities to evaluate | 1460 | 2026-11-06T12:29:17.045Z |
| `references/release-and-change-management.md` | Release and Change Management; Release dimensions; Safe delivery patterns | 910 | 2026-11-06T12:29:17.049Z |
| `references/reliability-engineering-patterns.md` | Reliability Engineering Patterns; Design for failure; Data and workflow correctness | 912 | 2026-11-06T12:29:17.049Z |
| `references/research-and-validation-methods.md` | Research and Validation Methods; Discovery; Evaluation | 817 | 2026-11-06T12:29:17.065Z |
| `references/security-control-catalogue.md` | Security Control Catalogue; Identity and access; Application security | 1076 | 2026-11-06T12:29:17.061Z |
| `references/technical-decision-records.md` | Technical Decision Records; Template | 628 | 2026-11-06T12:29:17.053Z |
| `specialists/3d-spatial-and-immersive-experiences.md` | 3D, Spatial, and Immersive Experiences Specialist; Mission; Work | 718 | 2026-11-06T12:29:17.273Z |
| `specialists/accessibility-and-inclusive-research.md` | Accessibility and Inclusive Research Specialist; Mission; Work | 689 | 2026-11-06T12:29:17.281Z |
| `specialists/accessibility-and-internationalization.md` | Specialist: Accessibility and Internationalization | 555 | 2026-11-06T12:29:17.097Z |
| `specialists/ai-evaluation-and-governance.md` | AI Evaluation and Governance Specialist; Mission; Responsibilities | 794 | 2026-11-06T12:29:17.205Z |
| `specialists/api-and-developer-experience.md` | API and Developer Experience Specialist; Mission; Responsibilities | 1115 | 2026-11-06T12:29:17.173Z |
| `specialists/architecture-and-systems-design.md` | Architecture and Systems Design Specialist; Mission; Work | 1044 | 2026-11-06T12:29:17.237Z |
| `specialists/backend-and-data-engineering.md` | Specialist: Backend and Data Engineering | 422 | 2026-11-06T12:29:17.101Z |
| `specialists/backup-and-disaster-recovery.md` | Backup and Disaster Recovery Specialist; Mission; Responsibilities | 693 | 2026-11-06T12:29:17.217Z |
| `specialists/billing-and-entitlements.md` | Specialist: Billing and Entitlements | 655 | 2026-11-06T12:29:17.157Z |
| `specialists/brand-and-art-direction.md` | Specialist: Brand and Art Direction | 640 | 2026-11-06T12:29:17.105Z |
| `specialists/commerce-and-checkout.md` | Commerce and Checkout Specialist; Mission; Scope to consider | 1021 | 2026-11-06T12:29:17.177Z |
| `specialists/content-platform-and-cms.md` | Content Platform and CMS Specialist; Mission; Responsibilities | 684 | 2026-11-06T12:29:17.193Z |
| `specialists/cost-and-capacity-engineering.md` | Cost and Capacity Engineering Specialist; Mission; Responsibilities | 676 | 2026-11-06T12:29:17.217Z |
| `specialists/customer-support-and-success.md` | Customer Support and Success Specialist; Mission; Work | 697 | 2026-11-06T12:29:17.265Z |
| `specialists/data-governance-and-compliance.md` | Specialist: Data Governance and Compliance | 565 | 2026-11-06T12:29:17.165Z |
| `specialists/data-platform-and-pipelines.md` | Data Platform and Pipeline Specialist; Mission; Responsibilities | 652 | 2026-11-06T12:29:17.201Z |
| `specialists/design-systems-and-ui.md` | Specialist: Design Systems and UI Engineering | 669 | 2026-11-06T12:29:17.105Z |
| `specialists/desktop-and-cross-platform.md` | Desktop and Cross-Platform Specialist; Mission; Responsibilities | 714 | 2026-11-06T12:29:17.221Z |
| `specialists/devops-and-release.md` | Specialist: DevOps and Release Engineering | 462 | 2026-11-06T12:29:17.109Z |
| `specialists/edge-and-distributed-systems.md` | Edge and Distributed Systems Specialist; Mission; Work | 744 | 2026-11-06T12:29:17.245Z |
| `specialists/education-and-learning-products.md` | Education and Learning Product Specialist; Mission; Responsibilities | 725 | 2026-11-06T12:29:17.185Z |
| `specialists/experimentation-and-growth.md` | Experimentation and Growth Specialist; Mission; Responsibilities | 698 | 2026-11-06T12:29:17.197Z |
| `specialists/financial-planning-and-unit-economics.md` | Financial Planning and Unit Economics Specialist; Mission; Work | 686 | 2026-11-06T12:29:17.289Z |
| `specialists/finops-and-cloud-economics.md` | FinOps and Cloud Economics Specialist; Mission; Work | 713 | 2026-11-06T12:29:17.257Z |
| `specialists/fintech-and-ledger-systems.md` | Financial Systems and Ledger Specialist; Mission; Responsibilities | 897 | 2026-11-06T12:29:17.185Z |
| `specialists/frontend-engineering.md` | Specialist: Frontend Engineering | 551 | 2026-11-06T12:29:17.113Z |
| `specialists/full-stack-application-architecture.md` | Specialist: Full-Stack Application Architecture | 1081 | 2026-11-06T12:29:17.137Z |
| `specialists/game-and-interactive-systems.md` | Game and Interactive Systems Specialist; Mission; Responsibilities | 713 | 2026-11-06T12:29:17.225Z |
| `specialists/hardware-and-iot-systems.md` | Hardware and IoT Systems Specialist; Mission; Responsibilities | 703 | 2026-11-06T12:29:17.225Z |
| `specialists/healthcare-product-safety.md` | Healthcare Product Safety Specialist; Mission; Responsibilities | 892 | 2026-11-06T12:29:17.189Z |
| `specialists/human-content-and-ux-writing.md` | Specialist: Human Content and UX Writing | 660 | 2026-11-06T12:29:17.117Z |
| `specialists/identity-and-access-management.md` | Identity and Access Management Specialist; Mission; Responsibilities | 719 | 2026-11-06T12:29:17.209Z |
| `specialists/import-export-and-data-portability.md` | Specialist: Import, Export and Data Portability | 582 | 2026-11-06T12:29:17.153Z |
| `specialists/legal-policy-and-regulatory-coordination.md` | Legal, Policy, and Regulatory Coordination Specialist; Mission; Work | 974 | 2026-11-06T12:29:17.261Z |
| `specialists/marketplace-and-reputation.md` | Marketplace and Reputation Specialist; Mission; Responsibilities | 790 | 2026-11-06T12:29:17.181Z |
| `specialists/migration-and-compatibility.md` | Migration and Compatibility Specialist; Mission; Responsibilities | 650 | 2026-11-06T12:29:17.213Z |
| `specialists/mobile-and-device-experiences.md` | Specialist: Mobile and Device Experiences | 504 | 2026-11-06T12:29:17.169Z |
| `specialists/monetization-and-growth.md` | Specialist: Monetization and Growth | 506 | 2026-11-06T12:29:17.169Z |
| `specialists/motion-3d-and-immersive.md` | Specialist: Motion, 3D and Immersive Experiences | 606 | 2026-11-06T12:29:17.117Z |
| `specialists/multi-tenancy-and-enterprise-governance.md` | Specialist: Multi-Tenancy and Enterprise Governance | 642 | 2026-11-06T12:29:17.153Z |
| `specialists/notifications-and-messaging.md` | Specialist: Notifications and Messaging | 625 | 2026-11-06T12:29:17.145Z |
| `specialists/observability-and-incident-response.md` | Specialist: Observability and Incident Response | 642 | 2026-11-06T12:29:17.161Z |
| `specialists/offline-and-resilient-experiences.md` | Specialist: Offline and Resilient Experiences | 612 | 2026-11-06T12:29:17.149Z |
| `specialists/performance-and-reliability.md` | Specialist: Performance and Reliability | 448 | 2026-11-06T12:29:17.121Z |
| `specialists/portfolio-and-program-management.md` | Portfolio and Program Management Specialist; Mission; Work | 656 | 2026-11-06T12:29:17.265Z |
| `specialists/privacy-engineering.md` | Privacy Engineering Specialist; Mission; Work | 680 | 2026-11-06T12:29:17.285Z |
| `specialists/product-strategy.md` | Specialist: Product Strategy and Product Management | 599 | 2026-11-06T12:29:17.125Z |
| `specialists/qa-and-verification.md` | Specialist: Quality Assurance and Verification | 509 | 2026-11-06T12:29:17.125Z |
| `specialists/quality-engineering-and-test-strategy.md` | Quality Engineering and Test Strategy Specialist; Mission; Work | 805 | 2026-11-06T12:29:17.241Z |
| `specialists/real-time-media-and-streaming.md` | Real-Time Media and Streaming Specialist; Mission; Work | 747 | 2026-11-06T12:29:17.249Z |
| `specialists/realtime-and-collaboration.md` | Specialist: Real-Time Systems and Collaboration | 734 | 2026-11-06T12:29:17.141Z |
| `specialists/research-and-discovery.md` | Specialist: Research and Discovery | 532 | 2026-11-06T12:29:17.129Z |
| `specialists/robotics-and-autonomous-systems.md` | Robotics and Autonomous Systems Specialist; Mission; Work | 826 | 2026-11-06T12:29:17.253Z |
| `specialists/search-and-information-retrieval.md` | Specialist: Search and Information Retrieval | 659 | 2026-11-06T12:29:17.145Z |
| `specialists/search-relevance-and-recommendations.md` | Search, Relevance, and Recommendations Specialist; Mission; Work | 765 | 2026-11-06T12:29:17.249Z |
| `specialists/security-and-privacy.md` | Specialist: Security and Privacy | 596 | 2026-11-06T12:29:17.133Z |
| `specialists/security-architecture-and-red-teaming.md` | Security Architecture and Red Team Specialist; Mission; Work | 778 | 2026-11-06T12:29:17.289Z |
| `specialists/seo-and-discoverability.md` | SEO and Discoverability Specialist; Mission; Responsibilities | 752 | 2026-11-06T12:29:17.193Z |
| `specialists/supply-chain-and-build-security.md` | Software Supply Chain and Build Security Specialist; Mission; Work | 804 | 2026-11-06T12:29:17.241Z |
| `specialists/technical-debt-and-modernization.md` | Technical Debt and Modernization Specialist; Mission; Responsibilities | 678 | 2026-11-06T12:29:17.233Z |
| `specialists/technical-documentation.md` | Specialist: Technical Documentation | 458 | 2026-11-06T12:29:17.133Z |
| `specialists/technical-writing-and-knowledge-management.md` | Technical Writing and Knowledge Management Specialist; Mission; Work | 709 | 2026-11-06T12:29:17.277Z |
| `specialists/trust-safety-and-moderation.md` | Trust, Safety, and Moderation Specialist; Mission; Responsibilities | 673 | 2026-11-06T12:29:17.229Z |
| `specialists/ux-and-information-architecture.md` | Specialist: UX and Information Architecture | 564 | 2026-11-06T12:29:17.137Z |
| `specialists/visualization-and-information-design.md` | Visualization and Information Design Specialist; Mission; Work | 702 | 2026-11-06T12:29:17.269Z |
| `specialists/voice-and-conversational-experiences.md` | Voice and Conversational Experiences Specialist; Mission; Work | 708 | 2026-11-06T12:29:17.273Z |
| `specialists/workflow-automation-and-integrations.md` | Specialist: Workflow Automation and Integrations | 666 | 2026-11-06T12:29:17.161Z |
| `templates/ACCESSIBILITY_AND_LOCALIZATION_REVIEW.md` | Accessibility and Localization Review; Accessibility; Localization | 764 | 2026-11-06T12:29:17.333Z |
| `templates/ACCESSIBILITY_CONFORMANCE_REPORT.md` | Accessibility Conformance Report; Scope; Results | 545 | 2026-11-06T12:29:17.393Z |
| `templates/ACCESSIBILITY_TEST_PLAN.md` | Accessibility Test Plan; Coverage; Manual checks | 836 | 2026-11-06T12:29:17.353Z |
| `templates/AI_EVALUATION_PLAN.md` | AI Evaluation Plan; Feature and boundaries; Evaluation set | 717 | 2026-11-06T12:29:17.349Z |
| `templates/AI_FEATURE_SAFETY_REVIEW.md` | AI Feature Safety and Quality Review; Trust boundaries; Reliability | 1110 | 2026-11-06T12:29:17.317Z |
| `templates/AI_TOOL_PERMISSION_MATRIX.md` | AI Tool Permission Matrix; Safety rules | 621 | 2026-11-06T12:29:17.401Z |
| `templates/ANALYTICS_METRIC_SPEC.md` | Analytics Metric Specification | 502 | 2026-11-06T12:29:17.321Z |
| `templates/API_CONTRACT_REVIEW.md` | API Contract Review; Interface; Error behavior | 752 | 2026-11-06T12:29:17.341Z |
| `templates/COST_MODEL_AND_CAPACITY_PLAN.md` | Cost Model and Capacity Plan; Assumptions; Unit economics | 684 | 2026-11-06T12:29:17.389Z |
| `templates/DATA_LIFECYCLE_AND_RETENTION.md` | Data Lifecycle and Retention Review; Lifecycle questions; Verification | 710 | 2026-11-06T12:29:17.345Z |
| `templates/DEPRECATION_AND_END_OF_LIFE_PLAN.md` | Deprecation and End-of-Life Plan; Change; Impact | 667 | 2026-11-06T12:29:17.405Z |
| `templates/DOMAIN_MODEL_AND_STATE_MACHINE.md` | Domain Model and State Machine; Domain; State model | 575 | 2026-11-06T12:29:17.377Z |
| `templates/FEATURE_DECISION_REGISTER.md` | Feature Decision Register; Decision notes | 471 | 2026-11-06T12:29:17.301Z |
| `templates/FULL_STACK_APPLICATION_BLUEPRINT.md` | Full-Stack Application Blueprint; Product; Existing project audit | 1389 | 2026-11-06T12:29:17.317Z |
| `templates/INCIDENT_POSTMORTEM.md` | Incident Review; Summary; Timeline | 596 | 2026-11-06T12:29:17.353Z |
| `templates/INTEGRATION_REGISTER.md` | Integration Register | 469 | 2026-11-06T12:29:17.325Z |
| `templates/LOCALIZATION_READINESS.md` | Localization Readiness; Languages and regions; Product checks | 781 | 2026-11-06T12:29:17.401Z |
| `templates/MIGRATION_RUNBOOK.md` | Migration Runbook; Change; Before | 760 | 2026-11-06T12:29:17.361Z |
| `templates/OBSERVABILITY_SPEC.md` | Observability Specification; Critical journeys and signals; Telemetry rules | 638 | 2026-11-06T12:29:17.365Z |
| `templates/OPERATIONAL_READINESS_REVIEW.md` | Operational Readiness Review; Service ownership; Reliability | 632 | 2026-11-06T12:29:17.329Z |
| `templates/PERFORMANCE_BUDGET.md` | Performance Budget; User journeys; Budgets | 588 | 2026-11-06T12:29:17.357Z |
| `templates/POST_LAUNCH_REVIEW.md` | Post-Launch Review; Release and audience; Outcomes | 554 | 2026-11-06T12:29:17.409Z |
| `templates/PRODUCT_RISK_REGISTER.md` | Product Risk Register; Review prompts | 537 | 2026-11-06T12:29:17.341Z |
| `templates/PROJECT_BRIEF.md` | Project Brief; Overview; Audience and context | 667 | 2026-11-06T12:29:17.305Z |
| `templates/PROJECT_CHARTER_AND_OUTCOME_MAP.md` | Project Charter and Outcome Map; Context; Outcomes | 611 | 2026-11-06T12:29:17.373Z |
| `templates/RELEASE_AND_EVIDENCE_REPORT.md` | Release and Evidence Report; Summary; Changes delivered | 539 | 2026-11-06T12:29:17.309Z |
| `templates/RELEASE_PLAN_AND_ROLLBACK.md` | Release Plan and Rollback; Release; Preflight | 676 | 2026-11-06T12:29:17.381Z |
| `templates/RESEARCH_PLAN_AND_FINDINGS.md` | Research Plan and Findings; Research question; Session guide | 546 | 2026-11-06T12:29:17.373Z |
| `templates/SCREEN_AND_STATE_INVENTORY.md` | Screen and State Inventory | 398 | 2026-11-06T12:29:17.313Z |
| `templates/SECURITY_THREAT_REGISTER.md` | Security Threat Register | 454 | 2026-11-06T12:29:17.337Z |
| `templates/TECHNOLOGY_DECISION_RECORD.md` | Technology Decision Record; Decision | 764 | 2026-11-06T15:00:11.062Z |
| `templates/THIRD_PARTY_DUE_DILIGENCE.md` | Third-Party and Dependency Review; Dependency; Risk review | 593 | 2026-11-06T12:29:17.369Z |
| `templates/THREAT_MODEL_WORKSHEET.md` | Threat Model Worksheet; System; Threat scenarios | 734 | 2026-11-06T12:29:17.397Z |
| `templates/USER_FEEDBACK_AND_SUPPORT_TAXONOMY.md` | User Feedback and Support Taxonomy; Intake categories; Record | 570 | 2026-11-06T12:29:17.385Z |
| `templates/USER_JOURNEY_AND_FAILURE_MAP.md` | User Journey and Failure Map | 417 | 2026-11-06T12:29:17.329Z |
| `templates/USER_STORY_AND_ACCEPTANCE_CRITERIA.md` | User Story and Acceptance Criteria; User need; Evidence and context | 596 | 2026-11-06T12:29:17.381Z |
| `templates/VENDOR_AND_EXIT_PLAN.md` | Vendor and Exit Plan; Provider; Operational review | 612 | 2026-11-06T12:29:17.393Z |

The full inventory is historical; the current [catalogue](../CATALOG.md) lists surviving and newly merged resources. The temporary session-added technology-decision template was consolidated into the original technical-decision-records reference and removed to avoid duplication.
