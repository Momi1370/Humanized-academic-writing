# Pattern Catalogue

Each entry gives the pattern, why it counts, and the repair. Sources are listed in `evidence.md`.

No single pattern shows that a text was machine-written. Humans produced all of them before 2022. What marks LLM prose is several at once, at high density, attached to sentences that say nothing specific.

Each pattern is also a fault in the writing, whoever wrote it: it takes the place of a fact, a source or a reason. That is the ground for removing it. Removing it does not make a text pass a detector, and this catalogue is not written for that purpose.

---

## Priority patterns in 2026 models

Added November 2026 from Graphite's AI Tells studies (September and October 2026), the October 2026 version of Wikipedia: Signs of AI writing, and Kobak et al. (2025). Sources, figures and confidence notes are in `evidence.md`, section 3.

Read the figures with two limits in mind. Graphite measured web articles written to one fixed prompt, so a ratio such as "70 times the human rate" describes that genre and does not transfer to a thesis. And the wording rotates: 55-72% of the tells Graphite found are unique to one version of a model family. P1 to P3 are moves that recur across versions and families. P4 to P6 are strongest in Gemini.

The repairs use facts from the three articles cited in `examples.md`.

### P1. Importance flagging (all families)

The sentence announces that something matters. The reason is missing or arrives later.

- Current forms: "this matters", "why X matters", "X matters because", "the distinction matters", "just as important", "absolutely essential"
- Older forms, rarer in current models but still common in drafts: "played a crucial role", "stands / serves as a testament to", "underscores the importance of"

"This matters" ran at 116 times the human rate and "why _ matters" at 92 times in Claude Opus 5.5; "matters because" at 357 times in GPT-6 Astra (Graphite, 2026).

**Repair:** delete the flag and state the reason as a fact.

> The design of the exemption threshold matters. → India raised its exemption threshold repeatedly, which kept the taxpaying population near 2-3% (Piketty & Qian, 2009).

See also A1.

### P2. Corrective framing (all families)

The sentence corrects a view that nobody in the text holds. Also called negative parallelism.

- "not simply X", "rather than simply / merely X"
- "is more than a ...; it is ...", "is not just X; it is Y"
- "less like X and more like Y", "not X, but Y"
- the reversed form, "Y rather than X"

"Not simply" ran at 157 times the human rate in GPT-6 Astra, "is not just a _ it is" at 153 times in Gemini 3.1 Pro and "is more than a _ it" at 98 times in Claude Opus 5.5 (Graphite, 2026). Wikipedia's editors describe the reversed form as particularly common in recent output.

**Repair:** ask who holds X. If a source does, cite it and keep the contrast. If nobody does, state Y.

> Economic growth is more than a policy target; it is a question of justice. → Rose (2020) argues that an affluent society may justly stop aiming for growth.

See also B3.

### P3. Sentence-final participial commentary (all families)

A clause after the final comma that comments on the sentence and adds no fact: highlighting, underscoring, emphasizing, contributing to, fostering, ensuring, reflecting. Wikipedia's list adds symbolizing, encompassing and enhancing.

Instruction-tuned models produce present-participle clauses at two to five times the human rate (Reinhart et al., 2025). Graphite did not measure this construction, so the evidence for 2026 models is the Wikipedia catalogue alone.

**Repair:** as in A4. Stop at the comma, or give the consequence its own sentence with a subject and a source.

### P4. Dense formal transitions (Gemini)

Furthermore, additionally and conversely at the head of sentence after sentence.

"Furthermore" appears in 45% of Gemini 4 Argon's articles, at 24 times the human rate, and in none of GPT-6 Astra's and one of Claude Opus 5.5's. "Conversely" runs at 14 times the human rate and "additionally" at 3.2 times (Graphite, 2026). GPT and Claude link with other stock phrases ("together these", "looking ahead").

This is a density signal tied to one model family. Wikipedia lists a transition word in isolation as an ineffective indicator, and one "furthermore" in a paragraph is ordinary academic English.

**Repair:** as in B6. Link by given-new order and keep at most one additive opener per paragraph. Use "conversely" only when the second statement reverses the first.

