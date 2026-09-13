# Homework 3 — Debugging, data files, recovery, and final diagnosis note

**ECBS5293 — Computing for Analytical Work · due Fri 9 Oct 2026, 23:59 · 7–8 hours**

## Goal

`scripts/pipeline.py` loads customers and orders, cleans the orders, joins, and writes `output/report.csv` — one row per region and month with order count and revenue — then prints a total. From a fresh clone, one command should do all of that.

## How to run (copy exactly)

```bash
uv sync
uv run python scripts/pipeline.py
```

## What is broken

Several things, and they are of **two kinds**: some are code errors you will meet as tracebacks; some are problems in the input files that the code's own sanity checks will catch. For each one, decide which kind it is *before* you fix it — the evidence is different (a traceback line vs. `head`/`dtypes`/`isna` on the data) and so is the right fix (a code change vs. a loading option). Do not edit the data files.

## What you must submit (all on Moodle)

In the repo, committed:

1. The repaired pipeline: runs end to end from a fresh unzip; `output/report.csv` is produced and sensible.
2. **Data-loading checks**: after each load, print or assert row count, column names, dtypes, missing counts (the four-line check). Leave them in.
3. **`DIAGNOSIS.md`** — one five-part note per failure, each labelled **code** or **data**, with the evidence that told you which.
4. **`AI_USE.md`** — what you asked, what it got right or wrong, how you verified.
5. **`REFLECTION.md`** — the end-of-course reflection (template provided; four prompts; ~300 words maximum; specifics beat length). It stays in the repo and travels in the archive.
6. A **final clean commit**: `git status` clean, `git diff` empty.

Then make the archive **with Git**:

```bash
git status                                   # clean? if not: git add . && git commit -m "…" first
git log --oneline > GIT_LOG.txt
git add GIT_LOG.txt && git commit -m "Add git log for submission"
git archive --format=zip -o ../hw3-submission.zip HEAD    # lands next to the project folder
```

Upload to the Homework 3 slot on **Moodle**:

7. `hw3-submission.zip` (in the folder above the project)
8. A **video, up to 2 minutes**: the repaired pipeline running end to end, then the failures you diagnosed — distinguishing data problems from code problems. Start by saying "Homework 3" and the repo name.

**Deadline: Fri 9 Oct, 23:59** — one day late at −10%, nothing after Sat 10 Oct 23:59. Do not expect *graded* feedback before the exam; when the late window closes, a self-check key listing every failure and what a correct diagnosis names is posted on Moodle, together with a mock exam in the final's format. Compare your notes against the key, then sit the mock. The exam is in reading week.

## Rules

- Fix causes. Loading options and cleaning steps for data problems; code changes for code problems. Never edit `data/raw/`.
- No paths to your own machine.
- AI may explain; you must be able to explain, on video, without notes.

## Hints, if stuck

1. Read the last line of every traceback first. `AssertionError` with a message is the code *telling you what it checked* — read the message.
2. `head -3` both data files before touching `load_*`. Count separators; count title lines.
3. `df.dtypes` and `df["amount"].head()` after loading. What is in the column besides digits? What strings mean "missing"?
4. Dates: `df["order_date"].head(10)`. One format or two? `pd.to_datetime` has `format="mixed"` and `dayfirst=`.
5. `KeyError` — `print(report.columns)` on the line before. Case matters.
6. `TypeError` on the last line — a number and a string. Format the number into the string.

## Grading

See the rubric on the course site. The diagnosis notes, the video, and the reflection together outweigh the fix.

## If you got lost: how to reset

Both of these **destroy work**. Read before running.

**Discard uncommitted changes (destructive)** — throw away edits and new files; keep your commits:

```bash
git restore --staged --worktree .    # every tracked file back to the last commit, staged or not
git clean -fd                        # and remove new, untracked files
```

> ⚠️ Permanently deletes uncommitted changes — staged or not — and any new untracked files.

**Full reset to the starter state (destructive)** — back to exactly what you cloned; throws away your commits too:

```bash
git reset --hard origin/main
git clean -fdx
```

> ⚠️ Discards your local commits and uncommitted changes. The `-x` also removes ignored files — `output/`, the `.venv/` environment — so the folder truly matches a fresh clone (`uv sync` rebuilds the environment in a minute). Without `-x`, leftover generated files can hide the very failure the lab wants you to meet again.
