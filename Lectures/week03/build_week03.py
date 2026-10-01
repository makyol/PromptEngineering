#!/usr/bin/env python3
"""Week 3 — How Large Language Models Work.

Build:  python3 build_week03.py
Output: week03.pptx
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "Theme"))
from theme import *  # noqa

prs = new_deck()

title_slide(
    prs, 3,
    "How Large Language Models Work",
    "Tokens, context windows, and why hallucination happens",
    notes="""
Welcome back.

Last week we did seventy years of history, and we ended on a specific claim: these systems
predict what is likely rather than what is true, and that was a deliberate design decision
taken in the 1990s because it worked better than the alternative.

Today I make good on that. We're going inside the model.

By the end of this hour you should be able to explain, to a colleague who knows nothing
about this, why these systems hallucinate. Not "because they're not perfect yet" — the
actual mechanism. And you should be able to explain why it is not a bug that somebody is
going to fix next year.

I want to set expectations. There is no mathematics in this session. There's no code. What
there is, is a set of ideas that are genuinely simple once you see them, and that most
people using these tools every day have never been told.

If you understand today properly, weeks seven and eight get much easier, because you'll
know why grounding and verification are necessary rather than just being told to do them.
""")

content_slide(
    prs, "Today: What We'll Explore",
    [
        "Tokens — how text becomes something a machine can work with",
        "Why Turkish costs more than English, and what that means for you",
        "Prediction — the single operation underneath everything",
        "The context window — what the model can see, and what happens when it fills",
        ("Why hallucination happens — the actual mechanism", None, "bold"),
        "Activity: Break the Tokenizer",
        "What differs between model families",
    ],
    notes="""
Where we're going.

Tokens first — how text becomes something a machine can operate on. This sounds like
plumbing and it explains a surprising number of things you've probably noticed.

Then a point that matters specifically in this room: Turkish costs more than English when
you use these systems. More tokens, more money, and often worse results. I'll show you
why.

Then prediction — the single operation that everything else sits on top of.

Then the context window: what the model can actually see, and what happens when you give
it more than fits. That's a quiet failure and it will bite you in week seven.

Then the centrepiece — why hallucination happens. Not a hand-wave. The mechanism.

Then an activity, and finally what actually differs between model families, so you can
make sensible choices without needing to follow every release.
""")

# ═════════════════════════════════════════════════════════ part 1 — tokens
section_slide(
    prs, 1, "From Text to Tokens",
    notes="""
Part one. How text becomes something a machine can work with.
""")

flow_slide(
    prs, "What Actually Happens When You Press Enter",
    [
        ("Your text", "\"Explain photosynthesis simply.\""),
        ("Tokens", "Split into pieces: [Explain][ photo][synthesis][ simply][.]"),
        ("Numbers", "Each piece becomes a number, then a long list of numbers"),
        ("Prediction", "The model produces a probability for every possible next piece"),
        ("Text back", "One piece is chosen, appended, and the whole thing repeats"),
    ],
    caption="Every response you have ever received was built one piece at a time, by repeating the last two steps.",
    notes="""
Here's the whole pipeline. Five steps, and I want you to be able to redraw this.

You type something. "Explain photosynthesis simply."

Step two: it's split into pieces called tokens. Notice in the example that "photosynthesis"
becomes two pieces — "photo" and "synthesis" — and that the spaces are attached to the
front of words. That's typical.

Step three: each piece becomes a number, and then each number becomes a long list of
numbers representing its position in that meaning-space we discussed last week.

Step four: the model produces a probability for every possible next piece. Not one answer
— a probability distribution across its entire vocabulary, which might be a hundred
thousand possibilities.

Step five: one piece gets chosen, added to the end, and then the whole thing runs again
with the new, slightly longer text.

Read the caption, because this is the sentence that reframes everything. Every response
you have ever received from one of these systems was built one piece at a time, by
repeating those last two steps, hundreds of times.

