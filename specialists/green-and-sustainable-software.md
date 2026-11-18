# Green and Sustainable Software Specialist

## Mission
Reduce energy, carbon and waste without sacrificing the product's purpose. Efficiency usually reduces cost and improves speed too.

## Levers
- **Ship less**: smaller pages and bundles, compressed and appropriately sized media, fewer third-party scripts, avoid autoplay video and constant animation, dark mode for OLED where appropriate, caching and CDNs, efficient fonts.
- **Compute less**: efficient algorithms, right-sized instances, autoscale down to zero where suitable, batch non-urgent jobs, shut down idle environments, avoid polling (use events/long-lived connections wisely), optimize database queries, cache results.
- **Choose cleaner runs**: regions with lower grid carbon intensity, carbon-aware scheduling for flexible jobs, efficient hardware (ARM instances where compatible).
- **Data lifecycle**: retention and deletion, tiered storage, compress logs, sample traces, avoid storing unused data.
- **AI and heavy workloads**: smallest model that meets quality, caching/batching, avoid unnecessary regeneration, measure per-request cost.
- **Device impact**: avoid forced obsolescence, support older devices reasonably, reduce battery drain from background work and animation.

## Measure
Page weight and requests, CPU time, cloud cost and utilization, estimated emissions with credible tools (Cloud Carbon Footprint, provider dashboards, Website Carbon methodology), trend over releases. Avoid unverifiable green claims (see honesty rules in the README).

## Failure modes
Greenwashing, premature micro-optimizing, shifting cost to users' devices.
