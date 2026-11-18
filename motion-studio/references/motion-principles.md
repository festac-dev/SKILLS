# Motion Studio Choreography

Plan causal beats in executable scene data, not a separate planning document. A document opens; its evidence layers separate; a verifier scans one layer; a hash locks into a human decision. Each action changes what the viewer understands. Recoloring one generic loop across products is insufficient.

| Event | Default | Easing | Required observation |
| --- | --- | --- | --- |
| Focus / hover | 200ms | ease-out-expo | Visible with keyboard as well as pointer |
| Panel / route | 320–480ms | ease-in-out | Selection and focus remain stable |
| Hero assembly | 600–1200ms | damped spring | Overshoot does not obscure a label |
| Sibling stagger | 40–90ms | shared curve | Ordered, without serial waiting |
| Progress / flow | actual duration | linear | Matches the process it represents |

```ts
import {motion, expo, clamp} from '../templates/motion-tokens';
const entrance = expo(clamp((time - wordCue.start) / motion.duration.hero));
const y = (1 - entrance) * 64;
const opacity = entrance;
// Frame-rate-independent pointer smoothing, dt in seconds:
current += (target - current) * (1 - Math.exp(-10 * Math.min(dt, 0.05)));
```

Use one motion clock. Define state boundaries from actual word timestamps or measured section geometry, not timers that race one another. Make reverse input continuous. Let an outgoing card become the incoming proof strip: interpolate position, scale and rotation across a shared transition interval, with scene opacity only supporting the transfer.

```ts
const handoff = clamp((time - cue.start) / 0.48);
const smooth = handoff * handoff * (3 - 2 * handoff);
const x = from.x + (to.x - from.x) * smooth;
const scale = from.scale + (to.scale - from.scale) * smooth;
```

For each 6–12 second scene, create several meaningful beats: reveal context, move the artifact, isolate the decision, carry it into the next scene. Between beats, a trace, scan, active code line or evolving object may maintain motion. A one-percent camera drift on an otherwise static slide does not qualify. Essential text holds readable while its supporting geometry changes.

## Common failures and fixes

- Every object enters together: assign one focal action and stagger dependent objects by 64ms.
- Spring keeps wobbling: increase damping before shortening the scene; use the same tested spring everywhere.
- Scene snaps at a cut: match the shared object's screen-space pose and velocity at the boundary.
- Rhythm feels uniform: change shot scale and focal action, not just transition duration.
- Video state outruns narration: bind the state change to the end of the spoken action; inspect before/after frames around that exact word.
