# Feature Decision Framework

Score candidate features qualitatively; do not manufacture precision.

For each feature, document:
- user problem and expected outcome;
- evidence source and confidence;
- impact if omitted;
- frequency and severity of the problem;
- implementation and ongoing maintenance cost;
- security, privacy, accessibility and compliance implications;
- dependencies and migration needs;
- measurable acceptance criteria.

## Decision labels

- **Must have:** core journey, safety, legal requirement, explicit acceptance criterion or essential operational capability.
- **Should have:** strong user value with a credible near-term case.
- **Could have:** optional enhancement with bounded cost.
- **Not applicable:** does not fit the product or target users.
- **Defer:** valid idea, but premature or blocked.
- **Reject:** weak value, redundant, harmful, or unjustified complexity.

## Anti-bloat test

Before adding anything, ask:
1. Which user problem does this solve?
2. What evidence shows the problem exists?
3. Is there already a simpler way to solve it?
4. Does it introduce new permissions, data, costs or failure modes?
5. How will users discover and understand it?
6. How will it be tested and maintained?
7. What existing behavior could it disrupt?

If there is no credible answer, do not add the feature.

## Current-task application

Tie every accepted feature to the current user request or observed problem. Treat later corrections as updates to acceptance, not unrelated suggestions; retain unfinished authorized work when a new maintenance request is added.
