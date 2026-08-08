#!/usr/bin/env python3
"""Week 10 — Building for Your Own Field.  Artifact: Field Build.

Build:  python3 build_week10.py
Output: week10.pptx
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "Theme"))
from theme import *  # noqa

prs = new_deck()

title_slide(
    prs, 10,
    "Building for Your Own Field",
    "Artifact: the Field Build",
    notes="""
Welcome back. This is the centre of the course.

Over the last four weeks you have built a tool, grounded an assistant in documents, tested it
until it broke, and chained three steps together. Four separate techniques, four separate
sessions.

Today they become one thing, applied to a problem you actually have.

And I want to be clear about what the deliverable is, because it isn't what you might expect.
The deliverable today is a one-page design — not a working system. If you get something running
as well, excellent. But the design is the assessed skill, it's what I'll examine you on, and
it's honestly the harder part.

Here's why. Building something is now easy — you've seen that. Deciding what to build, what to
ground it in, where to put the human, and how you'd know it was working: that's the part that
takes judgment, and it's the part that transfers to whatever tools exist in five years.

So today is mostly thinking, with building as the reward at the end.
""")

content_slide(
    prs, "Today: What We'll Explore",
    [
        "A complete worked example, end to end, with the reasoning behind each decision",
        "The design worksheet — six questions that define any AI workflow",
        "Scoping: what makes a good candidate, and what makes a bad one",
        "Where the human goes, and why that decision comes first",
        ("Build: your own Field Build, starting with the worksheet", None, "bold"),
    ],
    notes="""
Where we're going.

First, a complete worked example, end to end. I'll walk you through a finished Field Build in
one discipline, and — more usefully — the reasoning behind each decision. Not just what I
built, but what I rejected.

Then the design worksheet. Six questions that define any AI workflow. This is the artifact,
and it's deliberately short enough to fill in twenty minutes.

Then scoping — what makes a good candidate and what makes a bad one. Most failed projects fail
here, before anyone builds anything.

Then where the human goes, and why that's the first decision rather than the last.

Then you build. Worksheet first, then as far into the building as time allows.
""")

# ══════════════════════════════════════════════════════════ part 1 — worked example
section_slide(
    prs, 1, "A Complete Worked Example",
    notes="""
Part one. Let me show you a finished one and the thinking behind it.
""")

content_slide(
    prs, "The Problem",
    [
        ("The situation:", None, "bold"),
        (1, "A university department answers the same forty student questions every semester — deadlines, resit rules, transfer credit, attendance requirements", None),
        (1, "The answers are all in the regulations. Nobody reads the regulations.", None),
        (1, "Staff answer by email, inconsistently, and sometimes wrongly", None),
        "",
        ("Why this is a good candidate:", None, "bold"),
        (1, "Genuinely repetitive · answers exist in a fixed document · a wrong answer is recoverable · nobody is harmed by a delay", None),
    ],
    notes="""
Here's the problem. I've chosen education because it's the one everybody in this room can
follow regardless of discipline, and because the same shape appears in all five of your fields.

A university department answers the same forty student questions every semester. Deadlines,
resit rules, transfer credit, attendance requirements. The answers are all in the regulations.
Nobody reads the regulations — not the students, and often not the staff. So staff answer by
email, inconsistently, and occasionally wrongly, and the wrong answers propagate because
students tell each other.

Now, why is this a good candidate? Four reasons, and I want you to check your own idea against
these later.

It's genuinely repetitive — forty questions, every semester, for years.

The answers exist in a fixed document. That's what makes grounding possible.

A wrong answer is recoverable. Someone gets told the wrong deadline, they find out, it gets
corrected. Compare that with a wrong drug dose.

And nobody is harmed by a delay. There's no urgency that would tempt anyone to skip the human
check.

Those four conditions define the safe zone. Stay inside it for your first build.
""")

flow_slide(
    prs, "The Design",
    [
        ("Grounded assistant", "Regulations, exam rules and the academic calendar loaded as sources. Answers only from them."),
        ("Quote required", "Every answer carries the regulation clause it came from, quoted."),
        ("Refuses cleanly", "Anything not covered returns NOT IN SOURCES and routes to a person."),
        ("Staff review", "Answers are drafted for staff, who send them. The student never talks to it directly."),
    ],
    caption="Four decisions. Notice that three of the four are about what it must not do.",
    notes="""
Here's the design. Four boxes.

