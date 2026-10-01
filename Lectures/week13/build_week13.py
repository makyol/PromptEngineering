#!/usr/bin/env python3
"""Week 13 — Ethics, Copyright, Academic Integrity and Responsible Use.

Build:  python3 build_week13.py
Output: week13.pptx
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "Theme"))
from theme import *  # noqa

prs = new_deck()

title_slide(
    prs, 13,
    "Ethics, Copyright and Responsible Use",
    "Including the rules for your own work",
    notes="""
Welcome back.

This session sits at the end of the course deliberately. Ethics taught in week two is abstract
— a list of concerns about a technology you haven't used. Ethics taught now attaches to things
you have actually built, tested and attacked.

Four things today. Where bias comes from, mechanically, so you can predict it rather than
deplore it. Copyright — who owns what, and what's genuinely unsettled. Academic integrity,
with the actual reasoning rather than a list of prohibitions. And over-reliance, which I think
is the most underrated risk in this entire course.

I want to say something about how I'll teach this. I'm not going to give you a code of conduct
to memorise. Codes go out of date and they don't help you with the case that isn't on the list.
What I want you to leave with is the ability to reason about a situation you haven't seen
before — because that's what you'll actually face.
""")

content_slide(
    prs, "Today: What We'll Explore",
    [
        "Where bias comes from, and why it is a reporting problem rather than an attitude problem",
        "Copyright: what is settled, what is contested, and what nobody knows yet",
        ("Academic integrity — the actual rules for this course, with reasons", None, "bold"),
        "Over-reliance and skill atrophy",
        "Activity: four cases, no devices needed",
    ],
    notes="""
Where we're going.

First, bias — where it comes from mechanically. I want to reframe this as a reporting problem
rather than an attitude problem, because that reframe is what makes it predictable.

Then copyright. What's settled, what's contested, and what genuinely nobody knows yet. I'll be
explicit about which is which, including where I have to tell you I don't know.

Then academic integrity, in bold, because it's what several of you have been waiting for. The
actual rules for this course, with the reasoning, so you can apply them to situations I haven't
anticipated.

Then over-reliance and skill atrophy. This is the one I think about most, and it's the one
that's least discussed.

Then four cases to discuss. No devices needed for any of it.
""")

# ═══════════════════════════════════════════════════════════════ part 1 — bias
section_slide(
    prs, 1, "Bias",
    notes="""
Part one. And I want to do this mechanically, because the mechanism makes it predictable.
""")

callout_slide(
    prs,
    "The system is not prejudiced. It is reporting the shape of what it read.",
    "Which is worse in one specific way: it will reproduce the pattern faithfully, fluently, and at scale.",
    notes="""
Start here, because the framing matters.

The system is not prejudiced. It has no attitudes, no beliefs, no intentions. It is reporting
the shape of what it read.

Go back to week two, to embeddings. Words that appear in similar contexts end up near each
other. If the text of the world consistently associates certain occupations with certain
genders, or certain neighbourhoods with certain outcomes, that association is recorded. Not
because anyone chose it — because it was there.

Now, why do I say this is worse in one specific way?

Because a prejudiced person can be argued with, is inconsistent, gets tired, and can be
overruled. A system reporting a pattern will reproduce it faithfully, fluently, and at scale —
identically, every time, for everyone, without any of the friction that human prejudice
generates.

There's no malice to appeal to and no conscience to engage. There's a distribution.

And that's precisely why "be unbiased" as an instruction does so little. You're asking a
reporting mechanism to have a different opinion. It doesn't have opinions.
""")

boxes_slide(
    prs, "Where You Will Actually Meet It",
    [
        ("Who is assumed",
         "Ask for \"a nurse\" or \"an engineer\" and note what comes back — names, pronouns, "
         "background. The default person in the output is the statistically frequent one in the "
         "text."),
        ("Whose norms are default",
         "Week 1's displacement, seen ethically. Advice, examples and assumptions default to the "
         "best-represented context — usually American, usually English-speaking, usually urban."),
        ("Whose language is served worse",
         "Week 3's tokenisation, seen ethically. Turkish costs more and performs worse. Speakers "
         "of less-represented languages get a measurably worse tool."),
    ],
    notes="""
Three places you'll actually meet it — and notice that all three are things you already learned
as technical facts. Today we look at them ethically.

