# Homework 3 — Debugging, data files, recovery, and final diagnosis note

**ECBS5293 — Computing for Analytical Work · due Fri 9 Oct 2026, 23:59 (slot on Moodle)**

Budget about 7–8 hours, spread over the two weeks, not the night before. If you are well past that and still stuck, post on the Moodle forum. That tells us something useful about the assignment, and it is not a mark against you.

## Goal

`scripts/pipeline.py` loads customers and orders, cleans the orders, joins them, and writes `output/report.csv` — one row per region and month with an order count and revenue — then prints a total. From a fresh clone, one command should do all of that.

## How to get it

In your terminal (Git Bash on Windows, Terminal on macOS), in the folder where you keep course work:

```bash
git clone https://github.com/earino/ecbs5293-hw03-debugging-data-recovery.git
cd ecbs5293-hw03-debugging-data-recovery
```

Commands below run in that terminal, from this folder. Open **this folder** in VS Code (*File → Open Folder…*; trust the authors when asked) to edit files.

## Start here

In the terminal, from the project folder — the launch you have used since Lab 1, after a look at the files:

```bash
head -5 data/raw/customers.csv
head -5 data/raw/orders_2024.csv
wc -l data/raw/*.csv
uv sync
uv run python scripts/pipeline.py
```

It fails. That is the assignment.

## What is broken

Several things, and they are of **two kinds**: some are code errors you will meet as tracebacks; some are problems in the input files that the code's own sanity checks — or pandas — will catch. For each one, decide which kind it is *before* you fix it. The evidence is different (the failing line is yours and the object has the wrong name or type, versus a loader or a check stopping and `head` / `dtypes` / `isna` showing the file is not shaped as the code assumes), and so is the right fix (a code change versus a loading option or a cleaning step). Do not edit the data files.

Every failure here is a kind you met in Lab 5 or Lab 6. That is on purpose: this homework puts the whole course together before the exam. What is new is deciding which kind each one is, and saying why.

## The order of work

The list under *What you must submit* is what you hand in. This is the order to do it in.

**Open `DIAGNOSIS.md` before step 1.** Part 3 of every note has to be pasted while that failure is still on the screen: each repair destroys the traceback that proved the failure before it, and you cannot get it back without undoing the repair.

1. `head` and `wc -l` both data files, in the terminal — ask the file questions; do not open it and scroll. Write down what you see: the delimiter, the lines above the header, how the amounts and dates are written (and, for a slash date, which number is the day), the line counts. That is the evidence for every *data* note, and it is cheaper to gather now than to reconstruct later.
2. `uv sync`, then `uv run python scripts/pipeline.py`. **Paste the last line of the traceback and the line in your file into the next note's part 3 before you change anything.** Label the note *code* or *data*, and write one line on what told you which.
3. Fix that one failure. Run the same command again. A new failure appears — repeat step 2 for it. Do not read the whole file and fix everything at once: the sequence is where the evidence is.
4. When the pipeline runs end to end: the **four-line check** after each load (shape, dtypes, `head()`, `isna().sum()`), left in the code as prints or asserts, and the row count compared with `wc -l` minus the lines that are not data.
5. Read `output/report.csv`. Does the month column look right — are there orders in the months you expect, given the dates you saw in step 1? A load that does not crash is not a load that is right. The printed total comes out the same however the dates or the missing amounts are read, so it cannot tell you they are right: check the rows.
6. Commit as you go: at least one commit per failure, with a message that says what it fixed. `git status` should say *nothing to commit, working tree clean* after the last one. If Git answers *"Please tell me who you are"*, set `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"` once, then run the `git commit` again — the failed commit did not happen.
7. Finish the notes: complete `DIAGNOSIS.md` (the raw evidence is already pasted in, so this is parts 1, 2, 4 and 5 of each), write `AI_USE.md`, and write `REFLECTION.md` — after re-reading your HW1 and HW2 notes, which it asks you to quote.
8. Follow `SUBMITTING.md` — commit everything, save the git log, make the zip, record the video, upload both to Moodle.

