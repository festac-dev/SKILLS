# Terminal Compatibility Test

- Application/version:
- OS/platform:
- Terminal emulator:
- Shell:
- SSH/multiplexer:
- Terminal dimensions:
- Color mode/theme:
- Unicode/font:
- TTY or redirected:
- Date/tester:

## Checks
- [ ] Startup and exit restore terminal state.
- [ ] Resize works at narrow, standard, and short dimensions.
- [ ] Keyboard navigation and focus are usable.
- [ ] Mouse support works when available.
- [ ] Essential tasks remain possible without mouse.
- [ ] No-color and limited-color output remain understandable.
- [ ] Unicode fallback is readable.
- [ ] Long output, errors, and logs do not break layout.
- [ ] Cancellation and signals restore terminal state.
- [ ] SSH latency and tmux/screen behavior are acceptable.
- [ ] Non-TTY and redirected output produce useful results.
- [ ] Script/CI mode has stable exit codes and machine-readable output where required.

Record reproduction steps, evidence, severity, and known limitations.
