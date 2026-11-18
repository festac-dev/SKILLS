# AI and Automation Release Gate

- [ ] The feature has a specific user problem and measurable success criteria.
- [ ] Model output is treated as untrusted until validated.
- [ ] Tool permissions are narrow and server-enforced.
- [ ] Prompt injection and untrusted content are included in tests.
- [ ] High-impact actions have appropriate approval and confirmation.
- [ ] Actions are idempotent or protected against duplicate execution.
- [ ] Logs and evidence avoid leaking sensitive content.
- [ ] Evaluation includes normal, edge, adversarial, and failure cases.
- [ ] Cost, latency, quotas, fallback, and rollback are defined.
- [ ] Users can understand, correct, stop, or undo actions where feasible.
- [ ] Claims about model capability are supported by evaluation evidence.

Do not ship solely because a demo looks convincing.

## Application evidence

Require evidence from actual tool execution for permission and side-effect claims. A successful natural-language answer cannot mask a forbidden tool call or a repeated committed action.
