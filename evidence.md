# Evidence Base

Researched 11 November 2026; sections 3 and 7 added 12 November 2026. Detector behaviour and model vocabulary both change within months, so recheck anything here that a decision depends on.

Confidence labels: **Primary** means the full text of the paper or page was fetched and read during this research. **Secondary** means the figure came from a search summary and was not checked against the original; verify it before citing it in academic work.

---

## 1. How current detectors work

| Detector | Method | Source | Confidence |
|---|---|---|---|
| GPTZero | Supervised deep-learning classifier since 2023. Three top-level classes (Human, AI, Mixed), with "AI-polished" and "AI-paraphrased" as sub-classes. Trained against paraphrasers and humanizer services. The 2026 report does not mention burstiness and uses perplexity methods only as baselines. | Adam et al. (2026), arXiv:2602.13042 | Primary (vendor report) |
| Pangram | Supervised classifier trained with "synthetic mirrors": an AI text generated on the topic of each human document, with mislabelled cases mined and retrained. States that its published list of tells "are not inputs to our model". | Emi & Spero (2024), arXiv:2402.14873; pangram.com/signs-of-ai-writing | Primary for the signs page, secondary for the reports |
| Turnitin | Suppresses scores from 1% to 19% because false positives are more common there. Separate category for AI text altered by a paraphrasing tool (English only). States the score is one data point and not proof. | Turnitin guides | Secondary |
| Originality.ai | Trained classifier, architecture undisclosed. Independent false-positive measurements (about 5%) exceed the marketed rate. | Aggregated reviews | Secondary |
| Binoculars, Fast-DetectGPT, GLTR, DivEye | Open zero-shot methods built on token probability: perplexity ratios, probability curvature, surprisal variance. | Dugan et al. (2024); Basani & Chen (2026) | Secondary |

**Implication.** Perplexity and burstiness explain the older open tools. The commercial tools a university is likely to use are classifiers trained on large paired corpora, including humanized text. No published list of features determines their output.

---

## 2. What distinguishes LLM prose from human prose

| Finding | Source | Confidence |
|---|---|---|
| In 15.1 million PubMed abstracts, at least 13.5% of 2024 abstracts show LLM processing, up to about 40% in some subcorpora. Of 379 excess style words in 2024, 66% were verbs and 14% adjectives. "Delves" appeared at 28 times its expected frequency, "underscores" at 13.8, "showcasing" at 10.7. | Kobak et al. (2025), *Science Advances* 11(27); arXiv:2406.07016 | Primary |
| Instruction-tuned models use present-participle clauses at 2 to 5 times the human rate and nominalisations at 1.5 to 2 times, giving a dense, noun-heavy style. | Reinhart et al. (2025), *PNAS* 122(8); arXiv:2410.16107 | Secondary |
| Five annotators who use LLMs often misclassified 1 of 300 articles by majority vote and outperformed most automatic detectors, including on paraphrased and humanized text. They relied on vocabulary and also on structure, originality and clarity. | Russell, Karpinska & Iyyer (2025), ACL; arXiv:2501.15654 | Secondary |
| Per 10,000 words, human versus AI: flagged phrases 3 versus 30; dash asides 2 versus 17; triads 5 versus 19; "not just X but Y" 1 versus 3. Dash use differs by model family. The model versions behind these figures are not stated; for dash use in the newest models see section 3. | Pangram, "9 Signs of AI Writing" (2026) | Primary (vendor data, corpus not described) |
| Catalogue of content, grammar and style patterns. Reports that "delve" dropped sharply in 2025 and lists newer vocabulary and a shift to shorter sentences for 2026 models. Lists formal register, perfect grammar and isolated transition words as ineffective indicators. See section 3 for the October 2026 version. | Wikipedia: Signs of AI writing (WikiProject AI Cleanup) | Primary (community guide, not peer reviewed) |
| Overused words in scientific English are not explained by model architecture or training data alone; evidence for a human-feedback cause is mixed. | Juzek & Ward (2025), COLING; arXiv:2412.11385 | Secondary |
| Zero-shot detection improves when the variance and the token-to-token change of surprisal are used along with the mean. LLM text shows lower and more even surprisal. | Basani & Chen (2026), TMLR; arXiv:2509.18880 | Secondary |

---

