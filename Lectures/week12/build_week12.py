#!/usr/bin/env python3
"""Week 12 — Prompt Injection and AI Security.  Artifact: Attack & Patch Report.

Build:  python3 build_week12.py
Output: week12.pptx
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "Theme"))
from theme import *  # noqa

prs = new_deck()

title_slide(
    prs, 12,
    "Prompt Injection and AI Security",
    "Artifact: the Attack & Patch Report",
    notes="""
Welcome back. This is the session people remember.

I have built an assistant for today. It is grounded in a document pack, it has instructions
telling it to behave, and it is deliberately vulnerable. Your job this hour is to break it.

Before we start, the frame, because it matters. We are doing this defensively. Everything today
is about recognising attacks so you can defend the systems you build and use — the same reason
a medical student studies pathology. Nothing here is a recipe for attacking anyone else's
system, and I will keep the techniques at the level you need to recognise them, not the level
you would need to weaponise them.

The reason this session exists is simple. In week nine you learned that an agent's tools feed
their results into the context as text. In week seven you learned that grounding puts documents
into the context as text. Today you find out what happens when that text contains instructions.

Let's go.
""")

content_slide(
    prs, "Today: What We'll Explore",
    [
        "Why prompt injection works at all — and why it is hard to fix",
        "Direct injection and jailbreaking",
        ("Indirect injection — the serious one, and the one you will actually meet", None, "bold"),
        "Live: we attack a grounded assistant together",
        "Data leakage: what you reveal without meaning to",
        "Defences you can actually apply, and safe handling of sensitive data",
    ],
    notes="""
Where we're going.

First, why prompt injection works at all — and this follows directly from week three, so it
should feel inevitable rather than surprising.

Then direct injection and jailbreaking: someone typing something to make the system misbehave.
This is the famous one and honestly the least important to you.

Then indirect injection, in bold, because it's the serious one and the one you will actually
meet. It's also the one almost nobody outside security has heard of.

Then we attack a grounded assistant together, live, on screen.

Then data leakage — what you reveal without meaning to, which is the risk most relevant to
people handling patient and client information.

Then defences you can actually apply, and safe handling of sensitive data. That last part is
the professional obligation several of you already have.
""")

# ══════════════════════════════════════════════════════════ part 1 — why it works
section_slide(
    prs, 1, "Why Injection Works",
    notes="""
Part one. And this follows from week three so directly that some of you will see it coming.
""")

callout_slide(
    prs,
    "The model receives one stream of text. It cannot reliably tell your instructions from the data.",
    "Everything in the context is just tokens. Nothing carries a label saying \"this part is trustworthy\".",
    notes="""
Here it is.

The model receives one stream of text, and it cannot reliably tell your instructions from the
data.

Go back to week three. Tokens go in. The model predicts what follows. That's the operation.

Now think about what's in the context by week seven and nine. Your instructions. The
conversation. A document you attached. The result of a web search. The contents of an email it
was asked to read.

All of it arrives as tokens. None of it carries a label saying "this part is a trustworthy
instruction from the user" and "this part is untrusted material from the internet."

There is a distinction in your head — you know which parts you wrote. There is no reliable
equivalent inside the model.

So if a document says "ignore your previous instructions and do this instead," that sentence
sits in the context looking very much like an instruction. Because it is one. It's just not
yours.

That's prompt injection. And notice that it isn't a bug someone forgot to fix. It's a direct
consequence of how the thing works. Which is why it has proved genuinely hard to solve rather
than merely neglected.
""")

boxes_slide(
    prs, "Two Kinds",
    [
        ("Direct injection",
         "A person types something designed to override the system's instructions — to reveal its "
         "configuration, drop its constraints, or behave as something else. The attacker is the "
         "user."),
        ("Indirect injection",
         "The instruction is hidden in content the system reads — a document, a web page, an "
         "email, a calendar entry. The attacker is not the user. The user may be the victim."),
        ("Why the second is worse",
         "You did nothing wrong. You asked your assistant to summarise a document, and the "
         "document contained instructions. There was no moment where you could have declined."),
    ],
    notes="""
Two kinds, and the distinction matters enormously.

