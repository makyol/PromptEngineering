#!/usr/bin/env python3
"""Week 2 — A Brief History of AI, NLP and Large Language Models.

Build:  python3 build_week02.py
Output: week02.pptx
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "Theme"))
from theme import *  # noqa

prs = new_deck()

title_slide(
    prs, 2,
    "A Brief History of AI, NLP and LLMs",
    "How we got here — and why several of the surprises are old",
    notes="""
Welcome back.

Last week we agreed on a sentence: this is a course about working with a system that is
capable, confident, and sometimes wrong. And we agreed on four words — generative AI,
prompt, model, context — and four failure signatures: fabrication, displacement,
omission, overconfidence.

Today is the history. And I know how "history week" sounds. Let me tell you why it's
here.

Almost everything people get badly wrong about where this technology is going comes from
thinking it started in 2022. It didn't. This field is older than most of your parents.
It has been confidently declared solved at least three times, and it has collapsed at
least twice. There is a chatbot from 1966 that fooled people just as thoroughly as
today's systems fool people, for reasons that are worth understanding precisely.

If you know the shape of the last seventy years, you will be much harder to impress and
much harder to alarm. Both of those are useful professionally.

So: seventy years in about an hour.
""")

content_slide(
    prs, "Today: What We'll Explore",
    [
        "The long arc — seventy years in one picture",
        "The age of rules: writing intelligence by hand, and why it stalled",
        "ELIZA, 1966 — the first time people trusted a machine that understood nothing",
        "The turn to data: from writing rules to counting patterns",
        "2017 and the transformer — the idea underneath everything you use",
        "Activity: Date the Technology",
        "Three patterns that keep repeating",
    ],
    notes="""
Where we're going.

First, the long arc — the whole seventy years in one picture, so you have somewhere to
hang everything else.

Then the age of rules. For roughly thirty years, the plan was to write intelligence down
by hand. That approach produced real, useful systems, and then it hit a wall, and the
reasons it hit the wall are still relevant to you.

Then ELIZA, 1966. A program of a few hundred lines that convinced people it understood
them. I want to spend proper time on this one, because the mechanism by which it fooled
people is the same mechanism that fools people now.

Then the turn to data — the shift from writing rules to counting patterns, which is the
single most important conceptual move in the whole story.

Then 2017 and the transformer, the idea underneath every tool you'll use this semester.

Then an activity — no devices needed for this one — and finally three patterns that keep
repeating, which are what I actually want you to leave with.
""")

# ════════════════════════════════════════════════════════════ part 1 — the arc
section_slide(
    prs, 1, "The Long Arc",
    notes="""
Part one. Let's put the whole thing on one slide before we go anywhere near the detail.
""")

timeline_slide(
    prs, "Seventy Years in One Picture",
    [
        ("1950", "Turing asks",     "\"Can machines think?\" — the question, before the field"),
        ("1956", "The name",        "Dartmouth workshop; \"artificial intelligence\" coined"),
        ("1966", "ELIZA",           "A chatbot that understood nothing, and convinced people"),
        ("1997", "Deep Blue",       "Beats the world chess champion — by searching, not learning"),
        ("2017", "Transformers",    "\"Attention Is All You Need\" — the modern architecture"),
        ("2022", "Public release",  "Generative AI reaches ordinary users at scale"),
    ],
    notes="""
Here is the whole story. Six points. Take a moment to look at it.

1950 — Alan Turing asks whether machines can think, before there is a field to ask it in.
1956 — a summer workshop at Dartmouth College gives the field its name. 1966 — ELIZA.
1997 — Deep Blue beats Garry Kasparov at chess. 2017 — the transformer architecture is
published. 2022 — generative AI reaches ordinary people at scale.

Two things I want you to notice immediately.

First, look at the gaps. Forty-seven years between Turing's question and the chess
victory. Twenty years between the chess victory and the transformer. This is not a field
that has been moving fast for seventy years. It's a field that has been mostly slow, with
a few sharp jumps.

Second, look at where 2022 sits. Right at the end. Everything you have personally
experienced of this technology is the last sliver of a very long story. When someone
tells you that AI is brand new, or that nobody could have predicted any of this — they
are describing the last three years of a seventy-year project.

