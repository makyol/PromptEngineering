#!/usr/bin/env python3
"""Week 8 — Verification: Knowing When AI Is Wrong.  Artifact: Test Set.

Build:  python3 build_week08.py
Output: week08.pptx
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "Theme"))
from theme import *  # noqa

prs = new_deck()

title_slide(
    prs, 8,
    "Verification: Knowing When AI Is Wrong",
    "Artifact: the Test Set",
    notes="""
Welcome back.

Last week you built something that answers from your own documents, and we ended by naming
three ways a grounded answer goes wrong.

Today you find out how often that happens — on your own system, with your own eyes.

This is the session I care most about. Everything else in this course is useful. This is the
part that makes you professionally different from someone who has simply used these tools a
lot. Because anyone can use them. Almost nobody tests them.

And I want to warn you: today is slightly uncomfortable. You are going to build ten questions
designed to break something you made an hour ago, three of which your documents cannot
possibly answer. And it will answer them anyway. Confidently. With a citation, sometimes.

That's not a failure of your build. It's the mechanism from week three, and today you'll watch
it happen to you rather than hearing me describe it.
""")

content_slide(
    prs, "Today: What We'll Explore",
    [
        "Why verification is harder than generation — and why that gap keeps growing",
        "The test set: seven questions it should answer, three it cannot",
        ("Why the three unanswerable questions are the whole exercise", None, "bold"),
        "Writing a question that actually tests something",
        "Why asking twice is not checking",
        "Build: your own Test Set, and run it",
    ],
    notes="""
Where we're going.

First, why verification is harder than generation. There's an asymmetry here that gets worse
as the systems improve, and understanding it explains why this skill becomes more valuable
over time rather than less.

Then the test set — the actual artifact. Seven questions it should be able to answer, three
it cannot.

Then why those three unanswerable questions are the whole exercise. If you take one thing
from today, it's this.

Then how to write a question that actually tests something, because most questions people
write don't.

Then why asking twice isn't checking — a trap almost everyone falls into.

Then you build one and run it.
""")

# ══════════════════════════════════════════════════════════ part 1 — the gap
section_slide(
    prs, 1, "The Verification Gap",
    notes="""
Part one. Why this is hard.
""")

callout_slide(
    prs,
    "It takes seconds to generate an answer and much longer to check one.",
    "That asymmetry is the whole problem — and it widens as the output gets better.",
    notes="""
Here's the asymmetry.

It takes seconds to generate an answer and much longer to check one.

Ask for a summary of a forty-page report: five seconds. Verify that the summary is accurate
and complete: you read the forty pages. The tool has saved you nothing if you check properly,
and has saved you a great deal if you don't.

Almost everyone, almost always, doesn't.

Now the second line, which is the part people miss. This gap widens as output gets better.

When output is obviously bad, checking is fast — you spot the nonsense and discard it. As
quality rises, errors get rarer and subtler, so you have to look harder to find them, and
you're less motivated to look because the last twenty answers were fine.

So: better models make verification harder, not easier. That's counterintuitive and it's why
this skill appreciates rather than depreciating.

The response isn't to check everything, which is impossible. It's to test the system once,
properly, so you know what kind of thing it gets wrong. That's what a test set is for.
""")

flow_slide(
    prs, "Testing the System, Not the Answer",
    [
        ("Build once", "You make a grounded assistant, a tool, a workflow."),
        ("Test deliberately", "Ten questions where you already know the right answer — including what it cannot know."),
        ("Learn its shape", "You discover how it fails, not just whether it failed today."),
        ("Use it accordingly", "You now know which answers to trust and which to check."),
    ],
    caption="You cannot verify every answer forever. You can characterise the system once and use it knowingly.",
    notes="""
Here's the strategy, and it's different from what people expect.

You build something once. Then you test it deliberately — ten questions where you already know
the right answer, including questions about things it cannot possibly know.

From that, you learn its shape. Not "did it fail today" but *how* it fails. Does it invent
citations? Does it over-read? Does it quietly answer from memory when the documents run out?

And then you use it accordingly. You know which categories of answer to trust and which to
check every time.

Read the caption, because this is the realistic position. You cannot verify every answer
forever — nobody has that discipline and nobody has that time. What you can do is characterise
the system once and then use it knowingly.

That's the difference between a professional and an enthusiast. Not that the professional
checks more. That the professional knows what to check.
""")

# ═══════════════════════════════════════════════════════════ part 2 — test set
section_slide(
    prs, 2, "The Test Set",
    notes="""
