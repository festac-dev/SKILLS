"""Check native installation, repeat runs, and protection of existing skills."""

import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("install", ROOT / "scripts/install.py")
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "library"
        self.source.mkdir()
        (self.source / "SKILL.md").write_text("---\nname: example\ndescription: Example\n---\n")
        (self.source / "reference.md").write_text("# Supporting file\n")
        self.dest = self.root / "skills"

    def add_mcp_fixture(self):
        package = self.source / "skills-library"
        (package / "scripts").mkdir(parents=True)
        (package / "SKILL.md").write_text("---\nname: skills-library\ndescription: Search external guidance\n---\n")
        (package / "scripts/mcp-server.mjs").write_text("// Fixture server\n")

    def test_links_preserve_supporting_files_and_repeated_install(self):
        skills = {"example": self.source}
        self.assertEqual(installer.install_links(skills, [self.dest]), 1)
        target = self.dest / "example"
        self.assertTrue(target.is_symlink())
        self.assertEqual((target / "reference.md").read_text(), "# Supporting file\n")
        self.assertEqual(installer.install_links(skills, [self.dest]), 0)

    def test_conflict_is_checked_before_any_install(self):
        self.dest.mkdir()
        conflict = self.dest / "existing"
        conflict.mkdir()
        (conflict / "keep.md").write_text("Existing user skill\n")
        with self.assertRaisesRegex(ValueError, "left untouched"):
            installer.install_links({"new": self.source, "existing": self.source}, [self.dest])
        self.assertFalse((self.dest / "new").exists())
        self.assertEqual((conflict / "keep.md").read_text(), "Existing user skill\n")

    def test_broken_link_is_preserved(self):
        self.dest.mkdir()
        target = self.dest / "example"
        target.symlink_to(self.root / "missing")
        with self.assertRaisesRegex(ValueError, "left untouched"):
            installer.install_links({"example": self.source}, [self.dest])
        self.assertTrue(target.is_symlink())

    def test_dry_run_creates_no_directory(self):
        self.assertEqual(installer.install_links({"example": self.source}, [self.dest], dry_run=True), 1)
        self.assertFalse(self.dest.exists())

    def test_source_cannot_contain_destination(self):
        with self.assertRaisesRegex(ValueError, "inside the skill source"):
            installer.install_links({"example": self.source}, [self.source / "nested"])
        self.assertFalse((self.source / "nested").exists())

    def test_missing_skill_does_not_create_links(self):
        (self.source / "SKILL.md").unlink()
        with self.assertRaisesRegex(ValueError, "Missing SKILL.md"):
            installer.install_links({"example": self.source}, [self.dest])
        self.assertFalse(self.dest.exists())

    def test_builtin_install_does_not_need_collection_registry(self):
        (self.source / "COLLECTIONS.json").write_text("not valid JSON")
        skills = installer.available_skills(self.source, include_collections=False)
        self.assertEqual(skills["professional-product-creation"], self.source)

    def test_agent_paths_support_environment_and_project_scope(self):
        with patch.dict("os.environ", {"CODEX_HOME": str(self.root / "codex"), "CLAUDE_CONFIG_DIR": str(self.root / "claude"), "XDG_CONFIG_HOME": str(self.root / "config")}):
            dirs = installer.agent_directories(self.root)
            self.assertEqual(dirs["codex"], self.root / "codex/skills")
            self.assertEqual(dirs["claude-code"], self.root / "claude/skills")
            self.assertEqual(dirs["opencode"], self.root / "config/opencode/skills")
            dirs = installer.agent_directories(self.root, project=self.root / "project")
            self.assertEqual(dirs["codex"], self.root / "project/.agents/skills")

    def test_piped_bootstrap_downloads_once_and_reuses_checkout(self):
        # A small local Git remote exercises the real pipe/download flow.
        self.add_mcp_fixture()
        (self.source / "scripts").mkdir()
        shutil.copy2(ROOT / "scripts/install-native.sh", self.source / "scripts/install-native.sh")
        (self.source / "SKILL.md").write_text("---\nname: professional-product-creation\ndescription: Example\n---\n")
        (self.source / "native-skills.tsv").write_text("professional-product-creation\tSKILL.md\tcore\n")
        (self.source / "references").mkdir()
        (self.source / "references/source.md").write_text("# Supporting file\n")
        subprocess.run(["git", "init", "-b", "main", str(self.source)], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(self.source), "add", "."], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(self.source), "-c", "user.name=Installer Test", "-c", "user.email=installer@example.invalid", "commit", "-m", "Fixture"], check=True, capture_output=True)
        env = {**os.environ, "SKILLS_REPO": str(self.source), "XDG_DATA_HOME": str(self.root / "user data")}
        env.pop("SKILLS_SOURCE", None)
        env.pop("SKILLS_REF", None)
        command = ["sh", "-s", "--", "codex", "--dest", str(self.dest)]
        result = subprocess.run(command, input=(ROOT / "install.sh").read_text(), text=True, capture_output=True, cwd=self.root, env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        installed = self.dest / "skills-library"
        self.assertFalse((installed / "SKILL.md").is_symlink())
        self.assertEqual((installed / ".library-source").read_text().strip(), str(self.root / "user data/SKILLS"))
        self.assertFalse((installed / "references").exists())
        self.assertTrue((self.root / "user data/SKILLS/references/source.md").is_file())
        shutil.rmtree(self.source)
        result = subprocess.run(command, input=(ROOT / "install.sh").read_text(), text=True, capture_output=True, cwd=self.root, env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Installed one MCP entrypoint", result.stdout)
        self.assertEqual(list((self.root / "user data").glob("*.download.*")), [])

    def test_failed_download_leaves_no_partial_checkout(self):
        env = {**os.environ, "SKILLS_REPO": str(self.root / "missing-remote"), "XDG_DATA_HOME": str(self.root / "user-data")}
        env.pop("SKILLS_SOURCE", None)
        result = subprocess.run(["sh", "-s", "--", "--dest", str(self.dest)], input=(ROOT / "install.sh").read_text(), text=True, capture_output=True, cwd=self.root, env=env)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.root / "user-data/SKILLS").exists())
        self.assertEqual(list((self.root / "user-data").glob("*.download.*")), [])
        self.assertFalse(self.dest.exists())

    def test_default_installs_one_entrypoint_without_python_on_path(self):
        self.add_mcp_fixture()
        (self.source / "scripts").mkdir()
        shutil.copy2(ROOT / "scripts/install-native.sh", self.source / "scripts/install-native.sh")
        (self.source / "SKILL.md").write_text("---\nname: professional-product-creation\ndescription: Core\n---\n")
        motion = self.source / "motion-studio"
        motion.mkdir()
        (motion / "SKILL.md").write_text("---\nname: motion-studio\ndescription: Motion\n---\n")
        imported = self.source / "collection/example"
        (imported / "assets").mkdir(parents=True)
        (imported / "SKILL.md").write_text("---\nname: imported-example\ndescription: Imported\n---\n")
        (imported / "assets/example.txt").write_text("Complete supporting asset\n")
        (self.source / "native-skills.tsv").write_text(
            "professional-product-creation\tSKILL.md\tcore\n"
            "motion-studio\tmotion-studio/SKILL.md\tcore\n"
            "imported-example\tcollection/example/SKILL.md\tcollection\n")
        tools = self.root / "tools"
        tools.mkdir()
        for name in ["bash", "cat", "dirname", "mkdir", "mktemp", "cp", "mv", "rm"]:
            (tools / name).symlink_to(shutil.which(name))
        env = {**os.environ, "PATH": str(tools), "SKILLS_SOURCE": str(self.source)}
        command = [shutil.which("sh"), str(ROOT / "install.sh"), "codex", "--dest", str(self.dest)]
        result = subprocess.run(command, env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Installed one MCP entrypoint", result.stdout)
        self.assertTrue((self.dest / "skills-library/SKILL.md").is_file())
        self.assertFalse((self.dest / "motion-studio").exists())
        self.assertFalse((self.dest / "imported-example").exists())
        self.assertTrue((imported / "assets/example.txt").is_file())
        self.assertFalse((tools / "python3").exists())
        repeat = subprocess.run(command, env=env, capture_output=True, text=True)
        self.assertEqual(repeat.returncode, 0, repeat.stderr)

    def test_native_dry_run_and_conflicts_do_not_write_skills(self):
        self.add_mcp_fixture()
        (self.source / "scripts").mkdir()
        shutil.copy2(ROOT / "scripts/install-native.sh", self.source / "scripts/install-native.sh")
        (self.source / "SKILL.md").write_text("---\nname: professional-product-creation\ndescription: Core\n---\n")
        other = self.source / "other"
        other.mkdir()
        (other / "SKILL.md").write_text("---\nname: other\ndescription: Other\n---\n")
        (self.source / "native-skills.tsv").write_text(
            "professional-product-creation\tSKILL.md\tcore\nother\tother/SKILL.md\tcollection\n")
        command = ["bash", str(self.source / "scripts/install-native.sh"), "--dest", str(self.dest)]
        preview = subprocess.run(command + ["--dry-run"], capture_output=True, text=True)
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertFalse(self.dest.exists())
        (self.dest / "skills-library").mkdir(parents=True)
        (self.dest / "skills-library/keep.txt").write_text("User skill\n")
        conflict = subprocess.run(command, capture_output=True, text=True)
        self.assertNotEqual(conflict.returncode, 0)
        self.assertFalse((self.dest / "skills-library/.library-source").exists())
        self.assertEqual((self.dest / "skills-library/keep.txt").read_text(), "User skill\n")


if __name__ == "__main__":
    unittest.main()
