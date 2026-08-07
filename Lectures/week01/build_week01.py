#!/usr/bin/env python3
"""Week 1 — Introduction: Prompt Engineering and Generative AI.

Build:  python3 build_week01.py
Output: week01.pptx
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "Theme"))
from theme import *  # noqa

prs = new_deck()

# ══════════════════════════════════════════════════════════════════ opening
title_slide(
    prs, 1,
    "Introduction",
    "Prompt Engineering and Generative AI",
    notes="""
Good morning, and welcome. This is Prompt Engineering and Large Language Models.
I'm Mehmet Ali Akyol.

Before anything else, let me say who this course is for, because I know some of you
are checking whether you're in the right room. This is a university-wide elective.
There is no prerequisite. You do not need to know how to program. You will not write
a single line of code that I require you to understand. I have students here from
medicine, from law, from education, from business, from engineering — and that mix
is not a problem I'm working around. It's the point. The most interesting thing that
will happen in this room this semester is a law student and an engineering student
discovering they have the same problem with these systems.

Second thing. The title of this course changed this year. It used to be called
Prompt Engineering. It is now Prompt Engineering and Large Language Models. That is
not cosmetic. The course changed underneath the title, and in the next twenty minutes
I'm going to tell you exactly why, because the reason is genuinely interesting and it
tells you something true about the field you're walking into.

Let's begin.
""")

content_slide(
    prs, "Today: What We'll Explore",
    [
        "Why this course is different this year — and what changed in the field",
        "The vocabulary: generative AI, prompts, models, context",
        "Why this matters in your discipline, whatever it is",
        ("In-class activity: You Are the Expert", None),
        "What you will build between Week 6 and Week 13",
        "How you'll be assessed, and the ground rules",
    ],
    notes="""
Here's where we're going today.

We start with why this course exists in 2026, and I'm going to be honest with you
about what has and hasn't survived in this field. Some of what was taught in this
course last year I have deliberately removed, and I'll tell you why.

Then we build the vocabulary. Four words: generative AI, prompt, model, context. By
the end of that section you should be able to use all four precisely. Most people
use them interchangeably and they are not interchangeable.

Then we look at why this matters in your field specifically — I'll do healthcare,
law, education, business and engineering, and I want you thinking about yours while
I do it.

Then we stop talking and you do something. About twenty minutes of activity today,
and there will be an activity every single week. This is not a course you can pass
by watching.

Then the course map — what you'll actually build — and the practical business of
grading and rules.

One housekeeping note before we start: everything we use this semester runs in a
browser and is free. You will not be asked to pay for anything or install anything.
If that ever appears to be untrue, tell me immediately, because it means I've made
a mistake.
""")

# ══════════════════════════════════════════════════════ part 1 — the reframe
section_slide(
    prs, 1, "What This Course Is Actually For",
    notes="""
Part one. What this course is actually for.

I want to start somewhere uncomfortable, because I think you'll trust the rest of
the semester more if I'm straight with you in the first thirty minutes.
""")

callout_slide(
    prs,
    "You will not be hired to write prompts.",
    "So why are we spending fourteen weeks on this?",
    notes="""
Let me put this on the screen and let it sit for a second.

You will not be hired to write prompts.

If you came into this room expecting me to teach you a set of magic phrases that
make the AI behave — the secret words, the special formula — I want to disappoint
you now rather than in week nine. That course existed. It was a reasonable course
to teach in 2023. It is not a reasonable course to teach today, and I'll show you
the evidence for that on the next slide.

So the honest question is: why are we here? Why fourteen weeks?

The answer is that something more durable took its place, and it's actually harder
and more interesting than memorising prompt formulas. Hold that thought — I'll
answer it properly in about ten minutes. First, the evidence.
""")

content_slide(
    prs, "What Changed — and How Fast",
    [
        ("Reasoning is now inside the model.", None, "bold"),
        (1, "\"Let's think step by step\" was a genuine technique in 2022. Today's reasoning models do this internally.", None),
        (1, "Scripting the reasoning yourself can now conflict with the model's own process.", None),
        ("The specialist job largely evaporated.", None, "bold"),
        (1, "\"Prompt engineer\" job postings fell about 40% between 2024 and 2025.", None),
        (1, "Roles in workflow design and AI systems thinking grew over the same period.", None),
        ("Prompting became literacy, not expertise.", None, "bold"),
        (1, "Like using a search engine or a spreadsheet: expected of everyone, a career for almost no one.", None),
    ],
    notes="""