A grounded assistant with the regulations, exam rules and academic calendar as sources,
answering only from them. That's week seven.

Every answer carries the regulation clause it came from, quoted. Week seven again — and it does
double duty here, because a student who receives a clause number can check it themselves, which
builds trust in a way a bare answer never does.

Anything not covered returns NOT IN SOURCES and routes to a person. Week seven's fallback
principle.

And staff review the drafted answers and send them. The student never talks to it directly.
That's week nine's rule: the human goes before the irreversible action.

Now read the caption, because it's the thing I most want you to take from this slide. Four
decisions, and three of them are about what it must *not* do. Not answer from memory. Not answer
without a source. Not talk to a student directly.

That ratio is normal for a good design. Most of the work in designing these systems is
constraining them, not empowering them. The capability is free. The constraints are the
engineering.
""")

content_slide(
    prs, "What I Rejected, and Why",
    [
        ("Letting students query it directly.", None, "bold"),
        (1, "Removes the human before an irreversible action — a student acts on a wrong answer about a deadline", None),
        ("Adding \"and check the student's record\".", None, "bold"),
        (1, "Personal data, and a fourth step. Compounding error, plus a privacy problem — Week 12", None),
        ("Letting it answer from general knowledge when the regulations were silent.", None, "bold"),
        (1, "This is the tempting one. It would be more useful and far more dangerous — other universities' rules stated confidently as ours", None),
        "",
        ("Every rejection made it less impressive and more usable.", None, "bold"),
    ],
    notes="""
Three things I rejected, because this is where the real thinking is.

Letting students query it directly. Tempting — it would remove the staff workload entirely,
which is supposedly the point. Rejected: it removes the human before an irreversible action. A
student acts on a wrong deadline and misses a resit. That's not recoverable, even though the
information error was.

Adding "and check the student's individual record." Very tempting, because it would make
answers personal and much more useful. Rejected for two reasons: personal data, which we'll
deal with properly in week twelve, and it adds a fourth step, which the arithmetic from last
week says costs more than it gives.

And the third one is the genuinely tempting one, so I want to dwell on it. Letting it answer
from general knowledge when the regulations are silent. It would be more useful — fewer
refusals, fewer questions bounced to a human, better user experience.

And it would be far more dangerous, because what it would actually do is state other
universities' rules as ours, confidently. That's displacement from week one, and it's precisely
the failure that produces a student who followed the rules of an institution they don't attend.

The bold line: every rejection made it less impressive and more usable. That trade is the job.
""")

# ══════════════════════════════════════════════════════════ part 2 — the worksheet
section_slide(
    prs, 2, "The Design Worksheet",
    notes="""
Part two. Six questions. This is what you'll fill in.
""")

content_slide(
    prs, "Six Questions",
    [
        ("1.  What is the repetitive task?", None, "bold"),
        (1, "One sentence. If it takes three, the scope is too big.", None),
        ("2.  What sources hold the answers?", None, "bold"),
        (1, "Name the actual documents. If none exist, this is not a grounding problem.", None),
        ("3.  What are the steps?", None, "bold"),
        (1, "One, two, or three. Not more.", None),
        ("4.  Where does the human sit?", None, "bold"),
        (1, "Before which action? Name the irreversible step.", None),
        ("5.  How would you know it was working?", None, "bold"),
        (1, "Three test questions — including one it cannot answer.", None),
        ("6.  What could go wrong, and who would be harmed?", None, "bold"),
        (1, "Wrong answer, leaked data, over-trust. Name a person, not a category.", None),
    ],
    notes="""
Six questions. This is the worksheet, and it's the artifact for today.

One: what is the repetitive task? One sentence. If it takes three sentences, your scope is too
big and you should cut it now rather than discovering it in twenty minutes.

Two: what sources hold the answers? Name the actual documents. And note the sub-point — if no
documents exist, this isn't a grounding problem, and you need a different design. That
realisation alone saves people weeks.

Three: what are the steps? One, two, or three. Not more. You know why.

Four: where does the human sit? Before which action specifically? Name the irreversible step.

Five: how would you know it was working? Three test questions, including one it cannot answer.
That's week eight, compressed to its minimum viable version.

