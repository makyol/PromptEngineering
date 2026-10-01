#!/usr/bin/env python3
"""Week 4 — Principles of Effective Prompting.

Build:  python3 build_week04.py
Output: week04.pptx
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "Theme"))
from theme import *  # noqa

prs = new_deck()

title_slide(
    prs, 4,
    "Principles of Effective Prompting",
    "What actually improves results — and what only appears to",
    notes="""
Welcome back.

Last week we went inside the model. Tokens, prediction, context windows, and the sentence I
hope stayed with you: there is no step at which the system checks whether what it says is
true.

Today we use that. Because once you know the mechanism, you can tell the difference between
advice that works for a reason and advice that circulates because it sounds clever.

And there is a great deal of the second kind. If you search for prompt tips you will find
lists of magic phrases, instructions to threaten the model or offer it money, elaborate
acronyms. Some of it helps. Much of it doesn't. And almost none of it explains why.

Today I want to give you a small number of things that work, an explanation of why each one
works given what you now know, and an honest account of what's contested. That last part
matters — I'd rather tell you something is uncertain than pretend the field is tidier than
it is.
""")

content_slide(
    prs, "Today: What We'll Explore",
    [
        "The four levers that reliably change output quality",
        "One structure, taught properly — rather than eight acronyms taught badly",
        "Worked examples from healthcare and law",
        ("What doesn't work, and why the folklore persists anyway", None, "bold"),
        "Prompting as a loop: diagnose, then pull the right lever",
        "Activity: Fix a Bad Prompt",
    ],
    notes="""
Where we're going.

First, four levers. Just four. These are the things that reliably change output quality,
and for each one I'll explain the mechanism, so you're not memorising rules.

Then one structure taught properly. You may have seen lists of prompting frameworks with
memorable acronyms. I'm going to teach you one, thoroughly, and mention the others on a
single slide so you recognise the names. Eight frameworks taught badly is worse than one
framework taught well.

Then worked examples — healthcare and law today.

Then what doesn't work. This section matters as much as the first, because bad advice
costs you time and gives you false confidence.

Then prompting as a loop, which is the part most people skip: when output is wrong, which
lever do you actually pull?

Then you fix a bad prompt.
""")

# ═══════════════════════════════════════════════════════════ part 1 — levers
section_slide(
    prs, 1, "The Four Levers",
    notes="""
Part one. Four levers. Everything else is a combination of these.
""")

callout_slide(
    prs,
    "Most disappointing output is under-specified input.",
    "Not because the model is weak — because your request had many valid answers and it picked one.",
    notes="""
Start here, because it reframes the problem.

Most disappointing output is under-specified input.

And I want to be careful about how I say this, because it can sound like blaming the user.
That's not the point. The point is mechanical.

Think about what happened last week. You give it text, it produces a probability
distribution over continuations. If your request is compatible with many quite different
good answers, then the probability is spread across all of them, and it picks one. It may
be an excellent answer to a question you didn't quite ask.

"Summarise this report" — for whom? At what length? Emphasising what? Every one of those
is unspecified, and every combination is a legitimate reading of your instruction. You had
one in mind. You didn't say it.

So the first move, before any technique, is: what did I leave open that I actually cared
about?

That single question resolves more bad output than every clever phrase on the internet
combined.
""")

flow_slide(
    prs, "The Four Levers",
    [
        ("Context", "What the model needs to know that it cannot infer — audience, situation, constraints, the source material itself."),
        ("Task", "What to do, stated as an instruction. Specific verb, specific scope."),
        ("Format", "What the output should look like — length, structure, sections, table, list."),
        ("Examples", "One or two samples of what good looks like, when describing it is harder than showing it."),
    ],
    caption="Not an acronym. Four questions to ask yourself before pressing Enter.",
    notes="""
Four levers. Context, Task, Format, Examples.

Context: what does the model need to know that it cannot infer? Who is this for, what
situation are we in, what constraints apply, and — critically — the actual source material
if there is any.