Let's walk it.
""")

content_slide(
    prs, "1950 — The Question Before the Field",
    [
        "Alan Turing, \"Computing Machinery and Intelligence\"",
        (1, "Opens by asking \"Can machines think?\" — then argues the question is too vague to answer", None),
        (1, "Replaces it with a test: can a machine's replies be told apart from a person's?", None),
        "",
        ("Why this still matters to you:", None, "bold"),
        (1, "Turing moved the question from what a machine *is* to what it can *do*", None),
        (1, "Every benchmark since has inherited that move — including the ones used today", None),
        (1, "It also means a system can pass the test without understanding anything", None),
    ],
    notes="""
1950. Alan Turing publishes a paper called "Computing Machinery and Intelligence."

He opens by asking "Can machines think?" — and then does something clever. He argues that
the question is too vague to be answerable, because we can't agree on what "think" means.
So he replaces it with something testable: can a machine's written replies be reliably
told apart from a person's?

That's usually called the Turing test, though he called it the imitation game.

Why does a paper from 1950 still matter to you? Three reasons.

Turing moved the question from what a machine *is* to what a machine can *do*. That move
is still with us. Every benchmark, every evaluation, every "the model scored X percent"
claim you'll ever read inherits that decision. We do not test whether these systems
understand. We test what they produce.

And the third point is the sharp one, and it's the reason this is in week two rather than
week thirteen. If your test is "can it produce output indistinguishable from a person's,"
then a system can pass without understanding anything at all.

Turing knew that. Sixteen years later, somebody demonstrated it.
""")

content_slide(
    prs, "1956 — The Field Gets a Name",
    [
        "A summer workshop at Dartmouth College brings the founding researchers together",
        (1, "John McCarthy coins the term \"artificial intelligence\" for the proposal", None),
        "",
        ("The founding proposal claimed:", None, "bold"),
        (1, "that every aspect of learning and intelligence could be described precisely enough for a machine to simulate it", None),
        (1, "and that significant progress could be made by a small group over a single summer", None),
        "",
        ("The first prediction is still open. The second was wrong by about seventy years.", None, "bold"),
    ],
    notes="""
1956. A summer workshop at Dartmouth College. This is the founding moment — it's where
the field gets organised, and where John McCarthy coins the actual phrase "artificial
intelligence" for the funding proposal.

Read what the proposal claimed. Two things. First, that every aspect of learning and
intelligence could in principle be described precisely enough that a machine could
simulate it. That's a genuine philosophical position and it is still an open question —
serious people still disagree about it.

Second, that significant progress could be made by a small group of researchers working
together over a single summer.

One summer.

That second claim was wrong by roughly seventy years, and we're arguably not done.

I'm not telling you this to mock them. These were serious, brilliant people. I'm telling
you because it's the first instance of a pattern you'll see three more times today: the
core insight is often right, and the timeline is almost always catastrophically
optimistic. Hold onto that. It's the single most useful thing history gives you when
somebody tells you what AI will do by next year.
""")

# ═══════════════════════════════════════════════════════ part 2 — age of rules
section_slide(
    prs, 2, "The Age of Rules",
    notes="""
Part two. The age of rules — roughly the 1950s through the 1980s. Thirty years of trying
to write intelligence down by hand.
""")

content_slide(
    prs, "Writing Intelligence by Hand",
    [
        "The approach: if a human expert can explain what they do, we can encode it as rules",
        (1, "IF the patient has this symptom AND that test result, THEN consider this diagnosis", None),
        "",
        ("It genuinely worked — for a while:", None, "bold"),
        (1, "MYCIN (1970s, Stanford) recommended antibiotic treatments and reportedly matched specialists", None),
        (1, "By the 1980s, \"expert systems\" were a real commercial industry", None),
        "",
        (1, "Note what this required: an expert who could articulate every rule, and someone to write them all down.", None),
    ],
    notes="""
The idea was reasonable. If a human expert can explain what they do, then we can write
down what they explained, and the machine can follow it.

So you build rules. IF the patient has this symptom AND that test result, THEN consider
this diagnosis. Thousands of them.

And it genuinely worked, for a while. MYCIN, developed at Stanford in the 1970s,
recommended antibiotic treatments for blood infections, and in evaluations it performed
comparably to specialists. That's a real result. By the 1980s "expert systems" were an
actual commercial industry with actual revenue.