Six: what could go wrong, and who would be harmed? Wrong answer, leaked data, over-trust. And
name a person, not a category — "a student who misses a resit deadline," not "users." That
specificity changes the design, every time. It's very easy to accept risk to "users" and very
hard to accept it for a named person.
""")

content_slide(
    prs, "The Same Six Questions, Clinical",
    [
        ("1.  Task", None, "bold"),
        (1, "Turn a consultation transcript into a structured note in our standard format.", None),
        ("2.  Sources", None, "bold"),
        (1, "The department's note template and its completed examples. Not the patient record.", None),
        ("3.  Steps", None, "bold"),
        (1, "One. Transcript in, structured draft out. There is no second step worth adding.", None),
        ("4.  Human", None, "bold"),
        (1, "Before the note enters the record. The clinician edits and signs; the system never writes to anything.", None),
        ("5.  How I would know", None, "bold"),
        (1, "Three transcripts where I already wrote the note by hand. Compare. Plus one where a key symptom is mentioned only in passing.", None),
        ("6.  Who is harmed", None, "bold"),
        (1, "A patient whose reported symptom is dropped from the note because it was mentioned once, quietly, in the middle.", None),
    ],
    notes="""
The same six questions in a clinical setting, so you can see the pattern rather than one
instance.

Task: turn a consultation transcript into a structured note in our standard format. One
sentence.

Sources: the department's note template and completed examples. Note what is *not* a source —
the patient record. That's a deliberate exclusion and it's driven by question six.

Steps: one. Transcript in, structured draft out. And I want to point out that "one step" is a
legitimate and often correct answer. There's no second step worth adding here, and adding one
would cost reliability for nothing.

Human: before the note enters the record. The clinician edits and signs. The system never writes
to anything — it produces text on a screen.

How I'd know: three transcripts where I already wrote the note by hand, compared. Plus — and
this is the good one — one transcript where a key symptom is mentioned only in passing, because
that's the failure I actually fear.

Who is harmed: a patient whose reported symptom is dropped because it was mentioned once,
quietly, in the middle of a long transcript.

Notice how question six generated question five. Once you name the harm, the test writes itself.
That's the mechanism I want you to use.
""")

boxes_slide(
    prs, "Three Scoping Mistakes",
    [
        ("Building a system, not a task",
         "\"A tool for managing referrals\" is a project. \"Draft the referral letter from these "
         "notes\" is a task. Systems fail slowly and invisibly; tasks either work or do not."),
        ("Automating the interesting part",
         "The temptation is to hand over the judgment and keep the typing. Do the opposite — "
         "automate the tedium, keep the judgment. It is also the only version that is safe."),
        ("Designing for a task you cannot grade",
         "If you cannot tell whether the output is right, you cannot build this responsibly, "
         "however good the tool is. Pick something where you are the expert."),
    ],
    notes="""
Three scoping mistakes. Check your worksheet against these before you build.

Building a system rather than a task. "A tool for managing referrals" is a project — it has
sub-parts, state, edge cases, and it will produce something that demos well and works badly.
"Draft the referral letter from these notes" is a task. And note the distinction that matters:
systems fail slowly and invisibly, tasks either work or don't. You want failures that announce
themselves.

Automating the interesting part. This is the seductive one. The temptation is to hand over the
judgment — let it decide the diagnosis, the grade, the recommendation — and keep the typing for
yourself. Do exactly the opposite. Automate the tedium, keep the judgment. That's not only more
useful, it's the only version that's safe, and it's also the version that doesn't erode your own
skill.

And designing for a task you cannot grade. If you can't tell whether the output is right, you
cannot build this responsibly, no matter how capable the tool is. You'd be deploying something
whose failures are invisible to the one person meant to be checking. Pick something where you
are the expert.
""")

content_slide(
    prs, "When There Are No Documents",
    [
        "A common finding at question 2 — and it is a finding, not a failure",
        "",
        (1, "If the knowledge lives only in people's heads, grounding has nothing to work with", None),
        (1, "The honest options: write the knowledge down first, or design something that does not need it", None),
        "",
        ("Often the most valuable outcome of this worksheet:", None, "bold"),
        (1, "Discovering that your institution has never written down how something is actually done", None),
        (1, "That document is worth more than the assistant would have been — and the assistant becomes possible afterwards", None),
    ],
    notes="""
A common finding at question two, and one worth taking seriously rather than treating as a dead
end.

You get to "what sources hold the answers?" and the answer is: none. Nothing is written down. The
knowledge lives in three experienced people and in habit.

If that's true, grounding has nothing to work with, and no amount of tooling changes it.

