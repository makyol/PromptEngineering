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
a single line of code that I require you to understand.

I have students here from medicine, from law, from education, from business, from
engineering. That mix is not a problem I'm working around — it's the point. Some of
the best moments in this room come from a law student and an engineering student
discovering that they have exactly the same problem with these systems, arriving at
it from completely different directions.

So: fourteen weeks. The first five build the foundation. The eight after that, you
build things — every week, something that works, that you made, in a browser,
without writing code. The last week we pull it together.

Let's begin.
""")

content_slide(
    prs, "Today: What We'll Explore",
    [
        "What this course is for, and what you'll be able to do by the end of it",
        "The vocabulary: generative AI, prompt, model, context",
        "Why this matters in your discipline, whatever it is",
        "Activity: You Are the Expert — plus two worked examples",
        "What you will build between Week 6 and Week 13",
        "Assessment and ground rules",
    ],
    notes="""
Here's where we're going today.

First, what this course is for. I'll give you the one sentence that the whole
semester hangs on, and I'll tell you what you should be able to do in January that
you can't do today.

Then the vocabulary. Four words: generative AI, prompt, model, context. By the end
of that section you should be able to use all four precisely. Most people use them
interchangeably, and they are not interchangeable — and the confusion causes real
problems later, particularly in week twelve.

Then why this matters in your field specifically. I'll go through healthcare, law,
education, business and engineering. While I'm on the others, think about yours.

Then we do something rather than just talk about it. There's an activity, and there
are two worked examples that we'll go through together on screen.

Then the course map — what you'll actually build, with names — and the practical
business of assessment and rules.

One housekeeping note. Everything we use this semester runs in a browser and is
free. No installation, no payment, no API keys. If that ever appears to be untrue,
tell me straight away, because it means I've made a mistake and I need to fix it.
""")

# ══════════════════════════════════════════════ part 1 — what the course is for
section_slide(
    prs, 1, "What This Course Is For",
    notes="""
Part one. What this course is for.

I want to give you the thesis in the first fifteen minutes rather than build up to
it, because I think you'll follow the rest of the semester better if you know where
it's going.
""")

callout_slide(
    prs,
    "This is a course about working with a system that is capable, confident, and sometimes wrong.",
    "Every week of the semester serves that sentence.",
    notes="""
Here's the sentence. This is a course about working with a system that is capable,
confident, and sometimes wrong.

Take the three words one at a time, because each one is doing work.

Capable. Genuinely, remarkably capable — and I am not going to spend fourteen weeks
being cynical about that. These tools are useful. You should use them. I use them.
A course that spent the semester telling you to be suspicious would be a waste of
your time and mine.

Confident. It will never hedge unless you make it hedge. It has no facial
expression. It does not slow down when it's unsure. Think about what happens when
you ask a human expert something at the edge of their knowledge — they pause, they
say "I think," they qualify it. You read that signal without noticing you're reading
it. These systems give you no such signal. The confidence is flat, all the way
across.

And sometimes wrong. Not usually wrong. Not always wrong. Sometimes — which is much
more dangerous than usually, because a tool that's usually wrong gets abandoned in a
week, and a tool that's sometimes wrong gets trusted.

Capable, confident, sometimes wrong. Everything we do serves that sentence.
""")

content_slide(
    prs, "By the End of This Course You Will Be Able To",
    [
        "Explain, in plain language, how these systems produce an answer",
        ("Judge whether an answer is trustworthy — including outside your own expertise", None, "bold"),
        "Point a system at your own documents and check that it actually used them",
        "Design a multi-step workflow, and recognise when a single question would be better",
        "Identify how these systems can be attacked, and defend the ones you build",
        "Handle institutional, personal and patient data responsibly",
    ],
    notes="""
Concretely, this is what you should be able to do in January.

Explain in plain language how these systems produce an answer. Not the mathematics —
plain language, to a colleague who has never thought about it.

Judge whether an answer is trustworthy, including outside your own expertise. That's
in bold because it's the hardest one and the most valuable one, and we'll come back
to why in about half an hour.

Point a system at your own documents — a statute, a guideline, a set of lecture
notes — and then check whether it actually used them, rather than taking its word
for it.

Design a workflow of several steps. And, just as importantly, recognise when that's
overengineering and a single well-formed question would have done the job. Knowing
when not to build something is a real skill.

Identify how these systems can be attacked, and defend what you've built. Week
twelve. That's the one students tell me about afterwards.