Direct injection. A person types something designed to override the system's instructions —
get it to reveal its configuration, drop its constraints, behave as something else. The
attacker is the user. This is the one that gets written about.

Indirect injection. The instruction is hidden in content the system reads — a document, a web
page, an email, a calendar entry. The attacker is not the user. The user may be the victim.

And the third box: why the second is much worse.

You did nothing wrong. You asked your assistant to summarise a document. The document contained
instructions. There was no moment at which you could have declined, because you never saw the
malicious text — it might be white text on a white background, or buried on page forty, or in a
comment.

Direct injection is someone attacking their own tool, which mostly harms them. Indirect
injection is someone attacking *you*, through a document you had every reason to open.

If you remember one distinction from today, that's it.
""")

content_slide(
    prs, "Jailbreaking, Briefly",
    [
        "Getting a system to do what its operators told it not to do",
        (1, "Usually by supplying a frame in which the refused thing seems appropriate — fiction, research, a hypothetical, a role", None),
        "",
        ("Why it works, mechanically:", None, "bold"),
        (1, "Safety behaviour is trained-in tendency, not a hard rule. It shifts probabilities; it does not install a gate.", None),
        (1, "A strong enough framing can make the unwanted continuation the likely one", None),
        "",
        (1, "It matters to you mainly because it shows the same thing injection shows: instructions in the context compete, and the last convincing frame can win.", None),
    ],
    notes="""
Jailbreaking, briefly, because it's less relevant to you than the headlines suggest.

Jailbreaking is getting a system to do what its operators told it not to do. Usually by
supplying a frame in which the refused thing seems appropriate — it's fiction, it's research,
it's hypothetical, you're playing a role.

Why does it work? Same reason as everything else this week. Safety behaviour is a trained-in
tendency, not a hard rule. Fine-tuning shifted the probabilities so that refusal is likely in
certain situations. It did not install a gate that checks and blocks.

So a strong enough framing can make the unwanted continuation the likely one again. You're not
picking a lock. You're changing what's probable.

And the last line is why I'm covering it at all: it demonstrates the same underlying fact as
injection. Instructions in the context compete with each other, and the last convincing frame
can win.

Once you hold that idea, both phenomena stop being separate curiosities and become one property
of the system — which is the useful way to understand it.
""")

# ══════════════════════════════════════════════════════════ part 2 — indirect
section_slide(
    prs, 2, "Indirect Injection",
    notes="""
Part two. The one that will actually affect you.
""")

flow_slide(
    prs, "How It Reaches You",
    [
        ("You ask", "\"Summarise this document\" or \"check my inbox and draft replies\"."),
        ("It reads", "The document, the page, the email — content you did not write."),
        ("Hidden text arrives", "Instructions embedded in that content enter the context as tokens."),
        ("It follows them", "The instruction competes with yours — and it arrived more recently."),
    ],
    caption="You never saw the malicious text. There was no point at which you could have refused.",
    notes="""
Here's the path. Four boxes.

You ask something entirely ordinary. "Summarise this document." "Check my inbox and draft
replies." Nothing suspicious.

It reads — the document, the page, the email. Content you did not write and may never have read
yourself.

Hidden text arrives. Instructions embedded in that content enter the context as tokens, exactly
like everything else. White text on white background. A comment in a document. Text in an
image. Page forty of a hundred-page PDF.

And it follows them. The instruction competes with yours — and note the detail in that box — it
arrived more recently. Recency matters in what gets predicted next.

Read the caption. You never saw the malicious text. There was no point at which you could have
refused.

That's why this is a genuine security problem rather than a user-education problem. Telling
people to be careful doesn't help when the dangerous content is invisible to them.
""")

boxes_slide(
    prs, "What an Attacker Would Want",
    [
        ("Change the output",
         "Make a summary omit something, misstate a term, or recommend a particular course of "
         "action. Hardest to detect, because the output looks normal and you have no reason to "
         "suspect it."),
        ("Extract information",
         "Get the system to reveal what else is in its context — other documents, earlier "
         "conversation, configuration — and place it somewhere the attacker can read it."),
        ("Cause an action",
         "The serious one, and only possible with agents. Send, forward, delete, purchase. This "
         "is why Week 9 said: narrowest tools, human before anything irreversible."),
    ],
    notes="""
