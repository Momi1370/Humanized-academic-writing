# Pattern Catalogue

Each entry gives the pattern, why it counts, and the repair. Sources are listed in `evidence.md`.

No single pattern shows that a text was machine-written. Humans produced all of them before 2022. What marks LLM prose is several at once, at high density, attached to sentences that say nothing specific.

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

**Not the same thing:** a fronted participial clause whose subject is the main-clause subject ("Using annual tabulations from urban household surveys, we compute...") is standard and taught in the course notes.

### A5. Formula endings

- "Despite these challenges, X continues to..."
- "Future research should explore innovative approaches to..."
- "Ultimately, a collaborative effort among stakeholders..."
- Paragraphs that close by restating their topic sentence.

**Repair:** name the actual limitation and what it prevents the study from concluding. Name the next test. Use the last-sentence test on every paragraph.

### A6. Coverage without argument

Every side gets one balanced sentence; none is weighed. The literature review reads "A says, B says, C says".

**Repair:** the course rule. Synthesise: group the sources by the position they take, then say what the grouping shows about the research question.

---

## B. Sentence patterns

### B1. Elaborate verb where "is" or "has" belongs

- "serves as", "stands as", "acts as", "functions as", "represents a"
- "boasts", "features", "offers" for "has"

Human prose uses "is" and "has" freely. The three human articles measured for this skill run at 17-26 instances of is / are / was / were per 1,000 words.

### B2. Nominalised density

Nouns built from verbs, stacked: "the implementation of the optimisation of resource allocation". LLMs use nominalisations at 1.5 to 2 times the human rate (Reinhart et al., 2025). The course notes call the repair "writing tight": "have an effect on" becomes "affect".

### B3. Contrast frames with nothing to correct

- "not only X but also Y"
- "not just / merely / simply X, but Y"
- "X, rather than Y" where nobody proposed Y
- "It is not X; it is Y"

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

"Moreover, ... Furthermore, ... Additionally, ... Consequently, ..." The connectives are correct English and the course lists them. The defect is one at the head of every sentence, most of them additive.

**Repair:** given-new links. Place "however" after the subject where it reads better: "Rawls's position on this question, however, is limited to brief passages".

### B7. Staged reveals and one-line closers

- "The result? A ...", "Here is the key point:"
- A short quotable sentence closing each paragraph.

Listed in open-source pattern catalogues (see `evidence.md`). A short sentence is good when it carries a result. It is a tic when it carries a slogan.

---

## C. Vocabulary

Word lists date quickly. "Delve" was the best-known marker of 2023 and had largely dropped out of model output by 2025. Treat the lists as examples of a type: style words that add tone and no content.

Of the 379 excess style words Kobak et al. (2025) found in 2024 biomedical abstracts, 66% were verbs and 14% adjectives. Check verbs first.

### C1. Rarely justified in academic prose

delve, tapestry, testament, realm, landscape (abstract), showcase, underscore (figurative), boasts, vibrant, seamless, groundbreaking, transformative, revolutionise, game-changing, cutting-edge, unlock, embark, navigate (figurative), cornerstone, myriad, plethora, meticulous, commendable, invaluable, noteworthy, burgeoning, paramount, unravel, unveil

### C2. Legitimate words, a problem at density or as filler

crucial, pivotal, vital, key, comprehensive, nuanced, multifaceted, intricate, complex, foster, leverage, enhance, facilitate, harness, encompass, highlight, emphasise, elucidate, interplay, holistic, notably, importantly, additionally, potential, insights, align with, innovative, robust, significant

Two of these have technical meanings to protect. Reserve "significant" for statistical significance and "robust" for robustness checks.

### C3. Reported for 2026 models, not yet confirmed in academic corpora

challenge, clearer, dependable, leverage, matters, multifaceted, practical, prioritise, quietly, steady (Wikipedia: Signs of AI writing, 2026 section)

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

The course rules already list several (section 9.4 of `academic-writing-rules.md`).

**Not on this list:** standard reporting moves from the Manchester Academic Phrasebank. "This study investigates", "The results indicate", "These findings are consistent with" are how the genre works.

---

## E. Formatting carried over from chat

- Dash asides in pairs. LLMs use them at about ten times the human rate overall (Pangram, 2026), but Rose (2020) uses them heavily too. In a thesis, prefer commas or parentheses unless the supervisor's field uses dashes.
- Bold on key terms in running prose
- Bullet lists where the course expects paragraphs
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
- Replace dashes with commas mechanically, creating comma splices
- Vary sentence length at random, unrelated to content
- Swap a marker word for its nearest synonym ("delve into" to "dive into") and keep the empty sentence