Task: what to do, as an instruction. A specific verb and a specific scope. "Summarise" is
a verb but "summarise the three clinical recommendations" is a task.

Format: what should the output look like? Length, structure, sections, a table, a list.
This is the most under-used lever and the cheapest to pull.

Examples: one or two samples of what good looks like. Use this when describing what you
want is harder than showing it — which is more often than people expect.

Read the caption. This is not an acronym you memorise. It's four questions you ask yourself
before pressing Enter. If you can answer all four, your prompt is already better than most
of what gets written.

Let me take them one at a time, with the mechanism for each.
""")

content_slide(
    prs, "Lever 1 — Context",
    [
        "Everything the model needs that it cannot work out from your question alone",
        (1, "Audience: a patient's family, a court, a first-year student, a board", None),
        (1, "Situation: what has already happened, what has been tried, what constraints exist", None),
        (1, "Jurisdiction, institution, country — the single highest-value context in this room", None),
        "",
        ("Why it works, mechanically:", None, "bold"),
        (1, "Context is in the window when the model predicts. It shifts probabilities directly.", None),
        (1, "Saying \"under Turkish law\" makes Turkish-relevant continuations more likely — it does not create knowledge the model lacks", None),
    ],
    notes="""
Lever one: context. Everything the model needs that it can't work out from your question.

Audience is the big one. A summary for a patient's family and a summary for a court are
different documents. If you don't say, you get the average of everything it has read, which
serves nobody.

Situation: what's already happened, what's been tried, what constraints apply.

And jurisdiction, institution, country — which I'd argue is the highest-value context for
this room specifically. After last week, you know why: without it, the probable continuation
is drawn from wherever the training text was densest, which is usually somewhere else.

Now the mechanism, because I promised you mechanisms rather than rules. Context sits in the
window when the model predicts. It directly shifts the probability distribution. That's all
it does — but that's a lot.

And here's the honest limit, in the second bold sub-point. Saying "under Turkish law" makes
Turkish-relevant continuations more likely. It does not create knowledge the model doesn't
have. If it read very little Turkish law, the instruction steers it toward a thin region
rather than a rich one — and it will still answer confidently.

Context steers. It does not supply. Supplying is week seven.
""")

content_slide(
    prs, "Lever 2 — Task",
    [
        "State what to do, with a specific verb and a specific scope",
        "",
        (1, "Weak:  \"Look at this contract.\"", None),
        (1, "Better: \"List every clause that differs from the standard template.\"", None),
        (1, "Better still: \"List every clause that differs from the standard template, and for each one say whether the change favours us or them.\"", None),
        "",
        ("Split compound tasks rather than stacking them.", None, "bold"),
        (1, "\"Summarise, translate, and identify risks\" invites a shallow pass at all three", None),
        (1, "Three separate turns produce better work on each — and let you check each before continuing", None),
    ],
    notes="""
Lever two: task. What to do, with a specific verb and a specific scope.

Look at the progression. "Look at this contract" — that's not a task, that's a gesture.
There are a hundred things it might do.

"List every clause that differs from the standard template" — now there's a verb and a
scope. You could check whether it did it.

"...and for each one say whether the change favours us or them" — now the output is
directly usable, because you've specified the judgment you actually wanted.

Notice what improved. Not the phrasing. The specificity of what counts as success.

Now the bold line, and this is the mistake I see most often in student work: split compound
tasks rather than stacking them.

"Summarise this, translate it, and identify the risks" invites a shallow pass at all three,
because the model is budgeting a single response across three jobs. Three separate turns
produce better work on each — and, more importantly, they let you check each one before
building on it. If the summary is wrong, everything downstream inherits the error.

