# Systems Languages and Interoperability Specialist

## When to use
Load for Rust, Go, C/C++, native libraries, FFI, WebAssembly, or ABI/platform portability. Do not migrate an application language merely for presumed speed.

## Core principles
Make ownership, lifetimes, concurrency, layout, and error boundaries explicit. Unsafe/native boundaries need stronger evidence than ordinary glue code. Benchmark representative workloads before choosing a lower-level implementation.

## Step-by-step procedure
1. Inspect compiler/runtime versions, target triples, build system, supported operating systems, libc, and CPU architecture.
2. Identify ownership and allocation across FFI. The allocator that creates memory should have an explicit matching release operation.
3. Define ABI-stable types, alignment, encoding, length limits, nullability, thread safety, and error translation. Do not expose Rust layout or C++ exceptions as an assumed stable C ABI.
4. In Rust, minimize unsafe scope and document invariants. In Go, avoid goroutine leaks and define cancellation/ownership. In C/C++, use bounds checks, RAII where available, and configured sanitizers.
5. For WASM, distinguish browser and WASI hosts, imported capabilities, memory limits, and host-call cost. Sandboxing does not make an unsafe host import safe.
6. Run boundary, concurrency, malformed-input, and cross-target tests using the project's existing toolchain.

## Checklist
- [ ] Allocation and deallocation responsibility is unambiguous.
- [ ] Panics/exceptions do not unwind across unsupported boundaries.
- [ ] Integer widths, overflow, endianness, and alignment are explicit.
- [ ] Cancellation releases native resources.

## Common failure modes
Double-free across allocators; retained pointers outlive buffers; CGO changes deployment assumptions; lock-free code lacks memory-order reasoning; WASM code relies on unavailable host filesystem APIs.

## Concrete examples
Inspect versions with `rustc --version`, `cargo --version`, `go version`, `cc --version`, and `cmake --version` for installed tools. Use `cargo test` or `go test ./...` in their actual project. Verify sanitizer support with the installed compiler's help and project build configuration; do not assume Android and desktop toolchains expose the same flags.

An FFI byte buffer should specify pointer plus length, whether null with zero length is valid, and which exported release function owns deallocation.

## Verification
Record targets tested, compiler flags, sanitizer/race results where supported, malformed-input outcomes, and representative performance. A host-only pass does not establish cross-platform correctness.

## Related skills
[Termux](../references/termux-and-constrained-environments.md), [formal methods](formal-methods-and-invariants.md), [performance investigation](../playbooks/PERFORMANCE_INVESTIGATION_PLAYBOOK.md).

## Applied verification

Test ownership, buffer bounds and error propagation across the FFI boundary, including cancellation and partial initialization. Run supported sanitizers or equivalent checks on the relevant architecture and document unavailable targets.
