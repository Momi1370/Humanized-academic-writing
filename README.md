# Humanized Writing

A skill for Claude (and other models) that drafts and revises text a person will send under their own name, so that it reads as written by someone who knows the subject and the reader: specific, sourced, plainly worded and shaped for its genre.

It covers five kinds of writing:

| Genre | File |
|---|---|
| Thesis, dissertation, paper, literature review, abstract | `genres/academic.md` |
| Email and letters | `genres/email.md` |
| CV, résumé and cover letter | `genres/cv.md` |
| Research, grant and project proposals | `genres/proposal.md` |
| Slides and talk scripts | `genres/presentation.md` |

It is an editing aid. The patterns it removes are faults in the writing: each stands where a fact, a source or a reason should be. It does not promise any result from an AI detector, and it is not meant to hide AI use. Where your institution or employer asks for an AI logbook or disclosure, the workflow ends by drafting the entry.

The skill is self-contained. If you have a style guide, a template, a call for proposals, a job advertisement or a sample of your own writing, give it to the model: the skill asks for one, and it takes precedence over the built-in defaults.

## How it works

- **One avoid list for every genre.** Importance flagging ("this matters"), corrective framing ("not simply X"), trailing "-ing" commentary, attribution to nobody, praise without evidence, stacked transitions, emphatic modifiers and chat residue are faults in a thesis, an email and a CV alike.
- **One structure per genre.** The skill first works out what is being written and who reads it, asking when the request does not say. It then builds on that genre's structure: claim, evidence and interpretation for a paragraph; purpose first and next step last for an email; verb, object, method and result for a CV bullet; the reviewer's five questions for a proposal; a sentence title with visual evidence for a slide.
- **The writer stays the author.** Sentences that would be true of any topic, employer or recipient are sent back as questions: how much, says who, by what mechanism, compared with what. The skill never supplies a figure, citation or achievement.
- **Current evidence.** It follows the 2026 research on which patterns are current. First-generation tells such as "delve" and heavy dash use have faded and are weighted accordingly.
- **Genre conventions are left alone.** Formal register and the passive in a paper, a salutation in an email, fragments in a CV and repetition in a talk are not defects.

## Files

| File | Contents |
|---|---|
| `SKILL.md` | Principle, goal routing, workflow, the shared avoid list, self-checks |
| `genres/*.md` | Per genre: what to ask, the structure to build on, the forms the avoid list takes, a before and after pair, public sources |
| `patterns.md` | The full avoid list with word lists, evidence and repairs |
| `structures.md` | The academic structures in full: rules, examples, a table by section, a build order |
| `examples.md` | Six academic before and after pairs, built from three published articles |
| `evidence.md` | Research summary with sources and confidence labels, and what was not tested |
| `scripts/style_check.py` | Self-check script (Python 3, no dependencies) |

## Install

**Claude Code:**

```bash
git clone https://github.com/Momi1370/Humanized-academic-writing ~/.claude/skills/humanized-writing
```

Then ask Claude to draft or revise a text, or invoke `/humanized-writing`.

**Other models:** paste `SKILL.md`, `patterns.md` and the one genre file you need into the system prompt.

## Self-check script

```bash
python3 scripts/style_check.py draft.txt                  # academic prose (default)
python3 scripts/style_check.py draft.txt --genre email    # or cv, proposal, presentation
```

The script counts the avoid-list patterns, lists sentences worth rereading, and reports invisible characters and leftover placeholders. For academic prose and proposals it also reports sentence-length variation and connective use. It is not an AI detector. A clean report says nothing about how a detector will score the text.

## Status

Fourth version, November 2026. It widens the skill from academic prose to five genres: the avoid list became shared, the academic conventions moved into `genres/academic.md`, and four genre files were added from public writing-centre and careers guidance.

What has been checked: the academic rules on six short passages and three published articles; the script on those and on the examples in the genre files. What has not: any commercial detector, long drafts, and the four new genres on real drafts. The avoid list was measured by its sources on academic abstracts and web articles, and its use on emails, CVs, proposals and slides is an inference. See the last section of `evidence.md`.

## Credits

Three patterns and two practices are adapted from [blader/humanizer](https://github.com/blader/humanizer) (MIT licence). All sources are listed in `evidence.md`.
