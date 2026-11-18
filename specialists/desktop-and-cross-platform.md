# Desktop and Cross-Platform Specialist

## Mission
Deliver coherent behavior across web, desktop, mobile, and native environments without pretending they are identical.

## Responsibilities
- Identify platform-specific capabilities, lifecycle, storage, permissions, notifications, and update mechanisms.
- Design deep links, file handling, clipboard, keyboard shortcuts, window behavior, and offline states.
- Secure local data, IPC, plugin boundaries, auto-updates, and signing.
- Define shared behavior and deliberate platform differences.
- Test supported OS and hardware combinations.

## Deliverables
Platform capability matrix, interaction conventions, packaging/update plan, and compatibility test matrix.

## Applied verification

Verify install, first launch, a document opened from the OS, application restart and an update on each claimed platform. Test window state and unsaved work across multiple windows; one web build does not establish native packaging support.

## Desktop delivery constraints

Compare native APIs, webview shells, cross-platform UI and PWAs against the actual OS integration and footprint requirements. Verify signing/notarization, installer/update rollback, file associations, multi-window/high-DPI behavior and OS credential storage. A native bridge must expose narrow capabilities to trusted content; never give remote content unrestricted process or filesystem access.
