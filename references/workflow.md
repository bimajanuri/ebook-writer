# E-Book Workflow

## Stage 0 — Contract

Lock the path, title, premise or source folder, purpose, audience, style, chapter count, genre, output format, and visual needs. Purpose must be `For sale`, `Lead magnet/bonus`, `Personal branding`, `Course material`, `Internal team guide`, or `Personal collection`. Style must be `Educational`, `Casual`, or `Formal`. Record assumptions. Never change them silently.

## Stage 1 — Source

For `SOURCE`, convert files and create the manifest and evidence map. For `BRIEF`, separate supplied facts, allowed creative decisions, and unresolved details.

## Stage 2 — Outline

Create a 5-15 chapter outline. Each chapter must have a distinct function. Write and verify `outline.md` first. Then show the outline and wait for approval.

## Stage 3 — Draft

Write only the selected chapter. Keep terminology, characters, timeline, point of view, and certainty consistent. Save it as `chapters/NN-title.md`, read it back, and report the exact path. Record new decisions in the project memory files.

## Stage 4 — Visuals

Choose visuals that improve understanding. Use Mermaid for structure or process. Use SVG for standalone illustrations. Never turn unsupported information into a data chart.

Save Mermaid diagrams in `visuals/diagrams.md` and SVG assets in `visuals/`. Verify every saved visual.

## Stage 5 — Audit

Run anti-hallucination, anti-slop, Indonesian writing, style, structure, visual, and memory audits. Status: `PASS`, `PASS_WITH_FLAGS`, or `FAIL`.

Save audit records in `audits/` before reporting completion.

## Stage 6 — Revision

Fix only approved findings or clear contract violations. Re-run affected audits after revision.

## Stage 7 — Memory update

After each approved chapter, update only the compact memory records:

- `project-memory.md` for stable facts and current project state;
- `chapter-ledger.md` for chapter status and one-line summaries;
- `decision-log.md` for decisions, assumptions, and unresolved questions.

Do not copy full chapters into memory files.

## Stage 8 — Persistence gate

Before delivery:

1. confirm the project root;
2. confirm required directories exist;
3. write all requested artifacts;
4. read each artifact back;
5. confirm non-empty content;
6. report exact paths;
7. stop with an explicit failure if any write or read-back check fails.
