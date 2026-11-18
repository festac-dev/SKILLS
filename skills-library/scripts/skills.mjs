#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const inside = (parent, child) => child === parent || child.startsWith(parent + path.sep);
const integer = (value, fallback, min, max) => {
  const number = value === undefined ? fallback : Number(value);
  if (!Number.isInteger(number) || number < min || number > max) throw new Error(`Expected an integer from ${min} to ${max}`);
  return number;
};
const words = value => [...new Set(String(value).toLowerCase().match(/[\p{L}\p{N}]+/gu) || [])];
const stop = new Set(['a', 'an', 'and', 'the', 'to', 'for', 'of', 'in', 'with', 'my', 'please', 'build', 'use', 'skills', 'skill']);
const output = value => process.stdout.write(JSON.stringify(value) + '\n');

async function configuration() {
  const library = JSON.parse(fs.readFileSync(path.join(root, 'library.json'), 'utf8'));
  const marker = path.join(root, '.library-source');
  const configured = process.env[library.sourceVariable] || (fs.existsSync(marker) ? fs.readFileSync(marker, 'utf8').trim() : '');
  const checkout = path.resolve(root, ...Array(library.checkoutDepth).fill('..'));
  const source = configured || (fs.existsSync(path.join(checkout, library.registry)) ? checkout : null);
  const cache = path.resolve(process.env.XDG_CACHE_HOME || path.join(os.homedir(), '.cache'), 'festac-skills', library.repository, library.ref);
  const indexPath = source ? path.join(source, library.indexPath) : path.join(cache, 'index.json');
  if (!fs.existsSync(indexPath) && !source) await fetchFile(library, library.indexPath, indexPath);
  const index = JSON.parse(fs.readFileSync(indexPath, 'utf8'));
  return {...library, source, cache, skills: index.skills};
}

function argumentsFor(args) {
  const command = args.shift();
  const values = [], options = {};
  for (let i = 0; i < args.length; i++) {
    const key = args[i];
    if (key.startsWith('--')) {
      if (!['--limit', '--offset', '--column', '--section', '--file'].includes(key) || args[i + 1] === undefined || args[i + 1].startsWith('--')) throw new Error(`Invalid option: ${key}`);
      options[key.slice(2)] = args[++i];
    } else values.push(key);
  }
  const allowed = command === 'find' ? ['limit'] : ['limit', 'offset', 'column', 'section', 'file'];
  for (const key of Object.keys(options)) if (!allowed.includes(key)) throw new Error(`${command} does not accept --${key}`);
  return {command, values, options};
}