Part two. The artifact.
""")

content_slide(
    prs, "Ten Questions: Seven and Three",
    [
        ("Seven questions your sources genuinely answer.", None, "bold"),
        (1, "Two easy — the answer is stated plainly in one place", None),
        (1, "Three medium — the answer requires combining two parts of a document", None),
        (1, "Two hard — the answer is stated in unusual wording, or in a table, or as an exception", None),
        "",
        ("Three questions your sources cannot answer.", None, "bold"),
        (1, "Plausible questions someone would genuinely ask, about material that simply is not there", None),
        (1, "The correct response to all three is the refusal string from last week", None),
    ],
    notes="""
Ten questions. Seven plus three.

The seven your sources genuinely answer, graded by difficulty.

Two easy — the answer is stated plainly in one place. These check the basic machinery works.

Three medium — the answer requires combining two parts of a document. Remember from last week
that retrieval pulls passages, not whole documents, so this is where things start to strain.

Two hard — the answer is stated in unusual wording, or lives in a table, or is phrased as an
exception. Exceptions are particularly good tests, because a system that retrieves the general
rule and misses the exception gives you a confident answer that's wrong in exactly the cases
that matter.

Then three your sources cannot answer. Plausible questions somebody would genuinely ask, about
material that simply isn't in your documents. Not silly questions — plausible ones.

The correct response to all three is last week's refusal string. NOT IN SOURCES.

Anything else is a finding.
""")

callout_slide(
    prs,
    "The three unanswerable questions are the entire exercise.",
    "The other seven tell you it works. These three tell you what it does when it doesn't.",
    notes="""
If you remember one slide from this week, this one.

The three unanswerable questions are the entire exercise.

Here's why. The seven answerable ones tell you the system works, and it probably does — that's
the boring result and it's what most people stop at. Somebody builds something, tries a few
questions, gets good answers, and concludes it's reliable.

But they've only tested the case where things go well.

The three unanswerable questions test the case that actually matters: what does this system do
when it doesn't know? Because in real use, you will ask questions your sources don't cover.
That is guaranteed. You won't know you're doing it — that's the whole problem — but you will do
it.

And the behaviour in that situation is the single most important property of the system. Does
it refuse cleanly? Does it hedge and then answer anyway? Does it invent a citation?

You cannot discover that by using it normally, because when you use it normally you don't know
which questions are unanswerable. You only find out by constructing the situation deliberately.

That's what today is.
""")

boxes_slide(
    prs, "Writing a Question That Tests Something",
    [
        ("Specific enough to be wrong",
         "\"What does the guideline say about dosing?\" cannot be graded. \"What is the maximum "
         "daily dose it states for adults?\" has one right answer, so you can tell whether you "
         "got it."),
        ("You already know the answer",
         "If you have to look it up afterwards to grade it, you will not grade it. Write "
         "questions from material you have read. Note the answer before you run it."),
        ("The unanswerable ones must be plausible",
         "Not absurd. Something a colleague would genuinely ask, that your documents happen not "
         "to cover — an adjacent topic, a different jurisdiction, a later year."),
    ],
    notes="""
Three rules for writing questions that actually test something.

Specific enough to be wrong. "What does the guideline say about dosing?" cannot be graded —
almost any answer is arguably responsive. "What is the maximum daily dose it states for
adults?" has one right answer, so you can tell whether you got it. If you can't imagine
marking it wrong, it isn't a test question.

You already know the answer. If you have to go and look it up afterwards in order to grade it,
you won't grade it. You'll skim the answer, think "sounds right," and move on. So write
questions from material you've actually read, and write the expected answer down *before* you
run it. That order matters — writing it afterwards lets you unconsciously accept whatever you
got.

And the unanswerable ones must be plausible. This is the one people get wrong. Don't ask your
clinical guideline about football. Ask it something a colleague would genuinely ask that your
documents happen not to cover — an adjacent topic, a different jurisdiction, a later year, a
related condition. That's the realistic case, and it's where the system actually fails.
""")

content_slide(
    prs, "Grading What Comes Back",
    [
        ("For each of the ten, record one of:", None, "bold"),
        (1, "CORRECT — right answer, and the quotation genuinely supports it", None),
        (1, "UNSUPPORTED — plausible answer, but no quotation, or a quotation that does not support it", None),
        (1, "WRONG — the answer contradicts the source", None),
        (1, "REFUSED — said NOT IN SOURCES", None),
        "",
        ("Then read the pattern, not the score:", None, "bold"),
        (1, "REFUSED on all three unanswerable questions is the result you want", None),
        (1, "UNSUPPORTED on any of the three is your headline finding — write it down", None),
    ],
    notes="""
Four grades. Keep it this simple, because a complicated rubric doesn't get used.

CORRECT — right answer, and the quotation genuinely supports it. Both halves required.

