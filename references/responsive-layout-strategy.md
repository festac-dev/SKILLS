# Responsive Layout and Breakpoint Strategy

Choose transitions when content or tasks need them—not because a device category has a fixed width.

Use fluid constraints, intrinsic sizing, wrapping, Grid/Flexbox, container queries where useful, semantic order, and content-driven breakpoints. Define minimum/maximum widths for reading and work areas.

Plan transitions such as:
- Multi-column to single-column.
- Sidebar to collapsible or compact navigation.
- Wide table to prioritized columns, controlled horizontal scrolling, or detail view.
- Multi-pane workspace to stacked or switchable panes.
- Large dialog to full-screen sheet on constrained windows.
- Hover controls to visible touch and keyboard alternatives.

Prevent accidental clipping, overlap, unreadable text, unbounded line lengths, and hidden essential actions. Do not stretch every component to fill large screens. Handle orientation, resize, split-screen, virtual keyboard, safe areas, and fold/unfold transitions when relevant.

Test intermediate widths, not only preset device sizes. Record viewport, pixel ratio, zoom, text scaling, orientation, and input method.
