# Composable Writing Patterns

Use named operations instead of one undifferentiated rewrite instruction. Select only patterns required by the diagnosis.

| Pattern | Use when | Operation | Guardrail |
|---|---|---|---|
| `meaning-lock` | every mode | extract claims, literals, entities, modality, and scope | 1:1 claim map |
| `voice-match` | a sample or clear voice exists | match rhythm, openings, wording, punctuation, and deliberate quirks | do not copy claims from the sample |
| `state-directly` | staging or rhetorical run-up appears | state the supported point directly | retain real contrasts |
| `deinflate` | significance or sales language is inflated | keep the concrete fact and remove unsupported importance | do not weaken quantified claims |
| `de-slop` | filler, symmetry, or templates appear | cut redundancy and rebuild from the main point | no claim drops |
| `vary-rhythm` | openings or sentences are uniform | vary boundaries and paragraph rhythm | preserve voice |
| `grammar-mechanical` | local Indonesian writing check is needed | run the local Indonesian checklist | style suggestions are not errors |
| `claim-diff` | every rewrite | compare source and output claim by claim | fail on additions or drops |
| `flag-source-risk` | a source claim is suspicious | preserve it and add a flag | never invent a correction |
| `audience-fit` | the reader or purpose is mismatched | lead with the reader's decision or consequence | retain necessary context |

Default composition:

```text
meaning-lock
→ audience-fit
→ diagnose
→ flag-source-risk
→ de-slop
→ state-directly
→ de-inflate
→ voice-match
→ vary-rhythm
→ grammar-mechanical
→ claim-diff
→ memory-update
→ final-audit
```

Skip patterns without a trigger. Never apply `deinflate`, `de-slop`, or `state-directly` by blind word replacement.
