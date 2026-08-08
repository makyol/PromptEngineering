#!/usr/bin/env python3
"""Week 6 — Building Your First Tool Without Code.  Artifact: Micro-Tool.

Build:  python3 build_week06.py
Output: week06.pptx
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "Theme"))
from theme import *  # noqa

prs = new_deck()

title_slide(
    prs, 6,
    "Building Your First Tool Without Code",
    "Artifact: the Micro-Tool",
    notes="""
Welcome back. Today the course changes shape.

For five weeks we've built a foundation. You know what tokens are, why hallucination
happens, what the four levers are, how to specify register. Today you start using it, and
from now until week thirteen every session has the same structure: I show you something
working, we take it apart and find where it breaks, and then you build a smaller version.

Today you will build a tool. Something that runs in a browser, that you can send someone a
link to, that does one useful job in your field. Without writing code.

I want to name what usually happens in this session. Some of you have never programmed and
assume this is beyond you. It isn't, and you'll have something working within about twenty
minutes. Others have programmed and will be slightly offended by how this works. Both
reactions are fine.

The thing I actually want you to leave with isn't the tool. It's an understanding of what
you can and cannot trust about something you built but cannot read.
""")

content_slide(
    prs, "Today: What We'll Explore",
    [
        "Demonstration: a working tool, built from a description",
        "What is actually happening underneath — and why that matters to you",
        "What makes a good Micro-Tool: one job, one screen",
        ("Where it breaks — and the specific danger of code you cannot read", None, "bold"),
        "Build: your own Micro-Tool",
        "Concepts you must be able to define and diagnose",
    ],
    notes="""
The shape of every build session from now on.

First, a demonstration. I show you a finished thing working. About ten minutes.

Then we unpack it — what's actually happening underneath, and why that matters to you as
someone who will rely on the output.

Then what makes a good one. There's a shape to this, and getting the shape right is most of
the skill.

Then where it breaks. Every build week has this section and it's the most important part.
Today's version is specific and serious: what does it mean to use software you built but
cannot read?

Then you build. Twenty minutes.

And then a slide naming exactly what's examinable from today, because I said I'd do that
every build week and I will.
""")

# ═════════════════════════════════════════════════════════════ part 1 — demo
section_slide(
    prs, 1, "Demonstration",
    notes="""
Part one. Let me show you rather than describe.
""")

content_slide(
    prs, "What I Am About to Build, Live",
    [
        ("The description I will type:", None, "bold"),
        (1, "\"Build a single-page tool for clinic reception staff. Two inputs: appointment date, and patient's preferred language. It produces a reminder message in that language, with the date written out in full. Three language options: Turkish, English, Arabic. Add a copy button.\"", None),
        "",
        ("That is the entire input. No code, no setup, no account beyond a free login.", None, "bold"),
        "",
        (1, "Watch for two things: how long it takes, and how much I did not have to specify.", None),
    ],
    notes="""
Here's what I'm going to type. Read it while I set up.

"Build a single-page tool for clinic reception staff. Two inputs: appointment date, and
patient's preferred language. It produces a reminder message in that language, with the date
written out in full. Three language options: Turkish, English, Arabic. Add a copy button."

That's the whole input. No code, no setup, no account beyond a free login.

Watch for two things while I do this.

First, how long it takes. It'll be somewhere between thirty seconds and two minutes.

Second — and this is the more interesting one — how much I did not have to specify. I didn't
say what the page should look like. I didn't say what a date input is. I didn't say how the
copy button should behave, or what should happen when you click it. All of that arrives
anyway, because those are conventions and conventions are exactly what a system trained on
enormous amounts of existing code has learned.

[Run it live. If the tool is unavailable, use the fallback on the next slide, or describe
the result from the slide after — the session does not depend on this working.]
""")

boxes_slide(
    prs, "Tools You Can Use Today",
    [
        ("Chat assistants that render code",
         "Several major assistants will produce a working interactive page inside the chat and "
         "let you share it. Usually the fastest route, and no separate account is needed if you "
         "already have one."),
        ("Dedicated prompt-to-app builders",
         "Browser-based services that turn a description into a running web app and give you a "
         "URL. Free tiers exist and are generous enough for classroom use."),
        ("If everything fails",
         "Use my finished version — the link is on the board. Every step today can be done "
         "against a tool that already exists, and the thinking is the point."),
    ],
    notes="""
