# Specialist: DevOps and Release Engineering

Inspect the actual deployment target and operating model. Define reproducible builds, configuration, secrets handling, CI/CD, migrations, health checks, logs, metrics, alerts, backups, recovery, rollback and release procedures.

Do not assume a cloud provider, container platform or orchestration system. Do not deploy or alter production without authorization. Ensure release instructions match the actual project.

## Cloud, VPS, Linux, containers, and platform operations

### When to use
Use when selecting hosting, owning a server, containerizing a service, writing CI/IaC, operating Kubernetes, or preparing production rollout.

### Core principles
Default to the simplest environment that meets measured constraints. A VPS needs an operator; a managed platform has limits; a Kubernetes cluster needs lifecycle ownership. Do not introduce a cluster, service mesh, operator, or multi-region topology without a requirement that justifies its cost.

### Step-by-step procedure
1. Record workload, runtime, CPU architecture, data residency, network paths, storage durability, availability, budget, ownership, and supported recovery objectives.
2. Compare managed app hosting, serverless, VPS/VM, and containers against those constraints. Check job timeouts, connection limits, egress, and persistent storage before choosing.
3. On Linux servers, separate service/admin identities, restrict inbound ports, establish SSH recovery access before changing authentication/firewall rules, patch supported releases, and test log/storage rotation.
4. Define DNS, TLS termination/renewal, trusted proxies, timeouts, connection reuse, outbound rules, and internal versus public service exposure. Never expose a database publicly just to simplify application connectivity.
5. For Docker, use a reproducible build, minimal runtime stage, non-root user where supported, explicit writable paths, health checks, signal handling, and external durable volumes. Keep secrets out of build arguments, layers, and images.
6. For Kubernetes, define requests/limits, probes, disruption budgets, rollout, storage, network policy, workload identity, and version maintenance. HPA depends on useful metrics and available cluster capacity. Helm output needs review; an operator must reconcile safely and recover from partial state. Add a mesh only for a demonstrated transport/policy need.
7. For IaC, review plans and drift, secure state, lock concurrent changes, and separate preview from apply. CI builds immutable artifacts with scoped identities and protected release permissions.
8. Multi-region requires documented consistency, routing, failover authority, replication lag, and reconciliation. Include duplicate infrastructure, egress, and recovery costs in FinOps.

### Checklist
- [ ] Configuration names are documented without secret values.
- [ ] Readiness, liveness, and startup behavior have distinct purposes.
- [ ] Shutdown drains requests/jobs within a bounded deadline.
- [ ] Backup, restore, rollback, monitoring, certificate renewal, and patch ownership exist.
- [ ] Single points of failure and expected downtime are explicit.

### Common failure modes
A container image is mistaken for a backup; liveness restarts a slow but recoverable service; CI logs leak secrets; a firewall change locks out operators; “multi-region” masks a single-region database; autoscaling overloads dependencies.

### Concrete examples
Inspect installed capabilities first:
```sh
docker version
docker compose version
kubectl version --client
helm version
terraform version
```
Run only commands for installed tools. Read-only/preview checks include `docker compose config --quiet`, `kubectl config current-context`, and `helm template --help`. A rendered manifest or Terraform plan is a proposal, not a deployment. Verify current subcommand docs before applying anything. Termux is not assumed to provide Docker, systemd, or a local Kubernetes runtime.

### Verification
Record build digest, rendered configuration review, network/TLS checks, staged rollout, shutdown, and recovery evidence. An installation command or successful image build does not prove operability.

### Related skills
[Termux constraints](../references/termux-and-constrained-environments.md), [supply chain](supply-chain-and-build-security.md), [backup](backup-and-disaster-recovery.md), [FinOps](finops-and-cloud-economics.md).

## Applied verification

Start the built artifact using the documented configuration and verify readiness plus one real user operation. Track process identity, port and log location; an old PID or a successful build is not evidence that the current preview or release is serving.

When a running preview reads generated files, do not rebuild over its active output directory. Publish a completed artifact into a separate release location or use the project's existing atomic deployment mechanism. Include required runtime dependencies and assets, keep persistent data separate, and retain the previous usable artifact until the new one is checked. Probe a rendered workspace or lazy route as well as the API health endpoint; a healthy data route can coexist with broken page imports. Verify the identity of a process before stopping it and use a bounded shutdown appropriate to that service.

For a multi-process preview, check the frontend and API independently. Recovery must handle a stopped component while other services remain healthy, without resetting their persistent stores. Avoid duplicate listeners and verify the restored route before handing over its URL.

## Pipeline identity and promotion

Promote the same tested artifact across environments with configuration supplied separately. Use narrowly scoped short-lived workload credentials where supported, pin third-party build actions, and keep migration compatibility independent of rollout strategy. Fail closed on checks agreed as release blockers; preview environments, signed provenance and staged traffic are choices governed by the project’s risk. Track delivery lead time, change failures and recovery time when they help improve the process. See the [pipeline specification](../templates/DEPLOYMENT_PIPELINE_SPEC.md), [environment matrix](../templates/ENVIRONMENT_AND_CONFIG_MATRIX.md) and [infrastructure snippets](../references/infrastructure-config-snippets.md).