## What you must submit (all on Moodle)

In the repo, committed:

1. The repaired pipeline: runs end to end from a fresh unzip; `output/report.csv` is produced and sensible.
2. **Data-loading checks**: after each load, print or assert row count, column names, dtypes, missing counts (the four-line check). Leave them in.
3. **`DIAGNOSIS.md`** — one five-part note per failure, each labelled **code** or **data**, with the evidence that told you which. The file has the template and says how to copy it.
4. **`AI_USE.md`** — what you asked, what it got right or wrong, how you verified.
5. **`REFLECTION.md`** — the end-of-course reflection (template provided; four prompts; ~300 words maximum; specifics beat length). It stays in the repo and travels in the archive.
6. A **final clean commit**: `git status` clean, and `GIT_LOG.txt` showing one commit per fix with messages that say what each fixed.

Then the archive, made **with Git**, by the steps in **`SUBMITTING.md`** — four short steps, each with a sentence on what it does, and a seven-line check at the end, one per rubric criterion. Read its first step before you start: `git archive` packs **exactly what you have committed**, so anything still uncommitted is silently missing from your zip.

Upload to the Homework 3 slot on **Moodle**:

7. `hw3-submission.zip` (in the folder above the project)
8. A **video, up to 2 minutes**: the repaired pipeline running end to end, then the failures you diagnosed — distinguishing data problems from code problems. Start by saying "Homework 3" and the repo name. Two minutes is a ceiling, not a target.

**Deadline: Fri 9 Oct, 23:59** — one day late at −10%, nothing after Sat 10 Oct 23:59. Do not expect *graded* feedback before the exam; when the late window closes, a self-check key listing every failure and what a correct diagnosis names is posted on Moodle, together with a mock exam in the final's format. Compare your notes against the key, then sit the mock. The exam is in reading week.

## Rules

- Fix causes. Loading options and cleaning steps for data problems; code changes for code problems. Never edit `data/raw/` — if you have, `git restore data/raw` puts the files back.
- No paths to your own machine.
- AI may explain; you must be able to explain, on video, without notes.

## Hints, if stuck

1. Read the last line of every traceback first. `AssertionError` with a message is the code *telling you what it checked* — read the message. A `ParserError` or a `ValueError` from inside `read_csv` or `to_datetime` is pandas telling you about the file. `ParserError: Error tokenizing data` means the lines do not all have the same number of fields: count the lines above the real header.
2. `head -5` both data files before touching `load_customers` and `load_orders`. Count separators; count the title lines above the header — and read them: an export often says how it is written.
3. `print(df.dtypes)` and `print(df["amount"].head())` after loading — this is a script, so an inspection shows nothing without `print(...)`. If a column says `str` (or `object`, on an older pandas), it is text: what is in it besides digits? `print(df["amount"].unique())` shows every spelling, including the ones that mean "missing" — and pandas already knows some of those spellings.
4. Dates: `head -10` and `tail -10` on the orders file show how they are written without touching the script; `print(df["order_date"].head(10))` after loading shows what pandas made of them. One format or two? And is the slash layout day first or month first? Do not decide on a date like `01/02/2024`, which reads fine both ways; find one whose first number is above 12. If you name the wrong layout, every such date becomes `NaT`, and the count tells you. `pd.to_datetime` takes a `format=` that names one exact layout and an `errors="coerce"` that turns non-matches into `NaT`; two layouts means two calls, combined, then a count of the `NaT`. The error message will suggest `format="mixed"`; that guesses per value, and for a date with a day of 12 or less it can guess wrong with no error. Then check the months in the report against the dates you saw in the file.
5. `KeyError` — `print(report.columns)` on the line before. Case matters.
6. `TypeError` on the summary line — a string and a number, and `+` cannot join them. Format the number into the string.

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
