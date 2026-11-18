# AI Contamination Cleanup and Git Hygiene Playbook

## 1. Inspect before changing
- Inspect repository status, tracked/untracked files, existing `.gitignore`, tool-specific agent directories, and project conventions.
- Identify actual AI scratch files versus intentional project instructions, skills, prompts, tests, docs, and generated assets.
- Do not delete or ignore files based only on their names.

## 2. Clean project-facing content
- Search source, comments, docs, UI copy, metadata, and commit-ready assets for assistant self-references and conversational residue.
- Remove irrelevant AI disclaimers, progress narration, prompt fragments, copied transcripts, and obvious filler.
- Rewrite useful explanations in the project's own voice.
- Preserve meaningful engineering rationale, attribution, licenses, security warnings, and required provenance.
- Verify that removing comments does not remove important behavior or safety information.

## 3. Configure ignore rules
- Add narrow rules for confirmed local-only agent state, transcripts, scratch prompts, caches, logs, secrets, temporary files, and build artifacts.
- Preserve intentionally tracked project-level agent instructions and reproducible configuration.
- Prefer `.git/info/exclude` for personal-only exclusions.
- Include safe environment templates such as `.env.example` while excluding actual secret-bearing files.

## 4. Check Git behavior
Run and inspect:
```bash
git status --short
git status --ignored --short
git diff -- .gitignore
git diff --cached --stat
git ls-files
```
For suspicious paths:
```bash
git check-ignore -v path/to/file
```
Remember: ignore rules do not remove already tracked files. If a tracked local-only artifact should stop being tracked, first verify the exact path and intent, then use:
```bash
git rm --cached -- path/to/file
```
Do not use broad recursive removal commands without reviewing the exact file list.

## 5. Validate
- Confirm essential source, tests, docs, lockfiles, workflows, and deployment files remain visible to Git.
- Confirm real secrets and local state are not staged.
- Run tests, lint, type checks, and build checks affected by cleanup.
- Review the final diff and staged file list.
- Report exactly what was removed, ignored, preserved, and tested. Never claim a clean repository without checking it.
