---
name: copilot-pytest-coverage
description: 'Run pytest tests with coverage, discover lines missing coverage, and increase coverage to 100%.'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

The goal is for the tests to cover all lines of code.

Generate a coverage report with:

pytest --cov --cov-report=annotate:cov_annotate

If you are checking for coverage of a specific module, you can specify it like this:

pytest --cov=your_module_name --cov-report=annotate:cov_annotate

You can also specify specific tests to run, for example:

pytest tests/test_your_module.py --cov=your_module_name --cov-report=annotate:cov_annotate

Open the cov_annotate directory to view the annotated source code.
There will be one file per source file. If a file has 100% source coverage, it means all lines are covered by tests, so you do not need to open the file.

For each file that has less than 100% test coverage, find the matching file in cov_annotate and review the file.

If a line starts with a ! (exclamation mark), it means that the line is not covered by tests.
Add tests to cover the missing lines.

Keep running the tests and improving coverage until all lines are covered.
