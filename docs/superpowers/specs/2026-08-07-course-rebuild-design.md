# Course Rebuild Design — Prompt Engineering and Large Language Models

**Date:** 2026-08-07
**Owner:** Mehmet Ali Akyol, PhD — Ankara Medipol University
**Term:** Fall 2026–2027 (September – January 2027)

## 1. What this is

Rebuild of the 14-week undergraduate elective previously delivered as *Prompt Engineering*
(İstem Mühendisliği), retitled **Prompt Engineering and Large Language Models**
(İstem Mühendisliği ve Büyük Dil Modelleri).

This is not a migration. The course is being re-centred: from teaching prompt *technique*
to teaching *judgment and building*, for reasons set out in §3.

## 2. Fixed constraints

From the approved course proposal; not negotiable.

- **Program dışı seçmeli ders** — university-wide elective, all disciplines.
- **No prerequisite, no programming requirement.** Assume no Python, no command line,
  no API keys. Students come from healthcare, law, education, business, engineering.
- **2 hours theoretical, 0 practical, 2 credits, 2 AKTS.** No AKTS increase is sought.
  The existing form's "Öğretme Şekli" already describes theoretical sessions with live
  application examples and interactive exercises, which accommodates the demo-and-build
  format without a structural change.
- **Language of instruction:** English.
- **Browser-based tools, no installation, free tier only.**
- **14 weeks**, one session per week.
- **Lectures run 60–90 minutes**, not the full 2 hours.

## 3. Why the course is being re-centred

The prompt-technique core has depreciated faster than the rest of the curriculum:

- Chain-of-thought is now internal to reasoning models; the canonical "think step by step"
  is no longer the lever, and scripting reasoning explicitly can create redundancy or
  contradiction with the model's native process.
- "Prompt engineer" job postings fell ~40% between 2024 and 2025, while roles requiring
  workflow design and AI systems thinking grew.
- What employers now ask for is the ability to understand how outputs are generated,
  **recognise when they are wrong, spot hallucinations, and know when human judgment is
  required.** Prompting itself is foundational literacy, not specialised expertise.

This maps onto the material being *added* (grounding, verification, agents, security,
ethics) and away from the material that previously consumed five weeks and generated most
of the repetition. Technique therefore compresses from five weeks to four, and the back
half of the course becomes hands-on building.

**Sources to cite in Week 1 and in the forms:** see `docs/superpowers/specs/sources.md`
(to be created during step 3); claims above are drawn from 2026 industry and practitioner
reporting and must be re-verified before delivery.

## 4. Deliverable formats

| Artifact | Format |
|---|---|
| Lecture decks | **`.pptx`**, 16:9, custom clean theme. Beamer/pdfLaTeX retired. |
| Speaker notes | **Full verbatim script on every slide** — delivery text, not reminders. |
| Quizzes and exams | **LaTeX `article` class**. |
| PDF exports | **None.** pptx only. |
| Form content | A content document mapping form fields to exact TR/EN text to paste. |

Beamer is retired because verbatim speaker notes are native to pptx and awkward in Beamer.
Precedent exists: `Lectures/week1/Week1-Intro.pptx` already carries notes on 25 of 27 slides.

Slide conventions carried over: title slide with week number; second slide is an overview
("Today: What We'll Explore"); one section per major topic; every week ends with a wrap-up.

### 4.1 Session sizing

~55 min talking + ~15–20 min activity + buffer ≈ 75 min. At ~130 words/min that is
**~6,000–7,000 words of script**, and at 180–220 words/slide, **26–32 slides**.
**32 slides is a ceiling, not a target.** Cut rather than compress.

## 5. Assessment

| Component | Weight | Format |
|---|---|---|
| Midterm | 40% | In-class written exam |
| Final | 60% | Final exam |
| Pop-up quizzes (5) | **+10 bonus** | Unannounced, in class, all 5 count |

Bonus is added to the 100-point base and capped at 100.
Quizzes are **10** multiple-choice questions, 4 options, with separate answer keys.
Last year's final — 40 MCQs, 2.5 points each, 90 minutes — is the structural model for
both exams.