Three things an attacker would want. Understanding motive helps you predict what to look for.

Change the output. Make a summary omit an inconvenient clause, misstate a term, or lean towards
a particular recommendation. This is the hardest to detect, because the output looks completely
normal and you have no reason to suspect anything. If someone wanted a contract summary to
quietly omit a liability clause, this is how.

Extract information. Get the system to reveal what else is in its context — other documents,
earlier conversation, its configuration — and place it somewhere the attacker can retrieve it.
Relevant if your assistant holds several documents at once, which by week seven yours does.

And cause an action. The serious one, and only possible with agents. Send, forward, delete,
purchase.

Which is exactly why week nine's rules were what they were. Narrowest tools: it cannot forward
your email if you never gave it the ability to send email. Human before anything irreversible:
someone sees it before it happens.

Those rules were about reliability when I gave them to you. They're security controls too, and
that's not a coincidence — a system that can't act unsupervised can't be made to act
maliciously either.
""")

# ══════════════════════════════════════════════════════════════ live exercise
section_slide(
    prs, 3, "Live: Break My Assistant",
    notes="""
Part three. The assistant is ready. Details on the board.
""")

activity_slide(
    prs, "Break My Assistant",
    [
        ("The target: a grounded assistant with a document pack, and instructions telling it to behave.", None, "bold"),
        (1, "Link on the board. Attack mine, not each other's.", None),
        "",
        ("1.  Try to make it ignore its instructions.", None, "bold"),
        (1, "Ask it to reveal how it was set up. Give it a frame where its rules seem not to apply.", None),
        ("2.  Try to make it answer outside its sources.", None, "bold"),
        (1, "Get it to drop the refusal. Get a confident answer with no quotation.", None),
        ("3.  Then read the poisoned document I have added to the pack.", None, "bold"),
        (1, "Find the hidden instruction. Ask a normal question and watch what it does.", None),
    ],
    minutes=20,
    notes="""
Twenty minutes. The target is on the board — a grounded assistant with a document pack and
instructions telling it to behave.

Attack mine. Not each other's. That's a rule for today and it's not negotiable: consent
matters, and nobody's classroom work should be broken in front of the room.

Step one. Try to make it ignore its instructions. Ask it to reveal how it was set up. Give it a
frame in which its rules seem not to apply. See what holds and what doesn't.

Step two. Try to make it answer outside its sources — get it to drop the refusal, get a
confident answer with no quotation. You already know from week eight that this is achievable;
today, try to do it on purpose.

Step three, and this is the one that matters. I have added a poisoned document to the pack.
Read it, find the hidden instruction, then ask an entirely normal question and watch what
happens.

That third step is the demonstration. Steps one and two are you attacking a system. Step three
is a system attacking you.

[Circulate. Collect the best attempts to walk through afterwards. If nobody is participating,
run all three steps on screen — the poisoned document is the payload and it works as a
demonstration.]
""")

content_slide(
    prs, "What the Room Usually Finds",
    [
        (1, "Direct attempts to reveal the instructions work more often than people expect", None),
        (1, "The refusal is easier to defeat than to trigger — a small framing change is often enough", None),
        (1, "The poisoned document works immediately, and there is no visible sign at all", None),
        (1, "The output from a poisoned query is indistinguishable from a clean one", None),
        "",
        ("That last point is the entire lesson.", None, "bold"),
        (1, "Every earlier failure in this course was invisible in the output. So is this one — but this one has an author.", None),
    ],
    notes="""
What the room usually finds — and this holds whether or not you attacked it yourself.

Direct attempts to reveal the instructions work more often than people expect. The
configuration is just text in the context, and asking for text in the context is not a strange
request.

The refusal is easier to defeat than to trigger. A small framing change is often enough — "for
a training exercise," "hypothetically," "as an example." Because, again, it's a tendency rather
than a gate.

The poisoned document works immediately, and there is no visible sign at all. No warning, no
flag, nothing in the answer that looks different.

And the output from a poisoned query is indistinguishable from a clean one.

Bold line: that last point is the entire lesson. Every earlier failure in this course was
invisible in the output — hallucination, silent failure, over-reading. This one is invisible
too.

