#!/usr/bin/env python3
"""Self-check for academic prose: rhythm, connectives, and patterns over-represented in LLM output.

This is NOT an AI detector. It counts surface features and lists sentences worth rereading.
A clean report does not mean a text will pass a detector; a flagged sentence may be perfectly good.

Usage:
    python3 style_check.py draft.txt
    pbpaste | python3 style_check.py
"""
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
# Importance flagging in 2026 models (Graphite, AI Tells, 2026; Wikipedia: Signs of AI writing).
IMPORTANCE = (
    r"\b(?:this|that|it|distinction|difference) matters\b|\bwhy [\w' -]{1,40}? matters?\b|"
    r"\bmatters? (?:because|most|more than|enormously)\b|\bjust as important\b|\babsolutely essential\b|"
    r"(?<!these )(?<!those )(?<!such )(?<!other )\bmatters[.;:]"
)
# Emphatic modifiers and stock idioms elevated in Gemini (Graphite, AI Tells: Gemini 4 Argon, 2026).
EMPHATIC = (
    r"\bdrastic(?:ally)?\b|\bunmatched\b|\bfantastic\b|\bincredibl[ey]\b|\bimmense(?:ly)?\b|\bremarkabl[ey]\b|"
    r"\bbridg(?:e|es|ed|ing) th(?:e|is|at) gap\b|\bfast[- ]paced world\b|\bhalf the battle\b|\bheavy lifting\b|"
    r"\bcrystal clear\b|\bgold standard\b"
)
COPULA = r"\b(?:serves?|stands?|acts?|functions?|operates?) as (?:a|an|the)\b|\bboasts?\b|\brepresents? a (?:significant|major|key|crucial|pivotal)\b"
QUANTITY = r"third|quarter|half|fifth|tenth|decade|century|year|month|week|day|dozen|hundred|thousand|million|billion|few"
CONTRAST = (
    r"\bnot (?:only|just|merely|simply)\b|\bmore than just\b|\brather than\b|\bit is not\b[^.]{1,60}\bbut\b|"
    rf"\b(?:is|are|was|were) more than (?:simply |merely )?an? (?!(?:{QUANTITY})\b)|\bless like\b[^.]{{1,60}}\bmore like\b"
)
TAIL_VERBS = (
    "highlighting|underscoring|emphasi[sz]ing|showcasing|reflecting|demonstrating|illustrating|indicating|suggesting|"
    "ensuring|enabling|allowing|fostering|contributing|leading|making|providing|offering|paving|shaping|reinforcing|"
    "revealing|resulting|enhancing|facilitating|driving|creating|signaling|signalling|marking"
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
ABBR = r"\b(?:et al|e\.g|i\.e|cf|vs|Fig|Figs|Eq|No|Vol|pp|ca|approx|Dr|Prof|Mr|Ms|St)\."

# Indicative ranges from three published, pre-2022 human articles (economics, environmental science, political theory).
HUMAN = {"cv": "0.46-0.59", "conn": "5-10%", "markers": "0-1.8", "tails": "0.2-0.4", "numbers": "27-62"}


def split_sentences(paragraph):
    p = re.sub(ABBR, lambda m: m.group(0).replace(".", "<D>"), paragraph)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(\[])", p)
    return [s.replace("<D>", ".").strip() for s in parts if len(s.split()) >= 3]


def load(text):
    text = text.replace("’", "'").replace("“", '"').replace("”", '"')
    blocks = re.split(r"\n\s*\n", text) if re.search(r"\n\s*\n", text) else text.split("\n")
    paras = [re.sub(r"\s+", " ", b).strip() for b in blocks]
    return [p for p in paras if len(p.split()) >= 15 and not p.startswith("#")]


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


def main():
    raw = open(sys.argv[1], errors="ignore").read() if len(sys.argv) > 1 else sys.stdin.read()
    paras = load(raw)
    para_sents = [split_sentences(p) for p in paras]
    sents = [s for ps in para_sents for s in ps]
    if len(sents) < 3:
        sys.exit("Need at least three sentences of prose.")
    lengths = [len(s.split()) for s in sents]
    words = sum(lengths)
    text = " ".join(sents)
    per_k = lambda n: n / words * 1000
    flags = []

    print(f"Words: {words}   Sentences: {len(sents)}   Paragraphs: {len(paras)}")
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

    print("\nPATTERNS (per 1,000 words)")
    markers = re.findall(rf"\b(?:{MARKERS})\b", text, flags=re.I)
    tails = [s for s in sents if re.search(TAIL, s)]
    copulas = [s for s in sents if re.search(COPULA, s, flags=re.I)]
    contrasts = [s for s in sents if re.search(CONTRAST, s, flags=re.I)]
    stock = [s for s in sents if any(re.search(p, s, flags=re.I) for p in STOCK)]
    importance = [s for s in sents if re.search(IMPORTANCE, s, flags=re.I)]
    emphatic = [s for s in sents if re.search(EMPHATIC, s, flags=re.I)]
    vague = [s for s in sents if re.search(VAGUE, s, flags=re.I) and not re.search(CITED, s)]
    closers = [ps[-1] for ps in para_sents if len(ps) >= 3 and re.match(CLOSERS, ps[-1])]
    numbers = len(re.findall(r"\b\d[\d.,]*%?", text))
    dashes = len(re.findall("—| – | -- ", text))
    print(f"  marker vocabulary: {per_k(len(markers)):.1f}   [human articles: {HUMAN['markers']}]"
          + (f"   -> {', '.join(sorted(set(m.lower() for m in markers)))}" if markers else ""))
    print(f"  trailing -ing commentary clauses: {per_k(len(tails)):.1f}   [human articles: {HUMAN['tails']}]")
    print(f"  contrast frames (not only / not simply / rather than / more than a): {per_k(len(contrasts)):.1f}")
    print(f"  importance flags (this matters / matters because): {per_k(len(importance)):.1f}")
    print(f"  emphatic modifiers and stock idioms: {per_k(len(emphatic)):.1f}")
    print(f"  figures and dates: {per_k(numbers):.1f}   [human articles: {HUMAN['numbers']}]")
    print(f"  dash asides: {per_k(dashes):.1f}")
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
    if words >= 150 and per_k(numbers) < 5:
        flags.append("Almost no figures, dates or citations. Check whether claims can be anchored to evidence.")

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
    print("\nThis report counts surface features only. It cannot judge whether the argument is specific, "
          "sourced and yours.")


if __name__ == "__main__":
    main()
