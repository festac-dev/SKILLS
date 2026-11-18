# Specialist: Frontend Engineering

Preserve the existing stack and conventions unless evidence justifies change. Build accessible, responsive, resilient interfaces with real interactions and clear component boundaries.

Check loading, empty, error, success, disabled, permission-denied, offline and partial-data states as relevant. Handle focus, keyboard, touch, semantics, form validation, route transitions and reduced motion. Avoid unnecessary client-side complexity, oversized bundles, layout shifts and decorative effects that reduce usability.

## State, forms, responsive behavior, and measured delivery

### When to use
Use for interactive pages, client data flows, forms, or layout changes. Load platform coverage when the product targets more than ordinary browser windows.

### Core principles
Keep server data, URL state, local interaction state, and persisted drafts distinct. The server owns authorization and durable truth. Use native semantic controls by default. Choose breakpoints where content fails, not from a universal device list.

### Step-by-step procedure
1. Map every state to an owner and reset/persistence policy. Prevent stale requests from overwriting newer results through cancellation or request identity.
2. Make labels, validation, submission, duplicate prevention, pending feedback, and focus recovery explicit. Preserve safe input after errors.
3. Specify layout changes for content width, zoom, long text, RTL, virtual keyboard, and split-screen. Use container queries only where component context requires them.
4. Keep essential actions reachable by keyboard and touch. Test actual tab order and announcements, not only automated rules.
5. Profile representative mobile hardware/network. Measure field Core Web Vitals where available: LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1 at the 75th percentile are reference targets; verify current guidance and separate lab diagnostics from field evidence.
6. Check lazy loading, image dimensions, hydration, bundle cost, font loading, and long tasks against observed bottlenecks.

### Checklist
- [ ] Loading, empty, failed, denied, interrupted, and success states have real behavior.
- [ ] Zoom/reflow and text expansion retain content and actions.
- [ ] Client validation is repeated at trusted server boundaries.
- [ ] No accidental horizontal page scroll or focus loss at layout transitions.

### Common failure modes
One global state store obscures ownership; disabled buttons without explanations trap users; race responses overwrite edits; viewport-only layouts fail in split panes; desktop Lighthouse scores do not prove mobile field performance.

### Concrete examples
A resilient component rule:
```css
.results { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr)); gap: 1rem; }
.article { max-inline-size: 70ch; overflow-wrap: anywhere; }
:focus-visible { outline: 2px solid currentColor; outline-offset: 3px; }
```
Inspect installed tooling with `npm run`; use its existing checks. Test widths just below and above each observed content breakpoint, plus 200% text and 400% browser zoom.

### Verification
Record viewport, input, browser, locale, assistive technology, network/device profile, and actual results. No screenshot alone proves keyboard usability or performance.

### Related skills
[Platform coverage](../references/platform-compatibility-matrix.md), [accessibility](accessibility-and-internationalization.md), [mobile](mobile-and-device-experiences.md).

## Applied verification

Deep-link to a populated route, refresh, resize while a menu or dialog is open, and navigate back. Check request failures and long content without root-level clipping; inspect the same built assets that the preview serves.

## Platform options

Use [platform feature guidance](../references/modern-web-platform-features.md) to assess container queries, popovers, view transitions, content visibility and off-main-thread drawing against the browser support policy. Keep a working fallback for navigation and input. Check image dimensions/srcset, font loading, route splitting and error telemetry on the delivered artifact using [web performance guidance](../references/web-performance-and-delivery.md).

## Capacity and interruption feedback

Show the requested, available and unmatched quantities when a task exceeds current capacity. Offer the choices the product actually supports, such as partial completion, waiting or stopping, and explain independent outcomes. Do not silently change amounts, substitute resources or report a draft as completed work.

Make the primary information and its next actions easy to find. Preserve appropriate drafts across resize and reconnect, and distinguish saved intent from committed results. Close sensitive reviews when authorization or workspace access changes. Examples depend on the domain: stock allocation, file import batches and financial orders have different units and recovery evidence.

For batch entry, distinguish the selected source resources from the recipient rows. When the brief requests manual entry, pasted CSV and file upload, route them through the same validation and review model. Supply a sample matching the actual parser, preserve useful drafts when changing entry modes, and validate the entire import before replacing existing rows. Errors should identify the row and field without silently dropping invalid data.
