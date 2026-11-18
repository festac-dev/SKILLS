# Metrics and Experimentation Guide

## Metric contract
For every metric define purpose, numerator, denominator, population, exclusions, time window, timezone, source, freshness, owner, and known limitations.

## Metric hierarchy
Connect business outcomes to user outcomes and operational guardrails. Avoid optimizing proxy metrics in isolation.

## Experiment design
Write hypothesis, target population, assignment, exposure, primary metric, guardrails, duration, sample assumptions, and stop/ship criteria before launch.

## Integrity
Check event loss, duplicate events, bot traffic, selection bias, seasonality, novelty effects, and multiple comparisons.

## Reporting
Include uncertainty and limitations. Do not claim causality from observational correlation.

## Application evidence

Recompute a displayed metric from a small independently understood dataset, including duplicates, zero denominators and time-zone boundaries. Keep experiment assignment, exposure and outcome distinct so missing instrumentation does not become evidence of no effect.