That's not a prompting trick. That's just how you'd hand work to a person.
""")

content_slide(
    prs, "Lever 3 — Format",
    [
        "Say what the output should look like. This is the cheapest lever and the most neglected.",
        (1, "\"A table with columns: finding, source, confidence\"", None),
        (1, "\"Three bullets, maximum fifteen words each\"", None),
        (1, "\"Two paragraphs, no headings, no bullet points\"", None),
        "",
        ("A structural instruction that pays for itself:", None, "bold"),
        (1, "Ask for a column, section, or sentence recording what the answer is based on", None),
        (1, "It does not guarantee honesty — but it makes the basis visible, so you can check it", None),
        "",
        (1, "Length instructions are approximate. The model counts tokens, not words — Week 3.", None),
    ],
    notes="""
Lever three: format. Say what the output should look like. Cheapest lever, most neglected.

Three examples. A table with named columns. Three bullets with a word cap. Or — and people
forget this direction exists — two paragraphs with no headings and no bullets, when you're
tired of receiving everything as a list.

Now the bold part, because this is the one that connects to the rest of the course.

Ask for a column, a section, or a sentence recording what the answer is based on. "Add a
column: source." "End with one sentence saying which parts you are confident about and
which you are not."

Be clear about what this does and doesn't do. It does not guarantee honesty — the model can
produce a confident-looking source line for something it invented, and we saw exactly that
in week one. What it does is make the basis visible, so there's something concrete for you
to check. You've converted an invisible claim into a checkable one.

That's a real gain, and it costs you eight words.

Last line, from last week: length instructions are approximate, because the model counts
tokens rather than words. "About 200 words" is a steer, not a contract — and it's less
accurate in Turkish.
""")

content_slide(
    prs, "Lever 4 — Examples",
    [
        "Show one or two samples of what good looks like, when describing is harder than showing",
        (1, "Especially effective for tone, structure, and house style — things that resist description", None),
        (1, "One good example usually beats a paragraph of adjectives", None),
        "",
        ("Two cautions:", None, "bold"),
        (1, "It will copy more than you intended — including length, hedging, and quirks of your sample", None),
        (1, "A biased or unrepresentative example produces biased or unrepresentative output, faithfully", None),
        "",
        (1, "Never paste a real patient record, client file or personal document as your example.", None),
    ],
    notes="""
Lever four: examples. Show one or two samples of what good looks like.

This is most effective for exactly the things that resist description — tone, structure,
house style. Try describing your institution's writing style in words. It's hard. Now paste
two paragraphs of it. Much easier, and much more effective. One good example usually beats a
paragraph of adjectives.

Two cautions.

It will copy more than you intended. Length, hedging, the particular way your sample opens,
any quirk that happens to be present. If your example is 300 words, you'll tend to get 300
words. If your example hedges everywhere, you'll get hedging. The model can't tell which
features you meant to demonstrate.

And a biased or unrepresentative example produces biased output, faithfully. If your two
examples both happen to describe the same kind of case, you've narrowed the output without
realising you did it.

And the last line is not a caution, it's a rule for this course: never paste a real patient
record, client file, or personal document as your example. Week twelve explains exactly what
can happen to it. For now: don't.
""")

# ══════════════════════════════════════════════════════════ part 2 — structure
section_slide(
    prs, 2, "One Structure, Properly",
    notes="""
Part two. One structure, taught properly.
""")

content_slide(
    prs, "A Prompt That Uses All Four",
    [
        ("Context", None, "bold"),
        (1, "\"You are helping a hospital communications team in Turkey. The reader is an adult family member with no medical training.\"", None),
        ("Task", None, "bold"),
        (1, "\"Rewrite the discharge instructions below so the family can follow them at home. Do not add any advice that is not in the original.\"", None),
        ("Format", None, "bold"),
        (1, "\"Short paragraphs under each of: medicines, activity, warning signs, follow-up. End with one line listing anything in the original you could not make simpler.\"", None),
        ("Examples", None, "bold"),
        (1, "\"Match the tone of the sample letter below.\"  [paste sample]", None),
    ],
    notes="""
Here is a prompt that uses all four levers. Read it while I talk.

