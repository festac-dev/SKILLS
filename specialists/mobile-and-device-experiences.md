# Specialist: Mobile and Device Experiences

Design around actual devices, input methods, screen sizes, network quality, permissions, battery and platform conventions.

Consider responsive web, PWA, native apps, tablets, wearables, camera, location, sensors, background tasks and push notifications only when relevant. Request device permissions just in time, explain why, and provide useful denial states. Respect platform privacy controls and avoid background behavior users cannot understand or stop.

## Native lifecycle, synchronization, and form factors

### When to use
Use for mobile web, React Native, Flutter, platform-native applications, tablets, foldables, or store delivery. Preserve the existing framework unless constraints justify a change.

### Core principles
Model lifecycle interruptions and platform permissions as normal events. Screen width is not device identity. Shared code does not eliminate platform-specific behavior.

### Step-by-step procedure
1. Inventory target OS versions, device classes, input methods, network constraints, secure storage, background limits, and release channels.
2. Specify compact/large phones, folded/unfolded posture, hinge occlusion, dual-screen behavior, tablets, split view, rotation, stylus, and software-keyboard behavior where targeted.
3. Preserve drafts, navigation, selection, and focus across resizing and lifecycle changes. Do not assume a background process survives.
4. Queue offline mutations with client operation IDs, conflict policy, visible sync state, and server deduplication. Reconcile after reconnect and expired authorization.
5. Treat push delivery as best effort, not durable business truth. Verify deep links, revoked permission, duplicate notifications, and notification-to-record authorization.
6. For store releases, verify signing ownership, build/version codes, privacy declarations, permission explanations, review assets, staged rollout, and rollback limits.
7. Test on actual representative devices; mark emulator-only coverage as such.

### Checklist
- [ ] Safe areas and the virtual keyboard do not hide focused controls.
- [ ] Zoom/text scaling, RTL, orientation, and split-screen preserve the core task.
- [ ] Offline deletion/conflict behavior is explicit.
- [ ] Signing material never enters source control.

### Common failure modes
Fixed viewport heights break keyboards; foldable hinges obscure controls; a push is treated as a commit; app-store rollback cannot instantly remove every installed version; local caches retain sensitive data after logout.

### Concrete examples
For installed toolchains use `flutter doctor`, `flutter test --help`, or inspect React Native project scripts with `npm run`. Check Android device access with `adb devices` only when ADB is available and device access is authorized. Test a draft begun in portrait, resized into split view, backgrounded, and resumed with the same text and valid focus.

### Verification
Use the [platform matrix](../references/platform-compatibility-matrix.md) to record device, OS, posture, viewport, density, input, text scale, network, and lifecycle results. Store release readiness remains unverified until the target signing/build pipeline runs.

### Related skills
[Offline experiences](offline-and-resilient-experiences.md), [frontend](frontend-engineering.md), [accessibility](accessibility-and-internationalization.md).

## Applied verification

Suspend the app during a save, rotate or fold the device, and resume after credentials expire. Confirm input and server outcome reconcile without duplicate actions or exposing one user’s cached data to the next.

## Release and local-state compatibility

## Termux/PRoot and desktop-site browser checks

Record native Termux and Linux-guest toolchains separately; shared source does not make their executables or Python environments interchangeable. Before a source update, back up the replaced files, verify the archive and resulting inventory, and preserve wallets, journals and private configuration. Inspect a relocated environment's console-script prefixes before reinstalling dependencies.

SSH access proves terminal/backend access, not browser control. Android Wireless debugging may need Wi-Fi and local pairing. If that path is unavailable, continue supported native checks and a clearly labeled manual browser check rather than inventing device automation evidence. Keep pairing credentials off chat and logs.

A mobile browser's desktop-site mode can report a desktop user agent and use a wider logical viewport. Do not classify physical hardware solely from a user agent or viewport. Record the actual device, backend location and manual/automated evidence separately. Check initial and locked pages at their intended top position, long monetary values and addresses, keyboard states, reconnect and native app switching. Browser emulation and process death do not prove physical flash/power behavior.

Treat device-local schema migrations and server API compatibility as separate rollout constraints: old installed clients may remain active for months. Test keyboard/safe-area insets, OS background restrictions, local storage eviction, interrupted sync and expired credentials. Certificate pinning requires a workable rotation/recovery plan. Use staged release controls and observable crash/upgrade behavior appropriate to the project’s distribution channel.