## 3. Update, November 2026: patterns in current models

Three sources were used. All three describe what model prose looks like. None of them tests whether removing a pattern changes a detector's output, and nothing here supports such a claim.

| Source | What it is | What it supports here | Confidence |
|---|---|---|---|
| Graphite, AI Tells (16 September 2026), Opus 5.5 Update (1 October 2026), Gemini 4 Argon (21 October 2026); Druck, Paredes & Smith | 10,000 pre-ChatGPT web articles from Common Crawl, each matched with an article on the same topic from every model tested (nine models, later eleven). A "tell" is a word, phrase or frame used at least twice as often as in the human articles. 12,877 tells in the first study. | Importance flagging, corrective framing, Gemini's transitions, modifiers and idioms, mannered-prose scores, falling dash rates, turnover of tells between versions | Primary: all three pages read in full on 12 November 2026. Company research report, not peer reviewed. |
| Wikipedia: Signs of AI writing, version current in November 2026 (page text dated "As of October 2026") | Editors' catalogue from WikiProject AI Cleanup. An advice page, "descriptive, not prescriptive". | Significance wording, negative parallelism, sentence-final "-ing" commentary, the dating of vocabulary by model generation, the list of ineffective indicators | Primary: page read in full on 12 November 2026. Community observation, with no corpus or counts. |
| Kobak et al. (2025), *Science Advances* | Excess-vocabulary analysis of 15.1 million PubMed abstracts, 2010-2024 | The first-generation vocabulary and the weight on verbs. Its data end in 2024, so it documents those words at their peak and says nothing about their decline. | Primary: read for the first version of this file, not re-read for this update. Peer reviewed. |

**Findings used in `patterns.md`**

| Finding | Source |
|---|---|
| Between 55% and 72% of tells are unique to one version of a model family, and 65% are unique to one family. | Graphite, AI Tells |
| Importance flagging: "matters because" at 357 times the human rate in GPT-6 Astra and 132 times in Claude Opus 5; "this matters" at 116 times and "why _ matters" at 92 times in Claude Opus 5.5. Gemini 3.1 Pro flags importance with "absolutely essential" (32 times) and "remarkably" (19 times). | Graphite, AI Tells; Opus 5.5 Update |
| Corrective framing: "not simply" 157 times (Astra); "rather than merely" 160 times and "rather than simply" 43 times (Opus 5); "is more than a _ it" 98 times (Opus 5.5); "is not just a _ it is" 153 times (Gemini 3.1 Pro). Astra frames by correction about 12 times as often as human writers. | Graphite, AI Tells; Opus 5.5 Update |
| "Y rather than X" is "particularly common in recent LLM output". Significance wording to watch: "stands/serves as", "is a testament", "a crucial/pivotal role", "underscores its importance". The page marks these significance examples as outdated for current models. | Wikipedia |
| Sentence-final "-ing" phrases carry superficial analysis: highlighting, underscoring, emphasizing, ensuring, reflecting, contributing to, fostering. | Wikipedia; rate from Reinhart et al. (2025) |
| "Furthermore" appears in 45% of Gemini 4 Argon's articles (24 times the human rate), in none of Astra's and in one of Opus 5.5's. "Conversely" 14 times, "additionally" 3.2 times. | Graphite, Gemini 4 Argon |
| Gemini 4 Argon against human writing: drastically 12 times, unmatched 6.5, fantastic 4.2, incredible 2.6; bridges the gap 70, fast-paced world 51, half the battle 37, heavy lifting 15, crystal clear 10, gold standard 10. | Graphite, Gemini 4 Argon |
| Mannered-prose score, 0-100, judged by Claude Opus 5 on 1,000 topics: human 6.65, GPT-6 Astra 7.91, Claude Opus 5.5 10.57, Gemini 4 Argon 19.48. | Graphite, Gemini 4 Argon |
| Dashes against the pre-2022 human rate: Astra 88% lower, Opus 5.5 more than 99% lower, Argon 38% lower. Average strength of 11 well-known tells fell 21-50% across model families. | Graphite, all three |
| Delve, tapestry, testament and vibrant belong to models of 2023 to mid-2024; "delve" "dropped off sharply in 2025". Some newer models avoid dashes entirely, which the editors now treat as a sign of its own. | Wikipedia |
| Ineffective indicators: perfect grammar, formal or academic prose, bland prose, transition words in isolation. | Wikipedia |

