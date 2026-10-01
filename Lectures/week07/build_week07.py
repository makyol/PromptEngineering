#!/usr/bin/env python3
"""Week 7 — Grounding AI in Your Own Sources.  Artifact: Grounded Assistant.

Build:  python3 build_week07.py
Output: week07.pptx
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "Theme"))
from theme import *  # noqa

prs = new_deck()

title_slide(
    prs, 7,
    "Grounding AI in Your Own Sources",
    "Artifact: the Grounded Assistant",
    notes="""
Welcome back.

Last week you built a tool, and we ended on a sentence: the surface is not evidence. Today we
attack the deeper version of that problem.

Everything you've done so far runs on what the model absorbed during training. Which means
when you ask about your hospital's protocol, your university's regulations, Turkish
procedure, or a document that was written last month, it is working from either thin coverage
or nothing at all — and, as you know by now, telling you nothing about which.

Today we fix that. Not by making the model know more, which we can't do. By putting the right
material in front of it at the moment it answers.

This is, I think, the highest-value single session in the course for people who aren't
programmers. It's the difference between a system that sounds like it knows your field and a
system that is actually working from your documents. And the second half of today is about
the harder question: how do you know which one you've got?
""")

content_slide(
    prs, "Today: What We'll Explore",
    [
        "Why the model fails on your own material — and why that is not fixable by prompting",
        "What grounding actually is, conceptually",
        "Demonstration: an assistant answering from a document pack",
        "Source quality: what makes a document easy or hard to ground on",
        ("Checking whether an answer is genuinely supported — the part that matters", None, "bold"),
        "Build: your own Grounded Assistant",
    ],
    notes="""
Where we're going.

First, why the model fails on your own material — and I want to be clear that this is not
fixable by better prompting. That's an important negative result. Some of you have been trying
to prompt your way around it.

Then what grounding actually is, conceptually. No vector databases, no implementation. The
idea, which is simple.

Then a demonstration: an assistant answering from a pack of documents, with sources.

Then source quality — because the same content in two different document formats gives you
very different results, and knowing why saves you a lot of frustration.

Then the part that matters most: checking whether an answer is genuinely supported by the
sources, or whether it just looks like it is. That distinction is the whole session.

Then you build one.
""")

# ═══════════════════════════════════════════════════════════ part 1 — the problem
section_slide(
    prs, 1, "Why It Fails on Your Material",
    notes="""
Part one. Naming the problem precisely.
""")

content_slide(
    prs, "Three Reasons It Cannot Know Your Material",
    [
        ("It was never in the training data.", None, "bold"),
        (1, "Internal protocols, institutional regulations, unpublished documents, anything behind a login", None),
        ("It is newer than the knowledge cut-off.", None, "bold"),
        (1, "Guidelines updated last month; a regulation amended this year", None),
        ("It exists publicly, but thinly.", None, "bold"),
        (1, "Turkish-language professional material, local procedure, specialist practice — present, but sparse", None),
        "",
        ("In all three cases the answer is confident and the confidence means nothing.", None, "bold"),
    ],
    notes="""
Three reasons, and they need different responses, so it's worth distinguishing them.

It was never in the training data at all. Your hospital's internal protocol. Your faculty's
regulations. Anything behind a login, anything unpublished, anything internal. There is
simply no signal.

It's newer than the knowledge cut-off. Guidelines updated last month. A regulation amended
this year. The model isn't reading the news; it stopped learning at a date.

Or it exists publicly, but thinly. Turkish-language professional material, local procedure,
specialist practice. Present in the training data, but sparse — which after week three you
know is the most dangerous case of the three, because there's enough signal to produce
something confident and not enough to produce something reliable.

And the bold line, which is why all three matter equally: in every case the answer is
confident, and the confidence means nothing. You cannot distinguish these three situations
from the output. They all look the same.
""")

callout_slide(
    prs,
    "You cannot prompt your way to information the model does not have.",
    "\"Be accurate\" and \"only use reliable sources\" do not create knowledge. They only change tone.",
    notes="""
This slide exists because I know some of you have been doing this.

You cannot prompt your way to information the model does not have.

