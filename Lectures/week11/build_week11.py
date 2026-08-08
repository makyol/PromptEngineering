#!/usr/bin/env python3
"""Week 11 — Domain-Specific Applications.  Artifact: Domain Pack.

Build:  python3 build_week11.py
Output: week11.pptx
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "Theme"))
from theme import *  # noqa

prs = new_deck()

title_slide(
    prs, 11,
    "Domain-Specific Applications",
    "Artifact: the Domain Pack",
    notes="""
Welcome back.

Last week you designed something for your own field. Today we make its output look like work
from your profession rather than work from the internet.

Here's the gap I want to close. A generic assistant will produce something competent and
unmistakably generic. A clinician reads it and knows immediately it wasn't written by a
clinician. A lawyer reads it and knows. Not because the content is wrong — often it's fine —
but because the shape is wrong, the vocabulary is slightly off, and it doesn't do the things
professionals do without thinking about it.

That gap is where the value lives, and it's also where the risk lives, because output that
looks professional gets trusted like professional work.

Today you build a Domain Pack: a glossary, three golden examples, and your field's output
conventions. It's the least glamorous artifact in the course and probably the one you'll
actually reuse.
""")

content_slide(
    prs, "Today: What We'll Explore",
    [
        "Why generic output fails even when it is correct",
        "The Domain Pack: glossary, golden examples, output conventions",
        "Real structures from five fields — SOAP, IRAC, and others",
        ("How professional risk differs by field, and what that changes", None, "bold"),
        "Build: your own Domain Pack",
    ],
    notes="""
Where we're going.

First, why generic output fails even when it's correct. This is a real phenomenon and worth
understanding precisely rather than dismissing as style.

Then the Domain Pack — three components, all of which you can write today.

Then real structures from five fields. SOAP notes, IRAC, and the equivalents in education,
business and engineering. These aren't prompting inventions; they're how those professions
actually organise thought.

Then how professional risk differs by field. A hallucination in a brainstorm is a nuisance. In
a discharge summary it's a safety incident. The same system needs different handling in
different hands, and that changes the design.

Then you build your pack.
""")

# ══════════════════════════════════════════════════════ part 1 — the gap
section_slide(
    prs, 1, "Why Generic Output Fails",
    notes="""
Part one. Naming what's actually wrong with competent generic output.
""")

boxes_slide(
    prs, "Three Things Missing From Generic Output",
    [
        ("Vocabulary that means something local",
         "The same word means different things in different institutions. \"Discharge\", "
         "\"referral\", \"assessment\", \"term\" — each has a precise local meaning the model "
         "averages away."),
        ("The shape professionals expect",
         "A clinician scanning a note looks in fixed places for fixed things. Correct content in "
         "the wrong shape takes longer to read than no note at all."),
        ("What is conventionally left out",
         "Professions have norms about what you do not say — no diagnosis without qualification, "
         "no advice without a disclaimer. Generic output includes everything."),
    ],
    notes="""
Three things missing, and none of them are about accuracy.

Vocabulary that means something local. The same word means different things in different
institutions. "Discharge," "referral," "assessment," "term" — each has a precise local meaning,
and the model has read thousands of conflicting usages and produces something averaged. Not
wrong exactly. Just not yours.

The shape professionals expect. A clinician scanning a note looks in fixed places for fixed
things. If the medication is where the history should be, the note is harder to read than no
note at all, even when every word is correct. Shape is not decoration — it's an index.

And what is conventionally left out. This is the subtle one. Professions have strong norms
about what you don't say. No diagnosis without qualification. No legal advice without a
disclaimer. No prediction about an individual student. Generic output includes everything it
knows, because it has no concept of professional restraint.

That third one is where generic output most often becomes actively dangerous rather than merely
unhelpful — because it says the thing a professional would have known not to say.
""")

content_slide(
    prs, "The Domain Pack",
    [
        ("1.  A glossary — twenty terms, defined as your institution uses them.", None, "bold"),
        (1, "Especially terms that mean something different elsewhere", None),
        ("2.  Three golden examples — real outputs, approved, anonymised.", None, "bold"),
        (1, "One typical, one complex, one edge case. The edge case teaches most.", None),
        ("3.  Output conventions — the structure, and the restraint.", None, "bold"),
        (1, "The required sections, in order. And what must never appear without qualification.", None),
        "",
        ("Written once. Pasted into every prompt afterwards.", None, "bold"),
    ],
    notes="""
