# ebook-writer

Skill Agent Skills portabel untuk membuat e-book Bahasa Indonesia.

## Isi

- `SKILL.md` — router dan aturan utama.
- `scripts/convert_folder.py` — konversi folder lokal ke Markdown dengan Microsoft MarkItDown.
- `references/` — alur proyek, preset gaya, lexicon AI Bahasa Indonesia, sitasi, dan rubric evaluasi.
- `protocols/` — anti-halusinasi, anti-slop, humanizer Bahasa Indonesia, paraphrase, patterns, guardrails, evaluasi, sitasi, penulisan Indonesia, akademik, dan visual.
- `checklists/` — audit akhir.

## Instalasi lintas platform

Salin seluruh folder, bukan hanya `SKILL.md`, ke salah satu lokasi yang didukung:

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

Untuk upload Gemini atau ChatGPT, buat ZIP bersih dengan `SKILL.md` di root arsip:

```bash
cd /path/to/ebook-writer
zip -r -X ebook-writer.zip . \
  -x ".git/*" -x ".DS_Store" -x "__MACOSX/*" -x "*.pyc" -x "__pycache__/*"
```

Jangan memakai ZIP repository GitHub mentah bila platform mensyaratkan `SKILL.md` di root.

## Prasyarat konversi

Python 3.10–3.14 dan Microsoft MarkItDown:

```bash
python -m pip install 'markitdown[all]'
```

Skill tetap dapat membuat e-book dari brief tanpa MarkItDown.

## Pilihan proyek

Gaya: `Edukatif`, `Santai`, atau `Formal`.

Tujuan: `Dijual`, `Lead magnet/bonus`, `Personal branding`, `Materi kelas`, `Panduan internal tim`, atau `Koleksi pribadi`.
