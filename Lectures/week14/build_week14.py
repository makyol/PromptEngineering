#!/usr/bin/env python3
"""Week 14 — Synthesis and Course Wrap-Up.

Build:  python3 build_week14.py
Output: week14.pptx
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "Theme"))
from theme import *  # noqa

prs = new_deck()

title_slide(
    prs, 14,
    "Synthesis and Course Wrap-Up",
    "What holds it all together",
    notes="""
Welcome to the last session.

We're going to do three things today. Pull the course into a single shape, so it's one thing
rather than fourteen. Consolidate the failure taxonomy, because that's the part you'll actually
carry into your professional life. And go through exactly what the final exam covers, because
there's no reason for that to be a mystery.

I want to open by going back to week one. I gave you a sentence then, and I said the whole
semester would serve it. Let me put it back on the screen and ask whether it looks different
now.
""")

content_slide(
    prs, "Today: What We'll Explore",
    [
        "The through-line — one idea, fourteen weeks",
        "The consolidated failure taxonomy: every way these systems go wrong",
        "What each artifact was actually teaching you",
        "What to carry into professional practice",
        ("Exactly what the final exam covers", None, "bold"),
    ],
    notes="""
Five things.

The through-line — one idea running through fourteen weeks. If the course has been a list of
topics to you, today is where it becomes a single argument.

The consolidated failure taxonomy. Every way these systems go wrong, in one place, with names.
This is the most useful page in the course and I'd photograph it.

What each artifact was actually teaching you — because in several cases it wasn't the thing you
thought you were building.

What to carry into professional practice.

And exactly what the final exam covers. No surprises.
""")

# ══════════════════════════════════════════════════════════ part 1 — the through-line
section_slide(
    prs, 1, "The Through-Line",
    notes="""
Part one.
""")

callout_slide(
    prs,
    "This is a course about working with a system that is capable, confident, and sometimes wrong.",
    "Week 1. Everything since has been an answer to it.",
    notes="""
Here's the sentence from week one.

This is a course about working with a system that is capable, confident, and sometimes wrong.

In week one, this was an assertion. You had no reason to believe me beyond your own experience
of these tools.

Now you can justify every word of it mechanically.

Capable — because predicting text well across an enormous range of material requires internal
structure that functions like knowledge. Week three.

Confident — because there is no mechanism by which uncertainty could reach you. The same
operation runs whether the pattern is strong or weak, and nothing in the output distinguishes
them. Week three again.

And sometimes wrong — because the system optimises plausibility, and plausible correlates with
true but does not equal it. Where they come apart, nothing notices, because nothing is
checking.

That's the whole course in three clauses. Everything else was working out what to do about it.
""")

flow_slide(
    prs, "The Argument in Four Moves",
    [
        ("Understand the mechanism", "Weeks 1–5. Why it is confident, why it hallucinates, what actually improves output."),
        ("Constrain what it works from", "Weeks 6–7. Build small, ground in sources you chose, demand quotations."),
        ("Test rather than trust", "Weeks 8–9. Find how it fails before it matters. Keep chains short and inspectable."),
        ("Assume adversaries and consequences", "Weeks 10–13. Design deliberately, adapt to your field, expect attacks, act ethically."),
    ],
    caption="Each move exists because the previous one is insufficient on its own.",
    notes="""
Four moves. And read the caption first, because it explains why the order is what it is.

Understand the mechanism — weeks one to five. Why it's confident, why it hallucinates, what
actually improves output and what's folklore.

But understanding isn't enough, because knowing why it hallucinates doesn't stop it. So:
constrain what it works from — weeks six and seven. Build small things. Ground it in sources you
chose. Demand quotations.

But grounding isn't enough either, because it can still answer from memory, retrieve the wrong
passage, or over-read. So: test rather than trust — weeks eight and nine. Find out how it fails
before it matters, and keep automation short enough to inspect.

And testing isn't enough, because your test set assumes nobody is working against you and that
the consequences are yours alone. So: assume adversaries and consequences — weeks ten to
thirteen.

Each move exists because the previous one is insufficient. That's why the course couldn't be
reordered, and it's why the last four weeks aren't an appendix.
""")

# ══════════════════════════════════════════════════════════ part 2 — taxonomy
section_slide(
    prs, 2, "The Consolidated Failure Taxonomy",
    notes="""