**Confidence notes**

1. **Genre.** Graphite's corpus is web articles written to one fixed prompt in a "professional yet friendly tone". The ratios do not transfer to academic prose, and the idioms in particular are unlikely in a thesis from any author. No study found here measures these 2026 patterns in an academic corpus.
2. **Ratios.** A large ratio can come from a near-zero human baseline; Graphite states this itself. The human articles predate ChatGPT, so some differences may reflect change in writing style over time.
3. **Source type.** Graphite is a commercial company, and its studies are not peer reviewed. Its mannered-prose scores are a model's judgments, as the page notes. Graphite and Wikipedia both advise against deciding authorship from individual tells.
4. **Transitions are a Gemini finding.** Dense formal transitions are often described as a habit of all models. The sources do not support that for 2026 models: GPT-6 Astra and Claude Opus 5.5 almost never write "furthermore". `patterns.md` files the pattern under Gemini for that reason.
5. **Older wording.** "Played a crucial role", "stands as a testament" and "underscores" come from Wikipedia's list, which marks its significance examples as outdated. Graphite did not list them. The move persists under newer wording ("this matters", "matters because"), which both sources record.
6. **Participial tails.** Graphite did not measure them. Their place among the 2026 patterns rests on Wikipedia's catalogue and on Reinhart et al. (2025), which studied earlier models.
7. **Shelf life.** Given the turnover between versions, expect the phrase lists to be out of date within a model generation. The moves are more durable: importance flagging, corrective framing and participial commentary appear both in the earlier catalogues and in the 2026 material.

---

## 4. Limits of detection in academic writing

| Finding | Source | Confidence |
|---|---|---|
| On non-native academic manuscripts written 2018-2022, false-positive rates were 99.8-100% for four token-statistic detectors, 93.1% for a RoBERTa classifier, 88.3% for RADAR, 25.2% for Fast-DetectGPT and 0.0% for Binoculars. Professional human editing moved statistical detectors further towards "AI". | Park, Jeong & Kim (2026), arXiv:2608.26710 | Primary (partly from a summary of later sections) |
| Seven detectors flagged an average of 61% of 91 TOEFL essays as AI-written. Flagged essays had lower perplexity. | Liang et al. (2023), *Patterns*; arXiv:2304.02819 | Secondary |
| On published abstracts, Pangram and GPTZero flagged 0% of 2013-2015 originals and 14.9% and 8.9% of 2023-2025 originals. The later figures are flag rates, since undisclosed AI use cannot be excluded. Flagging correlated with Academic Word List density and long-word ratio and was higher in political science and theology than in chemistry. | Karr et al. (2026), arXiv:2608.11256 | Primary |
| A light LLM polish of a human abstract was flagged 64-80% of the time by Pangram and 38-49% by GPTZero. | Karr et al. (2026) | Primary |
| After a commercial humanizer, over 96% of AI rewrites went undetected by both tools. The humanizer lowered long-word ratio, academic-word ratio and type-token ratio and added words. | Karr et al. (2026) | Primary |
| GPTZero reports 93.5% recall on its own set of paraphrased and humanized texts. | Adam et al. (2026) | Primary (vendor claim; conflicts with Karr et al.) |
| Detectors generalise poorly to unseen models and domains and weaken under paraphrase attacks. | Dugan et al. (2024), RAID, ACL; arXiv:2405.07940 | Secondary |

**Open disagreement.** Vendor reports claim strong robustness to humanizers. The one independent test found here (Karr et al.) shows the opposite for one humanizer. Neither settles the question.

**What follows for a thesis writer.**

1. A detector score is weak evidence in both directions. A supervisor has two stronger ones: the logbook and the oral defence.
2. Asking a model to "polish" finished human text is the riskiest use. It adds little and is flagged often. Asking a model for critique and then revising by hand leaves the text the writer's own.
3. Dense formal vocabulary raises flag rates. Plain verbs and concrete claims are better academic writing in any case, and that is the reason this skill prefers them.

---

## 5. Measurements from three published articles

Three published articles, one each from economics, environmental science and political theory, were measured with a script. Full references are in `examples.md`. Body text only, references removed, text extracted from PDF. Sentence splitting on PDF text is imperfect, and three articles is a small sample, so read these as indicative.

