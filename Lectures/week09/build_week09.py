#!/usr/bin/env python3
"""Week 9 — AI Agents and Workflow Automation.  Artifact: Automation Chain.

Build:  python3 build_week09.py
Output: week09.pptx
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "Theme"))
from theme import *  # noqa

prs = new_deck()

title_slide(
    prs, 9,
    "AI Agents and Workflow Automation",
    "Artifact: the Automation Chain",
    notes="""
Welcome back.

Last week you tested a system and, for most of you, watched it answer a question it could not
possibly answer. You saw every one of those answers, because you asked each question yourself
and read each response.

Today we remove you from the loop.

An agent is a system that takes several steps on its own — it decides what to do next, does it,
looks at the result, and continues. Nobody reads the intermediate steps. That is the entire
appeal, and it is the entire danger, and today is mostly about making sure you can hold both
of those at once.

I'll show you one working. We'll do the arithmetic on why they fail, which is genuinely
surprising the first time you see it. And then you'll build a small one — deliberately small,
capped at three steps, because I want you to be able to see every step while learning what
happens when you can't.
""")

content_slide(
    prs, "Today: What We'll Explore",
    [
        "What makes something an agent rather than a chatbot",
        "Planning, tool use, and the termination problem",
        "Demonstration: a three-step automation, working — then failing",
        ("The arithmetic of compounding error, which is worse than you expect", None, "bold"),
        "When an agent is the wrong answer, and a single prompt is better",
        "Build: your own Automation Chain",
    ],
    notes="""
Where we're going.

First, what actually makes something an agent rather than a chatbot. The word is used loosely
and the distinction is real.

Then three ideas that define how agents behave: planning, tool use, and termination. The third
one is the interesting one and nobody talks about it.

Then a demonstration — a three-step automation working, and then the same one failing, which is
more instructive.

Then the arithmetic of compounding error. This is a slide with numbers on it and it will change
how you think about multi-step systems.

Then when an agent is the wrong answer. This matters, because the enthusiasm for automating
things runs well ahead of the evidence that it helps.

Then you build one.
""")

# ══════════════════════════════════════════════════════════ part 1 — what is an agent
section_slide(
    prs, 1, "Agent or Chatbot?",
    notes="""
Part one. The distinction.
""")

boxes_slide(
    prs, "What Changes When It Becomes an Agent",
    [
        ("A chatbot answers",
         "You ask, it responds, you read it, you decide what happens next. One step. You are in "
         "the loop every single time, whether you want to be or not."),
        ("An agent acts",
         "It decides what to do, does it, looks at the result, and decides again. Several steps. "
         "You see the beginning and the end."),
        ("What you lose",
         "The intermediate steps. Every check you were performing without noticing — every "
         "moment you read something and thought 'that's not right' — is gone."),
    ],
    notes="""
Three boxes, and the third is the one that matters.

A chatbot answers. You ask, it responds, you read, you decide what happens next. One step. And
notice — you are in the loop every single time, whether you intended to be or not. Every
response passes through your eyes.

An agent acts. It decides what to do, does it, looks at the result, and decides again. Several
steps, and you see the beginning and the end.

And the third box: what you lose. The intermediate steps. And more precisely — every check you
were performing without noticing.

That's the part I want you to sit with. When you use a chatbot, you are running a quality
check on every single output, unconsciously and for free. You glance at it and something in
you says "hm, that's not right." You reword, you push back, you correct.

When you build an agent, you delete all of that, and you generally don't notice you've deleted
it, because it never felt like work.

That's the trade. Speed and scale in exchange for the free quality control you didn't know you
were providing.
""")

flow_slide(
    prs, "The Loop",
    [
        ("Goal", "You state an outcome rather than a single instruction."),
        ("Plan", "It decides what steps are needed — often revising as it goes."),
        ("Act", "It uses a tool: search, read a file, send something, call a service."),
        ("Observe", "It reads the result and decides whether to continue or stop."),
    ],
    caption="The loop repeats until it decides it is done — which is a decision it is not especially good at making.",
    notes="""
Here's the loop. Four boxes, and it cycles.

You state a goal — an outcome rather than a single instruction. "Summarise every email from
this week and flag anything needing a reply," rather than "summarise this email."

It plans: decides what steps are needed, often revising as it goes.

It acts: uses a tool. Searches, reads a file, sends something, calls a service.

It observes: reads the result, and decides whether to continue or stop.

And then it loops.

Read the caption, because it names the problem that gets the least attention. The loop repeats
until it decides it's done — and that is a decision it is not especially good at making.