Three things changed, and they changed quickly.

First. Reasoning moved inside the model. In 2022 there was a famous result: if you
added the words "let's think step by step" to your question, accuracy on maths and
logic problems went up substantially. That was real. It was one of the genuine
discoveries of early prompt engineering. Today, the current generation of reasoning
models already does that internally before it answers you. And here's the part that
matters — adding the instruction yourself can now be redundant or can even conflict
with the model's own reasoning process. So a technique that was the crown jewel of
this field four years ago is now, at best, neutral. That should tell you something
about how fast the technique layer decays.

Second. The specialist job mostly evaporated. Job postings for "prompt engineer"
fell roughly forty percent between 2024 and 2025. Meanwhile the roles that grew were
about designing workflows and thinking about AI systems. Not phrasing. Design.

Third, and this is the important one. Prompting didn't become worthless. It became
literacy. It's now like being able to use a search engine, or a spreadsheet.
Everybody is expected to do it competently. Almost nobody is paid to do only that.

Now — if I stopped here, this would be a strange course to be enrolled in. So let
me tell you what replaced it.
""")

content_slide(
    prs, "What Replaced It — and What Employers Now Ask For",
    [
        "Understanding how these systems actually produce an answer",
        ("Recognising when an output is wrong", None, "bold"),
        "Spotting a hallucination before it reaches a patient, a client, or a grade",
        "Knowing when human judgment is required and cannot be delegated",
        "Designing a workflow, not writing a sentence",
        "",
        (1, "Sources: Campus, \"AI Skills Employers Want in 2026\"; TripleTen, \"AI Skills 2026\"; HackerNoon, \"Why Practical AI Skills Matter More Than Prompt Engineering in 2026\"", None),
    ],
    notes="""
This is the list that survey after survey now produces when employers are asked what
they actually want.

Understanding how the system produces an answer. Recognising when an output is
wrong — and I've put that one in bold because it is the spine of this entire course.
Spotting a hallucination before it reaches a patient, a client, or a student's grade.
Knowing when human judgment is required and simply cannot be handed over. And
designing a workflow rather than writing a clever sentence.

Look at that list carefully. Every single item is a judgment skill. Not one of them
is about phrasing.

And notice something else: every item on that list gets harder as the models get
better, not easier. When a system is wrong in an obvious way, anyone can catch it.
When a system is wrong in a fluent, confident, well-structured, professionally
formatted way — that is when you need someone trained. That is what I'm training
you to be.

I've put my sources at the bottom. I'll do that all semester. If I give you a number
in this course, I will tell you where it came from, and if I can't source something
I will say so out loud. I'd ask you to hold me to that.
""")

callout_slide(
    prs,
    "This is a course about working with a system that is capable, confident, and sometimes wrong.",
    "Everything else we do is in service of that.",
    notes="""
So here is the course in one sentence.

This is a course about working with a system that is capable, confident, and
sometimes wrong.

Capable — genuinely, remarkably capable, and I am not going to spend the semester
being cynical about that. These tools are useful and you should use them.

Confident — it will never hedge unless you make it. It has no facial expression. It
does not sound less certain when it's guessing. A human expert who doesn't know
something usually signals it. These systems do not, by default.

And sometimes wrong. Not usually. Not always. Sometimes — which is much more
dangerous than usually, because usually-wrong tools get abandoned and
sometimes-wrong tools get trusted.

Everything we do this semester serves that sentence.
""")

# ══════════════════════════════════════════════════════ part 2 — vocabulary
section_slide(
    prs, 2, "The Vocabulary",
    notes="""
Part two. The vocabulary.

Four words. We're going to use them precisely for fourteen weeks, so let's agree on
what they mean now. I promise this is the driest ten minutes of the semester.
""")

content_slide(
    prs, "Generative AI",
    [
        "AI that produces new content — text, images, audio, video, code",
        "As opposed to AI that classifies, ranks, or predicts a number",
        "",
        ("Not generative:", None, "bold"),
        (1, "Your bank's fraud detection deciding whether a transaction is suspicious", None),
        (1, "A hospital system flagging which scans a radiologist should read first", None),
        ("Generative:", None, "bold"),
        (1, "Drafting the letter, writing the summary, producing the image", None),
    ],
    notes="""