Two honest options. Write the knowledge down first — which is a real project with real value.
Or design something that doesn't need it.

And here's the bold part, which I've watched happen several times. Often the most valuable
outcome of filling in this worksheet is discovering that your institution has never written down
how something is actually done.

That document — the one that doesn't exist yet — is usually worth more than the assistant would
have been. It survives staff turnover. It makes training possible. It can be checked and
corrected.

And once it exists, the assistant becomes possible. So it isn't even a detour.

If you reach question two and find nothing, you haven't failed the exercise. You've found the
actual problem.
""")

boxes_slide(
    prs, "Good Candidates and Bad Ones",
    [
        ("Good",
         "Repetitive. The answer exists in a document you can point at. A wrong answer is "
         "recoverable. Delay harms nobody. You personally understand the task well enough to "
         "grade the output."),
        ("Bad",
         "Requires judgment you cannot specify. The answer is not written down anywhere. A wrong "
         "answer reaches a patient, client or grade directly. Needs personal data to be useful "
         "at all."),
        ("The honest test",
         "Would you be comfortable showing this to the person most affected by it, and "
         "explaining exactly how it works? If not, redesign it rather than hiding it."),
    ],
    notes="""
Good candidates and bad ones. Check your idea against this before you spend twenty minutes.

Good: repetitive; the answer exists in a document you can point at; a wrong answer is
recoverable; delay harms nobody; and you personally understand the task well enough to grade
the output. That last one is easy to forget — if you can't tell whether the output is right,
you cannot build this responsibly, no matter how good the tool is.

Bad: requires judgment you can't specify — if you can't write down the rule, the system can't
follow it. The answer isn't written down anywhere, so there's nothing to ground on. A wrong
answer reaches a patient, client or grade directly. Or it needs personal data to be useful at
all, which means the privacy problem isn't a detail you can solve later, it's the whole design.

And the honest test, which I'd like you to apply for the rest of your career: would you be
comfortable showing this to the person most affected by it, and explaining exactly how it
works?

If the answer is no — if the design only survives because the affected person doesn't know
about it — then redesign it. Don't hide it. That instinct will keep you out of more trouble
than any rule I could give you.
""")

# ══════════════════════════════════════════════════════════════ build
section_slide(
    prs, 3, "Build",
    notes="""
Part three. Twenty minutes. Worksheet first — the worksheet is the deliverable.
""")

activity_slide(
    prs, "Your Field Build",
    [
        ("1.  Fill the worksheet. All six questions. Ten minutes.", None, "bold"),
        (1, "Write it down. Everyone finishes this part — it needs no tool and no account.", None),
        ("2.  Check it against the good-candidate list.", None, "bold"),
        (1, "If it fails on scope, cut it in half and fill the worksheet again.", None),
        ("3.  Then build as far as you get in the remaining ten minutes.", None, "bold"),
        (1, "Ground it, or make the tool, or write the three steps out. Any progress is fine.", None),
        "",
        ("The worksheet is the deliverable. The working system is a bonus.", None, "bold"),
    ],
    minutes=20,
    notes="""
Twenty minutes.

One. Fill the worksheet. All six questions. Ten minutes. Write it down — on paper is fine.
Everyone finishes this part, because it needs no tool, no account, and no internet. If your
laptop won't connect today, you can still complete the assessed work.

Two. Check it against the good-candidate list. If it fails on scope — and about half of them do
— cut it in half and fill the worksheet again. Cutting scope is the most common correction and
it's not a failure, it's the exercise working.

Three. Then build as far as you get in the remaining ten minutes. Ground it, or make the tool,
or just write the three steps out properly. Any progress is fine. You will not finish, and
you're not meant to.

And the bold line, one more time: the worksheet is the deliverable. The working system is a
bonus.

[Circulate during the worksheet phase — that's where you add value. The two most common
problems: scope too large, and question six answered with a category rather than a person. Push
on both. If the room is quiet, fill the worksheet on screen for a problem from each discipline
present.]
""")

content_slide(
    prs, "The Two Questions People Get Wrong",
    [
        ("Question 3 — the steps.", None, "bold"),
        (1, "Most first drafts have five or six steps. Almost all of them collapse to two or three.", None),
        (1, "\"Read the document\" and \"find the relevant part\" are not two steps. They are one.", None),
        "",
        ("Question 6 — who is harmed.", None, "bold"),
        (1, "\"Users could get wrong information\" is not an answer. It is a way of not answering.", None),
        (1, "\"A student misses a resit because they were told the wrong date\" is an answer — and it changes the design.", None),
        "",
        (1, "Naming a specific person is the single most useful thing on the worksheet.", None),
    ],
    notes="""
