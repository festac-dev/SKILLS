"use strict";

const test = require("node:test");
const assert = require("node:assert");
const path = require("path");
const { scan, scanSource, rules, isSlopHue, main } = require("../skills/unslopovich/scripts/detect.js");

const fixtures = path.join(__dirname, "fixtures");
const rulesIn = (file) => new Set(scan([path.join(fixtures, "slop", file)]).findings.map((f) => f.rule));

test("clean fixtures produce no findings", () => {
  const { findings, filesScanned } = scan([path.join(fixtures, "clean")]);
  assert.strictEqual(filesScanned, 4);
  assert.deepStrictEqual(findings, []);
});

test("React Native slop is caught", () => {
  const found = rulesIn("HomeScreen.tsx");
  for (const id of [
    "slop-gradient", "gradient-text", "nested-cards", "status-dot", "unvirtualized-list",
    "fixed-text-size", "emoji-icon", "sparkle-icon", "oops-error", "buzzword-copy",
    "welcome-back", "vague-button", "invented-stat", "glow-shadow", "hover-only",
    "keyboard-cover", "back-gesture", "drawer-nav",
  ]) assert.ok(found.has(id), `missing ${id}`);
});

test("SwiftUI slop is caught", () => {
  const found = rulesIn("Dashboard.swift");
  for (const id of ["unvirtualized-list", "status-dot", "fixed-text-size", "slop-gradient", "glow-shadow", "back-gesture", "drawer-nav", "safe-area-off"]) {
    assert.ok(found.has(id), `missing ${id}`);
  }
});

test("Compose slop is caught", () => {
  const found = rulesIn("MainScreen.kt");
  for (const id of ["template-theme", "unvirtualized-list", "nested-cards", "status-dot", "drawer-nav", "back-gesture"]) {
    assert.ok(found.has(id), `missing ${id}`);
  }
});

test("Flutter slop is caught", () => {
  const found = rulesIn("home.dart");
  for (const id of ["template-theme", "back-gesture", "unvirtualized-list", "nested-cards", "status-dot", "fixed-text-size"]) {
    assert.ok(found.has(id), `missing ${id}`);
  }
});

test("every rule has a fixture that triggers it", () => {
  const all = new Set(scan([path.join(fixtures, "slop")], { platform: "mobile" }).findings.map((f) => f.rule));
  for (const rule of rules) assert.ok(all.has(rule.id), `no fixture for ${rule.id}`);
});

test("commented-out code is ignored", () => {
  const src = '// <LinearGradient colors={["#7C3AED", "#EC4899"]} />\n/* Oops! Something went wrong */\n';
  assert.deepStrictEqual(scanSource(src, "a.tsx"), []);
});

test("URLs in strings do not start a comment", () => {
  const src = 'const a = "https://x.dev"; const b = "Oops";\n';
  assert.deepStrictEqual(scanSource(src, "a.ts").map((f) => f.rule), ["oops-error"]);
});

test("inline ignore comments silence a line", () => {
  const src = '// unslopovich-ignore oops-error\nconst a = "Oops";\nconst b = "Oops"; // unslopovich-ignore\nconst c = "Oops";\n';
  assert.deepStrictEqual(scanSource(src, "a.ts").map((f) => f.line), [4]);
});

test("ignored rules are skipped", () => {
  assert.deepStrictEqual(scanSource('const a = "Oops";', "a.ts", { ignoreRules: ["oops-error"] }), []);
});

test("style percentages and scale multipliers are not findings", () => {
  const src = [
    "<View style={{ width: '80%', maxWidth: '100%' }} />",
    "<Text maxFontSizeMultiplier={1.5}>Hi</Text>",
    "<ScrollView horizontal>{chips.map((c) => <Chip key={c} />)}</ScrollView>",
    "const ref = useAnimatedRef<ScrollView>()",
  ].join("\n");
  assert.deepStrictEqual(scanSource(src, "a.tsx"), []);
});

test("emoji pickers are not icon findings, labeled emoji are", () => {
  assert.deepStrictEqual(scanSource("const picks = ['😀', '😂', '🎉'];", "a.ts"), []);
  assert.deepStrictEqual(scanSource("<Text>🚀 Fast</Text>", "a.tsx").map((f) => f.rule), ["emoji-icon"]);
});

test("the slop hue band", () => {
  assert.ok(isSlopHue("7C3AED")); // violet
  assert.ok(isSlopHue("6366F1")); // indigo
  assert.ok(isSlopHue("EC4899")); // pink
  assert.ok(!isSlopHue("1B6E5A")); // green
  assert.ok(!isSlopHue("0A7EA4")); // teal blue
  assert.ok(!isSlopHue("777777")); // gray
});

