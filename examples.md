# Before and After

Six pairs for academic writing, one per section type. The other genres have one pair each in their files under `genres/`. The "before" passages are written in default LLM style. Every fact and citation in the "after" passages comes from three published articles, chosen to cover three disciplines. The skill does not need them; they are here so that every example can be checked against a real source.

- Piketty, T., & Qian, N. (2009). Income inequality and progressive income taxation in China and India, 1986-2015. *American Economic Journal: Applied Economics, 1*(2), 53-63.
- Debrah, J. K., Vidal, D. G., & Dinis, M. A. P. (2021). Raising awareness on solid waste management through formal education for sustainability. *Recycling, 6*(1), 6.
- Rose, J. L. (2020). On the value of economic growth. *Politics, Philosophy & Economics, 19*(2), 128-153.

Citations to other authors (Rawls, Friedman, Speth and so on) are taken from Rose (2020). In real work, read and cite the originals.

Measured with `scripts/style_check.py`, the six "before" passages together trip six flags and the six "after" passages none:

| Measure | Before | After | Human articles |
|---|---|---|---|
| Sentence-length variation (cv) | 0.28 | 0.52 | 0.46-0.59 |
| Sentences opening with a connective | 29% | 0% | 5-10% |
| Marker vocabulary per 1,000 words | 33.8 | 0 | 0-1.8 |
| Trailing -ing commentary per 1,000 words | 15.4 | 0 | 0.2-0.4 |
| Figures and dates per 1,000 words | 21.5 | 88.2 | 27-62 |

---

## 1. Introduction: opening context

**Before**

> In today's rapidly urbanising world, solid waste management has emerged as a pivotal challenge for developing countries. It plays a crucial role in safeguarding public health, protecting the environment, and fostering sustainable development. Moreover, the multifaceted nature of this issue underscores the need for comprehensive and holistic solutions, highlighting the importance of education in shaping environmentally responsible citizens.

**After**

> Waste collection tracks national income closely. Low-income countries collect less than 50% of the waste they generate, middle-income countries between 50% and 80%, and high-income countries more than 90% (Hoornweg and Bhada-Tata, as cited in Debrah et al., 2021). Most accounts attribute the shortfall to resource constraints and missing infrastructure. Debrah et al. (2021) ask instead whether the environmental knowledge, awareness and attitudes that teachers pass on through formal education change what students do with waste.

**What changed**

- "In today's ... world" and "has emerged as a pivotal challenge" assert importance. The collection rates show it.
- The triad "public health, the environment and sustainable development" was decoration. The triad "knowledge, awareness and attitudes" stays because the review studies those three constructs.
- "Moreover" and the "highlighting" tail are gone. The link to the last sentence is the contrast between the usual explanation and the authors' question.
- The opening sentence is six words and states the claim the figures then support.

---

## 2. Literature review: synthesis

**Before**

> The debate over economic growth has garnered significant attention in recent years. Many scholars argue that growth is essential for society. Furthermore, critics have highlighted the environmental costs of growth. Additionally, some researchers suggest that growth fosters positive social attitudes. Rawls also discusses this topic, offering valuable insights into the relationship between justice and growth.

**After**

> Whether an affluent society must keep pursuing growth divides the literature along a clear line. Defenders hold that further growth remains valuable even at high levels of income and wealth (Baumol et al., 2007; Friedman, 2005; Tomasi, 2012). Critics reject the aim itself, asking why a society that has reached a high material standard of living should not 'declare victory on the economic growth front' (Speth, 2005, p. 192). Rawls rejects it too, but only in passing: his dismissal of growth that goes on 'indefinitely, upwards and onwards' is confined to brief passages and footnotes (Rawls, 1999b, p. 107). Rose (2020) starts from this gap. She grants the defenders' premises and argues that a society may still justly stop aiming for growth.

**What changed**

- "Many scholars", "critics" and "some researchers" became named sources grouped by position. This is the standard rule for a literature review: synthesise, do not list.
- "Furthermore" and "Additionally" are gone. Each sentence opens with the party it concerns (Defenders, Critics, Rawls, Rose), so the structure of the debate does the linking.
- "Offering valuable insights" said nothing about Rawls. The replacement says what he claimed and why it leaves a gap.
- A six-word sentence marks the turn from the existing debate to the paper's contribution.

---

## 3. Results: reporting

**Before**

