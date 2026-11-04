# Project Memory and Token Efficiency

Use compact project memory so later chapter requests do not require the user or model to repeat the full brief, source inventory, or previous decisions.

## Required memory files

For a complete project, create:

```text
project-memory.md
chapter-ledger.md
decision-log.md
```

### `project-memory.md`

Store stable, reusable facts only:

- title and subtitle;
- selected path: `SOURCE` or `BRIEF`;
- purpose and style;
- audience and genre;
- approved promise or central argument;
- canon facts, entities, terminology, point of view, tense, and boundaries;
- source manifest and evidence-map location;
- current chapter and next action;
- unresolved risks.

Use a compact table. One fact should appear once.

### `chapter-ledger.md`

Store one row per chapter:

| Chapter | Status | One-line purpose | Key decisions | Open items | Last updated |
|---:|---|---|---|---|---|

Allowed statuses: `OUTLINED`, `APPROVED`, `DRAFTING`, `DRAFTED`, `REVISED`, `FINAL`, `BLOCKED`.

Do not paste chapter text into the ledger. Keep summaries short enough to scan in one read.

### `decision-log.md`

Record only decisions that affect later work:

| ID | Decision | Reason | Affected chapters | Status |
|---|---|---|---|---|

Use `OPEN`, `RESOLVED`, or `REVISIT`.

## Read protocol for each chapter

Before drafting a chapter:

1. Read `project-memory.md`.
2. Read the selected chapter row in `chapter-ledger.md`.
3. Read relevant `decision-log.md` rows.
4. Read only the evidence-map entries and source sections required by that chapter.
5. Do not reread unrelated chapters or the full source folder unless a contradiction requires it.

## Write protocol after each chapter

After drafting or revising:

1. Update the chapter status and one-line summary.
2. Add only new durable decisions.
3. Update the current chapter and next action.
4. Record unresolved questions once.
5. Avoid copying prose, source documents, or repeated instructions into memory.

## Token-saving rules

- Prefer pointers over pasted content: use file paths, headings, page numbers, and anchors.
- Summarize repeated context once.
- Use stable IDs for claims, decisions, characters, concepts, and visual assets.
- Reuse approved terminology and style without re-explaining it.
- Load the smallest relevant evidence slice.
- Ask for missing decisions only; do not ask for information already stored.
- Do not regenerate an approved outline unless the user requests a structural change.
- Do not restate the complete project contract in every chapter response.
- When context is uncertain, report the exact missing item instead of loading everything.

## Memory integrity

- Memory is a project index, not a second source of truth.
- Evidence remains in source files and `evidence-map.md`.
- If memory conflicts with evidence, flag the conflict and update memory only after resolution.
- Never store secrets, credentials, private tokens, or unnecessary personal data.
- Keep memory human-readable and version-controlled with the project.

## Minimal chapter handoff

Use this internal handoff shape:

```text
project: <title>
purpose: <purpose>
style: <style>
audience: <audience>
chapter: <number and title>
status: <status>
must_preserve: <stable facts, entities, terminology>
decisions: <relevant decision IDs>
evidence: <relevant file/heading/page pointers>
open_items: <only unresolved items>
next_action: <one action>
```
