---
name: alireza-operator-audit
description: Run the full Kubernetes Operator audit (CRD + reconcile + capability) on the current repo
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# /operator-audit

Run the full audit on a Kubernetes Operator repository:

1. Validate every CRD YAML against operator-pattern best practices
2. Lint every Go controller's reconcile function for anti-patterns
3. Score the operator against OperatorHub Capability Levels (1-5)
4. Output a markdown report with pass/fail per check and concrete next steps

## Usage

```
/operator-audit
/operator-audit --operator-dir ./my-operator
/operator-audit --crd-dir ./config/crd --controller-dir ./controllers
```

## Implementation

```bash
SKILL=engineering/kubernetes-operator/skills/kubernetes-operator
DIR="${OPERATOR_DIR:-.}"

echo "## CRD validation"
python "$SKILL/scripts/crd_validator.py" --crd "$DIR/config/crd" || true

echo ""
echo "## Reconcile lint"
python "$SKILL/scripts/reconcile_lint.py" --controller "$DIR/controllers" || python "$SKILL/scripts/reconcile_lint.py" --controller "$DIR/internal/controller" || true

echo ""
echo "## Capability audit"
python "$SKILL/scripts/operator_capability_audit.py" --operator-dir "$DIR"
```

## Output

A markdown report with:

- **CRD findings** per file: FAIL / WARN / PASS for each check
- **Reconcile findings**: line-numbered anti-patterns
- **Current capability level** + concrete advancement steps

## Pre-conditions

- Run from a Kubernetes Operator repository
- Go controllers expected at `controllers/` or `internal/controller/`
- CRDs expected at `config/crd/` (kubebuilder layout)
- `kubernetes-operator` skill installed

## Post-conditions

- Markdown report streamed to terminal
- Exit code 0 if all PASS; 1 if any FAIL
