# User Experience and Content Gate

- [ ] Critical user journeys are complete and coherent.
- [ ] Navigation and information hierarchy match user tasks.
- [ ] Empty, loading, error, success, offline, and permission states are considered.
- [ ] Copy is specific, natural, honest, and actionable.
- [ ] Responsive and platform behavior is intentional.
- [ ] Keyboard, screen-reader, contrast, zoom, and reduced-motion needs are tested.
- [ ] No decorative effect or interaction obstructs the task.
- [ ] Research findings and usability issues are addressed or documented.

## Screen and input evidence

### When to use
Apply to changed critical interfaces and their declared supported environments.

### Core principles
A layout passes only when the user can complete the task with the required input and accessibility settings.

### Step-by-step procedure
1. Select required rows from the screen inventory.
2. Exercise each critical action, relevant failure, resize, text scale, and input alternative.
3. Check focus recovery, state continuity, content access, and shared-session privacy.
4. Record passed, failed, unverified, or not applicable using the gate protocol.

### Checklist
- [ ] Touch, keyboard, mouse, and specialized input work where required.
- [ ] Zoom/reflow and localization do not hide essential information.
- [ ] Unsupported hardware capabilities have tested alternatives.
- [ ] Terminal interfaces also satisfy their keyboard and plain-output contracts.

### Common failure modes
Visual approval replaces usability testing; unavailable hardware is marked passed; hover-only actions exclude touch and remote users.

### Concrete examples
Attempt the primary journey using keyboard only at high zoom. On a TUI, complete the same operation with mouse disabled and through the non-interactive command when provided.

### Verification
Release claims match the tested coverage matrix. Unverified required environments remain a stated gap.

### Related skills
[Screen inventory](../templates/SCREEN_AND_STATE_INVENTORY.md), [platform coverage](../references/platform-compatibility-matrix.md), [CLI/TUI](../specialists/cli-and-tui-engineering.md), [gate protocol](GATE_PROTOCOL.md).

## Application evidence

Verify requested autoplay at two elapsed times without a hover or click prerequisite, and check reduced-motion behavior separately. Inspect narrow layouts, focus and toast/dialog contrast; report the limits of automated accessibility scans.