Who is assumed. Ask for "a nurse" or "an engineer" and look at what comes back — names,
pronouns, implied background. The default person in the output is the statistically frequent
person in the text. Try it; it's a five-second experiment and it's more persuasive than
anything I can say.

Whose norms are default. This is week one's displacement failure, seen ethically. Advice,
examples and assumptions default to the best-represented context — usually American, usually
English-speaking, usually urban. When you asked about employment notice periods and got an
American answer, that was a technical failure. It's also a statement about whose working life
counts as the default case.

And whose language is served worse. This is week three's tokenisation, seen ethically. Turkish
costs more and performs worse. That's not a slight — it means speakers of less-represented
languages get a measurably worse tool, pay more for it, and are more likely to receive confident
wrong answers.

For a room in Turkey, that's not an abstract fairness question. It's your working conditions.
""")

# ══════════════════════════════════════════════════════════ part 2 — copyright
section_slide(
    prs, 2, "Copyright",
    notes="""
Part two. And I'm going to be careful to separate what's settled from what isn't.
""")

content_slide(
    prs, "What Is Reasonably Settled",
    [
        ("In the United States, purely machine-generated work is not copyrightable.", None, "bold"),
        (1, "The Copyright Office requires human authorship. This was upheld in Thaler v. Perlmutter.", None),
        (1, "Work with sufficient human creative contribution — selection, arrangement, substantial editing — can be protected", None),
        "",
        ("The United Kingdom is unusual.", None, "bold"),
        (1, "It has a provision for computer-generated works, assigning authorship to the person who made the arrangements for creation", None),
        "",
        (1, "Note that these are two developed jurisdictions reaching different answers. That should tell you how unsettled the area is.", None),
    ],
    notes="""
What's reasonably settled — and even "settled" is doing some work here.

In the United States, purely machine-generated work is not copyrightable. The Copyright Office
requires human authorship, and that position was upheld in Thaler v. Perlmutter. Work with
sufficient human creative contribution — selection, arrangement, substantial editing — can be
protected, but the protection attaches to the human contribution, not to the output as such.

The United Kingdom is unusual: it has a specific provision for computer-generated works, which
assigns authorship to the person who made the arrangements for the work's creation. That's a
genuinely different answer to the same question.

And the last line is the point I actually want you to take. Two developed jurisdictions, similar
legal traditions, opposite conclusions. That tells you how unsettled this area is — and it means
anyone who tells you confidently what the law is, globally, is overreaching.
""")

content_slide(
    prs, "What Is Contested, and What I Do Not Know",
    [
        ("Contested — being litigated now:", None, "bold"),
        (1, "Whether training on copyrighted material without permission is permitted. Major suits including NY Times v. OpenAI and Getty Images v. Stability AI.", None),
        (1, "Whether imitating a living artist's style is actionable, and whether it should be", None),
        "",
        ("What I do not know, and will not guess:", None, "bold"),
        (1, "How Turkish law treats AI-generated work, and how it will treat training data", None),
        (1, "If this matters for your work, ask a qualified lawyer in this jurisdiction. Do not ask a language model — see Week 1.", None),
    ],
    notes="""
What's contested, and then what I don't know.

Contested and being litigated right now: whether training on copyrighted material without
permission is permitted. Major suits including the New York Times against OpenAI and Getty
Images against Stability AI. These are live. The answers will matter enormously and they don't
exist yet.

Also contested: whether imitating a living artist's style is actionable, and separately whether
it should be. Those are different questions and it's worth keeping them apart — the legal
question and the ethical one can have different answers.

Now the second half, and I want to model something here.

I do not know how Turkish law treats AI-generated work, or how it will treat training data. I
could give you a plausible-sounding answer. I'm not going to, because I'd be doing exactly what
this course spends fourteen weeks warning you about — producing fluent, confident content in an
area of thin coverage.

If this matters for your work, ask a qualified lawyer in this jurisdiction. Do not ask a
language model, for the reason you learned in week one and understood mechanically in week
three.

Me saying "I don't know" here is the lesson, not a gap in it.
""")

content_slide(
    prs, "Practical Rules That Do Not Depend on the Outcome",
    [
        (1, "Do not ask for reproduction of specific copyrighted text. Ask for analysis, summary or transformation.", None),
        (1, "Do not upload material you do not have the right to share — that is a separate question from copyright in the output", None),
        (1, "Check whether your institution or publisher requires disclosure of AI assistance. Many now do.", None),
        (1, "Keep a record of what was generated and what you wrote. You may need to demonstrate your own contribution.", None),
        "",
        ("That last one protects you, whichever way the law settles.", None, "bold"),
    ],
    notes="""
