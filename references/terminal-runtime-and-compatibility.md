# Terminal Runtime and Compatibility

## Environment conditions
- TTY versus redirected stdin/stdout/stderr.
- Terminal width and height, including resize during execution.
- SSH, tmux, screen, serial, and remote latency.
- Common terminal emulators and platform terminal APIs.
- Unicode grapheme clusters, East Asian character widths, emoji, and fallback glyphs.
- 16-color, 256-color, true-color, and no-color output.
- Light and dark terminal themes.
- Alternate screen support, mouse reporting, bracketed paste, and clipboard capability.
- Limited-height terminals and narrow panes.

## Required behavior
- Provide useful plain-text output when interactive rendering is unavailable.
- Avoid corrupting the terminal after panic, exception, cancellation, or signal.
- Restore cursor visibility, alternate screen, mouse mode, and raw mode reliably.
- Handle resize without panic or unusable layout.
- Do not assume Unicode symbols or color are always available.
- Respect color-disable conventions such as `NO_COLOR`.
- Keep logs and diagnostics available without requiring a full-screen UI.
- Avoid excessive redraws and animation on high-latency remote sessions.

## Compatibility reporting
Record tested terminal emulators, OS/platforms, shell environments, multiplexer behavior, color modes, and known limitations. Do not claim universal terminal support from one local emulator.
