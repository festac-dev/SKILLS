# Learning from Visual References

Use when a user provides websites, screenshots, videos, carousels or a design collection as inspiration. Skip media retrieval for a routine fix that does not depend on a reference. Brand direction owns identity; UX owns journeys; motion owns implementation; video production owns exported films.

## Inspect the actual material

Resolve shared links and identify whether each target is a post, carousel, profile or repository. Remove duplicate share links and app-install promotions from the worklist. Use available, authorized tools; `yt-dlp` can retrieve many public videos, but an extractor failure does not prove that a post is a video or that an account is private. A photo post may expose only its backing audio through a video extractor. Inspect its public image metadata and retrieve the ordered slides instead. Do not substitute audio, a thumbnail or a title for the carousel.

Keep a bounded inventory: source, media type, accessible material, inspected timestamps or slide range, and gaps. For a profile, state the sampled date/range and selection; inspecting recent posts is not a review of the entire account. Inspect opening, major transitions, resting states and ending; expand sampling where motion is unclear. Review every retrieved carousel slide in order. Read small text at native resolution. Listen to the audio when drawing conclusions about sound, timing or narration.

If access fails, try a suitable public retrieval path, then report the actual gap. Do not invent observations, infer hidden functionality from a screenshot, or bypass access restrictions. For repositories, inspect the live result or previews alongside relevant source, dependency versions and license terms. A repository license may not cover photographs, fonts, music or third-party effects.

Delete downloaded media and derived frames when the user requests cleanup. Keep only the requested deliverable and concise findings; do not embed signed CDN URLs, account cookies, tracking parameters or copies of source media in a reusable skill.

## Separate observation from interpretation

For motion-led work, distinguish continuous playback, timed frame inspection, isolated screenshots and audio listening in the evidence record. State the actual method before claiming a reference was reviewed. A contact sheet can reveal poses and cuts, but sparse samples cannot establish easing, fluidity, interaction latency or audiovisual synchronization. If continuous playback is unavailable, say so and inspect denser timestamped sequences around the transitions that drive the design decision. Do not describe that fallback as watching the full video.

Separate motion inside the demonstrated product from camera movement, editing and overlays in the recording. Record the initiating input, starting composition, transition interval, hold, resulting composition and reverse/reset behavior. Identify whether the visible method uses live geometry, a fixed rendered sequence, ordinary DOM motion or an unverified technique. An image-to-video tutorial can establish the creator's demonstrated workflow without proving its implementation or performance on every device.

Record what is visible before deciding why it works. Useful dimensions include:

| Dimension | Observe | Translate into a project decision |
|---|---|---|
| Composition | Focal object, occupied space, text/image overlap, alignment, negative space | Which real product object deserves attention, and where the primary action remains reachable |
| Hierarchy | Reading sequence, type roles, contrast, section rhythm | What the user needs first, next and only on demand |
| Motion | Start/hold/end, trajectory, layer separation, camera, timing, reset | A specific sequence with a meaningful result and a readable rest state |
| Interaction | Scroll, pointer, click, keyboard, touch, visible feedback | An input contract that works beyond the recorded device |
| Craft | Materials, light, crop, depth, typography, sound | A small set of coherent choices, with appropriate asset and rendering methods |
| Journey | Discovery, selection, detail, confirmation, recovery | Real destinations, permissions and complete task flow |

A car exploding into parts can suggest revealing a product's structure. It does not require adding a car, explosions or 3D to every project. A fast-cut film suggests editorial pacing; it does not justify flashing a working dashboard. A polished mobile mockup shows a proposed hierarchy, not proof of a working checkout. Advertised prices, model capabilities, customer counts and performance claims remain unverified reference content.

## Turn a reference into an acceptance brief

Choose the transferable principle, the product object it serves, and the observable behavior to implement. Note what cannot be transferred because of task, licensing, accessibility, device or data constraints. Use the optional [direction brief](../templates/VISUAL_DIRECTION_AND_MOTION_BRIEF.md) when a substantial redesign needs coordination.

For sibling products, compare silhouettes, navigation, content order, density and dominant objects before colors or logos. If the pages remain interchangeable with their branding removed, revise the composition. Match each landing promise to a working workspace destination; a public introduction and an operational screen may share identity without sharing layout.

Select the rendering method from the effect:

- CSS/SVG for typography, interface transitions, logos, paths and modest layered diagrams.
- Real-time 3D for useful spatial inspection, changing geometry, camera control or live object state.
- Video or a frame sequence for a fixed cinematic shot when its memory, loading and seeking costs are acceptable.
- Original or licensed images for scenes whose detail is better represented as imagery.

Do not imply a rendered video is interactive geometry. Do not replace a requested detailed scene with generic primitives without evaluating the fidelity loss. Do not load hundreds of full-resolution frames eagerly; estimate decoded memory as width × height × four bytes × resident frames, then bound the working set.

## Review and reuse

Compare the implementation with the stated principle at desktop and narrow widths, including a populated journey, motion phases, keyboard/touch behavior, reduced motion and failure fallback. A successful build or two different screenshots establishes only part of the result. Evaluate framing, readability and continuity directly.

When a user says the result still feels the same, compare the reference and implementation at the level they are judging: dominant subject detail and scale, changing page composition, motion path, depth, camera, timing and relationship to scrolling. Recoloring primitives, increasing a rotation or adding another loop does not resolve a mismatch in those dimensions. Use a representative rendered sequence to validate the revised direction before propagating it across sibling products or running expensive full builds.

Combine several references by assigning each a purpose: one may inform scene continuity, another typography and composition, another mobile list/detail behavior. Preserve those contributions explicitly instead of averaging them into one generic template. Transfer the useful behavior to actual product content; do not add a carousel, pinned scene or bottom navigation solely because it appears in an example.

When updating this toolkit, put reusable guidance in the existing owner. Keep product names, specific colors, copied slogans, example metrics and one-off timing out of general rules. Preserve counterexamples where a static, dense or conventional interface is the correct choice.