| Measure | Piketty & Qian (2009) | Debrah et al. (2021) | Rose (2020) |
|---|---|---|---|
| Sentences measured | 120 | 406 | 280 |
| Mean sentence length (words) | 25.9 | 22.5 | 40.7 |
| Variation (sd / mean) | 0.59 | 0.46 | 0.58 |
| Sentences of 12 words or fewer | 26% | 16% | 8% |
| Sentences over 35 words | 26% | 12% | 51% |
| Mean difference between adjacent sentences (words) | 15.9 | 10.2 | 22.5 |
| Sentences opening with a connective (script list) | 7% | 10% | 5% |
| "Furthermore" + "additionally" per 10,000 words | 0 | 1.1 | 0 |
| "However" per 10,000 words | 9.7 | 16.4 | 3.5 |
| Marker vocabulary per 1,000 words | 0.0 | 0.2 | 1.8 |
| Figures and dates per 1,000 words | 61.9 | 26.7 | 42.6 |
| is / are / was / were per 1,000 words | 21.3 | 26.3 | 16.7 |
| Dash asides per 1,000 words | 0.0 | 0.2 | 4.3 |

Observations used in the skill:

- Variation is similar across three disciplines even though mean length nearly doubles.
- Cohesion comes mostly from repeated terms and demonstratives. Connectives open about one sentence in ten to twenty.
- Marker words appear in human text when they carry content. Rose's 1.8 per 1,000 is almost entirely "foster", the verb of the argument she examines.
- Debrah et al. (2021), written before ChatGPT by non-native authors, contains "multifaceted", "plays a vital role" and several trailing -ing clauses. This is the kind of text the false-positive studies describe.
- Rose (2020) uses dash asides at a rate above Pangram's AI average. Dash use reflects discipline and house style.

---

## 6. Institutional rules and the logbook step

Rules on AI use differ between institutions, programmes and supervisors. Read your own before using this skill on assessed work. The skill does not depend on any particular rule.

The logbook step in the workflow follows one common model, taken from the master's dissertation guidelines the skill was first written for. They are summarised here as an example only:

- AI may be used "for support ... but not as a co-author".
- A logbook is a mandatory appendix unless the supervisor exempts it. It records which tools were used and when, which prompts were entered and for what purpose, and how the student processed the output.
- Improper use is sanctioned, and at the oral defence the grade is reduced when the student cannot explain parts of the thesis.

Where no record is required, the logbook step is optional. Keeping one is still cheap protection if a detector score is ever questioned.

---

## 7. Sources for the positive structures

`structures.md` rests on open teaching material from university writing centres. These sources describe conventions of academic prose. They are not studies of AI text, and nothing in them concerns detection.

| Structure | Source | What it supplies | Confidence |
|---|---|---|---|
| Claim, evidence, interpretation | UNC Writing Center, "Paragraphs" | Five-step paragraph development (controlling idea, elaboration, example, explanation of the example, completion or transition); the example and explanation steps repeat; length does not define a paragraph | Primary |
| Given-new flow | Duke Graduate School Scientific Writing Resource, Lesson 2 | New information last; passive voice to move old information forward; first and last sentences of a paragraph match | Primary |
| Given-new flow | Gopen & Swan (1990), *American Scientist* | The original statement of topic and stress positions | Secondary: the page did not load during this research, so it is cited as background only |
| Hedging | Manchester Academic Phrasebank, "Being cautious" | Hedging phrases grouped by task | Primary |
| Hedging | George Mason University Writing Center, "Hedges" | Devices by word class; boosters are less common in academic writing | Primary |
| Concrete subjects and verbs | Duke Scientific Writing Resource, Lesson 1 | Actions in verbs, characters in subjects, subjects near verbs; nominalisations defined and their legitimate uses | Primary |
| Length from content | Purdue OWL, "Strategies for Variation" | Long sentences carry more information and short ones emphasise a point; also recommends alternating lengths for rhythm | Primary |

**Notes**