**No term project.** Consequently `Midterm/midterm_assignment.tex` and its grading guide
are retired, not migrated.

**Exam style:** conventional recall-based, per instructor decision. The known risk — a
build-led course assessed on recall — is mitigated in design rather than in assessment:
every build week closes with an explicit "concepts you must be able to define and
diagnose" frame that feeds the exam bank directly.

**In-class artifacts are not graded.** Students keep them in a running folder so Week 14
has concrete material to synthesise.

## 6. Structure

**Weeks 1–5 baseline · Weeks 6–13 build · Week 14 synthesis**

| Wk | Topic | Artifact |
|---|---|---|
| 1 | Introduction: Prompt Engineering and Generative AI | — |
| 2 | A Brief History of AI, NLP, and LLMs | — |
| 3 | How LLMs Work — context windows, hallucination, model families | — |
| 4 | Principles of Effective Prompting | — |
| 5 | Controlling Style, Tone, and Format | — |
| 6 | Building Your First Tool Without Code | Micro-Tool |
| 7 | Grounding AI in Your Own Sources | Grounded Assistant |
| 8 | Verification: Knowing When AI Is Wrong | Test Set |
| 9 | AI Agents and Workflow Automation | Automation Chain |
| 10 | Building for Your Own Field | Field Build |
| 11 | Domain-Specific Applications | Domain Pack |
| 12 | Prompt Injection and AI Security | Attack & Patch Report |
| 13 | Ethics, Copyright, Responsible Use, Academic Integrity | — |
| 14 | Synthesis and Course Wrap-Up | — |

### 6.1 Build week format

Every week 6–12 follows the same shape, so students know what to expect:

1. **Demo** (~10 min) — instructor shows a finished artifact.
2. **Unpack** (~30 min) — how it works, where it breaks.
3. **Build** (~20 min) — students build a smaller version.
4. **Examinable concepts** (~5 min) — what they must be able to define and diagnose.

### 6.2 The artifact spine

Each artifact feeds the next. Build it → ground it → break it → automate it → integrate it
→ professionalise it → attack it.

- **Micro-Tool** (6) — one single-screen web tool for a task in their field, generated from
  a description. Live shareable page.
- **Grounded Assistant** (7) — an assistant over 3–5 documents they bring or select from a
  provided pack, plus five questions answered *with the supporting passage*.
- **Test Set** (8) — ten questions against their own Week 7 assistant: seven answerable,
  **three deliberately unanswerable from the sources**, run and recorded in a failure log.
  The three unanswerable questions are the core teaching device of the course — students
  watch a system they built an hour earlier answer confidently from nothing.
- **Automation Chain** (9) — a two-to-three-step workflow that runs without them. Capped at
  three steps so compounding failure is visible but survivable.
- **Field Build** (10) — Micro-Tool + Grounded Assistant + Automation Chain integrated into
  one thing they would genuinely use. Centrepiece artifact.
- **Domain Pack** (11) — glossary, three golden examples, and the output conventions of
  their field (SOAP note, IRAC, lesson plan, brief), bolted onto the Field Build.
- **Attack & Patch Report** (12) — students attack a **classmate's** Field Build (direct
  injection, poisoned source document, data-leak probe), document what worked, patch their
  own. Attacking someone else's build is deliberate: you cannot red-team a system whose
  seams you already know.

### 6.3 What was cut and why

- **"Prompting for Complex Problem Solving"** as a standalone week. ~50% overlap with
  Patterns, and its CoT material is now obsolete. Decomposition is taught through building
  in Weeks 6 and 10.
- **Multimodal** as a standalone week. Every frontier model is natively multimodal.
  Appears once, as examples in Week 6 (screenshots, documents as inputs) and Week 11.
- **Mid-Semester Review** — lowest-value session on the calendar.
- **The framework zoo.** CO-STAR, RACI, IDEA, SMART, PLAN, SCQA, MECE were taught across
  four weeks with no evidence base. **Teach one properly, name the rest on a single slide.**
  IRAC survives — it is a real legal-reasoning structure, not a prompting gimmick.