Context: who this is for, where we are, what the reader knows. A hospital communications
team in Turkey; the reader is an adult family member with no medical training. Notice how
much that constrains — reading level, vocabulary, tone, and jurisdiction, all in one
sentence.

Task: rewrite the discharge instructions so the family can follow them at home. And then a
crucial constraint — do not add any advice that is not in the original. That line is doing
safety work. Without it, a model asked to make medical instructions clearer will happily
add helpful-sounding advice that nobody prescribed.

Format: named sections — medicines, activity, warning signs, follow-up. And then the line I
told you pays for itself: end with one line listing anything in the original you could not
make simpler. That surfaces exactly the parts a human needs to look at.

Examples: match the tone of this sample letter.

That's the whole method. No acronym, no magic words. Four questions, answered.

And notice: you could hand this prompt to a colleague and they'd know what you wanted. That's
a decent test of whether a prompt is well-specified.
""")

content_slide(
    prs, "The Same Structure, Legal",
    [
        ("Context", None, "bold"),
        (1, "\"You are assisting a junior lawyer. The governing law is Turkish. The client is a small business.\"", None),
        ("Task", None, "bold"),
        (1, "\"Using only the contract text below, list every obligation that falls on our client, with the clause number for each.\"", None),
        ("Format", None, "bold"),
        (1, "\"A table: obligation, clause number, deadline if stated, exact quoted wording.\"", None),
        ("Constraint that does real work", None, "bold"),
        (1, "\"If something is implied but not stated, put it in a separate list headed 'not explicit in the text'.\"", None),
    ],
    notes="""
The same structure, different discipline. And I want to draw your attention to one line in
particular.

Context: a junior lawyer, Turkish governing law, a small business client.

Task: using only the contract text below — that phrase matters enormously — list every
obligation on our client, with the clause number for each. Asking for clause numbers is a
format choice that doubles as a verification tool, because a clause number is checkable in
about four seconds.

Format: a table with obligation, clause number, deadline, and the exact quoted wording.
That last column is the one I'd fight for. Quoted wording means you can check the claim
against the source without re-reading the whole contract.

And then the constraint that does real work: if something is implied but not stated, put it
in a separate list headed "not explicit in the text."

Think about what that does. Without it, inferences and quotations arrive mixed together in
one confident list, and you can't tell which is which. With it, the model has been given a
place to put its inferences — so it's less likely to smuggle them in among the facts.

That's a general technique and it's worth stealing: give the model a designated place to put
the uncertain material, and it will tend to use it.
""")

boxes_slide(
    prs, "Frameworks You Will See Named",
    [
        ("CO-STAR",
         "Context, Objective, Style, Tone, Audience, Response. A more granular version of the "
         "same idea — it splits Format into style, tone and response shape."),
        ("RACI, SMART, IDEA and others",
         "Mostly project-management or goal-setting acronyms borrowed and applied to prompts. "
         "They rearrange the same four levers. None has strong evidence over the others."),
        ("IRAC — the exception",
         "Issue, Rule, Analysis, Conclusion. Not a prompting framework — a genuine legal "
         "reasoning structure. Worth using because lawyers actually think that way."),
    ],
    notes="""
You will encounter these names, so here they are once.

CO-STAR: Context, Objective, Style, Tone, Audience, Response. It's a more granular version
of what we just did — it splits Format into style, tone, and response shape. If you like
more structure, use it. It isn't teaching you anything new.

RACI, SMART, IDEA, and a dozen others. Mostly project-management or goal-setting acronyms
that were borrowed and applied to prompting. They rearrange the same four levers with
different letters. I'm not aware of good evidence that any of them outperforms the others,
and I'd be sceptical of anyone claiming otherwise.

IRAC is the exception, and it's worth knowing why. Issue, Rule, Analysis, Conclusion is not
a prompting framework at all — it's how lawyers are trained to reason. Asking for output in
IRAC form works because it matches the actual structure of legal analysis, so the output
lands in a shape a lawyer can use.

