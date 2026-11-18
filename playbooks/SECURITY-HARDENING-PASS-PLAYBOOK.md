# Playbook: Security Hardening Pass (Authorized)

1. Confirm authorization and scope; avoid destructive testing.
2. Inventory assets, entry points, secrets, identities, dependencies, data flows.
3. Threat model top risks; rank by impact and likelihood.
4. Review authentication, authorization (object-level), input handling, file uploads, SSRF, secrets, headers, CORS, rate limits, logging.
5. Scan dependencies, containers, IaC, and repositories (including history) for known issues and secrets.
6. Review infrastructure: exposed ports, IAM breadth, public storage, TLS, patch levels.
7. Test negative cases with automated tests where possible.
8. Record findings in `SECURITY_REVIEW_FINDINGS.md` with evidence and severity.
9. Fix highest-risk items first; retest; document accepted risks.
10. Establish ongoing checks in CI and a vulnerability response path.
Claims of "secure" require evidence and appropriate independent review for high-risk products.

## If an external tester is involved
Prepare scope, test accounts, and rules of engagement; obtain authorization; confirm logging and alerting would detect the tests; track residual risks and a disclosure contact; re-run after significant changes.
