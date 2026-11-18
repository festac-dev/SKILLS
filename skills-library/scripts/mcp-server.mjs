#!/usr/bin/env node
import readline from 'node:readline';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {spawn} from 'node:child_process';

const engine = path.join(path.dirname(fileURLToPath(import.meta.url)), 'skills.mjs');
const versions = ['2025-06-18', '2025-03-26', '2024-11-05'];
const annotations = {readOnlyHint: true, destructiveHint: false, idempotentHint: true, openWorldHint: true};
const tools = [
  {name: 'find', description: 'Search the external skill index. Return only a few IDs and short descriptions; no guide bodies are loaded.', inputSchema: {type: 'object', properties: {query: {type: 'string', minLength: 1, maxLength: 500}, limit: {type: 'integer', minimum: 1, maximum: 12, default: 5}}, required: ['query'], additionalProperties: false}, annotations},
  {name: 'read', description: 'Read a selected guide or relative supporting file. Return at most 160 lines and 10,000 UTF-8 content bytes with a continuation position. Files and index stay outside the agent skills folder.', inputSchema: {type: 'object', properties: {id: {type: 'string', minLength: 1}, file: {type: 'string'}, section: {type: 'string'}, offset: {type: 'integer', minimum: 0}, column: {type: 'integer', minimum: 0}, limit: {type: 'integer', minimum: 1, maximum: 160, default: 80}}, required: ['id'], additionalProperties: false}, annotations},
];
const send = value => process.stdout.write(JSON.stringify(value) + '\n');
const fail = (id, code, message) => send({jsonrpc: '2.0', id, error: {code, message}});

function invoke(name, parameters) {
  const tool = tools.find(tool => tool.name === name);
  if (!tool) throw new Error('Unknown tool');
  if (!parameters || typeof parameters !== 'object' || Array.isArray(parameters)) throw new Error('Tool arguments must be an object');
  for (const key of tool.inputSchema.required) if (!(key in parameters)) throw new Error(`Missing ${key}`);
  for (const [key, value] of Object.entries(parameters)) {
    const rule = tool.inputSchema.properties[key];
    if (!rule || (rule.type === 'integer' ? !Number.isInteger(value) : typeof value !== rule.type)) throw new Error(`Invalid argument: ${key}`);
    if (rule.type === 'integer' && (value < rule.minimum || (rule.maximum && value > rule.maximum))) throw new Error(`Invalid range: ${key}`);
    if (rule.type === 'string' && ((rule.minLength && value.length < rule.minLength) || (rule.maxLength && value.length > rule.maxLength))) throw new Error(`Invalid length: ${key}`);
  }
  const args = [engine, name, name === 'find' ? parameters.query : parameters.id];
  for (const [key, value] of Object.entries(parameters)) if (!['query', 'id'].includes(key)) args.push(`--${key}`, String(value));
  return new Promise(resolve => {
    const child = spawn(process.execPath, args, {stdio: ['ignore', 'pipe', 'pipe']});
    let stdout = '', stderr = '';
    const timer = setTimeout(() => child.kill(), 45000);
    child.stdout.on('data', data => { stdout += data; if (stdout.length > 150000) child.kill(); });
    child.stderr.on('data', data => { if (stderr.length < 4000) stderr += data; });
    child.on('error', error => { clearTimeout(timer); resolve({content: [{type: 'text', text: error.message}], isError: true}); });
    child.on('close', code => {
      clearTimeout(timer);
      if (code !== 0) resolve({content: [{type: 'text', text: stderr.trim() || 'Reader failed or exceeded its time limit'}], isError: true});
      else {
        try { const result = JSON.parse(stdout); resolve({content: [{type: 'text', text: stdout.trim()}], structuredContent: result, isError: false}); }
        catch { resolve({content: [{type: 'text', text: 'Reader returned invalid JSON'}], isError: true}); }
      }
    });
  });
}

async function handle(line) {
  let request;
  try { request = JSON.parse(line); }
  catch { fail(null, -32700, 'Parse error'); return; }
  if (!request || request.jsonrpc !== '2.0' || typeof request.method !== 'string') { fail(request?.id ?? null, -32600, 'Invalid request'); return; }
  if (request.id === undefined) return;
  if (request.method === 'initialize') {
    send({jsonrpc: '2.0', id: request.id, result: {protocolVersion: versions.includes(request.params?.protocolVersion) ? request.params.protocolVersion : versions[0], capabilities: {tools: {listChanged: false}}, serverInfo: {name: 'festac-skill-library', version: '1.0.0'}, instructions: 'Find relevant IDs, then read only selected guides and supporting files. Datasets and index remain outside agent skill folders.'}});
  } else if (request.method === 'ping') send({jsonrpc: '2.0', id: request.id, result: {}});
  else if (request.method === 'tools/list') send({jsonrpc: '2.0', id: request.id, result: {tools}});
  else if (request.method === 'tools/call') {
    try { send({jsonrpc: '2.0', id: request.id, result: await invoke(request.params?.name, request.params?.arguments || {})}); }
    catch (error) { fail(request.id, -32602, error.message); }
  } else fail(request.id, -32601, 'Method not found');
}

const input = readline.createInterface({input: process.stdin, crlfDelay: Infinity});
let pending = Promise.resolve();
input.on('line', line => {
  if (Buffer.byteLength(line) > 1024 * 1024) { fail(null, -32600, 'Request too large'); return; }
  pending = pending.then(() => handle(line)).catch(error => process.stderr.write(`${error.message}\n`));
});
