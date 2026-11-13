# CV, résumé and cover letter

A recruiter gives a CV a few seconds on first reading. The page has to show, in a familiar layout, evidence that this person has done what this position needs.

## Ask first

- Which position, and where is the advertisement or description? The skills it names decide what goes in.
- Which country and sector? Length, photo and personal details follow local convention, so follow the employer's country and any template it supplies.
- For each role or project: what did the writer do, with which tools or methods, and what was the result? Ask for numbers: how many, how much, how often, how fast, for whom.
- Is there an existing CV, or a past cover letter the writer was happy with?

**Never invent a metric.** If the writer has no number, ask whether one can be looked up. If none exists, state the scope in plain terms (team size, frequency, tools) and leave the bullet unquantified. An unquantified true bullet is better than an impressive false one, and the writer will be asked about every line at interview.

## Structure to build on

### CV bullets

| Slot | Rule | Example |
|---|---|---|
| Action verb | The bullet starts with what the writer did: built, analysed, designed, taught, negotiated. No "I", no full sentence. | Built |
| Object | What was made, run or changed | 12 Power BI dashboards |
| How | The tool, method or technique, in context | on SQL views replacing manual Excel exports |
| Result | The accomplishment, with a figure where one exists | cutting monthly reporting from 3 days to 4 hours |

Further rules:

- **Accomplishment, not duty.** "Responsible for reporting" describes the job. The bullet describes what this person achieved in it.
- **Select for the position.** Keep a full master CV, and build each application from it by choosing the experience that shows the skills the advertisement asks for. Use the advertisement's own terms for those skills where they are true of the writer.
- **Conventional layout.** Standard section headings, reverse chronological order, one conservative font, bold only for headings and key names. Readers find things fastest where they expect them.
- **Tense.** Past tense for finished roles, present for the current one.
- **Length.** One page for an early-career résumé in the United States; two pages is common for a European CV and for experienced candidates; an academic CV runs as long as the record. Follow the local norm.
- **Profile summary.** Optional. If present, two lines that only this candidate could write: the field, the years, the specialism and the direction. Apply the swap test hard here.

### Cover letter

One page, addressed to a named person where the name can be found.

| Paragraph | Content |
|---|---|
| Opening | The position (with its reference number), who the writer is in one clause, and the one or two strengths the letter will show |
| Middle, one or two paragraphs | Two examples from experience, each tied to a requirement in the advertisement. Add what the CV cannot hold: the circumstances, the decision, what was learned. Do not restate the CV in sentences. |
| Why this employer | One specific reason that could not be said of a competitor: a project, a product, a method, a person spoken to |
| Close | Interest restated in one sentence, availability, thanks |

First person is correct in the letter. Sample letters on careers sites often contain the stock phrases listed below, so take their structure and leave their wording.

## The avoid list in a CV and cover letter

| Move | Typical form | Repair |
|---|---|---|
| Praise without evidence | "results-driven professional", "proven track record", "highly motivated", "detail-oriented", "strong communication skills", "ideal candidate" | Replace with the evidence, or delete. "Strong communication skills" becomes "Presented monthly results to a 15-person management team". |
| Importance flag | "played a key role in", "was instrumental in" | Name the role: what the writer personally did. |
| Elaborate verb | "leveraged", "utilised", "spearheaded" on every line | Plain verbs: used, led, built, ran. Vary them because the actions differ. |
| Duty in place of result | "Responsible for ...", "Tasked with ...", "Duties included ..." | Verb first, then object, method and result. |
| Emphatic modifiers | "passionate about", "deeply committed", "thrilled to apply" | State what the writer has done in the area. Interest shows in the specifics. |
| Corrective frame | "more than just an engineer", "not only a developer but also a leader" | State the second thing with its evidence. |
| Reflex triads | "dynamic, innovative and collaborative" | Count the things that are true and evidenced. |
| Staged opening (letter) | "I am writing to express my keen interest in ...", "In today's competitive landscape ..." | "I am applying for the [position] ([reference])." Then the strongest fact. |
| Borrowed values (letter) | "Your values of excellence and integrity align with my own" | The specific reason for this employer. |
| Formula ending (letter) | "I am confident that my skills make me a perfect fit for your esteemed organisation" | Availability and thanks. |
| Chat residue | "[Company Name]", "Here is a tailored version" | Remove. Search for every bracket. |

**Not defects here.** Fragments, bullet lists, the missing "I", section headings, and keywords taken from the advertisement where they are true.

**Do not over-correct.** Do not turn bullets into paragraphs, add personality to a CV that the sector expects to be plain, or remove a technical keyword because it sounds like jargon. Screening software and recruiters search for those terms.

## Example

The person and the figures are invented for illustration. In real work every detail comes from the writer.

**Before**

> **Profile**
> Results-driven data analyst with a proven track record of leveraging data to drive business impact. Passionate about transforming complex datasets into actionable insights in fast-paced environments.
>
> **Data Analyst, Retail company (2022-2025)**
> - Responsible for dashboards and reporting
> - Played a key role in improving data quality
> - Collaborated with cross-functional stakeholders to deliver impactful solutions

**After**

> **Data Analyst, Retail company (2022-2025)**
> - Built 12 Power BI dashboards used weekly by 40 store managers
> - Cut monthly reporting time from 3 days to 4 hours by replacing manual Excel exports with SQL views
> - Found and corrected duplicate customer records affecting 6% of the loyalty database
> - Presented results each month to the 15-person commercial team

**What changed**

- The profile fitted any analyst at any company, so it was removed. The bullets now do its work.
- "Responsible for" became what was built, for whom and how often it is used.
- "Played a key role in improving data quality" became the specific problem and its size.
- "Cross-functional stakeholders" and "impactful solutions" became the audience and the activity.
- Every number came from the writer. Where the writer had none, the bullet would stay plain.

## Checks

1. Swap test: could another candidate put their name on this line unchanged?
2. Does each bullet start with a verb and contain a fact?
3. How many bullets carry a figure? Ask about the ones that do not.
4. Does each requirement in the advertisement meet at least one line of evidence?
5. Can the writer talk for two minutes about every line?
6. Letter: is the employer-specific paragraph true of this employer only?

`scripts/style_check.py draft.txt --genre cv` reports the share of bullets with a figure and lists the stock phrases.

## Sources

- MIT Career Advising and Professional Development. Resumes. https://capd.mit.edu/resources/resumes/ (target the position description, conventional format, action verbs, how the work was done, accomplishments over duties, quantify, keywords)
- MIT Career Advising and Professional Development. How to write an effective cover letter. https://capd.mit.edu/resources/how-to-write-an-effective-cover-letter/ (one page, named addressee, purpose in the opening sentence, examples tied to the role, do not repeat the résumé)
- Purdue Online Writing Lab. Résumé design. https://owl.purdue.edu/owl/job_search_writing/resumes_and_vitas/resume_design.html (conventional format, reading order, most important information first)
- Purdue Online Writing Lab. Cover letters 1: Quick tips. https://owl.purdue.edu/owl/job_search_writing/job_search_letters/cover_letters_1_quick_tips/index.html

Confidence notes are in `evidence.md`, section 8. The length norms by country and the four-slot bullet are this skill's own summary of common practice.
