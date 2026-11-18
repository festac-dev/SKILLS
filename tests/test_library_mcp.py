"""Verify MCP discovery, bounded reads, continuation and external dataset isolation."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

class LibraryMCPTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.dataset = self.root / 'external-dataset'
        self.guide = self.dataset / 'example/SKILL.md'
        self.guide.parent.mkdir(parents=True)
        self.guide.write_text('# Interface\n\n## Keyboard\nUse visible keyboard focus.\n\n## Motion\nReduce distracting movement.\n')
        (self.dataset / 'runtime').mkdir()
        (self.dataset / 'runtime/index.json').write_text(json.dumps({'skills': [{'id': 'example', 'description': 'Accessible keyboard interface and motion', 'path': 'example/SKILL.md'}]}))
        self.entry = self.root / 'agent/skills/skills-library'
        (self.entry / 'scripts').mkdir(parents=True)
        for script in ('skills.mjs', 'mcp-server.mjs'):
            shutil.copy2(ROOT / 'scripts' / script, self.entry / 'scripts' / script)
        (self.entry / 'library.json').write_text(json.dumps({'repository': 'test/fixture', 'ref': 'fixture', 'sourceVariable': 'TEST_LIBRARY_SOURCE', 'checkoutDepth': 1, 'registry': 'COLLECTIONS.json', 'indexPath': 'runtime/index.json'}))
        (self.entry / '.library-source').write_text(str(self.dataset))
        self.env = {k: v for k, v in os.environ.items() if k != 'TEST_LIBRARY_SOURCE'}

    def run_reader(self, *arguments, succeeds=True):
        result = subprocess.run(['node', str(self.entry / 'scripts/skills.mjs'), *map(str, arguments)], capture_output=True, text=True, env=self.env, timeout=10)
        self.assertEqual(result.returncode == 0, succeeds, result.stderr)
        return json.loads(result.stdout) if succeeds else result

    def test_find_and_read_keep_dataset_and_index_external(self):
        found = self.run_reader('find', 'keyboard')
        self.assertEqual([r['id'] for r in found['matches']], ['example'])
        read = self.run_reader('read', 'example', '--section', 'Keyboard')
        self.assertIn('visible keyboard focus', read['content'])
        self.assertNotIn('distracting', read['content'])
        self.assertEqual(Path(read['path']), self.guide)
        self.assertFalse((self.entry / 'index.json').exists())
        self.assertFalse((self.entry / 'example').exists())

    def test_long_unicode_line_can_be_read_without_skipping_characters(self):
        expected = '🎬界' * 6000
        self.guide.write_text(expected)
        parts, continuation = [], {'offset': 0, 'column': 0}
        for _ in range(10):
            page = self.run_reader('read', 'example', '--offset', continuation['offset'], '--column', continuation['column'])
            self.assertLessEqual(len(page['content'].encode()), 10000)
            parts.append(page['content'])
            continuation = page['next']
            if continuation is None: break
        self.assertIsNone(continuation)
        self.assertEqual(''.join(parts), expected)

    def test_traversal_and_external_symlinks_are_rejected(self):
        outside = self.root / 'private.txt'
        outside.write_text('Private fixture')
        self.run_reader('read', 'example', '--file', '../../private.txt', succeeds=False)
        (self.guide.parent / 'link.txt').symlink_to(outside)
        self.run_reader('read', 'example', '--file', 'link.txt', succeeds=False)
        self.run_reader('find', 'keyboard', '--file', 'x', succeeds=False)
        self.run_reader('read', 'example', '--limit', 1000, succeeds=False)

    def test_code_fence_headings_are_not_sections(self):
        self.guide.write_text('# Real\n```sh\n# Fake\n```\n## Actual\nText\n')
        page = self.run_reader('read', 'example')
        self.assertEqual([h['title'] for h in page['outline']], ['Real', 'Actual'])

    def test_real_stdio_mcp_initialize_list_find_read_and_invalid_arguments(self):
        requests = [
            {'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {'protocolVersion': '2024-11-05', 'capabilities': {}, 'clientInfo': {'name': 'test', 'version': '1'}}},
            {'jsonrpc': '2.0', 'method': 'notifications/initialized'},
            {'jsonrpc': '2.0', 'id': 2, 'method': 'tools/list'},
            {'jsonrpc': '2.0', 'id': 3, 'method': 'tools/call', 'params': {'name': 'find', 'arguments': {'query': 'keyboard', 'limit': 2}}},
            {'jsonrpc': '2.0', 'id': 4, 'method': 'tools/call', 'params': {'name': 'read', 'arguments': {'id': 'example', 'section': 'Keyboard'}}},
            {'jsonrpc': '2.0', 'id': 5, 'method': 'tools/call', 'params': {'name': 'read', 'arguments': {'id': 'example', 'limit': -1}}},
        ]
        result = subprocess.run(['node', str(self.entry / 'scripts/mcp-server.mjs')], input='\n'.join(map(json.dumps, requests))+'\n', text=True, capture_output=True, env=self.env, timeout=15)
        self.assertEqual(result.returncode, 0, result.stderr)
        replies = {row['id']: row for row in map(json.loads, result.stdout.splitlines())}
        self.assertEqual(replies[1]['result']['protocolVersion'], '2024-11-05')
        self.assertEqual([t['name'] for t in replies[2]['result']['tools']], ['find', 'read'])
        self.assertEqual(replies[3]['result']['structuredContent']['matches'][0]['id'], 'example')
        self.assertIn('visible keyboard focus', replies[4]['result']['structuredContent']['content'])
        self.assertEqual(replies[5]['error']['code'], -32602)

if __name__ == '__main__': unittest.main()
