# Project .gitignore Template

Use this as a starting point, not a universal file. Inspect the project's stack and actual generated paths before adopting each section.

```gitignore
# Secrets and local environment
.env
.env.*
!.env.example
!.env.sample
!.env.template
secrets/
.local-secrets/
*.pem
*.key
*.p12
*.pfx

# Local AI/agent state (only if these paths are local-only)
.ai-cache/
.agent-cache/
.agent-state/
.agent-sessions/
.agent-work/
.ai-logs/
.chat-transcripts/
.prompt-scratch/

# Logs and runtime files
*.log
*.pid
*.sock

# OS/editor noise
.DS_Store
Thumbs.db
*.swp
*.swo
*~

# Add stack-specific build/cache rules only after inspecting the project.
```

## Before committing
```bash
git status --short
git status --ignored --short
git diff -- .gitignore
```

Do not assume this template covers every tool or repository. Add exact local-only paths discovered during the audit, and preserve all intentional deliverables.
