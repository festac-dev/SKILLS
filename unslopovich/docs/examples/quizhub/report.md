# Dr. Unslopovich: treat the quiz setup screen (QuizHub `/setup`)

Command picked: `treat` (the user typed `/unslopovich treat the quiz setup screen`).
Chart: there is no `.unslopovich/chart.md`. I worked out the stack and brand from the code. Running `chart` afterwards would record the decisions below so later visits don't flag them again.

---

## 1. Diagnosis (before)

```text
Dr. Unslopovich's diagnosis
Verdict: When the topic list fails to load, the screen offers an empty dropdown and a faded Start button and says nothing, under a gradient banner announcing a learning journey.
Stack: React 19 + Vite, Tailwind via CDN (config in index.html), framer-motion, lucide-react, Firebase. Ships to the web (desktop and phone browsers). The separate Expo app in mobile/ is out of scope.
Reviewed: /setup with the shared Header, Footer and CustomModal. Two top tasks: (1) pick a test from the QuizHub team's folders and start it, (2) pick a topic and a length for quick Open Trivia DB practice and start it. Reviewed in a running app: Vite plus Playwright, with Open Trivia DB and Firestore replaced by mock data in a test harness. Viewed at 375, 390, 768, 1280 and 1920 wide, in light and dark, and at 640 CSS px with DPR 2 as a stand-in for 200% zoom.
Score: 10/24 Intensive care  Task path 2 · Truth 1 · Native fit 2 · States 2 · Access 2 · Specificity 1
Performance: Not profiled. Static leads: none worth reporting on this screen. Three Firestore and REST calls run in parallel on mount, and the lists are short and folder-scoped. framer-motion runs hover-scale springs on every card.
```

**Critical**
- `pages/QuizSetup.tsx:81-85` (and `utils/api.ts:18`): when Open Trivia DB fails, `Promise.all` rejects. The catch only logs the error, so the user sees an empty "Choose a topic..." dropdown and a disabled Start button with no explanation. Because of `Promise.all`, the team's tests also vanish, even when Firestore answered. This is a failed load shown as empty. It reproduces in this sandbox, where opentdb.com is blocked. -> Add an error state that names the cause and offers Try again, and have the select explain why it is empty.
- `pages/QuizSetup.tsx:655-664`: Start is disabled until a topic is chosen, and nothing says why. The "No Category Selected" alert in `handleStart` can never fire because the button is disabled. -> Add a visible hint ("Choose a topic to start.") tied to the button with `aria-describedby`.

**Noticeable**
- `pages/QuizSetup.tsx:253-262, 273-302`: two stacked purple-pink-orange gradient banners ("Configure Your Quiz / begin your learning journey", "Quizzes by QuizHub Team") take about 250px before any content, and 300px+ on a phone. [`slop-gradient` x15 in the screen and shared files] -> Use a plain page title and section headings.
- `pages/QuizSetup.tsx:283-299`: the search input is unlabeled, uses 12px text (iOS zooms on focus) and white/70 placeholder text on a gradient (low contrast). Its clear button has no accessible name. -> Add a real label, 16px text, normal input colors, and `aria-label="Clear search"`.
- `pages/QuizSetup.tsx:700-806`: the quiz info modal has no `role="dialog"`, no Escape handling, no initial focus and no focus return. Its close button has no name. On a phone it is a centered card. -> Add dialog semantics, Escape, focus on the main action, focus back to the row on close, and a bottom-sheet layout on phones.
- `pages/QuizSetup.tsx:549-571`: the "Select Category" and "Number of Questions & Time" labels are not tied to their controls. The count tiles are buttons with no selected state for assistive technology. -> Use `<label htmlFor>`, and make the tiles a radio group inside a `fieldset` and `legend`.
- `pages/QuizSetup.tsx:625-652`: the "Quiz Summary" box repeats the selected tile. It is a card inside a card inside the main card, with sparkle icons [`sparkle-icon`] and a blurred blob. -> Remove it.
- `pages/QuizSetup.tsx:417-470, 481-527`: folders and tests are cards with emoji-in-gradient icon tiles [`emoji-icon`, `hover-scale`]. Every test carries two colored pills ("Medium", "Available Now"), and "Available Now" sits on every unrestricted test, so it means nothing. -> Use one list with rows: a folder icon in the text color, a status only when it carries information, and the difficulty as text.
- `pages/QuizSetup.tsx:751-762`: in dark mode the difficulty and negative-marking pills in the modal stay light (no `dark:` variants).
- `components/Footer.tsx:32-45, 87, 93`: the footer has a gradient strip, a purple-pink gradient logo tile, gradient wordmark text [`gradient-text`] and a heart that pulses forever [`decorative-pulse`]. This contradicts the header's real mark (amber bolt, "QuizHub" in primary indigo).
- `components/CustomModal.tsx:43-45, 79-83`: the confirm buttons use purple-pink and red-rose gradients, the icons are emoji (💬 ⚠️ ✅), and there are no dialog semantics.
- `components/Header.tsx`: the mobile theme toggle and the menu button have no accessible name. The profile button sets `focus:outline-none` with nothing in its place. The "App" pill uses a gradient and a hover lift.

