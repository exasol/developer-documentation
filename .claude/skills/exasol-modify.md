# Exasol Developer Guide — Modify Section

Plan modifications to an existing developer guide section. Reads the current content, optionally researches updated information online, then produces a specific modification plan through interactive Q&A.

## Usage

```
/exasol-modify [section name or path]
```

Examples:
- `/exasol-modify UDF`
- `/exasol-modify connect_to_exasol`
- `/exasol-modify data_science`

---

## Context

- **Project path:** `C:\Users\mufa\documents\developer-documentation`
- **Docs root:** `doc/`
- **File format:** reStructuredText (`.rst`) rendered by Sphinx
- **Target audience:** Data professionals and developers — professional but accessible
- **Standard content structure:** What → How (step-by-step with code) → Benefits + Real-world use cases + Examples
- **Gold standard:** `doc/connect_to_exasol/` and `doc/gen_ai/ai_text_summary/`

---

## Step 1 — Locate the Section

If the user provided a section name or path, resolve it to a folder in `doc/`. If not, ask:
> "Which section do you want to modify?"

Use Glob to list all files in the section folder, then Read every file.

---

## Step 2 — Assess the Current Content

Evaluate the section against the developer guide standard:

**Expected structure:**
1. **What** — Clear definition: what the feature/tool is, why it exists
2. **How** — Step-by-step implementation with working, copy-paste-ready code examples
3. **Benefits + Real-world use cases** — Practical scenarios with concrete examples

**Check each file for:**
- Missing standard sections (What / How / Benefits)
- Incomplete or non-runnable code examples
- Outdated information (old version numbers, deprecated APIs, broken links)
- Tone issues — too technical/jargon-heavy, too vague, or condescending
- Missing prerequisites before step-by-step instructions
- Missing cross-references to related sections in the guide
- Content that is too dense and needs splitting or simplifying
- Content that is too thin and needs expanding

---

## Step 3 — Research Online (if relevant)

If the section covers a specific tool, connector, or API, check for updates:
- Search: `site:docs.exasol.com [topic]`
- Search: `site:github.com/exasol [topic]`
- Check for: new versions, changed APIs, new features, deprecated functionality

Only fetch URLs if you find something likely to contain useful updated information.

---

## Step 4 — Interactive Q&A

Present your assessment clearly:

**1. What exists** — Brief summary of current content per file
**2. What's missing** — Gaps against the standard structure
**3. What needs fixing** — Specific issues (be concrete, not vague)
**4. What could be cut** — Content that is redundant, outdated, or out of scope

Then ask the user:
1. What specifically prompted this modification request?
2. Are there new features, API changes, or corrections to document?
3. Should the file structure stay the same, or should files be split/merged/renamed?
4. Are there new code examples to add?
5. Anything to remove or simplify?
6. Any tone or style issues they've noticed?

Wait for responses before producing the plan.

---

## Step 5 — Sketch the Modification Plan

For each file to be changed, state:

**File path:**
**Current state:** (one-line summary)
**Changes:**
- [ ] Specific addition/removal/edit — be precise (e.g., "Add error handling try/except example after the connect() code block")
- [ ] Another change...

**New content to add:** (brief description with key points, not full RST)

**Content to remove:** (quote or describe the part to cut)

**Structural changes:** (e.g., split into two files, rename, reorder sections)

If a new file needs to be created as part of the modification, note it and its proposed content outline.

---

## Important

Do NOT write any files. This skill produces a plan only.
The user will run `/exasol-implement` to apply the changes once the plan is approved.
