# Interactive world contract

Use this contract when the output camera can orbit, pan, zoom, fly, or otherwise leave the exact
reference pose, and when browser feedback identifies a spatial defect. It is a scene-quality
contract, not a style prescription.

## Two independent gates

Pass both gates. Never trade one for the other.

1. **Reference-view fidelity:** at the declared reference time and aspect ratio, camera pose/FOV,
   silhouettes, landmarks, occlusion, scale, lighting, and composition match the evidence within
   the route's tolerances.
2. **Exploration validity:** every pose reachable through the shipped controls shows a coherent
   physical world without unintended geometry ends, disconnected traversal surfaces, invalid
   occupancy, floating supports, or backdrop seams.

If the deliverable intentionally supports only a locked camera, encode that restriction in the
controls and manifest. Do not claim a locked-camera exemption while shipping unrestricted orbit or
pan controls.

## Interpret spatial feedback before editing

A canvas annotation is localized evidence, not automatically a complaint about the entire canvas.

1. Reproduce the same URL state, timeline time, viewport/aspect ratio, and camera pose. Persist or
   export camera pose from the preview so this is normally possible.
2. Identify in words the exact visible feature nearest the marker: for example a surface cap,
   occlusion boundary, intersection seam, support gap, or misplaced object.
3. Classify the failure before selecting a correction:
   - reference-camera composition;
   - topology/connectivity;
   - physical support or occupancy;
   - occlusion/readability;
   - exploration boundary exposure;
   - material or asset fidelity.
4. Correct the classified cause, then recapture the same pose and at least one adversarial pose.

Do not use occluders to conceal a topology error, extend a texture to disguise disconnected
geometry, or move the camera to hide a world boundary. If substantially the same rejection remains
after a correction, invalidate the current diagnosis and inspect an adjacent class before editing
again.

## Camera envelope and world closure

Derive the reachable camera envelope from the actual controls: orbit target and polar/azimuth
limits, pan range, minimum/maximum distance, FOV or zoom range, near/far planes, collision limits,
and any scripted camera motion. Record the envelope in review evidence.

Within that envelope:

- Long roads, paths, rails, coastlines, water, ground, and terrain must either continue beyond all
  allowed views or terminate naturally in modeled terrain, architecture, vegetation, haze, or fog.
- A visible finite cap is a failure even when it lies outside the canonical reference frame.
- Orbitable scenes use a closed sky/background treatment; a finite backdrop plane is insufficient
  unless controls make its edges unreachable.
- Ground, terrain skirts, and water coverage must include the camera frustum at all allowed poses.
- Extensions preserve world-scale texture density using suitable repeat, world-space, or triplanar
  mapping; stretching the existing UV interval is not a valid extension.
- Repeated long-range detail should use instancing, LOD, batched segments, or bounded procedural
  generation where practical. World closure must not create an avoidable draw-call explosion.

## Traversal topology

Represent roads and paths as connected centerlines plus generated or explicitly modeled surface
polygons. Decorative overlap is not proof of connection.

- At an intersection or entrance, surfaces share a continuous traversable region with no cap,
  crack, vertical step, or blocking curb across the intended path.
- Lane markings, shoulders, guards, curbs, and vegetation open or merge consistently at the
  junction. A road that visually continues while its shoulder closes across it still fails.
- Tangents and widths remain readable through the connection; avoid abrupt pinches or implausible
  angle changes unless supported by the reference.
- Validate connectivity in world space by sampling the traversable region or inspecting the
  generated topology, not only from the canonical camera.

Occlusion and topology are separate checks. Vegetation may make a valid continuation hard to read;
that is an occlusion/readability failure. It cannot make a disconnected road valid.

## Physical support and occupancy

Define semantic occupancy zones for lanes, shoulders, sidewalks, paths, water, planting areas, and
support surfaces. Check object footprints in world space.

- Poles, signs, gantries, guard supports, trees, parked objects, and props stay outside traffic or
  traversal zones unless the evidence explicitly places them there.
- Use oriented footprints, polygon intersections, or sampled centerline clearance for long or
  rotated objects. Broad axis-aligned bounding boxes can falsely report or miss lane collisions.
- Every object with gravity semantics has a declared support surface and contact point/base. Reject
  visible gaps, buried bases, and support points resting on the wrong semantic surface.
- Vegetation follows terrain height or a declared planting surface; vehicles contact the road at
  wheel patches; fixtures contact their verge, sidewalk, or foundation.
- Re-check occupancy and grounding after proxy replacement, scaling, animation, and layout changes.

## Required adversarial review views

Keep the canonical reference capture, then add named, reproducible diagnostic views appropriate to
the shipped controls:

- first, middle, and last scripted camera poses when motion exists;
- high oblique overview;
- view along each long world axis;
- reverse and side views;
- maximum allowed orbit, pan, and zoom extents;
- behind or below only when those poses are reachable by the user.

Debug views must save camera pose, time, viewport, and control state. Review them for world edges,
surface caps, disconnected paths, occupancy violations, floating objects, sky seams, extreme texture
stretch, and newly exposed low-detail proxies.

## Evidence and hard failures

Record:

- camera envelope and control limits;
- world and major-surface bounds;
- reference-view comparison result;
- boundary-exposure result for every adversarial view;
- road/path connectivity result;
- semantic occupancy/clearance result;
- grounding/support result;
- captures and the exact reproducible state for failures and fixes.

Hard-fail completion if any allowed pose reveals an unintended road, terrain, water, or sky end; if
an intended path is disconnected; if a fixture or support occupies a traffic/traversal zone without
evidence; or if a gravity-bound object visibly floats or penetrates its support surface.
