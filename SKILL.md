---
name: humanized-academic-writing
description: Use when drafting, revising or reviewing academic prose (thesis or dissertation chapter, research paper, literature review, abstract, methodology, results, discussion) that reads as generic, inflated or machine-like; when the user asks to humanize or de-AI academic text, asks for academic mode with a humanized approach, or mentions AI detectors such as Turnitin, GPTZero, Pangram or Originality.ai.
---

# Humanized Academic Writing

## Core principle

Prose reads as machine-written when it could have been written without knowing the subject. The repair is knowledge on the page: a figure, a named source, a mechanism, a limitation. Swapping words does not supply any of these.

Three commitments follow.

1. **The writer is the author.** Edit, question and restructure. Never supply a claim, figure or citation the writer has not provided. If a sentence needs a fact that is not available, ask for it or cut the sentence.
2. **No promise about detectors.** Current detectors are trained classifiers that do not score a checklist, and they flag lightly AI-polished human text at high rates (see `evidence.md`). This skill removes real defects that readers and examiners notice. It cannot guarantee a score.
3. **Disclose.** Where the institution requires an AI logbook or a statement of AI use, every session ends with a logbook entry (Step 6).

## When to use

- Revising the writer's own draft, including one written with AI assistance.
- Reviewing a draft and reporting what reads as generic.
- Drafting from the writer's notes, outline, data and sources.

If the request is to produce a section from a topic alone, ask first for the notes, sources and results it should be built from.

## Before starting

Read the writer's course rules if a file named `academic-writing-rules.md` exists in the folder that contains this skill or in the project. It governs register, tense by section, hedging vocabulary and given-new order. This skill adds to it and changes one thing: the connectives it lists (moreover, furthermore, consequently) are correct, but they are used sparingly, as set out in the recipes below.

## Workflow

**Step 1. Lock the content.** List every claim, figure, citation, technical term and defined term in the draft. These survive unchanged. A technical term keeps one name throughout; do not vary it for style.

**Step 2. Diagnose before editing.** Run `python3 scripts/style_check.py draft.txt` where file access exists, then read the draft against the checklist below. Tell the writer what was found, quoting the sentences.

**Step 3. Question the empty sentences.** Apply the swap test: replace the topic with one from another field. If the sentence is still true, it carries no information. For each such sentence, find in the writer's material, or ask the writer for, one of:

- how much (a figure with its unit and date)
- says who (author and year)
- by what mechanism (the causal step)
- compared with what (the baseline or rival finding)

If none exists, delete the sentence. This step does most of the work. Skipping it produces a tidier version of the same generic text.

**Step 4. Rewrite paragraph by paragraph** using the recipes.

**Step 5. Verify.** Check the Step 1 list item by item against the new text. Rerun the script. Run the self-checks.

**Step 6. Report and log.** Give the writer the revised text, a short list of what changed and why, and any question still open. Then draft the logbook entry:

```
Date | Tool and model | Prompt (verbatim or summarised) | Purpose | How I processed the output
```

## Recipes

**A paragraph has four parts, in this order:**

1. A topic sentence making a claim that could be checked or disputed.
2. The evidence, with its source in the same sentence or the next.
3. One sentence of interpretation: what the evidence means for the research question.
4. An ending on the newest information. The paragraph stops when the point is made.

**Sentence length follows content.** A result, a pivot or a verdict takes twelve words or fewer. A mechanism, a qualification or a synthesis of several sources takes thirty or more. After revision, a stretch of ten sentences normally contains at least one of each. Four sentences in a row within six words of one another is a reason to look again: in the three human articles measured for this skill, that happens in 0-7% of four-sentence stretches.

**Links come from given-new order.** Open a sentence with a term the previous sentence ended on, or with "this" plus a noun ("This gap", "These surveys", "Such critics"). Add a connective where the logical relation would otherwise be misread, which is mostly contrast and concession: however, yet, although, whereas. In the three human articles measured for this skill, 5-10% of sentences open with a connective. Hold a revision to about one sentence in six, with at most one additive opener (moreover, furthermore, in addition) per paragraph.