### P5. Emphatic modifiers and stock idioms (Gemini)

| Type | Examples, with Gemini 4 Argon's rate relative to human writing |
|---|---|
| Modifiers | drastically (12x), unmatched (6.5x), fantastic (4.2x), incredible (2.6x); in Gemini 3.1 Pro also incredibly, profound, immense, remarkably |
| Idioms | bridges the gap (70x), fast-paced world (51x), half the battle (37x), heavy lifting (15x), crystal clear (10x), gold standard (10x) |

Most of these are wrong for a thesis on grounds of register alone.

**Repair:** replace the modifier with the magnitude and the idiom with the literal statement.

> Waste collection improves drastically as income rises. → Low-income countries collect less than 50% of their waste and high-income countries more than 90% (Hoornweg and Bhada-Tata, as cited in Debrah et al., 2021).

Two of the idioms have legitimate uses. "Gold standard" is an established term in diagnostic and clinical research, although many journals now prefer "reference standard"; follow the field. "Bridges the gap" appears in human gap statements too; keep it only if the next words name the gap.

### P6. Mannered prose (highest in Gemini)

Metaphor and flourish where a direct statement belongs. On a 0-100 scale scored by a language model, human articles averaged 6.7, GPT-6 Astra 7.9, Claude Opus 5.5 10.6 and Gemini 4 Argon 19.5 (Graphite, 2026).

**Repair:** translate the figure of speech into the literal claim. If nothing literal is left, cut the sentence. Keep a metaphor that has become the field's term (bottleneck, spillover).

### What has weakened

- **First-generation vocabulary.** Wikipedia's editors date delve, tapestry, vibrant and testament to models of 2023 to mid-2024 and report that "delve" fell sharply in 2025. One such word is weak evidence of anything. A cluster in an empty sentence is still poor writing and still worth removing. Drafts produced with older tools keep the older words.
- **Dashes.** GPT-6 Astra uses dashes 88% less often than pre-2022 human writers and Claude Opus 5.5 almost never. Gemini 4 Argon uses more than its predecessor but still 38% fewer than the human baseline (Graphite, 2026). Wikipedia's editors now note the opposite sign in some models: no dashes at all, with commas and full stops doing the work. Neither the presence nor the absence of dashes says much. Follow the field's house style.

---

## A. Content patterns

These survive paraphrasing and word substitution, and they are what experienced readers notice (Russell et al., 2025).

### A1. Significance in place of substance

The sentence asserts that something matters and stops.

- "X plays a crucial / pivotal / vital / key role in Y"
- "X has emerged as a significant challenge"
- "X is a testament to", "marks a turning point", "reflects broader trends"
- "the evolving landscape of", "in the realm of"
- "cannot be overstated"
- 2026 forms: "this matters", "why X matters", "matters because" (see P1)

**Repair:** state the fact that makes it matter. "SWM plays a vital role in urban sustainability" becomes "Low-income countries collect less than 50% of the waste they generate."

### A2. Generic claims

True of any topic. Found with the swap test.

- "This is a complex and multifaceted issue."
- "Various factors influence the outcome."
- "This has important implications for policy and practice."

**Repair:** name the factors, the implication, the policy. If the writer cannot, delete.

### A3. Attribution to nobody

- "Studies have shown", "Research suggests", "Many scholars argue", "Experts agree"
- "It is widely accepted / recognised that"
- "Some critics argue" where one source is meant

**Repair:** author and year, in that sentence. If the claim rests on one study, say one study.

### A4. Trailing -ing commentary

A participial clause after a comma that comments on the main clause without adding a fact.

- "..., highlighting the importance of..."
- "..., underscoring the need for..."
- "..., reflecting broader trends in..."
- "..., contributing to / paving the way for / ensuring..."

LLMs produce present-participle clauses at two to five times the human rate (Reinhart et al., 2025).

**Repair:** stop at the comma. If the clause holds a real consequence, give it its own sentence with a subject and a source.

**Not the same thing:** a fronted participial clause whose subject is the main-clause subject ("Using annual tabulations from urban household surveys, we compute...") is standard academic English.