But look at the last line, because it's where the whole approach dies.

This required an expert who could articulate every rule — every single one, explicitly,
in words. And it required a person to sit with that expert and write them all down.

Now think about your own field for a second. Think about something you know how to do
well. Could you write down every rule you follow? Completely? Including the exceptions,
and the exceptions to the exceptions, and the things you do because something feels
wrong?

Almost nobody can. Most expertise isn't available to the expert as a list of rules. And
that turned out to be the wall.
""")

content_slide(
    prs, "1966 — ELIZA, and the Illusion of Understanding",
    [
        "Joseph Weizenbaum, MIT. A few hundred lines of pattern-matching.",
        (1, "Its best-known script imitated a psychotherapist, which let it deflect almost anything", None),
        (1, "\"I am unhappy.\"  →  \"Do you think coming here will help you not to be unhappy?\"", None),
        "",
        ("It contained no knowledge, no memory, no model of the conversation.", None, "bold"),
        (1, "It matched keywords and reflected sentences back as questions. That is all.", None),
        "",
        ("People confided in it anyway — and did not believe it was that simple.", None, "bold"),
        (1, "Weizenbaum was so disturbed by this that he spent much of his later career arguing against the field.", None),
    ],
    notes="""
1966. Joseph Weizenbaum, at MIT, writes a program called ELIZA. A few hundred lines of
pattern matching.

Its most famous script imitated a Rogerian psychotherapist — and that choice was tactical,
because a therapist who mostly reflects your statements back at you can deflect almost
anything without needing to know what you're talking about.

Look at the example. You type "I am unhappy." It replies "Do you think coming here will
help you not to be unhappy?" It has taken your words, applied a template, and handed them
back as a question.

Here is what ELIZA contained: no knowledge. No memory of the conversation. No model of
you, no model of itself, no representation of what unhappiness is. It matched keywords
and reflected sentences. That is the entire mechanism.

And people confided in it. Genuinely. People disclosed personal problems to it. There are
accounts of people asking to be left alone with it. And crucially, when told how simple it
was, many of them did not believe it — or believed it and kept talking to it anyway.

Weizenbaum was so disturbed by his own program that he spent much of his later career
arguing against the direction of the field. He built the thing, and the reaction to it
frightened him.
""")

boxes_slide(
    prs, "Why ELIZA Matters in 2026",
    [
        ("The illusion is ours",
         "The sense of being understood was produced entirely by the reader, not the program. "
         "Fluent, relevant-sounding language is enough to trigger it. Nothing behind the "
         "language is required."),
        ("It has a name",
         "The tendency to attribute understanding to a system producing plausible language is "
         "called the ELIZA effect — named in 1966, and still the most common error people make "
         "with these tools."),
        ("The systems got better; we did not",
         "Today's systems have vastly more behind the language. But the mechanism that makes "
         "you trust them is the same one that worked on a few hundred lines in 1966."),
    ],
    notes="""
Three reasons this matters to you in 2026.

First: the illusion was ours, not the program's. ELIZA was not trying to deceive anybody —
it had no capacity to try anything. The sense of being understood was manufactured
entirely by the human reading the output. That tells you something uncomfortable: fluent,
relevant-sounding language is by itself sufficient to produce the feeling of being
understood. Nothing needs to be behind it.

Second: this has a name. The ELIZA effect — the tendency to attribute understanding,
intention, and knowledge to a system that is producing plausible language. Named in 1966.
It is still, sixty years later, the single most common error people make with these tools.

Third, and this is the one to write down. The systems got enormously better. We did not.
The psychological mechanism that made people trust ELIZA is exactly the mechanism
operating on you when a modern system gives you a confident, well-structured answer.
Your sense that it knows what it's talking about is not evidence that it does.