Four rules that hold regardless of how the litigation resolves. This is how to act under
uncertainty, which is the actual skill.

Don't ask for reproduction of specific copyrighted text. Ask for analysis, summary, or
transformation. That's on safer ground in essentially every jurisdiction.

Don't upload material you don't have the right to share. And note that this is a *separate*
question from who owns the output — people conflate them constantly. Uploading a confidential
document is a problem even if nobody ever claims copyright in what comes back.

Check whether your institution or publisher requires disclosure of AI assistance. Many now do,
and the requirements are changing quickly. Check per journal, per institution, per year.

And keep a record of what was generated and what you wrote.

That last one, in bold, protects you whichever way the law settles. If protection depends on
demonstrating human creative contribution, then evidence of your contribution is exactly what
you'll need. And if a dispute arises about authorship, the person with contemporaneous records
is in a very different position from the person reconstructing events afterwards.

It costs nothing to keep drafts. Keep drafts.
""")

# ══════════════════════════════════════════════════ part 3 — academic integrity
section_slide(
    prs, 3, "Academic Integrity",
    notes="""
Part three. The rules for this course, with reasons.
""")

content_slide(
    prs, "The Rule, and Why",
    [
        ("The rule: using it and telling me is fine. Using it and hiding it is not.", None, "bold"),
        "",
        ("The reason is not that AI is cheating. It is that assessment measures something.", None, "bold"),
        (1, "If I set a task to find out whether you can do X, and a tool does X, I have measured nothing", None),
        (1, "The problem is the broken measurement, not the tool", None),
        "",
        (1, "Which is why the rules differ by task: for the in-class builds, using AI is the entire point", None),
        (1, "And why the exams are written and in person — that is the only way to measure what they measure", None),
    ],
    notes="""
The rule first. Using it and telling me is fine. Using it and hiding it is not. That's been the
rule since week one and it hasn't changed.

Now the reason, because I want you to be able to apply this elsewhere.

The reason is not that AI is cheating. It's that assessment measures something. If I set a task
to find out whether you can do X, and a tool does X for you, I have measured nothing. I now
have a grade that means nothing, which harms you more than it harms me — because the grade is
supposed to be evidence about you, and now it isn't.

The problem is the broken measurement, not the tool.

And once you see it that way, the variation makes sense. For the in-class builds, using AI is
the entire point — I'm measuring whether you can design and evaluate an AI workflow, so of
course you use AI. Using it there isn't a loophole; it's the task.

And the exams are written and in person, because that's the only way to measure what they're
meant to measure — whether *you* can recognise an over-read answer, whether *you* can name the
failure mode.

Same principle. Different application. That's what I want you to be able to do in other courses
and in professional life, where nobody will have written the rule down for you.
""")

boxes_slide(
    prs, "Applying It Elsewhere",
    [
        ("Ask what is being measured",
         "A language course measuring your language: using a translator defeats it. A "
         "content course where you write in a second language: check, because the "
         "measurement may not be the language."),
        ("Ask what you are certifying",
         "Submitting work asserts it is yours. A literature review with citations you never "
         "checked is a false claim about your own diligence — regardless of whether AI was "
         "involved."),
        ("When unsure, disclose",
         "Disclosure almost never causes a problem. Non-disclosure that surfaces later always "
         "does. The asymmetry is enormous and it points one way."),
    ],
    notes="""
Three questions for situations nobody has written a rule for.

Ask what is being measured. A language course measuring your command of the language — using a
translator defeats the measurement entirely. A content course where you happen to be writing in
a second language — the measurement may be the content, not the language, in which case
language help may be fine. Check, don't assume, and note that these two situations look
identical from the outside.

Ask what you are certifying. This one generalises furthest. Submitting work asserts that it's
yours. A literature review with twenty citations you never opened is a false claim about your
own diligence — and notice that's true whether or not AI was involved. The AI just made it
faster to do something that was always dishonest.

And when unsure, disclose. Look at the asymmetry: disclosure almost never causes a problem.
Non-disclosure that surfaces later always does. Those two facts point in the same direction and
it isn't close.

If you find yourself calculating whether you'd get caught, you've already answered the question
— you're reasoning about detection rather than about whether it's right.
""")

# ═══════════════════════════════════════════════════════ part 4 — over-reliance
section_slide(
    prs, 4, "Over-Reliance",
    notes="""
