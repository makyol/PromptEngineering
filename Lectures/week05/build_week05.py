#!/usr/bin/env python3
"""Week 5 — Controlling Style, Tone and Format.

Build:  python3 build_week05.py
Output: week05.pptx
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "Theme"))
from theme import *  # noqa

prs = new_deck()

title_slide(
    prs, 5,
    "Controlling Style, Tone and Format",
    "Getting the register right — the part that decides whether work is usable",
    notes="""
Welcome back. This is the last of the foundation weeks — from next week you start building
things.

Last week we did four levers, and Format was one of them. Today we spend the whole session
on the third lever plus its neighbours, because it deserves it.

Here's why. In professional life, most documents don't fail because the facts are wrong.
They fail because the register is wrong. The letter to the family reads like a discharge
summary. The message to the board reads like a message to a colleague. The patient
information leaflet is written at a level no patient can read.

Those failures are invisible to the person who wrote them, because the writer knows what
they meant. And they're the difference between work that gets used and work that gets
rewritten by somebody else.

These systems are unusually good at this — better than they are at facts, honestly, because
register is a property of language and facts are a property of the world. This is a week
where you get a lot of value for very little effort.
""")

content_slide(
    prs, "Today: What We'll Explore",
    [
        "Why \"be professional\" produces inconsistent results",
        "Three dimensions of register — the vocabulary that makes tone specifiable",
        "Reading level, and why it matters more in healthcare and law than anywhere else",
        "Tone as observable behaviour rather than adjectives",
        "Structural contracts: output you can actually use",
        "Negative constraints — saying what not to do",
        "Activity: The Tone Ladder",
    ],
    notes="""
Where we're going.

First, why vague style instructions fail. "Be professional" is the single most common style
instruction and one of the least effective, and I want to show you exactly why.

Then three dimensions of register — this is borrowed from linguistics and it gives you
vocabulary for describing tone precisely instead of gesturing at it.

Then reading level, which matters more in healthcare and law than in any other field
represented in this room, and which is genuinely measurable.

Then tone as observable behaviour rather than adjectives — the single most useful reframe in
this session.

Then structural contracts: how to specify output you can actually use downstream.

Then negative constraints, which are underrated.

Then the tone ladder activity, which works with or without a device.
""")

# ═══════════════════════════════════════════════════════════ part 1 — register
section_slide(
    prs, 1, "Why \"Be Professional\" Fails",
    notes="""
Part one. Let's start with the instruction everybody gives and nobody examines.
""")

callout_slide(
    prs,
    "\"Professional\" describes a feeling. It does not describe a text.",
    "Two people asked to write professionally will produce different documents — and so will two runs.",
    notes="""
"Professional" describes a feeling. It does not describe a text.

Think about what happens when you give that instruction to a person. A lawyer's
professional is formal, hedged, precise, and dense. A nurse's professional is warm, clear,
and direct. A consultant's professional has bullet points and confidence. All three are
correct. All three are different documents.

Now give it to a system that predicts likely continuations. It has read all three, and
thousands of other things called professional. The instruction doesn't narrow much, so you
get something averaged — and from last week, you know there's randomness in the selection
too. So two runs give you two different answers, and neither is wrong, and you can't say why
you don't like either.

This is the under-specification problem from last week, applied to style rather than
content. Same diagnosis, same cure: work out what you actually meant and say that instead.

The rest of today is the vocabulary for saying it.
""")

boxes_slide(
    prs, "Three Dimensions of Register",
    [
        ("Field — the subject and its vocabulary",
         "How much specialist terminology, and at what density. "
         "\"Myocardial infarction\" or \"heart attack\". "
         "\"Force majeure\" or \"events outside anyone's control\"."),
        ("Tenor — the relationship",
         "The social distance between writer and reader, and who has standing. "
         "\"You must submit\" · \"I'd recommend\" · \"Would it be possible\". "
         "Same information, three relationships."),
        ("Mode — the channel",
         "Written to be read, or written to be spoken. Planned or spontaneous. "
         "A policy document, an email, a text message and a script are different modes "
         "even with identical content."),
    ],
    notes="""