**Verbs are plain.** The subject is the thing studied and the verb says what it does: is, has, shows, finds, uses, rose, fell. Keep the passive for methods, as the course rules require.

**A hedge carries its reason.** One hedge per claim, with the source of the doubt stated: "probably because the fraction of the population above the threshold was negligible until the 1990s". Match the modal to the evidence (may, might, could are not interchangeable).

**Attribution names the source.** Author and year in the sentence that makes the claim.

**A list has as many items as there are things.** Two if there are two, four if there are four.

## Detection checklist

Ordered by how well the evidence supports each as a marker of LLM prose. Full word lists, sources and fixes are in `patterns.md`.

| Tier | Pattern | Typical form |
|---|---|---|
| Strong | Inflated significance in place of a fact | "plays a pivotal role in", "has emerged as a key challenge" |
| Strong | Trailing -ing commentary | "..., highlighting the importance of X" |
| Strong | Clusters of marker vocabulary | several of: delve, underscore, showcase, foster, leverage, multifaceted, landscape, realm |
| Strong | Noun-heavy, nominalised density | "the implementation of the optimisation of" |
| Strong | Attribution to nobody | "studies have shown", "many scholars argue" with no citation |
| Moderate | Elaborate verb where "is" or "has" belongs | "serves as", "stands as", "boasts" |
| Moderate | Contrast frame with nothing to correct | "not only X but also Y", "rather than merely" |
| Moderate | Reflex triads | three abstract nouns or adjectives in a row |
| Moderate | Formula endings | "Despite these challenges...", "Future research should explore..." |
| Moderate | Stacked sentence-initial connectives | Moreover / Furthermore / Additionally in sequence |
| Weak | Uniform sentence and paragraph length | every sentence 15-22 words |
| Weak | Dash asides, bold terms, bullet lists inside prose | chat formatting carried into a paper |

**Do not treat as defects:** formal register, the passive, correct grammar, hedging, standard reporting phrases ("This study investigates", "The results indicate"), a single connective, or a marker word that is the field's own term. Rose (2020) uses "foster" sixteen times because it is the claim under examination.

**Do not over-correct.** No inserted errors, contractions or colloquialisms. No fragments for effect. No synonym cycling for technical terms. No stripping of hedges. Keep the vocabulary range of the original.

## Example

**Before:**

> The results reveal a striking divergence between the two countries, underscoring the transformative impact of tax policy design. China's income tax system has experienced remarkable growth, showcasing the power of fiscal reform. In contrast, India's system has remained relatively stagnant, highlighting the challenges of constant adjustment.

**After:**

> The share of the Chinese population subject to income tax rose from less than 0.1% in 1986 to about 20% in 2008. In India it stayed at around 2-3%. Revenues followed the same pattern. Chinese income tax receipts grew from less than 0.1% of GDP in 1986 to 2.5% in 2008, whereas Indian receipts remained at about 0.5% (Piketty & Qian, 2009).

The first version could describe any two countries and any policy. Every figure in the second came from the source. Five more pairs, one per section type, are in `examples.md`.

## Self-check without a detector

1. **Swap test.** Would the sentence survive a change of topic? Then specify it or cut it.
2. **Three questions.** For each claim: how much, says who, compared with what?
3. **Last-sentence test.** Delete the final sentence of each paragraph. If nothing is lost, leave it out.
4. **First-words column.** List the first two words of every sentence. Look for repeats and connective runs.
5. **Length row.** Write the word count of each sentence in a row. Look for flat stretches.
6. **Tail test.** For each sentence ending in ", -ing ...": does the clause add a sourced fact? If not, stop at the comma.
7. **Defence test.** Can the writer explain each paragraph's claim and its source without the text in front of them?

`scripts/style_check.py` automates checks 4 to 6 and counts the checklist patterns. It reports features and lists sentences to reread. It is not a detector.

## Files

- `patterns.md`: full pattern catalogue with word lists, evidence and fixes
- `examples.md`: before and after pairs by section type
- `evidence.md`: research summary with sources, dated, and the measurements behind the thresholds
- `scripts/style_check.py`: self-check script (Python 3, no dependencies)
