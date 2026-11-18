# Backend Threat Checklist

Use as prompts, not as proof of security. Mark each: not applicable, verified, partial, open.

## Access
- Every endpoint authenticated unless intentionally public; object-level checks; function-level checks; tenant scoping.
- Admin routes separated and protected; default accounts removed.

## Input and output
- Schema validation; parameterized queries; command and path safety; output encoding; file upload limits and type checks; request size and time limits; safe parsers (XML external entities disabled).

## Data
- TLS in transit; encryption at rest where needed; secrets in a manager; PII minimized; backups encrypted; deletion works; logs free of secrets and personal data.

## Sessions and identity
- Secure cookies; rotation; expiry; revocation; MFA options; rate limits on login, reset and OTP; breached password checks.

## Network and platform
- Default-deny firewall; private database networking; no exposed admin ports; TLS config scanned; security headers; CORS allow-list; SSRF controls; container non-root; patched OS and dependencies.

## Abuse and resilience
- Rate limiting; quota; bot controls on signup and expensive endpoints; queue and worker limits; graceful degradation; DoS-sensitive code paths reviewed (regex, large JSON, zip).

## Supply chain
- Lockfiles; vulnerability scanning; pinned CI actions or tools; minimal build secrets; artifact provenance when needed.

## Detection and response
- Security event logging; alerts for auth anomalies; incident contact path; key rotation procedure tested.

## Disclosure
Provide a security contact and policy when the product is public.