Three components.

A glossary. Twenty terms, defined as your institution actually uses them — and especially the
terms that mean something different elsewhere. Those are the high-value ones, because those are
where the averaged meaning is actively wrong rather than merely vague.

Three golden examples: real outputs, approved, anonymised. One typical, one complex, one edge
case. And the edge case teaches most, because it shows what to do when the standard shape
doesn't fit — which is exactly where generic output goes wrong.

And output conventions: the required sections in order, and the restraint. Both halves matter.
The structure is easy to specify and people do it. The restraint — what must never appear
without qualification — is what people forget, and it's what makes output safe rather than
merely well-formatted.

Bold line: written once, pasted into every prompt afterwards. This is a twenty-minute
investment that pays every time you use these tools for the rest of your career. That's why
it's the artifact I most expect you to actually keep.
""")

# ═════════════════════════════════════════════════════ part 2 — five fields
section_slide(
    prs, 2, "Structures From Five Fields",
    notes="""
Part two. Real structures, not prompting inventions.
""")

content_slide(
    prs, "Healthcare and Law",
    [
        ("SOAP — the clinical note", None, "bold"),
        (1, "Subjective: what the patient reports · Objective: what was measured · Assessment: clinical interpretation · Plan: what happens next", None),
        (1, "The discipline is in the S/O split — report and measurement kept apart, so interpretation is visible as interpretation", None),
        "",
        ("IRAC — legal analysis", None, "bold"),
        (1, "Issue: the legal question · Rule: the applicable law · Analysis: applying rule to facts · Conclusion", None),
        (1, "The discipline is that the rule is stated before it is applied — so a missing or wrong rule is visible", None),
    ],
    notes="""
Two structures, and I want to point at why each one exists rather than just listing the letters.

SOAP, the clinical note. Subjective — what the patient reports. Objective — what was measured.
Assessment — the clinical interpretation. Plan — what happens next.

The discipline is in the S/O split. What the patient said and what the instrument measured are
kept apart, deliberately, so that interpretation is visible as interpretation rather than
blending into fact. That separation is precisely what generic output destroys — it produces a
smooth narrative in which reported and measured are indistinguishable.

So asking for SOAP structure isn't formatting. It's forcing a separation that carries clinical
meaning.

IRAC, legal analysis. Issue, Rule, Analysis, Conclusion.

The discipline here is that the rule is stated before it is applied. Which means a missing rule,
or a wrong one, is visible — you can look at the Rule section and check it. In a flowing
paragraph, the rule is implicit and unverifiable.

Both structures do the same job: they make a specific kind of error visible. That's what makes
them worth using with these tools, given everything you know about how confident wrong output
looks.
""")

content_slide(
    prs, "Education, Business, Engineering",
    [
        ("Education — objective, activity, assessment", None, "bold"),
        (1, "What should the learner be able to do; what will they do; how will you know. The discipline is that the objective is measurable.", None),
        ("Business — situation, implication, recommendation", None, "bold"),
        (1, "The discipline is that a recommendation must be traceable to a stated fact, not to a general impression.", None),
        ("Engineering — requirement, constraint, acceptance criteria", None, "bold"),
        (1, "The discipline is that \"done\" is defined before work starts, in terms someone else could check.", None),
        "",
        ("In every case the structure exists to make a particular error visible.", None, "bold"),
    ],
    notes="""
Three more, briefly.

Education: objective, activity, assessment. What should the learner be able to do, what will
they do, and how will you know. The discipline is that the objective must be measurable — and
this is exactly where generic output fails, producing objectives like "understand
photosynthesis," which cannot be assessed and therefore isn't an objective.