And handle institutional, personal, and patient data responsibly — which for many of
you will be a professional obligation, not a preference.

Notice what's not on this list. There's no "memorise a set of prompt formulas."
Every item is a judgment skill.
""")

two_col_slide(
    prs, "What This Course Is — and Isn't",
    "It is",
    [
        "A course about judgment",
        (1, "when to trust an output, and how to check", None),
        "A course where you build things",
        (1, "eight weeks of them, all in a browser", None),
        "Cross-disciplinary by design",
        (1, "examples rotate through five fields", None),
    ],
    "It isn't",
    [
        "A programming course",
        (1, "no code is required of you at any point", None),
        "A course about one company's product",
        (1, "tools illustrate; concepts are the curriculum", None),
        "A collection of magic phrases",
        (1, "there is no secret wording that fixes everything", None),
    ],
    notes="""
Let me be precise about the boundaries, since this is an elective and you're deciding
whether to stay.

What it is. A course about judgment — when to trust an output and how to check it.
A course where you build things: eight weeks of building, all in a browser, all free.
And cross-disciplinary by design — every concept gets illustrated in five fields, and
if I only ever gave software examples I'd be teaching a different course to a
different room.

What it isn't. It is not a programming course. No code is required of you at any
point. If I ever show you code, it will be marked optional and I will explain what it
does in plain language, and you will never be examined on it.

It is not a course about one company's product. I'll name tools constantly, because
you can't do anything with abstractions. But the tools we use in week seven may not
be the leaders by the time you graduate, and what you learn about grounding will
still be true. Concepts are the curriculum. Tools are the illustration.

And it is not a collection of magic phrases. There is no secret wording. If someone
sells you a list of a hundred perfect prompts, they are selling you something with a
very short shelf life.
""")

# ══════════════════════════════════════════════════════ part 2 — vocabulary
section_slide(
    prs, 2, "The Vocabulary",
    notes="""
Part two. The vocabulary. Four words, used precisely for fourteen weeks. I promise
this is the driest ten minutes of the semester, and it pays for itself repeatedly.
""")

content_slide(
    prs, "Generative AI",
    [
        "AI that produces new content — text, images, audio, video, code",
        "As opposed to AI that classifies, ranks, or predicts a number",
        "",
        ("Not generative:", None, "bold"),
        (1, "Your bank deciding whether a transaction is suspicious — that's classification", None),
        (1, "A hospital system deciding which scans a radiologist should read first — that's ranking", None),
        ("Generative:", None, "bold"),
        (1, "Drafting the letter. Writing the summary. Producing the image.", None),
    ],
    notes="""
Generative AI. AI that produces new content — text, images, audio, video, code.

The word "generative" is doing real work, because it separates this from the AI that
has been running quietly in the background of your life for a decade.

Two things that are not generative. Your bank's fraud detection: it looks at a
transaction and decides suspicious or not suspicious. That's classification — it
picks from options that already exist. Or a hospital system that takes a queue of
scans and decides what order a radiologist should read them in. That's ranking. Also
not generative.

Generative is when it drafts the letter. Writes the summary. Produces the image.
Something exists afterwards that did not exist before, and it came out of the model
rather than being selected from a list.

Why does this distinction matter to us? Because classification systems are wrong in
ways you can count. You can measure how often the fraud detector was right, put a
number on it, and improve it. Generative systems are wrong in ways that need a human
being to read the output and judge it. There is no accuracy percentage for "was this
letter any good."

That gap — the fact that judging the output requires a person — is the entire reason
this course exists.
""")

content_slide(
    prs, "Prompt",
    [
        "What you give the system in order to get a response",
        "Not only a question — an instruction, an example, a document, an image",
        "",
        (1, "\"Summarise this discharge note for the patient's family.\"  —  an instruction", None),
        (1, "A photo of a damaged part, plus \"what failed here?\"  —  an image and a question", None),
        (1, "A contract, plus \"flag anything that differs from our standard terms.\"  —  a document and a task", None),
        "",
        ("Everything you put in is the prompt — including the file you attached.", None, "bold"),
    ],
    notes="""
A prompt is what you give the system in order to get a response.

Most people hear "prompt" and think "the question I typed." That's too narrow, and
the narrowness will cause you a specific problem later. A prompt is an instruction,
or an example, or a document, or an image — or all four at once.