"Be accurate." "Only use reliable sources." "Do not make anything up." "You are an expert in
Turkish employment law."

None of these create knowledge. Not one. What they do is change the tone of the output, and —
this is the genuinely dangerous part — they often make it sound *more* authoritative, because
you've asked for authority and authority is a style.

Think about the mechanism. You've adjusted the probability distribution towards text that
reads as careful and expert. You have not added a single fact. The result is a more confident
wrong answer.

I want this to land, because it's the most common mistake made by people who are otherwise
good at this. Prompting is powerful for shaping, structuring, and constraining. It is
completely powerless against absent information.

The only fix is to supply the information. Which is grounding.
""")

# ═══════════════════════════════════════════════════════ part 2 — what grounding is
section_slide(
    prs, 2, "What Grounding Is",
    notes="""
Part two. The concept, which is simpler than the terminology suggests.
""")

flow_slide(
    prs, "Grounding, Conceptually",
    [
        ("You ask", "\"What is the notice period for this contract?\""),
        ("Relevant passages are found", "The system searches your documents and pulls out the parts that look relevant."),
        ("They go into the context", "Those passages are placed in the window alongside your question."),
        ("It answers from what is there", "The model predicts an answer with your text in front of it, not from memory."),
    ],
    caption="You may see this called RAG — retrieval-augmented generation. That is all the phrase means.",
    notes="""
Here's the whole idea. Four boxes.

You ask a question. The system searches your documents and pulls out the passages that look
relevant. Those passages get placed into the context window alongside your question. And then
the model answers with your text in front of it, rather than from memory alone.

That's it. That is grounding.

Read the caption: you may see this called RAG, retrieval-augmented generation. People say it
in a way that suggests deep technical machinery. That is all the phrase means — retrieve
relevant text, add it to the context, then generate.

Now, the honest analogy. Remember week three: the model has no memory outside the context.
Grounding is putting the textbook on the desk before you ask the question. It's an open-book
exam instead of a closed-book one.

And I want you to hold onto that analogy, because it predicts the failures. Think about what
can go wrong in an open-book exam. You might grab the wrong page. The book might not contain
the answer, and you might write something anyway. You might read the right page and
misunderstand it.

Every failure mode of grounding is one of those three. We'll come back to this.
""")

content_slide(
    prs, "What This Changes — and What It Does Not",
    [
        ("What it fixes:", None, "bold"),
        (1, "Material the model never saw, or saw thinly, or that changed after the cut-off", None),
        (1, "You can now point at where an answer came from — the biggest practical gain", None),
        "",
        ("What it does not fix:", None, "bold"),
        (1, "It can still answer from memory when your documents do not contain the answer", None),
        (1, "It can still misread a passage it did retrieve", None),
        (1, "If your source is wrong or out of date, you now have a confident wrong answer with a citation attached", None),
        "",
        ("Grounding changes where the answer comes from. It does not install a truth check.", None, "bold"),
    ],
    notes="""
Be precise about what you're buying.

What it fixes: material the model never saw, saw thinly, or that changed after the cut-off.
That's the big one. And you can now point at where an answer came from, which is the largest
practical gain in this entire course — you've converted an unverifiable claim into a
verifiable one.

What it does not fix. Three things.

It can still answer from memory when your documents don't contain the answer. Nothing forces
it to use only what you gave it. This is the single most important thing to remember today.

It can still misread a passage it did retrieve.

And if your source is wrong or out of date, you now have a confident wrong answer *with a
citation attached* — which is worse than before, because the citation makes it more
persuasive to you and to whoever you show it to.

The bold line: grounding changes where the answer comes from. It does not install a truth
check. There is still no step where anything is verified. We've improved the inputs, not the
mechanism.
""")

boxes_slide(
    prs, "What Makes a Document Easy or Hard to Ground On",
    [
        ("Easy",
         "Real text, not scanned images. Clear headings. Short, self-contained sections. "
         "Consistent terminology. One topic per section. Tables with proper headers."),
        ("Hard",
         "Scanned PDFs where the text is a picture. Information spread across many pages. "
         "Meaning carried by layout — columns, boxes, indentation. Pronouns referring back "
         "across pages."),
        ("Practical fixes",
         "Split a large document into topic-sized pieces. Give each a descriptive heading. "
         "Convert scans to real text first. Remove irrelevant material — it competes for "
         "retrieval."),
    ],
    notes="""