Generative AI. AI that produces new content — text, images, audio, video, code.

The word "generative" is doing real work here, because it distinguishes this from
the AI that has been running quietly in the background of your life for a decade.

Two examples of AI that is not generative. Your bank's fraud detection: it looks at
a transaction and decides suspicious or not suspicious. That's classification. It
picks from options that already exist. Or a hospital system that looks at a queue of
scans and decides which order a radiologist should read them in. That's ranking.
Also not generative.

Generative is when it drafts the letter. Writes the summary. Produces the image.
Something exists afterwards that did not exist before, and that thing came out of
the model rather than being selected from a list.

Why does the distinction matter for us? Because classification systems are wrong in
ways you can measure — you count how often the fraud detector was right. Generative
systems are wrong in ways that require a human being to read the output and judge
it. There's no accuracy percentage for "was this letter good."

That's the whole reason this course has to exist.
""")

content_slide(
    prs, "Prompt",
    [
        "What you give the system to get a response",
        "Not only a question — an instruction, an example, a document, an image",
        "",
        (1, "\"Summarise this discharge note for the patient's family.\"  — instruction", None),
        (1, "A photo of a damaged part, with \"what failed here?\"  — image plus question", None),
        (1, "A contract, with \"flag anything that differs from our standard terms.\"  — document plus task", None),
        "",
        ("Everything you put in is the prompt — including the file you attached.", None, "bold"),
    ],
    notes="""
A prompt is what you give the system in order to get a response.

Most people hear "prompt" and think "the question I typed." That's too narrow, and
the narrowness will cause you real problems later in the semester. A prompt is an
instruction, or an example, or a document, or an image — or all four at once.

Three examples. "Summarise this discharge note for the patient's family" — that's an
instruction, not a question. A photo of a damaged component with "what failed here?"
— that's an image plus a question, and the image is part of the prompt. A contract
attached with "flag anything that differs from our standard terms" — the entire
contract is part of the prompt.

That last line is the one I want you to remember, and I want you to remember it in
week twelve especially: everything you put in is the prompt, including the file you
attached.

Why does that matter? Because in week twelve we're going to look at what happens
when someone hides an instruction inside a document you upload. If you think the
prompt is only what you typed, you will not see that attack coming. If you understand
that the document is also the prompt, you will.
""")

content_slide(
    prs, "Model",
    [
        "The system itself — the thing that was trained, that you send prompts to",
        "\"Large language model\" is the family most of this course is about",
        "",
        (1, "Different models have different strengths, costs, and knowledge cut-offs", None),
        (1, "The same prompt can give different answers to different models — and to the same model twice", None),
        "",
        ("We will not build a learning outcome around any one company's product.", None, "bold"),
        (1, "Tools change every few months. The concepts don't. Week 3 goes inside the model properly.", None),
    ],
    notes="""
The model is the system itself. The thing that was trained on an enormous amount of
material, and the thing you're sending your prompt to.

Large language model — LLM — is the family that most of this course is about. Week
three is entirely about what's going on inside one, so I'm keeping this brief.

Two properties to note now. Different models have genuinely different strengths,
different costs, and different knowledge cut-offs — meaning a point in time after
which they simply don't know what happened. And this one surprises people: the same
prompt can give you different answers on different models, and it can give you
different answers on the same model twice. These systems are not deterministic. If
you come from a background where you expect the same input to produce the same
output, adjust that expectation now.

And a promise about how I'll teach this. I will name specific tools constantly,
because you need to actually do things and you can't do things with abstractions.
But I will never build a learning outcome around one company's product. The tools we
use in week seven may not be the market leaders by the time you graduate. What you
learn about grounding will still be true. Concepts are the curriculum; tools are the
illustration.
""")

content_slide(
    prs, "Context",
    [
        "Everything the model can \"see\" when it answers you",
        "Your current message, the conversation so far, any attached files, any system instructions",
        "",
        ("Two consequences you will meet all semester:", None, "bold"),
        (1, "It has no memory outside the context. A new conversation knows nothing about the last one.", None),
        (1, "Context is finite. Give it a 300-page document and something has to give.", None),
        "",
        (1, "This is also why sharing a chat can leak more than you intended — Week 12.", None),
    ],
    notes="""
