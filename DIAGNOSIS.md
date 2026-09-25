# Diagnosis notes

**One five-part note per failure, each labelled `code` or `data`.** Copy the block below once per
failure, in the order you met them; the number of failures is yours to discover. That is the
default shape, not a rule: any organisation that gives every cause its own evidence and its own
label is fine, and two problems in the same column may share a note if it names both.

**Open this file before you start fixing anything.** Each repair destroys the traceback that
proved the failure before it. The moment a failure is on the screen, paste its last line and the
line in your file into part 3 of a new note — then fix, then write the rest.

**What decides the label.** *Code:* the failing line in the traceback is yours, and the object it
complains about has the wrong name or type because of something the code did. *Data:* the failing
line is a loader (`read_csv`, `to_datetime`) or one of the script's own checks, and `head`, `wc -l`,
`dtypes`, `.head()` on the column or `isna().sum()` show the file is not shaped the way the code
assumes. The evidence for a *data* note comes from the file first; the evidence for a *code* note
comes from the traceback and one inspection of the object.

---

## Note 1 — ______ · kind: code / data

**What told you which kind:** ______

1. **What was the symptom?**

2. **What was the actual cause?**

3. **What evidence showed that?** Paste the traceback's last line and the line in your file, then
   the inspection that showed the cause — `head -5` / `wc -l` for the file, `dtypes` / `.head()` /
   `isna().sum()` for the dataframe, `print(...columns)` / `type(...)` for an object — raw, not described.

```text

```

4. **What did you change?** (A loading option or cleaning step for *data*; a code change for *code* — and why that fix survives next month's export.)

5. **How did you verify it worked?** (The pipeline got further, and where it stopped next — or it finished, and which line of the four-line check shows the load is right.)

---

## Note 2 — ______ · kind: code / data

**What told you which kind:** ______

1. **What was the symptom?**

2. **What was the actual cause?**

3. **What evidence showed that?**

```text

```

4. **What did you change?**

5. **How did you verify it worked?**

---

*(Copy the block above for each further failure.)*
