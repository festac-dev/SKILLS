# Building CLI and Clickable TUI Products

## 1. Choose the interface deliberately
Decide which tasks belong in traditional commands, guided prompts, full-screen TUI, or non-interactive automation. Do not turn every CLI into a full-screen app.

## 2. Model capabilities before drawing menus
Define commands and actions in a validated registry. Discover integrations and available capabilities from supported metadata/configuration. Derive help, completion, and UI entries from shared definitions where practical. Never hard-code a fixed provider/model/action menu when the product is meant to be extensible.

## 3. Define the interaction model
Specify navigation, focus, selection, activation, mouse behavior, keyboard equivalents, command palette/search, context menus, forms, progress, logs, cancellation, and confirmation.

## 4. Design for terminal constraints
Handle resizing, narrow/short terminals, Unicode width, color capabilities, no-color mode, light/dark themes, SSH, tmux, non-TTY streams, and terminal restoration.

## 5. Keep architecture maintainable
Separate domain logic, command parsing, application state, rendering, input, and side effects. Keep asynchronous operations cancellable and rendering non-blocking.

## 6. Verify all modes
Test keyboard-only, mouse-assisted, non-interactive, redirected output, and relevant terminal environments. Include snapshot/unit tests and real terminal integration tests.

## 7. Document honestly
Publish tested terminals, minimum dimensions, optional capabilities, keymap, accessibility behavior, and unsupported environments.