Context. Everything the model can see at the moment it answers you.

That includes your current message, the conversation so far, any files you've
attached, and any behind-the-scenes instructions the tool itself adds without showing
you. That last part matters more than students expect.

Two consequences, and you'll meet both repeatedly.

First: it has no memory outside the context. If you open a new conversation, it
knows nothing about the previous one. Nothing. Students find this genuinely
disorienting because the system talks like a colleague who remembers you, and it
doesn't. Everything it appears to "know" about your situation is sitting in the
current context, and when that context ends, it's gone.

Second: context is finite. There's a limit. Give it a three-hundred-page document
and something has to give — either it won't accept it, or it will work from part of
it, and it may not tell you which part. Week three covers this properly, and week
seven is largely about how to work around it well.

And a preview of week twelve: this is also why sharing a chat transcript can leak
more than you meant to share. The context contains things you may have forgotten are
in there.
""")

two_col_slide(
    prs, "The Four Words Together",
    "The vocabulary",
    [
        ("Generative AI", None, "bold"),
        (1, "the category — systems that produce new content", None),
        ("Prompt", None, "bold"),
        (1, "everything you give it, including files", None),
        ("Model", None, "bold"),
        (1, "the trained system you're talking to", None),
        ("Context", None, "bold"),
        (1, "everything it can see right now", None),
    ],
    "Used precisely",
    [
        "\"I gave the model a prompt containing a PDF, and the context window couldn't hold all of it.\"",
        "",
        ("That sentence should now be completely clear to you.", None, "bold"),
        "",
        (1, "If it isn't, stop me now — everything from here builds on these four words.", None),
    ],
    notes="""
Let's put them together.

Generative AI is the category — systems that produce new content. The prompt is
everything you give it, including files. The model is the trained system you're
talking to. Context is everything it can see right now.

And here's the test. Read the sentence on the right.

"I gave the model a prompt containing a PDF, and the context window couldn't hold
all of it."

If that sentence is completely clear to you, you have the vocabulary for the
semester and we can move on.

If it isn't clear — genuinely, stop me now. Put your hand up. Everything from here
builds on these four words, and there is no advantage whatsoever to being the person
who nods in week one and is lost in week seven. I would much rather spend three more
minutes here.

[Pause. Actually wait. Count to five in your head before moving on.]
""")

# ══════════════════════════════════════════ part 3 — why it matters in your field
section_slide(
    prs, 3, "Why This Matters in Your Field",
    notes="""
Part three. Why this matters in your field.

I'm going to go through five disciplines. Yours is probably one of them. While I'm
talking about the others, I want you doing one thing: thinking about the equivalent
in your own work. Because in about ten minutes I'm going to ask you to use it.
""")

content_slide(
    prs, "Healthcare",
    [
        ("Genuinely useful:", None, "bold"),
        (1, "Turning a discharge summary into language a family can actually follow", None),
        (1, "Drafting patient education material at a controlled reading level", None),
        (1, "Structuring a messy consultation transcript into a standard note format", None),
        "",
        ("Where it bites:", None, "bold"),
        (1, "A fabricated drug interaction, written as fluently as a real one", None),
        (1, "Patient data typed into a tool that stores and reuses it", None),
    ],
    notes="""
Healthcare first, since we're at a medical university.

Genuinely useful things. Turning a discharge summary into language a family can
actually follow — this is a real problem, families routinely leave hospital not
understanding the instructions, and this is a task these systems are good at.
Drafting patient education material at a controlled reading level. Taking a messy
consultation transcript and structuring it into a standard note format.

Now where it bites. A fabricated drug interaction — and here is the thing I need you
to internalise — written exactly as fluently as a real one. It will not look
uncertain. It will not be hedged. It will read like the true ones read. There is no
visual difference between the model's knowledge and the model's invention.

And the second one: patient data typed into a tool that stores it and may reuse it.
Some of you will do a rotation where this is a live risk within the next two years.

