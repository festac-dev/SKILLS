---
name: agentic-awesome-2d-games
description: 2D game development principles. Sprites, atlases, tilemaps, physics,
  cameras, and genre patterns (platformer, top-down). Use for canvas/Phaser/Kaplay/Pixi
  2D games or guest viewports inside hybrid web apps.
metadata:
  aas-risk: none
  aas-source: community
  aas-date-added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# 2D Game Development

> Principles for 2D game systems. Pair with `game-development/web-games` / `game-development/engine-selection` for framework choice.

---

## Shell vs guest (web)

| Setup | 2D systems live… |
|-------|------------------|
| Full-screen 2D game | Entire app (Phaser/Kaplay/Pixi/Canvas) |
| Hybrid DOM + challenges | Only inside guest viewports; tear down when done |

---

## 1. Sprite Systems

| Component | Purpose |
|-----------|---------|
| **Atlas** | Combine textures, reduce draw calls |
| **Animation** | Frame sequences (often 8-24 FPS) |
| **Pivot** | Rotation/scale origin |
| **Layering** | Z-order control |

### Animation Principles

- Squash and stretch for impact
- Anticipation before action
- Follow-through after action

---

## 2. Tilemap Design

| Factor | Recommendation |
|--------|----------------|
| **Size** | 16x16, 32x32, 64x64 |
| **Auto-tiling** | Use for terrain |
| **Collision** | Simplified shapes |

| Layer | Content |
|-------|---------|
| Background | Non-interactive scenery |
| Terrain | Walkable ground |
| Props | Interactive objects |
| Foreground | Parallax overlay |

---

## 3. 2D Physics

| Shape | Use Case |
|-------|----------|
| Box | Rectangular objects |
| Circle | Balls, rounded |
| Capsule | Characters |
| Polygon | Complex shapes |

- Choose a movement/collision model per mechanic; pixel-art rendering can coexist with physics
- Fixed timestep for consistency
- Layers for filtering

---

## 4. Camera Systems

| Type | Use |
|------|-----|
| **Follow** | Track player |
| **Look-ahead** | Anticipate movement |
| **Multi-target** | Two-player |
| **Room-based** | Metroidvania |
| **Static** | Board games, modal skill-checks |

### Screen Shake

- Short duration (50-200ms)
- Diminishing intensity
- Use sparingly

---

## 5. Genre Patterns

### Platformer

- Coyote time (leniency after edge)
- Jump buffering
- Variable jump height

### Top-down

- 8-directional or free movement
- Aim-based or auto-aim
- Decide whether rotation matters

---

## 6. Anti-Patterns

| ❌ Don't | ✅ Do |
|----------|-------|
| Separate textures | Use atlases |
| Complex collision shapes | Simplified collision |
| Jittery camera | Smooth following |
| Uncoordinated movement and physics | Define one authority per body |
| Orphaned RAF/listeners after a guest closes | Full teardown |

---

> **Remember:** 2D is about clarity. Every pixel should communicate.

## When to Use

Use for canvas/Phaser/Kaplay/Pixi 2D systems, or guest viewports inside hybrid web apps.

## Example

**User request:**

> Add coyote time and jump buffering to our platformer while preserving the fixed physics timestep and testing corner collisions.

## Limitations

- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
