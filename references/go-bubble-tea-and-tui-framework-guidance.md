# Go, Bubble Tea, and TUI Framework Guidance

Framework choice is a project decision, not a default requirement.

## Go ecosystem examples
- Bubble Tea can provide an event-driven model/update/view architecture for terminal applications.
- Bubbles provides reusable components such as lists, text inputs, viewports, tables, and progress indicators.
- Lip Gloss can help with terminal styling and layout.
- Cobra is commonly used for structured CLI command trees.
- Viper may be useful for layered configuration when its complexity is justified.

These are examples, not mandatory dependencies. Evaluate maintenance, compatibility, accessibility, testing, binary size, licensing, and team familiarity before selection.

## Bubble Tea design considerations
- Keep application state explicit and model transitions predictable.
- Keep I/O and long-running work out of rendering functions.
- Use commands/messages for asynchronous work and cancellation.
- Make resize messages first-class.
- Treat mouse events as optional capabilities and provide keyboard equivalents.
- Compose Bubbles components only where they fit the product's interaction model.
- Keep business logic independent from the TUI framework.
- Provide a non-interactive execution path for scripts and CI.
- Test update transitions, command behavior, rendering snapshots, and real terminal interactions.

## Avoid
- Binding all domain logic to a single framework's model type.
- Hard-coding menu contents and provider choices into rendering code.
- Assuming mouse support, true color, or a particular terminal.
- Blocking the event loop on network, filesystem, or process operations.
- Requiring a full-screen TUI for automation.

## Asynchronous state and sensitive input

Return the updated model together with its command. When a helper mutates an epoch, loading flag or input focus, avoid evaluating a model copy before that mutation. Exercise the actual key-to-command-to-message path, not only the helper in isolation.

Tag asynchronous replies so a response started before a lock or newer operation cannot restore stale private state. Keep hidden input masked, clear submitted secrets from the rendered input model, and never place them in command arguments or logs. Verify a real PTY and the non-TTY refusal separately; TERM=dumb is not evidence of interactive ANSI support.
