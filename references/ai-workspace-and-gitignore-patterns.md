# AI Workspace and Git Ignore Patterns

## Suggested local-only paths
Adapt these patterns to the actual tools and repository. Do not copy blindly if a path is a real project deliverable.

```gitignore
# Local AI/agent session state
.ai/
.agent-state/
.agent-cache/
.agent-sessions/
.agent-work/
.ai-work/
.ai-cache/

# Local prompts, scratch notes, and transcripts
.local-prompts/
.prompt-scratch/
.agent-notes/
.chat-transcripts/
*.agent-transcript
*.prompt-draft

# Local execution output
.agent-logs/
.ai-logs/
*.agent.log
*.trace.local

# Local environment and secrets
.env
.env.*
!.env.example
!.env.sample
!.env.template
*.pem
*.key
*.p12
*.pfx
secrets/
.local-secrets/

# Common temporary/editor/OS files
.DS_Store
Thumbs.db
*.swp
*.swo
*~
```

## Add only when applicable
```gitignore
# Dependencies and build output
node_modules/
dist/
build/
coverage/
.venv/
venv/
__pycache__/
.pytest_cache/
.mypy_cache/
.ruff_cache/

# Local databases and runtime state
*.sqlite
*.sqlite3
*.db
*.pid
*.sock
```

## Important safeguards
- Do not ignore `.github/`, tests, migrations, lockfiles, source files, project documentation, or reproducible configuration without a specific reason.
- Do not ignore every file named `*.md`; project instructions and user-facing docs may be essential.
- Some agent tools intentionally use tracked project instructions such as `AGENTS.md`, `CLAUDE.md`, or repository-specific skill files. Keep them when the project intentionally shares them.
- Do not assume every directory beginning with `.ai` or `.agent` is disposable. Inspect before adding patterns.
- Add local patterns to `.git/info/exclude` when they should apply only to one clone and must not be shared.
- If sensitive data was already committed, remove it from history and rotate the exposed credential; adding `.gitignore` is not enough.

## Check the actual publication set

Use [repository hygiene](repository-hygiene-and-ai-artifact-policy.md) to classify development prompts and build caches. Ignore rules determine future additions; tracked files and the staged diff need separate review. Check an existing path with `git check-ignore -v -- path/to/file` and tracked ignored files with `git ls-files -ci --exclude-standard`. Use `git ls-files --stage -- path/to/file` when a symlink may explain why a file-name search missed an entry. Keep exclusions scoped to the receiving application; do not hide the reusable skill library when that library is itself being published.