Part four. The one I think about most.
""")

content_slide(
    prs, "The Risk Nobody Talks About",
    [
        "Automation bias: people accept a system's output more readily than a colleague's, and check it less",
        (1, "It arrives instantly, confidently, and without visible effort — all of which read as competence", None),
        (1, "And it is usually right, which trains you to stop checking", None),
        "",
        ("The second-order problem:", None, "bold"),
        (1, "The judgment that lets you catch errors is built by doing the work yourself", None),
        (1, "If you never draft, you may lose the ability to tell a good draft from a plausible one", None),
        "",
        (1, "This is not an argument against using these tools. It is an argument for keeping a practice that maintains the skill.", None),
    ],
    notes="""
Automation bias. People accept a system's output more readily than a colleague's, and check it
less.

Why? It arrives instantly, confidently, and without visible effort — and all three of those
read as competence to us. If a colleague produced a forty-page analysis in nine seconds, you'd
be suspicious. When software does it, you're impressed.

And it's usually right, which trains you to stop checking. That's the trap, and it's a trap
built out of the system working well. Twenty good answers teach you that checking is a waste of
time, and then the twenty-first is wrong.

Now the second-order problem, which is the one that actually worries me.

The judgment that lets you catch errors is built by doing the work yourself. You can spot a bad
discharge summary because you've written a hundred. You can feel that an argument is weak
because you've constructed weak ones and had them taken apart.

If you never draft, you may lose — or never develop — the ability to tell a good draft from a
merely plausible one. And that's the exact capability this whole course is trying to build in
you.

Last line, and I mean it: this is not an argument against using these tools. It's an argument
for keeping a practice that maintains the skill.
""")

boxes_slide(
    prs, "Keeping the Skill",
    [
        ("Draft first sometimes",
         "Not always. But if you never produce a first version yourself, you lose the "
         "comparison that tells you whether the generated one is good."),
        ("Predict before you read",
         "Say what you expect the answer to be, then look. Cheap, fast, and it keeps your "
         "own judgment engaged rather than dormant."),
        ("Keep one thing you do unaided",
         "Choose the skill most central to your profession and protect it deliberately. "
         "Use the tools everywhere else."),
    ],
    notes="""
Three practices. These are personal rather than institutional, and I offer them as someone who
uses these tools daily.

Draft first sometimes. Not always — that would waste the tool. But if you never produce a first
version yourself, you lose the comparison that tells you whether the generated one is any good.
You can't evaluate against a standard you no longer have.

Predict before you read. Before you look at the output, say what you expect the answer to be.
Then look. It takes three seconds, and it keeps your judgment engaged rather than dormant — and
it makes disagreements visible, which is when you actually learn something.

And keep one thing you do unaided. Choose the skill most central to your profession and protect
it deliberately. For a clinician that might be the differential. For a lawyer, constructing the
argument. For a teacher, designing the assessment. Use the tools everywhere else, freely.

That's not asceticism. It's the same logic as the four levers — deciding deliberately rather
than by default. The default is that you use it for everything and notice the loss in five
years.
""")

# ═══════════════════════════════════════════════════════════════ activity
section_slide(
    prs, 5, "Four Cases",
    notes="""
Part five. No devices needed. These work as discussion or as a thinking exercise.
""")

activity_slide(
    prs, "Four Cases",
    [
        ("For each: what is the problem, and what would you do?", None, "bold"),
        "",
        ("A.", None, "bold"),
        (1, "A colleague pastes a patient's full history into a public chat tool to draft a referral. It works well. They do it weekly.", None),
        ("B.", None, "bold"),
        (1, "A student submits an essay with fifteen citations. Twelve exist. Three do not. They say they did not know.", None),
        ("C.", None, "bold"),
        (1, "A department automates first-round application screening. Nobody has checked which applicants it rejects.", None),
        ("D.", None, "bold"),
        (1, "You generate a course handout. It is excellent. A colleague asks if you wrote it.", None),
    ],
    minutes=15,
    notes="""
Fifteen minutes. Four cases. For each: what's the problem, and what would you do?

Case A. A colleague pastes a patient's full history into a public chat tool to draft a referral.
It works well. They do it weekly.

Case B. A student submits an essay with fifteen citations. Twelve exist. Three don't. They say
they didn't know.

