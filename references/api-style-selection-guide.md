# API Style Selection Guide

| Situation | Strong candidates | Watch for |
|---|---|---|
| Public API for unknown developers | REST + OpenAPI, webhooks | Versioning, rate limits, docs quality |
| Many client types needing flexible data | GraphQL | Query cost, N+1, per-field auth |
| Internal high-throughput services | gRPC | Browser access, tooling, debugging |
| Live updates to browsers | SSE or WebSocket | Scaling, reconnect, auth |
| Third-party notification of events | Webhooks with signatures | Retries, ordering, replay |
| Async workflows across services | Events/queues | Idempotency, schema evolution |
| Simple server-rendered app | Form posts + HTML responses, thin JSON endpoints | Don't build an API nobody needs |
| Mobile apps | REST/GraphQL with pagination and delta sync | Offline, bandwidth, versioning of old clients |

## Universal checklist
Contract checked in, schema validation, consistent errors, pagination, idempotency, auth and object-level checks, rate limits, observability by endpoint, deprecation policy, examples that run.

## Error envelope example
```json
{
  "error": {
    "code": "validation_failed",
    "message": "Email address is not valid.",
    "request_id": "req_8f2c...",
    "details": [{ "field": "email", "issue": "format" }]
  }
}
```

## Pagination example
Cursor-based: `GET /items?limit=50&cursor=...` returns `next_cursor`. Prefer stable sort keys. Document maximum limit.
