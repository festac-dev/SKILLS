# Repository Cleanliness and Git Leakage Gate

- [ ] No irrelevant AI-generated disclaimers, self-references, or assistant chatter in shipped code/docs/UI.
- [ ] No accidental prompts, private chat transcripts, tool traces, local agent state, or scratch notes staged.
- [ ] No secrets, tokens, private keys, or real `.env` files staged.
- [ ] `.gitignore` reflects this repository's real stack and generated paths.
- [ ] Ignore rules are narrow and do not hide source, tests, docs, workflows, lockfiles, migrations, or intentional agent instructions.
- [ ] Already-tracked local artifacts are handled explicitly; `.gitignore` alone is not treated as sufficient.
- [ ] Required license notices, provenance, attribution, and meaningful technical comments are preserved.
- [ ] Git status, ignored status, staged diff, and suspicious ignore matches are reviewed.
- [ ] Tests and build checks pass after cleanup.
- [ ] Final report lists changes and evidence without claiming unverified cleanup.
