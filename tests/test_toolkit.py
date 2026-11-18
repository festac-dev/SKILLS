"""Regression checks for revision safety, routing, and evidence integrity."""

import importlib.util
import os
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("toolkit", ROOT / "scripts/toolkit.py")
toolkit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(toolkit)


class ToolkitTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=ROOT.parent)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "toolkit"
        collection_dirs = {c["directory"] for c in json.loads((ROOT / "COLLECTIONS.json").read_text())["collections"]}
        def copy_fixture(source, destination):
            # Imported snapshots are read-only in these core tests; copy mutated core files.
            rel = Path(source).relative_to(ROOT)
            if rel.parts[0] in collection_dirs:
                os.link(source, destination)
                return destination
            return shutil.copy2(source, destination)
        def ignore_fixture(directory, names):
            rel = Path(directory).relative_to(ROOT)
            if rel.parts and rel.parts[0] in collection_dirs:
                return set(names) & {"__pycache__", ".pytest_cache"}
            return set(names) & {"__pycache__", ".pytest_cache", ".git", "dist"}
        shutil.copytree(ROOT, self.root, copy_function=copy_fixture, ignore=ignore_fixture)

    def test_real_toolkit_passes(self):
        self.assertEqual(toolkit.validate(self.root), [])

    def test_broken_link_is_detected(self):
        path = self.root / "README.md"
        path.write_text(path.read_text() + "\n[Missing](does-not-exist.md)\n")
        self.assertTrue(any("Broken link" in error for error in toolkit.validate(self.root)))

    def test_route_cannot_escape_root(self):
        path = self.root / "orchestrator/ROUTES.json"
        data = json.loads(path.read_text())
        data["routes"][0]["resources"].append("../../outside.md")
        path.write_text(json.dumps(data))
        self.assertTrue(any("Invalid route target" in error for error in toolkit.validate(self.root)))

    def test_authorized_revision_does_not_require_append_only_content(self):
        path = self.root / "specialists/product-strategy.md"
        path.write_text(path.read_text().replace("product", "changed", 1))
        self.assertFalse(any("Original content is not preserved" in error for error in toolkit.validate(self.root)))

    def test_missing_original_resource_is_detected(self):
        (self.root / "specialists/product-strategy.md").unlink()
        self.assertIn("Baseline resource is missing: specialists/product-strategy.md", toolkit.validate(self.root))

    def test_historical_preservation_check_is_explicit(self):
        errors = toolkit.validate(self.root, preserve_baseline=True)
        self.assertIn("Original content is not preserved: README.md", errors)

    def test_duplicate_heading_is_detected(self):
        path = self.root / "orchestrator/GLOBAL_RULES.md"
        path.write_text(path.read_text() + "\n## When to use\nDuplicate.\n")
        self.assertTrue(any("Duplicate headings" in error for error in toolkit.validate(self.root)))

    def test_new_guide_requires_evaluation(self):
        path = self.root / "references/new-example.md"
        path.write_text("# New Example\n")
        self.assertTrue(any("without evaluations" in error for error in toolkit.validate(self.root)))

    def test_links_cannot_escape_root(self):
        outside = self.root.parent / "outside.md"
        outside.write_text("# Outside\n")
        with self.assertRaisesRegex(ValueError, "escapes toolkit"):
            toolkit.local_target(self.root, "README.md", "../outside.md")

    def test_symlink_source_is_rejected(self):
        (self.root / "references/link.md").symlink_to(self.root / "README.md")
        with self.assertRaisesRegex(ValueError, "Symlink"):
            toolkit.source_files(self.root)

    def test_duplicate_content_is_detected(self):
        source = self.root / "references/architecture-decision-records.md"
        (self.root / "references/duplicate-copy.md").write_text(source.read_text())
        self.assertTrue(any("Duplicate content" in error for error in toolkit.validate(self.root)))

    def test_same_reference_title_is_detected_with_different_content(self):
        source = self.root / "references/architecture-decision-records.md"
        (self.root / "references/duplicate-topic.md").write_text(source.read_text() + "\nDistinct body content.\n")
        self.assertTrue(any("Duplicate resource title" in error for error in toolkit.validate(self.root)))

    def test_retired_alias_cannot_be_reintroduced(self):
        record = json.loads((self.root / "reports/CLAUDE_MERGE_MAP.json").read_text())
        old = next(name for name in record["retiredAliases"] if name.startswith("specialists/"))
        (self.root / old).write_text("# Retired resource\nReintroduced copy.\n")
        self.assertIn(f"Retired resource was recreated: {old}", toolkit.validate(self.root))

    def test_retired_caller_is_detected(self):
        record = json.loads((self.root / "reports/CLAUDE_MERGE_MAP.json").read_text())
        old = next(name for name in record["retiredAliases"] if name.startswith("specialists/"))
        path = self.root / "README.md"
        path.write_text(path.read_text() + "\nRead `" + old + "`.\n")
        self.assertIn(f"Retired resource reference: README.md -> {old}", toolkit.validate(self.root))

    def test_example_assets_do_not_allow_arbitrary_root_javascript(self):
        (self.root / "examples/fixture.html").write_text("<!doctype html><title>Fixture</title>")
        self.assertIn("examples/fixture.html", toolkit.source_files(self.root))
        (self.root / "unexpected.js").write_text("void 0;\n")
        with self.assertRaisesRegex(ValueError, "Unexpected root file"):
            toolkit.source_files(self.root)

    def test_missing_import_target_is_rejected(self):
        (self.root / "AGENTS.md").unlink()
        self.assertTrue(any("Invalid imported resource target: AGENTS.md" in error for error in toolkit.validate(self.root)))

    def test_index_is_repeatable_and_refreshes_manifest(self):
        path = self.root / "README.md"
        path.write_text(path.read_text() + "\nA maintained description.\n")
        self.assertIn("Machine manifest is stale; run index", toolkit.validate(self.root))
        toolkit.index(self.root)
        first = (self.root / "manifest.json").read_bytes()
        toolkit.index(self.root)
        self.assertEqual(first, (self.root / "manifest.json").read_bytes())
        self.assertEqual(toolkit.validate(self.root), [])

    def test_five_routes_and_environment_supplement(self):
        routes = toolkit.registry(self.root)
        for task, expected in toolkit.DRY_RUNS:
            with self.subTest(task=task):
                self.assertEqual(toolkit.route_task(task, routes)["primary"], expected)
        result = toolkit.route_task("Build a TUI on Termux", routes)
        self.assertEqual(result["resources"][0], "references/termux-and-constrained-environments.md")

    def test_near_ordinary_word_does_not_activate_blockchain(self):
        result = toolkit.route_task("Prepare a demo near a deadline", toolkit.registry(self.root))
        self.assertNotEqual(result["primary"], "cross-chain")

    def test_code_fences_do_not_create_document_headings(self):
        self.assertEqual(toolkit.headings("# Guide\n```python\n# comment\n```\n## End\n"), ["Guide", "End"])

    def test_passed_behavior_requires_evidence(self):
        path = self.root / "evals/SKILL_EVALS.json"
        data = json.loads(path.read_text())
        case = data["suites"][0]["cases"][0]
        case["status"] = "passed"
        path.write_text(json.dumps(data))
        self.assertIn(f"Executed eval needs evidence: {case['id']}", toolkit.validate(self.root))

    def test_missing_behavior_artifact_is_detected(self):
        path = self.root / "evals/SKILL_EVALS.json"
        data = json.loads(path.read_text())
        data["suites"][0]["cases"][0].update(status="failed", evidence="../reports/missing.md")
        path.write_text(json.dumps(data))
        self.assertTrue(any("Broken link" in error for error in toolkit.validate(self.root)))

    def test_invalid_behavior_status_is_reported_without_crashing(self):
        path = self.root / "evals/SKILL_EVALS.json"
        data = json.loads(path.read_text())
        data["suites"][0]["cases"][0]["status"] = {"passed": True}
        path.write_text(json.dumps(data))
        self.assertTrue(any("Invalid eval status" in error for error in toolkit.validate(self.root)))


