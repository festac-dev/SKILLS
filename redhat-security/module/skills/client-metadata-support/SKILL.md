---
name: redhat-security-client-metadata-support
description: Support OAuth Client ID Metadata Documents in authorization servers.
  Use when building or reviewing authorization server client validation and registration
  mechanisms for MCP ecosystems.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: authorization-server
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# OAuth Client ID Metadata Document Support in Authorization Servers

## Security Recommendation

Authorization servers SHOULD support OAuth Client ID Metadata Documents. This mechanism allows clients (including MCP clients) to present their identity and configuration without requiring pre-registration, by hosting a metadata document at their `client_id` URL.

## How It Works

1. Client presents a `client_id` that is an HTTPS URL (e.g., `https://mcp-client.example.com/client-metadata`)
2. Authorization server fetches the metadata document from that URL
3. Authorization server validates the client's configuration from the document
4. Authorization server uses the metadata for the OAuth flow

## Validation Rules

When fetching and processing client metadata documents, the authorization server MUST:

| Rule | Details |
|---|---|
| Fetch over HTTPS | Only retrieve metadata from HTTPS URLs |
| Verify `client_id` match | The `client_id` in the document must match the URL it was fetched from |
| Validate `redirect_uris` | Ensure redirect URIs are valid and use HTTPS |
| Check grant types | Only allow grant types the server supports |
| Apply security policies | Enforce server-side policies on client configurations |

## Implementation Checklist

- [ ] Accept `client_id` values that are HTTPS URLs
- [ ] Fetch client metadata documents from the `client_id` URL
- [ ] Validate the `client_id` field in the document matches the fetch URL
- [ ] Validate `redirect_uris` for security (HTTPS, no wildcards)
- [ ] Apply rate limiting on metadata document fetches
- [ ] Cache fetched metadata with appropriate TTL
- [ ] Reject metadata documents that fail validation
- [ ] Log client metadata fetch attempts for audit
