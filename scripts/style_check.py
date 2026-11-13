#!/usr/bin/env python3
"""Self-check for writing: patterns over-represented in LLM output, plus rhythm and connectives for prose.

This is NOT an AI detector. It counts surface features and lists sentences worth rereading.
A clean report does not mean a text will pass a detector; a flagged sentence may be perfectly good.

Usage:
    python3 style_check.py draft.txt
    python3 style_check.py draft.txt --genre email
    pbpaste | python3 style_check.py --genre cv

Genres: academic (default), proposal, email, cv, presentation.
Rhythm and connective thresholds come from journal articles, so they run for academic and proposal only.
"""
import argparse
import re
import statistics as st
import sys

# Style words with excess frequency in post-2022 academic text (Kobak et al. 2025; Wikipedia: Signs of AI writing).
# Mostly first-generation vocabulary, which has faded in 2026 models: flagged only as a cluster, never singly.
MARKERS = (
    r"delv\w*|tapestr\w*|testament|pivotal|multifacet\w*|intricat\w*|intricac\w*|meticulous\w*|underscor\w*|"
    r"showcas\w*|foster\w*|leverag\w*|landscape|realms?|interplay|nuanc\w*|bolster\w*|garner\w*|groundbreaking|"
    r"transformative|seamless\w*|holistic\w*|harness\w*|encompass\w*|elucidat\w*|unveil\w*|vibrant|invaluable|"
    r"commendable|burgeoning|noteworthy|paramount|myriad|plethora|embark\w*|unravel\w*|unlock\w*|revolutioni[sz]\w*|"
    r"cornerstone|ever-evolving|game-chang\w*|cutting-edge|aligns? with|deep dive"
)
STOCK = [
    r"it is (?:important|worth|crucial|essential|imperative) to (?:note|mention|highlight|recogni[sz]e|emphasi[sz]e)",
    r"it is worth noting", r"in today'?s\b", r"in the (?:realm|landscape|era) of", r"a testament to",
    r"sheds? (?:new )?light on", r"pav(?:es?|ing) the way", r"valuable insights?", r"despite these challenges",
    r"play(?:s|ed|ing)? an? (?:crucial|pivotal|vital|key|significant|important|central|critical|essential) role",
    r"(?:rapidly|constantly|ever) (?:evolving|changing)", r"a (?:wide|broad|diverse) (?:range|array|variety) of",
    r"(?:this|these findings?|the results?) (?:highlights?|underscores?|emphasi[sz]es?) the (?:importance|need|significance)",
    r"cannot be overstated", r"in conclusion,", r"when it comes to",
    r"(?:stands?|serves?) as a (?:testament|reminder)",
]
# Stock phrases by genre. Humans wrote all of these before 2022; they are listed because they delay or replace a fact.
GENRE_STOCK = {
    "email": [
        r"hope this (?:email|message|note|letter) finds you", r"I (?:just )?wanted to reach out", r"touch base",
        r"circle back", r"at your earliest convenience", r"do(?: not|n't) hesitate to",
        r"thank you (?:so much |very much )?for your time and consideration", r"I am writing to express",
        r"I (?:truly|really|deeply|sincerely) appreciate", r"I cannot stress enough", r"esteemed",
    ],
    "cv": [
        r"responsible for", r"tasked with", r"duties included", r"results[- ]driven", r"track record",
        r"highly motivated", r"detail[- ]oriented", r"team player", r"fast[- ]paced", r"passion(?:ate)? (?:about|for)",
        r"strong (?:communication|interpersonal|analytical|leadership) skills", r"ideal candidate", r"perfect fit",
        r"keen interest", r"esteemed", r"spearhead\w*", r"utili[sz]\w+", r"synerg\w+", r"stakeholders",
        r"actionable insights", r"driv(?:e|es|ing) (?:business )?(?:impact|results|growth)", r"instrumental in",
        r"play(?:s|ed)? a key role",
    ],
    "proposal": [
        r"innovative", r"\bnovel\b", r"state[- ]of[- ]the[- ]art", r"world[- ]class", r"critical gap",
        r"timely and relevant", r"significant impact", r"stakeholders", r"paradigm", r"unique opportunity",
        r"lasting contribution", r"has the potential to", r"rapidly evolving",
    ],
    "presentation": [
        r"^(?:overview|agenda|introduction|background|results|conclusions?|key takeaways|summary|next steps|"
        r"challenges and opportunities|thank you!?|questions\??|any questions\??)$",
        r"excited to", r"take you on a journey", r"without further ado", r"fast[- ]paced world", r"let'?s dive in",
        r"the power of", r"why (?:this|it) matters", r"significant (?:improvement|growth|impact|increase)",
        r"\benhanced\b", r"promising (?:implications|results)",
    ],
}
# Importance flagging in 2026 models (Graphite, AI Tells, 2026; Wikipedia: Signs of AI writing).
IMPORTANCE = (
    r"\b(?:this|that|it|distinction|difference) matters\b|\bwhy [\w' -]{1,40}? matters?\b|"
    r"\bmatters? (?:(?:here|now|most|more) )?because\b|\bmatters? (?:most|more than|enormously|as much as)\b|"
    r"\bjust as important\b|\babsolutely essential\b|"
    r"(?<!these )(?<!those )(?<!such )(?<!other )\bmatters[.;:]"
)
# Emphatic modifiers and stock idioms elevated in Gemini (Graphite, AI Tells: Gemini 4 Argon, 2026).
EMPHATIC = (
    r"\bdrastic(?:ally)?\b|\bunmatched\b|\bfantastic\b|\bincredibl[ey]\b|\bimmense(?:ly)?\b|\bremarkabl[ey]\b|"
    r"\bbridg(?:e|es|ed|ing) th(?:e|is|at) gap\b|\bfast[- ]paced world\b|\bhalf the battle\b|\bheavy lifting\b|"
    r"\bcrystal clear\b|\bgold standard\b"
)
# The assistant's wrapper or a template placeholder left in the text.
RESIDUE = (
    r"\bI hope this helps\b|\b(?:certainly|of course|absolutely)!|\bgreat question\b|"
    r"\bhere(?: is|'s) (?:a|an|the|your) (?:draft|revised|tailored|polished|updated|rewritten)\b|"
    r"\blet me know if you(?:'d| would) like\b|\bfeel free to (?:adjust|adapt|modify|tweak|customi[sz]e)\b|"
    r"\[(?:your|insert|company|name|recipient|date|position|role)[^\]]{0,40}\]"
)
INVISIBLE = "[​‌‍⁠﻿]"
COPULA = r"\b(?:serves?|stands?|acts?|functions?|operates?) as (?:a|an|the)\b|\bboasts?\b|\brepresents? a (?:significant|major|key|crucial|pivotal)\b"
QUANTITY = r"third|quarter|half|fifth|tenth|decade|century|year|month|week|day|dozen|hundred|thousand|million|billion|few"
CONTRAST = (
    r"\bnot (?:only|just|merely|simply)\b|\bmore than just\b|\brather than\b|\bit is not\b[^.]{1,60}\bbut\b|"
    r"\bnot (?:as )?an? [^.,;]{1,60}\bbut\b|"
    rf"\b(?:is|are|was|were) more than (?:simply |merely )?an? (?!(?:{QUANTITY})\b)|\bless like\b[^.]{{1,60}}\bmore like\b"
)
TAIL_VERBS = (
    "highlighting|underscoring|emphasi[sz]ing|showcasing|reflecting|demonstrating|illustrating|indicating|suggesting|"
    "ensuring|enabling|allowing|fostering|contributing|leading|making|providing|offering|paving|shaping|reinforcing|"
    "revealing|resulting|enhancing|facilitating|driving|creating|signaling|signalling|marking|delivering"
)
TAIL = rf",\s+(?:thereby |thus |further |ultimately |effectively )?(?:{TAIL_VERBS})\b"
VAGUE = (
    r"\b(?:studies|research|scholars|experts|researchers|the literature|evidence|many|some critics|observers)\s+"
    r"(?:have |has )?(?:shown|show|suggests?|indicates?|argue[sd]?|found|demonstrated?|agree)\b|"
    r"\bit is (?:widely|generally|commonly|well) (?:accepted|recogni[sz]ed|known|acknowledged|believed)\b"
)
CITED = r"\(\D{0,60}\d{4}[a-z]?[^)]*\)|\[\d+[^\]]*\]|et al\.|\b(?:19|20)\d{2}\)"
CONNECTIVES = [
    "however", "moreover", "furthermore", "additionally", "in addition", "therefore", "thus", "hence",
    "consequently", "nevertheless", "nonetheless", "in contrast", "conversely", "on the other hand", "for example",
    "for instance", "indeed", "similarly", "overall", "in conclusion", "in summary", "notably", "importantly",
    "ultimately", "as a result", "in particular", "likewise", "first", "second", "third", "finally",
]
ADDITIVE = ["moreover", "furthermore", "additionally", "in addition"]
FORMAL = ADDITIVE + ["conversely"]
CLOSERS = r"^(?:Overall|Ultimately|In summary|In conclusion|In essence|In short|This (?:highlights|underscores|demonstrates|shows)|These findings (?:highlight|underscore|demonstrate))\b"
ABBR = r"\b(?:et al|e\.g|i\.e|cf|vs|Fig|Figs|Eq|No|Vol|pp|ca|approx|Dr|Prof|Mr|Mrs|Ms|St)\."

