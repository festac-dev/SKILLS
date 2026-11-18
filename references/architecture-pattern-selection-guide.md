# Architecture Pattern Selection Guide

## Candidate styles
- Modular monolith: strong default when one team/product can benefit from a cohesive deployable unit.
- Service-oriented or microservices: consider when independent ownership, scaling, isolation, or release cadence justify the operational cost.
- Serverless: consider for event-driven or bursty workloads when platform constraints and execution limits fit.
- Event-driven: consider when asynchronous decoupling and durable event processing solve a real problem.
- Edge/distributed: consider when locality, latency, resilience, or data residency demands it.
- Embedded/on-device: consider for offline, privacy, latency, or hardware integration needs.

## Compare on
Team capability, domain boundaries, data consistency, failure isolation, observability, deployment complexity, cost, security, latency, portability, and expected evolution.

## Decision method
1. State the problem and non-functional constraints.
2. Establish a simple baseline.
3. Compare credible alternatives.
4. Identify operational burden and failure modes.
5. Prototype only the uncertain, high-impact parts.
6. Record decision and revisit triggers.

Avoid architecture by trend, diagram aesthetics, or hypothetical scale.

## Application evidence

Compare a candidate against the current deployment on one real operation: latency, failure recovery, ownership and operating cost. Select distribution only when the measured constraint or required isolation justifies its added failure boundaries.
