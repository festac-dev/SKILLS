# Examples

Runnable pattern examples. Palettes, copy and sample records are demonstration values; adapt them to the project's own identity and stack.

| Folder / file | What it shows | How to check |
|---|---|---|
| `backend-reference/` | Request IDs, structured logs, problem+json errors, validation, rate limiting, idempotency, pagination, signed webhooks, retries and graceful shutdown | `cd backend-reference && node --test` (Node 20+) |
| [Animated graphics](animated-graphics/index.html) | Orbit with inertia, flowing network, layered parallax, WebGL2 field and rerouting SVG connectors | `cd animated-graphics && python3 test_examples.py` (requires Python Playwright, Pillow and a compatible Chromium installation) |

Consult current execution evidence before treating an example as verified. The supplied browser suite checks its stated states and interactions; it does not establish real-device frame rates, screen-reader behavior or Safari/Firefox support. Measure those on the project's target devices before making performance or accessibility claims.