This comes from linguistics and it's the most useful thing in today's session. Three
dimensions. Any register is a point in this space.

Field: the subject and its vocabulary. How much specialist terminology, at what density.
"Myocardial infarction" versus "heart attack." "Force majeure" versus "events outside
anyone's control." Same referent, different field setting.

Tenor: the relationship between writer and reader. Social distance, and who has standing to
tell whom what to do. Look at the three examples: "you must submit," "I'd recommend," "would
it be possible." Identical information content. Three completely different relationships,
and using the wrong one is how people cause offence without noticing.

Mode: the channel. Written to be read, or written to be spoken aloud? Planned or
spontaneous? A policy document, an email, a text message and a script for a video are
different modes even when the content is identical.

Now — here's why this is worth learning. Instead of "be professional," you can now say:
technical field, peer tenor, written-planned mode. That specifies something. It's
reproducible. And you can change one dimension at a time and see what happens, which is the
method from last week.
""")

content_slide(
    prs, "Specifying Register Precisely",
    [
        ("Instead of:", None, "bold"),
        (1, "\"Make it professional.\"    \"Make it friendly.\"    \"Make it more formal.\"", None),
        "",
        ("Say:", None, "bold"),
        (1, "\"Everyday vocabulary, no medical terms without a plain-language gloss; warm but not casual; written to be read aloud to a patient.\"", None),
        (1, "\"Full legal terminology; addressed to opposing counsel as an equal; formal written register, no contractions.\"", None),
        (1, "\"Plain language; you are advising someone senior to you; short email, no preamble.\"", None),
        "",
        (1, "Longer to write once. Reusable forever — these become templates you keep.", None),
    ],
    notes="""
Here's the difference in practice.

Instead of "make it professional," "make it friendly," "make it more formal" — three
instructions that could mean almost anything —

Say what you actually want. Look at the three examples.

First: everyday vocabulary, no medical terms without a plain-language gloss, warm but not
casual, written to be read aloud to a patient. Field, tenor, and mode, all specified. And
notice "written to be read aloud" — that's a mode instruction that changes sentence length,
punctuation, and rhythm.

Second: full legal terminology, addressed to opposing counsel as an equal, formal written
register, no contractions. Notice "as an equal" — that's tenor, and it's the difference
between a letter that reads as confident and one that reads as either deferential or
aggressive.

Third: plain language, you are advising someone senior to you, short email, no preamble.
That tenor setting — advising upward — is genuinely hard to describe any other way, and it
completely changes the output.

Last line, and this is the practical payoff. Yes, it's longer to write. You write it once.
These become templates you keep and reuse, and after a month you have a small library of
register specifications for the situations you actually face.
""")

content_slide(
    prs, "Reading Level",
    [
        "The most consequential style setting in healthcare, law and public communication",
        (1, "Patient information routinely fails because it is written at the level of the person who wrote it", None),
        (1, "So do consent forms, contracts, and letters to families", None),
        "",
        ("Ways to specify it:", None, "bold"),
        (1, "By audience: \"a reader who left school at 15\", \"a first-year undergraduate\", \"a parent with no medical background\"", None),
        (1, "By language level: CEFR A2, B1, B2 — precise and widely understood", None),
        (1, "By constraint: \"sentences under 15 words; no word longer than three syllables where a shorter one exists\"", None),
        "",
        ("Then verify it. Ask it to list every word it thinks the reader might not know.", None, "bold"),
    ],
    notes="""
Reading level. In this room, I'd argue this is the most consequential style setting there
is.

Patient information routinely fails because it's written at the level of the person who
wrote it. So do consent forms — where it has genuine ethical weight, because consent that
isn't understood isn't consent. So do contracts, and letters to families.

Three ways to specify it.

By audience: a reader who left school at fifteen, a first-year undergraduate, a parent with
no medical background. Intuitive and usually enough.

By language level: CEFR A2, B1, B2. Precise, widely understood, and useful when your readers
are reading in a second language — which matters here.

