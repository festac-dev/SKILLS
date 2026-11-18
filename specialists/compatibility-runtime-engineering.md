# Compatibility Runtime and Windows API Specialist

## When to use
Load for Wine/Proton, Box64, DXVK, Windows API shims, or running Windows applications across OS/CPU/GPU boundaries.

## Core principles
Diagnose each layer separately: application, Windows API compatibility, CPU instruction translation, graphics translation, driver, and host. Wine is not a VM; Box64 is not a Windows API layer; DXVK translates selected Direct3D APIs to Vulkan and does not guarantee host driver support.

## Step-by-step procedure
1. Record host OS, CPU architecture, executable bitness, runtime versions, GPU/driver, Vulkan availability, and application requirements.
2. Use an isolated prefix and legally obtained software. Preserve existing prefixes before changes.
3. Establish a minimal reproducer and capture the earliest relevant failure. Change one runtime or configuration at a time.
4. Verify ABI, calling convention, struct packing, handles, Unicode, threading, and error codes when implementing a Windows API shim.
5. Separate unsupported APIs from missing dependencies and driver/translation failures. Avoid random DLL replacement or broad registry tweaks.
6. Compare behavior with a known supported environment when available; document unsupported paths explicitly.

## Checklist
- [ ] Architecture and bitness match across relevant layers.
- [ ] Prefix/configuration changes are reversible.
- [ ] Runtime/driver licenses and redistribution rights are checked.
- [ ] Logs and crash dumps are reviewed for private data.

## Common failure modes
Blaming Wine for a Vulkan failure; assuming desktop Linux packages work on Android/Bionic; a stub returns success without implementing semantics; a shim ignores ABI layout; changing several layers destroys the reproducer.

## Concrete examples
Read-only inspection: `uname -m`, `file /bin/sh` on a host with that path, and `wine --version` when installed. Use `box64 --help` and `vulkaninfo --help` only for installed tools; verify current package docs before selecting diagnostics. An API shim test must check return value, output buffer, last-error behavior, and resource cleanup.

## Verification
Record a per-layer compatibility matrix and minimal test case. Compare expected and actual observable API behavior. Unsupported calls must return an explicit appropriate failure, never silent success.

## Related skills
[Systems languages](systems-languages-and-interop.md), [Termux](../references/termux-and-constrained-environments.md), [desktop](desktop-and-cross-platform.md).

## Applied verification

Capture the first failing boundary with the executable architecture, host kernel, loader and translation versions. Run a minimal reproducer at that layer before changing the application; a successful launch alone does not verify input, rendering or persistence.