It never planned the paragraph. It never knew how the sentence would end when it started
writing it.
""")

content_slide(
    prs, "Tokens Are Not Words",
    [
        "A token might be a whole word, part of a word, a single character, or punctuation",
        (1, "Common words are usually one token: \"the\", \"hospital\", \"patient\"", None),
        (1, "Rarer words get broken up: \"tokenization\" might become \"token\" + \"ization\"", None),
        (1, "A space is usually attached to the word that follows it", None),
        "",
        ("Why break words at all? So the system is never stuck.", None, "bold"),
        (1, "A fixed list of whole words fails the moment it meets a word it has never seen", None),
        (1, "With pieces, any word can be assembled — like building from a limited set of bricks", None),
    ],
    notes="""
The first thing to unlearn: tokens are not words.

A token might be a whole word, part of a word, a single character, or a piece of
punctuation. Common words are usually a single token — "the", "hospital", "patient". Rarer
words get broken into pieces: "tokenization" might become "token" plus "ization". And a
space is usually attached to the front of the word that follows it, which is why the
token is " hospital" with a space rather than "hospital".

Now, why break words at all? Why not just have a list of words?

Because a fixed list of whole words fails the instant it meets a word that isn't on the
list. A new drug name. A surname. A technical term. A typo. Any of those would simply be
unrepresentable.

With pieces, anything can be assembled. It's like building with a limited set of bricks —
you can't have a brick for every possible object, but with enough small bricks you can
build anything. The system is never stuck, and that robustness is worth the cost of words
being fragmented.

And that fragmentation has consequences, which is the next slide.
""")

content_slide(
    prs, "Turkish Costs More Than English",
    [
        "Tokenizers are trained mostly on English text, so English words tend to be single tokens",
        (1, "Agglutinative languages build long words from many suffixes — exactly what gets fragmented", None),
        (1, "A Turkish word can become four, five, six tokens where the English equivalent is one", None),
        "",
        ("Three practical consequences, and they are not small:", None, "bold"),
        (1, "The same document in Turkish fills the context window faster than in English", None),
        (1, "Where usage is metered or limited, Turkish costs more for the same content", None),
        (1, "Performance is often measurably weaker, because there is far less Turkish training text", None),
        "",
        (1, "Verify this yourself with any online tokenizer — paste the same sentence in both languages.", None),
    ],
    notes="""
This slide matters more in this room than it would in most.

Tokenizers are trained mostly on English text. So English words tend to come out as single
tokens, because they appeared often enough during training to earn their own entry.

Turkish is agglutinative — you build long words by stacking suffixes. And stacked suffixes
are exactly the kind of thing that gets fragmented, because the whole assembled word
appeared rarely, even if every piece of it is common.

So a Turkish word that an English speaker would express in one word can become four, five,
six tokens.

Three consequences, and none of them are small.

One: the same document in Turkish fills the context window faster than the English
version. You will hit limits sooner.

Two: wherever usage is metered — paid plans, free-tier caps, message limits — Turkish
costs more to process the same content. You are, in a small and quiet way, paying a tax
for the language you speak.

Three, and this is the significant one: performance is often measurably weaker in Turkish,
because there is far less Turkish text in training data than English. This is exactly the
displacement failure from week one, seen from the inside. Now you know why it happens.

Don't take my word for any of this — paste the same sentence in both languages into any
online tokenizer and count. That's the activity later.
""")

boxes_slide(
    prs, "Things Tokens Explain",
    [
        ("Bad at counting letters",
         "Ask how many times a letter appears in a word and it may get it wrong. It never saw "
         "letters — it saw chunks. You are asking about something it cannot directly perceive."),
        ("Odd with spelling and rhyme",
         "Reversing a word, spelling it out, or finding rhymes are all letter-level tasks "
         "performed by a system that operates on pieces, not characters."),
        ("Length limits feel arbitrary",
         "Limits are counted in tokens, not words or characters. That is why \"about 500 words\" "
         "behaves inconsistently, and why the limit differs by language."),
    ],
    notes="""
Three things you may have noticed, all explained by tokens.

First: these systems can be strangely bad at counting letters. Ask how many times a
particular letter appears in a word and you may get a confident wrong answer. Why? It never
saw letters. It saw chunks. You are asking it about something it cannot directly perceive —
like asking someone to count the bricks in a wall they only ever saw as complete panels.