That is a direct line from 1966 to last week's failure signatures. Overconfidence works
on us because fluency works on us.
""")

boxes_slide(
    prs, "Why the Age of Rules Ended",
    [
        ("Brittleness",
         "Rules covered the cases someone thought of. Reality kept producing cases nobody "
         "thought of, and the system had no way to degrade gracefully — it simply failed."),
        ("The knowledge bottleneck",
         "Every rule had to be extracted from an expert by hand. Experts could not articulate "
         "most of what they knew. The extraction was slower than the world changed."),
        ("Ambiguity",
         "Ordinary language resists rules. \"He saw the man with the telescope\" has two "
         "readings, and no reasonable set of hand-written rules settles which is meant."),
    ],
    notes="""
So why did it end? Three walls.

Brittleness. The rules covered the cases somebody had thought of. Reality kept producing
cases nobody thought of. And a rule-based system has no way to fail gracefully — it
doesn't produce a slightly worse answer at the edges, it just stops working or produces
nonsense. There's no "roughly right."

The knowledge bottleneck. Every rule had to be extracted from a human expert, by hand,
through interviews. And as we said — experts cannot articulate most of what they know. So
extraction was slow, incomplete, and expensive. Slower, in fact, than the domains
themselves changed. You'd finish encoding the medical guidelines and the guidelines would
have been updated.

And ambiguity. Ordinary language simply resists rules. The classic example: "He saw the
man with the telescope." Did he use a telescope to see the man, or did he see a man who
had a telescope? You resolved that instantly, using context, and no reasonable set of
hand-written rules settles it.

Language is full of this. Every sentence. And that's fatal for an approach built on
writing down explicit rules.
""")

content_slide(
    prs, "The AI Winters",
    [
        "Twice, the field promised far more than it delivered — and funding collapsed",
        (1, "First winter, roughly 1974–1980: government funding cut sharply after critical reviews", None),
        (1, "Second winter, roughly 1987–1993: the specialised AI hardware market collapsed", None),
        "",
        ("What actually caused them was not failure. It was the gap between promise and delivery.", None, "bold"),
        "",
        (1, "1965: \"Machines will be capable, within twenty years, of doing any work a man can do.\" — Herbert Simon", None),
        (1, "1970: \"In from three to eight years we will have a machine with the general intelligence of an average human being.\" — Marvin Minsky", None),
    ],
    notes="""
Twice, the field collapsed. These are called the AI winters.

The first, roughly 1974 to 1980. Government funding was cut sharply on both sides of the
Atlantic after critical reviews concluded the field had not delivered what it promised.

The second, roughly 1987 to 1993, when the market for specialised AI hardware collapsed
and the expert systems industry went with it.

Now read the bold line, because this is the part people get wrong. What caused the winters
was not that the technology failed. Real systems existed and did real work. What caused
them was the gap between what had been promised and what was delivered.

And look at the promises. Herbert Simon, 1965 — a Nobel laureate, one of the most serious
thinkers of the century — machines will be capable, within twenty years, of doing any work
a man can do. Marvin Minsky, 1970, in a magazine interview — in from three to eight years
we will have a machine with the general intelligence of an average human being.

Three to eight years. From 1970.

These were not cranks. These were the leading figures in the field, and they were
spectacularly wrong about timing while being at least partly right about direction.

I want you to remember these two quotes the next time you read a confident prediction
about what AI will do by 2028. Not because the prediction is necessarily wrong — but
because you now know the base rate.
""")

# ══════════════════════════════════════════════════════ part 3 — turn to data
section_slide(
    prs, 3, "The Turn to Data",
    notes="""
Part three. The single most important conceptual shift in the whole story — and the one
that actually explains the tools you'll use in week six.
""")

flow_slide(
    prs, "The Four Eras",
    [
        ("Rules", "Humans write down what to do. Brittle, and limited by what experts can articulate."),
        ("Statistics", "Count patterns in large text collections. Learn what is likely, not what is correct."),
        ("Neural networks", "Learn layered representations from data, rather than being given features."),
        ("Transformers", "Weigh every word against every other word at once. The current architecture."),
    ],
    caption="Each era did not replace the last so much as absorb it. The direction is constant: less hand-written, more learned.",
    notes="""
Here is the whole intellectual arc in four boxes. I'd like you to be able to reproduce
this diagram from memory — it will show up on an exam and it's genuinely the map of the
field.

Rules. Humans write down what to do. Brittle, and limited by what experts can put into
words. That's where we've just been.

Statistics. Instead of writing rules, count patterns across enormous collections of text.
Don't try to encode what is correct — learn what is likely. This is the big move, and I'll
come back to it.