### A5. Formula endings

- "Despite these challenges, X continues to..."
- "Future research should explore innovative approaches to..."
- "Ultimately, a collaborative effort among stakeholders..."
- Paragraphs that close by restating their topic sentence.

**Repair:** name the actual limitation and what it prevents the study from concluding. Name the next test. Use the last-sentence test on every paragraph.

### A6. Coverage without argument

Every side gets one balanced sentence; none is weighed. The literature review reads "A says, B says, C says".

**Repair:** synthesise. Group the sources by the position they take, then say what the grouping shows about the research question.

---

## B. Sentence patterns

### B1. Elaborate verb where "is" or "has" belongs

- "serves as", "stands as", "acts as", "functions as", "represents a"
- "boasts", "features", "offers" for "has"

Human prose uses "is" and "has" freely. The three published articles measured for this skill run at 17-26 instances of is / are / was / were per 1,000 words.

### B2. Nominalised density

Nouns built from verbs, stacked: "the implementation of the optimisation of resource allocation". LLMs use nominalisations at 1.5 to 2 times the human rate (Reinhart et al., 2025).

**Repair:** turn the noun back into its verb. "Have an effect on" becomes "affect"; "carry out a review of" becomes "review".

### B3. Contrast frames with nothing to correct

- "not only X but also Y"
- "not just / merely / simply X, but Y"
- "X, rather than Y" where nobody proposed Y
- "It is not X; it is Y"
- 2026 forms: "not simply X", "is more than a ...; it is ..." (see P2)

**Repair:** state the positive claim. Keep the frame where a real rival view is cited and answered.

### B4. Reflex triads

Three abstract items for rhythm: "efficient, scalable and robust"; "public health, the environment and sustainable development".

**Repair:** count the things. Debrah et al. (2021) study knowledge, awareness and attitudes, so three is right there.

### B5. Uniform rhythm

Every sentence between about 15 and 22 words, every paragraph four or five sentences. Reports from 2026 describe newer models moving to shorter sentences in a narrow 8-20 word band with more full stops (Wikipedia: Signs of AI writing).

Human reference, three published articles:

| Article | Mean words | Spread (cv) | 12 words or fewer | Over 35 words |
|---|---|---|---|---|
| Piketty & Qian (2009), economics | 25.9 | 0.59 | 26% | 26% |
| Debrah et al. (2021), environmental science | 22.5 | 0.46 | 16% | 12% |
| Rose (2020), political theory | 40.7 | 0.58 | 8% | 51% |

Sentence length differs by discipline. Variation is what the three share.

**Repair:** the length recipe in `SKILL.md`. Length follows content; do not vary it at random.

### B6. Stacked openers

"Moreover, ... Furthermore, ... Additionally, ... Consequently, ..." The connectives are correct English and academic style guides list them. The defect is one at the head of every sentence, most of them additive. Among 2026 models the habit is concentrated in Gemini (see P4).

**Repair:** given-new links. Place "however" after the subject where it reads better: "Rawls's position on this question, however, is limited to brief passages".

### B7. Staged reveals and one-line closers

- "The result? A ...", "Here is the key point:"
- A short quotable sentence closing each paragraph.

Listed in open-source pattern catalogues (see `evidence.md`). A short sentence is good when it carries a result. It is a tic when it carries a slogan.

---

## C. Vocabulary

Word lists date quickly. "Delve" was the best-known marker of 2023 and had largely dropped out of model output by 2025, and most of a model's phrase-level tells change with each version (see "What has weakened" above). Treat the lists as examples of a type: style words that add tone and no content. A word from C1 on its own is weak evidence of machine writing; it is listed because it rarely earns its place in academic prose.

Of the 379 excess style words Kobak et al. (2025) found in 2024 biomedical abstracts, 66% were verbs and 14% adjectives. Check verbs first.

### C1. Rarely justified in academic prose