PROSE = ("academic", "proposal")          # rhythm and connective thresholds apply
LINE_UNITS = ("cv", "presentation")       # the unit is the bullet or slide line, not the sentence
# Indicative ranges from three published, pre-2022 human articles (economics, environmental science, political theory).
HUMAN = {"cv": "0.46-0.59", "conn": "5-10%", "markers": "0-1.8", "tails": "0.2-0.4", "numbers": "27-62",
         "contrast": "0.2-1.0"}


def split_sentences(paragraph, min_words=3):
    p = re.sub(ABBR, lambda m: m.group(0).replace(".", "<D>"), paragraph)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(\[])", p)
    return [s.replace("<D>", ".").strip() for s in parts if len(s.split()) >= min_words]


def clean_line(line):
    """Strip quote, bullet, heading and bold markup so a bullet or slide line can be read as text."""
    line = re.sub(r"^\s*(?:>\s*)*", "", line)
    line = re.sub(r"^(?:[-*•–]|\d+[.)]|#+)\s+", "", line)
    return line.replace("**", "").strip()


def load(text, genre):
    """Return a list of units, each a list of sentences (prose and email) or a single line (cv, presentation)."""
    text = text.replace("’", "'").replace("“", '"').replace("”", '"')
    if genre in LINE_UNITS:
        return [[clean_line(l)] for l in text.split("\n") if clean_line(l)]
    blocks = re.split(r"\n\s*\n", text) if re.search(r"\n\s*\n", text) else text.split("\n")
    paras = [re.sub(r"\s+", " ", b).strip() for b in blocks]
    if genre in PROSE:
        paras = [p for p in paras if len(p.split()) >= 15 and not p.startswith("#")]
        return [split_sentences(p) for p in paras]
    paras = [" ".join(clean_line(l) for l in b.split("\n")) for b in re.split(r"\n\s*\n", text)]
    return [s for s in (split_sentences(p, min_words=2) for p in paras if p.strip()) if s]