I want to be clear that I am not telling you not to use these tools in clinical
contexts. I'm telling you that the skill of checking is the job, and we're going to
practise it.
""")

content_slide(
    prs, "Law",
    [
        ("Genuinely useful:", None, "bold"),
        (1, "Comparing a contract against a standard template and flagging deviations", None),
        (1, "Summarising a large volume of documents to decide what deserves reading", None),
        (1, "Translating a clause into plain language for a client", None),
        "",
        ("Where it bites:", None, "bold"),
        (1, "Invented case citations — real courts have sanctioned real lawyers for this", None),
        (1, "Confident statements about jurisdictions the model knows little about", None),
    ],
    notes="""
Law.

Useful: comparing a contract against a standard template and flagging what's
different. Summarising a large volume of documents to work out what actually deserves
a human reading. Translating a clause into plain language for a client — lawyers
spend a lot of time doing this and it's genuinely tedious.

Where it bites. Invented case citations. This is the famous one. Real courts have
sanctioned real lawyers for filing documents containing cases that do not exist. The
citations looked perfect — correct format, plausible court, plausible year, plausible
party names. They were fiction.

And the quieter one, which I think is more dangerous because nobody gets famous for
it: confident statements about jurisdictions the model knows very little about. It
has read an enormous amount of American law. It has read much less Turkish law. It
will not tell you that. Its confidence does not drop when its knowledge does.

That asymmetry — confidence staying flat while knowledge drops — is worth writing
down. It applies to every field in this list.
""")

content_slide(
    prs, "Education, Business, Engineering",
    [
        ("Education", None, "bold"),
        (1, "Useful: differentiated materials, question banks, feedback drafts. Bites: plausible pedagogy that's wrong for the age group; work students didn't do.", None),
        ("Business", None, "bold"),
        (1, "Useful: synthesising customer feedback, first drafts, competitor summaries. Bites: invented statistics with invented sources.", None),
        ("Engineering", None, "bold"),
        (1, "Useful: explaining unfamiliar code, drafting documentation, generating test cases. Bites: code that runs perfectly and does the wrong thing.", None),
    ],
    notes="""
Three more, more briefly.

Education. Useful for differentiated materials — the same concept rewritten for
different levels — question banks, and first drafts of feedback. Where it bites:
plausible-sounding pedagogy that is wrong for the age group, and of course, work that
students didn't do. We'll deal with that honestly in week thirteen, and I mean
honestly — not with a list of prohibitions.

Business. Useful for synthesising a large volume of customer feedback, first drafts
of almost anything, and competitor summaries. Where it bites: invented statistics
attached to invented sources. This is a specific and common failure. It will give
you a number and attribute it to a real consulting firm that never published it.

Engineering. Useful for explaining code you didn't write, drafting documentation
that nobody wants to write, and generating test cases. Where it bites: code that runs
perfectly and does the wrong thing. Which is worse than code that fails, because code
that fails announces itself.

Do you see the pattern across all five? The failure mode is never "it broke." The
failure mode is always "it worked, beautifully, and it was wrong."
""")

callout_slide(
    prs,
    "In every field, the dangerous failure is not the obvious one.",
    "It is the fluent, well-formatted, professional-looking answer that happens to be false.",
    notes="""
Let me make that explicit, because it's the thesis of the course.

In every field, the dangerous failure is not the obvious one. It's the fluent,
well-formatted, professional-looking answer that happens to be false.

If these systems produced obvious nonsense, we would not need a course. You'd look at
it, you'd laugh, you'd move on. The reason we need fourteen weeks is that the output
looks exactly like competent professional work. It has the right structure. It uses
the right vocabulary. It's confident. It's well-organised. And a certain percentage
of the time, it is simply not true.

Your professional value — genuinely, in whatever field you end up in — is going to
sit substantially in being the person who can tell the difference.

Right. I've been talking for a while. Let's find out if any of this is real.
""")

# ══════════════════════════════════════════════════════════════ part 4 — activity
section_slide(
    prs, 4, "Activity: You Are the Expert",
    notes="""
Part four. Our first activity.