**Minor**
- `pages/QuizSetup.tsx:413, 477`: tracked small-caps section labels ("SUB-SECTIONS & CATEGORIES") [`tracked-caps-label`].
- `pages/QuizSetup.tsx:392, 677, 795`: emoji standing in for icons (🏠 📝 🚀) [`emoji-icon`].
- Copy: "Configure Your Quiz", "begin your learning journey", "for a unique experience". Title Case everywhere.
- `pages/QuizSetup.tsx:671-696`: the "Quiz Features" card repeats the shuffle line above it. I checked the claims against the code and they are true (2x pool and Fisher-Yates in `utils/api.ts`, autosave every 5000ms and mark-for-review in `QuizRunner.tsx`), so I kept them as plain text.

**Ask first**
- `pages/QuizSetup.tsx:loadData`: replacing `Promise.all` with `Promise.allSettled` would keep the team's tests visible when only Open Trivia DB is down. It changes how the screen's data loads, so I left it. Recommended.
- The folder you are in lives only in component state, so browser Back leaves `/setup` entirely, and a folder can't be shared or reopened. Moving it into the URL (`/setup?folder=…`) changes URLs and navigation.
- `admin/utils/adminFirestore.ts:251-305`: `getPublishedAdminQuizzes` and `getAllQuizFolders` swallow errors and return `[]`, so a Firestore failure makes the whole "Tests by the QuizHub team" section disappear without a word. Fixing this means changing the data layer, which is outside this screen.

**Worth keeping**
- The brand: the amber bolt (`accent #F59E0B`) and "QuizHub" in `primary #4F46E5` in the header.
- Real `<button>` elements everywhere on the screen, the folder and test model, alphabetical sorting, and the existing search and empty states.
- The test terms themselves: question count, minutes, and negative marking at −0.25. This is what an exam-prep user scans for.

**Not checked (before)**
- Performance: not profiled.
- Real data: Firestore and Open Trivia DB are blocked in this sandbox, so all populated views use mock folders and tests I injected in the test harness. These are not product data.

---

## 2. Severity and direction

**Case: heavy.** Generated tells span color (gradients), icons (sparkles, emoji), copy, and layout (cards inside cards). Truth scored 1.

The direction below is the one I would have shown the user before the first edit. The user wasn't present, so I took it as approved, as instructed.

- **Product.** Timed mock tests from the QuizHub team (section-wise test series with negative marking), plus quick topic practice from Open Trivia DB, for students preparing for exams.
- **Use.** Mostly on a phone, in short sessions, choosing a test and then committing 10 to 60 minutes to it. This needs scannable terms, big enough targets, and Start within easy reach.
- **Character.** Exam-hall plain, exact, encouraging without cheering.
- **The bright spot.** A test's terms and its availability window, plus the one Start action in the brand indigo. Everything else stays gray.
- **Signature.** The "paper line": a test's terms written the way an exam paper states them, `100 questions · 60 min · Hard · −0.25 per wrong answer`, in tabular figures. It is used in every row, in the dialog's details, and on the practice Start button.

Brand kept: indigo `#4F46E5` as the only accent and the amber bolt as the mark. The purple-pink gradients are not part of the brand. The header never used them, and the user has not said they are the brand.

---

## 3. What changed and why

Order of work: tokens, then shared components, then the screen. On the screen I worked in passes.

**Tokens: `index.css`**
- Added a global `:focus-visible` outline in primary indigo (lighter indigo `#A5B4FC` in dark mode), `accent-color: #4F46E5`, and `color-scheme: dark` under `.dark` so native selects and scrollbars follow dark mode. This is a shared fix and affects every page.

