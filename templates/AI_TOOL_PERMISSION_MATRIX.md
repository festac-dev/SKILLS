# AI Tool Permission Matrix

| Tool/action | Read/write/execute | Data scope | Allowed roles | Approval required | Limits | Audit event | Recovery |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Safety rules
- Model output never grants its own permission.
- Enforce permissions in trusted application code.
- Treat retrieved documents, web pages, and tool outputs as untrusted data.
- Require confirmation for consequential or irreversible actions.
- Bound execution time, resource use, and action count.
- Make execution status and evidence visible.
- Define cancellation, compensation, and rollback behavior.

## Execution record

Keep only fields relevant to this artifact.

- Existing authorization source and exact permitted destination:
- Uncertain-outcome reconciliation operation:
- Evidence of denied out-of-scope access:
