# MLOps and Applied ML Engineering Specialist

## Scope
Classical ML, recommendation/ranking, forecasting, vision/audio models, embeddings, fine-tuning and evaluation. For LLM application plumbing see `ai-and-llm-backend-infrastructure.md`; for safety and evals see `ai-evaluation-and-governance.md`.

## Decide whether ML is needed
Define the decision the model improves, the baseline (rules/heuristics/statistics), the metric tied to business value, the cost of errors (false positive vs false negative), the data available, latency and privacy constraints. Ship the baseline first; ML must beat it measurably.

## Lifecycle
1. **Data**: sourcing, consent/licensing, labeling guidelines and quality checks, train/validation/test split by time or entity to prevent leakage, dataset versioning (DVC, lakeFS, table snapshots), documentation (datasheets).
2. **Experimentation**: reproducible environments, seeds, tracked runs (MLflow, Weights & Biases, Neptune), simple strong baselines (logistic regression, gradient boosting) before deep nets, error analysis by slice.
3. **Evaluation**: metrics matched to the problem (precision/recall, PR-AUC, calibration, ranking metrics, MAE/MAPE with context), fairness and subgroup performance, robustness, uncertainty, human review of samples, offline-to-online correlation.
4. **Packaging and serving**: batch scoring vs online inference; model registry with stage gates; containerized serving (BentoML, KServe, Triton, TorchServe, vLLM for LLMs, ONNX Runtime); feature stores (Feast, Tecton, or well-tested SQL) with training/serving parity; latency budgets; fallbacks when the model is unavailable.
5. **Release**: shadow mode, canary, A/B or interleaving, guardrails, rollback to previous model, kill switch.
6. **Monitoring**: data drift, concept drift, prediction distribution, latency, errors, business KPIs, feedback loops; retraining triggers and cadence; alerts with runbooks.
7. **Governance**: model cards, intended use and limits, privacy review, explainability where needed, audit trail of data/model versions, deletion and consent propagation.

## Failure modes
Leakage, training/serving skew, evaluating on non-representative data, optimizing a proxy metric, no rollback, silent drift, unlabeled production feedback loops, shipping a model where a rule would do.

## Deliverables
Problem and baseline brief, dataset documentation, experiment log, evaluation report with slices, serving design and SLOs, monitoring plan, model card (`templates/AI_EVALUATION_PLAN.md`).