1. Three rules in the hedging section are this skill's own and are not stated by the two hedging sources: the table matching wording to strength of evidence, one hedge per claim, and a stated reason for each hedge. They are consistent with the sources and go beyond them.
2. The skill departs from Purdue OWL on one point. The OWL advises alternating short and long sentences for rhythm. The skill assigns length by content, because alternation by rule is one of the patterns it removes.
3. The section-by-section table and the build order in `structures.md` are a synthesis of standard conventions and have no single source.
4. The UNC handout is licensed CC BY-NC-ND 4.0. It is summarised and linked, not reproduced.

---

## 8. What was not tested

- The skill was not tested against any commercial detector. No claim is made about scores.
- The rules were checked by running the script on six short AI-style passages and their revisions (see `examples.md`). They were not tested with a fresh model session on an unseen draft.
- The positive structures follow established teaching conventions. Their effect on drafts produced with this skill was not measured.
- The script's thresholds come from three articles. A different discipline may sit outside them legitimately.
- The 2026 patterns in section 3 were measured on web articles. Their rates in academic prose are unknown.

---

## Sources

- Adam, G. A., et al. (2026). GPTZero: Robust detection of LLM-generated texts. https://arxiv.org/abs/2602.13042
- Basani, A., & Chen, P.-Y. (2026). Diversity boosts AI-generated text detection. https://arxiv.org/abs/2509.18880
- Dugan, L., et al. (2024). RAID: A shared benchmark for robust evaluation of machine-generated text detectors. https://arxiv.org/abs/2405.07940
- Duke Graduate School. Scientific Writing Resource, Lessons 1 and 2. https://sites.duke.edu/scientificwriting/
- Druck, G., Paredes, J. L., & Smith, E. (2026a). AI tells. Graphite. https://graphite.io/research/ai-tells
- Druck, G., Paredes, J. L., & Smith, E. (2026b). AI tells: Opus 5.5 update. Graphite. https://graphite.io/research/ai-tells-opus-5-5-update
- Druck, G., Paredes, J. L., & Smith, E. (2026c). AI tells: Gemini 4 Argon. Graphite. https://graphite.io/research/ai-tells-gemini-4-argon-update
- Emi, B., & Spero, M. (2024). Technical report on the Pangram AI-generated text classifier. https://arxiv.org/abs/2402.14873
- George Mason University Writing Center. Hedges: Softening claims in academic writing. https://writingcenter.gmu.edu/guides/hedges-softening-claims-in-academic-writing
- Gopen, G. D., & Swan, J. A. (1990). The science of scientific writing. *American Scientist, 78*, 550-558. https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing
- Juzek, T., & Ward, Z. (2025). Why does ChatGPT "delve" so much? https://arxiv.org/abs/2412.11385
- Karr, J. A., Khvatskii, G., Hua, T., & Chawla, N. V. (2026). Why AI detection fails for academic integrity. https://arxiv.org/abs/2608.11256
- Kobak, D., et al. (2025). Delving into LLM-assisted writing in biomedical publications through excess vocabulary. https://arxiv.org/abs/2406.07016
- Liang, W., et al. (2023). GPT detectors are biased against non-native English writers. https://arxiv.org/abs/2304.02819
- Pangram Labs (2026). 9 signs of AI writing, backed by data. https://www.pangram.com/signs-of-ai-writing
- Park, H., Jeong, G., & Kim, B. (2026). Style as a confound: False positives in AI detection of non-native academic writing. https://arxiv.org/abs/2608.26710
- Purdue Online Writing Lab. Strategies for variation. https://owl.purdue.edu/owl/general_writing/academic_writing/sentence_variety/index.html
- Reinhart, A., et al. (2025). Do LLMs write like humans? Variation in grammatical and rhetorical styles. https://arxiv.org/abs/2410.16107
- Russell, J., Karpinska, M., & Iyyer, M. (2025). People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text. https://arxiv.org/abs/2501.15654
- The Writing Center, University of North Carolina at Chapel Hill. Paragraphs. https://writingcenter.unc.edu/tips-and-tools/paragraphs/
- Turnitin. AI writing detection guides. https://guides.turnitin.com
- University of Manchester. Academic Phrasebank: Being cautious. https://www.phrasebank.manchester.ac.uk/using-cautious-language/
- Wikipedia. Signs of AI writing. https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Open-source pattern catalogues: https://github.com/blader/humanizer, https://github.com/egc365/signs-of-ai-writing, https://github.com/berenslab/llm-excess-vocab