- **The enterprise-tooling layer:** DSPy, LangGraph, Temporal, Pydantic, BM25, git-based
  PromptOps, live-traffic A/B testing, BLEU/ROUGE, cosine similarity, Cohen's kappa.
  Unteachable to a law student, untestable on paper, stale within a year. Concepts survive
  where they matter (agents fail by compounding error); vendor names go.

## 7. Content standards

- **Every week needs at least one in-class activity**, runnable cold: no student pre-work,
  no instructor setup beyond opening a browser. Accounts must be creatable in ~2 minutes.
  **Every activity needs a primary tool, an independent fallback, and a demo path.**
- **Teach transferable concepts, illustrate with current tools.** Never build a learning
  outcome around one vendor.
- **Cite every factual and statistical claim** to the standard of last year's Week 13.
  Flag anything unsourceable rather than inventing it.
- **Verify currency by web search** — model families, free-tier limits, tool availability.
  Report explicitly which claims could not be verified.
- **No code in required material.** Any code shown is optional and explained plainly.
- **Rotate examples across disciplines** — healthcare, law, education, business, engineering.

### 7.1 Known-stale content requiring re-verification

- "Why Prompting Matters in 2025" (Week 1); GPT-3/GPT-4 parameter claims (Week 2)
- "GPT-2 2019, GPT-3 2020, GPT-4 2023" model timeline (Week 2)
- **The Week 2 hallucination exercise uses "OpenAI released GPT-5 in 2018" as its false
  statement — this no longer reads as obviously false and must be replaced.**
- Claude 3.x / Gemini 1.5 / GPT-4o described as current (Weeks 9, 13)
- "Knowledge cutoff e.g. 2023" (Week 10)
- Tool free-tier limits for all build weeks

### 7.2 Defects found in existing material

- `Lectures/week8/quiz_week6_week8.tex` is titled "Quiz 4"; its answer key says "Quiz 3".
- `Lectures/week11/week11.tex` has an unescaped `&` in `\section{Collaboration & Governance}`.
- Weeks 4, 6, 8, 10, 12, 13 have no in-class activity; Weeks 4 and 5 have activity
  sections explicitly commented out.
- Week 3 contains two near-duplicate anti-pattern slides within the same deck.

## 8. Learning outcomes

Keep the existing four; add three covering **grounding**, **agent workflow design**, and
**security risk mitigation** — seven total.

## 9. Order of work

Each step ends with a stop for review.

1. ~~Read everything; summarise coverage, weaknesses, repetition.~~ **Done.**
2. **Restructure.** Create `archive/2025-2026/`, move the old semester in untouched, create
   the new working tree, verify nothing lost by file-count and checksum comparison.
3. **Theme + Week 1 as format prototype.** One complete deck with verbatim notes, so voice
   and density can be corrected before scaling. Deliberately ahead of everything else —
   fourteen decks of verbatim script is too much committed work to write in an unreviewed
   voice.
4. **Weeks 2–5** (baseline block).
5. **Weeks 6–8** (Micro-Tool, Grounded Assistant, Test Set).
6. **Weeks 9–10** (Automation Chain, Field Build).
7. **Weeks 11–13** (Domain Pack, Attack & Patch, Ethics).
8. **Week 14** (Synthesis).
9. **Assessment materials** — 5 × 10-question quizzes with keys, midterm + solution,
   final + solution, makeup exam. All compiled.
10. **Form content document** — field-by-field TR/EN text to paste. Blank current templates
    in `PROGRAM DIŞI SEÇMELİ DERS BAŞVURU BELGELERİ/` are the field reference; content
    reused from `CourseInformation/` where still accurate. The instructor fills the forms.

## 10. Quality gates

- Every `.tex` compiles cleanly via `latexmk` before delivery. No uncompiled source.
- Every `.pptx` opens and carries notes on every content slide.
- Each step reports what changed, including anything left out and why.
- Verified available: `latexmk`, `pdflatex`, `pandoc`, `python-pptx`.
