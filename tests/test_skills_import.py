"""Verify skill names, duplicate detection and complete supporting resources."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tarfile
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]

class SkillsImportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.work = self.base / 'external-import-work'
        self.work.mkdir()
        self.dataset = self.base / 'external-dataset'
        self.dataset.mkdir()
        with patch.dict('os.environ', {'SKILLS_IMPORT_WORK': str(self.work)}):
            spec = importlib.util.spec_from_file_location('skills_import', ROOT / 'scripts/import_skills_sh.py')
            self.importer = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(self.importer)
        self.importer.ROOT = self.dataset

    def test_names_follow_daem_style_and_resolve_collisions(self):
        name = self.importer.skill_name('azure-deploy', 'microsoft/azure-skills', set())
        self.assertEqual(name, 'skills-azure-deploy')
        self.assertEqual(self.importer.skill_name('azure-deploy', 'microsoft/azure-skills', {name}), 'skills-microsoft-azure-deploy')
        long = self.importer.skill_name('very-long-name-' * 20, 'owner/repository', set())
        self.assertLessEqual(len(long), 64)
        self.assertFalse(long.startswith('skills-sh-'))

    def test_index_refreshes_counts_from_inventory_and_preserves_readme_text(self):
        spec = importlib.util.spec_from_file_location('library_builder', ROOT / 'scripts/build_library.py')
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        scripts = self.dataset / 'scripts'
        scripts.mkdir()
        for name in ('skills.mjs', 'mcp-server.mjs', 'setup-mcp.mjs'):
            (scripts / name).write_text('// fixture ' + name + '\n')
        (self.dataset / 'SKILL.md').write_text('# Core\n')
        (self.dataset / 'motion-studio').mkdir()
        (self.dataset / 'motion-studio/SKILL.md').write_text('# Motion\n')
        rows = []
        for i in range(3):
            guide = self.dataset / f'fixture/topic-{i}/SKILL.md'
            guide.parent.mkdir(parents=True)
            guide.write_text(f'# Topic {i}\n')
            rows.append({'name': f'skills-topic-{i}', 'upstream_name': f'topic-{i}', 'description': 'Fixture', 'path': guide.relative_to(self.dataset).as_posix()})
        (self.dataset / 'COLLECTIONS.json').write_text(json.dumps({'skills': rows, 'collections': [{'skill_count': 3, 'import_source': 'skills.sh'}]}))
        readme = self.dataset / 'README.md'
        readme.write_text('# Library\n\nSKILLS contains **99 skills**: stale count.\n\nPreserve these reader notes.\n')
        (self.dataset / 'reports').mkdir()
        (self.dataset / 'reports/SKILLS_SH_IMPORT.json').write_text(json.dumps({'total_library_skills': 5, 'added_skills_this_batch': 2}))
        builder.build(self.dataset)
        text = readme.read_text()
        self.assertIn('**5 skills**: 3 imported skills and two core skills', text)
        self.assertIn('latest batch added **2 skills**', text)
        self.assertNotIn('99 skills', text)
        self.assertIn('Preserve these reader notes.', text)

    def test_import_skips_existing_source_bytes_and_preserves_resources_and_licence(self):
        source = self.base / 'source'
        source.mkdir()
        licence = 'MIT License\nCopyright Fixture\nPermission is hereby granted, free of charge, to any person obtaining a copy.\n'
        (source / 'LICENSE').write_text(licence)
        raw = {}
        for name in ('duplicate', 'new-topic'):
            folder = source / 'skills' / name
            (folder / 'scripts').mkdir(parents=True)
            body = f'---\nname: {name}\ndescription: Guidance for {name}\n---\n\n# {name}\nUse [helper](scripts/helper.py).\n'
            (folder / 'SKILL.md').write_text(body)
            (folder / 'scripts/helper.py').write_text('print("fixture")\n')
            raw[name] = hashlib.sha256(body.encode()).hexdigest()
        (self.dataset / 'COLLECTIONS.json').write_text(json.dumps({'schema_version': 1, 'collections': [{'directory': 'existing', 'repository': 'other/source'}], 'skills': [{'collection': 'existing', 'name': 'old-duplicate', 'upstream_name': 'duplicate', 'source_sha256': raw['duplicate']}]}))
        (self.work / 'archives').mkdir()
        archive = self.work / 'archives/example--skills.tar.gz'
        with tarfile.open(archive, 'w:gz') as tar: tar.add(source, arcname='source')
        metadata = [{'repository': 'example/skills', 'revision': 'a'*40, 'requested': ['*'], 'archive_sha256': hashlib.sha256(archive.read_bytes()).hexdigest()}]
        (self.work / 'fetched-sources.json').write_text(json.dumps(metadata))
        self.importer.run()
        result = json.loads((self.work / 'import-result.json').read_text())
        self.assertEqual([r['name'] for r in result['added']], ['skills-new-topic'])
        self.assertIn('duplicate', result['decisions'][0]['duplicate_source_skills'])
        folder = self.dataset / 'example-skills'
        self.assertEqual((folder / 'LICENSE').read_text(), licence)
        self.assertTrue((folder / 'skills/new-topic/scripts/helper.py').is_file())
        self.assertFalse((folder / 'skills/duplicate/SKILL.md').exists())

if __name__ == '__main__': unittest.main()
