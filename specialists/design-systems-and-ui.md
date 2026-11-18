# Specialist: Design Systems and UI Engineering

Audit existing tokens, components, patterns, accessibility and implementation before creating or changing a system.

A design system may include semantic tokens, typography roles, spacing, sizing, layout constraints, component APIs, states, responsive rules, motion rules and documentation. Include only what the product needs.

Do not hard-code a universal palette, font, radius, shadow, grid, card style or component library. Prefer semantic, contextual tokens and preserve existing conventions. Ensure components are usable, composable, documented and tested. Avoid token proliferation and abstraction without reuse.

## Applied verification

Inspect tokens and component states in the rendered app, including dialogs, tables, toasts and mobile navigation. Use semantic roles for colors, keep focus and status contrast legible, and fix the component causing overflow instead of hiding clipped content at the page root.

## Theme options when in scope

Use the existing theme provider and storage convention where available. Apply the stored choice before the first painted frame, follow system preference when no explicit choice exists, and keep the visible control, root state and rendered surfaces synchronized across routes. Storage being unavailable should not prevent a local toggle from working. Give the control an accessible name and state; verify keyboard activation and persistence after reload.

Theme semantic roles rather than applying a blanket invert filter. Check raised surfaces, inputs, hover/selected/disabled states, status colors, dialogs, charts, SVG marks and canvas scenes in both modes. Maintain the project's identity while adapting contrast; a bright accent may need different text-on-accent and text-accent roles. Do not introduce theme switching or mandate a dark palette in unrelated briefs.

## Replacing product templates

When a brief requests distinct templates for sibling products, change the composition and information hierarchy as well as the skin. Start with each product's primary object and decision: a dossier may benefit from an index and evidence sequence, an assembly from proposals and participant responsibilities, and a purchase tool from a decision pipeline. These are examples, not prescribed layouts. Preserve real actions, permissions, deep links and working states while moving them into the new composition.

Review sibling pages together at desktop and narrow widths. Distinction should remain visible without relying on the logo or accent color. Check source order, keyboard order, primary action visibility, long content and both requested themes. Keep motion integrated with the page hierarchy; a new frame should not hide labels, crop the scene or turn decorative indicators into misleading controls.

## Consistency without interchangeable templates

Share semantic tokens, interaction contracts and accessibility primitives where they help. Let each product's composition, navigation, density and dominant object reflect its own task. Before coding sibling pages, compare a simple silhouette and content order; a color swap and a different scene inside the same card are not a template change.

Keep artwork, logos and illustrations aligned with the product's existing visual grammar. Choose optical spacing and type hierarchy in the rendered result. Verify long labels, real populated content, narrow layouts, both requested themes and state changes; a polished empty mockup is insufficient. Use the [direction brief](../templates/VISUAL_DIRECTION_AND_MOTION_BRIEF.md) only for changes that benefit from explicit coordination.

## Token and component ownership

Separate semantic token roles from primitive values so themes and densities can change without per-component forks. Use the existing token pipeline; DTCG-compatible interchange can help when multiple design/build tools need to share values. A component workbench is useful when it exposes real loading/error, focus and disabled behavior, not merely static swatches. Deprecation belongs with the documented component contract.