By constraint: sentences under fifteen words, no word longer than three syllables where a
shorter one exists. Blunt, but it works, and it's checkable.

And the bold line, which is the part people skip: verify it. Ask the model to list every word
in its own output that the target reader might not know. It's surprisingly good at this, and
it turns an invisible property into a list you can look at.

That's the same move as last week — make the basis visible so you can check it.
""")

# ═══════════════════════════════════════════════════════════════ part 2 — tone
section_slide(
    prs, 2, "Tone as Behaviour",
    notes="""
Part two. The single most useful reframe in this session.
""")

content_slide(
    prs, "Translate Adjectives into Behaviours",
    [
        "An adjective is a label for a feeling. A behaviour is something the text does — and can be checked.",
        "",
        ("Warm", None, "bold"),
        (1, "→ use the reader's name; acknowledge their situation; thank them for something specific", None),
        ("Urgent", None, "bold"),
        (1, "→ short sentences; the deadline in the first line; state the consequence of inaction", None),
        ("Neutral", None, "bold"),
        (1, "→ no evaluative adjectives; no exclamation marks; attribute claims rather than asserting them", None),
        ("Reassuring", None, "bold"),
        (1, "→ say what is known before what is uncertain; name the next concrete step; avoid absolute promises", None),
    ],
    notes="""
Here's the reframe. An adjective is a label for a feeling. A behaviour is something the text
actually does — and therefore something you can check.

Warm. What does warm text do? It uses the reader's name. It acknowledges their situation.
It thanks them for something specific rather than generically. Now "warm" is three
instructions instead of one vague one, and you can look at the output and see whether it did
them.

Urgent. Short sentences. The deadline in the first line, not the fourth paragraph. The
consequence of inaction stated plainly. That's what urgency is made of.

Neutral. No evaluative adjectives. No exclamation marks. Attribute claims rather than
asserting them — "the report states" rather than "it is clear that."

Reassuring, which is the hardest and the most needed in clinical communication. Say what is
known before what is uncertain — that ordering alone does most of the work. Name the next
concrete step, because uncertainty is more tolerable when there's an action. And avoid
absolute promises, because reassurance that turns out to be false is worse than none.

Do this translation once for the tones you use often, and you'll never write "make it warmer"
again.
""")

content_slide(
    prs, "Style by Example",
    [
        "For house style, showing beats describing — as with any example (Week 4)",
        (1, "Paste two or three short pieces of approved writing and say \"match this voice\"", None),
        (1, "It will pick up sentence length, formality, how you open, how you close, how much you hedge", None),
        "",
        ("Make it explicit if you want to know what it copied:", None, "bold"),
        (1, "\"Before writing, list the five features of this voice you intend to reproduce.\"", None),
        (1, "You get a description of your own house style — which is often useful on its own", None),
        "",
        (1, "Use approved published material. Do not paste confidential documents to demonstrate tone.", None),
    ],
    notes="""
For house style specifically — the way your institution actually writes — showing beats
describing, exactly as we said last week about examples generally.

Paste two or three short pieces of approved writing and say "match this voice." It will pick
up sentence length, level of formality, how you open, how you close, how much you hedge.
Those are precisely the features nobody can articulate but everyone recognises when they're
wrong.

Now the useful trick in bold. Ask it: before writing, list the five features of this voice
you intend to reproduce.

Two benefits. You can check whether it identified the right things before it writes anything
— which is much cheaper than reading a finished draft and feeling vaguely dissatisfied. And
you end up with a written description of your own house style, which many institutions have
never actually produced. I've seen that output become a real style guide.

And the last line, which by now you can predict: use approved published material. Do not
paste confidential documents in order to demonstrate tone. Your annual report is fine. A
client letter is not.
""")

# ═════════════════════════════════════════════════════════ part 3 — structure
section_slide(
    prs, 3, "Structural Contracts",
    notes="""
