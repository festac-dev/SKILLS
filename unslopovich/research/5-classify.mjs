// Step 5: label the sample with Claude through the Message Batches API.
// Usage:
//   node 5-classify.mjs --preview      print one request, spend nothing
//   node 5-classify.mjs --try 5        label 5 reviews right away, to check the setup
//   node 5-classify.mjs                submit, wait, and collect every batch (resumable)
// Output: data/labels.jsonl.gz, data/classify-state.json

import Anthropic from "@anthropic-ai/sdk";
import { EFFORT } from "./config.mjs";
import { requestParams, parseLabel, runBatches, batchCost } from "./lib/claude.mjs";
import { dataPath, readJsonlGz, args, log } from "./lib/util.mjs";

const opts = args();
const sample = readJsonlGz(dataPath("sample.jsonl.gz"));

if (opts.preview) {
  console.log(JSON.stringify({ custom_id: sample[0].key, params: requestParams(sample[0].review, EFFORT) }, null, 2));
} else if (opts.try) {
  const client = new Anthropic();
  for (const item of sample.slice(0, Number(opts.try))) {
    const msg = await client.messages.create(requestParams(item.review, EFFORT));
    console.log(item.review.rating, "|", item.review.text.slice(0, 100).replace(/\n/g, " "));
    console.log("   ->", JSON.stringify(parseLabel(msg)), JSON.stringify(msg.usage));
  }
} else {
  const { labelled, usage, missing } = await runBatches({
    items: sample,
    effort: EFFORT,
    stateFile: dataPath("classify-state.json"),
    outFile: dataPath("labels.jsonl.gz"),
  });
  log(`labelled ${labelled.size} of ${sample.length}, ${missing} missing, about $${batchCost(usage).toFixed(2)} at batch prices`);
}