Three routes, and you should use whichever loads.

Route one: a chat assistant that renders code. Several of the major assistants will produce
a working interactive page inside the conversation and let you share it. Usually fastest, and
if you already have an account you need nothing new.

Route two: a dedicated prompt-to-app builder. Browser-based services that take a description
and give you a running web app with a URL. Free tiers exist and are generous enough for what
we're doing.

I'm deliberately not putting product names on this slide, and I want to explain why rather
than have you think I forgot. These services change constantly — names, free tiers, limits.
I'll give you two or three current ones verbally now, and if one has changed by the time you
read these slides back, the category is still correct. That's the difference between learning
a concept and learning a product.

Route three: if everything fails, use my finished version. The link's on the board. Nothing
today depends on your particular tool working — the thinking is the point, and you can do all
of it against a tool that already exists.
""")

# ═══════════════════════════════════════════════════════════ part 2 — unpack
section_slide(
    prs, 2, "What Is Actually Happening",
    notes="""
Part two. Let's take it apart, because what happened is not what it looks like.
""")

flow_slide(
    prs, "It Wrote Code. You Did Not Read It.",
    [
        ("Your description", "Ordinary language describing what the tool should do."),
        ("Generated code", "The model predicts code — the same next-token operation from Week 3."),
        ("It runs", "The browser executes it. You see a working interface."),
        ("You judge the surface", "You can see whether it looks right. You cannot see whether it is right."),
    ],
    caption="Nothing new is happening. This is next-token prediction, where the tokens happen to be code.",
    notes="""
Here's what happened, and I want to be precise because the magic wears off usefully.

You wrote a description. The model predicted code — and I want to stress the word predicted.
This is exactly the operation from week three. Same mechanism. The tokens happen to be code
instead of prose, and code is unusually well-suited to it because code is highly patterned and
there is an enormous amount of it publicly available.

The browser ran that code. You saw a working interface.

And then the fourth box, which is where the whole session turns: you judged the surface. You
could see whether it looked right. You could not see whether it was right.

Read the caption. Nothing new is happening here. This is next-token prediction where the
tokens are code. Which means everything you learned in week three applies — including that
there's no step where it checks whether what it produced is correct.

The difference is that with prose, you can read the output and judge it. With code, most of
you cannot. That gap is what makes this week both powerful and dangerous.
""")

content_slide(
    prs, "Why This Works So Well",
    [
        "Code is a good fit for next-token prediction:",
        (1, "It is highly patterned — far more regular than natural language", None),
        (1, "There is an enormous amount of it publicly available to learn from", None),
        (1, "Common tasks — a form, a button, a date picker — appear thousands of times in near-identical form", None),
        "",
        ("So the more ordinary your tool, the better this goes.", None, "bold"),
        (1, "A form that formats text: extremely well-trodden. Expect it to work.", None),
        (1, "Something genuinely unusual: much thinner ground, and the same confident delivery", None),
    ],
    notes="""
Why does this work so well? Three reasons, and they should sound familiar.

Code is highly patterned — far more regular than natural language. There are conventions,
and violating them tends to break things, so the training material is unusually consistent.

There's an enormous amount of it publicly available.

And common tasks — a form, a button, a date picker, a copy-to-clipboard — appear thousands of
times in nearly identical form.

So the bold line: the more ordinary your tool, the better this goes.

A form that takes some input and formats text? Extremely well-trodden ground. Expect it to
work, first time, and it usually will.

Something genuinely unusual — an unusual calculation, an unusual workflow, something specific
to your institution? Much thinner ground. And here's the part to hold onto: the delivery is
identical. It will produce something that looks equally finished, equally confident, with the
same clean interface.

