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
