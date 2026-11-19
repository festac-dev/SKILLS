# Claude Entry Point

Read [SKILL.md](SKILL.md) for product work and [AGENTS.md](AGENTS.md) when maintaining this library. These are shared sources; do not create a separate Claude copy of the instructions.

## AI Model Skills Discovery

Do not scan all directories or load entire collection folders in SKILLS (19,573 skills). Use the CLI discovery tool to locate and preview skills in milliseconds:

```sh
# Search for skills by topic
python3 scripts/search.py "<topic>"

# Preview a skill's instructions without reading the full file
python3 scripts/search.py --info <skill-id>
```
For the complete navigation guide, consult `SKILLS_GUIDE.md` at the repository root.