That's thin coverage from week three, showing up in a new form. The confidence doesn't drop
when the ground gets thin. It never does.
""")

content_slide(
    prs, "What Makes a Good Micro-Tool",
    [
        ("One job.", None, "bold"),
        (1, "Not \"a system for managing appointments\" — \"turn an appointment into a reminder message\"", None),
        ("One screen.", None, "bold"),
        (1, "No login, no saved data, no pages to navigate between. Input at the top, output below.", None),
        ("A job that is annoying rather than difficult.", None, "bold"),
        (1, "The best candidates are small, repetitive, and currently done by hand", None),
        "",
        ("Good candidates from your fields:", None, "bold"),
        (1, "A referral letter formatter · a citation checker checklist · a rubric scorer · a unit converter for your lab · a consent-form readability checker", None),
    ],
    notes="""
Three rules for what to build, and they matter more than the tool you use.

One job. Not "a system for managing appointments" — that's a project, and it will produce
something that looks impressive and works badly. "Turn an appointment into a reminder
message" is a job.

One screen. No login, no saved data, no navigating between pages. Input at the top, output
below. The moment you need to store something between visits, you've left the territory where
this works reliably.

And a job that is annoying rather than difficult. This is the one people get wrong. The best
candidates are small, repetitive things currently done by hand — not the hardest problem in
your field. If it's intellectually hard, you want a conversation with a model, not a tool. If
it's tedious and you do it forty times a week, that's a Micro-Tool.

Some candidates from your fields, on the slide. A referral letter formatter. A checklist for
checking citations. A rubric scorer for marking. A unit converter for your particular lab. A
consent-form readability checker — which, after last week, several of you could specify very
precisely.

Pick something you actually do. It makes the next twenty minutes much better.
""")

# ═════════════════════════════════════════════════════════ part 3 — where it breaks
boxes_slide(
    prs, "Candidates From Your Fields",
    [
        ("Healthcare · Education",
         "A dosage-schedule formatter that turns a prescription into a printable timetable. "
         "A rubric scorer that takes marks and produces standard feedback text. "
         "A reading-level checker for patient information."),
        ("Law · Business",
         "A clause checklist that confirms a draft contains your standard sections. "
         "A citation formatter. A meeting-note structurer that sorts free text into decisions, "
         "actions and open questions."),
        ("Engineering · Any field",
         "A unit converter for the specific quantities your lab uses. A checklist generator for a "
         "recurring procedure. A form that turns five fields into a correctly worded standard "
         "message."),
    ],
    notes="""
Concrete candidates, so nobody spends five of their twenty minutes deciding what to build.

Healthcare and education. A dosage-schedule formatter — take a prescription, produce a printable
timetable a patient can put on the fridge. A rubric scorer that takes your marks and produces
standard feedback text. A reading-level checker for patient information, which several of you
could specify very precisely after last week.

Law and business. A clause checklist that confirms a draft contains your standard sections. A
citation formatter. A meeting-note structurer that takes free text and sorts it into decisions,
actions and open questions.

Engineering and anything else. A unit converter for the specific quantities your lab actually
uses — not a general one, yours, with your units and your precision. A checklist generator for a
recurring procedure. A form that turns five fields into a correctly worded standard message.

Look at what all nine have in common. Every one is boring. Every one is something a person
currently does by hand, repeatedly, slightly differently each time. None of them require judgment.

That's the target. If your idea sounds impressive, it's probably too big.
""")

content_slide(
    prs, "When the First Attempt Is Wrong",
    [
        ("Describe the behaviour you want, not the code you imagine.", None, "bold"),
        (1, "\"The date should show as 15 March 2027, not 2027-03-15\" — not \"change the date format function\"", None),
        ("Give a concrete failing example.", None, "bold"),
        (1, "\"When I enter a name with an apostrophe, the output is blank. It should show the name.\"", None),
        ("Change one thing at a time.", None, "bold"),
        (1, "Same reason as Week 4 — otherwise you cannot tell which change fixed it, or what it broke.", None),
        ("Re-test what already worked.", None, "bold"),
        (1, "You cannot see what a change affected. This is the compensation for not reading the code.", None),
    ],
    notes="""