That's the general principle worth taking away. A structure helps when it matches how work is
really done in your field — SOAP notes in medicine, IRAC in law, lesson objectives in
teaching. A structure invented to have a nice acronym helps much less.
""")

# ════════════════════════════════════════════════════════════ part 3 — folklore
section_slide(
    prs, 3, "What Doesn't Work",
    notes="""
Part three. This section is as valuable as the first one.
""")

content_slide(
    prs, "Folklore",
    [
        ("Politeness — \"please\", \"thank you\"", None, "bold"),
        (1, "Evidence is mixed and effects are small. Be polite if you like; don't count on it.", None),
        ("Incentives and threats — offering money, urgency, consequences", None, "bold"),
        (1, "Circulated widely; evidence is weak and inconsistent across models.", None),
        ("Magic phrases — \"take a deep breath\", \"think step by step\"", None, "bold"),
        (1, "Some had measurable effects on particular models at particular times. They are not durable.", None),
        ("Stacked role-play — \"you are a world-class expert with 30 years of experience\"", None, "bold"),
        (1, "A role helps by setting register and vocabulary. Piling on superlatives adds nothing.", None),
    ],
    notes="""
Four things you'll be told to do, with an honest account of each.

Politeness. Please and thank you. The evidence is genuinely mixed and any effects reported
are small. Be polite if it feels right to you — I am, out of habit — but don't build a
method on it.

Incentives and threats. Offering the model money, inventing urgency, threatening
consequences. This circulated very widely a few years ago. The evidence is weak and doesn't
hold consistently across models. I'd let it go.

Magic phrases. "Take a deep breath." "Think step by step." Some of these did have
measurable effects on particular models at particular times — that's real, it was
published. But they are not durable, and as models change, phrases that once helped can
become neutral or counterproductive.

And stacked role-play. "You are a world-class expert with thirty years of experience and
three doctorates." A role genuinely helps — it sets register and vocabulary, and that's a
real effect. But piling superlatives on top adds nothing. "You are a paediatric nurse
explaining this to a parent" is more useful than "you are the world's greatest
paediatrician," because the first specifies a situation and the second specifies flattery.
""")

content_slide(
    prs, "Why Folklore Persists",
    [
        "You changed something and the output improved. So the change worked — didn't it?",
        "",
        (1, "Output varies between runs even with an identical prompt — Week 3", None),
        (1, "Any change you make is accompanied by a fresh roll of the dice", None),
        (1, "You will usually also have rewritten other things at the same time", None),
        (1, "And you are judging the result yourself, having hoped it would improve", None),
        "",
        ("Change one thing at a time, and compare across several runs before believing it.", None, "bold"),
        (1, "That is the whole method of Week 8, applied to your own prompting.", None),
    ],
    notes="""
So why does bad advice survive? This slide is really about how to evaluate anything, not
just prompts.

Somebody adds a magic phrase, the output gets better, and they conclude the phrase worked.
Reasonable inference. Usually wrong. Four reasons.

First — from last week — output varies between runs even with an identical prompt. There is
deliberate randomness in the selection.

Second, and this follows: any change you make comes with a fresh roll of the dice. You
cannot tell whether the improvement came from your change or from the roll.

Third, you will usually have rewritten other things at the same time. People rarely change
exactly one word. They rewrite the prompt, add the magic phrase, and attribute the
improvement to the phrase.

And fourth, you are judging the result yourself, having hoped it would improve. That's not a
criticism of you; it's how everyone works.

So: change one thing at a time, and compare across several runs before believing it.

That's the bold line, and notice it's not really prompting advice. It's experimental method.
Week eight is that idea applied systematically — and the reason I'm previewing it here is
that you should apply it to me too. If I tell you something works, ask how I'd know.
""")

# ══════════════════════════════════════════════════════════ part 4 — the loop
section_slide(
    prs, 4, "Prompting Is a Loop",
    notes="""
