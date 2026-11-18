# A real run on QuizHub

[QuizHub](https://github.com/ramkrishnajha5/QuizHub) is an open-source quiz app by [ramkrishnajha5](https://github.com/ramkrishnajha5), built with React, Vite, Tailwind and Firebase, under the MIT license. Thanks for sharing it.

We ran `/unslopovich treat the quiz setup screen` on commit `84ca084` and changed nothing by hand.

- [report.md](report.md): the full diagnosis and what the treatment did
- [treatment.diff](treatment.diff): the code change (5 files)

Score 10 to 18 out of 24. Detector findings on this screen 39 to 0.

The sandbox blocked Firestore and Open Trivia DB, so the folders, tests and topics in the screenshots are sample data. Both sides use the same sample data.

Three changes were left for the owner because they change how data loads. The biggest: if Open Trivia DB is down, the team's tests disappear too, because both loads share one `Promise.all`.
