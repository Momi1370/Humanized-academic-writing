# Proposals

Research proposals, grant applications and project proposals. A reviewer scores the text against stated criteria, often with many other applications on the desk. The proposal has to answer the reviewer's questions in the order and the space the call allows.

## Ask first

- Where is the call, template or set of instructions? Read it before anything else. Its sections, criteria, word and page limits, and formatting rules override every default in this file. Reviewers may stop reading at the first departure from the instructions.
- Who decides, and on which criteria? Ask for the scoring grid if there is one.
- What will be done, why, how, by when and with what resources? The writer supplies all five.
- What exists already: a pilot, preliminary data, earlier work by the team, a supervisor's agreement?
- For a thesis proposal: the problem statement, the research question and the intended research strategy.

If the call is not available, say that the result follows general conventions and must be checked against the call before submission.

## Structure to build on

A proposal answers five questions. Each section of the template usually maps to one of them.

| Question | What the reviewer needs | Common section names |
|---|---|---|
| What will be done? | The aim in one or two sentences, with boundaries: which population, place, period, system | Summary, aims, objectives |
| Why is it needed? | The problem shown with evidence (a figure, a source), and what is missing in existing work | Background, problem statement, state of the art |
| How will it be done? | Steps a competent reader could picture: design, data, method, who does what | Method, work plan, approach |
| How will success be known? | A measure for each aim, and what result would count against the idea | Evaluation, expected outcomes, milestones |
| Can this team do it with this budget and time? | Evidence of feasibility: preliminary results, skills, access, a timeline, each cost tied to a task | Feasibility, timeline, budget justification, qualifications |

Rules:

- **The aim is checkable.** A reader should be able to tell, at the end of the project, whether the aim was met. "Improve customer experience" fails. "Test whether SMS reminders reduce missed appointments at one outpatient clinic" passes.
- **Need is shown.** The claim, evidence and interpretation paragraph from `genres/academic.md` applies to the background section, including its citation rules.
- **Novelty is a comparison.** Name the closest existing work and state what it did not do. The word "novel" adds nothing to that sentence.
- **Benefit has a beneficiary and a measure.** Who gains, how much, and how it will be observed.
- **Feasibility is evidence.** A pilot result, access already granted, a method the team has used before. Preliminary work shows that the applicant can run the study and has met its first problems.
- **Each budget line has a task.** A cost that no step of the method needs raises a question.
- **Future tense for the plan, present for the argument, past for work already done.** "We will randomise ..."; "the gap is ..."; "the pilot recruited ...".
- **Hedge with a reason.** A risk section that names a real risk and its mitigation is stronger than one that reports no risks.
- **Mirror the call.** Use the call's own section headings and criterion words, in its order, so the reviewer can find each answer.

## The avoid list in a proposal

| Move | Typical form | Repair |
|---|---|---|
| Praise without evidence | "innovative", "novel", "cutting-edge", "state-of-the-art", "world-class team", "unique opportunity" | The comparison that shows it: what the closest work did and did not do; what the team has delivered before. |
| Importance flag | "addresses a critical gap", "is of paramount importance", "timely and relevant" | Name the gap and the evidence that it is one. |
| Unmeasured benefit | "will have significant impact on stakeholders", "will transform practice" | Who benefits, by how much, measured how. |
| Emphatic modifiers and idioms | "drastically improve", "bridge the gap between research and practice", "holistic approach" | The size of the expected change and the mechanism. |
| Nominalised density | "the facilitation of the implementation of an optimisation framework" | Verbs with actors: "we will test", "the clinic will send". |
| Attribution to nobody | "It is widely recognised that ...", "Recent studies show ..." | Author and year, or cut. |
| Reflex triads | "efficient, scalable and sustainable" | Keep the properties the method section actually delivers. |
| Formula ending | "In conclusion, this project has the potential to make a lasting contribution ..." | End the section on its last fact. If the template requires a conclusion, restate the aim and the measure. |
| Corrective frame | "more than just a study", "not merely a tool but a paradigm" | State what it is. |

**Not defects here.** Formal register, section headings and numbered aims, the call's own terminology repeated exactly, tables for timelines and budgets, and a summary that repeats the aim (the template asks for it).

## Example

The project and its figures are invented for illustration. In real work every detail comes from the writer.

**Before**

> This innovative project will leverage cutting-edge digital tools to transform patient engagement, addressing a critical gap in healthcare delivery. By fostering a holistic approach, it will drastically reduce missed appointments, delivering significant impact for patients, clinicians and other stakeholders, and paving the way for future research in this rapidly evolving field.

**After**

> The project tests whether SMS reminders reduce missed appointments at the outpatient clinic of one regional hospital. In 2025 the clinic recorded 1,840 missed appointments, 14% of all bookings. We will randomise 2,000 patients to a reminder two days before the appointment or to no reminder, over six months, and compare the share of missed appointments in the two groups. A four-week pilot with 150 patients has confirmed that the hospital's existing SMS gateway can send the messages. The study needs one research assistant at half time for eight months and no new equipment.

**What changed**

- "Innovative", "cutting-edge" and "transform" became the intervention and the place.
- "A critical gap" became the figure that shows the problem.
- "Drastically reduce" became a comparison the study can make. The proposal does not promise the size of the effect, because the writer does not know it yet.
- "Significant impact for stakeholders" was removed. The measure is the missed-appointment rate.
- The pilot and the resource line answer the feasibility question, which the first version did not address.

## Checks

1. Does every section and limit match the call?
2. Can a reviewer find the answer to each scoring criterion under a matching heading?
3. Is each aim checkable at the end of the project?
4. Does every claim of need, novelty or benefit carry a source, a comparison or a measure?
5. Does each budget line and each month of the timeline connect to a step of the method?
6. Read the summary alone. Does it say what, why, how and with what result?

`scripts/style_check.py draft.txt --genre proposal` applies the academic rhythm and connective measures and lists praise words.

## Sources

- Purdue Online Writing Lab. Introduction to grant writing; Grant writing in the sciences: planning. https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/grant_writing/index.html (follow the grantmaker's directions; specificity; preliminary study as evidence of feasibility; checklist of the funder's requirements)
- U.S. National Science Foundation. Preparing your proposal. https://www.nsf.gov/funding/preparing-proposal (the project description says what, why, how, how success will be known and what benefits could follow; every budget line is justified)
- Sacred Heart University Library. Organizing academic research papers: Writing a research proposal. https://library.sacredheart.edu/c.php?g=29803&p=185956 (the three questions what, why and how; common failures: no boundaries, loss of focus, detail on minor issues)

Confidence notes are in `evidence.md`, section 8. The five-question table merges the NSF and Sacred Heart lists and is this skill's own arrangement.
