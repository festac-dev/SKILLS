# Motion Accessibility and Safety Reference

- Honor `prefers-reduced-motion: reduce`: replace large movement, parallax, zoom, spin, and autoplay with static or minimal fades, including when the preference changes while the page is open.
- Follow the [motion specialist](../specialists/motion-3d-and-immersive.md) when choosing interaction behavior. Reduced-motion support alone does not establish WCAG conformance; assess applicable success criteria when accessibility conformance is in scope.
- Avoid vestibular triggers: large-area parallax, continuous zoom, rapid background motion, rotating full-screen elements.
- Keep text legible over motion: contrast measured against the worst frame.
- Do not convey information by motion alone; provide text/ARIA alternatives and a data table for data visualizations.
- Keyboard and screen-reader parity for any pointer-revealed content; maintain visible focus; do not trap focus in animated overlays.
- Touch: no hover-only functionality; 44×44 CSS px targets; avoid gesture conflicts with scroll and system gestures.
- Performance is accessibility: slow devices and low-battery modes should receive lighter experiences; honor `prefers-reduced-data` where available and Save-Data hints with care.
- Photosensitivity and seizure safety: avoid strobing and high-contrast flicker; test with analyzers when risk exists.
- Sound: never autoplay audio with sound; provide mute and respect system settings.
- Document the reduced-motion experience as a designed state, not an afterthought.

## Performance targets (adjust to the project)
Interactions respond within about 100 ms; animation holds close to 60 fps on a mid-range device or a lower stable rate by design. Cap devicePixelRatio, particle count, and draw calls; use instancing and texture compression. Pause when hidden or offscreen and release GPU resources on teardown. Lazy-load heavy scenes after core content and budget them in `templates/PERFORMANCE_BUDGET.md`. Test on a low-end phone, with the OS reduced-motion preference, keyboard-only, a screen reader spot check, and long-session battery/thermal sanity. Provide static or simplified fallbacks for no-WebGL, low-power, print, and error cases. Hide purely decorative animation from assistive technology.