Second, and for the same reason: reversing a word, spelling something out, finding rhymes.
All letter-level tasks, performed by a system that works on pieces.

Third: length limits feel arbitrary because they're counted in tokens, not words or
characters. That's why asking for "about 500 words" behaves inconsistently, and why the
same limit gets you noticeably less content in Turkish than in English.

I want to point at something about all three of these. None of them are the system being
stupid. Each is a perfectly predictable consequence of how text gets represented. Once you
know the mechanism, the behaviour stops being mysterious and becomes something you can
anticipate — which is the difference between being surprised by a tool and being able to
use it well.
""")

# ═════════════════════════════════════════════════════════ part 2 — prediction
section_slide(
    prs, 2, "Prediction",
    notes="""
Part two. The single operation underneath everything.
""")

content_slide(
    prs, "One Operation, Repeated",
    [
        "Given everything so far, produce a probability for every possible next token",
        (1, "\"The capital of France is ___\"  →  \"Paris\" gets a very high probability", None),
        (1, "\"My favourite colour is ___\"  →  probability spread across many plausible options", None),
        "",
        ("The model does not know which of those two situations it is in.", None, "bold"),
        (1, "It performs the same operation either way, with the same apparent confidence", None),
        (1, "A near-certain answer and a wild guess come out looking identical to you", None),
    ],
    notes="""
Here is the whole thing. Given everything so far, produce a probability for every possible
next token. That is the operation. There isn't a second one.

Two examples. "The capital of France is —" and "Paris" gets an overwhelming probability,
because in essentially every text where that phrase appeared, Paris followed.

"My favourite colour is —" and the probability is spread thinly across many options, none
of them clearly right, because there's no fact to recover.

Now the bold line, and this is the most important sentence in today's session.

The model does not know which of those two situations it is in.

It performs the same operation either way. It doesn't have a separate mode for "I know
this" and "I'm guessing." And critically, nothing in the output tells you which one
happened. A near-certain answer and a wild guess come out looking identical — same fluent
prose, same confident tone, same structure.

That's overconfidence from week one, and now you can see its source. It isn't a
personality flaw in the system. There is simply no mechanism by which uncertainty could
reach you, because uncertainty isn't part of what gets produced.
""")

content_slide(
    prs, "Why Prediction Looks Like Knowledge",
    [
        "To predict text well across an enormous range of material, you need internal structure",
        (1, "Predicting the next word in a medical case note requires something functioning like medical knowledge", None),
        (1, "Predicting the end of a logical argument requires something functioning like reasoning", None),
        "",
        ("So the capability is real, even though the mechanism is prediction.", None, "bold"),
        (1, "Do not conclude \"it's just autocomplete, so it's useless\" — that is as wrong as over-trusting it", None),
        "",
        (1, "Whether this constitutes understanding is genuinely disputed. You do not need to settle it to use these tools well.", None),
    ],
    notes="""
Now I need to correct something, because students often over-learn the previous slide.

People hear "it just predicts the next word" and conclude the whole thing is a parlour
trick. That conclusion is wrong, and it's wrong in a way that will make you worse at using
these tools, not better.

Here's why. To predict text well — across medicine, law, code, poetry, six languages — you
need internal structure. Predicting the next word in a medical case note accurately
requires something that functions like medical knowledge. Predicting how a logical argument
concludes requires something that functions like reasoning. You cannot get good at the
prediction task without developing those structures, because the prediction task is hard.

So the capability is real. Genuinely real. The bold line matters: do not conclude "it's
just autocomplete, so it's useless." That error is as damaging as over-trusting it, and
it's the error educated sceptics tend to make.

And the last line, which I'll say plainly: whether any of this constitutes understanding is
genuinely disputed among serious people, and I'm not going to pretend to settle it in a
Tuesday afternoon lecture.

