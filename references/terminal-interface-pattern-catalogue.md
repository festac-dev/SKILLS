# Terminal Interface Pattern Catalogue

Use patterns only when they improve the actual workflow.

## CLI patterns
- Commands, subcommands, flags, arguments, stdin/stdout pipelines.
- Help, examples, version, diagnostics, completion, and man-page output.
- Structured output modes such as JSON where useful.
- Interactive setup and guided prompts.
- Non-interactive operation for scripts and CI.

## Interactive TUI patterns
- Command palette and fuzzy action search.
- Selectable lists, searchable tables, and tree navigation.
- Tabs, sidebars, split panes, and master/detail layouts.
- Forms, inline editing, validation, and secret input.
- Logs, streaming output, task queues, and progress indicators.
- Status bars, contextual help, notifications, and error panels.
- Confirmation flows, undo, retry, and cancellation.
- Mouse-clickable buttons, rows, tabs, links, and context menus where supported.

## Navigation patterns
- Tab/Shift+Tab focus traversal.
- Arrow-key movement and vim-style bindings when appropriate.
- Enter/Space activation.
- Escape to close or cancel with predictable semantics.
- Back navigation that preserves selection and scroll position.
- Shortcut help and remappable key bindings when useful.

## Interaction contract
Every visible control must have a defined action, focus behavior, disabled behavior, loading behavior, error behavior, and keyboard equivalent. Mouse support is progressive enhancement, not a prerequisite for completing tasks.