Every week has one of these. This is not a course you can pass by watching me.
""")

activity_slide(
    prs, "You Are the Expert",
    [
        ("1.  Open any free AI assistant in your browser.", None, "bold"),
        (1, "ChatGPT, Claude, Gemini, Copilot — whichever you can reach. No account needed for most.", None),
        ("2.  Ask it something you personally know well.", None, "bold"),
        (1, "Your degree subject. Your home town. A hobby. Something where YOU are the expert in this room.", None),
        ("3.  Ask a real question — not a trick, not a riddle.", None, "bold"),
        (1, "The kind of thing a colleague might genuinely ask you.", None),
        ("4.  Now grade the answer honestly.", None, "bold"),
        (1, "What is right? What is subtly off? What is confidently wrong? What did it leave out?", None),
    ],
    minutes=15,
    notes="""
Here's what you're going to do. Fifteen minutes.

Step one. Open any free AI assistant in your browser. ChatGPT, Claude, Gemini,
Copilot — whichever you can reach from the campus network. Most of them let you ask
questions without an account. If one won't load, use a different one. If nothing
loads, pair up with the person next to you.

Step two, and this is the important one. Ask it something you personally know well.
Your degree subject. Your home town. A hobby you've had for years. Something where
you — not me, not the internet — are the actual expert in this room.

Step three. Ask a real question. Not a trick, not a riddle, not "how many Rs in
strawberry." I want the kind of question a colleague might genuinely ask you. The
whole exercise fails if you try to break it, because breaking it is easy and tells
you nothing about how it will fail when you're relying on it.

Step four. Grade the answer honestly. Four things: what's right? What's subtly off —
not wrong exactly, but not how you'd put it? What is confidently wrong? And what did
it leave out that you would have said?

That last question is the one people skip and it's often the most revealing.

I'll come round. Start now.

