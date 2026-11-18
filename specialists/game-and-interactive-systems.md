# Game and Interactive Systems Specialist

## Mission
Design interactive systems with clear rules, responsive feedback, and reliable state.

## Responsibilities
- Define core loops, progression, input mapping, simulation rules, save states, and accessibility.
- Profile frame time, memory, loading, network synchronization, and device limits.
- Plan deterministic simulation or replay where required.
- Design multiplayer authority, latency compensation, anti-cheat boundaries, and reconnect behavior when applicable.
- Use 3D, physics, audio, and effects only when they strengthen the intended experience.

## Deliverables
Interaction model, technical performance budget, state architecture, and test scenarios.

## Deterministic simulation, fault injection, and replay

### When to use
Use for simulations, stateful workflows, hard-to-reproduce races, or failures sensitive to time/order. This procedure also applies to non-game systems with explicit events and state.

### Core principles
Separate state transitions from clock, randomness, I/O, and rendering. Record external inputs and scheduling decisions needed to reproduce behavior. A random seed alone does not make concurrent I/O deterministic.

### Step-by-step procedure
1. Define initial state, event schema, transition function, virtual clock, and deterministic random source.
2. Log inputs with sequence, time model, version, and relevant external outcomes. Minimize sensitive payloads.
3. Inject dropped, duplicated, delayed, reordered, and failed events at explicit boundaries.
4. Replay from a checkpoint and compare state hashes or domain invariants.
5. Bisect the event sequence to the first divergent transition. Fix the cause and retain the minimal replay case.

### Checklist
- [ ] Replay pins code/schema and initial state versions.
- [ ] External dependencies are represented by recorded outcomes or controlled fixtures.
- [ ] Clock/randomness/scheduling are controlled where claimed.
- [ ] Logs have access and retention limits.

### Common failure modes
Wall-clock reads escape the virtual clock; unordered iteration changes results; a replay omits external responses; time-travel debugging is claimed from a seed alone; production secrets are embedded in event logs.

### Concrete examples
```python
def replay(events):
    state = 0
    for delta in events:
        state += delta
        assert state >= 0
    return state
events = [5, -2, -3]
assert replay(events) == replay(list(events)) == 0
```
This small pure transition test illustrates replay; a real system must record its actual inputs, external results, and versioned state.

### Verification
Replay a known failure twice with identical results, identify the first divergence, and demonstrate that the fix preserves invariants under the same fault schedule.

### Related skills
[Distributed systems](edge-and-distributed-systems.md), [formal methods](formal-methods-and-invariants.md), [differential testing](../references/differential-and-metamorphic-testing.md).

## Applied verification

Replay recorded input after suspending the application, changing refresh rate and reconnecting. Confirm simulation time and state hashes follow the declared model while rendering and audio resources are released after leaving the scene.

## Simulation and replay

Where deterministic simulation matters, separate fixed-step updates from interpolated rendering, record seeded randomness and version saved/replay state. Measure allocation spikes and entity growth before pooling or spatial partitioning. Multiplayer prediction needs authoritative reconciliation and an explicit lag/interest-management policy; input buffering and accessibility controls belong in the playable prototype before expanding content.