Two questions people consistently get wrong, whether or not you filled it in yourself.

Question three, the steps. Most first drafts have five or six. Almost all of them collapse to
two or three when you look properly, because people list *sub-tasks* rather than steps. "Read
the document" and "find the relevant part" are not two steps — that's one retrieval. Count
actual handoffs, where output from one stage becomes input to another.

Question six, who is harmed. And this is the one that matters most.

"Users could get wrong information" is not an answer. It's a way of not answering — a sentence
shaped like a risk assessment that commits to nothing and changes no decision.

"A student misses a resit because they were told the wrong date" is an answer. It's specific,
it's plausible, and — crucially — it changes the design. The moment you write that sentence,
"let students query it directly" becomes obviously wrong. You don't need a rule; the specificity
does the work.

Naming a specific person is the single most useful thing on this worksheet. If you fill in
nothing else properly, fill in that.
""")

concepts_slide(
    prs,
    [
        ("The six design questions", None, "bold"),
        (1, "Task · sources · steps · human placement · how you would know it works · what could go wrong and to whom.", None),
        ("Good candidate criteria", None, "bold"),
        (1, "Repetitive · answers exist in documents · wrong answers recoverable · delay harmless · you can grade the output.", None),
        ("Constraint over capability", None, "bold"),
        (1, "In a good design most decisions are about what the system must not do. Capability is free; constraints are the engineering.", None),
        ("Human placement", None, "bold"),
        (1, "The human goes before the irreversible action, not at the end of the process. Identify the irreversible step first.", None),
        ("Naming the harmed person", None, "bold"),
        (1, "A specific person, not a category. Specificity changes the design; abstraction does not.", None),
    ],
    notes="""
What's examinable. Five items, and this week appears on the final almost certainly.

The six design questions. Be able to list them. A likely exam question gives you a proposed
workflow and asks which of the six was not answered.

Good candidate criteria — including the one people forget, that you must understand the task
well enough to grade the output.

Constraint over capability. In a good design, most decisions are about what the system must not
do. Learn that sentence; it's a short-answer question waiting to happen.

Human placement: before the irreversible action, not at the end. And you identify the
irreversible step first, then place the human. That ordering is the examinable part.

And naming the harmed person specifically rather than as a category, with the reason:
specificity changes the design.
""")

content_slide(
    prs, "Wrap-Up",
    [
        "Design is the skill. Building is now the easy part.",
        "Six questions: task · sources · steps · human · how you'd know · who is harmed",
        ("In a good design, most decisions are about what the system must not do", None, "bold"),
        "The human goes before the irreversible action",
        "Name the person who would be harmed — a category is not an answer",
        "",
        ("Next week:", None, "bold"),
        (1, "Domain-Specific Applications — making the output look like work from your profession", None),
    ],
    notes="""
Five things.

Design is the skill. Building is now the easy part, and that's a genuine shift — five years ago
the ratio was the other way round.

Six questions: task, sources, steps, human, how you'd know it works, who is harmed.

In a good design, most decisions are about what the system must not do.

The human goes before the irreversible action.

And name the person who would be harmed. A category is not an answer.

Keep your worksheet. Next week we make the output look like real work from your profession —
SOAP notes, IRAC, lesson plans, briefs — and the week after, we attack something built exactly
like the thing you designed today. So the worksheet gets used twice more.

Questions?
""")

closing_slide(
    prs,
    notes="""
Take questions here.

Common ones:

"What if my field doesn't have good documents?" — Then grounding isn't your design, and that's
a real finding rather than a failure. A well-specified single prompt with good context may be
the whole answer.

"Can I build this for real at work?" — With the worksheet, and with someone senior who knows
you're doing it. Never quietly. Question six is what you show them.

"Is the worksheet enough for the exam?" — The reasoning behind it is. I'll give you scenarios
and ask which design decision is wrong and why.

"My idea needs personal data to be useful." — Then it's a week twelve conversation before it's
a build. Come and talk to me — that's not a no, it's a different design problem.
""")

save(prs, str(pathlib.Path(__file__).parent / "week10.pptx"))