Think about why, using week three. "Am I finished?" is not a fact to look up. There's no
passage to retrieve. It's a judgment about whether the work matches an intention that lives in
your head, not in the context. So it gets predicted like everything else, from what completion
usually looks like in text.

Which means agents stop too early — declaring success on partial work — and they also fail to
stop, going round and round elaborating. Both are common.
""")

content_slide(
    prs, "Tool Use — What It Actually Means",
    [
        "The model does not run anything itself. It produces a request, and something else runs it.",
        (1, "It writes: search for X · read file Y · send message Z", None),
        (1, "The surrounding system performs the action and hands back the result as text", None),
        "",
        ("Two consequences worth holding onto:", None, "bold"),
        (1, "Whatever the tool returns enters the context — and is treated as information", None),
        (1, "If that content contains instructions, they arrive alongside yours. That is Week 12.", None),
        "",
        (1, "An agent's power is exactly the set of tools you connected. Nothing more, and nothing less.", None),
    ],
    notes="""
Tool use, and there's a common misconception to clear up.

The model does not run anything itself. It produces a request, and something else runs it. It
writes "search for X" or "read file Y" or "send message Z," and the surrounding system performs
that action and hands the result back as text.

Two consequences, and the second one is the reason week twelve exists.

Whatever the tool returns enters the context and is treated as information. A web page, a
document, an email — it all arrives as text in the window, sitting right next to your
instructions.

And if that content contains instructions, they arrive alongside yours. The model sees one
stream of text. It does not have a reliable way to know that this part came from you and that
part came from a web page it just fetched.

Hold that thought for three weeks. It's the entire basis of indirect prompt injection, and once
you've seen the mechanism you'll find it obvious rather than surprising.

And the last line, which is the practical safety rule: an agent's power is exactly the set of
tools you connected. Nothing more, nothing less. If you didn't give it the ability to send
email, it cannot send email, no matter what it decides. Choose the tools narrowly.
""")

# ══════════════════════════════════════════════════════════ part 2 — failure
section_slide(
    prs, 2, "Where Agents Fail",
    notes="""
Part two. The arithmetic, which is genuinely surprising.
""")

content_slide(
    prs, "The Arithmetic of Compounding Error",
    [
        "Suppose each step is 95% reliable. That sounds good.",
        "",
        (1, "3 steps:   0.95 × 0.95 × 0.95   ≈  86% end-to-end", None),
        (1, "5 steps:   ≈  77%", None),
        (1, "10 steps:  ≈  60%", None),
        (1, "20 steps:  ≈  36%", None),
        "",
        ("A system where every part is excellent can be a system that mostly fails.", None, "bold"),
        (1, "And each step consumes the previous step's output — so an early error is inherited, not averaged away.", None),
    ],
    notes="""
Here's the arithmetic. Do this slowly, because it's the most useful slide in the session.

Suppose each step is ninety-five percent reliable. That sounds good. In most contexts that
would be excellent.

Three steps: ninety-five percent, three times over. About eighty-six percent end to end.

Five steps: seventy-seven percent.

Ten steps: sixty percent.

Twenty steps: thirty-six percent.

Read that last number again. Every individual component is ninety-five percent reliable, and
the system as a whole fails about two times in three.

The bold line: a system where every part is excellent can be a system that mostly fails. That's
not a paradox — it's just multiplication — but it is genuinely counterintuitive, and it's why
enthusiasm for long agent chains keeps running ahead of results.

And the last line makes it worse. This isn't independent random error that averages out. Each
step consumes the previous step's output. So an early mistake is inherited by everything
downstream. Step two doesn't just have its own five percent chance of error — it's doing its
work on possibly-wrong input.

That's why the practical rule is: keep chains short. Three steps. Not because three is magic,
but because eighty-six percent is recoverable and thirty-six percent is not.
""")

boxes_slide(
    prs, "Three Ways an Agent Fails Badly",
    [
        ("Silent failure",
         "A step produces something wrong but plausible. Nothing errors. The chain continues "
         "confidently on bad input and produces a complete, well-formatted, wrong result."),
        ("Wrong stopping point",
         "It decides it is finished when it is not — a partial answer delivered as a complete "
         "one. Or it never decides it is finished, and loops, elaborating."),
        ("Cost and volume",
         "Each step costs. A loop that does not terminate costs repeatedly. And an agent that "
         "acts — sending, posting, writing — can do the wrong thing many times before anyone "
         "notices."),
    ],
    notes="""
Three failure modes.