Case C. A department automates first-round application screening. Nobody has checked which
applicants it rejects.

Case D. You generate a course handout. It's excellent. A colleague asks if you wrote it.

Think about them, or discuss them with the person next to you. I'll walk through all four
either way.

[If the room is willing, take one case at a time and hear a couple of views before giving the
analysis. If it's quiet, go straight to the next slide — it has the analysis. Case D is
deliberately the mildest and usually produces the most disagreement, so it's a good one to end
on.]
""")

content_slide(
    prs, "The Cases, Discussed",
    [
        ("A — the patient history.", None, "bold"),
        (1, "Not a grey area. Data leaves the institution; the terms were never checked; \"it works well\" is not a safeguard. Raise it, kindly and promptly.", None),
        ("B — the three citations.", None, "bold"),
        (1, "\"I did not know\" may well be true and is not exculpatory. Submitting the work certified they were real. The dishonesty is in the unchecked claim.", None),
        ("C — the screening.", None, "bold"),
        (1, "The failure is not automation — it is the absence of anyone examining the rejections. An unexamined system encodes whatever pattern it found.", None),
        ("D — the handout.", None, "bold"),
        (1, "The mildest case and the one worth being straightforward about. \"I generated it and edited it.\" Nothing is lost by saying so.", None),
    ],
    notes="""
Let's take them.

A, the patient history. Not a grey area, and I'd want you clear about that. Data leaves the
institution. The terms were never checked. "It works well" is not a safeguard — it's the reason
they'll keep doing it. Raise it, kindly and promptly, because your colleague is exposed and
probably hasn't thought about it. Kindly matters; people respond badly to being accused and
well to being warned.

B, the three citations. "I didn't know" may well be true, and it isn't exculpatory. Submitting
the work certified they were real. That's the point from earlier — the dishonesty lives in the
unchecked claim, not in the tool. And note this is a week one failure, fabrication, arriving
with real consequences.

C, the screening. The failure is not automation. It's that nobody has examined the rejections.
An unexamined system encodes whatever pattern it found in whatever data it was given, and
applies it identically to everyone, forever. The fix isn't necessarily to stop — it's to look at
who is being rejected and why. That's week eight, applied to a decision about people's lives.

D, the handout. The mildest case, and the one worth being straightforward about. "I generated
it and edited it." Nothing is lost by saying so. And the fact that this feels slightly
uncomfortable is worth noticing — that discomfort is exactly the thing that grows into
non-disclosure if you don't address it early.
""")

content_slide(
    prs, "Wrap-Up",
    [
        "Bias is a reporting problem, not an attitude problem — which makes it predictable",
        "Copyright is genuinely unsettled; keep records of your own contribution regardless",
        ("Integrity is about what is being measured and what you are certifying", None, "bold"),
        "Over-reliance erodes the judgment that lets you catch errors — protect one skill deliberately",
        "When unsure, disclose. The asymmetry points one way.",
        "",
        ("Next week:", None, "bold"),
        (1, "Synthesis and Course Wrap-Up", None),
    ],
    notes="""
Five things.

Bias is a reporting problem rather than an attitude problem — and that framing makes it
predictable, which is what lets you design around it.

Copyright is genuinely unsettled. Keep records of your own contribution regardless of how it
resolves.

Integrity is about what's being measured and what you're certifying. Those two questions will
serve you in situations no rule covers.

Over-reliance erodes the judgment that lets you catch errors. Protect one skill deliberately.

And when unsure, disclose.

Next week is the last session. We'll pull the whole course together — the failure taxonomy, the
artifacts, the through-line — and I'll tell you exactly what the final covers.

Questions?
""")

closing_slide(
    prs,
    notes="""
Take questions here.

Common ones:

"Can I use AI to write my thesis?" — Depends on your institution's rules and your supervisor,
and both are changing. Ask explicitly and get the answer in writing. Never assume from silence.

"What if my supervisor says no but everyone does it?" — Then the answer is no, and "everyone
does it" is the reasoning that ends careers rather than protecting them.

"Is it unethical to use it at all, given the training data disputes?" — A reasonable position
that reasonable people hold. It's also unresolved. I'd say: form a view, be able to defend it,
and don't pretend the question isn't there.

"Do you use it?" — Yes, daily, including in preparing this course. Which I'm telling you
because it would be strange to teach disclosure and not practise it.
""")

save(prs, str(pathlib.Path(__file__).parent / "week13.pptx"))