UNSUPPORTED — plausible answer, but no quotation, or a quotation that doesn't actually support
the claim. Note that an answer can be *true* and still graded UNSUPPORTED, because you're
testing the system's process, not its luck.

WRONG — the answer contradicts the source.

REFUSED — said NOT IN SOURCES.

Now the bold part: read the pattern, not the score. Nobody cares that you got seven out of ten.
What matters is *which* ones and *how*.

REFUSED on all three unanswerable questions is the result you want. That's a well-behaved
system and you can use it with reasonable confidence.

UNSUPPORTED on any of the three unanswerable questions is your headline finding. Write it down
in words: "when it doesn't know, it answers anyway." That single sentence should change how
you use the system permanently.
""")

content_slide(
    prs, "Why Asking Twice Is Not Checking",
    [
        "The most common informal verification method, and it does not work",
        (1, "You get an answer, feel unsure, ask again, get something similar, feel reassured", None),
        "",
        ("What consistency actually measures:", None, "bold"),
        (1, "How strongly the pattern is represented in the training data — not whether it is true", None),
        (1, "A widely repeated error is reproduced very consistently indeed", None),
        "",
        ("What does work:", None, "bold"),
        (1, "Check against a source. Check against something you already know. Ask for the quotation and look it up.", None),
        (1, "Asking a different model is slightly better than asking the same one twice — but they may share the same error.", None),
    ],
    notes="""
The most common informal verification method, and it doesn't work.

The pattern: you get an answer, you feel unsure, you ask again, you get something similar, and
you feel reassured. Everyone does this. It feels like checking.

What consistency actually measures is how strongly a pattern is represented in the training
data. Not whether it's true. And the crucial consequence: a widely repeated error is reproduced
very consistently indeed. Common misconceptions are, by definition, common in text. So the
things you're most likely to get wrong are the things that will come back most consistently.

Consistency is, if anything, weak evidence in the wrong direction for exactly the errors that
matter.

What does work: check against a source. Check against something you already know. Ask for the
quotation and look it up. All of those compare the answer against something outside the system.

Asking a different model is slightly better than asking the same one twice, because the errors
may differ. But they're trained on overlapping material, so a widespread misconception may
appear in both. Better than nothing; not proof.

The general principle: verification requires something outside the system. Another opinion from
inside it isn't independent.
""")

# ══════════════════════════════════════════════════════════════ build
section_slide(
    prs, 3, "Build",
    notes="""
Part three. Twenty minutes. This one is uncomfortable by design.
""")

activity_slide(
    prs, "Build and Run Your Test Set",
    [
        ("1.  Write seven questions your sources answer — two easy, three medium, two hard.", None, "bold"),
        (1, "Write the expected answer next to each one BEFORE you run anything.", None),
        ("2.  Write three plausible questions your sources cannot answer.", None, "bold"),
        (1, "Adjacent topic, different jurisdiction, a later year. Realistic, not absurd.", None),
        ("3.  Run all ten against your Week 7 assistant — or against mine.", None, "bold"),
        ("4.  Grade each: CORRECT · UNSUPPORTED · WRONG · REFUSED.", None, "bold"),
        (1, "Then write one sentence describing how this system behaves when it does not know.", None),
    ],
    minutes=20,
    notes="""
Twenty minutes. Four steps.

One. Seven questions your sources answer — two easy, three medium, two hard. And write the
expected answer next to each one *before* you run anything. I'll keep saying this because it's
the step everyone skips and it's the step that makes the exercise honest.

Two. Three plausible questions your sources cannot answer. Adjacent topic, different
jurisdiction, a later year. Realistic, not absurd.

Three. Run all ten against your week seven assistant. If you don't have one — if you weren't
here, or it didn't work — use mine, it's on the board with its source pack.

Four. Grade each one, and then write a single sentence describing how this system behaves when
it doesn't know.

That sentence is what you take away. Not the assistant. Not the score. The sentence.

[Circulate. Watch for: unanswerable questions that are too absurd — push them to make them
plausible; and people grading generously. Ask "did you look up that quote?" If nobody is
building, run the provided test set on the provided assistant on screen — the three
unanswerable ones are the demonstration.]
""")

boxes_slide(
    prs, "What Almost Always Happens",
    [
        ("It answers at least one unanswerable question",
         "Usually with something reasonable-sounding drawn from general knowledge, sometimes with "
         "a hedge attached. This is the mechanism from Week 3, on your own system, in front of "
         "you."),
        ("The hard questions expose retrieval, not reasoning",
         "Failures cluster on answers spread across sections, stated as exceptions, or held in "
         "tables. It did not reason badly — it never saw the right passage."),
        ("Over-reading is the most common wrong answer",
         "The claim is stronger than the quoted sentence supports. \"May\" becomes \"must\"; a "
         "specific case becomes a general rule."),
    ],
    notes="""