Silent failure. A step produces something wrong but plausible. Nothing errors — there's no
exception, no red text, no alert. The chain continues confidently on bad input and produces a
complete, well-formatted, wrong result. This is the characteristic agent failure and it's the
one to be most afraid of, because everything about the output says success.

Wrong stopping point, in both directions. It decides it's finished when it isn't — you get a
partial answer presented as a complete one, which is worse than an obvious failure. Or it never
decides it's finished and loops, elaborating, refining, going round again.

And cost and volume. Each step costs something. A loop that doesn't terminate costs repeatedly.
And this is the one that produces the horror stories: an agent that *acts* — sending, posting,
writing, deleting — can do the wrong thing many times before a human notices.

Notice that all three are the same underlying issue. You removed the human who was checking,
and the system has no equivalent check of its own, because — week three — there is no step at
which it verifies anything.
""")

content_slide(
    prs, "A Three-Step Chain, Written Out",
    [
        ("The task: incoming student enquiries, sorted and drafted.", None, "bold"),
        "",
        ("Step 1 — Classify.", None, "bold"),
        (1, "\"Read the enquiry. Output one of: DEADLINE, REGISTRATION, GRADES, OTHER. Nothing else.\"", None),
        ("Step 2 — Retrieve and draft.", None, "bold"),
        (1, "\"Using only the regulations provided, draft a reply. Quote the clause. If not covered, output NOT IN SOURCES.\"", None),
        ("Step 3 — Format.", None, "bold"),
        (1, "\"Format as an email with our standard greeting and signature. Change no factual content.\"", None),
        "",
        ("Then: a person reads it and sends it. That is the fourth step, and it is not automated.", None, "bold"),
    ],
    notes="""
Here's a real three-step chain, so you can see the shape.

The task: incoming student enquiries, sorted and drafted.

Step one, classify. Read the enquiry, output one of four labels, nothing else. Notice how tightly
constrained the output is — one word from a fixed list. That's deliberate. A step whose output is
one of four values can be checked at a glance, and it cannot silently corrupt the next step with a
paragraph of hedging.

Step two, retrieve and draft. Using only the regulations, draft a reply, quote the clause, and
output NOT IN SOURCES if it isn't covered. That's week seven, dropped straight into a workflow.

Step three, format. Standard greeting and signature, and — the crucial constraint — change no
factual content. Without that line, a formatting step will smooth and adjust, and you'll have
introduced a change nobody reviewed.

And then a person reads it and sends it. That's the fourth step and it is not automated. Which is
the whole design: three cheap steps that prepare, one human step that commits.

Notice also that step two can refuse. Refusals propagate to the human, which is exactly right —
the uncovered cases are the ones that most need a person.
""")

boxes_slide(
    prs, "Worth Automating, and Not",
    [
        ("Worth it",
         "Sorting a queue by type. Extracting fields from many similar documents. Reformatting "
         "between two fixed shapes. Flagging items for attention. All repetitive, all "
         "recoverable, all checkable at a glance."),
        ("Not worth it",
         "Anything you do twice a year. Anything where you cannot specify the judgment. Anything "
         "whose output goes straight to a person without review."),
        ("The honest test",
         "Would you hand this task, with these instructions, to a capable new colleague on their "
         "first day — and let them act on it unsupervised? If not, do not automate it either."),
    ],
    notes="""
Worth automating and not. This is the slide that saves you from building things you'll abandon.

Worth it: sorting a queue by type. Extracting fields from many similar documents. Reformatting
between two fixed shapes. Flagging items for attention. Look at what those have in common — all
repetitive, all recoverable, and all checkable at a glance. That last one matters: if verifying
the output takes as long as doing the task, you've gained nothing.

Not worth it: anything you do twice a year — the automation costs more than the task. Anything
where you cannot specify the judgment, because if you can't write the rule the system can't
follow it. And anything whose output goes straight to a person without review.

And the honest test, which I'd like you to carry: would you hand this task, with these
instructions, to a capable new colleague on their first day — and let them act on it
unsupervised?

If the answer is no, don't automate it either. A new colleague is actually a generous comparison:
they'd ask when confused, they'd notice something odd, they'd remember the last conversation.
Your automation does none of those things.

