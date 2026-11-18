#!/usr/bin/env node
const fs = require("fs");
const os = require("os");
const path = require("path");

const args = process.argv.slice(2);
const root = path.join(__dirname, "..");
const skill = path.join(root, "skills", "unslopovich");

if (args[0] === "detect") {
  process.exitCode = require(path.join(skill, "scripts", "detect.js")).main(args.slice(1));
  return;
}

const home = os.homedir();

// Where each agent looks for skills. `global` is a folder in your home
// directory, `project` is relative to the project you run the installer in.
// Cursor and OpenCode also read ~/.claude/skills and ~/.agents/skills, so a
// global install for them goes to the shared folder.
const AGENTS = {
  claude: { name: "Claude Code", global: ".claude/skills", project: ".claude/skills", seen: [".claude"], call: "/unslopovich" },
  codex: { name: "Codex", global: ".agents/skills", project: ".agents/skills", seen: [".codex"], call: "$unslopovich" },
  cursor: { name: "Cursor", global: ".agents/skills", project: ".cursor/skills", seen: [".cursor"], call: "/unslopovich" },
  opencode: { name: "OpenCode", global: ".agents/skills", project: ".opencode/skills", seen: [".config/opencode", ".opencode"], call: "/unslopovich" },
  gemini: { name: "Gemini CLI", global: null, project: ".gemini/skills", seen: [".gemini"], call: "/unslopovich" },
  copilot: { name: "GitHub Copilot", global: null, project: ".github/skills", seen: [], call: "/unslopovich" },
};

const usage = `Usage:
  npx unslopovich                      install for every agent found on this machine
  npx unslopovich --agent codex,cursor install for these agents (${Object.keys(AGENTS).join(", ")})
  npx unslopovich --project            install into this project instead of your home folder
  npx unslopovich --dir <folder>       install into any skills folder
  npx unslopovich detect [paths...]    scan mobile and web source for slop`;

function option(name) {
  const i = args.indexOf(name);
  if (i === -1) return null;
  if (!args[i + 1] || args[i + 1].startsWith("--")) {
    console.error(usage);
    process.exit(1);
  }
  return args[i + 1];
}

if (args.includes("--help") || args.includes("-h")) {
  console.log(usage);
  return;
}

function copySkill(base) {
  const dest = path.join(base, "unslopovich");
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(skill)) {
    fs.rmSync(path.join(dest, entry), { recursive: true, force: true });
    fs.cpSync(path.join(skill, entry), path.join(dest, entry), { recursive: true });
  }
  return dest;
}

const dir = option("--dir");
if (dir) {
  const dest = copySkill(path.resolve(dir.replace(/^~(?=$|\/)/, home)));
  console.log(`Dr. Unslopovich will see you now.\nInstalled to ${dest}\nNext, ask your agent: review my app with unslopovich`);
  return;
}

const project = args.includes("--project");
const requested = option("--agent");
let agents;
if (requested) {
  agents = requested.split(",").map((a) => a.trim().toLowerCase());
  const unknown = agents.filter((a) => !AGENTS[a]);
  if (unknown.length) {
    console.error(`Unknown agent: ${unknown.join(", ")}. Choose from ${Object.keys(AGENTS).join(", ")}.`);
    process.exit(1);
  }
} else {
  agents = Object.keys(AGENTS).filter((a) => AGENTS[a].seen.some((d) => fs.existsSync(path.join(home, d))));
  if (!agents.length) agents = ["claude"];
}

const installed = new Map();
const skipped = [];
for (const id of agents) {
  const agent = AGENTS[id];
  const folder = project ? agent.project : agent.global;
  if (!folder) {
    skipped.push(agent.name);
    continue;
  }
  const base = project ? path.resolve(folder) : path.join(home, folder);
  if (!installed.has(base)) installed.set(base, { dest: copySkill(base), agents: [] });
  installed.get(base).agents.push(agent);
}

console.log("Dr. Unslopovich will see you now.");
for (const { dest, agents: list } of installed.values()) {
  console.log(`\n${list.map((a) => a.name).join(", ")}\n  installed to ${dest}`);
  for (const a of list) console.log(`  in ${a.name}: ${a.call} review my app`);
}
if (skipped.length) console.log(`\n${skipped.join(", ")}: no global skills folder. Run again with --project inside your project.`);