Part three. Format, but specified tightly enough to rely on.
""")

content_slide(
    prs, "Specify the Shape, Not Just the Style",
    [
        "A structural contract is a description of the output precise enough that you could check compliance mechanically",
        "",
        (1, "Named sections, in a fixed order", None),
        (1, "A table with named columns and stated types — \"date as DD/MM/YYYY\", \"one of: low, medium, high\"", None),
        (1, "Hard limits — \"exactly three bullets\", \"under 400 words\", \"one sentence\"", None),
        (1, "A stated fallback — \"if a field cannot be filled from the source, write NOT STATED\"", None),
        "",
        ("The fallback is the important one, and it is the one everybody forgets.", None, "bold"),
    ],
    notes="""
A structural contract is a description of the output precise enough that you could check
compliance mechanically — someone else could look at the result and say yes or no, without
judgment.

Named sections in a fixed order. A table with named columns and stated types — date as
day-month-year, risk as one of low, medium, high. Hard limits: exactly three bullets, under
400 words, one sentence. And a stated fallback.

The fallback is the important one and it's the one everybody forgets. Read the bold line,
and then let me explain why it matters so much.

If you ask for a table with a "deadline" column and the source document doesn't state a
deadline, what happens? The model has a column to fill. Empty cells are unlikely
continuations — tables in its training data are mostly full. So it will tend to produce
something plausible.

Unless you give it somewhere else to go. "If a field cannot be filled from the source, write
NOT STATED." Now there's a likely, legitimate continuation for the missing case.

That's the general principle, and it's the same one from the legal example last week: give
the model a designated place to put the absent or uncertain material, and it will usually
use it. Without one, the gap gets filled.
""")

flow_slide(
    prs, "Why the Fallback Matters",
    [
        ("You ask for a table", "Columns: obligation, clause, deadline."),
        ("The source has no deadline", "Nothing in the document states one."),
        ("Without a fallback", "An empty cell is an unlikely continuation. Something plausible appears."),
        ("With a fallback", "\"NOT STATED\" is now a likely, legitimate thing to write."),
    ],
    caption="You are not appealing to the model's honesty. You are making the honest answer the probable one.",
    notes="""
Let me draw that, because it's one of the most useful ideas in the whole course.

You ask for a table with columns: obligation, clause, deadline. The source document doesn't
state a deadline for one of the rows. Without a fallback, an empty cell is an unlikely
continuation — the model has read a great many tables, and they're mostly full. So something
plausible appears in the gap.

With a fallback — "if not stated, write NOT STATED" — you've made an honest answer into a
likely one.

And read the caption, because it generalises far beyond tables.

You are not appealing to the model's honesty. It doesn't have any, in the sense you'd mean
that word about a person. You are making the honest answer the probable one.

That is the entire design philosophy of everything we do from week seven onwards. You don't
ask the system to be truthful. You arrange the situation so that truthful output is what the
mechanism produces. That's a much more reliable strategy than trust, and it follows directly
from week three.
""")

content_slide(
    prs, "Negative Constraints",
    [
        "Saying what not to do is often more effective than adding more of what to do",
        "",
        (1, "\"Do not add any recommendation that is not in the source document.\"", None),
        (1, "\"Do not cite any law, regulation or case. If one is relevant, say so without naming it.\"", None),
        (1, "\"Do not use headings or bullet points.\"", None),
        (1, "\"Do not soften the findings. Report them as stated.\"", None),
        "",
        ("Negative constraints work best when they are specific and checkable.", None, "bold"),
        (1, "\"Don't be boring\" is not a constraint. \"No sentence longer than 20 words\" is.", None),
    ],
    notes="""
Negative constraints. Saying what not to do, which is often more effective than adding more
of what to do.

Four examples worth stealing.

"Do not add any recommendation that is not in the source document." This is a safety
constraint and I'd use it whenever the output could be acted on. Models asked to improve
instructions tend to helpfully add advice.

"Do not cite any law, regulation or case. If one is relevant, say so without naming it."
This one is precisely calibrated to what you learned in week three — the format of a
citation is easy to imitate, the content is not. So forbid the citation and keep the signal.

"Do not use headings or bullet points" — when you want prose and keep getting structure.