What almost always happens — and this holds whether or not you ran it yourself.

It answers at least one unanswerable question. Usually with something reasonable-sounding
drawn from general knowledge, sometimes with a hedge attached, occasionally with a citation
that doesn't exist. That is week three's mechanism, on a system you built, in front of you. If
that happened to you in the last twenty minutes, that's the most valuable thing that will
happen to you in this course.

The hard questions expose retrieval rather than reasoning. Failures cluster on answers spread
across sections, stated as exceptions, or held in tables. And the diagnosis matters: the model
didn't reason badly. It never saw the right passage. Those need completely different fixes —
one is a prompting problem, the other is a document-structure problem, and you'd waste a lot of
time treating one as the other.

And over-reading is the most common wrong answer. The claim is stronger than the sentence
supports. "May" becomes "must." A specific case becomes a general rule.

Go back and check yours for that specifically. It's easy to miss because the answer isn't
false, it's overstated.
""")

concepts_slide(
    prs,
    [
        ("The verification gap", None, "bold"),
        (1, "Generating is fast, checking is slow, and the gap widens as output quality rises.", None),
        ("Test set structure", None, "bold"),
        (1, "Seven answerable, graded easy/medium/hard, plus three plausible unanswerable ones. Expected answers written before running.", None),
        ("Why the unanswerable questions matter most", None, "bold"),
        (1, "They test behaviour when the system does not know — the situation you cannot detect in normal use.", None),
        ("Grading", None, "bold"),
        (1, "CORRECT · UNSUPPORTED · WRONG · REFUSED. Read the pattern, not the score.", None),
        ("Consistency is not correctness", None, "bold"),
        (1, "Repeating a question measures how common the pattern is, not whether it is true. Verification needs something outside the system.", None),
    ],
    notes="""
What's examinable from today, and this week is heavily represented on both exams.

The verification gap, including the counterintuitive part: it widens as output quality rises.
Expect to be asked why better models make checking harder.

Test set structure. Seven answerable graded by difficulty, three plausible unanswerable ones,
expected answers written before running. I may give you a proposed test set and ask what's
wrong with it — usually the unanswerable questions are absurd rather than plausible, or the
questions are too vague to grade.

Why the unanswerable ones matter most: they test behaviour in the situation you cannot detect
during normal use.

The four grades, and reading the pattern rather than the score.

And consistency is not correctness — with the reason. Repeating a question measures how common
a pattern is. Verification requires something outside the system. That is a near-certain exam
question.
""")

content_slide(
    prs, "Wrap-Up",
    [
        "Generating is fast; checking is slow; the gap grows as quality rises",
        "Test the system once, deliberately, instead of hoping to catch errors forever",
        ("Three unanswerable questions tell you more than seven answerable ones", None, "bold"),
        "Grade the pattern, not the score",
        "Asking twice is not checking — verification needs something outside the system",
        "",
        ("Next week:", None, "bold"),
        (1, "AI Agents and Workflow Automation — what happens when it acts without you watching", None),
    ],
    notes="""
Five things.

Generating is fast, checking is slow, and the gap grows as quality rises. Which is why this
skill matters more over time, not less.

Test the system once, deliberately, rather than hoping to catch errors forever. You will not
catch them forever. Nobody does.

Three unanswerable questions tell you more than seven answerable ones.

Grade the pattern, not the score.

And asking twice is not checking. Verification requires something outside the system.

Next week: agents and workflow automation. Today you tested a system where you saw every
answer. Next week we build something that runs several steps without you watching — and every
problem from today gets multiplied, because now the errors happen where nobody is looking.

If today made you slightly uncomfortable, next week is designed to make that productive.

Questions?
""")

closing_slide(
    prs,
    notes="""
Take questions here.

Common ones:

"Ten questions doesn't sound like much." — It isn't statistically. It's not meant to be. It's
enough to characterise the failure shape, which is what you need. Ten questions you actually
run beat a hundred you plan and don't.

"What if it passes everything?" — Then your unanswerable questions probably weren't plausible
enough, or too close to something in your documents. Make them harder and try again.

"Do I need to redo this when I change something?" — Yes, at least the three unanswerable ones.
That's why ten is the right number — small enough to rerun.

"Isn't this what professional evaluation does?" — It's a simplified version of it, and the
professional versions add scale and automation. The logic is the same, and the logic is the
part that transfers.
""")

save(prs, str(pathlib.Path(__file__).parent / "week08.pptx"))
