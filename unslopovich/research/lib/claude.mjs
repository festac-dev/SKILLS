// Message Batches plumbing for classification and validation: build requests,
// submit in chunks, poll, and collect parsed labels. Resumable through a state
// file, so a restart never pays for the same review twice.

import fs from "node:fs";
import Anthropic from "@anthropic-ai/sdk";
import { MODEL } from "../config.mjs";
import { SCHEMA, SYSTEM, userMessage, THEME_IDS } from "./taxonomy.mjs";
import { readJson, writeJson, writeJsonlGz, readJsonlGz, sleep, log } from "./util.mjs";

const CHUNK = 10_000;

export function requestParams(review, effort) {
  return {
    model: MODEL,
    max_tokens: 4000,
    // The instructions are identical in every request; cache them for an hour
    // because batch requests are processed over a long window.
    system: [{ type: "text", text: SYSTEM, cache_control: { type: "ephemeral", ttl: "1h" } }],
    messages: [{ role: "user", content: userMessage(review) }],
    output_config: { effort, format: { type: "json_schema", schema: SCHEMA } },
  };
}

// Parse a finished message into a label, or explain why it cannot be used.
export function parseLabel(message) {
  if (message.stop_reason !== "end_turn") return { error: `stop_reason ${message.stop_reason}` };
  const text = message.content.find((b) => b.type === "text")?.text;
  if (!text) return { error: "no text block" };
  let label;
  try {
    label = JSON.parse(text);
  } catch {
    return { error: "invalid json" };
  }
  const themes = [...new Set(label.themes)].filter((t) => THEME_IDS.includes(t));
  return { english: !!label.english, complaint: !!label.complaint, themes, primary: label.primary };
}

export async function runBatches({ items, effort, stateFile, outFile, client = new Anthropic() }) {
  const state = readJson(stateFile, { batches: [] });
  const labelled = new Map();
  if (fs.existsSync(outFile)) for (const row of readJsonlGz(outFile)) labelled.set(row.key, row);

  // Submit every chunk that has no batch yet. Requests already labelled are skipped.
  const submitted = new Set(state.batches.flatMap((b) => b.keys));
  const todo = items.filter((it) => !labelled.has(it.key) && !submitted.has(it.key));
  for (let i = 0; i < todo.length; i += CHUNK) {
    const chunk = todo.slice(i, i + CHUNK);
    const batch = await client.messages.batches.create({
      requests: chunk.map((it) => ({ custom_id: it.key, params: requestParams(it.review, effort) })),
    });
    state.batches.push({ id: batch.id, keys: chunk.map((it) => it.key), status: batch.processing_status });
    writeJson(stateFile, state);
    log(`submitted ${batch.id} with ${chunk.length} requests`);
  }

  // Poll until every batch has ended, collecting results as each one finishes.
  const usage = state.usage || { input: 0, cacheRead: 0, cacheWrite: 0, output: 0 };
  for (;;) {
    let open = 0;
    for (const b of state.batches) {
      if (b.status === "collected") continue;
      const info = await client.messages.batches.retrieve(b.id);
      if (info.processing_status !== "ended") {
        open++;
        log(`${b.id}: ${info.processing_status}, ${info.request_counts.processing} processing, ${info.request_counts.succeeded} done`);
        continue;
      }
      let failed = 0;
      for await (const result of await client.messages.batches.results(b.id)) {
        const key = result.custom_id;
        if (result.result.type !== "succeeded") {
          failed++;
          continue;
        }
        const msg = result.result.message;
        const u = msg.usage || {};
        usage.input += u.input_tokens || 0;
        usage.cacheRead += u.cache_read_input_tokens || 0;
        usage.cacheWrite += u.cache_creation_input_tokens || 0;
        usage.output += u.output_tokens || 0;
        const label = parseLabel(msg);
        if (label.error) {
          failed++;
          continue;
        }
        labelled.set(key, { key, ...label });
      }
      b.status = "collected";
      b.failed = failed;
      state.usage = usage;
      writeJsonlGz(outFile, [...labelled.values()]);
      writeJson(stateFile, state);
      log(`${b.id}: collected, ${failed} failed`);
    }
    if (!open) break;
    await sleep(60_000);
  }

  // Requests that failed are not in labelled; drop their batch membership so
  // the next run resubmits them.
  const missing = items.filter((it) => !labelled.has(it.key)).length;
  if (missing) {
    for (const b of state.batches) b.keys = b.keys.filter((k) => labelled.has(k));
    writeJson(stateFile, state);
    log(`${missing} requests have no label; run again to resubmit them`);
  }
  return { labelled, usage, missing };
}

// Cost in dollars at Batch API rates (half of the standard price).
export function batchCost(usage, { input = 4, output = 20 } = {}) {
  const m = 1e6;
  return (
    0.5 *
    ((usage.input * input) / m + (usage.cacheRead * input * 0.05) / m + (usage.cacheWrite * input * 2) / m + (usage.output * output) / m)
  );
}