"Do not soften the findings. Report them as stated." Models trained to be helpful and
agreeable tend to smooth uncomfortable material.

And the bold line: negative constraints work when they're specific and checkable. "Don't be
boring" isn't a constraint, it's a complaint. "No sentence longer than twenty words" is a
constraint — you can count.
""")

boxes_slide(
    prs, "Three Format Specifications Worth Reusing",
    [
        ("The extraction table",
         "\"A table with columns: finding, exact quoted wording, source location, confidence. "
         "If a field cannot be filled from the source, write NOT STATED.\" "
         "Use whenever you are pulling facts out of a document."),
        ("The bounded summary",
         "\"Three bullets, maximum fifteen words each, in order of importance. Then one sentence "
         "naming anything important you had to leave out.\" "
         "That final sentence is what makes it safe to skim."),
        ("The two-audience pair",
         "\"Produce two versions under headings FOR THE FILE and FOR THE FAMILY. Same facts, "
         "different register. Do not add anything to the second that is not in the first.\""),
    ],
    notes="""
Three format specifications you can steal today. I use all three regularly and they cover most
professional situations.

The extraction table. A table with columns: finding, exact quoted wording, source location,
confidence — and the fallback. Use this whenever you're pulling facts out of a document. Notice
it combines everything from today: named columns, a quoted-wording column that makes claims
checkable, and a fallback so gaps don't get filled.

The bounded summary. Three bullets, fifteen words maximum each, in order of importance. Then one
sentence naming anything important that had to be left out.

That last sentence is what makes the summary safe to skim, and I'd argue it's the single most
valuable line in this slide. A summary without it hides its own omissions — and omission, from
week one, is the failure you cannot detect by reading.

And the two-audience pair. Two versions under explicit headings, same facts, different register,
with a constraint that the second must not add anything the first didn't contain. That last
clause matters: without it, the family version tends to acquire reassurance that nobody
authorised.

Write these down. They're reusable across every field in this room.
""")

content_slide(
    prs, "Writing in English for Turkish Readers",
    [
        "A situation most of you will face, and it is a register problem rather than a translation problem",
        "",
        (1, "Ask for shorter sentences than you would use for first-language readers", None),
        (1, "Ask it to avoid idiom and phrasal verbs — \"postpone\" rather than \"put off\"", None),
        (1, "Ask for the main point first, before the qualifications", None),
        "",
        ("A useful instruction:", None, "bold"),
        (1, "\"The reader is a competent professional reading in their second language. Avoid idiom. One idea per sentence.\"", None),
        (1, "Note what this is not: it is not simplification, and it is not writing down to anyone.", None),
    ],
    notes="""
Here's a situation most of you will face, and it's under-discussed: writing in English for
readers whose first language is not English.

The key insight is that this is a register problem, not a translation problem. The text stays in
English. What changes is field, and to some extent mode.

Three moves. Ask for shorter sentences than you'd use for first-language readers. Ask it to
avoid idiom and phrasal verbs — "postpone" rather than "put off," "tolerate" rather than "put up
with." Phrasal verbs are one of the hardest parts of English for second-language readers and
they're everywhere in natural writing. And ask for the main point before the qualifications,
because a reader working harder to decode has less capacity left for holding a suspended clause.

The instruction on the slide does all three at once: "the reader is a competent professional
reading in their second language. Avoid idiom. One idea per sentence."

And read the last line carefully, because it's the part people get wrong. This is not
simplification, and it is not writing down to anyone. The reader is a competent professional —
you're removing incidental difficulty, not content. Getting that distinction wrong produces
patronising text, which is worse than difficult text.
""")

content_slide(
    prs, "When Not to Over-Specify",
    [
        "Every constraint narrows the output. Enough of them and you narrow it to something useless.",
        "",
        (1, "Fifteen simultaneous constraints tend to produce cautious, hedged, lifeless text", None),
        (1, "Conflicting constraints — \"be comprehensive\" and \"under 100 words\" — force an arbitrary choice you did not make", None),
        (1, "Over-specifying format can suppress something you would have wanted to see", None),
        "",
        ("Practical guide:", None, "bold"),
        (1, "Three or four targeted constraints beat fifteen. Add them as problems appear, rather than in advance.", None),
    ],
    notes="""
