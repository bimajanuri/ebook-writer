# Anti-Hallucination and Evidence Grounding

## Claim inventory

For each claim, record:

- claim text or summary;
- provenance such as `file:heading`, `file:page`, or `brief`;
- type: fact, number, opinion, quotation, causal claim, prediction, or fiction;
- certainty level;
- status: `VERIFIED`, `SOURCE-RELATIVE`, `UNVERIFIED`, or `CONFLICT`.

## Creation boundary

You may reorganize, summarize, connect, and write transitions. You may not add names, numbers, dates, sources, quotations, studies, examples presented as facts, or background claims not supplied by the source or brief.

For fiction, new details are allowed only when the brief permits creative invention. Record them as project decisions and keep them consistent with the project canon.

## Flags

Do not silently correct a suspicious claim:

```text
Flag: [claim] — status [UNVERIFIED/CONFLICT]. Verify or revise before publication.
```

## Gate

- every source claim has an output counterpart;
- every output claim has a source or approved creative decision;
- negation, numbers, names, quotations, causality, and certainty are preserved;
- placeholders are reported;
- no full source text is duplicated in memory records.
