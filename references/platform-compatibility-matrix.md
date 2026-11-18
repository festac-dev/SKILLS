# Platform Compatibility Matrix

| Platform/device | Supported versions | Input methods | Accessibility tech | Storage constraints | Network assumptions | Unique capabilities | Test owner |
|---|---|---|---|---|---|---|---|
| Web desktop | | | | | | | |
| Web mobile | | | | | | | |
| iOS | | | | | | | |
| Android | | | | | | | |
| Windows | | | | | | | |
| macOS | | | | | | | |
| Linux | | | | | | | |
| Embedded/IoT | | | | | | | |

Only list platforms that the product intends to support. Define graceful degradation and explicit unsupported behavior.

## Form-factor and multi-input coverage procedure

### When to use
Use when specifying supported screens, windows, inputs, accessibility behavior, or compatibility tests. Support selected environments based on user need; do not claim every device is supported.

### Core principles
Separate physical form factor, logical viewport, density, input, viewing distance, posture, and device capability. A high-resolution display does not necessarily need a different layout. Essential controls must not rely on hover, color, motion, or mouse input alone.

### Step-by-step procedure
1. Select support tiers: required/tested, best effort, or unsupported with a useful alternative. Record why each environment matters.
2. Specify behavior by content constraints: navigation transformation, columns, text measure, overflow, master/detail, modal placement, and state preservation.
3. Cover the relevant families below:
   - Compact/large phones: one-handed reach, keyboards, safe areas, portrait/landscape, text scaling.
   - Foldables/dual screens: posture, hinges, occlusion, continuity, and unsupported capability fallback.
   - Tablets/split-screen: resizable windows, master/detail, stylus, keyboard, drag/drop alternatives.
   - Laptops/desktops: narrow windows, keyboard shortcuts, mouse, high density, portrait monitors.
   - Ultrawide/4K–8K/multi-monitor: bounded reading width, useful density, independent windows, per-display scaling; avoid stretching content indiscriminately.
   - TVs/streaming/projectors/signage: viewing distance, remote/D-pad focus graph, safe margins, low contrast environments, unattended recovery.
   - Kiosks/POS/public displays: large touch targets, gloves where relevant, explicit completion, session timeout/reset, privacy, peripheral failures.
   - Wearables/e-ink: glanceable content, tiny round/rectangular screens, low refresh, battery, hardware buttons, no animation-dependent status.
   - Automotive/industrial/embedded: distraction and safety constraints, physical controls, latency, sunlight, fixed hardware, approved platform rules.
   - Gaming/spatial: controller focus, text legibility, comfort, depth, seated/standing contexts, non-spatial alternatives.
4. Define touch, mouse, keyboard, stylus, remote, controller, and assistive-technology paths. Detect capabilities rather than inferring input solely from width.
5. Test zoom, text scale, long translations, RTL, orientation, resize during interaction, input changes, reduced motion, high contrast, and slow/offline states.
6. Record real device versus emulated evidence and unresolved support gaps.

### Checklist
- [ ] No essential hover-only or drag-only action.
- [ ] Focus order and visible focus survive layout changes.
- [ ] Public/shared sessions clear sensitive state.
- [ ] Canvas/media buffers respect memory and density budgets.
- [ ] Unsupported capabilities produce an explicit usable alternative.

### Common failure modes
Shrinking one desktop layout fails touch/TV use; a pixel-width matrix misses input; e-ink refresh obscures loading; monitor changes break fixed positioning; a kiosk keeps the previous user's account; a controller cannot escape a modal.

### Concrete examples
Test a booking form at 320 CSS pixels and with 400% desktop zoom, allowing exceptions only for content that genuinely needs two-dimensional layout. For a TV flow, traverse every action using only directional input and select/back. For a multi-monitor app, move its window between displays with different scale factors while a dialog is open.

### Verification
For each required journey record form factor, OS/browser/runtime, viewport, density, input, locale, zoom/text scale, expected adaptation, actual result, and evidence. Inspect boundaries immediately below/above each content breakpoint. Emulator coverage alone does not verify remote, stylus, e-ink, GPU, or assistive-technology behavior.

### Related skills
[Screen/state specification](../templates/SCREEN_AND_STATE_INVENTORY.md), [mobile](../specialists/mobile-and-device-experiences.md), [frontend](../specialists/frontend-engineering.md), [accessibility](../specialists/accessibility-and-internationalization.md).

## Application evidence

Record browser viewport emulation separately from actual-device evidence. Test content-driven widths, zoom and long values, including narrow 320px web layouts where supported; diagnose the overflowing element instead of suppressing all page overflow.