Three examples. "Summarise this discharge note for the patient's family" — an
instruction, not a question. A photo of a damaged component with "what failed here?"
— an image and a question, and the image is every bit as much part of the prompt as
the words. A contract attached with "flag anything that differs from our standard
terms" — the entire contract, every page of it, is part of the prompt.

The bold line is the one to keep: everything you put in is the prompt, including the
file you attached.

Here's why I'm making a point of it. In week twelve we look at what happens when
somebody hides an instruction inside a document that you upload. If you believe the
prompt is only what you typed, you will not see that coming, because you'll be
watching the wrong thing. If you understand that the document is also the prompt,
you'll see it immediately.
""")

content_slide(
    prs, "Model",
    [
        "The system itself — the thing that was trained, and the thing you send prompts to",
        "\"Large language model\", or LLM, is the family this course is mostly about",
        "",
        (1, "Different models have different strengths, costs, and knowledge cut-offs", None),
        (1, "A knowledge cut-off is a date after which the model simply doesn't know what happened", None),
        (1, "The same prompt can produce different answers on different models — and on the same model twice", None),
        "",
        ("Week 3 goes inside the model properly.", None, "bold"),
    ],
    notes="""
The model is the system itself. The thing that was trained on an enormous quantity of
material, and the thing you're sending your prompt to.

Large language model — LLM — is the family this course is mostly about. Week three
is entirely about what's happening inside one, so I'm keeping this short.

Three properties worth having now. Different models have genuinely different
strengths, different costs, and different knowledge cut-offs. A knowledge cut-off is
a date after which the model simply doesn't know what happened — it isn't reading the
news, it isn't updating. Ask it about something from last month and you may get a
confident answer built out of nothing.

And this one surprises people, so I'll say it slowly: the same prompt can give you
different answers on different models, and it can give you different answers on the
same model twice. These systems are not deterministic. If you come from mathematics
or engineering, where the same input gives the same output, adjust that expectation
now — it will save you confusion in week eight when you're testing something and the
result moves under you.
""")

content_slide(
    prs, "Context",
    [
        "Everything the model can \"see\" at the moment it answers you",
        "Your message, the conversation so far, attached files, and instructions the tool adds invisibly",
        "",
        ("Two consequences you'll meet all semester:", None, "bold"),
        (1, "There is no memory outside the context. A new conversation knows nothing about the last one.", None),
        (1, "Context is finite. Give it a 300-page document and something has to give.", None),
        "",
        (1, "It's also why sharing a chat transcript can reveal more than you meant to — Week 12.", None),
    ],
    notes="""
Context. Everything the model can see at the moment it answers you.

That includes your current message, the conversation so far, any files you've
attached, and — this part matters — any behind-the-scenes instructions the tool adds
without showing you. Most products you'll use put text in front of your message that
you never see.

Two consequences.

First: there is no memory outside the context. Open a new conversation and it knows
nothing about the previous one. Nothing at all. Students find this genuinely
disorienting, because the system talks like a colleague who remembers you, and it
does not. Everything it appears to know about your situation is sitting in the
current context, and when that context ends, it's gone.

Second: context is finite. There's a ceiling. Give it a three-hundred-page document
and something has to give — either it refuses, or it works from part of it. And it
may not tell you which part. That's a quiet failure and it's exactly the kind we care
about. Week three covers the mechanism; week seven is largely about working around it
well.

One preview: this is also why sharing a chat transcript can reveal more than you
meant to. The context holds things you've stopped thinking about.
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
    "The test",
    [
        "\"I gave the model a prompt containing a PDF, and the context window couldn't hold all of it.\"",
        "",
        ("That sentence should now be completely clear.", None, "bold"),
        "",
        (1, "Everything from here builds on these four words.", None),
    ],
    notes="""
Let's put them together.

Generative AI is the category — systems that produce new content. The prompt is
everything you give it, including files. The model is the trained system you're
talking to. Context is everything it can see right now.

And here's the test. Read the sentence on the right.

"I gave the model a prompt containing a PDF, and the context window couldn't hold all
of it."

Four words, one sentence, and it should now be completely transparent to you. It
describes a situation you'll be in personally by week seven.

If any part of that is fuzzy, say so now — this is a five-minute fix today and a
serious handicap in week eight. Everything from here builds on these four words.

[Pause here properly. Count to five before moving on. If nobody speaks, move on —
but give them the five seconds.]
""")