Part two. The single most useful page in the course.
""")

boxes_slide(
    prs, "Failures of the Answer Itself",
    [
        ("Fabrication",
         "A specific detail invented inside an otherwise correct answer — a citation, a "
         "statistic, a study. The format is easy to imitate; the content is not."),
        ("Displacement",
         "Correct somewhere else — another country, era or context. Nothing is false; nothing "
         "applies. The most common failure for work in Turkey."),
        ("Omission",
         "Everything present is true; the thing that mattered most is absent. The hardest to "
         "catch, because there is no wrong sentence to point at."),
    ],
    notes="""
The taxonomy, in three parts. First: failures of the answer itself. These are from week one, and
they apply to any output.

Fabrication. A specific detail invented inside an otherwise correct answer — a citation, a
statistic, a study, a drug interaction. And you now know why the format is convincing: citations
are highly patterned, so the shape is easy to predict even when the content doesn't exist.

Displacement. Correct somewhere else — another country, another era, another context. Nothing
in it is false; nothing in it applies to you. And you know the mechanism: thin coverage means
the probable continuation comes from wherever the text was densest. For a room working in
Turkey, this is your most common failure.

Omission. Everything present is true, but the thing that mattered most isn't there. Hardest to
catch, because there's no wrong sentence to point at — you can only catch it if you already know
what should have been said. Which is why it's most dangerous outside your own expertise.

And running underneath all three: overconfidence. Not a separate failure so much as the property
that makes the other three dangerous.
""")

boxes_slide(
    prs, "Failures of Grounded and Built Systems",
    [
        ("Answered from memory",
         "Your sources did not contain it; something adjacent was used instead. Detect it: no "
         "quotation, or a vague one."),
        ("Wrong passage · over-read",
         "The right words in an unrelated place, or a claim stronger than the sentence it cites. "
         "\"May\" becomes \"must\". Detect it: compare claim strength against quote strength."),
        ("Silent failure",
         "A step produces something wrong but plausible; nothing errors; the chain continues "
         "confidently. The characteristic failure of anything multi-step."),
    ],
    notes="""
Second part: failures of systems you build.

Answered from memory. Your sources didn't contain it, so something adjacent was used instead.
Detect it by the absence of a quotation, or a vague gesture where a sentence should be. Week
seven.

Wrong passage, and over-reading. The right words appearing in an unrelated place, or a claim
stronger than the sentence it cites — "may" becoming "must," an example becoming a rule. Detect
it by comparing the strength of the claim against the strength of the quote. If the answer is
more confident than its evidence, something has been added. Week seven again, and it's the most
common of the three.

And silent failure. A step produces something wrong but plausible, nothing errors, and the chain
continues confidently on bad input. The characteristic failure of anything multi-step, and the
reason chains stay short and inspectable. Week nine.

Notice the pattern across all six failures so far. Every single one is invisible in the output.
That's not a coincidence — it's the same root cause each time. There's no truth check, so
there's nothing to report.
""")

boxes_slide(
    prs, "Failures With an Author",
    [
        ("Direct injection · jailbreaking",
         "Someone types something to override the system's instructions. Safety behaviour is a "
         "trained tendency, not a gate."),
        ("Indirect injection",
         "Instructions hidden in content the system reads. You never see it and there is no "
         "point at which you could refuse. The one that will actually reach you."),
        ("Leakage",
         "Context is shared more widely than intended — a shared link carries the whole history. "
         "Anonymisation is harder than removing names."),
    ],
    notes="""
Third part: failures with an author. Week twelve.

Direct injection and jailbreaking. Someone types something to override the instructions. And you
know why it works: safety behaviour is a trained tendency that shifts probabilities, not a gate
that blocks.

Indirect injection. Instructions hidden in content the system reads — a document, a page, an
email. You never see it. There's no point at which you could have refused. This is the one that
will actually reach you, and it's why "be careful what you upload" is insufficient advice.

And leakage. Context shared more widely than intended — a shared link carries the whole history,
not just the last message. Anonymisation is harder than removing names, because a rare
condition, a date and a small department can identify someone precisely.

Now step back and look at all nine failures together. Every one of them is invisible in the
output. Not most. All of them.