**Shared components**
- `components/CustomModal.tsx`
  - Gradients become solid semantic colors: primary indigo, red-600, green-700.
  - Emoji icons removed; the `✕` text becomes a lucide `X` with a 40px target.
  - Added `role="dialog"` (`alertdialog` for alerts), `aria-modal`, and labelled-by and described-by.
  - Focus moves to the confirm button on open.
  - Text is left-aligned with the actions on the right; buttons are 44px tall with `transition-colors` instead of `transition-all`.
  - Behavior and the props API are unchanged. It is also used by other pages, which now get the same fix.
- `components/Footer.tsx`
  - The mark now matches the header: amber bolt plus "QuizHub" in primary.
  - Removed the gradient strip, the gradient text and the pulsing heart.
  - Social links are icon-only links with 44px targets, no tinted tiles and no hover-scale.
  - Raised the low-contrast gray-400 small text to gray-500/600.
- `components/Header.tsx`
  - Gave names to the theme toggles ("Switch to dark/light mode") and the menu button (with `aria-expanded`). The profile button gets `aria-expanded` and `aria-haspopup`, and I removed its `focus:outline-none`.
  - The "App" link (shown only at 768-1023px) and the mobile "Download Android App" button change from a green gradient to an outline style. The 768-1023px link now reads "Android app".
  - Login hover changes from blue-700 to indigo-700 to match primary.
  - No links moved, and none were added or removed.

**Screen: `pages/QuizSetup.tsx`**

*Business logic and data flow:* `checkBanAndStart`, `handleStart`, `handleStartCustomQuiz`, the folder and search memos, and the three loader calls are unchanged. The only additions are a `loadError` flag in the existing catch, and a Try again button that re-runs the same loader.

- **Spacing and layout**
  - Removed the outer glass card, both gradient banners, the summary box and the features card.
  - The page is now a `max-w-3xl` column: an h1 "Start a quiz", then two sections in their original order (team tests first, quick practice second).
  - Each section is one surface. Folders and tests are divided rows in a list instead of a grid of cards.
- **Color**
  - Indigo is used only for selection, links and Start.
  - Status colors carry meaning, and each has an icon backup: green "Live now" with a dot, amber "Opens <date time>" with a clock, gray "Ended" with a slashed circle.
  - Negative marking is red text.
  - Dark mode uses the existing `darkbg` and `darkcard` tokens throughout.
- **Icons**
  - All emoji and sparkles are gone. The icons are lucide, in the text color: folder, chevron, lock, check, clock, alert.
- **Copy**
  - "Start a quiz", "Tests by the QuizHub team", "Section-wise test series and set papers", "Quick practice", "Random multiple-choice questions on a topic, from Open Trivia DB", "Topic", "Length".
  - The breadcrumb root "🏠 All Categories" becomes "All tests".
  - "Quiz Ended" becomes "Ended", and "Available Now" is no longer shown, since it is the default.
  - The modal button reads "Start test", "Log in to take this test", "Not open yet" or "This test has ended", in place of the lock icon with "Locked".
  - The practice button reads "Start 15-question quiz · 15 min".
  - The four feature claims, which I verified, are now one plain paragraph.
- **Type**
  - One scale: a 2xl/3xl h1, lg section titles, base for rows and sm for meta text. Weights are bold and semibold; the extrabold, black and Title Case are gone. Numbers use tabular figures.
- **Controls**
  - Search: a labeled `type="search"` input, 16px text, 44px tall, with a named clear button.
  - Breadcrumbs: a `nav` with an `ol` and `aria-current`.
  - Topic: a `<label htmlFor>` tied to the select. When the topic list did not load, the select is disabled and explains why.
  - Length: a radio group in a `fieldset` and `legend`. Arrow keys move the selection, and the focus ring shows on the tile.
- **States**
  - Loading: a quiet skeleton with the real h1 and `role="status"`, in place of the spinner with a sparkle on a gradient.
  - Load error: a `role="alert"` banner that names the cause, with Try again.
  - Start disabled: a visible reason.
  - Search: a match count and an empty state with a next step. The empty folder message is kept.
