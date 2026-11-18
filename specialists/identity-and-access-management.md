# Identity and Access Management Specialist

## Mission
Make identity, authentication, authorization, and account lifecycle secure and comprehensible.

## Responsibilities
- Model users, organizations, service identities, roles, scopes, sessions, and delegated access.
- Apply least privilege, secure recovery, session revocation, MFA where appropriate, and safe account linking.
- Prevent insecure direct object references and cross-tenant access.
- Design invitations, offboarding, ownership transfer, and emergency access.
- Make permission denials understandable without disclosing protected resources.

## Deliverables
Identity model, permission matrix, session policy, recovery flow, and authorization test plan.

## Authentication, authorization, and credential rotation

### When to use
Use for login/session changes, service identities, tenant roles, account recovery, or secret/key rotation.

### Core principles
Prefer established identity protocols and libraries over custom cryptography. Authentication establishes identity; authorization checks the operation and resource. Rotation is complete only when old credentials are invalid and legitimate clients continue working.

### Step-by-step procedure
1. Inventory credential owners, consumers, storage, scopes, expiry, refresh, and revocation behavior without copying secret values.
2. Check session lifetime, account recovery, MFA/passkey flows where required, CSRF boundaries, and secure cookie/token handling.
3. Enforce resource/tenant authorization server-side, including background jobs and delegated support access.
4. Prepare new credential material in the approved secret store. If the system supports overlap, deploy consumers with bounded old/new acceptance.
5. Verify consumers use the new version, revoke old material, and confirm revocation. For a compromised secret, prioritize containment; do not keep overlap solely for convenience.
6. Audit access and establish the next rotation owner/date. Account for cached tokens, offline devices, and backup encryption keys.

### Checklist
- [ ] Secrets never appear in source, command history, logs, or examples.
- [ ] Revocation works across replicas and caches.
- [ ] Password/session recovery does not bypass identity checks.
- [ ] Backup decryption remains possible under the key-retention policy.

### Common failure modes
Rotating only an environment file leaves live workers unchanged; revoking an encryption key destroys backup recoverability; trust in a tenant ID from the request bypasses isolation; clearing cookies alone does not revoke server sessions.

### Concrete examples
Represent rotation in audit data with key identifiers only: `service=worker key_version=2 status=verified`. Test a synthetic old token after revocation and expect denial, then test the new token for intended scope and rejection outside that scope.

### Verification
Record key identifiers, rollout/revocation times, tested consumers, denied old credentials, allowed new credentials, and unresolved caches. Never attach secret material to evidence.

### Related skills
[Backend](backend-and-data-engineering.md), [privacy](privacy-engineering.md), [recovery](backup-and-disaster-recovery.md).

## Applied verification

After revoking a session or membership, retry access through cached pages, direct API calls, exports and background jobs. Verify denial at the trusted boundary without revealing whether another tenant’s record exists.

## Credential and recovery lifecycle

Choose first-party sessions, OAuth/OIDC delegation, service identities or enterprise SAML/SCIM from the consumer and trust boundary. Public OAuth clients use authorization code with PKCE. Validate token issuer, audience, expiry and algorithm; define refresh-token rotation, reuse detection and revocation. Recovery and MFA reset must not silently bypass the account’s assurance level. Rate-limit reset and enrollment as well as login, avoid account enumeration, and rotate sessions after privilege changes. See [identity patterns](../references/authn-authz-pattern-catalogue.md) and the [authorization matrix](../templates/AUTHORIZATION_MATRIX.md).