Business: situation, implication, recommendation. The discipline is that a recommendation has
to be traceable back to a stated fact, not to a general impression. Which is a defence against
exactly the failure we saw in week one — the invented statistic supporting a confident
conclusion.

Engineering: requirement, constraint, acceptance criteria. The discipline is that "done" is
defined before work starts, in terms somebody else could check.

And the bold line ties them together: in every case the structure exists to make a particular
error visible. That's the general principle, and it's why I said in week four that a structure
helps when it matches how work is really done.

So when you write your own conventions, ask: what error does this shape catch? If the answer is
"none, it just looks organised," you've got formatting rather than structure.
""")

content_slide(
    prs, "A Domain Pack, Written Out",
    [
        ("Glossary (extract)", None, "bold"),
        (1, "\"Referral\" = transfer to a named consultant, not a request for advice. Advice requests are \"consultations\".", None),
        (1, "\"Discharge\" = discharge from the ward, not from the service. Discharge from the service is \"closure\".", None),
        ("Output conventions", None, "bold"),
        (1, "Sections in order: reason for referral · relevant history · current medication · specific question asked.", None),
        (1, "Maximum one page. No abbreviations except those in the glossary.", None),
        ("Restraint — the \"never\" statements", None, "bold"),
        (1, "Never state a diagnosis. Never suggest a medication change. Never include anything not stated in the source notes.", None),
    ],
    notes="""
Here's a pack written out, so you can see the shape rather than the description.

Glossary. Two entries, both chosen because the term means something different elsewhere. In this
department, "referral" means transfer to a named consultant — a request for advice is a
"consultation." Get that wrong and you've mislabelled the entire document. And "discharge" means
from the ward, not from the service; leaving the service is "closure."

Neither of those is universal. Both are locally exact. That's what a glossary entry should be.

Output conventions: sections in order — reason for referral, relevant history, current
medication, the specific question being asked. Maximum one page. No abbreviations except those
in the glossary, which is a nice constraint because it makes the glossary do double duty.

And the restraint statements. Never state a diagnosis. Never suggest a medication change. Never
include anything not stated in the source notes.

Read those three again. That's a system prompt that keeps a referral letter within the author's
professional scope. Three sentences. And that's the part that would take a colleague years to
articulate and takes you ten minutes to write down, because you know your field.
""")

content_slide(
    prs, "Writing the Glossary Quickly",
    [
        "The bottleneck is recall, not writing. You know these terms; you cannot list them on demand.",
        "",
        ("Three prompts that surface them:", None, "bold"),
        (1, "What did I have to explain to the last new colleague who joined?", None),
        (1, "What has someone from another department misunderstood in the last year?", None),
        (1, "Which words would mean something different in a textbook than they mean here?", None),
        "",
        (1, "Ten terms is enough to start. The pack improves every time something goes wrong.", None),
    ],
    notes="""
A practical difficulty: the bottleneck is recall, not writing. You know these terms perfectly
well. You cannot list them on demand, because expertise doesn't come with an index — which is
exactly the knowledge bottleneck that killed the age of rules in week two, showing up in your own
life.

Three prompts that surface them reliably.

What did I have to explain to the last new colleague who joined? Whatever you explained is
exactly what isn't obvious, and you have a recent memory of it.

What has someone from another department misunderstood in the last year? Cross-department
misunderstandings almost always come from a term that means two things. Those are your
highest-value entries.

And which words would mean something different in a textbook than they mean here? That's the
gap between the general usage the model learned and your local usage.

Ten terms is enough to start. And the pack improves every time something goes wrong — when
output is subtly off, ask which term it misread, and add that one. After six months you have
something genuinely valuable that nobody sat down to write.
""")

content_slide(
    prs, "Risk Is Not Distributed Evenly",
    [
        "The same output quality carries very different consequences by field",
        "",
        (1, "A fabricated citation in a brainstorm: a nuisance", None),
        (1, "A fabricated citation in a filed legal document: sanctions", None),
        (1, "A fabricated drug interaction in a discharge summary: a safety incident", None),
        (1, "A wrong deadline in a student email: recoverable, unless they miss the resit", None),
        "",
        ("So the same system needs different handling in different hands:", None, "bold"),
        (1, "Higher risk → more constraint, more quoting, earlier human review, narrower scope", None),
    ],
    notes="""
