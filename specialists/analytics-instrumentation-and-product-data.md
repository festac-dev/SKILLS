# Analytics Instrumentation and Product Data Specialist

## Mission
Collect the minimum trustworthy data needed to learn and decide, with privacy by default.

## Plan
Questions first (`templates/ANALYTICS_METRIC_SPEC.md`): what decisions will this data inform? Define North Star and input metrics, funnels, retention cohorts, and guardrail metrics (performance, errors, support load).

## Event design
Object-action naming (`project_created`), a small stable taxonomy, required properties (user/account IDs pseudonymous, timestamp UTC, platform, app version, experiment arms), versioned schemas with validation at ingestion, server-side events for money/security/critical outcomes (client events are lossy and spoofable), deduplication via event IDs, no free-text PII.

## Stack choices
Privacy-friendly web analytics (Plausible, Fathom, Umami, Matomo) for simple needs; product analytics (PostHog, Amplitude, Mixpanel) for funnels/cohorts; warehouse-native (events to BigQuery/Snowflake/ClickHouse + dbt + BI) for control; tag manager only with governance. Self-host vs SaaS by data sensitivity, cost and team capacity.

## Privacy and consent
Consent banners where law requires (ePrivacy/GDPR) with granular choices; honor Do Not Track/Global Privacy Control where applicable; IP truncation; retention limits; no session recording of sensitive fields (mask inputs); data processing agreements; user deletion propagation.

## Experimentation
Hypothesis, primary metric, guardrails, sample size and duration set in advance, randomization at the right unit, sample-ratio-mismatch checks, avoid peeking, document outcomes; feature flags for exposure control.

## Quality
Tracking plan in version control, automated tests for critical events, debug view in staging, data quality monitors (volume, null rates), dashboards with definitions and owners.

## Failure modes
Tracking everything, inconsistent names, client-only revenue events, consent ignored, dashboards nobody trusts.
