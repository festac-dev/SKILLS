---
name: motion-studio
description: Create animated landing pages, scroll animations, motion graphics, kinetic typography, animated diagrams, product demos, launch/explainer and voice-over videos. Use for Remotion, GSAP, Framer Motion, Three.js, Lottie, or requests to make an experience feel alive, premium or cinematic when motion is an intended deliverable. Do not trigger for plain static pages, simple CSS tweaks or still images.
---
# Motion Studio

Motion is designed, not sprinkled. Give every animation a purpose: guide the eye, show causality, build hierarchy, or create rhythm. Never ship a static result when motion was requested. A still dashboard with a slow zoom, a repeated card layout, or a sequence of centered titles does not meet an advanced-motion brief.

## Route the actual request

| Mode | Read these exact references |
| --- | --- |
| Animated frontend page | [motion-principles](references/motion-principles.md), [design-system](references/design-system.md), [frontend-motion](references/frontend-motion.md), [qa-checklist](references/qa-checklist.md) |
| Rendered demo or explainer | [motion-principles](references/motion-principles.md), [design-system](references/design-system.md), [video-remotion](references/video-remotion.md), [audio-pipeline](references/audio-pipeline.md), [qa-checklist](references/qa-checklist.md) |
| Motion component or graphic | [motion-principles](references/motion-principles.md), [frontend-motion](references/frontend-motion.md), [qa-checklist](references/qa-checklist.md); add the video route for a rendered export |
| Combined web and film | Both relevant routes; share identity and tokens, but compose separately for interaction and a fixed timeline |
| Remotion cannot run | Read [video-fallback](references/video-fallback.md); verify the actual failure and use deterministic browser capture, or Manim for technical diagrams |

Read only relevant resources. Sample repository URLs, products, metrics and source files in a prompt are references unless the user makes them the task. Preserve the current project and earlier corrections.

## Core workflow

1. **Inspect reality.** Read project instructions, README, relevant docs, entry points, CLI/API definitions, config, source and tests. Exercise safe representative operations. Bind every visible claim, command, diagram and number to real code or captured output. Label fixtures and reconstructions; never invent capabilities, endorsements, metrics or successful integrations. Preserve the project's source when the assignment is capture-only.
2. **Set the visual system.** Derive one tight palette from the brand; absent a brand, start with the restrained dark palette in the design reference. Use one display family plus one mono family and an 8px spacing grid. Preserve a supplied identity. Numerical optical corrections are deliberate exceptions, not random spacing.
3. **Define the motion language before implementation.** Use [motion-tokens.ts](templates/motion-tokens.ts) for entrance easing, movement easing, spring configs, durations and stagger. Tune this one owner and reuse it. Keep the decisions in code; do not create a planning document.
4. **Choreograph.** Give every scene one hero moment and subordinate the rest. Define its start, focal action, readable state and handoff. Carry a real object through matched transitions. For siblings, change composition, subject, camera path and rhythm as well as color. A text panel plus a rotating primitive repeated for the whole film is not a finished direction.
5. **Build a representative moving sequence.** Verify the renderer, fonts, one complex transition and readable detail before expanding. For film, synthesize/import speech first and derive the timeline from actual words. For a frontend, test viewport entry, scroll reversal, touch and reduced motion before adding sections.
6. **Build the rest, then run the mandatory QA loop.** Inspect real pixels and runtime behavior, fix observed defects and re-render affected scenes. A compiler pass, a contact sheet or an audio waveform alone cannot establish the complete experience.

## Concrete motion bar

- Entrances use a damped spring or ease-out-expo; movement between positions uses ease-in-out. Linear is reserved for progress, clocks and continuous loops.
- Default stagger: 40–90ms. UI transitions: 200–500ms. Hero reveals: 600–1200ms. Time values are tokens, not scattered literals.
- Animate DOM transform and opacity; measure once, batch reads/writes and avoid animating layout. SVG stroke drawing, canvas and GPU geometry use their own rendering APIs and require separate cost checks.
- Build camera pushes, parallax depth and object-continuous transitions. Avoid hard cuts. Reframe important artifacts at a readable size; do not fit an entire dense workspace into a postage stamp.
- Animate code with a real syntax tokenizer and time typing to spoken cues. Diagrams draw edges and activate nodes in causal order. Terminals show actual captured output or an explicitly identified reconstruction of existing tests/docs.
- Use glow, grain and depth sparingly. Do not substitute decorative effects for a meaningful moving subject. Keep graphics alive through staged transformations; do not let a film sit on an unchanged composition for more than two seconds.