Source quality. This is the difference between grounding that works and grounding that
frustrates you, and almost nobody tells you about it.

Easy: real text rather than scanned images. Clear headings. Short, self-contained sections.
Consistent terminology — if your document calls the same thing three different names,
retrieval suffers. One topic per section. Tables with proper headers.

Hard: scanned PDFs where the text is actually a picture — very common with older institutional
documents, and it may extract nothing at all. Information spread across many pages, so no
single retrieved passage contains the answer. Meaning carried by layout, like columns or boxes
or indentation, all of which flatten out. And pronouns referring back across pages — "as
described above" is useless when the passage is retrieved on its own.

That last one is worth dwelling on. Retrieval pulls out a passage. If the passage says "this
requirement applies in the cases listed above," and "above" wasn't retrieved, the model has a
sentence that means nothing and it will interpret it anyway.

Practical fixes on the right. Split large documents into topic-sized pieces. Give each a
descriptive heading. Convert scans to real text. And remove irrelevant material — it competes
for retrieval and crowds out what you wanted.
""")

# ═══════════════════════════════════════════════════════ part 3 — checking
section_slide(
    prs, 3, "Checking Whether It Actually Used Your Sources",
    notes="""
Part three. The heart of the session.
""")

content_slide(
    prs, "The Instruction That Does Most of the Work",
    [
        ("Put this in every grounded assistant you build:", None, "bold"),
        "",
        (1, "\"Answer only from the documents provided.\"", None),
        (1, "\"After each claim, quote the sentence from the source that supports it.\"", None),
        (1, "\"If the documents do not contain the answer, reply exactly: NOT IN SOURCES — and nothing else.\"", None),
        "",
        ("Why the third line matters most:", None, "bold"),
        (1, "It gives the honest answer a fixed, likely form — the fallback principle from Week 5", None),
        (1, "\"NOT IN SOURCES\" is easy to spot when skim-reading. \"I could not find specific information\" is not.", None),
    ],
    notes="""
Three instructions. Put these in every grounded assistant you build. Write them down.

"Answer only from the documents provided."

"After each claim, quote the sentence from the source that supports it."

"If the documents do not contain the answer, reply exactly: NOT IN SOURCES — and nothing else."

Now, why the third line matters most, and it's the fallback principle from week five doing its
work again.

You're giving the honest answer a fixed, likely form. Not asking the system to be truthful —
making the truthful output the probable one, because there's now a specific short string that
fits the situation.

And there's a second reason, which is about you rather than the model. "NOT IN SOURCES" in
capitals is easy to spot when you're skim-reading at four in the afternoon. Compare that with
"I could not find specific information about this in the provided documents, however, based on
general principles..." — which is the same admission, buried in a paragraph, followed by an
answer anyway. You will read past that. Everyone does.

Make the refusal short, fixed, and visually obvious. That's a design decision about your own
attention, and it matters as much as the instruction itself.
""")

content_slide(
    prs, "The Quote Test",
    [
        "Asking for a quotation is the single most useful verification move available to you",
        "",
        ("It converts an unverifiable claim into a checkable one:", None, "bold"),
        (1, "\"The notice period is 30 days\" — you must trust it or read the whole document", None),
        (1, "\"The notice period is 30 days. Source: 'Either party may terminate on thirty (30) days written notice.' (clause 12.4)\" — you can check this in seconds", None),
        "",
        ("But you must actually check.", None, "bold"),
        (1, "A quotation can be fabricated, or real but from the wrong place, or real but not supporting the claim made", None),
        (1, "Search your document for the quoted string. If it is not there, everything else is suspect.", None),
    ],
    notes="""
The quote test. Single most useful verification move available to you, and it's free.

Look at the two versions. "The notice period is 30 days." To check that, you either trust it
or you read the whole contract. Those are your options.

"The notice period is 30 days. Source: 'Either party may terminate on thirty days written
notice.' Clause 12.4." Now you can check it in about five seconds. Search for the string. Look
at clause 12.4. Done.