Part four. The part most people skip.
""")

flow_slide(
    prs, "Diagnose Before You Rewrite",
    [
        ("Run", "Get output. Read it properly rather than skimming for the shape you expected."),
        ("Diagnose", "Name what is wrong — not 'it's bad', but which of the four levers failed."),
        ("Pull one lever", "Change the single thing your diagnosis points at."),
        ("Compare", "Judge against the previous version, not against your hopes."),
    ],
    caption="Most people rewrite the whole prompt from scratch and learn nothing. The diagnosis is where the skill lives.",
    notes="""
Here's the loop, and the second box is the one that matters.

Run: get output, and read it properly. Not skim it for the shape you expected — actually
read it. Most errors survive because nobody looked.

Diagnose: name what's wrong. Not "it's bad" — which of the four levers failed? Was
information missing? Was the task ambiguous? Was the shape wrong? Did it need an example?

Pull one lever: change the single thing your diagnosis points at.

Compare: judge against the previous version, not against what you were hoping for.

And read the caption, because it's the honest description of what people actually do. Most
people, when output is disappointing, rewrite the entire prompt from scratch. Sometimes the
new one is better. But they've learned nothing transferable, because they don't know which
change helped, so next time they start from scratch again.

The diagnosis is where the skill lives. Everything else is typing.
""")

boxes_slide(
    prs, "Which Lever Do You Pull?",
    [
        ("Wrong shape or length",
         "Too long, wrong structure, bullets when you wanted prose, a wall of text. → Format. "
         "The cheapest fix and the most common problem."),
        ("Right shape, wrong content",
         "It answered a slightly different question, or assumed the wrong reader, country or "
         "situation. → Context, or a sharper Task verb and scope."),
        ("Correct but lifeless",
         "Accurate, complete, and reads like nothing you would send. → Examples. Show it two "
         "paragraphs of the real thing."),
    ],
    notes="""
A diagnostic table. I'd photograph this one.

Wrong shape or length. It's too long, or it's a wall of text, or it gave you bullets when
you wanted prose. That's Format. Cheapest fix, most common problem, and people almost never
reach for it — they rewrite the task instead, which doesn't touch the actual issue.

Right shape, wrong content. The structure is fine but it answered a slightly different
question, or assumed the wrong reader, or the wrong country. That's Context, or it's a
sharper Task — you need a more specific verb and scope.

Correct but lifeless. This is the frustrating one. Everything is accurate and complete and
it reads like nothing you would ever send to anyone. That's Examples. Stop describing the
tone and paste two paragraphs of the real thing.

Three diagnoses, three different fixes. If you learn only this slide today, you'll get more
out of these tools than most people do.
""")

# ═══════════════════════════════════════════════════════════════ activity
section_slide(
    prs, 5, "Activity: Fix a Bad Prompt",
    notes="""
Part five. Ten minutes.
""")

activity_slide(
    prs, "Fix a Bad Prompt",
    [
        ("Here is a genuinely bad prompt:", None, "bold"),
        (1, "\"Write something about data protection for our staff.\"", None),
        "",
        ("1.  Name what is missing, lever by lever.", None, "bold"),
        (1, "What context is absent? What exactly is the task? What shape should it take? Would an example help?", None),
        ("2.  Rewrite it using all four levers.", None, "bold"),
        ("3.  If you have a device, run both and compare.", None, "bold"),
        (1, "If not, compare your rewrite with the one on the next slide.", None),
    ],
    minutes=10,
    notes="""
Ten minutes. Here's a genuinely bad prompt, and it's bad in a very ordinary way — this is
the kind of thing people actually type.

"Write something about data protection for our staff."

Step one. Name what's missing, lever by lever. What context is absent? What exactly is the
task — what does "write something" mean? What shape should the output take? Would an example
help?

Step two. Rewrite it using all four levers.

Step three. If you have a device, run both and compare. If not, compare your rewrite against
mine on the next slide — and I'd genuinely encourage you to write yours down first, because
comparing is much more useful than reading.