- **Dialog**
  - `role="dialog"` with `aria-modal` and labelled-by; Escape closes it, but defers to the login confirm when that is open on top.
  - Focus goes to the main action, or to Close when the test is locked, and returns to the row that opened it.
  - On phones it is a bottom sheet with safe-area padding.
  - The details are a `dl` (questions, time limit, difficulty, negative marking, window), and dark variants are correct.
- **Motion**
  - Removed every hover-scale, entrance stagger and spring.
  - The dialog keeps a 150ms fade and slide, which explains where it came from. The screen is wrapped in `MotionConfig reducedMotion="user"`.

### Score after

```text
Score: 18/24 Outpatient  Task path 3 · Truth 3 · Native fit 3 · States 3 · Access 3 · Specificity 3
```

| Dimension | Before | After | Reason for the after score |
|---|---|---|---|
| Task path | 2 | 3 | Tests appear right under the title. Start says what it starts and why it is disabled. Still short of 4: folder state is not in the URL, so Back leaves the page (Ask first). |
| Truth | 1 | 3 | An Open Trivia DB failure is now said out loud with a retry. Still short of 4: `Promise.all` still drops the team tests in that case, and Firestore errors are still swallowed in `adminFirestore.ts` (both Ask first). |
| Native fit | 2 | 3 | Real labels, radios, dialog semantics, Escape and focus return. Still short of 4: no focus trap inside the dialog, and Back does not step out of folders. |
| States | 2 | 3 | Loading, error, empty, search-empty, disabled-with-reason, locked, upcoming and ended are all designed. Still short of 4: no offline-specific message. |
| Access | 2 | 3 | Every control has a name, there is a visible focus ring everywhere, inputs are 16px, and contrast is raised (estimated, see Not checked). Still short of 4: not tested with a screen reader, and the dialog has no focus trap. |
| Specificity | 1 | 3 | The screen is built from the product's own nouns and its test terms (the paper line and negative marking). Still short of 4: the calm white-surface, one-accent look is close to the new default (see self-check). |

---

## 4. Detector results

Rule hits are evidence; I checked each one in context.

**Files I touched** (`pages/QuizSetup.tsx`, `components/Header.tsx`, `components/Footer.tsx`, `components/CustomModal.tsx`; `index.css` added after)

| | Findings | By rule |
|---|---|---|
| Before (4 files) | 39 | slop-gradient 15, hover-scale 5, transition-all 4, sparkle-icon 4, emoji-icon 3, gradient-text 2, icon-tile 2, tracked-caps-label 2, clickable-div 1, decorative-pulse 1 |
| After (5 files) | 0 | 5 hits were silenced inline with reasons (below) |

Inline ignores I added, each confirmed as a false positive:
- `icon-tile` x4 (CustomModal close, Footer social links, the search clear button, the dialog close button): these are icon-only buttons and links that are transparent at rest and only show a hover background. They are not tinted tiles.
- `clickable-div` x1 (the CustomModal backdrop): the div is `aria-hidden` and click-to-dismiss only. Escape and the Close button are the keyboard routes.

**Whole repo** (`node detect.js . --json`, 116 files)

| | Findings |
|---|---|
| Before | 344 |
| After | 305 |