When the first attempt is wrong — and it often is, in a small way — here's how to fix it without
making things worse.

Describe the behaviour you want, not the code you imagine. Say "the date should show as fifteenth
of March twenty twenty-seven, not two-thousand-twenty-seven dash oh-three dash fifteen." Don't say
"change the date format function," because you're guessing at an internal structure you can't see,
and if you guess wrong the instruction is worse than useless.

Give a concrete failing example. "When I enter a name with an apostrophe, the output is blank. It
should show the name." That's a test case and a specification in one sentence, and it's far more
effective than "it doesn't handle special characters properly."

Change one thing at a time. Same reason as week four — otherwise you can't tell which change fixed
it, and you certainly can't tell what it broke.

And re-test what already worked. You cannot see what a change affected. When you can read code,
you can look at the blast radius. You can't, so re-testing is the compensation. It isn't optional
and it isn't paranoia — it's the price of the trade you made.
""")

section_slide(
    prs, 3, "Where It Breaks",
    notes="""
Part three. Every build week has this section, and today's is serious.
""")

callout_slide(
    prs,
    "You can see whether it looks right. You cannot see whether it is right.",
    "This is the same gap as Week 1 — but now the fluent, confident, wrong thing is software.",
    notes="""
Here's the danger, stated plainly.

You can see whether it looks right. You cannot see whether it is right.

And I want you to notice that this is exactly the gap from week one. A fluent, confident,
professional-looking output that may or may not be correct, produced by a system with no
mechanism for checking.

The only thing that's changed is the medium. In week one it was prose, and at least you could
read prose. Now it's software, and most of you cannot read it. So the one defence you had —
your own judgment applied to the output — is gone.

The interface looks finished. The buttons work. It produces an answer. Everything your eye
uses to judge quality is present and correct, and none of it tells you whether the logic is
right.

That's why the next slide exists, and it's the most important slide in today's session.
""")

boxes_slide(
    prs, "Three Ways a Micro-Tool Fails Quietly",
    [
        ("Wrong logic, right appearance",
         "A calculation that is subtly wrong — a rounding rule, an off-by-one in a date, the "
         "wrong threshold. The interface looks perfect. The number is wrong every single time, "
         "consistently, which makes it look reliable."),
        ("Correct for the cases you tried",
         "You tested it with typical input. Nobody tested the empty field, the very long name, "
         "the date in the past, the unusual character. Those paths were generated too — they "
         "were just never run."),
        ("Silently discarded input",
         "It accepts something, appears to process it, and quietly ignores part of it. The most "
         "dangerous failure, because there is no error and no gap in the output."),
    ],
    notes="""
Three ways this fails, and none of them announce themselves.

Wrong logic, right appearance. A calculation that's subtly wrong — a rounding rule, an
off-by-one error in a date, the wrong threshold in a comparison. The interface is perfect. The
number is wrong. And note the cruel detail: it's wrong *consistently*, every time, which is
exactly the behaviour we associate with reliability. A tool that failed randomly would get
caught. One that's steadily wrong looks trustworthy.

Correct for the cases you tried. You tested it with typical input, because that's what comes
to mind. Nobody tested the empty field, the very long name, the date in the past, the name
with an apostrophe, the Turkish characters. Those paths were generated too — they were simply
never run. The code exists; nobody knows what it does.

And silently discarded input. It accepts something, appears to process it, and quietly ignores
part of it. This is the worst one, because there's no error message and no visible gap. The
output is complete and confident and missing something.

Notice that all three are the same shape as the failures from week one. Wrong content in a
right-looking container.
""")

content_slide(
    prs, "How to Use One Responsibly",
    [
        ("Test the edges before you trust it, not after.", None, "bold"),
        (1, "Empty input. Very long input. Turkish characters. A date in the past. A number where text is expected.", None),
        ("Check a case where you already know the answer.", None, "bold"),
        (1, "Run something you have done by hand. If it disagrees with you, you learn something either way.", None),
        ("Keep it advisory.", None, "bold"),
        (1, "It drafts, formats, checks, reminds. A person decides. Never let it be the final step before something reaches a patient or client.", None),
        ("Do not put real personal data into it.", None, "bold"),
        (1, "You do not know where the input goes. That is Week 12, and it applies from today.", None),
    ],
    notes="""
