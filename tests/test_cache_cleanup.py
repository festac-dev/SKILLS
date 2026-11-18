"""Exercise cleanup against real temporary files, Git indexes and processes."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/cache_cleanup.py'
SPEC = importlib.util.spec_from_file_location('cache_cleanup', SCRIPT)
cleanup = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cleanup)


@unittest.skipUnless(shutil.which('git'), 'Git is required for ownership checks')
class CleanupTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)

    def put(self, name, content='fixture'):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return path

    def test_cli_default_only_inspects(self):
        artifact = self.put('build/index.js')
        result = subprocess.run([sys.executable, str(SCRIPT), '--root', str(self.root),
                                 '--path', 'build'], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(result.stdout)['entries'][0]['files'], 1)
        self.assertTrue(artifact.exists())

    def test_apply_preserves_runtime_data_exports_and_source(self):
        self.put('build/index.js')
        retained = [self.put(name) for name in ['data/app.db', '.local/session.json',
                    'out/demo.mp4', 'src/main.ts', 'package-lock.json', 'AGENTS.md']]
        plan = cleanup.make_plan(self.root, ['build'])
        removed = cleanup.apply_plan(self.root, plan)
        self.assertEqual(len(removed), 1)
        self.assertFalse((self.root / 'build').exists())
        self.assertTrue(all(p.read_text() == 'fixture' for p in retained))

    def test_stale_plan_refuses_all_targets_before_deletion(self):
        first = self.put('build/a.js')
        second = self.put('dist/b.js')
        plan = cleanup.make_plan(self.root, ['build', 'dist'])
        second.write_text('changed after inspection')
        with self.assertRaisesRegex(ValueError, 'changed'):
            cleanup.apply_plan(self.root, plan)
        self.assertTrue(first.exists())
        self.assertTrue(second.exists())

    def test_tracked_generated_source_is_preserved(self):
        file = self.put('build/schema.ts')
        subprocess.run(['git', '-C', str(self.root), 'add', 'build/schema.ts'], check=True)
        with self.assertRaisesRegex(ValueError, 'Tracked'):
            cleanup.make_plan(self.root, ['build'])
        self.assertTrue(file.exists())

    def test_literal_git_pathspec_cannot_miss_brackets(self):
        self.put('build/[app]/schema.ts')
        subprocess.run(['git', '-C', str(self.root), 'add', '.'], check=True)
        with self.assertRaisesRegex(ValueError, 'Tracked'):
            cleanup.make_plan(self.root, ['build/[app]'])

    def test_target_and_ancestor_symlinks_are_refused(self):
        outside = self.put('kept/file.txt')
        (self.root / 'cache').symlink_to(outside.parent, target_is_directory=True)
        for name in ['cache', 'cache/file.txt']:
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, 'Symlink'):
                cleanup.make_plan(self.root, [name])
        self.assertEqual(outside.read_text(), 'fixture')

    def test_symlink_inside_cache_never_deletes_destination(self):
        outside = self.put('kept/file.txt')
        self.put('build/a.js')
        (self.root / 'build/link').symlink_to(outside.parent, target_is_directory=True)
        cleanup.apply_plan(self.root, cleanup.make_plan(self.root, ['build']))
        self.assertEqual(outside.read_text(), 'fixture')

    def test_protected_paths_and_whole_dependencies_are_refused(self):
        for name in ['.local', 'data', 'out', 'assets', '.git', '.venv', 'node_modules']:
            (self.root / name).mkdir(exist_ok=True)
            with self.subTest(name=name), self.assertRaises(ValueError):
                cleanup.make_plan(self.root, [name])

    def test_only_dependency_cache_is_removed(self):
        library = self.put('node_modules/example/index.js')
        self.put('node_modules/.vite/deps.js')
        cleanup.apply_plan(self.root, cleanup.make_plan(self.root, ['node_modules/.vite']))
        self.assertEqual(library.read_text(), 'fixture')
        with self.assertRaisesRegex(ValueError, 'Installed dependency'):
            cleanup.make_plan(self.root, ['node_modules/example'])

    def test_database_or_credentials_inside_build_are_refused(self):
        for name in ['app.db', 'PG_VERSION', '.env', '.env.production']:
            with self.subTest(name=name):
                file = self.put('build/' + name)
                with self.assertRaisesRegex(ValueError, 'marker'):
                    cleanup.make_plan(self.root, ['build'])
                file.unlink()

    def test_overlap_escape_and_wrong_root_are_refused(self):
        self.put('build/nested/a.js')
        for names in [['build', 'build/nested'], ['../outside'], ['.'], [str(self.root)]]:
            with self.subTest(names=names), self.assertRaises(ValueError):
                cleanup.make_plan(self.root, names)
        plan = cleanup.make_plan(self.root, ['build'])
        with self.assertRaisesRegex(ValueError, 'root mismatch'):
            cleanup.apply_plan(self.root / 'build', plan)

    @unittest.skipUnless(Path('/proc').is_dir(), 'Linux process inspection')
    def test_running_process_protects_its_working_directory(self):
        self.put('build/a.js')
        process = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(30)'],
                                   cwd=self.root / 'build')
        try:
            with self.assertRaisesRegex(ValueError, 'used by process'):
                cleanup.make_plan(self.root, ['build'])
        finally:
            process.terminate()
            process.wait(timeout=5)

    def test_git_failure_is_not_treated_as_untracked(self):
        self.put('build/a.js')
        failure = subprocess.CompletedProcess([], 128, '', 'fatal: detected dubious ownership')
        with patch.object(cleanup.subprocess, 'run', return_value=failure):
            with self.assertRaisesRegex(ValueError, 'Git ownership'):
                cleanup.make_plan(self.root, ['build'])

    def test_equivalent_root_alias_keeps_plan_scope(self):
        self.put('build/a.js')
        plan = cleanup.make_plan(self.root, ['build'])
        alias = self.root / 'workspace-alias'
        alias.symlink_to(self.root, target_is_directory=True)
        cleanup.apply_plan(alias, plan)
        self.assertFalse((self.root / 'build').exists())
        self.assertTrue((self.root / '.git').is_dir())


if __name__ == '__main__':
    unittest.main()