def longest_flat_run(lengths, tolerance=6):
    """Longest run of consecutive sentences whose lengths all sit within `tolerance` words of each other."""
    best = run_start = 0
    for i in range(len(lengths)):
        while max(lengths[run_start:i + 1]) - min(lengths[run_start:i + 1]) > tolerance:
            run_start += 1
        best = max(best, i - run_start + 1)
    return best


def show(title, items, limit=8):
    if not items:
        return
    print(f"\n{title} ({len(items)})")
    for s in items[:limit]:
        print("  - " + (s if len(s) <= 190 else s[:187] + "..."))
    if len(items) > limit:
        print(f"  ... and {len(items) - limit} more")


def report_rhythm(sents, lengths, flags):
    print("\nRHYTHM")
    mean, sd = st.mean(lengths), st.pstdev(lengths)
    cv = sd / mean
    run = longest_flat_run(lengths)
    print(f"  sentence length: mean {mean:.1f}, sd {sd:.1f}, min {min(lengths)}, max {max(lengths)}")
    print(f"  variation (cv): {cv:.2f}   [human articles: {HUMAN['cv']}]")
    print(f"  longest run of similar-length sentences: {run}")
    if len(sents) >= 8 and cv < 0.40:
        flags.append("Sentence lengths are uniform (cv below 0.40).")
    if len(sents) >= 8 and run >= max(5, 0.3 * len(sents)):
        flags.append(f"{run} consecutive sentences sit within 6 words of each other.")
    if len(sents) >= 10 and (min(lengths) > 12 or max(lengths) < 30):
        flags.append("No short sentence (12 words or fewer) or no long one (30 or more).")