Four rules. These are the professional practice, and they're what I'd actually want you doing
in six months.

Test the edges before you trust it, not after. Empty input. Very long input. Turkish
characters — genuinely, test these, because a lot of generated code assumes English text and
breaks on them. A date in the past. A number where text was expected. Five minutes of this
tells you more than an hour of using it normally.

Check a case where you already know the answer. Run something you've done by hand. If it
agrees, you've gained confidence. If it disagrees, you've learned something important — and
notice you learn either way, which makes this the highest-value five minutes available.

Keep it advisory. It drafts, formats, checks, reminds. A person decides. Never let a
Micro-Tool be the final step before something reaches a patient or a client. Not because it's
bad — because you cannot verify it, and unverifiable things need a human between them and
consequences.

And don't put real personal data into it. You don't know where the input goes, who hosts it,
or what's logged. That's week twelve, and it applies from today.
""")

# ══════════════════════════════════════════════════════════════ build
section_slide(
    prs, 4, "Build",
    notes="""
Part four. Your turn. Twenty minutes.
""")

activity_slide(
    prs, "Build Your Micro-Tool",
    [
        ("1.  Pick one annoying, repetitive job from your own field.", None, "bold"),
        (1, "Small. Something you or someone you know does by hand, often.", None),
        ("2.  Write the description using Week 4's four levers.", None, "bold"),
        (1, "Context: who uses it. Task: what it does. Format: what the output looks like. Example: a sample output if useful.", None),
        ("3.  Generate it. Then immediately try to break it.", None, "bold"),
        (1, "Empty input. Turkish characters. Something absurd. Note what happens.", None),
        ("4.  Write one sentence: what would you have to check before letting anyone else use this?", None, "bold"),
    ],
    minutes=20,
    notes="""
Twenty minutes. Four steps.

One. Pick one annoying, repetitive job from your own field. Small. Something you or someone
you know does by hand, often. Resist the urge to pick the most impressive thing you can think
of — pick the most boring one.

Two. Write the description using the four levers from week four. Context: who uses this and
in what situation. Task: what it does, specific verb and scope. Format: what the output looks
like. And an example output if it helps.

Three. Generate it — and then immediately try to break it. Empty input. Turkish characters.
Something absurd. Note what happens. Don't skip this because the first version worked; the
breaking is where the learning is.

Four. Write one sentence: what would you have to check before letting anyone else use this?
That sentence is the actual deliverable of today's session. Keep it.

[Circulate. Common problems: too ambitious a scope — tell them to cut it in half; and
forgetting to test the edges — remind them at the ten-minute mark. If nobody is building, work
through step two aloud for one example from each discipline present.]
""")

content_slide(
    prs, "What You Probably Found",
    [
        (1, "It worked, and faster than expected. That is the normal outcome — it is not luck.", None),
        (1, "It broke on empty input, or handled it in a way nobody would have chosen deliberately", None),
        (1, "Turkish characters caused a problem somewhere — very common", None),
        (1, "Asking for a change worked, but occasionally broke something that had been working", None),
        "",
        ("That last one is worth naming: you cannot see what a change affected.", None, "bold"),
        (1, "When you ask for a modification, re-test the things that already worked. Every time.", None),
    ],
    notes="""
Whether or not you built one, here's what typically happens.

It worked, and faster than expected. That's the normal outcome and it isn't luck — it's the
well-trodden-ground effect we discussed. Don't over-update on it.

It broke on empty input, or handled it in a way nobody would have deliberately chosen.

Turkish characters caused a problem somewhere. Very common, and worth remembering as a
systematic issue rather than bad luck — a lot of generated code carries assumptions from
predominantly English source material.

