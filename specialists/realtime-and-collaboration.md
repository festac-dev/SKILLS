# Specialist: Real-Time Systems and Collaboration

Use real-time behavior only when users benefit from shared, timely state.

Evaluate WebSockets, server-sent events, polling, push notifications or managed realtime services against scale, hosting, reliability and complexity. Define presence semantics, reconnect behavior, ordering, conflict resolution, authorization, backpressure, offline edits and duplicate event handling.

For collaborative editing, distinguish transient presence from durable document state. Use versioning or operational/CRDT techniques only when concurrent editing requirements justify them. Never imply an update was saved until persistence is confirmed. Provide clear connection and synchronization status.

## Applied verification

Disconnect a participant during concurrent edits, then reconnect from its last acknowledged position. Verify ordering, permissions, deduplication and the documented merge or conflict behavior without losing acknowledged edits.

## Connection and synchronization contract

Specify what is durable, the ordering scope, event identity, last acknowledged cursor and retention window. On reconnect, resume from a supported cursor or request a complete snapshot; do not silently skip a gap. Authorize initial subscriptions, each protected stream and changes in membership. Revoke access on active connections as well as on the next login.

Bound per-client buffers and fan-out. For slow consumers, coalesce replaceable presence updates, apply backpressure, or disconnect with an explicit resync path. Durable events need a different loss policy. Define heartbeat, idle timeout and proxy behavior across the actual host.

Choose polling, SSE, WebSockets or managed transport from directionality, latency, hosting and scale. CRDT/OT techniques require defined data types, merge rules and deletion/permission behavior; they are not a default for every shared form. Test duplicate/out-of-order events, prolonged offline edits, expired cursors, mid-session revocation and shutdown/reconnect without losing acknowledged work.

## Connection capacity and recovery

Separate durable state from ephemeral presence and typing indicators. Authenticate connection establishment and credential refresh, then authorize each channel/message. Define the replay window and snapshot-plus-delta recovery when a resume cursor expires; bound slow-consumer buffers and plan a polling fallback when the network blocks sockets. Measure file-descriptor, memory and load-balancer timeout limits as well as message throughput. Test gradual connection drain, tab sleep and reconnect bursts; WebRTC also requires signaling and a STUN/TURN plan.
