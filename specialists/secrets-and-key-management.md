# Secrets and Key Management Specialist

## Mission
Keep credentials and cryptographic keys out of the wrong hands, rotatable, and auditable.

## Practices
- Inventory every secret: owner, purpose, scope, storage location, rotation interval, blast radius.
- Store in a secret manager (cloud KMS/Secrets Manager, HashiCorp Vault, Doppler, 1Password/Infisical-style tools) or encrypted platform variables; never in git, images, client bundles, tickets, or chat.
- Prefer short-lived, workload-identity credentials (OIDC, IAM roles) to long-lived static keys.
- Separate secrets per environment and per service; least privilege scopes.
- Rotate on schedule and on suspicion; design systems to support two valid keys during rotation.
- Encrypt sensitive data with envelope encryption; keep key use audited; define key loss and compromise procedures.
- Scan repositories and history for leaked secrets; if one leaks, revoke and rotate first, then clean history.
- Mask secrets in CI logs; restrict who can read production secrets.
- Frontend rule: anything shipped to the browser is public. Public keys and publishable identifiers only.

## Failure modes
`.env` committed, shared admin tokens, no rotation path, secrets pasted in screenshots, over-privileged CI tokens.

## Deliverables
Secrets inventory, rotation runbook, access list, leak-response steps.