And asking for a change worked, but occasionally broke something that had been working
before.

That last one deserves its own name, in bold: you cannot see what a change affected. When you
modify code you can read, you can see the blast radius. When you ask for a modification in
plain language, you can't. Something three screens away may have changed.

So: when you ask for a change, re-test the things that already worked. Every time. That's not
paranoia, it's the only compensation available for not being able to read the thing.
""")

concepts_slide(
    prs,
    [
        ("Micro-Tool", None, "bold"),
        (1, "A single-purpose, single-screen tool generated from a description. One job, one screen, no stored data.", None),
        ("Why generated code is well predicted", None, "bold"),
        (1, "Code is highly patterned, abundantly available, and common tasks recur in near-identical form.", None),
        ("The verification gap", None, "bold"),
        (1, "You can judge the appearance of a generated tool; you cannot judge its logic. The surface is not evidence.", None),
        ("Three quiet failures", None, "bold"),
        (1, "Wrong logic with right appearance · correct only for the cases tried · silently discarded input.", None),
        ("Responsible use", None, "bold"),
        (1, "Test edges first · check a known answer · keep it advisory · no real personal data.", None),
    ],
    notes="""
This is the slide that connects today to your exam, and I'll do one of these every build week.

Five things you must be able to define and diagnose.

What a Micro-Tool is: single-purpose, single-screen, generated from a description, no stored
data.

Why generated code is well predicted: it's highly patterned, abundantly available, and common
tasks recur almost identically. If an exam question asks why these tools succeed at ordinary
software and struggle with unusual requirements, that's the answer.

The verification gap. You can judge appearance; you cannot judge logic. The surface is not
evidence. Learn that sentence.

The three quiet failures, by name: wrong logic with right appearance; correct only for the
cases tried; silently discarded input. I will give you a scenario and ask you which one it is.

And responsible use: test edges first, check a known answer, keep it advisory, no real
personal data.

Photograph this slide.
""")

content_slide(
    prs, "Wrap-Up",
    [
        "You can build working software from a description — and it usually works",
        "It is next-token prediction where the tokens are code. Week 3 still applies.",
        ("The surface is not evidence. Looking right and being right are different properties.", None, "bold"),
        "Test the edges, check a known case, keep it advisory",
        "",
        ("Next week:", None, "bold"),
        (1, "Grounding AI in Your Own Sources — how to make it answer from documents you trust, and check that it did", None),
    ],
    notes="""
Four things.

You can build working software from a description, without writing code, and it usually
works. That's genuinely new and genuinely useful, and I don't want to be sour about it.

But it's next-token prediction where the tokens happen to be code. Everything from week three
still applies, including that nothing checks correctness.

The surface is not evidence. Looking right and being right are different properties, and this
week they came apart more completely than anywhere else in the course, because you can't read
the thing you made.

So: test the edges, check a known case, keep it advisory.

Next week, grounding. Today's tool works from what the model already knows. Next week we point
one at documents you choose — a guideline, a statute, a syllabus — so it answers from your
sources rather than from memory. And then we check whether it actually did, which turns out to
be the hard part.

Bring documents if you have some. I'll provide packs if you don't.

Questions?
""")

closing_slide(
    prs,
    notes="""
Take questions here.

Common ones:

"Can I use this for real work?" — For drafting and formatting, yes, with the four rules.
For anything where a wrong answer reaches a patient or client without a human in between, no.

"Do I need to learn to code now?" — No. But notice what you gained by not being able to read
it: a permanent dependence on testing rather than inspection. That's a real trade, and it's
worth knowing you made it.

"What if my tool stops working later?" — Common with free tiers and hosted services. Keep the
description you used. Regenerating from the description is cheap; recovering a tool you can't
read isn't.

"Can it build something bigger?" — It can appear to. The failure modes get much harder to spot
as scope grows, and you have no way to inspect. That's exactly why the rule is one job, one
screen.
""")

save(prs, str(pathlib.Path(__file__).parent / "week06.pptx"))
