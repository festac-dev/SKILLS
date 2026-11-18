# Standout Experience Techniques

A catalogue for making a product memorable **for its real audience**. Nothing here is mandatory, and generic application is the opposite of the goal. Pick one or two signature qualities, execute them with craft, and keep everything else quiet.

## How to find the signature
1. **Subject truth**: what is this product's real subject (freight moves, music breathes, money is trust, code is structure)? Let that drive form and motion.
2. **Audience moment**: where do people feel friction, anxiety, pride or delight? Invest there.
3. **Unfair advantage**: unique data, domain expertise, access, craft, speed. A standout product shows what only it can show.
4. **Constraint as style**: a tight palette, one typeface, a single interaction model, a strict grid, an unusual medium (terminal, print, audio).
5. **Memorability test**: can a user describe it to a friend in one sentence? Would a screenshot be recognizable without the logo?

## Technique families
### Interaction and feel
- Direct manipulation: drag, scrub, pinch, shape things instead of filling forms.
- Weighted motion: springs, inertia, anticipation, overshoot tuned to the object's "mass".
- Micro-feedback: optimistic UI, haptics, sound, state changes that confirm every action within 100 ms.
- Keyboard-first power paths: command palette, shortcuts, undo/redo everywhere, scriptable actions.
- Forgiveness: undo instead of confirm dialogs, drafts, versioning, safe defaults.

### Information and storytelling
- Data as the hero: live, real data visualized with purpose (maps, timelines, flow diagrams, small multiples).
- Scroll narratives with real state change (pinned scenes, progressive reveals) that survive reduced motion as plain sections.
- Explorable explanations: sliders and toggles that let people *see* a concept change.
- Personalized "this is yours" moments built from the user's own data (summaries, timelines, comparisons), privacy-respecting.

### Visual identity (only when the project invites it)
- Generative or parametric identity that varies with data or time of day.
- Custom illustration or iconography with consistent construction rules.
- Typography with a clear point of view, tuned optical sizes, variable-font expression, true tabular numerals where data matters.
- Color systems built in a perceptual space (OKLCH) with accessible pairings by construction.
- Materials and depth used sparingly and consistently (not a pile of glass, glow and gradients).

### Sensory and spatial
- Sound design: subtle, optional, event-linked cues; never autoplay; always a mute.
- 3D that carries meaning (product configurators, globes with real data, spatial UI), with a 2D fallback.
- Cursor and pointer craft: magnetic targets, contextual cursors, spotlight reveals, proximity effects; with touch and keyboard equivalents.
- Shader or canvas "living" backgrounds tied to state (load, activity, time), paused when idle.

### Systems and speed
- Performance as a feature: instant navigation (prefetch, view transitions), skeleton-free fast paths, offline-first behavior, local-first editing.
- Reliability as a feature: visible status, graceful degradation, honest error messages, resumable uploads.
- Craft in the unglamorous places: empty states that teach, error states that help, loading states with progress, settings that explain.
- Developer experience as a product: great docs, copy-paste examples, a playground, a CLI, a type-safe SDK, transparent changelogs.

### Voice and trust
- A specific, human voice documented in a short guide; real examples instead of slogans.
- Radical clarity: pricing, limits, data use and security stated plainly.
- Proof over claims: live status page, public roadmap, open benchmarks, case data with permission.
- Small signs of care: considerate defaults, accessibility as a baseline, considerate notifications.

## Project-type ideas (adapt, reject freely)
| Project | Candidate signature ideas |
|---|---|
| SaaS dashboard | Time-travel scrubber over metrics; command palette; annotated charts; "explain this number" popovers |
| Developer tool / API | Live request playground; generated typed SDKs; interactive architecture diagram of the user's own setup |
| E-commerce | Fast filtering with instant feedback; accurate 3D/AR viewers; transparent shipping/returns up front |
| Portfolio / studio | One memorable interaction tied to the discipline; case studies with real outcomes; swift load |
| Education | Explorable simulations; adaptive pacing; progress that celebrates real mastery |
| Fintech | Clarity of money flows (Sankey/ledger views), visible safeguards, calm, trustworthy motion |
| Health / wellbeing | Gentle, low-stimulation interaction; accessible by default; privacy controls surfaced early |
| Media / publishing | Typography-led reading experience; scroll-driven annotated visuals; audio companions |
| Games / toys | Systemic feel (juice) tuned for responsiveness; modding hooks; shareable moments |
| Infrastructure / ops | Beautiful, honest status and topology views; flow animation mapped to real throughput |
| CLI / TUI | Mouse-aware TUI panels, great help text, themes that respect the terminal, fast startup |
| Internal tools | Ruthless speed, keyboard flow, bulk actions, audit trails, thoughtful permissions |
| Open-source library | Superb README, runnable examples, tiny API surface, benchmarks, migration guides |

## Anti-patterns (generic "AI-looking" or empty polish)
Gradient orbs and glassmorphism by default; identical card grids; stock three-column feature rows; unexplained particles; fake testimonials or metrics; auto-playing hero video; scroll-jacking; effects that hide content or block input; copy such as "unlock the power of"; dark-pattern urgency; motion without a reason; heavy libraries for light effects.

## Quality bar for any signature element
It serves a user goal or expresses the subject truthfully; it is distinctive in context; it is accessible (keyboard, screen reader, reduced motion, contrast); it is performant on a mid-range phone; it has a graceful fallback; it is maintainable; and it can be explained in one sentence.

## Process
Fill `templates/STANDOUT_OPPORTUNITY_REGISTER.md`, prototype the top idea in a small spike, test with real users or stakeholders, measure cost (bundle, frame time, accessibility), then keep, simplify or drop it. Gate: `quality-gates/DISTINCTIVENESS_AND_CRAFT_GATE.md`.
