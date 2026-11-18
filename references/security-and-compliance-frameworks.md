# Security and Compliance Frameworks Map

Orientation for choosing which frameworks and standards matter. This is **not legal advice and does not certify compliance**; obligations depend on jurisdiction, data, customers and contracts. Involve qualified counsel, auditors and security professionals for regulated work. Verify current versions.

## Technical security references
| Reference | Use it for |
|---|---|
| OWASP Top 10 (web) | Awareness baseline for web app risks |
| OWASP API Security Top 10 | Broken object/function/property-level authorization, auth, resource consumption, SSRF, misconfiguration, inventory, unsafe third-party use |
| OWASP ASVS | Detailed verifiable requirements by level (L1 baseline, L2 most apps, L3 high assurance) |
| OWASP MASVS / MASTG | Mobile app requirements and testing |
| OWASP Top 10 for LLM applications | Prompt injection, insecure output handling, excessive agency, data leakage, supply chain |
| CWE Top 25 / CWE | Weakness taxonomy for code review and SAST triage |
| NIST SSDF (SP 800-218) | Secure software development practices |
| NIST CSF | Organization-level security program structure (Identify, Protect, Detect, Respond, Recover, Govern) |
| NIST SP 800-63 | Digital identity, authentication assurance, password guidance |
| CIS Benchmarks / Controls | Concrete hardening for OS, cloud, containers, Kubernetes |
| SLSA | Build provenance and supply-chain integrity levels |
| Sigstore, SBOM (SPDX, CycloneDX) | Signing, provenance, dependency transparency |
| MITRE ATT&CK / D3FEND | Threat modeling and detection mapping |
| STRIDE / LINDDUN | Threat modeling (security / privacy) |

## Assurance and compliance regimes (typical triggers)
| Regime | Typical trigger | Core themes |
|---|---|---|
| SOC 2 (Type I/II) | Selling B2B SaaS to US enterprises | Security, availability, confidentiality, processing integrity, privacy controls with evidence over time |
| ISO/IEC 27001 (and 27701 for privacy) | International customers, formal ISMS | Risk assessment, control set, audits |
| GDPR / UK GDPR | Personal data of people in the EU/UK | Lawful basis, data minimization, rights (access, erasure, portability), DPIAs, processors, breach notification (72 hours to the regulator where required), cross-border transfers |
| CCPA/CPRA and US state privacy laws | Personal data of residents of those states | Notice, opt-out of sale/sharing, rights handling |
| HIPAA (US) | Protected health information handled for covered entities | Safeguards, BAAs, audit controls, breach rules |
| PCI DSS | Storing, processing or transmitting card data | Minimize scope (use hosted fields or tokenization from a PCI-compliant provider), segmentation, logging, vulnerability management |
| COPPA / GDPR-K / age-appropriate design codes | Products used by children | Consent, data minimization, safe defaults |
| WCAG 2.2 (AA typical target), EN 301 549, ADA/Section 508, European Accessibility Act | Public sites, commerce, government and many private services | Perceivable, operable, understandable, robust; accessibility statements and testing evidence |
| FedRAMP / CMMC / IRAP / C5 and other national schemes | Selling to governments or defense supply chains | Prescriptive control baselines and assessments |
| EU NIS2 / DORA / Cyber Resilience Act | Essential/important entities, financial entities, products with digital elements | Risk management, incident reporting, supply-chain obligations |
| EU AI Act and AI risk frameworks (NIST AI RMF, ISO/IEC 42001) | AI systems in covered risk categories | Risk classification, documentation, transparency, human oversight, monitoring |
| Payment/financial rules (PSD2/SCA, AML/KYC, local money-transmission rules) | Moving or holding money | Licensing, strong authentication, record keeping |
| Export controls, sanctions, content and consumer law | Cross-border products | Specialist review |

## How to use this map
1. Identify data types (personal, health, financial, children's, credentials), user locations, customer segments and contractual demands.
2. List which regimes plausibly apply; mark **unknown** where unsure and ask the owner or counsel.
3. Build a controls baseline once (access control, encryption, logging, vulnerability management, backups, incident response, vendor management, change management, secure SDLC, training) and map it to each regime rather than building a program per regime.
4. Automate evidence collection (CI logs, access reviews, backup tests, change tickets).
5. Record decisions and residual risks. Use `templates/SECURITY_THREAT_REGISTER.md`, `templates/THIRD_PARTY_DUE_DILIGENCE.md`, `templates/DATA_LIFECYCLE_AND_RETENTION.md`, `quality-gates/DATA_SAFETY_AND_RECOVERY_GATE.md`.

## Baseline controls that satisfy most regimes' technical core
Least-privilege access with MFA and periodic review; encryption in transit and at rest with managed keys; secrets management and rotation; centralized, tamper-resistant logging with retention; vulnerability and patch management with SLAs; secure SDLC (code review, SAST/SCA, secret scanning, dependency pinning); change management and approvals; tested backups and disaster recovery; incident response plan with exercises; vendor risk process; data inventory, retention and deletion; privacy by design; employee security training; physical and endpoint security where relevant.

## Boundaries
Do not claim "compliant", "certified", "secure" or "HIPAA/PCI/SOC 2 ready" without the actual attestations or assessments. State what was implemented and what evidence exists.
