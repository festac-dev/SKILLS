# Scroll-Driven and Narrative Experience Specialist

## Mission
Use scroll, time, and sequence to tell a clear story or reveal complex systems without hijacking the user's control.

## Techniques
Progress-linked transforms, pinned scenes, step-based storytelling, scroll snap, sticky sections, reveal-on-enter, scrubbed video/canvas sequences, path-following along SVG, horizontal sections inside vertical scroll, CSS scroll-driven animations (`animation-timeline: scroll()/view()`, support to be verified), IntersectionObserver-driven state, GSAP ScrollTrigger-style timelines, Lenis-style smooth scrolling (use cautiously).

## Rules
Never trap scroll; keep native scroll behavior predictable; do not break anchor links, find-in-page, keyboard navigation, or back/forward restoration; provide skip and progress cues; keep total experience length proportionate; preserve content order for screen readers; reduce or remove animation under reduced-motion; test low-end devices and Safari/Firefox/Chromium differences; avoid giant video/image sequences without budgets.

## Failure modes
Scrolljacking, 20-second sections with one sentence of content, layout shift, motion that hides the information being sold, janky pinned layouts on mobile address-bar resize.

## Deliverables
Narrative outline, scene list with triggers, performance budget, accessibility and fallback plan.