def report_connectives(sents, text, per_k, flags):
    print("\nCONNECTIVES AND OPENERS")
    starts = [c for s in sents for c in CONNECTIVES if re.match(rf"{c}\b[ ,]", s.lower())]
    additive = [c for c in starts if c in ADDITIVE]
    share = len(starts) / len(sents)
    print(f"  sentences opening with a connective: {share:.0%}   [human articles: {HUMAN['conn']}]")
    print(f"  additive openers (moreover/furthermore/additionally/in addition): {len(additive)}")
    if len(sents) >= 8 and share > 0.25:
        flags.append("More than a quarter of sentences open with a connective.")
    if len(additive) >= 3 and per_k(len(additive)) > 3:
        flags.append("Additive openers are stacked; link by repeating the key term instead.")
    formal = len(re.findall(rf"\b(?:{'|'.join(FORMAL)})\b", text, flags=re.I))
    print(f"  furthermore/additionally/moreover/in addition/conversely, any position: {per_k(formal):.1f} per 1,000 words")
    first = [re.sub(r"[^a-z]", "", s.split()[0].lower()) for s in sents]
    repeats = sorted({first[i] for i in range(len(first) - 2) if first[i] == first[i + 1] == first[i + 2]})
    if repeats:
        print(f"  same opening word three times running: {', '.join(repeats)}")


