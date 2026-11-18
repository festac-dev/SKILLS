# CLI and TUI Engineering Specialist

## When to use
Load for traditional commands, guided prompts, full-screen terminal applications, interactive developer tools, command palettes, or terminal compatibility. Skip GUI-only work.

## Core principles
Keep the command/domain layer independent of rendering. Support a scriptable non-interactive path for meaningful operations where feasible. Mouse interaction is optional enhancement; keyboard access and predictable output are the baseline. Choose a framework from constraints, not fashion.

## Step-by-step procedure
1. Define command names, arguments, flags, stdin/stdout/stderr, exit codes, output format/version, configuration precedence, and cancellation.
2. Choose modes deliberately: direct command, guided prompt, full-screen TUI, or machine-readable output. Do not prompt when input is not a TTY; require needed arguments or return an actionable error.
3. Build a command registry from actual available commands/providers/models/plugins, including stable ID, label, schema, availability, permissions, handler, and help. Refresh capabilities on change; handle stale selections without hard-coded invented choices.
4. Define focus order, shortcuts, modal scope, escape/back behavior, search, panes, forms, logs, progress, and command palette. Avoid shortcut collisions with terminal/OS conventions.
5. For clickable buttons, rows, tabs, menus, and context actions, define hit regions and keyboard equivalents. Recompute regions after resize/scroll; distinguish press, release, and drag.
6. Keep slow I/O outside the render/update loop. Use cancellable work, bounded streams, backpressure, and explicit loading/error/partial states. Restore terminal modes on exit, interruption, and recoverable failures.
7. Assess framework fit: Go Bubble Tea/Bubbles/Lip Gloss for event-driven composition, Cobra for command structure; other Go libraries, Rust, Python, Node/TypeScript, or custom rendering remain valid alternatives. Verify installed APIs/versions.
8. Test SSH, tmux, resizing, narrow terminals, redirected output, TERM=dumb, limited colors, no color, Unicode width, paste, mouse-disabled operation, remote/controller mappings where applicable, and Windows terminals if supported.
9. Escape untrusted control sequences in logs/labels. Do not let remote text emit terminal escapes, clipboard sequences, or forged UI instructions.

## Checklist
- [ ] Commands can be discovered from the registry rather than guessed menus.
- [ ] Every mouse action has a keyboard path.
- [ ] Machine output stays on stdout; diagnostics/progress use stderr or the TUI.
- [ ] Non-TTY mode does not emit cursor controls or wait for hidden prompts.
- [ ] Focus and selection survive resize and capability refresh.
- [ ] Cancellation releases resources and restores the terminal.

## Common failure modes
Hard-coded model menus become stale; blocking network calls freeze rendering; rune counts do not match grapheme/display width; ANSI sequences contaminate JSON; mouse hit regions drift after scrolling; an error leaves raw mode enabled; application logs overwrite the UI.

## Concrete examples
For a Go project inspect `go version`, `go list -m all`, and `go doc` for the installed package before using Bubble Tea, Bubbles, Lip Gloss, or Cobra APIs. Major versions may use different import paths; verify against current docs and the go.mod actually present.

A command registry should distinguish an unavailable provider from an empty list and explain how to configure access. Use the same domain handler from both “orders list” and the TUI's order screen.

Minimal Python capability detection:
```python
import os
import sys
interactive = sys.stdin.isatty() and sys.stdout.isatty()
color = sys.stdout.isatty() and os.environ.get("TERM") != "dumb" and not os.environ.get("NO_COLOR")
print({"interactive": interactive, "color": color})
```
This is a baseline signal, not a complete terminal-capability probe. Respect explicit user output preferences and feature detection.

## Verification
Exercise a command with a real PTY and redirected pipes. Verify exit status, stdout/stderr separation, keyboard navigation, mouse alternatives, Unicode/wide characters, cancellation, resize, and terminal restoration. A golden screenshot alone cannot establish interaction correctness.

## Related skills
[Systems languages](systems-languages-and-interop.md), [Termux](../references/termux-and-constrained-environments.md), [platform coverage](../references/platform-compatibility-matrix.md), [experience gate](../quality-gates/USER_EXPERIENCE_AND_CONTENT_GATE.md).

## Applied verification

Run the command with piped input/output, a narrow PTY, Ctrl-C and a resized terminal. Confirm exit status and machine-readable output survive errors; interactive rendering must restore terminal modes when interrupted.

## Capability discovery and input parity

When commands or providers are extensible, derive help, completion and action menus from the same validated registry used for execution. Do not pretend a service supports discovery when it exposes only a fixed configuration. Keep selection and return position when changing views, offer an alternative to mouse-only actions, and test narrow and short terminals, Unicode-width ambiguity, tmux/SSH and redirected streams. Use the [command registry](../templates/CLI_COMMAND_AND_ACTION_REGISTRY.md) and [terminal keymap](../templates/TERMINAL_KEYMAP_AND_MOUSE_SPEC.md) for a complex interactive surface.

## Asynchronous state and portable builds

In an event-driven TUI, tag asynchronous responses with the current request or authorization generation. Ignore responses from an earlier view or session after locking, cancelling or changing selection. Keep secrets masked while entering them, and clear secret inputs and sensitive review state when access changes. Verify those transitions through the actual service contract as well as the rendered interface.

When shipping a native terminal binary with a launcher in another language, verify its source fingerprint, OS and architecture before reuse. A binary cross-compiled successfully on the build host still needs a run on the target device. Exercise both redirected input and a real PTY there; record graceful noninteractive rejection separately from keyboard navigation and terminal restoration.
