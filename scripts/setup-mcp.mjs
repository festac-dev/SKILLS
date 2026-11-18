#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import {fileURLToPath} from 'node:url';

const location = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const installed = fs.existsSync(path.join(location, 'library.json'));
const library = installed ? JSON.parse(fs.readFileSync(path.join(location, 'library.json'), 'utf8')) : null;
const repository = installed ? null : location;
const daem = installed ? library.repository.endsWith('/Daem') : fs.existsSync(path.join(repository, 'SOURCES.json'));
const name = daem ? 'daem' : 'skills-library';
const entry = installed ? location : path.join(repository, daem ? 'skills/daem' : 'skills-library');
const server = path.join(entry, 'scripts/mcp-server.mjs');
const variable = daem ? 'DAEM_LIBRARY_SOURCE' : 'SKILLS_LIBRARY_SOURCE';
const marker = path.join(entry, '.library-source');
const source = repository || (fs.existsSync(marker) ? fs.readFileSync(marker, 'utf8').trim() : null);
const environment = source ? {[variable]: source} : {};
const managed = args => Array.isArray(args) && args.length === 1 && String(args[0]).replaceAll('\\', '/').endsWith(`/${name}/scripts/mcp-server.mjs`);
const args = process.argv.slice(2);
const dryRun = args.includes('--dry-run');
const selected = args.filter(arg => arg !== '--dry-run');
const all = !selected.length || selected.includes('--all');
if (args.includes('--help')) { process.stdout.write('Usage: node scripts/setup-mcp.mjs [--all|--codex|--claude-code|--opencode] [--dry-run]\nRegisters the read-only find/read MCP server globally; preserves other servers.\n'); process.exit(0); }
if (selected.some(arg => !['--all', '--codex', '--claude-code', '--opencode'].includes(arg))) throw new Error('Unknown option');
if (!fs.existsSync(server)) throw new Error('Build the library package before registering MCP');
const profile = process.env.FESTAC_MCP_CONFIG_ROOT;
const home = profile ? path.resolve(profile) : os.homedir();
const changes = [];
function jsonChange(file, transform) {
  const original = fs.existsSync(file) ? fs.readFileSync(file, 'utf8') : null;
  const data = original ? JSON.parse(original) : {};
  transform(data);
  const text = JSON.stringify(data, null, 2) + '\n';
  changes.push({file, original, text});
}
if (all || selected.includes('--claude-code')) {
  jsonChange(path.join(home, '.claude.json'), data => {
    data.mcpServers ||= {};
    const old = data.mcpServers[name];
    if (old && !managed(old.args)) throw new Error(`Existing Claude MCP server preserved: ${name}`);
    data.mcpServers[name] = {command: process.execPath, args: [server], env: {...old?.env, ...environment}};
  });
}
if (all || selected.includes('--opencode')) {
  const directory = path.join((!profile && process.env.XDG_CONFIG_HOME) || path.join(home, '.config'), 'opencode');
  const file = path.join(directory, 'opencode.json');
  if (!fs.existsSync(file) && fs.existsSync(path.join(directory, 'opencode.jsonc'))) throw new Error('OpenCode uses opencode.jsonc; register the server there to preserve its comments');
  jsonChange(file, data => {
    data.mcp ||= {};
    const old = data.mcp[name];
    if (old && !managed(old.command?.slice(1))) throw new Error(`Existing OpenCode MCP server preserved: ${name}`);
    data.mcp[name] = {type: 'local', command: [process.execPath, server], environment: {...old?.environment, ...environment}, enabled: true};
  });
}
if (all || selected.includes('--codex')) {
  const file = path.join((!profile && process.env.CODEX_HOME) || path.join(home, '.codex'), 'config.toml');
  const original = fs.existsSync(file) ? fs.readFileSync(file, 'utf8') : null;
  const marker = `[mcp_servers."${name}"]`;
  if (original && (original.includes(marker) || original.includes(`[mcp_servers.${name}]`))) {
    const header = original.includes(marker) ? marker : `[mcp_servers.${name}]`;
    const start = original.indexOf(header) + header.length;
    const block = original.slice(start).split(/\n\[/)[0];
    let previous;
    try { previous = JSON.parse(block.match(/^\s*args\s*=\s*(.+)$/m)?.[1]); } catch {}
    if (!managed(previous)) throw new Error(`Existing Codex MCP server preserved: ${name}`);
    const updated = block.replace(/^\s*command\s*=.*$/m, `\ncommand = ${JSON.stringify(process.execPath)}`).replace(/^\s*args\s*=.*$/m, `\nargs = ${JSON.stringify([server])}`);
    changes.push({file, original, text: original.slice(0, start) + updated + original.slice(start + block.length)});
  } else {
    const env = source ? `\n[mcp_servers."${name}".env]\n${variable} = ${JSON.stringify(source)}\n` : '';
    const addition = `\n${marker}\ncommand = ${JSON.stringify(process.execPath)}\nargs = ${JSON.stringify([server])}\n${env}`;
    changes.push({file, original, text: (original || '') + addition});
  }
}
// Preflight every selected configuration before changing any of them.
const backup = path.join((!profile && process.env.XDG_DATA_HOME) || path.join(home, '.local/share'), 'festac-skills', 'config-backups', new Date().toISOString().replace(/[:.]/g, '-'));
for (const change of changes) {
  if (change.text === change.original) continue;
  if (!dryRun) {
    fs.mkdirSync(path.dirname(change.file), {recursive: true});
    if (change.original !== null) {
      fs.mkdirSync(backup, {recursive: true});
      fs.writeFileSync(path.join(backup, `${changes.indexOf(change)}-${path.basename(change.file)}`), change.original, {mode: 0o600});
    }
    const temporary = `${change.file}.${process.pid}.tmp`;
    fs.writeFileSync(temporary, change.text, {mode: change.original !== null ? fs.statSync(change.file).mode & 0o777 : 0o600});
    fs.renameSync(temporary, change.file);
  }
  process.stdout.write(`${dryRun ? 'Would register' : 'Registered'} ${name}: ${change.file}\n`);
}
process.stdout.write('Open a fresh agent session to load the MCP tools.\n');