class DiscoveryTests(unittest.TestCase):
    def test_route_cases_cover_expected_inclusions_and_exclusions(self):
        results = toolkit.routing_checks(ROOT, toolkit.registry(ROOT))
        self.assertGreaterEqual(len(results), 20)
        self.assertEqual([row for row in results if not row["passed"]], [])

    def test_environment_never_displaces_the_actual_task(self):
        result = toolkit.route_task("Fix an API on a Termux Android host with low-RAM offline build", toolkit.registry(ROOT))
        self.assertEqual(result["primary"], "backend")
        self.assertEqual(result["resources"][0], "references/termux-and-constrained-environments.md")

    def test_compound_design_request_exposes_relevant_candidates(self):
        result = toolkit.route_task("Create a logo and visual identity with autoplay animation", toolkit.registry(ROOT))
        self.assertIn("brand", result["candidates"])
        self.assertIn("graphics", result["candidates"])
        self.assertIn("skip", result)

    def test_search_finds_a_domain_without_a_primary_route(self):
        rows = toolkit.search_resources(ROOT, "healthcare")
        self.assertEqual(rows[0]["resource"], "specialists/healthcare-product-safety.md")

    def test_unknown_search_has_no_fabricated_match(self):
        self.assertEqual(toolkit.search_resources(ROOT, "zznonexistenttokenzz"), [])

    def test_audit_is_read_only_and_fingerprints_actual_files(self):
        import hashlib
        result = toolkit.audit(ROOT)
        row = next(row for row in result["files"] if row["path"] == "SKILL.md")
        self.assertEqual(row["sha256"], hashlib.sha256((ROOT / "SKILL.md").read_bytes()).hexdigest())
        self.assertEqual(result["sources"], len(result["files"]))
        self.assertGreater(result["behavioral_statuses"]["not_run"], 0)

    def test_malformed_route_registry_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "orchestrator").mkdir()
            path = root / "orchestrator/ROUTES.json"
            for malformed in ([], {"schema_version": 1, "routes": [None]},
                              {"schema_version": 1, "routes": [{"id": "bad", "keywords": "API"}]}):
                with self.subTest(malformed=malformed):
                    path.write_text(json.dumps(malformed))
                    with self.assertRaises(ValueError):
                        toolkit.registry(root)


if __name__ == "__main__":
    unittest.main()