You've converted an unverifiable claim into a checkable one. That's the whole game.

But — bold line — you must actually check. And I know how this goes: the presence of a
quotation feels like verification, so people stop there. The quote marks do the reassuring and
nobody looks.

Three ways a quotation fails. It can be fabricated outright. It can be real but from the wrong
place — a genuine sentence from your document that doesn't say what the claim says. Or it can
be real and correctly located and simply not support the claim being made, which is the
subtlest and the most common.

The check is quick: search your document for the quoted string. If it isn't there, stop
trusting everything else in that answer too.
""")

content_slide(
    prs, "The Three Instructions in Action",
    [
        ("Question:", None, "bold"),
        (1, "\"What is the maximum period for submitting an appeal?\"", None),
        "",
        ("A good answer looks like this:", None, "bold"),
        (1, "\"Fifteen working days from the date of notification.\"", None),
        (1, "\"Source: 'An appeal shall be lodged within fifteen (15) working days of the date on which the decision is notified.' (Regulation 8.2)\"", None),
        "",
        ("A bad answer looks like this:", None, "bold"),
        (1, "\"Appeals are generally expected to be submitted promptly, typically within two to four weeks of the decision.\"", None),
        (1, "No quotation. No clause. Hedged language. Nothing you can check.", None),
    ],
    notes="""
Let me show you the difference concretely, because it's easy to nod at the three instructions and
still accept a bad answer.

The question: what's the maximum period for submitting an appeal?

A good answer. Fifteen working days from notification. Then the source: a quoted sentence, with a
regulation number. You can search your document for that sentence and find clause 8.2 in about
five seconds. And notice the quotation contains the number, so the answer and its evidence agree
in a way you can see.

Now the bad answer. "Appeals are generally expected to be submitted promptly, typically within
two to four weeks of the decision."

Read it again and notice the tells. "Generally expected." "Typically." A range instead of a
figure. No quotation. No clause number.

That is what answering from memory looks like — and it's plausible, professional-sounding, and
completely useless. If you skim it while thinking about something else, you take away "two to four
weeks" and act on it.

The hedging is the signal. A grounded answer working from an actual passage tends to be more
specific than a remembered one, not less. When the answer goes vague, ask where the quote is.
""")

content_slide(
    prs, "Preparing Documents So Retrieval Works",
    [
        "Fifteen minutes of preparation buys more than any amount of prompt rewriting",
        "",
        (1, "Split a long document into sections of roughly one topic each, with descriptive headings", None),
        (1, "Replace \"as described above\" and \"see section 3\" with the actual content, where you can", None),
        (1, "Convert scanned pages to real text — otherwise nothing is retrievable at all", None),
        (1, "Delete material irrelevant to the questions you will ask; it competes for retrieval", None),
        "",
        ("Then re-run the same questions and compare. This is the fastest improvement available to you.", None, "bold"),
    ],
    notes="""
This slide is the practical one, and it's the thing people skip because it feels like admin
rather than work.

Fifteen minutes of document preparation buys more than any amount of prompt rewriting. Genuinely.
If a grounded assistant is disappointing you, the source is more often the problem than the
prompt.

Four moves.

Split a long document into sections of roughly one topic each, with descriptive headings. This
matters because retrieval pulls passages — if your passages each cover one thing, the right one
gets found.

Replace "as described above" and "see section 3" with the actual content where you can. Remember
why: a retrieved passage arrives on its own, and a cross-reference to something that wasn't
retrieved is a sentence that means nothing — which the model will interpret anyway.

Convert scanned pages to real text. If the text is a picture, nothing is retrievable at all, and
this is very common with older institutional documents.

And delete material irrelevant to the questions you'll ask. It competes for retrieval and crowds
out what you wanted.

Then re-run the same questions and compare. That comparison is the fastest improvement available
to you in this entire course.
""")

boxes_slide(
    prs, "Three Ways a Grounded Answer Goes Wrong",
    [
        ("Answered from memory",
         "Your documents did not contain it. The model knew something adjacent and used that "
         "instead. Detect it: the answer has no quotation, or a vague one."),
        ("Retrieved the wrong passage",
         "The right words appeared somewhere unrelated. The quotation is genuine and the "
         "conclusion is wrong. Detect it: read the quoted passage in its original context."),
        ("Over-read the passage",
         "The source says something narrower than the answer claims. \"May\" becomes \"must\". "
         "An example becomes a rule. Detect it: compare the strength of the claim with the "
         "strength of the quote."),
    ],
    notes="""