[Two minutes of quiet writing, then move on. If anyone wants to read theirs out, take one or
two — but don't wait for volunteers.]
""")

content_slide(
    prs, "One Way to Fix It",
    [
        ("What was missing:", None, "bold"),
        (1, "Context — which staff, which country, what data, what triggered this", None),
        (1, "Task — \"write something\" is not a task. Inform? Instruct? Warn? Train?", None),
        (1, "Format — length, structure, whether it is an email, a poster, a policy", None),
        "",
        ("A rewrite:", None, "bold"),
        (1, "\"Our clinic administrative staff in Turkey handle patient records daily; most have no formal data-protection training. Write a one-page internal briefing telling them what they may and may not put into public AI chat tools. Four sections: what is at risk, three things never to do, three safe alternatives, who to ask. Plain language, no legal citations, under 400 words.\"", None),
    ],
    notes="""
Here's one way to fix it. Not the only way.

What was missing. Context: which staff, in which country, handling what data, and what
prompted this being written at all. Task: "write something" isn't a task — did we want to
inform, instruct, warn, or train? Those produce four different documents. Format: nothing at
all was specified.

And here's a rewrite. Read it while I point at the parts.

Context: clinic administrative staff, in Turkey, handling patient records daily, most with
no formal training. Four facts, each of which changes the output.

Task: write a one-page internal briefing telling them what they may and may not put into
public AI chat tools. Specific verb, specific scope, specific decision the reader needs to
make.

Format: four named sections, plain language, no legal citations, under 400 words. Notice
"no legal citations" — that's a negative constraint doing real work, because a model asked
about data protection will reach for regulation names, and after week three you know how
reliable it will be about the specifics of Turkish regulation.

No examples in this one, because the format spec is doing enough work. Four levers, and you
use the ones you need.

Compare that with "write something about data protection for our staff." Same intent.
Entirely different output.
""")

content_slide(
    prs, "Wrap-Up",
    [
        "Most disappointing output is under-specified input",
        "Four levers: Context, Task, Format, Examples — ask four questions, not one acronym",
        "Format is the cheapest lever and the most neglected; ask for the basis of the answer",
        ("Change one thing at a time, or you learn nothing about what worked", None, "bold"),
        "Diagnose before rewriting: wrong shape → Format; wrong content → Context or Task; lifeless → Examples",
        "",
        ("Next week:", None, "bold"),
        (1, "Controlling Style, Tone and Format — precise control over how it sounds, not just what it says", None),
    ],
    notes="""
Five things.

Most disappointing output is under-specified input. Start there before reaching for
technique.

Four levers: Context, Task, Format, Examples. Four questions, not an acronym.

Format is the cheapest lever and the most neglected — and ask for the basis of the answer,
because it converts an invisible claim into a checkable one.

Change one thing at a time, or you learn nothing about what worked. That applies to prompts,
and to advice about prompts, including mine.

And diagnose before rewriting. Wrong shape means Format. Wrong content means Context or
Task. Lifeless means Examples.

Next week we go deeper on the third lever — controlling style, tone and format precisely.
How it sounds, rather than what it says. Which matters more than people expect, because most
professional writing fails on register rather than on facts.

Questions?
""")

closing_slide(
    prs,
    notes="""
Take questions here.

Common ones:

"So role-play doesn't work?" — It does, modestly, when the role specifies a real situation:
"a nurse explaining this to a parent" sets vocabulary and register. What doesn't add
anything is stacking superlatives on top.

"Should I write long prompts?" — Long enough to answer the four questions. Length isn't the
goal; specificity is. A precise three-line prompt beats a vague page.

"What if I don't know what format I want?" — Ask for two versions in different formats and
pick. That's a legitimate use of a turn.

"Does this all still work as models change?" — The four levers are about supplying
information the model can't infer, so they should be durable. The folklore is what decays.
That's roughly the test: does this advice have a mechanism, or is it a phrase?
""")

save(prs, str(pathlib.Path(__file__).parent / "week04.pptx"))