A corrective, because today has been an argument for specificity and specificity has a limit.

Every constraint narrows the output. Enough of them and you narrow it to something useless.

Three ways this bites. Fifteen simultaneous constraints tend to produce cautious, hedged,
lifeless text — the model is satisfying rules rather than doing the job, and you can feel it in
the result.

Conflicting constraints force an arbitrary choice you didn't make. "Be comprehensive" and "under
100 words" cannot both be honoured. Something gets dropped, and you don't get to choose what,
and you may not notice what went.

And over-specifying format can suppress something you'd have wanted. If you demand exactly three
bullets and there were four important things, one is gone. The format won.

The practical guide: three or four targeted constraints beat fifteen. And add them as problems
appear rather than in advance — which is the loop from last week. Diagnose, then constrain. Don't
pre-emptively defend against every failure you can imagine; you'll strangle the output before you
find out which failures actually happen.
""")

content_slide(
    prs, "One Source, Several Audiences",
    [
        "A common professional need: the same content, correctly pitched to different readers",
        "",
        (1, "A clinical finding → the notes, the referral letter, and the explanation to the family", None),
        (1, "A contract review → the memo to the partner and the email to the client", None),
        (1, "An exam result → the transcript, the report to parents, the feedback to the student", None),
        "",
        ("Do them as separate turns from the same source, not as one request.", None, "bold"),
        (1, "One request produces three versions that drift towards each other", None),
        (1, "Separate turns keep each register clean — and let you check each before sending", None),
    ],
    notes="""
Here's a need that comes up constantly in professional work: the same content, correctly
pitched to different readers.

A clinical finding goes into the notes, into a referral letter, and into an explanation for
the family. Three registers. Three vocabularies. Same facts.

A contract review becomes a memo to the partner and an email to the client. An exam result
becomes a transcript entry, a report to parents, and feedback to the student.

The bold line is the practical advice: do these as separate turns from the same source, not
as one request.

Why? Two reasons. If you ask for all three at once, they drift towards each other — the
model is producing one response, and there's a pull toward internal consistency of voice
across it. You get three versions that are more similar than they should be, which defeats
the point.

And separate turns let you check each one before it goes anywhere. The family explanation
needs different scrutiny from the file note, and you want to give it that scrutiny
separately.

This, incidentally, is one of the highest-value uses of these tools in professional practice.
Not writing things from nothing — re-pitching things you already have.
""")

# ═══════════════════════════════════════════════════════════════ activity
section_slide(
    prs, 4, "Activity: The Tone Ladder",
    notes="""
Part four. Ten minutes. This one works fine with no device.
""")

activity_slide(
    prs, "The Tone Ladder",
    [
        ("The situation:", None, "bold"),
        (1, "A patient has missed two appointments. You need to contact them.", None),
        "",
        ("1.  Write the same message at three points on a ladder.", None, "bold"),
        (1, "Rung 1: warm and no pressure.  Rung 2: neutral and factual.  Rung 3: firm, with consequences.", None),
        ("2.  For each rung, write down the behaviours — not the adjectives.", None, "bold"),
        (1, "What does the text actually do differently? Sentence length? Opening? What comes first?", None),
        ("3.  If you have a device, generate all three and compare with yours.", None, "bold"),
    ],
    minutes=10,
    notes="""
Ten minutes. The situation: a patient has missed two appointments and you need to contact
them. This is a real task, and getting it wrong in either direction has real consequences —
too soft and they miss a third, too hard and they disengage entirely.

Step one. Write the same message at three points on a ladder. Rung one: warm, no pressure.
Rung two: neutral and factual. Rung three: firm, with consequences stated.

Step two, and this is the actual learning. For each rung, write down the behaviours, not the
adjectives. What does the text do differently? Sentence length? How it opens? What
information comes first? Whether it asks or tells?