test("exit codes and json shape", () => {
  const log = console.log;
  let out = "";
  console.log = (s) => (out += s);
  try {
    assert.strictEqual(main([path.join(fixtures, "slop"), "--json"]), 2);
    const parsed = JSON.parse(out);
    assert.strictEqual(parsed.version, 1);
    assert.ok(parsed.findings.every((f) => f.rule && f.severity && f.file && f.line && f.message && f.fix));
    out = "";
    assert.strictEqual(main([path.join(fixtures, "clean")]), 0);
  } finally {
    console.log = log;
  }
  const err = console.error;
  console.error = () => {};
  try {
    assert.strictEqual(main(["--ignore", "not-a-rule"]), 1);
    assert.strictEqual(main(["--nope"]), 1);
  } finally {
    console.error = err;
  }
});

test("a quote inside a regex literal does not hide a real comment", () => {
  assert.deepStrictEqual(scanSource('const quote = /"/g; // Oops\n', "a.ts"), []);
  assert.deepStrictEqual(scanSource("<Text>Hi</Text> // Oops\n", "a.tsx"), []);
  assert.deepStrictEqual(scanSource('const r = a / b; const s = "Oops";\n', "a.ts").map((f) => f.rule), ["oops-error"]);
});

test("horizontal={false} is still a vertical list", () => {
  const src = "<ScrollView horizontal={false}>{items.map((i) => <Row key={i} />)}</ScrollView>";
  assert.deepStrictEqual(scanSource(src, "a.tsx").map((f) => f.rule), ["unvirtualized-list"]);
});

test("Android color resources reach template-theme", () => {
  const src = '<resources>\n  <color name="purple_500">#6200EE</color>\n</resources>\n';
  assert.deepStrictEqual(scanSource(src, "colors.xml").map((f) => f.rule), ["template-theme"]);
});

test("XML ignore comments work", () => {
  const src = '<resources>\n  <!-- unslopovich-ignore template-theme -->\n  <color name="purple_500">#6200EE</color>\n</resources>\n';
  assert.deepStrictEqual(scanSource(src, "colors.xml"), []);
});

test("project config is found above the scan target", () => {
  const fs = require("fs");
  const os = require("os");
  const root = fs.mkdtempSync(path.join(os.tmpdir(), "unslop-"));
  fs.mkdirSync(path.join(root, ".unslopovich"));
  fs.writeFileSync(path.join(root, ".unslopovich", "config.json"), JSON.stringify({ ignoreRules: ["oops-error"] }));
  fs.mkdirSync(path.join(root, "src", "screens"), { recursive: true });
  fs.writeFileSync(path.join(root, "src", "screens", "A.ts"), 'const a = "Oops";\n');
  try {
    assert.deepStrictEqual(scan([path.join(root, "src", "screens")]).findings, []);
  } finally {
    fs.rmSync(root, { recursive: true, force: true });
  }
});

test("an unreadable file makes the scan fail, not pass", () => {
  const fs = require("fs");
  const os = require("os");
  const root = fs.mkdtempSync(path.join(os.tmpdir(), "unslop-"));
  const file = path.join(root, "A.ts");
  fs.writeFileSync(file, "const a = 1;\n");
  const read = fs.readFileSync;
  fs.readFileSync = (f, ...rest) => {
    if (f === file) throw Object.assign(new Error("EACCES"), { code: "EACCES" });
    return read(f, ...rest);
  };
  const err = console.error;
  const log = console.log;
  console.error = () => {};
  console.log = () => {};
  try {
    assert.strictEqual(main([file]), 1);
  } finally {
    fs.readFileSync = read;
    console.error = err;
    console.log = log;
    fs.rmSync(root, { recursive: true, force: true });
  }
});

test("web slop is caught", () => {
  const found = new Set(scan([path.join(fixtures, "slop", "web")]).findings.map((f) => f.rule));
  for (const id of [
    "slop-gradient", "gradient-text", "tracked-caps-label", "unverified-claim", "img-no-alt", "decorative-pulse",
    "clickable-div", "transition-all", "hover-scale", "icon-tile", "focus-removed", "zoom-disabled",
  ]) assert.ok(found.has(id), `missing ${id}`);
});

test("clean web fixtures produce no findings", () => {
  const { findings, filesScanned } = scan([path.join(fixtures, "clean-web")]);
  assert.strictEqual(filesScanned, 2);
  assert.deepStrictEqual(findings, []);
});

test("mobile-only rules stay quiet on web projects", () => {
  const found = new Set(scan([path.join(fixtures, "slop", "web")]).findings.map((f) => f.rule));
  assert.ok(!found.has("hover-only"));
  const src = '<a onMouseEnter={x}>Docs</a>\nconst Nav = createDrawerNavigator();\n';
  assert.deepStrictEqual(scanSource(src, "a.tsx", { kind: "web" }).map((f) => f.rule), []);
  assert.deepStrictEqual(scanSource(src, "a.tsx", { kind: "mobile" }).map((f) => f.rule).sort(), ["drawer-nav", "hover-only"]);
  assert.deepStrictEqual(scanSource(src, "a.tsx", { kind: "universal" }).map((f) => f.rule), ["drawer-nav"]);
});

test("--platform overrides the detected project kind", () => {
  const found = new Set(scan([path.join(fixtures, "slop", "web")], { platform: "mobile" }).findings.map((f) => f.rule));
  assert.ok(found.has("hover-only"));
});