Three failure modes. These map exactly onto the open-book exam analogy from earlier, and I'll
examine you on them.

Answered from memory. Your documents didn't contain it; the model knew something adjacent and
used that. How you detect it: the answer has no quotation, or has a vague gesture instead of a
sentence. If there's no quote, assume memory.

Retrieved the wrong passage. The right words appeared somewhere unrelated — the word "notice"
appears in a clause about notices to third parties, not about termination. The quotation is
completely genuine. The conclusion is wrong. How you detect it: read the quoted passage in its
original context, not in isolation.

And over-read the passage — the subtlest one and my personal favourite for exam questions. The
source says something narrower than the answer claims. "May" becomes "must." "In some cases"
becomes "in all cases." An example becomes a rule. How you detect it: compare the strength of
the claim against the strength of the quote. If the answer is more confident than the sentence
it cites, something has been added.

Learn these three by name.
""")

# ══════════════════════════════════════════════════════════════ build
section_slide(
    prs, 4, "Build",
    notes="""
Part four. Twenty minutes. Everything you need is provided if you didn't bring documents.
""")

activity_slide(
    prs, "Build Your Grounded Assistant",
    [
        ("1.  Choose your sources — three to five short documents.", None, "bold"),
        (1, "Bring your own, or take a pack from me: clinical guideline, statute extract, course regulations, annual report, technical standard.", None),
        ("2.  Load them into any tool that lets you attach documents and ask questions about them.", None, "bold"),
        (1, "Several free assistants do this. Notebook-style tools do it well. Any of them is fine.", None),
        ("3.  Add the three instructions.", None, "bold"),
        (1, "Answer only from the documents · quote the supporting sentence · reply NOT IN SOURCES if absent.", None),
        ("4.  Ask five questions. Check every quotation against the source.", None, "bold"),
    ],
    minutes=20,
    notes="""
Twenty minutes. Four steps.

One. Choose your sources — three to five short documents. Bring your own if you have them.
Otherwise take a pack from me: I have a clinical guideline extract, a statute extract, a set of
course regulations, an annual report, and a technical standard. Pick whichever is closest to
your field. All public material, so no data concerns.

Two. Load them into any tool that lets you attach documents and ask questions about them.
Several free assistants do this directly. Notebook-style tools do it particularly well. Any of
them works — we're doing a general technique, not a product tutorial.

Three. Add the three instructions from earlier. Answer only from the documents. Quote the
supporting sentence. Reply NOT IN SOURCES if it isn't there.

Four, and this is the actual exercise: ask five questions, and check every single quotation
against the source. Not four of them. All five.

[Circulate. The most common thing to catch: people accept a quotation without checking it.
Ask "did you find that sentence?" and watch what happens. If nobody is building, work through
three questions on the provided pack on screen.]
""")

content_slide(
    prs, "What You Probably Found",
    [
        (1, "With the three instructions, it refused at least once — and the refusal was correct", None),
        (1, "Quotations were usually genuine. \"Usually\" is the operative word.", None),
        (1, "At least one answer was broader than the sentence it quoted", None),
        (1, "Questions spanning several documents were answered worse than questions inside one document", None),
        "",
        ("The last one is structural and worth remembering:", None, "bold"),
        (1, "Retrieval pulls passages, not whole documents. Anything requiring you to combine three separate places is fragile.", None),
    ],
    notes="""
What typically happens.

With the three instructions in place, it refused at least once — and when you checked, the
refusal was correct. That's the system working. Notice how much better that feels than a
confident answer you have to disprove.

Quotations were usually genuine. "Usually" is the operative word and it's why you check.

At least one answer was broader than the sentence it quoted. That's over-reading, and it's the
most common of the three failures. If you didn't spot one, look again — go back and compare
each claim with its quote for strength rather than content.

