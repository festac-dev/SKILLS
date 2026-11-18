# Imported Skill Collections

The collections below are stored directly under SKILLS. Each retains its skills and supporting source files, scripts, assets and license notices. Skills have collection-prefixed names so similarly named skills can coexist. No owner mapping or merged capability layer is used.

| Local collection | Upstream repository | Skills |
|---|---|---|
| [openai-plugins](openai-plugins/README.md) | [openai/plugins](https://github.com/openai/plugins) | 541 |
| [anthropic-skills](anthropic-skills/README.md) | [anthropics/skills](https://github.com/anthropics/skills) | 20 |
| [vercel-agent-skills](vercel-agent-skills/README.md) | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | 9 |
| [jeffallan-skills](jeffallan-skills/README.md) | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | 67 |
| [alireza-skills](alireza-skills/README.md) | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 495 |
| [superpowers](superpowers/README.md) | [obra/superpowers](https://github.com/obra/superpowers) | 15 |
| [awesome-copilot](awesome-copilot/README.md) | [github/awesome-copilot](https://github.com/github/awesome-copilot) | 482 |
| [scientific-agent-skills](scientific-agent-skills/README.md) | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 177 |
| [awesome-claude-skills](awesome-claude-skills/README.md) | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 864 |
| [motionmaxxing](motionmaxxing/README.md) | [Tejashmakwana/motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing) | 1 |
| [impeccable](impeccable/README.md) | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 26 |
| [threejs-full-stack](threejs-full-stack/README.md) | [full-stack-skills/threejs-skills](https://github.com/full-stack-skills/threejs-skills) | 30 |
| [stitch-skills](stitch-skills/README.md) | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 16 |
| [video-shotcraft](video-shotcraft/README.md) | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 1 |
| [media2threejs](media2threejs/README.md) | [promptwhisper/media2threejs](https://github.com/promptwhisper/media2threejs) | 1 |
| [gamedev-skills](gamedev-skills/README.md) | [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | 80 |
| [unslop](unslop/README.md) | [heydamir/unslop](https://github.com/heydamir/unslop) | 1 |
| [unslopovich](unslopovich/README.md) | [erkamyaman/unslopovich](https://github.com/erkamyaman/unslopovich) | 1 |
| [demo-video-capture](demo-video-capture/README.md) | [surajshetty3416/demo-video-skill](https://github.com/surajshetty3416/demo-video-skill) | 1 |
| [demo-video-narrated](demo-video-narrated/README.md) | [ajanaku1/demo-video-skill](https://github.com/ajanaku1/demo-video-skill) | 1 |
| [narova](narova/README.md) | [ammar-hasan/narova](https://github.com/ammar-hasan/narova) | 8 |
| [mediagen](mediagen/README.md) | [Cripacx/mediagen](https://github.com/Cripacx/mediagen) | 1 |
| [anti-defensive-writing](anti-defensive-writing/README.md) | [Kiterlin/anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing) | 2 |
| [origami-3d](origami-3d/README.md) | [lejrimostfa/Origami-3Dfolder-ai](https://github.com/lejrimostfa/Origami-3Dfolder-ai) | 1 |

## Find a skill

```sh
python3 scripts/skill_collections.py list
python3 scripts/skill_collections.py search 'PDF editing'
python3 scripts/skill_collections.py search 'React performance'
python3 scripts/skill_collections.py validate
```

Search returns the skill's direct local path. Read that `SKILL.md` and the relevant bundled references for the task. Apply [collection rules](COLLECTION_RULES.md), including the user's current scope, authorization, documentation and publication preferences.

Upstream host instruction/configuration files are retained with `UPSTREAM_` names rather than activated. Directory aliases are recorded in the [source inventory](COLLECTIONS.json); their real target content is retained. Connector manifests and installer scripts are source material and have not been executed by this import. Check dependencies and tool access before using a tool-specific skill.

The source inventory records pinned revisions and source/installed digests. License and notice files remain in their collections. Upstream claims and examples remain attributed source content; static import validation does not establish live provider behavior.
