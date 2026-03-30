# Exasol Developer Guide — Explore & Audit

Crawl the existing developer guide, surface improvement opportunities, and co-create an action plan with the user through interactive Q&A.

---

## Context

- **Project path:** `C:\Users\mufa\documents\developer-documentation`
- **Docs root:** `doc/`
- **File format:** reStructuredText (`.rst`) rendered by Sphinx
- **Target audience:** Data professionals and developers — professional but accessible
- **Gold standard sections:** `doc/connect_to_exasol/` and `doc/gen_ai/ai_text_summary/`

---

## Step 1 — Explore the Project

Read the following in parallel using Glob and Read tools:
- Full folder/file tree of `doc/` (use Glob with `doc/**/*`)
- `doc/index.rst` — top-level toctree
- Every `index.rst` inside section subfolders
- 2–3 representative content files per section (pick the most substantial ones)

Do NOT skip any section folder. Read actual file contents, not just filenames.

---

## Step 2 — Assess Each Section

Evaluate every section against the developer guide standard:

**Expected structure per section:**
1. **What** — Clear definition: what the feature/tool is, why it exists
2. **How** — Step-by-step implementation with working, copy-paste-ready code examples
3. **Benefits + Real-world use cases** — Practical scenarios, when to use it, what it enables

**Quality checklist per section:**
- Is the tone professional but accessible? Not overwhelming, not condescending.
- Are prerequisites clearly stated before any steps?
- Are code examples present and complete (not just snippets)?
- Is information up to date (no outdated version references)?
- Are there cross-references to related sections?
- Is complexity appropriate — does it avoid dumping advanced detail on beginners?
- Does it follow the What → How → Benefits structure?

---

## Step 3 — Interactive Q&A

Present your findings to the user in this structure:

**1. Current state**
Table or list of all sections with a brief quality rating (Good / Needs Work / Incomplete / Missing).

**2. Gaps identified**
Features or tools that exist in the Exasol ecosystem but have no section yet.

**3. Specific improvement areas**
Be concrete — e.g., "UDF/debugging.rst is only one sentence, needs a real debugging walkthrough" or "connect_to_exasol/connection.rst has no error handling example."

**4. Ranked suggestions**
List improvements ordered by impact (high / medium / low).

Then ask the user targeted questions to understand priorities:
- Which of these improvements matters most right now?
- Are there specific features or connectors they want to document next?
- Any sections they want to fully restructure vs. just expand?
- Anything they want to remove or consolidate?

Wait for user responses before proceeding.

---

## Step 4 — Sketch the Plan

Based on the Q&A responses, produce a concrete action plan:

For each proposed change, state:
- Section name and file(s) affected
- Type of change: **new section** / **add content** / **restructure** / **simplify**
- Brief description of what will change and why
- Priority: High / Medium / Low

Group by priority. Note which changes can be directly executed with `/exasol-implement` (content additions, modifications) versus which need a planning session first with `/exasol-new` (entirely new sections) or `/exasol-modify` (structural overhaul).

---

## Important

Do NOT write any files during this skill. This skill is exploration and planning only.