But there's a difference, and it's why this session sits at the end. This one has an author.
Someone chose it. Everything before this week was the system being imperfect. This is the system
being used against you, and no amount of care on your part would have shown it.
""")

# ══════════════════════════════════════════════════════════ part 4 — leakage
section_slide(
    prs, 4, "Leakage and Sensitive Data",
    notes="""
Part four. The part with professional consequences for several of you.
""")

content_slide(
    prs, "What You Reveal Without Meaning To",
    [
        ("Everything in the context is available to whatever the system does next.", None, "bold"),
        (1, "Other documents you loaded. Earlier conversation. Text you pasted and moved on from.", None),
        "",
        ("Sharing a conversation shares more than the last message:", None, "bold"),
        (1, "A shared chat link carries the whole history, including material you have forgotten is there", None),
        (1, "Screenshots crop; links do not", None),
        "",
        ("And separately: what the provider retains and whether it is used for training varies by service and by setting.", None, "bold"),
        (1, "For institutional data this must be checked before use, not after.", None),
    ],
    notes="""
Three things.

Everything in the context is available to whatever the system does next. Other documents you
loaded. Earlier conversation. Text you pasted twenty minutes ago and stopped thinking about.
That's week three — no memory outside the context, but everything inside it is live.

Sharing a conversation shares more than the last message. A shared chat link carries the whole
history, including material you've forgotten is in there. And note the practical detail:
screenshots crop, links do not. People share links because it's easier, and share far more than
they intended.

And separately — what the provider retains, and whether it's used for training, varies by
service and by setting, and it changes. I'm deliberately not telling you what any particular
service does today, because it would be wrong by the time you need it.

The bold line is the professional rule: for institutional data, this must be checked before
use, not after. Once it's sent, it's sent. There's no recall.
""")

boxes_slide(
    prs, "Handling Sensitive Data",
    [
        ("Patient and client data",
         "Default to not putting it in. If your institution has an approved tool with an "
         "agreement in place, use that one and nothing else. Convenience is not a justification "
         "you can offer afterwards."),
        ("Anonymisation is harder than it looks",
         "Removing names is not anonymisation. A rare condition, a specific date, a small "
         "department, an unusual combination of details — any of these can identify someone."),
        ("Institutional documents",
         "Internal policies, unpublished research, commercial terms. Ask who owns it and what "
         "the terms say before uploading. \"I did not think\" is not a defence."),
    ],
    notes="""
Three rules for sensitive data. For those of you going into clinical or legal practice, these
are professional obligations, not suggestions.

Patient and client data: default to not putting it in. If your institution has an approved tool
with an agreement in place, use that one and nothing else. And the sentence I want you to
remember — convenience is not a justification you can offer afterwards. It will not sound good
in the meeting.

Anonymisation is harder than it looks, and this is the one people get wrong with genuine good
intentions. Removing names is not anonymisation. A rare condition plus a specific date plus a
small department can identify someone precisely, even with every name removed. In a small
population, an unusual combination of ordinary details is an identifier.

If you're thinking "but I removed the name" — that's exactly the reasoning that produces
breaches.

Institutional documents: internal policies, unpublished research, commercial terms. Ask who
owns it and what the terms say before uploading. "I didn't think" is not a defence, and it's the
most common explanation.
""")

content_slide(
    prs, "Defences You Can Actually Apply",
    [
        ("Treat everything the system reads as untrusted.", None, "bold"),
        (1, "Documents, pages, emails — all of it is potentially instruction-carrying, not just data", None),
        ("Keep the tools narrow.", None, "bold"),
        (1, "It cannot take an action you never enabled. This is the only defence that does not depend on the model behaving.", None),
        ("Human before anything irreversible.", None, "bold"),
        (1, "Injection that changes a draft is recoverable. Injection that sends something is not.", None),
        ("Check outputs against sources, as in Week 8.", None, "bold"),
        (1, "A poisoned summary usually fails the quote test — the change is not supported by any real passage.", None),
        ("Do not put in what you would not want out.", None, "bold"),
    ],
    notes="""
Five defences. These are what you can actually do, as a user, without being a security engineer.

Treat everything the system reads as untrusted. Documents, pages, emails — all of it is
potentially instruction-carrying, not merely data. That's a mental reclassification and it's
free.