# ══════════════════════════════════════════ part 3 — why it matters in your field
section_slide(
    prs, 3, "Why This Matters in Your Field",
    notes="""
Part three. Why this matters in your field.

Five disciplines. Yours is probably one of them. While I'm on the others, think about
the equivalent in your own work — because shortly I'm going to ask you to use it.
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
        (1, "A fabricated drug interaction, written exactly as fluently as a real one", None),
        (1, "Patient data typed into a tool that stores it and may reuse it", None),
    ],
    notes="""
Healthcare first, since we're at a medical university.

Genuinely useful. Turning a discharge summary into language a family can actually
follow — this is a real, documented problem. Families leave hospital not understanding
the instructions they were given, and this is a task these systems do well. Drafting
patient education material at a controlled reading level. Taking a messy consultation
transcript and structuring it into a standard note format.

Now where it bites. A fabricated drug interaction — and here's the part to
internalise — written exactly as fluently as a real one. It will not look uncertain.
It will not be hedged. It will read precisely the way the true ones read. There is no
visual difference between the model reporting what it knows and the model inventing
something.

And the second: patient data typed into a tool that stores it and may reuse it. Some
of you will be on a rotation where that's a live risk within two years.

I want to be clear that I am not telling you never to use these tools clinically. I'm
telling you that the checking is the job, and we're going to practise it until it's
a habit.
""")

content_slide(
    prs, "Law",
    [
        ("Genuinely useful:", None, "bold"),
        (1, "Comparing a contract against a standard template and flagging deviations", None),
        (1, "Summarising a large volume of documents to decide what deserves reading", None),
        (1, "Translating a dense clause into plain language for a client", None),
        "",
        ("Where it bites:", None, "bold"),
        (1, "Invented case citations — courts have sanctioned lawyers who filed them", None),
        (1, "Confident statements about jurisdictions the model knows very little about", None),
    ],
    notes="""
Law.

Useful: comparing a contract against a standard template and flagging what differs.
Summarising a large volume of documents to work out what actually deserves a human
reading — that triage is valuable and tedious. Translating a dense clause into plain
language for a client, which lawyers spend a great deal of time doing.

Where it bites. Invented case citations. Courts have sanctioned lawyers who filed
documents containing cases that do not exist. And the citations looked perfect —
correct format, plausible court, plausible year, plausible party names. Entirely
fiction. We'll look at one on the next few slides.

And the quieter failure, which I think is more dangerous precisely because nobody
becomes famous for it: confident statements about jurisdictions the model knows very
little about. It has read an enormous amount of American law. It has read
considerably less Turkish law. It will not tell you that. Its confidence does not
fall when its knowledge does.

Write that down, because it generalises to every field on this list. Confidence stays
flat while knowledge drops.
""")

content_slide(
    prs, "Education, Business, Engineering",
    [
        ("Education", None, "bold"),
        (1, "Useful: differentiated materials, question banks, feedback drafts.  Bites: plausible pedagogy that's wrong for the age group.", None),
        ("Business", None, "bold"),
        (1, "Useful: synthesising customer feedback, first drafts, competitor summaries.  Bites: invented statistics attached to real-sounding sources.", None),
        ("Engineering", None, "bold"),
        (1, "Useful: explaining unfamiliar code, drafting documentation, generating test cases.  Bites: code that runs perfectly and does the wrong thing.", None),
    ],
    notes="""
Three more, more briefly.

Education. Useful for differentiated materials — the same concept rewritten for
three different levels — question banks, and first drafts of feedback. Where it
bites: plausible-sounding pedagogy that's simply wrong for the age group. It will
confidently produce a lesson plan for eight-year-olds that no eight-year-old could
follow, and it will look like a lesson plan.

Business. Useful for synthesising a large volume of customer feedback, first drafts
of almost anything, competitor summaries. Where it bites: invented statistics
attached to real-sounding sources. This is a specific and common failure — it gives
you a number and attributes it to a real consulting firm that never published it.
The firm exists. The report doesn't.

Engineering. Useful for explaining code you didn't write, drafting documentation
nobody wants to write, generating test cases. Where it bites: code that runs
perfectly and does the wrong thing — which is worse than code that fails, because
code that fails announces itself.

Do you see the pattern across all five? The failure is never "it broke." The failure
is always "it worked beautifully, and it was wrong."
""")

callout_slide(
    prs,
    "In every field, the dangerous failure is not the obvious one.",
    "It is the fluent, well-formatted, professional-looking answer that happens to be false.",
    notes="""
Let me make that explicit, because it's the thesis restated.

In every field, the dangerous failure is not the obvious one. It's the fluent,
well-formatted, professional-looking answer that happens to be false.

If these systems produced obvious nonsense, we wouldn't need a course. You'd look at
it, you'd laugh, you'd move on. The reason we need fourteen weeks is that the output
looks exactly like competent professional work. Right structure. Right vocabulary.
Confident tone. Well organised. And a certain fraction of the time, simply untrue.

Your professional value — genuinely, in whatever field you end up in — is going to
sit substantially in being the person who can tell the difference.

Right. Let's look at what that actually looks like on screen.
""")

# ══════════════════════════════════════════════════════════════ part 4 — activity
section_slide(
    prs, 4, "Activity: You Are the Expert",
    notes="""
Part four.

Every week has an activity. If you have a laptop or a phone, you can run this one
yourself. If you'd rather watch, that's fine too — I'll work through two examples on
screen afterwards and we'll get to the same place.
""")

activity_slide(
    prs, "You Are the Expert",
    [
        ("1.  Open any free AI assistant in your browser.", None, "bold"),
        (1, "ChatGPT, Claude, Gemini, Copilot — whichever loads. Most need no account.", None),
        ("2.  Ask it something you personally know well.", None, "bold"),
        (1, "Your degree subject. Your home town. A hobby. Something where YOU are the expert here.", None),
        ("3.  Ask a real question — not a trick, not a riddle.", None, "bold"),
        (1, "The kind of thing a colleague might genuinely ask you.", None),
        ("4.  Grade the answer honestly.", None, "bold"),
        (1, "What's right? What's subtly off? What's confidently wrong? What's missing?", None),
    ],
    minutes=10,
    notes="""
Ten minutes. Here's what to do.

Step one. Open any free AI assistant in your browser — ChatGPT, Claude, Gemini,
Copilot, whichever loads on the campus network. Most let you ask questions without an
account. If one won't load, try another. If nothing loads, just watch; we'll cover
the same ground together in a moment.

Step two, and this is the important one. Ask it something you personally know well.
Your degree subject. Your home town. A hobby you've had for years. Something where
you — not me, not the internet — are the actual expert in this room.

Step three. Ask a real question. Not a trick, not a riddle, not "how many letters in
this word." I want the kind of question a colleague might genuinely ask you. The
exercise fails if you try to break it, because breaking it is easy and tells you
nothing about how it behaves when you're actually relying on it.

Step four. Grade the answer honestly, on four things. What's right? What's subtly off
— not wrong exactly, but not how you would put it? What's confidently wrong? And what
did it leave out that you'd have said?

That last question is the one people skip, and it's often the most revealing.

[Circulate if they're working. If the room is quiet or nobody has a device, don't
force it — go straight to the worked examples on the next slides. They stand alone.]
""")

content_slide(
    prs, "Worked Example 1 — The Citation That Doesn't Exist",
    [
        ("The question:", None, "bold"),
        (1, "\"Give me a leading case on employer liability for workplace injury, with the citation.\"", None),
        "",
        ("The shape of the answer:", None, "bold"),
        (1, "A confident paragraph summarising the principle — largely accurate", None),
        (1, "A case name in correct format, a plausible court, a plausible year", None),
        (1, "A one-line statement of what the case held", None),
        "",
        ("The problem: the case does not exist.", None, "bold"),
        (1, "Everything around it was right. That is what made it convincing.", None),
    ],
    notes="""
First worked example. This is the failure that has put real lawyers in front of real
judges, and it's worth understanding precisely, because the mechanism generalises.

Somebody asks for a leading case on employer liability for workplace injury, with the
citation.

What comes back has three parts. A confident paragraph summarising the legal
principle — and this part is often largely accurate, because the principle is
genuinely well represented in what the model has read. Then a case name, in correct
citation format, attributed to a plausible court, with a plausible year. Then a
one-line statement of what the case supposedly held.

And the case does not exist. It was never decided. Nobody ever argued it.

Now — why is this so convincing? Not because the model is trying to deceive anyone.
Because everything around the fabrication was correct. The legal principle was right.
The citation format was right. The court exists. The year is plausible. The
fabrication is a single element embedded in a correct structure, and that structure
is what your judgment is checking against.

This is the general shape. The wrong thing sits inside a frame of right things. Which
is exactly why "does this look right?" is not a sufficient test — it looked right.

[If a student produced something similar in the activity, use theirs instead and
compare. If not, this stands on its own.]
""")

content_slide(
    prs, "Worked Example 2 — The Answer That's Right Somewhere Else",
    [
        ("The question:", None, "bold"),
        (1, "\"What are the notice requirements for terminating an employee?\"", None),
        "",
        ("The shape of the answer:", None, "bold"),
        (1, "A clear, well-structured, confident answer — with specific periods and thresholds", None),
        (1, "Describing a system that is essentially American", None),
        (1, "No mention of Turkey. No question about where you are. No hedge.", None),
        "",
        ("Nothing is fabricated. Everything is inapplicable.", None, "bold"),
        (1, "You asked a local question and received a foreign answer, delivered identically.", None),
    ],
    notes="""
Second worked example, and I think this one is more dangerous, because it never makes
the news.

Somebody asks about notice requirements for terminating an employee. A completely
ordinary question.

What comes back is clear, well structured, confident, with specific periods and
thresholds. And it describes a system that is essentially American. There's no
mention of Turkey. It didn't ask where you are. It didn't hedge.

Here's what makes this different from the first example. Nothing was fabricated.
Every fact in that answer might be perfectly true — somewhere. It is simply
inapplicable to you. You asked a local question and got a foreign answer, delivered
in exactly the same tone as a correct one.

Why does it happen? Because of what these systems have read. There is vastly more
English-language American material about employment law on the internet than there is
Turkish material. So when the model reaches for an answer, that's what's there. And
its confidence, as I said earlier, does not fall when its coverage does.

This one matters enormously for this room, because most of you will work in Turkey,
on Turkish problems, in Turkish institutions. Every single one of you will meet this
failure, probably repeatedly.

The defence is not clever prompting. The defence is asking "right for where?" — and
in week seven, giving it the actual local source.
""")

content_slide(
    prs, "Four Failure Signatures to Recognise",
    [
        ("Fabrication", None, "bold"),
        (1, "A specific detail invented inside an otherwise correct answer — the citation, the statistic, the study", None),
        ("Displacement", None, "bold"),
        (1, "Correct for another country, era, or context. Nothing false; nothing applicable.", None),
        ("Omission", None, "bold"),
        (1, "Everything present is true; the thing that mattered most isn't there", None),
        ("Overconfidence", None, "bold"),
        (1, "No hedge, no caveat, no question back — regardless of how thin the ground is", None),
    ],
    notes="""
Let me name the four patterns, because we'll use these names all semester and they're
the vocabulary for the exams.

Fabrication. A specific detail invented inside an otherwise correct answer. The
citation, the statistic, the study, the drug interaction. Our first worked example.

Displacement. Correct for another country, another era, another context. Nothing in
it is false; nothing in it applies to you. Our second worked example, and the one I
expect will affect this room most often.

Omission. Everything present is true, but the thing that mattered most isn't there.
This is the hardest to catch, because there is no wrong sentence to point at. You
can only catch it if you already know what should have been said — which is why it's
so dangerous outside your own expertise.

And overconfidence, which isn't really a separate failure so much as the thing that
makes the other three dangerous. No hedge, no caveat, no question back, however thin
the ground is.

Four names: fabrication, displacement, omission, overconfidence. Learn them. You will
see them on an exam paper, and more usefully, you'll see them at work.
""")

callout_slide(
    prs,
    "Would you have caught it if it hadn't been your area of expertise?",
    "Almost always, the answer is no. That gap is what this course is for.",
    notes="""
And here's the question I actually brought you here for. I'd like you to sit with it
rather than answer it quickly.

Would you have caught it if it hadn't been your area of expertise?

For the activity, whatever you found — you found it because you already knew. Your
expertise was doing the checking, silently, the whole time you were reading.

Now think about how you actually use these tools. You use them for the things you
don't know. That's the whole point of asking. Which means, precisely when you most
need to catch an error, you have the least ability to.

That is the gap. Not "how do I get better output" — the output is already good. How
do I know whether it's any good, when I'm not the expert?

Everything from week six onwards is an answer to that question. Week seven: give it
sources you trust, so it isn't working from memory. Week eight: test it deliberately,
including with questions you know it cannot answer. Week twelve: assume somebody is
attacking it.

That's the course.
""")

# ═══════════════════════════════════════════════════════════ part 5 — the course
section_slide(
    prs, 5, "How This Course Works",
    notes="""
Part five. The practical business — the shape of the semester, what you'll build,
how you're graded, and the ground rules.
""")

two_col_slide(
    prs, "The Shape of the Semester",
    "Weeks 1–5 · Baseline",
    [
        ("1   Introduction", None, "plain"),
        ("2   A Brief History of AI, NLP and LLMs", None, "plain"),
        ("3   How LLMs Work", None, "plain"),
        ("4   Principles of Effective Prompting", None, "plain"),
        ("5   Controlling Style, Tone and Format", None, "plain"),
        "",
        (1, "Enough foundation that the failures make sense when you meet them.", None),
    ],
    "Weeks 6–13 · Build",
    [
        ("6    Building Your First Tool Without Code", None, "plain"),
        ("7    Grounding AI in Your Own Sources", None, "plain"),
        ("8    Verification: Knowing When AI Is Wrong", None, "plain"),
        ("9    AI Agents and Workflow Automation", None, "plain"),
        ("10  Building for Your Own Field", None, "plain"),
        ("11  Domain-Specific Applications", None, "plain"),
        ("12  Prompt Injection and AI Security", None, "plain"),
        ("13  Ethics, Copyright and Responsible Use", None, "plain"),
    ],
    notes="""
The semester has two halves, and they feel quite different.

Weeks one to five, the baseline. Today. Then a history of artificial intelligence,
natural language processing and large language models — because you cannot judge
where this is going without knowing how it got here, and because it's genuinely a
good story with several surprises in it. Then how these models actually work. Then
principles of effective prompting. Then controlling style, tone and format.

The purpose of those five weeks is not scholarly completeness. It's that when things
fail in the second half, you'll understand why, instead of just noticing that they
did.

Weeks six to thirteen, you build, every week. Your first working tool without code.
Grounding a system in documents you choose. Verification — how to know when it's
wrong. Agents and automation. Week ten you build something for your own field. Week
eleven you make it professional. Week twelve you attack it — and that's the week
students tell me about a year later. Week thirteen, ethics, copyright and responsible
use, placed deliberately at the end, once you've built things and can see what the
ethical questions actually attach to.

Week fourteen we pull it together.
""")

content_slide(
    prs, "What You Will Actually Build",
    [
        ("Micro-Tool", None, "bold"),
        (1, "Week 6 — a working, single-purpose web tool for a task in your field. No code.", None),
        ("Grounded Assistant", None, "bold"),
        (1, "Week 7 — answers from documents you choose, and shows you which passage it used.", None),
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
These things will exist because you were in this room. They have names, and we'll use
the names all semester.

The Micro-Tool, week six. A working, single-purpose web tool for a task in your
field. You describe what you want, and you get something that runs in a browser and
that you can send to somebody. Without writing code. Some of you will find that week
genuinely startling — students who have never programmed walk out having built
something that works.

The Grounded Assistant, week seven. It answers from documents you choose — a statute,
a clinical guideline, a syllabus — and shows you which passage each answer came from.

The Test Set, week eight. Ten questions designed to break your own week seven
assistant. Seven it should answer, and three that are deliberately unanswerable from
your documents. I'll tell you now what happens: it answers the unanswerable three
anyway, confidently, and you will have built the thing that does it. I would much
rather you learned that from your own system in a classroom than from a patient.

Week nine, the Automation Chain — something that runs without you.

Week ten, the Field Build. All of it combined, for your discipline. The centrepiece.

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
        (1, "Five across the semester, unannounced, ten multiple-choice questions, about ten minutes", None),
        (1, "All five count. Added on top of your 100. They can only help you.", None),
        "",
        ("The things you build aren't graded. Every build week ends by telling you exactly what is examinable.", None, "bold"),
    ],
    notes="""
Grading. Simple, and I want no ambiguity.

Midterm, forty percent, in-class written exam. Final, sixty percent, written exam.

Pop quizzes: five across the semester, unannounced, ten multiple-choice questions,
about ten minutes each. Here's the important part — they're worth up to ten bonus
points added on top of your hundred. All five count. They cannot hurt you. They can
only help you. I do it this way because I want you here and keeping up, but I don't
want one bad morning to damage your grade.

Now the obvious question. If the exams are written, and the things you build aren't
graded, why build them?

Two answers. First, because you'll learn more, and I would rather teach a course
that's worth attending than one that's convenient to mark.

Second, and practically: every build week ends with a slide that names exactly which
concepts from that week are examinable. The exams test whether you understood what
you built. I'll put a grounded assistant and one of its answers in front of you and
ask what's wrong with it — and the four failure signatures we just named are the kind
of thing I mean. If you did the building, those questions are straightforward. If you
skipped it, they're very hard.

So the building isn't graded directly. It's simply how you pass.
""")

content_slide(
    prs, "Ground Rules",
    [
        ("Everything is free and runs in a browser.", None, "bold"),
        (1, "No installation, no payment, no API keys. If something asks you to pay, stop and tell me.", None),
        ("Bring a laptop if you can.", None, "bold"),
        (1, "A phone works for most activities. Neither? Pair up — that's normal and fine.", None),
        ("Never put real patient, client, or personal data into these tools in class.", None, "bold"),
        (1, "Not even anonymised. We use the sample material I provide. Week 12 shows exactly why.", None),
        ("Using AI on your own work: full rules in Week 13.", None, "bold"),
        (1, "Short version — using it and telling me is fine. Using it and hiding it is not.", None),
    ],
    notes="""
Four ground rules.

One. Everything in this course is free and runs in a browser. No installation, no
payment, no API keys. If any tool I recommend ever asks you to pay for something I
said was free, stop and tell me — it means a free tier has changed and I need to know
before the rest of you hit it.

Two. Bring a laptop if you have one. A phone will do for most of what we do. If you
have neither, pair up. That happens every year and some of the best work in this
course comes out of pairs.

Three, and this one is not negotiable. Never put real patient, client or personal
data into these tools in this classroom. Not even anonymised — because anonymising
properly is much harder than it looks, and we will demonstrate exactly that in week
twelve. For every activity I will give you sample material. Use it.

Four. Using AI on your own coursework. Full rules in week thirteen, with the actual
reasoning rather than a list of prohibitions. The short version so nobody is confused
in the meantime: using it and telling me is fine. Using it and hiding it is not.
That's the whole rule.
""")

# ═══════════════════════════════════════════════════════════════════ wrap-up
content_slide(
    prs, "Wrap-Up",
    [
        "Capable, confident, sometimes wrong — the sentence the whole semester serves",
        "Four words, used precisely: generative AI, prompt, model, context",
        "Four failure signatures: fabrication, displacement, omission, overconfidence",
        "The gap that matters: judging an answer when you are not the expert",
        "",
        ("Next week:", None, "bold"),
        (1, "A Brief History of AI, NLP and LLMs — how we got here, and why several of the surprises are old", None),
    ],
    notes="""
Let's close. Four things.

Capable, confident, sometimes wrong. That's the sentence the whole semester serves,
and if you remember one thing from today, that's the one.

Four words used precisely: generative AI, prompt, model, context. If you're shaky on
any of them, it's a five-minute fix and it's worth doing before next week.

Four failure signatures: fabrication, displacement, omission, overconfidence. These
come back constantly, including on the exams.

And the gap that the whole course exists to close — judging an answer when you're not
the expert. You could do it today for your own subject. By January you should be able
to do it well outside it.

Next week, a brief history of AI, natural language processing and large language
models. I know "history week" sounds like the one to skip. I'd ask you not to,
because a lot of what people get wrong about where this technology is going comes
from not knowing how many of the surprises are actually old.

Nothing to prepare. Just turn up.

Questions?
""")

closing_slide(
    prs,
    notes="""
Take questions here.

The common week-one questions, with short answers:

"Do I need to pay for ChatGPT Plus?" — No. Never. Everything in this course works on
free tiers and I check that every year.

"Can I use AI for the assignments?" — There are no assignments. Assessment is two
written exams plus bonus quizzes. For the in-class builds, using AI is the entire
point.

"What if I've never used any of this before?" — Genuinely fine. Weeks one to five
assume nothing at all, and roughly a third of the room is in that position.

"Is this course hard?" — The exams are fair, and every build week tells you what's
examinable. The part people find hard isn't technical — it's the habit of checking
something that already looks right.

"Do I need a laptop?" — Helpful, not required. Phone works. Pairing works.

If there are no questions, let them go early. A short first week is not a failure.
""")

save(prs, str(pathlib.Path(__file__).parent / "week01.pptx"))