That's why this course is built the way it is. If any of these announced themselves, you'd need
a warning, not a semester. The procedures exist because perception doesn't work here.
""")

# ══════════════════════════════════════════════════════════ part 3 — artifacts
section_slide(
    prs, 3, "What the Artifacts Were Teaching",
    notes="""
Part three. In several cases it wasn't what you thought.
""")

content_slide(
    prs, "The Artifacts, Reconsidered",
    [
        ("Micro-Tool", None, "bold"),
        (1, "Not \"you can build software\". That the surface is not evidence — you could see it looked right and not whether it was right.", None),
        ("Grounded Assistant", None, "bold"),
        (1, "Not \"how to use a document tool\". That you cannot prompt your way to absent information — you must supply it.", None),
        ("Test Set", None, "bold"),
        (1, "Not \"how to test\". That the three unanswerable questions reveal what normal use cannot.", None),
        ("Automation Chain", None, "bold"),
        (1, "Not \"how to automate\". That removing yourself removes the checking you were doing for free.", None),
        ("Field Build · Domain Pack · Attack Report", None, "bold"),
        (1, "That design is mostly constraint, that formatting is not accuracy, and that some failures have an author.", None),
    ],
    notes="""
Let me tell you what each artifact was actually for, because in several cases it wasn't what it
looked like.

The Micro-Tool was not about proving you can build software, although you can. It was to create
a situation where you could see that something looked right and had no way to check whether it
was right. The verification gap, made personal.

The Grounded Assistant was not a tutorial in a document tool. It was to establish that you
cannot prompt your way to absent information — you have to supply it. That's a negative result
and negative results are hard to teach abstractly.

The Test Set was not about testing methodology. It was so that three unanswerable questions
would reveal something normal use never could. Most of you watched your own system answer a
question it couldn't possibly answer. That's the moment the course was built around.

The Automation Chain was not about automation. It was so you would notice that removing yourself
removes the checking you were doing for free and never counted as work.

And the last three: design is mostly constraint, formatting is not accuracy, and some failures
have an author.

None of the artifacts matter. What you noticed while building them does.
""")

content_slide(
    prs, "What to Carry Into Practice",
    [
        (1, "Ask what is being measured, and what you are certifying", None),
        (1, "Supply sources rather than instructing accuracy", None),
        (1, "Ask for the basis of an answer, then check it — the quote test costs seconds", None),
        (1, "Write three questions it cannot answer, before you trust any system", None),
        (1, "Put the human before the irreversible action", None),
        (1, "Treat everything the system reads as instruction-carrying", None),
        (1, "Name the person who would be harmed", None),
        (1, "Keep one skill you practise unaided", None),
    ],
    notes="""
Eight things. If you keep nothing else, keep this slide.

Ask what is being measured, and what you're certifying. That covers academic integrity and most
professional ethics.

Supply sources rather than instructing accuracy. "Be accurate" adds authority, not facts.

Ask for the basis of an answer, then check it. The quote test costs seconds and catches
fabrication, over-reading and poisoned summaries all at once.

Write three questions it cannot answer, before you trust any system. Three questions and five
minutes tell you more than a month of ordinary use.

Put the human before the irreversible action.

Treat everything the system reads as instruction-carrying, not merely as data.

Name the person who would be harmed — a category is not an answer.

And keep one skill you practise unaided.

Eight habits. None of them require a particular tool, and none of them will be obsolete when the
tools change.
""")

# ══════════════════════════════════════════════════════════ part 4 — the exam
section_slide(
    prs, 4, "The Final Exam",
    notes="""
Part four. No mysteries.
""")

content_slide(
    prs, "What the Final Covers",
    [
        ("Format: 40 multiple-choice questions · 2.5 points each · 90 minutes · closed book", None, "bold"),
        "",
        ("Coverage: the whole course, weighted towards Weeks 6–13", None, "bold"),
        (1, "Roughly one third mechanism — tokens, prediction, context, why hallucination happens", None),
        (1, "Roughly one third diagnosis — here is an answer and its source; what is wrong with it?", None),
        (1, "Roughly one third design and judgment — where does the human go, what should this system not do", None),
        "",
        ("Every \"concepts you must be able to define and diagnose\" slide is examinable in full.", None, "bold"),
    ],
    notes="""
