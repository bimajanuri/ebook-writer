# Ebook Writer

Portable Agent Skill for creating evidence-grounded e-books in Bahasa Indonesia from local source folders or structured user briefs.

The skill is designed for Agent Skills-compatible hosts, including Claude Code, OpenCode, Gemini CLI, GitHub Copilot CLI, Antigravity, Gemini Apps, ChatGPT Skills, Codex CLI, Cursor, Windsurf, and other hosts that support folder-based `SKILL.md` packages.

## What it does

| Capability | Result |
|---|---|
| Local-source e-books | Converts a folder of documents to Markdown with Microsoft MarkItDown, then maps evidence before drafting. |
| Brief-based e-books | Collects title, premise, chapter count, style, purpose, audience, and constraints. |
| Approved outline flow | Shows a 5-15 chapter outline and waits for approval before writing chapters. |
| Incremental drafting | Lets the user choose which approved chapter to write first. |
| Indonesian writing quality | Applies anti-hallucination, anti-slop, humanization, paraphrase, guardrails, citation, evaluation, and local Indonesian writing protocols. |
| Visuals | Produces Mermaid diagrams and standalone SVG illustrations. |
| Academic support | Adds evidence mapping, citation integrity, limitations, and academic guardrails when needed. |

## Non-negotiable constraints

1. **No fabrication** — never invent facts, sources, quotations, numbers, names, dates, research findings, testimonials, or bibliographic metadata.
2. **Claim fidelity** — preserve source claims, modality, scope, negation, causality, entities, and literal data.
3. **Human-readable prose** — remove generic AI scaffolding, empty transitions, forced symmetry, buzzwords, and repetitive conclusions.
4. **Indonesian output** — operational instructions are in English for cross-model compatibility; generated e-book content remains in Bahasa Indonesia unless the user requests another language.
5. **Explicit uncertainty** — flag suspicious or unavailable information. Never silently repair it with model knowledge.

## Project choices

### Writing styles

Choose exactly one:

- `Educational` — clear, progressive, concrete, and application-oriented.
- `Casual` — warm, natural, direct, and conversational without forced slang.
- `Formal` — standard, structured, official, and free of unnecessary filler.

### E-book purposes

Choose exactly one:

- `For sale`
- `Lead magnet/bonus`
- `Personal branding`
- `Course material`
- `Internal team guide`
- `Personal collection`

Indonesian labels are accepted: `Edukatif`, `Santai`, `Formal`, `Dijual`, `Lead magnet/bonus`, `Personal branding`, `Materi kelas`, `Panduan internal tim`, and `Koleksi pribadi`.

## Package layout

```text
ebook-writer/
├── SKILL.md
├── README.md
├── scripts/
│   └── convert_folder.py
├── protocols/
│   ├── academic-mode.md
│   ├── anti-hallucination.md
│   ├── anti-slop.md
│   ├── citations.md
│   ├── evaluation.md
│   ├── guardrails.md
│   ├── humanizer-id.md
│   ├── indonesian-writing.md
│   ├── paraphrase.md
│   ├── patterns.md
│   └── visuals.md
├── references/
│   ├── ai-lexicon-id.md
│   ├── citation-styles.md
│   ├── evaluation-rubric.md
│   ├── style-presets.md
│   └── workflow.md
└── checklists/
    └── final-audit.md
```

The package intentionally excludes English grammar protocols and English-language reference files. The local Indonesian writing protocol remains included because the generated e-book is Indonesian.

## Installation

Copy the complete folder, not only `SKILL.md`, into a supported skill directory:

```text
<project>/.agents/skills/ebook-writer/
~/.agents/skills/ebook-writer/
<project>/.gemini/skills/ebook-writer/
~/.gemini/skills/ebook-writer/
<project>/.claude/skills/ebook-writer/
~/.claude/skills/ebook-writer/
<project>/.github/skills/ebook-writer/
~/.copilot/skills/ebook-writer/
```

Reload the host after installation. Use its skills list or natural-language activation to verify discovery:

```text
Use the ebook-writer skill to create an Indonesian e-book.
```

## Local-source conversion

The SOURCE path requires Python 3.10-3.14 and Microsoft MarkItDown:

```bash
python -m pip install 'markitdown[all]'
python scripts/convert_folder.py --install-missing /path/to/source-folder
```

The converter writes Markdown files and `source-manifest.md` into `converted/`. It does not modify or delete source files. It reports conversion failures explicitly.

The BRIEF path does not require MarkItDown.

## Gemini Apps and ChatGPT upload

Create a clean ZIP with `SKILL.md` at the archive root:

```bash
cd /path/to/ebook-writer
zip -r -X ebook-writer.zip . \
  -x ".git/*" -x ".DS_Store" -x "__MACOSX/*" -x "*.pyc" -x "__pycache__/*"
```

Do not upload GitHub's raw `Code -> Download ZIP` archive when the host requires `SKILL.md` at the root. GitHub wraps that archive in a repository subdirectory.

Upload the clean ZIP through the host's Skills interface, then enable the skill. Availability and upload permissions depend on the host plan and current product support.

## Typical workflow

1. Choose `SOURCE` or `BRIEF`.
2. Lock title, audience, purpose, style, chapter count, genre, output format, and visual needs.
3. For `SOURCE`, convert the folder and build `evidence-map.md`.
4. Create a 5-15 chapter outline.
5. Wait for user approval.
6. Draft only the selected chapter.
7. Add Mermaid or SVG only when supported by the source or brief.
8. Run the final audit and report flags.

## Validation

Run the focused converter check:

```bash
python3 -m py_compile scripts/convert_folder.py
python3 scripts/convert_folder.py --help
```

Before delivery, verify:

- `SKILL.md` has valid YAML frontmatter;
- no excluded English grammar file is present;
- no `.DS_Store`, `.git`, `.pyc`, or `__pycache__` is packaged;
- the ZIP contains `SKILL.md` at its root;
- source claims and visual data pass the final audit.

## License

MIT. See the repository license file if one is added.