Neural networks. Rather than a human deciding which features of the data matter, the
system learns layered representations directly from the data.

Transformers. Weigh every word against every other word simultaneously. This is the
architecture underneath everything you'll touch this semester.

And read the caption, because it's the thing to actually understand: each era didn't so
much replace the last as absorb it. The direction is constant across seventy years. Less
hand-written. More learned from data. Every single shift goes the same way.
""")

content_slide(
    prs, "From Writing Rules to Counting Patterns",
    [
        "In the late 1980s and 1990s, machine translation research moved from grammar rules to statistics",
        (1, "Instead of encoding how a language works, count how often things co-occur in translated texts", None),
        (1, "The system has no theory of grammar at all. It has counts.", None),
        "",
        ("The uncomfortable result: the systems that knew less about language performed better.", None, "bold"),
        "",
        (1, "A line attributed to IBM's Frederick Jelinek captures the mood of the shift:", None),
        (1, "\"Every time I fire a linguist, the performance of the speech recogniser goes up.\"", None),
        (1, "(Jelinek later said he could not recall saying it in those words — but the field remembered it, which tells you something.)", None),
    ],
    notes="""
Here's the turn, and it happened first in machine translation.

Through the late 1980s and 1990s, researchers at IBM and elsewhere moved from encoding
grammar rules to doing statistics. Instead of writing down how French works and how
English works and how to map between them, you take large collections of the same
documents in both languages, and you count how often things co-occur.

The resulting system has no theory of grammar. None. It has counts.

And here's the uncomfortable result, which is the bold line: the systems that knew less
about language performed better than the systems that had been carefully taught how
language works.

That was genuinely humiliating for a lot of very good linguists, and it produced a famous
line attributed to Frederick Jelinek at IBM: "Every time I fire a linguist, the
performance of the speech recogniser goes up."

I'll note honestly that Jelinek later said he couldn't remember saying it in those words.
But the field remembered it and repeated it for thirty years, and that tells you how the
shift felt to the people living through it.

Why does this matter to you? Because it's the origin of the thing we said in week one:
these systems predict what is likely, not what is true. That property isn't a bug someone
introduced recently. It is the foundational design decision of the entire modern field,
made deliberately, in the 1990s, because it worked better.
""")

content_slide(
    prs, "Meaning as Position: Word Embeddings",
    [
        "From around 2013, a practical way to represent words as positions in a space",
        (1, "Words that appear in similar contexts end up near each other", None),
        (1, "\"Doctor\" sits near \"nurse\" and \"hospital\"; \"bank\" sits awkwardly between money and rivers", None),
        "",
        ("Nobody defined any of these relationships. They fell out of counting context.", None, "bold"),
        "",
        (1, "This is also where bias becomes measurable: if the text associates certain jobs with certain genders, the positions record it", None),
        (1, "The model is not being unfair. It is reporting the shape of what it read.", None),
    ],
    notes="""
Around 2013, a set of practical techniques arrives for representing words as positions in
a mathematical space. You'll hear these called embeddings.

The idea: words that appear in similar contexts end up near each other. "Doctor" ends up
near "nurse" and "hospital." "Bank" ends up sitting awkwardly between money words and
river words, because it genuinely is used both ways.

And the key point, in bold: nobody defined any of those relationships. No one told it that
doctors and nurses are related. It fell out of counting which words appear near which
other words, across an enormous amount of text.

Now the part that matters ethically, and we'll return to it properly in week thirteen.
This is where bias stops being an abstract worry and becomes measurable. If the text a
system reads consistently associates certain occupations with certain genders, then the
positions record that association. You can measure it. You can point at it.

And I want to be precise about what's happening, because students often get this wrong.
The model is not being unfair. It has no capacity to be fair or unfair. It is reporting
the shape of what it read. If the shape of what it read is unjust, the system will
faithfully reproduce that injustice — and it will do so fluently and confidently, which is
exactly what makes it dangerous.
""")

# ═══════════════════════════════════════════════════════ part 4 — transformer
section_slide(
    prs, 4, "2017 and the Transformer",
    notes="""