The good news is you don't need to settle it. You need to know what the system does
reliably and where it fails. That's an engineering question, not a philosophical one.
""")

content_slide(
    prs, "Why the Same Question Gives Different Answers",
    [
        "Having produced probabilities, the system must choose one token — and it usually does not simply take the highest",
        (1, "Always choosing the most likely token produces repetitive, flat, oddly lifeless text", None),
        (1, "So there is deliberate randomness in the selection", None),
        "",
        ("Often exposed as a setting called \"temperature\":", None, "bold"),
        (1, "Lower — more predictable, more repetitive. Better for extraction and structured output.", None),
        (1, "Higher — more varied, more surprising. Better for brainstorming and drafting.", None),
        "",
        ("Consequence: asking twice and getting the same answer is not confirmation.", None, "bold"),
    ],
    notes="""
Last week somebody may have wondered why the same question gives different answers. Here's
why.

Having produced probabilities across the vocabulary, the system has to pick one. And it
usually does not simply take the highest.

Why not? Because always taking the most likely token produces text that is repetitive,
flat, and strangely lifeless. It gets stuck in loops. So there is deliberate randomness
introduced into the selection.

That's often exposed to you as a setting called temperature. Lower temperature means more
predictable and more repetitive — better when you're extracting data or need consistent
structure. Higher means more varied and more surprising — better for brainstorming and
first drafts.

Now the consequence, and it's a trap I want you to avoid.

Asking the same question twice and getting the same answer is not confirmation. People do
this constantly — they get an answer, they feel unsure, they ask again, they get something
similar, and they feel reassured.

But a consistent answer means the pattern is strong in the training data. It does not mean
the answer is correct. A widely repeated error will be reproduced very consistently
indeed. Consistency measures how common something is, not whether it's true.

We'll build the actual check in week eight.
""")

# ═════════════════════════════════════════════════════ part 3 — context window
section_slide(
    prs, 3, "The Context Window",
    notes="""
Part three. What the model can see — and what happens when you exceed it.
""")

content_slide(
    prs, "What Is in the Window",
    [
        "The context window is the total amount of text the model can consider at once — measured in tokens",
        "",
        ("It holds more than you think:", None, "bold"),
        (1, "Hidden instructions the product adds before your message ever arrives", None),
        (1, "Everything either of you has said so far in this conversation", None),
        (1, "Any documents or images you attached", None),
        (1, "The response currently being generated", None),
        "",
        (1, "All of it competes for the same finite space.", None),
    ],
    notes="""
The context window is the total amount of text the model can consider at once, measured in
tokens.

And it holds more than people realise. Four things.

Hidden instructions that the product adds before your message ever arrives — every
commercial tool does this. Text you never see, telling the model how to behave.

Everything either of you has said so far in this conversation. All of it, re-sent every
single time. This is worth pausing on: the model isn't remembering your conversation. The
entire conversation is being handed to it afresh with every message. That's what memory
means here.

Any documents or images you attached.

And the response currently being generated, which also occupies space as it grows.

All four compete for the same finite budget. And this is why, in a long conversation,
things start to drift — earlier material is being squeezed by everything that came after
it.
""")

content_slide(
    prs, "What Happens When It Fills Up",
    [
        "Windows are large now, but they are not infinite — and behaviour at the edge is what matters",
        "",
        (1, "Some tools refuse the input outright. That is the good case: you know something went wrong.", None),
        (1, "Others silently drop or summarise the earlier part of the conversation", None),
        (1, "Others accept a long document but attend to it unevenly, favouring the beginning and end", None),
        "",
        ("The failure is quiet. You get a confident answer based on part of your document, and no warning.", None, "bold"),
        (1, "This is the single most common reason \"I gave it the whole report and it missed something obvious.\"", None),
    ],
    notes="""
Windows are large now — much larger than a few years ago — and it is tempting to conclude
the problem is solved. It isn't, and the reason is what happens at the edge.

Three behaviours. Some tools refuse the input outright: too long, won't process. That is
the good case, and I want you to notice that it's good. An error message is a gift. You
know something went wrong.

Others silently drop or compress the earlier part of the conversation to make room.

And others accept your long document but attend to it unevenly, doing better on material
at the beginning and the end than in the middle.

Now the bold line. The failure is quiet. You get a fluent, confident answer that was based
on part of your document, and there is no warning anywhere that this happened.

This is the single most common explanation for a complaint I hear every year: "I gave it
the whole report and it missed something obvious." It didn't miss it. It very likely never
saw it.

