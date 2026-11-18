---
name: agentic-awesome-superpowers-lab
description: Evaluate experimental Claude workflow skills in an isolated lab with
  reproducible tasks, observed results, and explicit adoption criteria.
metadata:
  upstream_headers:
    risk: safe
    source: https://github.com/obra/superpowers-lab
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Superpowers Lab

## When to Use
- You want to evaluate an experimental workflow from the upstream Superpowers lab before adopting it.
- You need a reproducible comparison of baseline behavior and a proposed skill.

## Workflow
1. Select one experiment from the [upstream lab](https://github.com/obra/superpowers-lab). Read its instructions, status, prerequisites, and license before using it; this entry does not bundle the lab's experiments.
2. Define a small representative task, success criteria, time/cost limits, and the files/tools each run may access. Use disposable fixtures and no production credentials.
3. Record the baseline agent/tool configuration and run the task without the experimental skill. Capture outputs, observed failures, and validation results.
4. Review the experiment's complete content and any commands before loading it. Run the same task with the experimental skill in an isolated workspace under the same permissions and acceptance criteria.
5. Compare the actual outputs and failures. Separate observed improvements from subjective preferences; record changed model/tool settings as confounders.
6. Decide whether to retain, revise, or reject the experiment. Keep production adoption separate from the lab run, and include a rollback/removal plan if adoption is proposed.

## Example
> Compare one lab workflow against our baseline on a disposable bug-fix fixture. Report tests and failure modes without installing it globally.

## Limitations
- Experimental guidance is not a production guarantee. Do not infer compatibility or improvement without a controlled run.
- The original experiment and its fixtures are external prerequisites; report unavailable materials.
- Do not execute unreviewed scripts, expand permissions, or use private production data for the experiment.
