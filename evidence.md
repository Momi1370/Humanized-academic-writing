# Evidence Base

Researched 11 November 2026. Detector behaviour and model vocabulary both change within months, so recheck anything here that a decision depends on.

Confidence labels: **Primary** means the full text of the paper or vendor page was fetched and read during this research. **Secondary** means the figure came from a search summary and was not checked against the original; verify it before citing it in academic work.

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
| Per 10,000 words, human versus AI: flagged phrases 3 versus 30; dash asides 2 versus 17; triads 5 versus 19; "not just X but Y" 1 versus 3. Dash use differs by model family. | Pangram, "9 Signs of AI Writing" (2026) | Primary (vendor data, corpus not described) |
| Catalogue of content, grammar and style patterns. Reports that "delve" dropped sharply in 2025 and lists newer vocabulary and a shift to shorter sentences for 2026 models. Lists formal register, perfect grammar and isolated transition words as ineffective indicators. | Wikipedia: Signs of AI writing (WikiProject AI Cleanup) | Primary (community guide, not peer reviewed) |
| Overused words in scientific English are not explained by model architecture or training data alone; evidence for a human-feedback cause is mixed. | Juzek & Ward (2025), COLING; arXiv:2412.11385 | Secondary |
| Zero-shot detection improves when the variance and the token-to-token change of surprisal are used along with the mean. LLM text shows lower and more even surprisal. | Basani & Chen (2026), TMLR; arXiv:2509.18880 | Secondary |

---

## 3. Limits of detection in academic writing

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
3. Dense formal vocabulary raises flag rates. This is a reason to prefer plain verbs and concrete claims, which the course notes already teach as "writing tight".

---

## 4. Measurements from the course materials

Three published articles used in the Abstract Writing class were measured with a script. Body text only, references removed, text extracted from PDF. Sentence splitting on PDF text is imperfect, and three articles is a small sample, so read these as indicative.

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

## 5. Institutional rule that shapes the workflow

From the master's dissertation guidelines this skill was first written for (kept locally, not in this repository):

- AI may be used "for support ... but not as a co-author".
- A logbook is a mandatory appendix unless the supervisor exempts it. It records which tools were used and when, which prompts were entered and for what purpose, and how the student processed the output. The main text must refer to it at least once.
- A first improper use brings a written warning; a second brings a failing grade for the thesis process.
- At the defence, a mastery coefficient from 1 down to 0.4 applies when the student cannot explain parts of the thesis.

The skill's workflow ends with a logbook entry for this reason. Confirm the current version of the guidelines and any supervisor-specific agreement before relying on this summary.

---

## 6. What was not tested

- The skill was not tested against any commercial detector. No claim is made about scores.
- The rules were checked by running the script on six short AI-style passages and their revisions (see `examples.md`). They were not tested with a fresh model session on an unseen draft.
- The script's thresholds come from three articles. A different discipline may sit outside them legitimately.

---

## Sources

- Adam, G. A., et al. (2026). GPTZero: Robust detection of LLM-generated texts. https://arxiv.org/abs/2602.13042
- Basani, A., & Chen, P.-Y. (2026). Diversity boosts AI-generated text detection. https://arxiv.org/abs/2509.18880
- Dugan, L., et al. (2024). RAID: A shared benchmark for robust evaluation of machine-generated text detectors. https://arxiv.org/abs/2405.07940
- Emi, B., & Spero, M. (2024). Technical report on the Pangram AI-generated text classifier. https://arxiv.org/abs/2402.14873
- Juzek, T., & Ward, Z. (2025). Why does ChatGPT "delve" so much? https://arxiv.org/abs/2412.11385
- Karr, J. A., Khvatskii, G., Hua, T., & Chawla, N. V. (2026). Why AI detection fails for academic integrity. https://arxiv.org/abs/2608.11256
- Kobak, D., et al. (2025). Delving into LLM-assisted writing in biomedical publications through excess vocabulary. https://arxiv.org/abs/2406.07016
- Liang, W., et al. (2023). GPT detectors are biased against non-native English writers. https://arxiv.org/abs/2304.02819
- Pangram Labs (2026). 9 signs of AI writing, backed by data. https://www.pangram.com/signs-of-ai-writing
- Park, H., Jeong, G., & Kim, B. (2026). Style as a confound: False positives in AI detection of non-native academic writing. https://arxiv.org/abs/2608.26710
- Reinhart, A., et al. (2025). Do LLMs write like humans? Variation in grammatical and rhetorical styles. https://arxiv.org/abs/2410.16107
- Russell, J., Karpinska, M., & Iyyer, M. (2025). People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text. https://arxiv.org/abs/2501.15654
- Turnitin. AI writing detection guides. https://guides.turnitin.com
- Wikipedia. Signs of AI writing. https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Open-source pattern catalogues: https://github.com/blader/humanizer, https://github.com/egc365/signs-of-ai-writing, https://github.com/berenslab/llm-excess-vocab