Part four. The paper that produced the tools you'll use in week six.
""")

content_slide(
    prs, "\"Attention Is All You Need\"",
    [
        "2017. A Google research paper introduces the transformer architecture.",
        (1, "Earlier systems read text roughly in order, one piece at a time, and struggled to carry information far", None),
        (1, "The transformer weighs every word against every other word in the passage at once", None),
        "",
        ("The example that makes it concrete:", None, "bold"),
        (1, "\"The trophy would not fit in the suitcase because it was too large.\"", None),
        (1, "What does \"it\" refer to? Change \"large\" to \"small\" and the answer flips.", None),
        (1, "Resolving that requires weighing distant words against each other — which is what attention does.", None),
    ],
    notes="""
2017. A Google research paper with a memorable title: "Attention Is All You Need." This
is the origin of the architecture underneath essentially every system you will use in this
course.

What problem did it solve? Earlier neural approaches read text roughly in order, one piece
at a time, and they struggled to carry information across long distances. By the end of a
long paragraph, the beginning had faded.

The transformer's move is to weigh every word against every other word in the passage,
simultaneously. That's what "attention" means here — for each word, how much should each
other word matter to understanding it?

Here's the example that makes it concrete, and it's worth doing slowly.

"The trophy would not fit in the suitcase because it was too large."

What does "it" refer to? The trophy. Obviously — you didn't even notice yourself deciding.

Now change one word. "The trophy would not fit in the suitcase because it was too small."

Now "it" is the suitcase. One adjective, at the end of the sentence, flipped what a pronoun
in the middle refers to.

To resolve that, you have to weigh words against each other across the whole sentence. You
cannot do it by reading left to right and forgetting as you go. That is precisely what
attention does, and that is why this architecture won.
""")

content_slide(
    prs, "What Happened When These Got Bigger",
    [
        "The architecture turned out to improve substantially with more data and more computation",
        (1, "This was not obviously going to be true — many approaches stop improving", None),
        "",
        ("At larger scales, capabilities appeared that were not specifically trained for:", None, "bold"),
        (1, "Following instructions given in ordinary language", None),
        (1, "Learning a task from one or two examples in the prompt itself", None),
        (1, "Producing usable translation, summary and code without task-specific training", None),
        "",
        (1, "Whether these are genuinely new abilities or artefacts of how we measure them is still argued about.", None),
    ],
    notes="""
Then something happened that was not guaranteed.

The architecture turned out to keep improving as you gave it more data and more
computation. I want to stress that this was not obviously going to be true. Plenty of
approaches in the history of this field improve for a while and then flatten out. This one
kept going, for longer than most people expected.

And at larger scales, capabilities showed up that nobody had specifically trained for.
Following instructions written in ordinary language. Learning a task from one or two
examples given in the prompt itself. Producing usable translation, summary, and code
without being trained for those tasks individually.

That's the thing that made this different from previous eras. Not that it was better at a
task — that it could do tasks it wasn't built for, described to it in words.

Last line, and I'm being deliberately careful here: whether these are genuinely new
abilities that appear at a threshold, or whether they're artefacts of how we choose to
measure performance, is still argued about by serious researchers. I'm not going to tell
you it's settled. It isn't.

Which is itself a useful lesson for this course: a lot of what you'll read stated
confidently online is, in the actual literature, contested.
""")

content_slide(
    prs, "2022 — It Reaches Everyone",
    [
        "The technology had existed for years. What changed was access.",
        (1, "A conversational interface, free to use, requiring no technical knowledge at all", None),
        (1, "Adoption was extraordinarily fast — faster than almost any consumer technology before it", None),
        "",
        ("The important consequence for this course:", None, "bold"),
        (1, "Hundreds of millions of people began relying on a system nobody had taught them to evaluate", None),
        (1, "The capability arrived everywhere at once. The judgment did not.", None),
        (1, "Closing that gap, for you, is what the remaining twelve weeks are for.", None),
    ],
    notes="""
2022. And here's the thing to understand: the technology was not new in 2022. The
architecture was five years old. Large models had existed for years and researchers had
been using them.

What changed was access. A conversational interface, free, requiring no technical
knowledge — you type, it answers. Adoption was extraordinarily fast, faster than almost
any consumer technology before it.

Now the consequence, and this is why the whole history lesson has been pointing here.

