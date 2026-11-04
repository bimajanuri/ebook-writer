# Humanize Protocol — Indonesian (HUM / id)

Goal: remove machine-like writing patterns while keeping Indonesian prose natural, accurate, and faithful to the source. Detection uses the 26 baseline AI patterns plus Indonesian-specific signals. The supporting lexicon is `references/ai-lexicon-id.md`.

## Method rule

Rewrite the underlying idea. Do not merely replace one formal word with a dictionary synonym. Synonym swapping keeps the machine skeleton intact.

## Pattern families

### A. Empty openings and essay scaffolding

1. Cliché world-opening: replace phrases such as `Dalam era globalisasi yang serba cepat ini...` with the actual point.
2. `Tak dapat dipungkiri` and `Tidak dapat dipungkiri bahwa`: remove them; state or support the claim directly.
3. `Perlu diketahui` and `Perlu dicatat`: remove them unless the notice itself is necessary.
4. Article-introduction filler such as `Artikel ini akan membahas...`: replace with a concrete problem, event, number, or question.
5. Cliché closings such as `Semoga artikel ini bermanfaat`: replace with a useful conclusion or omit it.
6. Empty invitations such as `Yuk, simak sampai habis!`: remove them.

### B. Rigid formality and English calques

7. English-syntax calques such as `memainkan peran penting`, `memberikan dampak yang signifikan`, and `memiliki kemampuan untuk`: use natural Indonesian structures.
8. Weak verb plus noun stacks: prefer direct verbs such as `menganalisis`, `mengamati`, `menilai`, and `menjelaskan`.
9. Layered formal padding such as `Berdasarkan hal tersebut di atas...`: write one direct sentence.
10. Passive voice without a useful actor: identify who acts and what they do.

### C. Rhythm and syntax

11. Do not force a three-part list when the items are not genuinely parallel.
12. Vary repeated sentence openings such as `Dengan...`, `Selain itu...`, and `Di sisi lain...`.
13. Use one connector per transition; avoid stacks such as `namun demikian` or `akan tetapi`.
14. Mix sentence lengths deliberately.
15. Reduce excessive ellipses, exclamation marks, and conversational filler.

### D. Inflated authority

16. Replace vague signals such as `sangat penting`, `revolusi`, `sinergi`, `komprehensif`, and `terdepan` with their concrete meaning.
17. Remove unsupported significance inflation.
18. Explain a mechanism when using a causal verb such as `mempengaruhi`.
19. Name a source for claims such as `para ahli sepakat`; otherwise lower the claim to an attributed or reasoned opinion.

### E. Formatting and chat residue

20. Use bold only for real terms or headings, not decoration.
21. Avoid decorative titles and excessive emoji unless the audience requires them.
22. Normalize pasted AI formatting without changing content.
23. Remove chat residue such as `Tentu! Berikut adalah...`, `Semoga membantu!`, and `Sebagai AI...`.
24. Do not open a paragraph with meta-commentary about the document structure.
25. Do not repeat the title as the first sentence.
26. Write for the actual reader. Lead with the decision, subject, or consequence they need.

## Density heuristic

- At least two occurrences of one pattern per page: fix all occurrences.
- At least three pattern families in one paragraph: rewrite from the paragraph's idea.
- If unsure, read aloud. If it sounds like a corporate presentation or a generic academic template, rewrite it.

## Do not humanize away

- established technical, legal, medical, or academic terms;
- deliberate formal voice;
- quotations, titles, people, and institutions;
- grammar or precision;
- uncertainty and source attribution.

Do not add typos, forced slang, or casual abbreviations to imitate humans.

## Voice reconstruction

When the source has no clear voice:

1. identify the implied reader and purpose;
2. choose one voice, such as an informed practitioner who is direct and concrete;
3. apply it consistently;
4. record the choice in the change log when it may matter to the user.

## Verification pass

After rewriting:

- scan again with `references/ai-lexicon-id.md`;
- keep any remaining signal only when it is precise, quoted, or necessary;
- check sentence rhythm and paragraph openings;
- check decorative formatting;
- confirm that the draft answers the reader's need without repeating available context.

The generated text remains in Bahasa Indonesia. This protocol is written in English for cross-model compatibility.