Remember this in week seven. When we ground a system in your documents, "did it actually
read all of this?" is a question you must ask deliberately, because the system will never
volunteer the answer.
""")

# ═══════════════════════════════════════════════════ part 4 — hallucination
section_slide(
    prs, 4, "Why Hallucination Happens",
    notes="""
Part four. The centrepiece. If you take one thing from week three, take this.
""")

callout_slide(
    prs,
    "There is no step at which the system checks whether what it is saying is true.",
    "Not a weak check. No check. Truth is not part of the operation.",
    notes="""
Here it is.

There is no step at which the system checks whether what it is saying is true.

I want to be precise, because students soften this. It isn't that the check is weak, or
unreliable, or sometimes skipped. There is no check. Truth is not part of the operation
being performed.

Go back to the pipeline from earlier. Text in, tokens, numbers, probabilities, choose,
repeat. Point at the step where truth enters. It isn't there. There's nowhere for it to
be.

What the system optimises is plausibility — what would likely come next, given everything
so far. And most of the time, in most domains, the plausible continuation is also the true
one, because the text it learned from was mostly written by people trying to be accurate.
That correlation is why these tools work at all.

But it is a correlation. Not a guarantee. And when it breaks — when the plausible
continuation and the true one come apart — the system has no way to notice, because it was
never tracking the difference.

That is hallucination. Not a malfunction. The system working exactly as designed, in a
region where plausible and true diverge.
""")

boxes_slide(
    prs, "Three Situations Where It Reliably Breaks",
    [
        ("Thin coverage",
         "Topics with little training text: local law, minority languages, niche procedures, "
         "recent events. The pattern is weak, so plausible-sounding filler wins. This is why "
         "Turkish-specific questions are higher risk than English ones."),
        ("Specific details",
         "Citations, numbers, dates, names, references. These are exactly the things that "
         "cannot be inferred from surrounding text — they must be recalled. The format is easy "
         "to imitate; the content is not."),
        ("Confident framing",
         "If you ask a question that presupposes something false, the likely continuation "
         "accepts the premise. \"Explain why X causes Y\" produces an explanation whether or not "
         "X causes Y."),
    ],
    notes="""
Three situations where the correlation between plausible and true predictably breaks.

Thin coverage. Topics with little training text — local law, minority languages, niche
procedures, recent events. The pattern is weak, so plausible-sounding filler wins by
default. Note this is the mechanism behind week one's displacement failure, and note again
that it means Turkish-specific questions carry more risk than English ones. Not because the
model is biased against Turkish, but because there's less of it to learn from.

Specific details. Citations, numbers, dates, names, references. These are precisely the
things that cannot be inferred from the surrounding text — they have to be recalled. And
here's the cruel part: the *format* of a citation is extremely easy to imitate, because
citations are highly patterned. The content is not. So you get a perfectly formatted
citation to a paper that doesn't exist. That's our week one worked example, explained.

Confident framing. If you ask a question that presupposes something false, the likely
continuation accepts the premise. Ask "explain why X causes Y" and you will get an
explanation, regardless of whether X causes Y. The system is completing your framing, not
auditing it.

That last one is a genuinely useful defensive habit: watch what your own question assumes.
""")

content_slide(
    prs, "Why It Doesn't Just Say \"I Don't Know\"",
    [
        "\"I don't know\" is itself just a sequence of tokens — it competes with every other continuation",
        (1, "In most training text, a question is followed by an answer, not by an admission of ignorance", None),
        (1, "So \"I don't know\" is usually a low-probability continuation, even when it is the correct one", None),
        "",
        ("Fine-tuning pushes models to hedge more, and it genuinely helps — but it is a tendency, not a guarantee.", None, "bold"),
        "",
        (1, "You can raise the odds: \"If the answer is not in the sources provided, say so and stop.\"", None),
        (1, "This works better when there are actual sources to check against — which is Week 7.", None),
    ],
    notes="""
The obvious question: why doesn't it just say it doesn't know?

Because "I don't know" is itself just a sequence of tokens, competing with every other
possible continuation. It isn't a special escape hatch. It's a phrase.

