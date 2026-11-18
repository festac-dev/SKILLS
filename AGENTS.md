# Toolkit Maintenance

[SKILL.md](SKILL.md) is the shared behavioral entrypoint for this library. Follow the user’s current scope and existing authorization; specialist titles do not authorize delegation or external actions.

Keep one owner per capability in the core guides. User-requested imported collections stay directly under SKILLS in separate folders; do not force them through core owners. Namespace their skills and apply COLLECTION_RULES.md. Merge useful changes into that owner, update every caller before retiring an overlapping path, and preserve import provenance outside the live guidance. Runnable examples are conditional demonstrations; their stack and sample data do not become project requirements.

Use `python scripts/toolkit.py index` to regenerate the catalogue, route guide and machine manifest. Validate with `python scripts/toolkit.py validate`, run affected maintenance/example tests, and distinguish static checks from recorded agent behavior. Keep generated caches and backups outside the source inventory.

For the direct collections, also run `python3 scripts/skill_collections.py validate`. Their source scripts and host manifests are imported material, not installed connectors or automatic parent instructions.