Hundreds of millions of people began relying, daily, on a system that nobody had taught
them how to evaluate. There was no course. There was no professional training. The
capability arrived everywhere, at once, and the judgment required to use it well did not
arrive with it.

That gap is the reason this course exists. And closing it, for the thirty or so of you in
this room, is what the remaining twelve weeks are for.

That's the history. Let's do something with it.
""")

# ══════════════════════════════════════════════════════════════ part 5 — activity
section_slide(
    prs, 5, "Activity: Date the Technology",
    notes="""
Part five. This activity needs no devices at all — just your judgment. If you'd rather sit
and think quietly, that works too; I'll give the answers either way.
""")

activity_slide(
    prs, "Date the Technology",
    [
        ("I'll read four descriptions. For each one, write down the year you think it happened.", None, "bold"),
        "",
        ("A.", None, "bold"),
        (1, "A conversational program that people confide personal problems to — and who refuse to believe it doesn't understand them.", None),
        ("B.", None, "bold"),
        (1, "A senior researcher predicts machines will do any work a human can do, within twenty years.", None),
        ("C.", None, "bold"),
        (1, "A machine defeats the reigning world champion at chess.", None),
        ("D.", None, "bold"),
        (1, "Software identifies objects in ordinary photographs far more accurately than anything before it.", None),
    ],
    minutes=10,
    notes="""
Ten minutes, no devices needed. I'll read four descriptions. For each one, write down the
year you think it happened. Just a number. Don't discuss yet.

A. A conversational program that people confide personal problems to, and who refuse to
believe it doesn't really understand them.

B. A senior researcher predicts that machines will be capable of doing any work a human
can do, within twenty years.

C. A machine defeats the reigning world champion at chess.

D. Software identifies objects in ordinary photographs far more accurately than anything
before it.

Write four years. Take two minutes.

[Then, if the room is willing, take a show of hands for each: "who said after 2015 for A?"
The hands are the lesson. If nobody engages, just move to the answers — they work fine
read aloud.]
""")

timeline_slide(
    prs, "The Answers",
    [
        ("1966", "A — ELIZA",        "People confided in a few hundred lines of pattern matching"),
        ("1965", "B — Simon",        "\"...within twenty years, of doing any work a man can do\""),
        ("1997", "C — Deep Blue",    "Beat Kasparov by searching millions of positions, not by learning"),
        ("2012", "D — Image recognition", "The result that convinced the field neural networks had arrived"),
    ],
    notes="""
Here are the answers, and I'd guess most of you were late on at least two.

A — 1966. ELIZA. Sixty years ago.

B — 1965. Herbert Simon. Which means the twenty-year deadline expired in 1985.

C — 1997. Deep Blue and Kasparov. And here's the detail that matters: Deep Blue won by
searching enormous numbers of positions very fast. It did not learn chess the way modern
systems learn. It's a triumph of engineering and search, not of learning — and at the
time, a great many people said it proved machines could think. It proved nothing of the
kind. It proved that chess is more amenable to search than we assumed.

D — 2012. The image recognition result that convinced the research community neural
networks had genuinely arrived. Note that this is ten years before ChatGPT — the
revolution was well underway before any of us noticed it.

Now the point of the exercise. Most people place these far too recently, because our sense
of this field's history is compressed into the last three years. If you thought ELIZA was
from the 2010s, you're in very good company, and you've just learned something about how
badly your intuition tracks this field.
""")

boxes_slide(
    prs, "Three Patterns That Keep Repeating",
    [
        ("Right idea, wrong decade",
         "The direction of predictions has often been reasonable. The timing has been wrong "
         "almost every time, usually by decades and usually too optimistic. Treat any specific "
         "date with suspicion — including today's."),
        ("Fluency reads as understanding",
         "From ELIZA to now, humans reliably attribute comprehension to systems that produce "
         "plausible language. The systems changed enormously. This response did not change at "
         "all."),
        ("The winner is whatever hand-writes less",
         "Rules lost to statistics; hand-picked features lost to learned ones. Every major shift "
         "moved work from human specification to learning from data."),
    ],
    notes="""
Three patterns. If you leave today with only one slide, make it this one.