And think about the text these systems learned from. When a question appears, what usually
follows? An answer. Textbooks answer questions. Forums answer questions. Documentation
answers questions. Very little written text consists of somebody asking something and
somebody else saying "no idea." So "I don't know" is a low-probability continuation — even
in exactly the situations where it's the correct one.

Now, fine-tuning does push models to hedge and refuse more than raw prediction would. That
is real and it genuinely helps. But read the bold line: it's a tendency, not a guarantee.
It shifts probabilities. It doesn't install a mechanism.

You can improve your odds with instructions like "if the answer is not in the sources
provided, say so and stop." That helps.

But notice the condition hiding in that sentence — "in the sources provided." It works much
better when there *are* sources to check against, because then there's something concrete
to fail against rather than an abstract judgment about its own knowledge.

Which is week seven, and now you know why week seven exists.
""")

# ═══════════════════════════════════════════════════════════════ activity
section_slide(
    prs, 5, "Activity: Break the Tokenizer",
    notes="""
Part five. Ten minutes. If you have a device, run it. If not, the results are on the
following slides and we'll walk them together.
""")

activity_slide(
    prs, "Break the Tokenizer",
    [
        ("1.  Open any online tokenizer.", None, "bold"),
        (1, "Search \"tokenizer\" — several are free, browser-based, no account required.", None),
        ("2.  Paste the same sentence in English and in Turkish. Compare the token counts.", None, "bold"),
        (1, "Try a long agglutinated Turkish word on its own and watch it shatter.", None),
        ("3.  Try your own name, a place name, and a technical term from your field.", None, "bold"),
        (1, "Which stay whole? Which break apart? Why might that be?", None),
        ("4.  Then ask an assistant to count the letters in a long word.", None, "bold"),
        (1, "Check its answer by hand.", None),
    ],
    minutes=10,
    notes="""
Ten minutes. Four steps.

One. Open any online tokenizer. Search for "tokenizer" — several are free, run in the
browser, need no account. Any of them will do; we're looking at a general property, not a
specific product.

Two. Paste the same sentence in English and in Turkish and compare the counts. Then try a
long agglutinated Turkish word on its own — one of the ones that makes foreigners laugh —
and watch it shatter into pieces.

Three. Try your own name. A place name. A technical term from your own field. Which stay
whole? Which break apart? And think about why — what does staying whole tell you about how
often that string appeared in training text?

Four. Then go to an assistant and ask it to count how many times a particular letter
appears in a long word. Check it by hand.

[If nobody has a device, skip straight to the next slide — the comparison is on it.]
""")

boxes_slide(
    prs, "What You Should Have Found",
    [
        ("Turkish takes more tokens",
         "The same meaning, expressed in Turkish, typically costs noticeably more tokens than in "
         "English. Long agglutinated words fragment heavily — each suffix tends to become its "
         "own piece."),
        ("Familiarity predicts wholeness",
         "Common names and common terms survive as single tokens. Rare names, local place names "
         "and specialist vocabulary fragment. Whether a string stayed whole tells you how often "
         "it appeared in training text."),
        ("Letter counting is unreliable",
         "Because the system never saw letters. If it got it right, it likely reasoned about it "
         "explicitly rather than perceiving it — try a longer or more unusual word and it "
         "becomes fragile again."),
    ],
    notes="""
Whether or not you ran it, here's what the exercise shows.

Turkish takes more tokens. The same meaning, in Turkish, costs noticeably more than in
English, and long agglutinated words fragment heavily — each suffix tends to become its own
piece. That's the tax we discussed, and now you've seen it measured rather than asserted.

Familiarity predicts wholeness. Common names and terms survive as single tokens. Rare
names, local place names, specialist vocabulary — these fragment. And there's a genuinely
useful inference available here: whether a string stayed whole tells you something about
how often it appeared in the training text. Which tells you something about how reliable
the system is likely to be on that topic. That's a rough signal, but it's a real one.

And letter counting is unreliable, because the system never saw letters. If yours got it
right, it probably reasoned about it explicitly rather than perceiving it directly — try a
longer or stranger word and watch it become fragile again.

