# Termux, Android, Offline, and Resource-Constrained Work

## When to use
Load for Termux/Android hosts, offline development, low-memory builds, or requested file-patch delivery. A Termux-looking path alone does not prove the executing host is Android.

## Core principles
Inspect the actual environment before choosing tools. Android/Bionic, app sandboxing, storage permissions, CPU architecture, background limits, and executable filesystem behavior differ from desktop Linux. Never assume root, systemd, Docker, glibc, or unlimited RAM.

## Step-by-step procedure
1. Inspect OS/architecture, shell, working directory, available tools, disk space, memory, and repository status. Avoid printing the whole environment because it may contain secrets.
2. Keep source/builds in Termux private storage where feasible; shared Android storage may not support executable permissions, symlinks, or reliable tool metadata.
3. Check installed package availability before prescribing installs. Use the user's existing package manager/runtime and preserve their configuration.
4. For low RAM, begin with one build job, limit concurrent test workers, and reuse caches only when inputs match. Stop on memory pressure instead of repeatedly restarting a failing parallel build.
5. For offline work, use local docs, cached verified dependencies, lockfiles, and existing tools. State missing dependencies; do not invent test success or silently replace a backend with a mock.
6. If patch delivery is requested, inventory explicit changed/new paths, choose the next unused patch number, reject absolute/traversal/symlink entries, and include checksums. Preserve paths expected by the destination. Do not create an archive when the user asks for directory-only updates.
7. Reconcile the patch against destination versions and back up affected files before applying overwrites. An archive extraction does not delete obsolete files.

## Checklist
- [ ] Actual host and available tools are verified.
- [ ] Shared-storage and background-execution constraints are explicit.
- [ ] Build concurrency fits memory and cooling limits.
- [ ] Offline checks distinguish available evidence from missing verification.
- [ ] Patch contents exclude credentials, caches, and unrelated local work.

## Common failure modes
Desktop packages assume glibc; processes die under Android background limits; an extracted executable loses permissions; a low-memory linker is mistaken for a source bug; whole-directory zips leak local state.

## Concrete examples
```sh
pwd
uname -a
command -v python
command -v git
df -h .
```
When installed in Termux, `termux-info` reports environment details; review output before sharing. For a Make-based project use `make -j1`; for Cargo use `cargo build -j 1`, only after confirming the actual project and tool. Inspect archive members before extraction with `unzip -l patch1.zip` when that real file exists.

## Verification
Record actual host, tool versions, concurrency, elapsed time, and failures. For a requested patch, compare hashes and paths after applying to a disposable destination before providing installation instructions.

## Related skills
[Systems languages](../specialists/systems-languages-and-interop.md), [compatibility runtimes](../specialists/compatibility-runtime-engineering.md), [context recovery](agent-context-and-handoffs.md).

## Application evidence

Verify the current kernel, executable architecture and runtime rather than relying on the workspace path. After environment restoration, old PIDs, sockets and background processes may be unusable; probe them, preserve logs and restart only the task’s own services before reporting localhost readiness.

If native tooling reports inconsistent missing modules whose files exist, inspect resolution paths, installed versions and a fresh cache before changing application types. A compatible alternate compiler can help isolate a host failure; record its version and keep the configured checker’s result separate. Do not hide the failure with declarations, disabled checks or an unsupported passing claim.

For disk cleanup, use [repository hygiene](repository-hygiene-and-ai-artifact-policy.md) to preserve local databases, ledger identities, SDKs and offline dependencies while removing proven build caches. Bind mounts and PRoot may expose the same directory under different absolute paths; confirm filesystem identity before treating them as separate workspaces. Do not promise that a session cannot be killed. Use task-owned processes, bounded concurrency and resumable checkpoints, and release any task-acquired wake lock when the work ends.

For background or power-interruption drills, bind evidence to the actual device, build and durable data. Require continuity and no duplicated side effects after reconnecting. A changed kernel boot ID proves a reboot, not abrupt battery/storage power loss; a process kill or emulator restart cannot stand in for hardware evidence. Keep elapsed background observations, operator-confirmed physical action and independently verified recovery outcomes distinct.
