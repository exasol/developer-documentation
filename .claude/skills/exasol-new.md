# Exasol Developer Guide — New Section

Plan a new developer guide section for an Exasol feature, connector, or tool. Searches online for relevant content and produces a structured plan ready for `/exasol-implement`.

## Usage

```
/exasol-new [feature or topic name]
```

Examples:
- `/exasol-new kafka connector`
- `/exasol-new jdbc driver`
- `/exasol-new virtual schemas`

---

## Context

- **Project path:** `C:\Users\mufa\documents\developer-documentation`
- **Docs root:** `doc/`
- **File format:** reStructuredText (`.rst`) rendered by Sphinx
- **Target audience:** Data professionals and developers — professional but accessible
- **Gold standard examples:** `doc/connect_to_exasol/` (connector) and `doc/gen_ai/ai_text_summary/` (tutorial)
- **Standard content structure:** What → How (step-by-step with code) → Benefits + Real-world use cases + Examples

---

## Step 1 — Identify the Subject

If the user provided a feature/topic name as an argument, use it. If not, ask:
> "What feature, connector, or tool do you want to document?"

---

## Step 2 — Research Online

Use WebSearch and WebFetch to gather information from all of the following:

**Official Exasol sources:**
- Search: `site:docs.exasol.com [topic]`
- Search: `site:github.com/exasol [topic]`
- Fetch the relevant Exasol docs page if found

**Package registry (if applicable):**
- Search: `site:pypi.org [topic] exasol`
- Fetch the PyPI page if a Python package exists

**General:**
- Search: `[topic] exasol tutorial getting started`
- Search: `[topic] exasol example`

From the research, extract:
- What the feature/tool does and why it exists
- Key concepts and terminology
- Official API / configuration parameters
- Code examples and usage patterns
- Prerequisites and system requirements
- Common real-world use cases
- Links to authoritative external documentation

---

## Step 3 — Read the Existing Project

Read these files to ensure the new section fits the project's conventions:
- `doc/index.rst` — understand the current top-level toctree structure
- `doc/connect_to_exasol/index.rst` and one content file from it
- `doc/gen_ai/ai_text_summary/index.rst`

Note the RST formatting conventions, heading styles, and toctree patterns used.

---

## Step 4 — Ask Clarifying Questions

Before sketching the plan, ask:

1. Is this a **connector**, a **feature**, a **tool**, or a **tutorial/example**?
2. Who is the primary user — data engineers, analysts, data scientists, or all?
3. Are there existing code examples or GitHub repos to reference?
4. Any specific aspects to emphasize — e.g., performance, ease of setup, integrations?
5. Should this be a **top-level section** in `doc/` or a **subsection** of an existing one (e.g., under `examples/` or `data_science/`)?
6. Are there any topics that should be excluded or kept minimal?

Wait for user responses before sketching the plan.

---

## Step 5 — Sketch the Plan

Output a concrete plan with the following:

### Proposed Folder Structure

```
doc/[section-folder-name]/
├── index.rst          — Section landing page with toctree
├── overview.rst       — What: definition, key concepts, system requirements
├── installation.rst   — (if applicable) Setup, dependencies, pip/brew commands
├── [descriptive].rst  — How: step-by-step with working code examples
└── [examples].rst     — Real-world use cases and complete end-to-end examples
```

Adjust the file list based on the complexity and type of content.

### Per-File Content Plan

For each file, state:
- **Title**
- **Sections/headings** to include
- **Key content points** (bullet list — not full content)
- **Code examples** to include (language, what the example shows)
- **External links** to reference (from research in Step 2)

### Toctree Update

State exactly:
- Which line in `doc/index.rst` to insert the new entry (between which existing entries)
- The exact toctree entry string (e.g., `   [section-folder-name]/index.rst`)

### Cross-References

Note any `:ref:` links to or from existing sections that should be added.

---

## Important

Do NOT write any files. This skill produces a plan only.
The user will run `/exasol-implement` to write the files once the plan is approved.
