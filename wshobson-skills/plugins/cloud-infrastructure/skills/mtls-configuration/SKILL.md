---
name: wshobson-mtls-configuration
description: Configure mutual TLS (mTLS) for zero-trust service-to-service communication.
  Use when implementing zero-trust networking, certificate management, or securing
  internal service communication.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# mTLS Configuration

Comprehensive guide to implementing mutual TLS for zero-trust service mesh communication.

## When to Use This Skill

- Implementing zero-trust networking
- Securing service-to-service communication
- Certificate rotation and management
- Debugging TLS handshake issues
- Compliance requirements (PCI-DSS, HIPAA)
- Multi-cluster secure communication

## Core Concepts

### 1. mTLS Flow

```
┌─────────┐                              ┌─────────┐
│ Service │                              │ Service │
│    A    │                              │    B    │
└────┬────┘                              └────┬────┘
     │                                        │
┌────┴────┐      TLS Handshake          ┌────┴────┐
│  Proxy  │◄───────────────────────────►│  Proxy  │
│(Sidecar)│  1. ClientHello             │(Sidecar)│
│         │  2. ServerHello + Cert      │         │
│         │  3. Client Cert             │         │
│         │  4. Verify Both Certs       │         │
│         │  5. Encrypted Channel       │         │
└─────────┘                              └─────────┘
```

### 2. Certificate Hierarchy

```
Root CA (Self-signed, long-lived)
    │
    ├── Intermediate CA (Cluster-level)
    │       │
    │       ├── Workload Cert (Service A)
    │       └── Workload Cert (Service B)
    │
    └── Intermediate CA (Multi-cluster)
            │
            └── Cross-cluster certs
```

## Templates and detailed worked examples

Full template library and detailed worked examples live in `references/details.md`. Read that file when you need the concrete templates.

## Best Practices

### Do's

- **Start with PERMISSIVE** - Migrate gradually to STRICT
- **Monitor certificate expiry** - Set up alerts
- **Use short-lived certs** - 24h or less for workloads
- **Rotate CA periodically** - Plan for CA rotation
- **Log TLS errors** - For debugging and audit

### Don'ts

- **Don't disable mTLS** - For convenience in production
- **Don't ignore cert expiry** - Automate rotation
- **Don't use self-signed certs** - Use proper CA hierarchy
- **Don't skip verification** - Verify the full chain