## Frontend contract

Use scroll-driven choreography, smooth navigation, hover **and focus** feedback, route continuity, and real loading/skeleton states when those states exist. The starter provides entry reveals, a transforming hero, scroll-driven layers, magnetic pointer feedback and its keyboard equivalent.

Target 60fps: at 60Hz the whole frame has 16.7ms. Report the measured environment; a software browser is not a hardware-GPU benchmark. Reserve media dimensions and prevent layout shifts. Keep controls responsive while transitions run. Support 320px screens, zoom, keyboard and accessible contrast.

Honor `prefers-reduced-motion`, including changes while mounted: present a composed static state and remove long pinned scroll distances. This accessibility fallback does not permit a static default when motion was requested. Pause work offscreen and when hidden. No autoplay sound on webpages. No playback bars, speed sliders, step selectors or rotation toolbars for decorative page motion unless the user requested them; use scrolling, viewport entry, pointer or automatic choreography.

## Video contract

Default to **1920×1080, 60fps, H.264 at a measured high bitrate** (start at 20–30Mbps), BT.709 limited range and `yuv420p`, with fast-start metadata. Respect an explicit destination or length; a launch film commonly runs 60–90 seconds. Remotion is the first choice; use the documented fallback if its renderer cannot run reliably.

Conversational, confident VO: under 150 words per minute, one idea per sentence, specific verbs, no buzzwords. Use actual word timestamps; a character-count estimate is not alignment. Tie every meaningful scene action, type reveal, diagram edge and transition to word cues. Derive frames once with `round(seconds * fps)`. Provide burned-in captions and an `.srt`, unless the user explicitly permits only the single MP4.

Match the audience. Hackathon and launch films close on the product, its value and a real public destination when available. Keep localhost addresses, internal setup commands and production labels out of those films. Install commands belong in a developer tutorial when requested. Preserve brief disclosures that materially distinguish simulated data, ledger accounting or mock transactions from real outcomes.

Mix a subtle, audible ambient bed, sidechain-ducked below speech, with light whooshes and material/interaction clicks. Measure the bed separately so it does not disappear on ordinary listening levels. Master in two passes to **−14 LUFS**, with encoded true peak no higher than **−1 dBTP**. Use authorized original or licensed sound. Listen to the complete mix where audio review is available; accurately disclose a missing listening check rather than certifying it from numbers.

## Autonomy and workspace

Proceed without questions or approval gates when the brief supplies enough to act. Resolve reversible choices with judgment. Do not create BRIEF, SCRIPT, planning or report documents unless the user requests them. Working code, machine timing data and essential test evidence belong in the dedicated work folder; final delivery contains only requested artifacts.

Use free tools and free/offline TTS when keys or a confirmed included allowance are absent. **Never spend money.** Key presence is not proof of a zero-cost request. OpenAI has no general free TTS entitlement; do not call it under this default. ElevenLabs may be used only with an inspected free plan, sufficient included quota and overage disabled. Reuse already authorized recordings where suitable. Never silently substitute robotic speech and call it professional.

Install required tools in the dedicated folder where possible; keep credentials in environment or non-echoing input, never source, logs, video metadata or the ZIP. Commit nothing. Save completed render chunks atomically and resume them after interruption; never regenerate narration merely because a session restarted. Verify source/timeline fingerprints before reusing a chunk.

## Mandatory QA loop

Read [qa-checklist](references/qa-checklist.md). Render, extract frames just before and after **every** scene boundary and at complex intermediate states, inspect overflow/clipping/contrast/grid alignment, then check continuous motion, sync and sound. Verify full decoding and final metadata. For web, exercise keyboard, touch, reverse scroll, resize, hidden-tab recovery and reduced motion. Fix defects and re-render affected work until required checks are clean. Mark unavailable subjective or hardware checks honestly; do not label an unobserved check passed.

Helpers: [extract_frames.sh](scripts/extract_frames.sh), [loudnorm.sh](scripts/loudnorm.sh), [duck_mix.sh](scripts/duck_mix.sh), [tts.py](scripts/tts.py), [check_contrast.py](scripts/check_contrast.py). Sampled pixel contrast checks supplement authored color checks; they are not an automatic WCAG audit of an entire frame.

## Avoid

Fade-in-everything; gratuitous bounce; motion that blocks reading or input; incompatible easings; centered-text slideshows; stock gradients; tiny screenshot collages; long unchanged holds; generic floating cards offered as advanced graphics; invented command output; premature success states; guessed word times; inaudible music; SFX that bury speech; and animation that ignores reduced motion.
