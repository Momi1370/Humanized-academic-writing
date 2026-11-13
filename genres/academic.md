# Academic writing

Thesis and dissertation chapters, papers, literature reviews, abstracts, reports. The avoid list in `SKILL.md` was built on this genre, so it applies here without adjustment.

## Ask first

- Which section is this (introduction, literature review, methods, results, discussion, conclusion, abstract)?
- What are the research question and the claim of this section?
- Which sources, data and results should it be built from? If the request is to produce a section from a topic alone, ask for these before writing anything.
- Is there a style guide, a set of course or journal instructions, or a word limit?

## Defaults

A supplied style guide overrides these.

| Convention | Default |
|---|---|
| Register | Formal. No contractions or colloquialisms. First person only where the field accepts it. |
| Tense | Present perfect for the state of research ("has been studied"). Simple past for procedures and for reported data. Simple present for tables and figures, interpretation and conclusions. |
| Voice | Passive for procedures in the methods section. Elsewhere, active when the actor matters. |
| Hedging | The modal matches the strength of the evidence. |
| Order | Known information opens the sentence; new information ends it. |
| Citation | The style the writer already uses, unchanged. |

One point holds even against a style guide that lists them: connectives such as moreover, furthermore and consequently are correct, but they are used sparingly, as set out below.

## Structure to build on

Build the paragraph on these before checking it for defects. Each avoid-list pattern is what fills a slot when the content for it is missing. Worked examples, a section-by-section table, the build order and public sources are in `structures.md`.

| Structure | Rule | What it displaces |
|---|---|---|
| Claim, evidence, interpretation | A checkable claim, its evidence with the source, then what the evidence means for the research question | Importance flags, formula endings, coverage without argument |
| Given-new flow | Open on what the reader already has; end on what is new | Stacked transitions |
| Hedge with a reason | One hedge per claim, with the source of the doubt in the sentence | Hedge stacks, "should be interpreted with caution" |
| Concrete subject and verb | The thing studied is the subject and its action is the verb | "Serves as", nominalised density, emphatic modifiers |
| Length from content | Short for a result or a turn; long for a mechanism or a qualification | Uniform rhythm |

The rules in full:

**A paragraph has four parts, in this order:**

1. A topic sentence making a claim that could be checked or disputed.
2. The evidence, with its source in the same sentence or the next.
3. One sentence of interpretation: what the evidence means for the research question.
4. An ending on the newest information. The paragraph stops when the point is made.

**Sentence length follows content.** A result, a pivot or a verdict takes twelve words or fewer. A mechanism, a qualification or a synthesis of several sources takes thirty or more. After revision, a stretch of ten sentences normally contains at least one of each. Four sentences in a row within six words of one another is a reason to look again: in the three published articles measured for this skill (`evidence.md`, section 5), that happens in 0-7% of four-sentence stretches.

**Links come from given-new order.** Open a sentence with a term the previous sentence ended on, or with "this" plus a noun ("This gap", "These surveys", "Such critics"). Add a connective where the logical relation would otherwise be misread, which is mostly contrast and concession: however, yet, although, whereas. In the same three articles, 5-10% of sentences open with a connective. Hold a revision to about one sentence in six, with at most one additive opener (moreover, furthermore, additionally, in addition) per paragraph.

**Verbs are plain.** The subject is the thing studied and the verb says what it does: is, has, shows, finds, uses, rose, fell. Keep the passive for procedures in the methods section.

**A contrast needs an opponent.** Write "not X but Y" or "Y rather than X" when a cited source holds X. Otherwise state Y.

**Magnitude replaces emphasis.** Where the draft says drastically, remarkable or crucial, give the figure, the comparison or the consequence. If none exists, the modifier goes.

**A hedge carries its reason.** One hedge per claim, with the source of the doubt stated: "probably because the fraction of the population above the threshold was negligible until the 1990s". Match the modal to the evidence (may, might, could are not interchangeable).

**Attribution names the source.** Author and year in the sentence that makes the claim.

**A list has as many items as there are things.** Two if there are two, four if there are four.

## Not defects here

Formal register, the passive, hedging as such, standard reporting phrases ("This study investigates", "The results indicate"), a chapter roadmap, parallel wording across hypotheses or propositions, a technical term repeated without variation, and a marker word that is the field's own term. Rose (2020) uses "foster" sixteen times because it is the claim under examination.

Do not add contractions, colloquialisms, rhetorical questions or a personal voice the field does not use.

## Extra self-checks

Run these after the seven in `SKILL.md`.

1. **Slot test.** Mark each sentence of a paragraph C (claim), E (evidence) or I (interpretation). A sentence that takes no mark is a candidate for cutting. A paragraph with no E needs material from the writer.
2. **First-words column.** List the first two words of every sentence. Look for repeats and connective runs, and check that each opener points back to the sentence before.
3. **Length row.** Write the word count of each sentence in a row. Look for flat stretches.

`scripts/style_check.py` automates checks 2 and 3.

## Example

The pair in `SKILL.md` is a results paragraph. `examples.md` has one pair for each of: introduction, literature review, discussion, conclusion and methods.

## Sources

Listed in `structures.md` and in `evidence.md`, sections 2 to 5 and 7.
