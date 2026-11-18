# Networking and Server Operations

Use for VPS/VM administration, DNS/TLS, reverse proxies, service exposure, Linux process management or network diagnosis. Skip host changes for an application-only task. DevOps owns release artifacts and rollout; identity owns credentials; this guide owns the host and traffic path.

## Establish the operating context

Inspect the actual OS, architecture, privileges, init system, container runtime, provider network, current services, storage and recovery access. Termux/PRoot, containers and managed runtimes do not necessarily support systemd, Docker or kernel features available on a conventional VM. Preserve the project's runtime and hosting choices unless a demonstrated constraint requires change.

Map client → DNS → edge/load balancer → TLS/proxy → application → datastore/provider, including IPv4/IPv6, public/private boundaries and outbound dependencies. Define the owner of patching, certificates, backups, disk capacity and incident response. A localhost bind, container port mapping and public firewall rule are different exposure decisions.

## Diagnose before changing

Separate name resolution, routing, connection establishment, TLS validation, HTTP behavior and application readiness. Compare the same request at successive boundaries using the configured hostname and protocol. Check certificate hostname/chain/expiry, SNI, proxy upstreams, forwarded-header trust, body-size limits, idle timeouts and keepalive. Do not disable TLS verification to make a failing check pass.

Use installed tools such as `ss`, `dig`, `curl` or `openssl` when relevant; verify flags locally. A successful TCP connection does not prove the application is healthy. A firewall change will not repair a failed process or incorrect upstream port. Keep request traces and logs free of authorization headers and private bodies.

## Operate the host

Use separate service identities, least-privilege writable directories, supported packages and bounded resources. Define startup/restart behavior, environment loading, working directory, signal handling and log rotation using the available supervisor. Distinguish a long startup from a failed service; restart loops can worsen dependency overload.

Before changing SSH or firewall policy, verify an authorized recovery channel and preserve the current working connection until a fresh connection succeeds. Preview changes and retain rollback commands. Protect databases and administrative endpoints through explicit network boundaries, not obscure ports. Do not expose them publicly to compensate for unresolved connectivity.

For containers, verify image architecture, host/container UID mapping, durable volumes, read-only paths where suitable, signal propagation, DNS and network isolation. Never mount the host container socket or grant broad privileges without a justified operational requirement. Packaging does not establish persistence or high availability.

## Endpoint failover

For an application with configurable upstream pools, establish what makes each required service usable. One healthy endpoint for one service does not satisfy another dependency. Validate network/protocol identity before sending sensitive queries; a successful TCP handshake or HTTP 200 can still contain an application-level busy status, RPC error or unusable payload.

Classify retries by operation semantics. Read requests may try another validated endpoint; a mutation with a lost response needs the API's idempotency or reconciliation contract. A failover proxy must not independently repeat an ambiguous payment or broadcast. Keep TLS verification, proxy-side DNS and the selected privacy route intact across failures; do not add direct access or route substitution to make a check pass.

Exercise a dead primary with a working alternative, all endpoints unavailable, wrong network, application errors inside HTTP 200, and a lost mutation response. If pools can change while requests are running, keep each request's endpoint selection internally consistent and apply the new pool to subsequent work. Distinguish synthetic fault checks from an observed live-provider request; neither establishes future uptime or complete host isolation.

## Verify the result

Start the exact artifact with its documented configuration. Check readiness and a representative user operation through the intended ingress. Exercise a process restart, graceful drain, TLS renewal path and storage/log limits as appropriate. Verify external exposure from an authorized vantage point; local success alone cannot establish public reachability.

Record service identity, artifact, listener, ingress path, configuration names, rollback and unresolved dependencies. Test backups through [recovery](backup-and-disaster-recovery.md); use [release guidance](devops-and-release.md) for CI/CD and deployment authorization. Do not run host-changing examples merely because this guide contains them.

## Private SSH through a gateway

Check the gateway's documented forwarding capabilities before choosing a tunnel. A gateway that terminates SSH may support local forwarding while rejecting remote forwarding even though the sandbox's own SSH server allows it. Changing the requested port does not repair an unsupported forwarding operation. For example, [instabox's SSH gateway](https://instabox.sh/docs/access/ssh.md#limits) supports local forwarding and rejects remote forwarding.

When reverse access is authorized, a supported local tunnel can reach a separate loopback-only SSH listener inside the sandbox, and that inner connection can carry the restricted reverse forward. Use temporary credentials limited to the required listen port, disable unrelated shell/forwarding access, pin host keys through the authenticated path, and clean up owned listeners and temporary files. Preserve the working administrative connection and avoid changing the global SSH policy.

Commands copied onto a phone may acquire line breaks. Keep each option with its argument and use explicit shell continuations for long commands. Distinguish successful package installation, account sign-in, tunnel establishment and public-key authentication; resolve the failing boundary without repeating unrelated setup or overwriting an existing authorized-keys file.

## Proxy boundaries and host lifecycle

Align request and idle timeouts across CDN, load balancer, proxy and application, including SSE/WebSocket connections. Trust forwarded client headers only from configured proxies and check whether direct origin access bypasses edge controls. Plan DNS TTL changes, certificate renewal and registrar recovery before a cutover. On self-managed hosts, include filesystem growth, log rotation, time synchronization, runtime/OS end of support, reboot and OOM behavior in the operating plan; test a new SSH session before removing an access path. Use the [hardening reference](../references/server-hardening-reference.md), [network map](../templates/NETWORK_AND_DNS_MAP.md) and [VPS playbook](../playbooks/VPS-DEPLOYMENT-PLAYBOOK.md); adapt service supervision to the host rather than assuming systemd exists.
