// A rule-based classifier for the themes in taxonomy.mjs. It is fast, free,
// and runs on every review in the population. It is also imperfect: its
// accuracy per theme is measured against a hand-labelled reference sample,
// and the estimates are corrected for its errors (see 7-analyze.mjs).

import { THEME_IDS } from "./taxonomy.mjs";

const r = (s) => new RegExp(s, "i");

export const RULES = {
  performance: r(String.raw`\b(lag|lags|laggy|lagging|slow|slower|slowly|sluggish|takes forever|forever to (load|open)|keeps? loading|stuck (on )?loading|loading (screen|forever|time)|load times?|freez(e|es|ing)|froze|frozen|hangs?|stutter\w*|choppy|unresponsive|delay(ed|s)?|battery|drains?|draining|overheat\w*|heats? up|storage space)\b`),
  crash: r(String.raw`\b(crash(es|ed|ing)?|force[- ]?clos\w*|closes (itself|by itself|on its own|out)|keeps? (closing|shutting)|shuts? down|won'?t (open|load|launch|start)|(doesn'?t|does not|will not|can'?t|cannot) (open|launch|start up)|black screen|white screen|blank screen|kicks? me out|kicked out)\b`),
  bug: r(String.raw`\b(bug|bugs|buggy|glitch\w*|errors?|broken|(doesn'?t|does not|isn'?t|is not|not|stopped|stop) work(ing|s)?|won'?t (let|save|sync|update|send|load|play|connect|download)|fail(s|ed|ing|ure)?|nothing happens|keeps? (saying|showing)|(can'?t|cannot|unable to) (download|upload|save|send|see|access|connect|sync|play|load)|disappear(s|ed|ing)?|lost (my|all))\b`),
  ui_change: r(String.raw`\b(new|latest|recent|last|this) (update|version|design|layout|interface|ui|look)\b|\b(since|after) (the|this|last|latest|recent|an) (update|redesign)\b|\b(redesign\w*|re-design\w*|bring (it |them )?back|put (it |them )?back|used to (be|have|let|show|work)|why (did|would) (you|they) (change|remove|move)|(old|previous) (version|layout|design)|removed (the|my|a|its|their)|changed (the|it|everything|how)|if it ain'?t broke)\b`),
  hard_to_use: r(String.raw`\b(confus\w*|hard to (use|find|navigate|understand|read|follow)|difficult to (use|navigate|find|understand)|not (very )?(user[- ]friendly|intuitive)|unintuitive|clunky|cumbersome|too many (steps|clicks|taps|screens)|(can'?t|cannot|couldn'?t) find|complicated|cluttered)\b`),
  interruption: r(String.raw`\b(ads|advert\w*|commercials?|pop[- ]?ups?|spam\w*|keeps? asking|nag\w*|interrupt\w*|too many notifications|notification spam|rate (this|the) app)\b`),
  ai_intrusion: r(String.raw`\b(ai|a\.i\.|chat ?bot|copilot|gemini|meta ai|my ai|chatgpt|artificial intelligence)\b`),
  layout_display: r(String.raw`\b(cut off|cuts off|cut-off|overlap\w*|font|text (is |too )*(small|big|tiny|large)|too (small|tiny) to|dark mode|landscape|orientation|ipad|tablet|fold(able)?|screen size|zoom|accessib\w*|voice ?over|talkback|screen reader|blind|layout|display (issue|problem)|doesn'?t fit|off (the )?screen)\b`),
  login_account: r(String.raw`\b(log ?in|logged (in|out)|log(s|ging)? (me )?out|sign ?in|signed (in|out)|sign ?up|password|verif\w*|otp|code (never|not|isn'?t)|two[- ]factor|2fa|account (was |got |is |has been )?(locked|banned|suspended|disabled|deleted|deactivated)|locked out|banned|suspended)\b`),
  paywall_pricing: r(String.raw`\b(subscri\w*|paywall|pay ?wall|premium|pro version|price|pricing|overpriced|expensive|charg(e|ed|es|ing)|billing|billed|in[- ]app purchases?|pay(ing)? (for|to)|free trial|costs?|fees?)\b`),
  support_trust: r(String.raw`\b(customer (service|support|care)|support (team|staff|agent)|no (response|reply)|never (responded|replied|heard back)|refund\w*|scam\w*|fraud\w*|stole|stolen|steal\w*|hacked|rip ?off|ripoff|contact (them|support|us)|help ?desk|live (chat|agent|person))\b`),
  privacy_data: r(String.raw`\b(privacy|private (data|info\w*)|personal (data|info\w*)|tracking|tracks? (me|my|you|your)|permissions?|location (access|data|tracking)|sell(s|ing)? (my|your|our) data|data (collection|harvest\w*|mining)|spyware)\b`),
  content_service: r(String.raw`\b(deliver(y|ies|ed)|driver|dasher|courier|shipping|shipped|package|orders?|restaurant|seller|merchant|pay to win|p2w|matchmaking|gameplay|levels?|rigged|unfair|tips?|payout|pay rate|shifts?|hotspots?|episodes?|articles?|news (coverage|stories)|catalog\w*|selection|stock|forecast\w*|accuracy|inaccurate)\b`),
  missing_feature: r(String.raw`\b(please add|add (a|an|the|some|more|option|feature|support)|i wish|wish (it|there|you|they|i could)|would be (nice|great|better|awesome) if|needs? (a|an|more) (option|feature|way)|no option to|there'?s no (way|option)|should (have|add|allow|let)|feature request|let us|allow (us|me|users) to|why (can'?t|isn'?t there))\b`),
};

const NEGATIVE = r(String.raw`\b(but|however|annoying|annoyed|bad|worse|worst|terrible|horrible|awful|hate|issue|issues|problem|problems|disappoint\w*|useless|frustrat\w*|unfortunately|fix|poor|garbage|trash|sucks?|ridiculous|waste)\b`);

const STOPWORDS = new Set(
  "the a an and or but is are was were be been it its this that i you he she we they my your our their me to of in on at for with not no can can't don't doesn't it's i'm have has had do does did will would app just so if when what why how all very".split(" "),
);

export function isEnglish(text) {
  const letters = text.match(/\p{L}/gu) || [];
  if (!letters.length) return false;
  const latin = letters.filter((c) => /[a-z]/i.test(c)).length;
  if (latin / letters.length < 0.8) return false;
  const tokens = text.toLowerCase().match(/[a-z']+/g) || [];
  if (tokens.length < 3) return true;
  return tokens.filter((t) => STOPWORDS.has(t)).length / tokens.length >= 0.12;
}

export function classifyByRules(review) {
  const body = `${review.title || ""}. ${review.text || ""}`;
  const themes = THEME_IDS.filter((t) => t !== "other" && RULES[t].test(body));
  const complaint = review.rating <= 2 || themes.length > 0 || NEGATIVE.test(body);
  if (complaint && !themes.length) themes.push("other");
  return { english: isEnglish(body), complaint, themes, primary: themes[0] || "none" };
}