delve, tapestry, testament, realm, landscape (abstract), showcase, underscore (figurative), boasts, vibrant, seamless, groundbreaking, transformative, revolutionise, game-changing, cutting-edge, unlock, embark, navigate (figurative), cornerstone, myriad, plethora, meticulous, commendable, invaluable, noteworthy, burgeoning, paramount, unravel, unveil

### C2. Legitimate words, a problem at density or as filler

crucial, pivotal, vital, key, comprehensive, nuanced, multifaceted, intricate, complex, foster, leverage, enhance, facilitate, harness, encompass, highlight, emphasise, elucidate, interplay, holistic, notably, importantly, additionally, potential, insights, align with, innovative, robust, significant

Two of these have technical meanings to protect. Reserve "significant" for statistical significance and "robust" for robustness checks.

### C3. Reported for 2026 models, not yet confirmed in academic corpora

- Wikipedia: Signs of AI writing, "mid-2026 and on": challenge, clearer, dependable, echoed, foster, leverage, matters, multifaceted, practical, prioritise, quietly, steady, universally
- Graphite (2026), evaluative adjectives in web articles: dependable, practical, meaningful (GPT-6 Astra); deliberate, steady, measured (Claude Opus 5); profound, immense, incredibly (Gemini 3.1 Pro)

"Dependable", "practical" and "steady" appear in both sources. Several of these words are ordinary in academic prose ("challenge", "practical", "measured"), so they count only at density and never in their technical sense.

### C4. The exception

Keep any of these words when it is the field's term or the source's term. "Foster" is the right verb when reporting Friedman's claim that growth fosters tolerance. Replacing it would misreport the source.

### C5. Plain replacements

| Inflated | Plain |
|---|---|
| utilise, leverage | use |
| facilitate | allow, help |
| demonstrate (non-experimental) | show |
| underscore, highlight | show, or state the fact |
| a wide range of | several, or the number |
| in order to (mid-sentence) | to |
| prior to | before |
| a growing body of research | name two or three studies |

---

## D. Phrases

**Openers:** "In today's ...", "In recent years, X has gained significant attention", "In the rapidly evolving field of", "It is important / worth noting that"

**Fillers:** "plays a ... role", "sheds light on", "paves the way for", "valuable insights", "a wide range of", "when it comes to"

**Closers:** "In conclusion,", "Overall,", "Ultimately,", "In summary," at the end of a body paragraph

**Not on this list:** standard reporting moves from the Manchester Academic Phrasebank. "This study investigates", "The results indicate", "These findings are consistent with" are how the genre works.

---

## E. Formatting carried over from chat

- Dash asides in pairs. This was a strong marker of models up to 2025 and is now mostly historical: the newest GPT, Claude and Gemini models use dashes less often than pre-2022 human writers (Graphite, 2026), while Rose (2020) uses them heavily. In a thesis, follow the field's house style; where there is none, prefer commas or parentheses.
- Bold on key terms in running prose
- Bullet lists where the genre expects paragraphs
- Title Case in Headings
- Leftover markdown symbols, curly and straight quotes mixed

---

## F. Not defects

Leave these alone. Wikipedia's editors list most of them as ineffective indicators, and detector research shows that formal and non-native writing is flagged for exactly these features.

- Formal or academic register
- Correct grammar and spelling
- Passive voice in methods
- Hedging as such
- One connective at the head of a sentence
- Long words and Academic Word List vocabulary
- Discipline terms repeated without variation

---

## G. Over-correction

Commercial humanizers lower detection scores by damaging the text: narrower vocabulary, more words, lower academic-word density (Karr et al., 2026). Expert readers still identify the result (Russell et al., 2025). Do none of the following.

- Insert errors, typos or awkward phrasing
- Add contractions, colloquialisms or rhetorical questions
- Break sentences into fragments for effect
- Rotate synonyms for a technical term
- Remove every hedge or every connective
- Trade one transition for another ("furthermore" to "moreover") and keep the stacking
- Replace dashes with commas mechanically, creating comma splices
- Vary sentence length at random, unrelated to content
- Swap a marker word for its nearest synonym ("delve into" to "dive into") and keep the empty sentence
- Rewrite "this matters" as "this is important". The flag is the fault, whatever its wording
