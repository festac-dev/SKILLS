# Motion and Interactive Graphics Gate

- [ ] Every moving element has a stated purpose (explain, guide, confirm, express).
- [ ] The static composition works without motion.
- [ ] `prefers-reduced-motion`, touch, keyboard, low-power, and no-JS/no-WebGL behaviors are defined and tested.
- [ ] Scroll, viewport, pointer or autoplay behavior matches the brief without unrequested animation controls.
- [ ] No flashing above safe thresholds; no vestibular-heavy full-screen motion by default.
- [ ] Text remains readable over every frame; contrast checked.
- [ ] Pointer effects use pointer events, smoothing, and do not block clicks or hide essential cursors.
- [ ] One render loop; paused offscreen and when the tab is hidden.
- [ ] Frame pacing measured on representative devices; memory stable over several minutes; resources disposed.
- [ ] Asset and bundle weight within budget; heavy libraries lazy-loaded.
- [ ] Motion tokens (duration/easing/spring) are consistent.
- [ ] Flowing connections/data motion encode real information and include a legend or accessible equivalent.
- [ ] Requested behaviors (rotation, moving layers, flowing connections, cursor response) actually run in a real browser, evidenced by recordings and frame-rate numbers.
- [ ] Fallbacks for no-WebGL and low-power verified.
