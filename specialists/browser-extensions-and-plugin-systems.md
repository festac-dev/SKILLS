# Browser Extensions and Plugin Systems Specialist

## Browser extensions
- **Manifest V3** (Chrome, Edge, and Firefox with its own differences; Safari via converter): service-worker background (event-driven, no persistent page), declarative net request instead of blocking webRequest, content scripts with isolated worlds, action popups, side panels, options pages, `chrome.storage` (sync/local/session), alarms, messaging between contexts, `activeTab`/optional permissions to minimize access.
- **Security and review**: minimal permissions and host patterns; no remote code execution; strict CSP; sanitize any DOM insertion; treat page content as untrusted; secure messaging (verify sender); store tokens carefully; clear privacy policy and data disclosures; expect store review and policy updates.
- **Cross-browser**: WebExtensions polyfill, feature detection, build per target, test on each store's review constraints.
- **UX**: explain permissions before requesting, graceful behavior when site DOM changes (resilient selectors, mutation observers), performance impact kept near zero, uninstall cleanup.

## Plugin and extension architectures inside your product
Decide extension points (hooks, events, UI slots, commands), isolation (iframes, workers, WASM sandboxes, separate processes), capability-based permissions with user consent, stable versioned API, manifest with metadata and signature, distribution and review process, resource limits, error isolation (a bad plugin must not crash the host), telemetry and kill switch, documentation and SDK.

## Failure modes
Over-broad permissions, reliance on brittle selectors, remote code, plugins with full host access, no versioning for the plugin API.