Step three. If you have a device, generate all three and compare them with yours — you'll
often find it makes a choice you didn't consider.

[If nobody has a device this still works completely; the comparison is on the next slide.
Two minutes of writing, then move on.]
""")

boxes_slide(
    prs, "What Moves Between the Rungs",
    [
        ("What comes first",
         "Warm opens with the person — \"we hope you are well\". Firm opens with the fact — "
         "\"you have missed two appointments\". Ordering carries more tone than vocabulary does."),
        ("Who is the subject",
         "\"We would love to see you\" versus \"You have not attended\". Warm makes the "
         "institution the actor; firm makes the reader the actor. This single shift moves the "
         "tone further than any adjective."),
        ("What is left implicit",
         "Warm implies the consequence; firm states it. Neutral often states it once, without "
         "elaboration. Explicitness, not harshness, is what people read as firm."),
    ],
    notes="""
Here's what actually moves between the rungs, and none of it is the words people expect.

What comes first. The warm version opens with the person — "we hope you're well." The firm
version opens with the fact — "you have missed two appointments." Ordering carries more tone
than vocabulary does. You can write a firm message in gentle words if you lead with the
problem, and a soft message in blunt words if you lead with the person.

Who is the subject. "We would love to see you" versus "You have not attended." The warm
version makes the institution the actor; the firm version makes the reader the actor. This
single grammatical shift moves the tone further than any adjective you could add. Watch for
it in your own writing — it's how letters accidentally become accusatory.

And what is left implicit. The warm version implies the consequence and trusts you to infer
it. The firm version states it. Neutral usually states it once, without elaboration.

That last one is the insight I'd want you to leave with: explicitness, not harshness, is
what people read as firm. If you want a message to land harder, you usually don't need
stronger words. You need to say the thing you were hinting at.
""")

content_slide(
    prs, "Wrap-Up",
    [
        "\"Professional\" describes a feeling, not a text — specify field, tenor and mode instead",
        "Translate tone adjectives into behaviours you can check",
        "Reading level is the highest-value style setting in clinical and legal communication",
        ("Always give a fallback — make the honest answer the probable one", None, "bold"),
        "Negative constraints work when they are specific and countable",
        "",
        ("Next week:", None, "bold"),
        (1, "Building Your First Tool Without Code — you make something that runs", None),
    ],
    notes="""
Five things.

"Professional" describes a feeling, not a text. Specify field, tenor and mode — subject
vocabulary, relationship, and channel.

Translate tone adjectives into behaviours you can check. Warm means: use the name,
acknowledge the situation, thank them for something specific.

Reading level is the highest-value style setting in clinical and legal communication, and
you can verify it by asking for a list of words the reader might not know.

Always give a fallback. And remember why: you are not appealing to the model's honesty,
you're making the honest answer the probable one. That idea runs through the rest of the
course.

Negative constraints work when they're specific and countable.

Now — that's the foundation done. Five weeks of it. From next week the shape of the session
changes completely. I'll show you something working, we'll take it apart, and then you build
one. Next week you make a tool that runs in a browser, without writing code, and you'll be
able to send someone a link to it.

Nothing to prepare. Bring a laptop if you have one.

Questions?
""")

closing_slide(
    prs,
    notes="""
Take questions here.

Common ones:

"Is CEFR better than saying 'simple language'?" — More precise and more reproducible,
especially for readers working in a second language. But "explain it to a parent with no
medical background" is often just as effective and easier to remember. Use whichever you'll
actually use.

"What if I don't have approved samples for house style?" — Then describe behaviours instead,
and build the samples over time. The output you approve today becomes the example you paste
next month.

"Can it imitate a specific person's writing?" — Technically yes, to a degree. There are
consent and impersonation questions attached, and we handle those properly in week thirteen.
For institutional voice, no issue. For a named individual, think first.

"Do negative constraints ever backfire?" — Occasionally, if you pile up many of them —
you can end up with output that's cautious to the point of uselessness. Three or four
targeted ones beat a list of fifteen.
""")

save(prs, str(pathlib.Path(__file__).parent / "week05.pptx"))