The remaining 305 are on pages and admin screens outside this scope: Home, Dashboard, QuizRunner, Results, Study, About, Contact, Login, Signup, admin/*, src/*, and mobile/*. They include slop-gradient 126, emoji-icon 34, gradient-text 25, tracked-caps-label 18, sparkle-icon 14, hover-scale 14, transition-all 13, glow-shadow 12, unvirtualized-list 12, invented-stat 9, and others. I did not triage them. A `scan` of the repo or a `review` of Home and QuizRunner would be the next visit.

TypeScript: `npx tsc --noEmit -p .` gives the same result before and after: 1 error, the pre-existing `pages/QuizRunner.tsx(482,11)` UserAnswer `timeSpent` mismatch. None of my changes add errors.

---

## 5. Self-check

1. **Cover the logo.** With the bolt hidden, the folder list with "−0.25 per wrong answer", "Opens 11/18/2026 10:42 AM", "Section-wise test series" and the length picker reads as exam prep, not banking or fitness. Even so, the surfaces are white, rounded and gray-bordered with one indigo accent, which is close to the calm default. The specificity comes from content, not form.
2. **Neighbor test.** A competing quiz app would likely get similar bordered surfaces. The decision that differs is the paper line: test terms stated as on an exam paper, with negative marking in red, used the same way in rows, the dialog and the Start button. I did not add a second visual flourish to differentiate further. Using the amber brand accent somewhere on this screen would be a visual-identity question for the user.
3. **Count the containers.** They went down. Before: outer glass card, 2 gradient banners, a breadcrumb card, one card per folder, one card per test, the summary box with 2 inner cards, the features card, and 4 tinted pills per test. After: 2 section surfaces with divided rows, and the 4 length options.
4. **Count the colors.** Indigo means selection, link or primary action. Green means live, amber means opens later, gray means ended, and red means negative marking or an error. Nothing is decorative.
5. **Find the dots.** There is one dot, on "Live now". It always comes with the words "Live now", so it reads without color.
6. **Find the task.** Team tests are still first and practice second. The search box and the Back control kept their positions within the section. Start is closer to the length picker, and on a phone the practice Start button is at about 1000px instead of about 1250px in the loaded state. Every control is reachable with Tab in reading order (verified).
7. **Detector** on the changed files: 0 after the 5 explained ignores.
8. **Fresh look.** I could not start a fresh-context reviewer: this agent has no sub-agent tool. The self-check above is mine, so it is not independent.
9. **Not checked:** see below.

---

## 6. What I left alone

- Every other page: Home, QuizRunner, Results, Dashboard, Study and so on, plus the admin pages and the `mobile/` Expo app. The one exception is the shared fixes in Header, Footer, CustomModal and index.css, which those pages now inherit:
  - CustomModal no longer shows emoji icons, and its buttons are solid instead of gradient.
  - Every page gets the indigo focus ring.
- Data and logic:
  - `Promise.all` in `loadData` (see Ask first).
  - `adminFirestore.ts`, which swallows errors (Ask first).
  - The ban check and its fail-open behavior.
  - The navigation state passed to `/quiz`.
- URL and navigation: the folder location is still in component state (Ask first).
- The Inter web font from index.html. It is a project-wide choice, and I saw no brand reason to remove it.
- The `cdn.tailwindcss.com` script tag and the inline tailwind.config in index.html. I did not change the config, so `twtool/tw.config.cjs` did not need an edit.
- `package-lock.json` was already modified in the working tree before I started (+29 lines). I did not touch it.
- I made no commits.

## 7. Not verified

- **Performance:** not profiled. No Lighthouse run, no production build, and no CPU throttling.
- **Real data:** Firestore and Open Trivia DB are blocked in this sandbox. Every populated screenshot uses mock folders and tests that I injected into the Playwright run (intercepted `adminFirestore.ts` and opentdb responses). These live only in `twtool/states.cjs` and `twtool/keys.cjs`, not in the product. The plain `shot.cjs` final screenshots (`qh-after-desk.png`, `qh-after-phone.png`) therefore show the real behavior in this sandbox, which is the new load-error state.
- **The logged-in path:** "Start test", the ban check and navigation to `/quiz`. Auth is blocked, so I only saw the logged-out "Log in to take this test" path and the login confirm.
- **Screen reader:** names, roles and focus order were checked in the DOM with Playwright. I did not test with VoiceOver, TalkBack or NVDA.
- **Contrast:** estimated from Tailwind palette values (gray-600 on white about 7:1, gray-500 about 4.8:1, amber-700 about 5:1, gray-400 on `#1F2937` about 5.6:1). Not measured with a tool.
- **200% zoom:** approximated as a 640 CSS px viewport at DPR 2, not true browser zoom.
- **Real devices:** iOS Safari behavior (16px inputs, safe-area padding on the bottom sheet) was not tested on a device.
- **Dialog focus trap:** Tab can leave the quiz dialog. Escape, initial focus and focus return were verified.
- **Reduced motion:** screenshots ran with `reducedMotion: 'reduce'`, but I did not compare the motion side by side.

## Files

- Changed: `pages/QuizSetup.tsx`, `components/CustomModal.tsx`, `components/Footer.tsx`, `components/Header.tsx`, `index.css`.
- Final screenshots: `cand/qh-after-desk.png`, `cand/qh-after-phone.png`.
- Before and after state screenshots with mock data, at desk, phone, dark, folder, search, modal, load-failure, 768, 1920 and zoom: `cand/shots/before-*.png` and `cand/shots/after-*.png`.
- Visit record: `QuizHub/.unslopovich/visits/2026-11-16-1046-quiz-setup.md`.