Risk is not distributed evenly, and this is where the cross-disciplinary nature of this room is
genuinely useful — you get to see how differently the same tool sits in different hands.

The same output quality carries very different consequences.

A fabricated citation in a brainstorm: a nuisance. You notice, you move on.

The same fabricated citation in a filed legal document: sanctions. Real ones, imposed on real
lawyers.

A fabricated drug interaction in a discharge summary: a safety incident, and potentially
someone harmed.

A wrong deadline in a student email: recoverable — unless they miss the resit, in which case it
isn't.

Notice that the *system* is identical in all four cases. The failure rate is identical. What
differs entirely is what happens afterwards.

So the bold line: the same system needs different handling in different hands. Higher risk means
more constraint, more quoting, earlier human review, narrower scope.

That's why I can't give this room a single set of rules. What's proportionate for a marketing
draft is negligent for a clinical note, and what's proportionate for a clinical note would make
a marketing workflow useless.

Calibrating that is a professional judgment, and it's yours to make in your own field.
""")

# ══════════════════════════════════════════════════════════════ build
section_slide(
    prs, 3, "Build",
    notes="""
Part three. Twenty minutes. This one needs no tool at all.
""")

activity_slide(
    prs, "Build Your Domain Pack",
    [
        ("1.  Glossary — ten terms minimum.", None, "bold"),
        (1, "Prioritise terms that mean something different outside your institution.", None),
        ("2.  One golden example.", None, "bold"),
        (1, "A real, approved, anonymised output from your field. Anonymise properly — no names, dates or identifiers.", None),
        ("3.  Output conventions — sections in order, plus the restraint.", None, "bold"),
        (1, "\"Never state a diagnosis.\" \"Never cite a case.\" \"Never predict an individual student's result.\"", None),
        ("4.  Add it to your Week 10 design and run one test.", None, "bold"),
        (1, "Compare the output with and without the pack.", None),
    ],
    minutes=20,
    notes="""
Twenty minutes, and this activity needs no tool at all for the first three steps — pen and
paper works.

One. Glossary, ten terms minimum. Prioritise terms that mean something different outside your
institution, because those are where the averaged meaning actively misleads.

Two. One golden example. A real, approved, anonymised output from your field. And anonymise
properly — no names, no dates, no identifiers, no unusual details that would identify someone
in a small population. If you're unsure whether it's anonymous enough, it isn't. Use a textbook
example instead.

Three. Output conventions: sections in order, plus the restraint. And write the restraint as a
"never" statement. "Never state a diagnosis." "Never cite a case." "Never predict an individual
student's result." Those are the lines that make output safe.

Four. Add it to your week ten design and run one test. Compare output with and without the
pack. That comparison is the whole point — most people are surprised by how much changes.

[If nobody is building, write a glossary and conventions on screen for whichever discipline is
best represented, and take terms from the room. This works as a discussion.]
""")

content_slide(
    prs, "What the Pack Changes — and What It Does Not",
    [
        ("What it changes:", None, "bold"),
        (1, "Vocabulary becomes local. Structure becomes recognisable. Restraint appears where it was absent.", None),
        (1, "Output stops looking like the internet and starts looking like your institution", None),
        "",
        ("What it does not change:", None, "bold"),
        (1, "Accuracy. A well-formatted SOAP note can contain a fabricated finding.", None),
        (1, "If anything, professional formatting makes wrong content more persuasive, not less", None),
        "",
        ("A Domain Pack makes output usable. Grounding and testing make it trustworthy. You need all three.", None, "bold"),
    ],
    notes="""
Be precise about what you've bought, because this is the slide where students most often
over-conclude.

What it changes. Vocabulary becomes local. Structure becomes recognisable. Restraint appears
where it was absent. Output stops looking like the internet and starts looking like your
institution.

What it does not change: accuracy. Not at all. A beautifully formatted SOAP note can contain a
completely fabricated finding, sitting in the Objective section, looking exactly like a
measurement.

