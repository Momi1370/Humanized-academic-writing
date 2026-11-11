# Humanized Academic Writing

A skill for Claude (and other models) that revises academic prose so it reads like a competent human scholar wrote it: specific, sourced and plainly worded.

It is an editing aid. The patterns it removes are faults in the writing: each stands where a fact, a source or a reason should be. It does not promise any result from an AI detector, and it is not meant to hide AI use. Where your institution asks for an AI logbook or disclosure, the workflow ends by drafting the entry.

The skill is self-contained. It needs no course notes, style guide or sample papers. If you have a style guide or journal instructions, point the model to them and they take precedence over the built-in defaults.

## What it does

- Finds sentences that would be true of any topic and asks for the figure, source, mechanism or comparison that would make them specific.
- Removes patterns that research links to LLM prose: importance flagging ("this matters"), corrective framing ("not simply X"), trailing "-ing" commentary, attribution to nobody, stacked transitions, emphatic modifiers and stock idioms.
- Follows the 2026 evidence on which patterns are current. First-generation tells such as "delve" and heavy dash use have faded and are weighted accordingly.
- Leaves alone what is normal in academic writing: formal register, the passive, hedging, standard reporting phrases.
- Keeps every claim, figure, citation and technical term unchanged.

## Files

| File | Contents |
|---|---|
| `SKILL.md` | Principle, workflow, rewriting recipes, detection checklist, self-checks |
| `patterns.md` | Full pattern catalogue with word lists and fixes, starting with the patterns of 2026 models |
| `examples.md` | Six before and after pairs, one per section type, built from three published articles |
| `evidence.md` | Research summary with sources and confidence labels, including the November 2026 update |
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

Second version, November 2026. It adds the patterns of 2026 models (Graphite's AI Tells studies and the current Wikipedia catalogue) and removes the dependence on private course materials.

The rules were checked on six short passages and three published articles. They have not been tested against any commercial detector or on long drafts, and the 2026 patterns were measured by their sources on web articles, not on academic prose. See the last section of `evidence.md` for what was not tested.