If you wouldn't trust the new colleague unsupervised, you shouldn't trust the chain.
""")

content_slide(
    prs, "Designing Around It",
    [
        ("Keep the chain short.", None, "bold"),
        (1, "Three steps is usually enough to be useful and short enough to inspect. Resist adding a fourth.", None),
        ("Make every step inspectable.", None, "bold"),
        (1, "Have it write down what it did at each stage. If you cannot see the middle, you cannot debug the end.", None),
        ("Put the human before anything irreversible.", None, "bold"),
        (1, "Drafting, sorting, summarising: automate. Sending, posting, deleting, paying: approve first.", None),
        ("Give it the narrowest tools that do the job.", None, "bold"),
        (1, "It cannot misuse a capability it does not have. This is the most reliable control you have.", None),
    ],
    notes="""
Four design rules. These are the professional practice.

Keep the chain short. Three steps is usually enough to be useful and short enough to inspect.
Resist adding a fourth — and notice from the arithmetic that each additional step costs you
more than the last.

Make every step inspectable. Have it write down what it did at each stage. If you can't see the
middle, you can't debug the end — you'll know the output is wrong and have no idea which step
broke.

Put the human before anything irreversible. This is the line that keeps you out of trouble.
Drafting, sorting, summarising, flagging — automate all of it. Sending, posting, deleting,
paying — approve first. The asymmetry is simple: if a draft is wrong you fix it; if a message
is sent you can't unsend it.

And give it the narrowest tools that do the job. It cannot misuse a capability it doesn't have.
This is the single most reliable control available to you, because it doesn't depend on the
system behaving well. Everything else is a request. This is a wall.
""")

callout_slide(
    prs,
    "Most tasks people want to automate are better served by one good prompt.",
    "Automation is worth it when the task is genuinely repetitive, and the cost of a mistake is low.",
    notes="""
And here's the slide that will save you the most time.

Most tasks people want to automate are better served by one good prompt.

There's real enthusiasm for building agents at the moment, and a lot of it produces fragile
systems that do badly what a single well-specified request did well.

Ask two questions before building anything multi-step.

Is this genuinely repetitive? Not "could it happen again" — do you actually do it many times?
If you do it twice a year, automating it costs more than doing it.

And what does a mistake cost? If a mistake is embarrassing, expensive, or reaches a patient or
client, then removing the human is the wrong direction, and the answer is a good prompt plus
your judgment.

The honest summary: automation is worth it when the task is genuinely repetitive and the cost
of a mistake is low. That's a narrower set of situations than the enthusiasm suggests, and
knowing that is a professional skill.

Now — with all of that said, let's build one, because the narrow set is real and useful.
""")

# ══════════════════════════════════════════════════════════════ build
section_slide(
    prs, 3, "Build",
    notes="""
Part three. Twenty minutes, three steps maximum.
""")

activity_slide(
    prs, "Build Your Automation Chain",
    [
        ("1.  Pick a repetitive task with three natural stages.", None, "bold"),
        (1, "Intake → process → format. Read → extract → summarise. Collect → classify → route.", None),
        ("2.  Write each step as a separate instruction, with its own input and output.", None, "bold"),
        (1, "Step 2 should not need to know how Step 1 did its job — only what it produced.", None),
        ("3.  Run it. Then deliberately give Step 1 bad input and watch what Step 3 produces.", None, "bold"),
        (1, "This is the important part. Note whether anything anywhere signalled a problem.", None),
        ("4.  Write one sentence: where would you put the human?", None, "bold"),
    ],
    minutes=20,
    notes="""
Twenty minutes. Three steps maximum — if you find yourself wanting a fourth, cut something.

One. Pick a repetitive task with three natural stages. Intake, process, format. Read, extract,
summarise. Collect, classify, route. Some examples: incoming enquiries sorted by urgency and
drafted a reply. A set of references checked for format and flagged. Student feedback grouped
into themes.

Two. Write each step as a separate instruction with its own input and output. And notice the
sub-point, because it's a design principle worth having: step two shouldn't need to know how
step one did its job, only what it produced. Clean handoffs make failures locatable.

Three, and this is the actual exercise: run it, then deliberately give step one bad input and
watch what step three produces. Feed it something incomplete, or wrong, or empty. Note whether
anything anywhere signalled a problem.

It usually won't. That's silent failure, and you'll have produced it yourself.

Four. Write one sentence: where would you put the human?

[If nobody is building, run the provided three-step chain on screen — first clean, then with
corrupted input at step one. The second run is the lesson.]
""")

content_slide(
    prs, "What You Probably Found",
    [
        (1, "It worked on clean input, and felt genuinely impressive", None),
        (1, "With bad input at step one, step three still produced a confident, well-formatted result", None),
        (1, "Nothing anywhere said \"something is wrong\"", None),
        (1, "The output looked exactly as good as the correct one", None),
        "",
        ("That is silent failure, and you just built it deliberately.", None, "bold"),
        (1, "In real use you would not have known — which is precisely why the human goes before anything irreversible.", None),
    ],
    notes="""