The format: forty multiple-choice questions, two and a half points each, ninety minutes, closed
book. Same shape as the midterm, so nothing about the format should surprise you.

Coverage is the whole course, weighted towards weeks six to thirteen — because that's where the
judgment lives, and judgment is what I'm assessing.

Roughly a third is mechanism. Tokens, prediction, context windows, why hallucination happens.
These are the questions you can prepare for by understanding rather than memorising.

Roughly a third is diagnosis. I give you an answer and its source and ask what's wrong with it.
Which of the failure modes is this? These are the questions the build weeks prepared you for,
and if you did the building they'll feel easy.

And roughly a third is design and judgment. Where does the human go? What should this system not
do? Which design rule does this workflow violate?

And the bold line: every "concepts you must be able to define and diagnose" slide is examinable
in full. There are seven of them, one per build week. That is your revision list, and it's
deliberately short.
""")

boxes_slide(
    prs, "How to Revise",
    [
        ("Learn the taxonomy by name",
         "Nine failure modes across three groups. Most diagnosis questions are asking you to name "
         "one. If you can name them, you can answer them."),
        ("Be able to explain mechanisms, not just state them",
         "Not \"it hallucinates\" but why — no truth check, plausibility optimised, thin coverage "
         "where plausible and true come apart."),
        ("Practise on your own artifacts",
         "Take your Field Build worksheet and ask: which of the nine could hit this? Where is the "
         "human? What did I constrain? That is the exam."),
    ],
    notes="""
Three pieces of revision advice.

Learn the taxonomy by name. Nine failure modes across three groups — failures of the answer,
failures of built systems, failures with an author. Most diagnosis questions are asking you to
name one. If you can name them reliably, that third of the paper is straightforward.

Be able to explain mechanisms, not just state them. Not "it hallucinates" but why — there's no
truth check, it optimises plausibility, and in thin coverage plausible and true come apart. The
distractors on the mechanism questions are designed to catch people who memorised the label
without the reason.

And practise on your own artifacts. Take your week ten worksheet and ask: which of the nine could
hit this system? Where's the human? What did I constrain and why? That's the exam. If you can do
that for your own design, you can do it for one I hand you.

That's genuinely the most efficient revision available, and it takes about twenty minutes.
""")

content_slide(
    prs, "Closing",
    [
        "You can explain how these systems work, in plain language, to anyone",
        "You have built four things and broken three of them",
        ("You know that every failure that matters is invisible in the output", None, "bold"),
        "And you know what to do about it: supply sources, ask for the basis, test what it cannot know, keep the human before the irreversible step",
        "",
        (1, "The tools will change. All of that survives them.", None),
    ],
    notes="""
Where you started and where you are.

In week one, most of you could use these tools. Now you can explain how they work, in plain
language, to anyone — a colleague, a supervisor, a patient who asks whether the AI wrote their
letter.

You've built four things and broken three of them, which is a better ratio than most
professional training manages.

You know that every failure that matters is invisible in the output. That's the sentence I'd
most like to survive this course, because it's what stops you relying on your own perception in
a situation where perception doesn't work.

And you know what to do about it. Supply sources. Ask for the basis. Test what it cannot know.
Keep the human before the irreversible step.

The tools will change. Everything in that list survives them, because none of it depends on
which product you're using.

Thank you for the semester. It's been a genuinely good group, and the cross-disciplinary mix did
what I hoped it would — the best questions this term came from people asking about fields that
weren't their own.

Good luck in the exam. My email is on the next slide and it stays open after the course ends.
""")

closing_slide(
    prs,
    notes="""
Take final questions.

Common ones:

"Will the exam have questions about specific tools?" — No. Nothing product-specific. Concepts,
mechanisms, diagnosis and design only.

"Can we see a sample question?" — Yes, and you should have the midterm back to look at. The
final is the same style, with more diagnosis and design.

"What should I do next if I want to go further?" — Build something real, in your own field, with
someone senior aware of it. That will teach you more than any further course, and you now have
the worksheet and the taxonomy to do it responsibly.

"Can I contact you after the course?" — Yes. Genuinely. If you're building something in your
department and want a second opinion on the design, that's exactly the thing I'd like to hear
about.
""")

save(prs, str(pathlib.Path(__file__).parent / "week14.pptx"))
