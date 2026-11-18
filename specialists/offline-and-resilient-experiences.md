# Specialist: Offline and Resilient Experiences

Offline capability is optional and must follow actual user context.

Identify which tasks must work offline, which data may be cached, how stale data is labelled, how edits queue, how conflicts resolve and how sensitive data is protected on-device. Define retry/backoff, idempotency, storage quotas, expiry, synchronization status and recovery after interrupted sync.

Do not promise offline support when the product only has a service worker or cached shell. Test airplane mode, intermittent connectivity, expired sessions, partial sync and conflicting updates.

## Applied verification

Queue an edit offline, change the same record elsewhere, then reconnect with an expired session. Verify the conflict policy, retained input and reauthentication path; a cached shell does not demonstrate offline editing.

## Storage and sync failure drills

Test process termination mid-sync, clock skew, quota exhaustion and a client remaining on an older local schema. A service worker must have a deliberate update and cache-expiry path. Select cached reads, queued writes or local-first collaboration from the product’s conflict requirements; CRDTs are useful for mergeable data but cannot allocate scarce authoritative resources by themselves.