> The results reveal a striking divergence between the two countries, underscoring the transformative impact of tax policy design. China's income tax system has experienced remarkable growth, showcasing the power of fiscal reform. In contrast, India's system has remained relatively stagnant, highlighting the challenges of constant adjustment.

**After**

> The share of the Chinese population subject to income tax rose from less than 0.1% in 1986 to about 20% in 2008. In India it stayed at around 2-3%. Revenues followed the same pattern. Chinese income tax receipts grew from less than 0.1% of GDP in 1986 to 2.5% in 2008, whereas Indian receipts remained at about 0.5% (Piketty & Qian, 2009).

**What changed**

- Three -ing tails carried the interpretation ("transformative impact", "power of fiscal reform"). By convention, interpretation stays out of the results section, so they are removed here and the reasoning moves to the discussion.
- "Striking", "remarkable" and "relatively stagnant" became the numbers they stood for.
- Simple past for the data, as the tense convention in `genres/academic.md` requires.

---

## 4. Discussion: hedging and limits

**Before**

> It is important to note that these findings should be interpreted with caution. While the projections are promising, various factors may potentially influence the outcomes. Nevertheless, the results not only demonstrate the potential of income taxation but also pave the way for future research in this evolving field.

**After**

> The projection that Chinese income tax revenues could exceed 5% of GDP by 2015 assumes constant trends in both income levels and tax schedules over 2004-2015 (Piketty & Qian, 2009). The second half of that assumption is the weaker one. An upward revision of the exemption threshold would probably remove many new taxpayers at once, which is how India has kept its taxpaying population near 2-3%. The 5% figure is therefore better read as what unchanged law would yield than as a forecast.

**What changed**

- "Interpreted with caution" and "various factors" are hedges with no object. The replacement names the assumption the projection depends on and says which part is doubtful.
- "May potentially" stacked two hedges on nothing. "Would probably" is one hedge on one stated mechanism.
- "Not only ... but also" and "pave the way" are gone. The paragraph ends on the writer's own reading of the figure.
- The third and fourth sentences are the writer's interpretation. A model cannot supply that part; the writer must hold the view and be able to defend it.

---

## 5. Conclusion: limitations and further research

**Before**

> Despite these challenges, environmental education continues to play a vital role in promoting sustainability. Future research should explore innovative approaches to further enhance its effectiveness. Ultimately, a collaborative effort among stakeholders will be essential to unlocking the full potential of education for sustainable development.

**After**

> One finding sets the agenda for further work. Students' knowledge and attitudes ran ahead of their practice: awareness was high, yet participation in waste management was not (Debrah et al., 2021). Whether practical instruction or incentives close that gap remains untested. A fair test would use one standardised instrument across sites, because the studies reviewed here were conducted by different authors, in different places and at different times, and their results may not generalise.

**What changed**

- The "Despite these challenges ... Future research should explore ... Ultimately" sequence fits any paper on any subject. The replacement names the specific gap, the specific next test and the specific limitation.
- The limitation is tied to its consequence: results "may not generalise" because the underlying studies differ in author, place and time.

---

## 6. Methods: rhythm

**Before** (four sentences of 20, 18, 19 and 17 words)

> The Chinese data used in the study were obtained from urban household income surveys conducted by the National Statistical Bureau. These surveys were designed to be representative of the urban population of China during the period under study. The sample size ranged between 13,000 and 17,000 households in each year until the survey was expanded in 2002. The sample subsequently increased to between 45,000 and 50,000 households in the years 2002 and 2003 respectively.

**After** (the authors' own text, quoted from Piketty & Qian, 2009, p. 54; sentences of 18, 10, 11, 10 and 33 words)

> "The Chinese data used in this paper comes from the urban household income surveys collected by China's NSB. These surveys are designed to be representative of urban China. Between 13,000 and 17,000 households were surveyed each year until 2002. The sample rose to 45,000-50,000 households in 2002 and 2003. The individual level data from these surveys are not available for all years, and we asked the NSB to provide us with annual tabulations (for the period of 1986-2003) based on the micro-files."

**What to notice**

- The first version pads each fact to the same length ("during the period under study", "respectively"). The published version lets a simple fact take ten words and a constraint with its workaround take thirty-three.
- Nothing in the published version is ornamental. It is not trying to vary its rhythm. The variation comes from the facts being of different sizes.