Right idea, wrong decade. The direction of predictions in this field has often been
reasonable. The timing has been wrong nearly every time, usually by decades, and usually
in the optimistic direction. So when you read that something will happen by 2028, the
useful response is not "that's wrong" — it's "that's the kind of claim that has been
wrong before, so what would I need to see to believe it?" And note that this applies to
today's predictions too. Including mine.

Fluency reads as understanding. From 1966 to right now, humans reliably attribute
comprehension to systems producing plausible language. The systems changed beyond
recognition. Our response to them did not change at all. That's why last week's
overconfidence failure works on smart people — it isn't a knowledge problem, it's a
perceptual one.

And the winner is whatever hand-writes less. Rules lost to statistics. Hand-designed
features lost to learned ones. Every major shift in seventy years moved work away from
human specification and towards learning from data. That's the most reliable trend line in
the whole story, and it's a decent guide to which claims about the future are plausible.
""")

content_slide(
    prs, "What This History Gives You",
    [
        "A base rate — you now know how often confident predictions in this field have been wrong",
        "A name for the central risk — the ELIZA effect, described sixty years ago and still operating",
        "An explanation for why these systems predict likelihood rather than truth",
        (1, "That was a deliberate design decision in the 1990s, because it worked better. It is not a recent flaw.", None),
        "",
        ("Next week we go inside the model itself:", None, "bold"),
        (1, "tokens, context windows, and precisely why hallucination happens", None),
    ],
    notes="""
So what has today actually given you? Four things.

A base rate. You now know how often confident predictions in this field have been wrong,
and by how much. That is genuinely useful, and most people commenting publicly on AI do
not have it.

A name for the central risk. The ELIZA effect. Described in 1966, still operating on
every one of us, every day.

And an explanation for something we asserted last week without justifying. These systems
predict what is likely rather than what is true. Now you know why: it was a deliberate
design decision, taken in the 1990s, because it produced better results than the
alternative. It is not a recent flaw that somebody will patch. It is the foundation.

Next week we go inside the model. Tokens, context windows, and precisely why hallucination
happens — which, after today, should feel less like a mystery and more like an obvious
consequence of the design.
""")

content_slide(
    prs, "Wrap-Up",
    [
        "Seventy years, not three — and two collapses along the way",
        "ELIZA, 1966: fluency alone was enough to convince people. It still is.",
        "The constant direction: from hand-written rules towards learning from data",
        "Right idea, wrong decade — the base rate for confident predictions in this field",
        "",
        ("Next week:", None, "bold"),
        (1, "How LLMs Work — tokens, context windows, and why hallucination happens", None),
    ],
    notes="""
To close. Four things.

Seventy years, not three. And two collapses along the way, both caused by the gap between
promise and delivery rather than by technical failure.

ELIZA, 1966. Fluency alone was enough to convince people that something understood them.
It still is. That's the thread running from the oldest thing we discussed today straight
into your professional life.

The constant direction: away from hand-written rules, towards learning from data. Every
shift, for seventy years, the same way.

And right idea, wrong decade — the base rate you should apply to any confident prediction,
including the ones you'll read this week.

Next week, inside the model. Tokens, context windows, why hallucination happens.

Nothing to prepare. Questions?
""")

closing_slide(
    prs,
    notes="""
Take questions here.

Common ones for this week:

"Are we in another AI winter / will there be one?" — Honest answer: nobody knows, and the
people who say they know have been wrong before. What I'd point at is the pattern: winters
followed gaps between promise and delivery, not technical failure. So the thing to watch
is the size of that gap.

"Did Deep Blue really not learn?" — Correct, not in the modern sense. It searched enormous
numbers of positions using hand-crafted evaluation. Systems that learn chess by playing
came much later, and they're a different achievement.

"If it's all just statistics, how can it write code?" — Fair question, and week three is
partly an answer. Short version: at sufficient scale, predicting the next piece of text
well requires internal structure that behaves a lot like knowing things. Whether that
counts as understanding is a genuinely open argument.

"Is the ELIZA effect avoidable?" — Not really, not by willpower. That's why this course
teaches procedures for checking rather than telling you to be sceptical. Procedures work
when intuition doesn't.
""")

save(prs, str(pathlib.Path(__file__).parent / "week02.pptx"))