And questions spanning several documents were answered worse than questions inside a single
document.

That last one is structural, and it's the bold line. Retrieval pulls passages, not whole
documents. So a question whose answer requires combining three separate places is fragile —
each piece has to be retrieved, and if one isn't, the model fills the gap.

Practical consequence: ask narrow questions of grounded systems. If you need a synthesis across
sources, do it in steps and check each step. That's a design decision you now know to make.
""")

concepts_slide(
    prs,
    [
        ("Grounding", None, "bold"),
        (1, "Placing relevant passages from chosen sources into the context so the model answers from them rather than from memory. Also called retrieval-augmented generation.", None),
        ("What grounding does and does not do", None, "bold"),
        (1, "Changes where the answer comes from. Does not install a truth check, and does not fix a wrong source.", None),
        ("Why prompting cannot substitute", None, "bold"),
        (1, "Instructions change tone and shape, never available information. \"Be accurate\" adds authority, not facts.", None),
        ("The three verification instructions", None, "bold"),
        (1, "Answer only from sources · quote the supporting sentence · a fixed, visible refusal string.", None),
        ("Three grounded failure modes", None, "bold"),
        (1, "Answered from memory · retrieved the wrong passage · over-read the passage.", None),
    ],
    notes="""
What's examinable from today. Five items, and this week is heavily represented on both exams.

Grounding: placing relevant passages from chosen sources into the context so the model answers
from them rather than memory. Know that RAG means this and nothing more mysterious.

What it does and doesn't do. Changes where the answer comes from. Does not install a truth
check. Does not fix a wrong source — and I may well give you a scenario where the source itself
is out of date and ask what grounding did and didn't help with.

Why prompting cannot substitute. Instructions change tone and shape, never available
information. Expect a question that offers "be accurate" as a tempting wrong answer.

The three verification instructions, and specifically why the refusal string should be fixed
and visible.

And the three grounded failure modes by name: answered from memory, retrieved the wrong
passage, over-read the passage. I'll give you an answer and a source and ask which one it is.
That's a guaranteed exam question, so practise it.
""")

content_slide(
    prs, "Wrap-Up",
    [
        "You cannot prompt your way to information the model does not have — you must supply it",
        "Grounding puts your passages in the context. That is all RAG means.",
        ("It changes where the answer comes from. It does not install a truth check.", None, "bold"),
        "Ask for quotations — then actually check them",
        "Three failures: answered from memory · wrong passage · over-read",
        "",
        ("Next week:", None, "bold"),
        (1, "Verification — you will build ten questions designed to break the thing you made today", None),
    ],
    notes="""
Five things.

You cannot prompt your way to information the model doesn't have. You have to supply it.

Grounding puts your passages into the context at the moment of answering. That's all RAG
means, and you should now be immune to people using the acronym to sound impressive.

It changes where the answer comes from. It does not install a truth check. Please hold both
halves of that sentence.

Ask for quotations, and then actually check them — because the quotation marks feel like
verification and are not verification.

And the three failures: answered from memory, wrong passage, over-read.

Next week we do the thing that makes all of this real. You'll build ten questions designed to
break what you made today — seven it should answer, and three it cannot possibly answer from
your sources. And you'll watch a system you built an hour ago answer those three anyway,
confidently.

I'd rather you saw that here than discovered it at work.

Questions?
""")

closing_slide(
    prs,
    notes="""
Take questions here.

Common ones:

"Which tool is best for this?" — Several work well and they change. What matters is that it
accepts your documents and lets you ask questions about them. Try two; use whichever handles
your file types.

"Can I ground it on a website instead of files?" — Often yes. Same principles apply, plus you
inherit whatever is wrong on the website, and it may change under you without notice.

"Is my document used to train the model?" — Depends entirely on the service and the settings,
and it is genuinely worth reading the terms for anything institutional. That's week twelve, and
it's why today's exercise uses public material.

"What if the model and my document disagree?" — Excellent question and a good sign. Your
document should win — that's the point of grounding — but the disagreement is worth
investigating, because it sometimes means your document is out of date.
""")

save(prs, str(pathlib.Path(__file__).parent / "week07.pptx"))
