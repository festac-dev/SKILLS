# Screen and State Inventory

| Journey | Screen/route | User goal | Entry conditions | Main actions | Loading/empty/error/success states | Responsive/accessibility notes | Verification |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Include only screens and states relevant to the actual product. A marketing site, dashboard, sidebar, footer or settings page is not automatically required.

## Responsive behavior and screen evidence extension

### When to use
Use this existing inventory as the owner for responsive behavior and screen coverage instead of creating competing screen lists.

### Core principles
Specify how each critical journey adapts; do not record resolutions without behavior. Mark unsupported environments honestly.

### Step-by-step procedure
1. Identify supported form factors and inputs from actual users.
2. Add a row per meaningful adaptation, not every device model.
3. Define navigation, layout, overflow, focus, state continuity, and fallback.
4. Execute the critical journey on the required combinations and record evidence.

### Checklist
- [ ] Required, best-effort, and unsupported tiers are explicit.
- [ ] Zoom, text scaling, orientation, resize, and alternate input are covered.
- [ ] Shared-display privacy and specialized hardware limits are addressed where relevant.

### Common failure modes
A matrix lists devices but no acceptance behavior; screenshots omit focus; the same passing desktop test is copied into every row.

### Concrete examples
| Journey | Context/input | Adaptation | Expected evidence |
|---|---|---|---|
| Edit booking | Compact phone/touch + keyboard | Single column; focused field remains visible | Submit with keyboard open; no hidden error |
| Browse orders | Tablet split-screen/keyboard | Master/detail collapses; selection preserved | Resize during selection without data loss |
| Select programme | TV/remote | Visible directional focus and back path | Finish journey without mouse |
| Checkout | Shared kiosk/touch | Session clears after completion/timeout | Next user sees no prior identity |
| Read report | Ultrawide/mouse + keyboard | Bounded text width; useful data columns | Reflow/zoom keeps essential actions |

### Verification
Attach build/environment, procedure, result, and limitation for each required row. Use [the platform guide](../references/platform-compatibility-matrix.md) for broader families.

### Related skills
[Frontend](../specialists/frontend-engineering.md), [accessibility plan](ACCESSIBILITY_TEST_PLAN.md), [user-experience gate](../quality-gates/USER_EXPERIENCE_AND_CONTENT_GATE.md).

## Execution record

Keep only fields relevant to this artifact.

- Populated data, loading failure and deep-link refresh result:
- Viewport/zoom, open overlay and long-content result:
- Requested animation observed over time and reduced-motion result:
