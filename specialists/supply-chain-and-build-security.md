# Software Supply Chain and Build Security Specialist

## Mission
Protect the path from source code to the software users actually run.

## Work
- Review dependency provenance, lockfiles, package lifecycle scripts, maintainers, licenses, and update practices.
- Secure CI identities, build secrets, artifact storage, signing, provenance, and release permissions.
- Use least privilege, isolated builds, pinned or verified inputs, and protected release branches.
- Generate and review SBOMs where appropriate; define vulnerability triage and exception expiry.
- Protect against dependency confusion, typosquatting, compromised maintainers, and poisoned build artifacts.

## Deliverables
Threat model, dependency policy, CI permission map, artifact integrity strategy, SBOM process, and incident playbook.

## Dependency and artifact verification

### When to use
Use for dependency changes, build pipelines, release artifacts, or suspected supply-chain compromise.

### Core principles
Lockfiles improve reproducibility but do not establish trust. Pin CI actions and build inputs according to project policy, verify provenance, and minimize build credentials. Treat package lifecycle scripts as executable third-party code.

### Step-by-step procedure
1. Inventory manifests, lockfiles, registries, lifecycle hooks, CI actions, and transitive dependencies.
2. Review changes for unexpected sources, scripts, licenses, and privilege expansion. Run the ecosystem's existing audit and secrets scanner.
3. Use clean isolated builds with immutable dependency resolution. Record source revision, builder identity, build inputs, and artifact digest.
4. Generate an SBOM for the actual artifact where required; compare it with deployed content. Assess SLSA provenance against the applicable current specification rather than claiming a level from a checklist.
5. Triage findings by exploitability and impact, assign owners/expiry to exceptions, and test upgrades.
6. If secrets were committed, revoke/rotate first and assess exposure. Removing the current file does not remove history or copies.

### Checklist
- [ ] Dependency locks and release artifacts agree.
- [ ] CI permissions are least privilege.
- [ ] SBOM and provenance refer to the shipped digest.
- [ ] Known critical findings have an explicit release decision.

### Common failure modes
Using a floating image tag; trusting an unsigned checksum from the same compromised source; scanning only direct dependencies; hiding vulnerabilities in blanket ignores; exposing production credentials to pull-request builds.

### Concrete examples
In a Node project, `npm ci` consumes the lockfile and can execute lifecycle scripts; run it only in the approved build environment. Inspect `npm audit --help` and the repository's configured scanner help before use. Review lockfile changes with `git diff -- package-lock.json` when that file exists.

### Verification
Retain scanner version/results, dependency diff, SBOM/provenance digest, and reproducible build evidence. An audit with no known findings is not proof of absence of vulnerabilities.

### Related skills
[DevOps](devops-and-release.md), [repository audit](../playbooks/EXISTING_REPOSITORY_AUDIT_PLAYBOOK.md), [security controls](../references/security-control-catalogue.md).

## Applied verification

Rebuild from the declared lockfile and inspect the artifact’s dependency and provenance information. Verify critical signatures or digests at the boundary that consumes them; a generated SBOM alone does not prove dependency safety.

For a package lifecycle hook that installs native software, distinguish package installation from runtime initialization. Document required OS/toolchain versions and privilege needs, resume completed download/install steps, and serialize shared writes with the application's setup path. Where installation is intended to prepare software only, verify that it does not create wallet keys, initialize user recovery state or start transactions. Exercise the real hook, not only dependency resolution with lifecycle scripts disabled; describe an explicit offline/external-service skip only when the product supports it.

Source archives may lack Git metadata. Keep revision absence explicit and use a deterministic, scoped file inventory and hashes when evidence tooling needs an artifact identity. Exclude secrets, runtime stores and caches; do not fabricate a commit or require users to initialize Git just to verify downloaded code.