function outlineFor(lines) {
  const outline = [];
  let fence = null;
  for (let offset = 0; offset < lines.length; offset++) {
    const marker = lines[offset].match(/^\s{0,3}(`{3,}|~{3,})/);
    if (marker) {
      if (!fence) fence = marker[1];
      else if (marker[1][0] === fence[0] && marker[1].length >= fence.length) fence = null;
      continue;
    }
    const heading = !fence && lines[offset].match(/^(#{1,6})\s+(.+?)\s*#*\s*$/);
    if (heading) outline.push({title: heading[2].slice(0, 160), offset, level: heading[1].length});
  }
  return outline;
}

async function fetchFile(config, repositoryPath, target, digest) {
  const url = `https://raw.githubusercontent.com/${config.repository}/${encodeURIComponent(config.ref)}/${repositoryPath.split('/').map(encodeURIComponent).join('/')}`;
  const response = await fetch(url, {signal: AbortSignal.timeout(30000)});
  if (!response.ok) throw new Error(`Could not download ${repositoryPath}: HTTP ${response.status}`);
  const chunks = [];
  let bytes = 0;
  for await (const chunk of response.body) {
    bytes += chunk.length;
    if (bytes > 64 * 1024 * 1024) throw new Error('Supporting file exceeds the 64 MiB download limit');
    chunks.push(Buffer.from(chunk));
  }
  const content = Buffer.concat(chunks);
  if (digest && crypto.createHash('sha256').update(content).digest('hex') !== digest) throw new Error('Downloaded guide does not match its pinned index');
  fs.mkdirSync(path.dirname(target), {recursive: true});
  const temporary = `${target}.${process.pid}.${crypto.randomBytes(4).toString('hex')}.tmp`;
  try { fs.writeFileSync(temporary, content); fs.renameSync(temporary, target); }
  finally { if (fs.existsSync(temporary)) fs.unlinkSync(temporary); }
}

async function locate(config, entry, filename) {
  const sourceRoot = config.source ? fs.realpathSync(config.source) : path.join(config.cache, 'data');
  const download = !config.source;
  const guide = path.resolve(sourceRoot, entry.path);
  const file = filename === undefined ? guide : path.resolve(path.dirname(guide), filename);
  if (filename !== undefined && (path.isAbsolute(filename) || filename.includes('\\'))) throw new Error('Use a relative supporting-file path');
  if (!inside(sourceRoot, guide) || !inside(sourceRoot, file)) throw new Error('File path escapes the library');
  // Cache directories may already exist: resolve their nearest existing ancestor
  // before downloading, so a symlink cannot redirect a write outside the cache.
  let ancestor = file;
  while (!fs.existsSync(ancestor)) ancestor = path.dirname(ancestor);
  if (fs.existsSync(sourceRoot) && !inside(fs.realpathSync(sourceRoot), fs.realpathSync(ancestor))) throw new Error('File path follows a symlink outside the library');
  if (!fs.existsSync(file) && download) await fetchFile(config, path.relative(sourceRoot, file).split(path.sep).join('/'), file, file === guide ? entry.sha256 : undefined);
  if (!fs.existsSync(file)) throw new Error('Supporting file is unavailable. Use --file to select a bundled file or install a complete checkout for offline use.');
  const actualRoot = fs.realpathSync(sourceRoot), actualFile = fs.realpathSync(file);
  if (!inside(actualRoot, actualFile)) throw new Error('File path follows a symlink outside the library');
  if (!fs.statSync(actualFile).isFile()) throw new Error('Requested path is not a file');
  return {file: actualFile, baseDirectory: path.dirname(guide), sourceRoot: actualRoot};
}

function pageFor(lines, offset, column, end, limit) {
  let content = '', bytes = 0, line = offset, position = column, completed = 0;
  while (line < end && completed < limit) {
    const remaining = lines[line].slice(position);
    let hitLimit = false;
    for (const character of remaining) {
      const size = Buffer.byteLength(character);
      if (bytes + size > 10000) { hitLimit = true; break; }
      content += character; bytes += size; position += character.length;
    }
    if (hitLimit) break;
    line++; position = 0; completed++;
    if (line < end && completed < limit) {
      if (bytes + 1 > 10000) break;
      content += '\n'; bytes++;
    }
  }
  return {content, next: line < end ? {offset: line, column: position} : null};
}

try {
  const {command, values, options} = argumentsFor(process.argv.slice(2));
  const config = await configuration();
  const entries = config.skills;
  if (!command || command === '--help') {
    output({usage: ['find "topic" --limit 5', 'read <id> --offset 0 --limit 80', 'read <id> --section "title"', 'read <id> --file references/example.md', 'read <id> --offset <next.offset> --column <next.column>'], skills: entries.length});
  } else if (command === 'find') {
    const query = values.join(' ').trim();
    if (!query || query.length > 500) throw new Error('find requires a topic of 1 to 500 characters');
    const tokens = words(query).filter(token => !stop.has(token));
    const limit = integer(options.limit, 5, 1, 12);
    const documents = entries.map(entry => ({entry, title: words(`${entry.id} ${entry.name || ''} ${entry.purpose || ''}`), description: words(entry.description)}));
    const frequencies = new Map(tokens.map(token => [token, documents.filter(doc => doc.title.includes(token) || doc.description.includes(token)).length]));
    const matches = documents.map(({entry, title, description}) => {
      const score = tokens.reduce((sum, token) => sum + Math.log(1 + entries.length / (1 + frequencies.get(token))) * ((title.includes(token) ? 5 : 0) + (description.includes(token) ? 1 : 0)), entry.id === query ? 1000 : 0);
      return {id: entry.id, description: String(entry.description).slice(0, 240), score: Math.round(score * 100) / 100};
    }).filter(entry => entry.score > 0).sort((a, b) => b.score - a.score || a.id.localeCompare(b.id)).slice(0, limit);
    output({query, matches});
  } else if (command === 'read') {
    if (values.length !== 1) throw new Error('read requires one skill ID');
    const entry = entries.find(entry => entry.id === values[0]);
    if (!entry) throw new Error('Unknown skill ID. Use find to select an ID.');
    const limit = integer(options.limit, 80, 1, 160);
    const location = await locate(config, entry, options.file);
    const bytes = fs.statSync(location.file).size;
    const descriptor = fs.openSync(location.file, 'r');
    const sample = Buffer.alloc(Math.min(bytes, 8192));
    try { fs.readSync(descriptor, sample); } finally { fs.closeSync(descriptor); }
    if (sample.includes(0) || /\.(png|jpe?g|gif|webp|avif|pdf|mp[34]|mov|woff2?|ttf|zip|gz|glb)$/i.test(location.file)) {
      output({id: entry.id, path: location.file, baseDirectory: location.baseDirectory, bytes, binary: true});
    } else {
      if (bytes > 64 * 1024 * 1024) throw new Error('Text file exceeds the 64 MiB read limit');
      const lines = fs.readFileSync(location.file, 'utf8').split(/\r?\n/);
      const outline = outlineFor(lines);
      let offset = integer(options.offset, 0, 0, lines.length - 1), end = lines.length;
      if (options.section !== undefined) {
        const query = options.section.toLowerCase();
        const section = outline.find(item => item.title.toLowerCase() === query) || outline.find(item => item.title.toLowerCase().includes(query));
        if (!section) throw new Error('Section not found. Read the outline to choose a section.');
        if (options.offset === undefined) offset = section.offset;
        end = outline.find(item => item.offset > section.offset && item.level <= section.level)?.offset ?? end;
        if (offset < section.offset || offset >= end) throw new Error('Offset is outside the selected section');
      }
      const column = integer(options.column, 0, 0, lines[offset].length);
      const page = pageFor(lines, offset, column, end, limit);
      output({id: entry.id, path: location.file, baseDirectory: location.baseDirectory, totalLines: lines.length, offset, column, next: page.next, outline: outline.slice(0, 20), ...page});
    }
  } else throw new Error(`Unknown command: ${command}. Use --help.`);
} catch (error) {
  process.stderr.write(`Skill library: ${error.message}\n`);
  process.exitCode = 1;
}