And read the second sub-point carefully, because it's the uncomfortable one. If anything,
professional formatting makes wrong content *more* persuasive, not less. You've taken output
with a known error rate and dressed it in the visual language of professional authority. A
colleague glancing at it will trust it more than they would have trusted the generic version.

So you've increased both usefulness and risk simultaneously.

Which is why the bold line matters: a Domain Pack makes output usable. Grounding and testing
make it trustworthy. You need all three, and doing only this one leaves you worse off than
doing none.
""")

concepts_slide(
    prs,
    [
        ("The Domain Pack", None, "bold"),
        (1, "Glossary of locally-defined terms · golden examples including an edge case · output conventions including what must never appear.", None),
        ("Why professional structures exist", None, "bold"),
        (1, "Each makes a particular error visible — SOAP separates report from measurement; IRAC states the rule before applying it.", None),
        ("Three gaps in generic output", None, "bold"),
        (1, "Local vocabulary · expected shape · conventional restraint.", None),
        ("Risk varies by field, not by system", None, "bold"),
        (1, "Identical output carries different consequences. Higher risk demands more constraint, more quoting, earlier review.", None),
        ("Formatting is not accuracy", None, "bold"),
        (1, "A Domain Pack makes output usable and more persuasive. It does nothing for correctness — and may increase over-trust.", None),
    ],
    notes="""
What's examinable. Five items.

The Domain Pack and its three components, including the edge-case example and the restraint
statements.

Why professional structures exist — each makes a particular error visible. Be ready to explain
SOAP's S/O split and IRAC's rule-before-application. That's a strong short-answer question.

The three gaps in generic output: local vocabulary, expected shape, conventional restraint.

Risk varies by field rather than by system. Expect a scenario asking why the same assistant
needs different controls in a clinic and a marketing department.

And formatting is not accuracy — with the sting in the tail: professional formatting can
increase over-trust. That's a likely question because it's counterintuitive.
""")

content_slide(
    prs, "Wrap-Up",
    [
        "Generic output fails on vocabulary, shape and restraint — not usually on facts",
        "A Domain Pack is a glossary, golden examples, and output conventions. Written once, reused forever.",
        "Professional structures exist to make specific errors visible",
        ("Formatting makes output usable and more persuasive. It does not make it correct.", None, "bold"),
        "Risk varies by field: higher stakes need more constraint and earlier review",
        "",
        ("Next week:", None, "bold"),
        (1, "Prompt Injection and AI Security — we attack an assistant together and see how easy it is", None),
    ],
    notes="""
Five things.

Generic output fails on vocabulary, shape and restraint — not usually on facts. Which is why
people dismiss the problem as cosmetic and why they're wrong to.

A Domain Pack is a glossary, golden examples, and output conventions. Written once, reused
forever. Genuinely, keep yours.

Professional structures exist to make specific errors visible. That's the design principle
worth carrying.

Formatting makes output usable and more persuasive. It does not make it correct — and the gap
between those two is where professional harm happens.

And risk varies by field. Higher stakes need more constraint and earlier review.

Next week is the one people remember. We attack an assistant together — I've built one for the
purpose and I'd like you to break it. You'll see how little effort it takes, and then we'll fix
it, and then you'll know what to check in anything you build.

Bring a laptop if you can. Questions?
""")

closing_slide(
    prs,
    notes="""
Take questions here.

Common ones:

"Where do I get approved examples?" — Published material from your institution, textbook
examples, or anything already public. If you'd have to anonymise it carefully, use something
else for the classroom.

"Isn't a glossary just a prompt?" — Yes, it's context in the week four sense. The difference is
that it's written once, deliberately, and reused — rather than improvised differently each time.

"What if my institution has no written conventions?" — Very common. Writing your pack is often
the first time anyone has written them down, and that output has value beyond this course.

"Does the pack go in every prompt?" — In every prompt for that task, yes. If it's long, put it
in the persistent instructions of whatever tool you use rather than pasting it each time.
""")

save(prs, str(pathlib.Path(__file__).parent / "week11.pptx"))