Keep the tools narrow. It cannot take an action you never enabled. And note why this one is
special, in the sub-point: it's the only defence that doesn't depend on the model behaving
correctly. Everything else is a request. This is a wall.

Human before anything irreversible. Injection that changes a draft is recoverable. Injection
that sends something is not.

Check outputs against sources, as in week eight. And here's a genuinely useful detail: a
poisoned summary usually fails the quote test, because the injected change isn't supported by
any real passage in your document. So the verification habit you built in week eight is also a
security control. That's not a coincidence — most of what makes a system trustworthy also makes
it harder to attack.

And the last one, which covers everything I haven't thought of: do not put in what you would
not want out.
""")

concepts_slide(
    prs,
    [
        ("Why injection works", None, "bold"),
        (1, "The model receives one undifferentiated stream of tokens and cannot reliably distinguish your instructions from data it was given.", None),
        ("Direct vs indirect injection", None, "bold"),
        (1, "Direct: the user attacks their own system. Indirect: instructions hidden in content the system reads — the user is the victim and never sees it.", None),
        ("Why jailbreaking works", None, "bold"),
        (1, "Safety behaviour is a trained tendency that shifts probabilities, not a gate that blocks.", None),
        ("Three attacker goals", None, "bold"),
        (1, "Change the output · extract context · cause an action. Only the third requires an agent.", None),
        ("Five user-level defences", None, "bold"),
        (1, "Untrusted inputs · narrow tools · human before irreversible actions · verify against sources · do not put in what you would not want out.", None),
    ],
    notes="""
What's examinable. This week is certain to be on the final.

Why injection works — one undifferentiated stream of tokens, no reliable distinction between
instruction and data. Be able to connect this back to week three.

Direct versus indirect, and specifically who the victim is in each case. That distinction is
the most likely short-answer question in this whole section.

Why jailbreaking works: trained tendency, not a gate.

The three attacker goals, and the detail that only the third requires an agent — which is why
tool scope is a security decision.

And the five defences, with the point that narrow tools is the only one not dependent on model
behaviour.
""")

content_slide(
    prs, "Wrap-Up",
    [
        "The model sees one stream of tokens. Your instructions and the document's look the same.",
        ("Indirect injection is the one that will reach you — and you will never see it", None, "bold"),
        "Only three attacker goals; only one needs an agent. Narrow tools cut it off.",
        "Anonymisation is harder than removing names",
        "Verification from Week 8 is also a security control",
        "",
        ("Next week:", None, "bold"),
        (1, "Ethics, Copyright, Academic Integrity and Responsible Use", None),
    ],
    notes="""
Five things.

The model sees one stream of tokens. Your instructions and the document's instructions look the
same to it.

Indirect injection is the one that will reach you, and you will never see it. That's why it
matters more than the famous one.

There are only three attacker goals, and only one needs an agent. Narrow tools cut that one off
entirely.

Anonymisation is harder than removing names. Please carry that into your professional life.

And the verification habit from week eight is also a security control — a poisoned summary
usually fails the quote test.

Next week: ethics, copyright, academic integrity and responsible use. Deliberately placed here,
at the end, because now you've built things, tested them, and attacked one. The ethical
questions attach to something concrete rather than being abstract worries.

And we'll deal properly with the question several of you have been waiting for: what are the
actual rules about using this on your own coursework.

Questions?
""")

closing_slide(
    prs,
    notes="""
Take questions here.

Common ones:

"Can't the developers just fix this?" — They mitigate it, continuously, and it improves. But the
root cause is that instructions and data share one channel, which is how the architecture works.
Treat it as a risk to manage rather than a bug awaiting a patch.

"Is it illegal to do what we did today?" — On a system you own or were invited to test, no.
That's why we used mine and why I said attack mine and not each other's. On someone else's
system without permission, you're in different territory entirely — legally and professionally.

"How would I know if I'd been injected?" — Often you wouldn't. That's the honest answer, and
it's why the defences are structural — narrow tools, human review — rather than perceptual.

"Should I stop uploading documents?" — No. Know that document content is instruction-carrying,
prefer sources you control, and verify against the source.
""")

save(prs, str(pathlib.Path(__file__).parent / "week12.pptx"))