What typically happens.

It worked on clean input, and it felt genuinely impressive. Three steps running by themselves
is a good feeling and I don't want to take that away.

Then with bad input at step one, step three still produced a confident, well-formatted result.

Nothing anywhere said "something is wrong." No error, no warning, no hedge.

And — this is the part to notice — the output looked exactly as good as the correct one. Same
formatting, same confidence, same completeness. If I showed you both without telling you which
was which, you could not pick.

That's silent failure. And you just built it deliberately, which means you now know what it
looks like from the inside.

The last line is the practical conclusion. In real use, you wouldn't have known. There was no
signal available to you. Which is exactly why the human goes before anything irreversible — not
because the system is bad, but because the system has no way to tell you when it's wrong, and
you have no way to tell from the output.
""")

concepts_slide(
    prs,
    [
        ("Agent vs chatbot", None, "bold"),
        (1, "A chatbot answers one step with you reading it; an agent takes several steps and you see only the ends. You lose the checks you were performing unconsciously.", None),
        ("The loop", None, "bold"),
        (1, "Goal → plan → act → observe → repeat until it decides it is done. Termination is a judgment it makes poorly.", None),
        ("Tool use", None, "bold"),
        (1, "The model requests an action; the surrounding system performs it and returns the result as text into the context.", None),
        ("Compounding error", None, "bold"),
        (1, "95% per step is ~60% over ten steps. Errors are inherited by later steps, not averaged away.", None),
        ("Three agent failures · four design rules", None, "bold"),
        (1, "Silent failure · wrong stopping point · cost and volume.  Short chains · inspectable steps · human before irreversible actions · narrowest tools.", None),
    ],
    notes="""
What's examinable. Five items.

Agent versus chatbot, and specifically what you lose — the unconscious checking.

The loop, and that termination is a judgment it makes poorly. Be ready to explain why: "am I
finished?" isn't a fact to retrieve.

Tool use: the model requests, the system performs, the result comes back into the context as
text. That last part sets up week twelve, and I may examine the connection.

Compounding error, with the numbers. You should be able to do this calculation. Ninety-five
percent over ten steps is about sixty. And you should be able to say why it's worse than
independent error — because steps inherit each other's output.

And the three failures plus the four design rules. A likely exam question gives you a described
workflow and asks which design rule it violates.
""")

content_slide(
    prs, "Wrap-Up",
    [
        "An agent acts across several steps; you lose the checking you were doing for free",
        ("95% per step is about 60% over ten steps — and errors are inherited, not averaged", None, "bold"),
        "Silent failure is the characteristic agent problem: wrong input, confident output, no signal",
        "Short chains · inspectable steps · human before anything irreversible · narrowest tools",
        "Most tasks are better served by one good prompt",
        "",
        ("Next week:", None, "bold"),
        (1, "Building for Your Own Field — you design something end to end for your own discipline", None),
    ],
    notes="""
Five things.

An agent acts across several steps, and what you lose is the checking you were doing for free
without noticing.

Ninety-five percent per step is about sixty percent over ten steps, and errors are inherited
rather than averaged. If you remember one number this semester, make it that one.

Silent failure is the characteristic agent problem. Wrong input, confident output, no signal
anywhere.

Four design rules: short chains, inspectable steps, human before anything irreversible,
narrowest tools.

And most tasks are better served by one good prompt. Knowing when not to build something is a
real skill and it will save you more time than any technique in this course.

Next week you put it all together — you design something end to end for your own field. Bring
a real problem from your own work. That session is the centre of the course, and it works
much better if you arrive with something you actually care about.

Questions?
""")

closing_slide(
    prs,
    notes="""
Take questions here.

Common ones:

"Isn't 95% pessimistic?" — For a well-defined step, maybe. For a step involving judgment on
messy real input, it's often optimistic. Either way the shape of the curve is the lesson.

"What about agents that check their own work?" — Helps, genuinely. But the checker is the same
kind of system with the same lack of a truth mechanism. It reduces error; it doesn't create a
guarantee. Verification still needs something outside the system — week eight.

"Can I automate marking / triage / replies?" — Draft, yes. Decide, no. Put yourself before the
thing that reaches a person.

"Which automation tool should I use?" — Whichever free one you can reach. The design rules
transfer completely; the interfaces don't matter.
""")

save(prs, str(pathlib.Path(__file__).parent / "week09.pptx"))
