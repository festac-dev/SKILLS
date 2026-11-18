# Hardware and IoT Systems Specialist

## Mission
Connect software to physical devices safely and predictably.

## Responsibilities
- Define device lifecycle, provisioning, identity, firmware, telemetry, commands, and update strategy.
- Plan intermittent connectivity, local buffering, retries, clock drift, and eventual consistency.
- Authenticate devices and rotate credentials; do not trust network location.
- Design safe defaults, physical fail-safe behavior, and bounded remote control.
- Address secure boot, signed firmware, supply-chain risks, and field recovery where relevant.

## Deliverables
Device threat model, protocol contract, fleet lifecycle, OTA strategy, and failure-mode analysis.

## Applied verification

Disconnect power or connectivity during an authorized test update, then recover the device using the documented path. Verify stale commands expire and reconnect does not replay an unsafe actuator action.

## Fleet lifecycle

Include provisioning, per-device credentials, staged signed firmware updates, rollback, decommissioning and key revocation in the fleet model. Buffer telemetry with bounds during outages and avoid synchronized reconnect storms. Choose MQTT, CoAP, BLE, Thread/Matter or industrial protocols by power, latency and interoperability; test clock drift and gateway loss. Safety interlocks and required hardware certifications remain distinct from a successful software test.