None of this is the system being defective. All of it is a direct consequence of the
pipeline we drew at the start of the hour.
""")

# ═══════════════════════════════════════════════════════ part 6 — model families
section_slide(
    prs, 6, "What Differs Between Models",
    notes="""
Part six, and briefly. Enough to make sensible choices without following every release.
""")

content_slide(
    prs, "Choosing Without Chasing",
    [
        "New models are released constantly. The useful move is to know which axes matter, not which name is current.",
        "",
        ("The axes worth checking:", None, "bold"),
        (1, "Context window — how much can it hold at once?", None),
        (1, "Knowledge cut-off — how recent is what it knows?", None),
        (1, "Whether it can search or read documents you give it, rather than working from memory alone", None),
        (1, "Whether it has an explicit reasoning mode for harder problems", None),
        (1, "Cost, rate limits, and what the free tier actually allows", None),
        "",
        ("For this course, any current free assistant is sufficient. Do not pay for anything.", None, "bold"),
    ],
    notes="""
Models are released constantly, and any specific list I gave you today would be out of date
before your exam. So I'm not going to give you one. What's durable is knowing which axes
matter.

Five of them.

Context window — how much can it hold at once. Now you know exactly what that means and
why it matters.

Knowledge cut-off — how recent is what it knows. Anything after that date is unknown to it,
and it will not necessarily tell you.

Whether it can search or read documents you provide, rather than working purely from
memory. This is the biggest practical difference between tools, and it's what makes week
seven possible.

Whether it has an explicit reasoning mode — a setting that makes it work through harder
problems more slowly and more carefully.

And cost, rate limits, and what the free tier actually allows.

For this course, read the bold line: any current free assistant is sufficient. Do not pay
for anything. If a week's activity seems to need a paid feature, I've made a mistake and I
want to hear about it.
""")

content_slide(
    prs, "Wrap-Up",
    [
        "Text becomes tokens; tokens become numbers; the model predicts one piece at a time",
        "Turkish fragments more than English — more tokens, more cost, thinner coverage",
        ("There is no step where the system checks whether what it says is true", None, "bold"),
        "Hallucination is that design working normally where plausible and true come apart",
        "Context is finite, and overflowing it fails quietly",
        "",
        ("Next week:", None, "bold"),
        (1, "Principles of Effective Prompting — what actually improves results, and what only appears to", None),
    ],
    notes="""
Five things to leave with.

Text becomes tokens, tokens become numbers, and the model predicts one piece at a time,
repeatedly, without ever planning ahead.

Turkish fragments more than English. More tokens, more cost, thinner coverage. That affects
you specifically, and it's a reason to be more careful with Turkish-language questions, not
less.

There is no step where the system checks whether what it says is true. If you remember one
sentence from today, that's it.

Hallucination is therefore not a malfunction. It's the design working normally, in a region
where plausible and true have come apart. Which is why it can't simply be patched out, and
why the response has to be procedural — check things — rather than hopeful.

And context is finite, and overflowing it fails quietly.

Next week, principles of effective prompting. What actually improves results, and what only
appears to — because there's a good deal of folklore in circulation, and you now know
enough mechanism to tell the difference.

Questions?
""")

closing_slide(
    prs,
    notes="""
Take questions here.

Common ones for this week:

"If it doesn't check truth, how is it right so often?" — Because the text it learned from
was mostly written by people trying to be accurate. Plausible and true correlate strongly.
The course is about the cases where they don't.

"Will hallucination be fixed?" — Reduced, yes, and it has been. Eliminated by better
prediction alone, no — there's no truth signal in the objective. The practical fixes are
external: give it sources, check the output. Weeks seven and eight.

"Should I write prompts in English instead of Turkish?" — Often it does perform better, for
the reasons we covered. But if the subject is Turkish law or Turkish practice, the language
isn't the real problem — coverage is. Switching to English won't give it Turkish knowledge
it never had.

"Is temperature something I can control?" — In the consumer chat tools, usually not
directly. It matters more when using these through an interface that exposes settings. Know
the concept; don't worry about the dial.
""")

save(prs, str(pathlib.Path(__file__).parent / "week03.pptx"))