def main():
    ap = argparse.ArgumentParser(description="Self-check for writing. Not an AI detector.")
    ap.add_argument("file", nargs="?", help="text file; reads standard input when omitted")
    ap.add_argument("--genre", default="academic", choices=["academic", "proposal", "email", "cv", "presentation"])
    args = ap.parse_args()
    genre = args.genre
    raw = open(args.file, errors="ignore").read() if args.file else sys.stdin.read()

    invisible = len(re.findall(INVISIBLE, raw))
    raw = re.sub(INVISIBLE, "", raw)
    units = load(raw, genre)
    sents = [s for u in units for s in u]
    if not sents:
        sys.exit("Not enough text to check.")
    lengths = [len(s.split()) for s in sents]
    words = sum(lengths)
    text = " ".join(sents)
    per_k = lambda n: n / words * 1000
    flags = []
    unit_name = "Lines" if genre in LINE_UNITS else "Sentences"
    print(f"Genre: {genre}   Words: {words}   {unit_name}: {len(sents)}"
          + ("" if genre in LINE_UNITS else f"   Paragraphs: {len(units)}"))

    if genre in PROSE:
        report_rhythm(sents, lengths, flags)
        report_connectives(sents, text, per_k, flags)
    else:
        print("\nRhythm and connective measures are skipped for this genre; their thresholds come from journal articles.")

    print("\nPATTERNS (per 1,000 words)")
    markers = re.findall(rf"\b(?:{MARKERS})\b", text, flags=re.I)
    tails = [s for s in sents if re.search(TAIL, s)]
    copulas = [s for s in sents if re.search(COPULA, s, flags=re.I)]
    contrasts = [s for s in sents if re.search(CONTRAST, s, flags=re.I)]
    stock = [s for s in sents if any(re.search(p, s, flags=re.I) for p in STOCK)]
    genre_stock = [s for s in sents if any(re.search(p, s, flags=re.I) for p in GENRE_STOCK.get(genre, []))]
    importance = [s for s in sents if re.search(IMPORTANCE, s, flags=re.I)]
    emphatic = [s for s in sents if re.search(EMPHATIC, s, flags=re.I)]
    residue = [s for s in sents if re.search(RESIDUE, s, flags=re.I)]
    vague = [s for s in sents if re.search(VAGUE, s, flags=re.I) and not re.search(CITED, s)]
    closers = [u[-1] for u in units if len(u) >= 3 and re.match(CLOSERS, u[-1])]
    numbers = len(re.findall(r"\b\d[\d.,]*%?", text))
    dashes = len(re.findall("—| – | -- ", text))
    human = lambda key: f"   [human articles: {HUMAN[key]}]" if genre in PROSE else ""
    print(f"  marker vocabulary: {per_k(len(markers)):.1f}{human('markers')}"
          + (f"   -> {', '.join(sorted(set(m.lower() for m in markers)))}" if markers else ""))
    print(f"  trailing -ing commentary clauses: {per_k(len(tails)):.1f}{human('tails')}")
    print(f"  contrast frames (not only / not simply / rather than / more than a): {per_k(len(contrasts)):.1f}{human('contrast')}")
    print(f"  importance flags (this matters / matters because): {per_k(len(importance)):.1f}")
    print(f"  emphatic modifiers and stock idioms: {per_k(len(emphatic)):.1f}")
    print(f"  figures and dates: {per_k(numbers):.1f}{human('numbers')}")
    print(f"  dash asides: {per_k(dashes):.1f}")
    if genre == "cv":
        with_figure = sum(1 for s in sents if re.search(r"\d", s))
        print(f"  lines containing a figure: {with_figure} of {len(sents)}")
    if invisible:
        print(f"  invisible characters (zero-width): {invisible}")
        flags.append(f"{invisible} invisible zero-width characters found. Delete them.")
    if residue:
        flags.append("Chat residue or a template placeholder is still in the text.")
    if len(markers) >= 3 and per_k(len(markers)) > 3:
        flags.append("Marker vocabulary is dense. Replace each with the plain verb or the specific claim.")
    if len(tails) >= 2 and per_k(len(tails)) > 2:
        flags.append("Many sentences end in an -ing commentary clause.")
    if len(contrasts) >= 2 and per_k(len(contrasts)) > 3:
        flags.append("Contrast frames are frequent; state the positive claim directly.")
    if len(importance) >= 2:
        flags.append("Importance is asserted more than once ('this matters'). Give the reason as a fact instead.")
    if len(emphatic) >= 2 and per_k(len(emphatic)) > 2:
        flags.append("Emphatic modifiers or idioms recur. Replace each with the magnitude or the literal statement.")
    if genre in PROSE and words >= 150 and per_k(numbers) < 5:
        flags.append("Almost no figures, dates or citations. Check whether claims can be anchored to evidence.")
    if len(genre_stock) >= 2:
        flags.append(f"Stock {genre} phrases recur. Replace each with the fact, the request or the evidence.")

    show("REREAD: chat residue or placeholder", residue)
    show(f"REREAD: stock {genre} phrases; give the fact, the request or the evidence", genre_stock)
    show("REREAD: trailing -ing commentary", tails)
    show("REREAD: stock phrases", stock)
    show("REREAD: importance asserted ('this matters', 'matters because')", importance)
    show("REREAD: emphatic modifier or idiom; give the magnitude or the literal claim", emphatic)
    show("REREAD: 'serves as' / 'boasts' where 'is' or 'has' would do", copulas)
    show("REREAD: contrast frames; who holds the view being corrected?", contrasts)
    show("REREAD: attribution without a citation in the sentence", vague)
    show("REREAD: paragraph ends on a summary or moral", closers)

    print("\nSUMMARY")
    for f in flags or ["No threshold crossed. Read the REREAD lists above and the text aloud."]:
        print("  * " + f)
    print("\nThis report counts surface features only. It cannot judge whether the text is specific, "
          "sourced and yours.")


if __name__ == "__main__":
    main()
