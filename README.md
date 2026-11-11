# Humanized Academic Writing

A skill for Claude (and other models) that revises academic prose so it reads like a competent human scholar wrote it: specific, sourced and plainly worded.

It is an editing aid. It does not promise any result from an AI detector, and it is not meant to hide AI use. Where your institution asks for an AI logbook or disclosure, the workflow ends by drafting the entry.

## What it does

- Finds sentences that would be true of any topic and asks for the figure, source, mechanism or comparison that would make them specific.
- Removes patterns that research links to LLM prose: inflated significance, trailing "-ing" commentary, clusters of marker vocabulary, attribution to nobody, stacked connectives.
- Leaves alone what is normal in academic writing: formal register, the passive, hedging, standard reporting phrases.
- Keeps every claim, figure, citation and technical term unchanged.

## Files

| File | Contents |
|---|---|
| `SKILL.md` | Principle, workflow, rewriting recipes, detection checklist, self-checks |
| `patterns.md` | Full pattern catalogue with word lists and fixes |
| `examples.md` | Six before and after pairs, one per section type |
| `evidence.md` | Research summary with sources and confidence labels |
| `scripts/style_check.py` | Self-check script (Python 3, no dependencies) |

## Install

**Claude Code:**

```bash
git clone https://github.com/Momi1370/Humanized-academic-writing ~/.claude/skills/humanized-academic-writing
```

Then ask Claude to revise a draft in academic mode, or invoke `/humanized-academic-writing`.

**Other models:** paste `SKILL.md` and `patterns.md` into the system prompt.

## Self-check script

```bash
python3 scripts/style_check.py draft.txt
```

The script reports sentence-length variation, connective use and pattern counts, and lists sentences worth rereading. It is not an AI detector. A clean report says nothing about how a detector will score the text.

## Status

First version. The rules were checked on six short passages and three published articles. They have not been tested against any commercial detector or on long drafts. See the last section of `evidence.md` for what was not tested.