[Circulate. Look for a strong "confidently wrong" example and a strong "subtly off"
example to use in the debrief. Ask permission before sharing anyone's screen.]
""")

content_slide(
    prs, "Debrief: What Did You Find?",
    [
        "Who got an answer that was essentially correct?",
        "Who found something subtly off — right facts, wrong emphasis, wrong for the context?",
        ("Who found something confidently, specifically wrong?", None, "bold"),
        "Who noticed something important missing?",
        "",
        ("The question that matters:", None, "bold"),
        (1, "Would you have caught it if it hadn't been your area of expertise?", None),
    ],
    notes="""
Let's hear it. Hands up.

Who got an answer that was essentially correct? — good, and that should be most of
you. These tools are genuinely good. I'm not here to convince you otherwise.

Who found something subtly off? Right facts, but wrong emphasis, or right in general
but wrong for the specific context you had in mind? [Take two or three.]

Who found something confidently, specifically wrong? [Take these carefully. Ask them
to read the sentence out. Ask: did it look uncertain? It won't have.]

Who noticed something important missing — something you would definitely have said?

Now here's the question I actually brought you here for, and I want you to sit with
it rather than answer it quickly.

Would you have caught it if it hadn't been your area of expertise?

Almost always the answer is no. You caught it because you already knew. Which means
every time you use one of these systems outside your expertise — which is most of
the time, because that's why you're asking — you are not in a position to catch the
same class of error.

That is the problem this course exists to address. Not "how do I get better output."
How do I know whether the output is any good, when I'm not the expert?
""")

# ═══════════════════════════════════════════════════════════ part 5 — the course
section_slide(
    prs, 5, "How This Course Works",
    notes="""
Part five. How the course works, what you'll build, and how you'll be graded.
""")

two_col_slide(
    prs, "The Shape of the Semester",
    "Weeks 1–5 · Baseline",
    [
        ("1  Introduction", None, "plain"),
        ("2  A Brief History of AI, NLP and LLMs", None, "plain"),
        ("3  How LLMs Work", None, "plain"),
        ("4  Principles of Effective Prompting", None, "plain"),
        ("5  Controlling Style, Tone and Format", None, "plain"),
        "",
        (1, "Enough foundation that the failures make sense when you meet them.", None),
    ],
    "Weeks 6–13 · Build",
    [
        ("6   Building Your First Tool Without Code", None, "plain"),
        ("7   Grounding AI in Your Own Sources", None, "plain"),
        ("8   Verification: Knowing When AI Is Wrong", None, "plain"),
        ("9   AI Agents and Workflow Automation", None, "plain"),
        ("10  Building for Your Own Field", None, "plain"),
        ("11  Domain-Specific Applications", None, "plain"),
        ("12  Prompt Injection and AI Security", None, "plain"),
        ("13  Ethics, Copyright and Responsible Use", None, "plain"),
    ],
    notes="""
The semester has two halves and they feel quite different.

Weeks one to five are the baseline. Introduction — today. Then a history of AI,
natural language processing and large language models, because I think you cannot
judge where this is going without knowing how it got here, and because the history
is genuinely a good story. Then how these models actually work. Then principles of
effective prompting. Then controlling style, tone and format.

That's five weeks of foundation. The purpose of it is not scholarly completeness —
it's that when things fail in the second half of the course, you'll understand why
rather than just observing that they did.

Weeks six to thirteen, you build. Every single week. Your first tool without writing
code. Grounding a system in your own documents. Verification — how to know when it's
wrong. Agents and automation. Then week ten you build something for your own field.
Week eleven you make it professional. Week twelve you attack it. Week thirteen,
ethics, copyright and responsible use — placed deliberately at the end, after you've
built things and can see what the ethical questions actually attach to.

Week fourteen we pull it together.
""")

content_slide(
    prs, "What You Will Actually Build",
    [
        ("Micro-Tool", None, "bold"),
        (1, "Week 6 — a working, single-purpose web tool for a task in your field. No code.", None),
        ("Grounded Assistant", None, "bold"),
        (1, "Week 7 — an assistant that answers from documents you choose, and shows you where.", None),
        ("Test Set", None, "bold"),
        (1, "Week 8 — ten questions to break your own assistant. Three of them unanswerable.", None),
        ("Automation Chain", None, "bold"),
        (1, "Week 9 — a workflow that runs without you.", None),
        ("Field Build", None, "bold"),
        (1, "Week 10 — all of it, combined, for your own discipline.", None),
        ("Domain Pack  ·  Attack & Patch Report", None, "bold"),
        (1, "Weeks 11–12 — make it professional, then break a classmate's and defend your own.", None),
    ],
    notes="""
These are the things that will exist because you were in this room. They have names
and we'll use the names all semester.

The Micro-Tool, week six. A working, single-purpose web tool for a task in your
field. You will describe what you want and get something that runs, in a browser,
that you can send to someone. Without writing code. Some of you will find this week
genuinely startling.

The Grounded Assistant, week seven. An assistant that answers from documents you
choose — a statute, a clinical guideline, a syllabus — and shows you which passage
each answer came from.

The Test Set, week eight. Ten questions designed to break your own week seven
assistant. Seven that it should be able to answer, and three that are deliberately
unanswerable from your documents. I'll tell you now what happens: it will answer the
unanswerable three anyway, confidently, and you will have built the thing that does
it. I'd rather you learned that from your own system than from a patient.

The Automation Chain, week nine. Something that runs without you.

Week ten, the Field Build — all of it combined, for your discipline. That's the
centrepiece.

Weeks eleven and twelve: make it professional, then break a classmate's and defend
your own.
""")

content_slide(
    prs, "Assessment",
    [
        ("Midterm — 40%", None, "bold"),
        (1, "In-class written exam", None),
        ("Final — 60%", None, "bold"),
        (1, "Written exam", None),
        ("Pop quizzes — up to +10 bonus points", None, "bold"),
        (1, "Five of them, unannounced, ten multiple-choice questions, about ten minutes.", None),
        (1, "All five count. Added on top of your 100. They can only help you.", None),
        "",
        ("The things you build are not graded. Every build week ends by telling you exactly what is examinable.", None, "bold"),
    ],
    notes="""
Grading. This is simple and I want no ambiguity about it.

Midterm, forty percent, in-class written exam. Final, sixty percent, written exam.

Pop quizzes — five of them across the semester, unannounced, ten multiple-choice
questions, about ten minutes each. Here's the important part: they are worth up to
ten bonus points added on top of your hundred. All five count. They cannot hurt you.
They can only help you. I do it this way because I want you here and I want you
keeping up, but I don't want a bad morning to damage your grade.

And now the thing you're all thinking. If the exams are written, and the things you
build aren't graded, why build them?

Two answers. First, because you'll learn more, and I'd rather teach a course that's
worth attending than one that's easy to grade. Second, and practically: every build
week ends with a slide that tells you exactly which concepts from that week are
examinable. The exams test whether you understood what you built — I'll show you a
grounded assistant and an answer and ask you what's wrong with it. If you did the
building, those questions will be easy. If you skipped it, they'll be very hard.

So the building isn't graded directly. It's just how you pass.
""")

content_slide(
    prs, "Ground Rules",
    [
        ("Everything is free and runs in a browser.", None, "bold"),
        (1, "No installation, no payment, no API keys. If something asks you to pay, stop and tell me.", None),
        ("Bring a laptop if you can.", None, "bold"),
        (1, "A phone works for most activities. If you have neither, pair up — that's fine and normal.", None),
        ("Never put real patient, client, or personal data into these tools in class.", None, "bold"),
        (1, "Not even anonymised. We use the sample material I provide. Week 12 explains exactly why.", None),
        ("Using AI on your own work: we'll set out the rules properly in Week 13.", None, "bold"),
        (1, "Short version — using it and telling me is fine. Using it and hiding it is not.", None),
    ],
    notes="""
Four ground rules.

One. Everything in this course is free and runs in a browser. No installation, no
payment, no API keys. If any tool I recommend ever asks you to pay for something I
said was free, stop and tell me — that means a free tier has changed and I need to
know.

Two. Bring a laptop if you have one. A phone will work for most of what we do. If
you have neither, pair up with someone. That's completely fine and it happens every
year — some of the best work in this course comes out of pairs.

Three, and this one is not negotiable. Never put real patient, client, or personal
data into these tools in this classroom. Not even anonymised — because anonymising
properly is much harder than it looks, and we will demonstrate exactly that in week
twelve. For every activity I will give you sample material. Use it.

Four. Using AI on your own coursework. We'll do this properly in week thirteen, with
the actual reasoning rather than a list of prohibitions. The short version, so nobody
is confused in the meantime: using it and telling me is fine. Using it and hiding it
is not. That's the whole rule.
""")

# ═══════════════════════════════════════════════════════════════════ wrap-up
content_slide(
    prs, "Wrap-Up",
    [
        "Prompting is now literacy, not a specialism — the durable skill is judgment",
        "Four words, used precisely: generative AI, prompt, model, context",
        "Across every field, the dangerous failure is the fluent, confident, wrong answer",
        "You caught today's errors because you were the expert. Usually you won't be.",
        "",
        ("Next week:", None, "bold"),
        (1, "A Brief History of AI, NLP and LLMs — how we got from 1950 to this, and why it matters that you know", None),
    ],
    notes="""
Let's close.

Four things to take away.

Prompting is now literacy rather than a specialism, and the durable skill underneath
it is judgment. That's why this course looks the way it does.

Four words, used precisely: generative AI, prompt, model, context. If you're shaky on
any of them, that's a five-minute fix and it's worth doing before next week.

Across every field we looked at, the dangerous failure isn't the obvious one. It's
the fluent, confident, professional-looking answer that's wrong.

And the thing from your own activity: you caught those errors because you were the
expert. Most of the time, you won't be. That gap is what we spend fourteen weeks on.

Next week, a brief history of AI, natural language processing and large language
models. How we got from 1950 to whatever this is. I know "history week" sounds like
the week to skip. I'd ask you not to — almost everything people get wrong about
where this technology is going comes from not knowing how many times the field has
been here before.

Nothing to prepare. Just turn up.

Questions?
""")

closing_slide(
    prs,
    notes="""
Take questions here.

Common ones in week one, and short answers:

"Do I need to buy ChatGPT Plus?" — No. Never. Everything in this course works on
free tiers and I check that each year.

"Can I use AI for the assignments?" — There are no assignments; assessment is two
written exams. For the in-class builds, using AI is the entire point.

"What if I've never used any of this before?" — Genuinely fine, and about a third of
the room is in that position every year. Weeks one to five assume nothing.

"Is this course hard?" — The exams are fair and I tell you what's examinable every
week. The part people find hard is not technical. It's the habit of checking
something that looks right.

If nobody has questions, let them go early. Week one running short is not a failure.
""")

save(prs, str(pathlib.Path(__file__).parent / "week01.pptx"))
