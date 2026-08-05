# Course Update Prompt

**My recommendation before you use this: don't start from scratch.** Weeks 1–6 are well-sequenced and still accurate — rewriting them would burn your week and produce something no better. The prompt below archives the old semester intact, migrates what works, and rebuilds only what's genuinely out of date. That's four new/rewritten sessions instead of fourteen.

Copy everything between the lines into a fresh session with this folder connected.

---

## PROMPT — copy from here

You are helping me rebuild an undergraduate elective course for the upcoming semester. Work carefully and ask me the questions in §10 before producing any slides.

### 1. Context — who I am and what this course is

I am Mehmet Ali Akyol, PhD, and I teach at **Ankara Medipol Üniversitesi**. Last year I delivered a 14-week course called **Prompt Engineering** (Turkish title: *İstem Mühendisliği*). I am now revising and retitling it to **Prompt Engineering and Large Language Models** (*İstem Mühendisliği ve Büyük Dil Modelleri*).

**Critical facts about this course — these constrain everything:**

- It is a **program dışı seçmeli ders** — a university-wide elective open to students from **all disciplines**, not a computer engineering course.
- **There is no prerequisite and no programming requirement.** Students come from healthcare, law, education, business, engineering, and elsewhere. Assume no Python, no command line, no API keys.
- Approved format: **2 hours theoretical per week, 0 practical/lab, 2 credits, 2 AKTS.** I am requesting an increase to 3 AKTS to accommodate a term project.
- **Language of instruction: English.**
- Tools must be **browser-based with no installation required**. This is stated in the approved course proposal form. Free tiers only — do not assume students can pay for anything.
- 14 weeks, one session per week.

### 2. Source material — read this before doing anything

Everything from last year is in this folder. **Read it first.** Do not propose changes to material you have not read.

```
Lectures/week1/ … week14/     Beamer slide sources (.tex) + compiled PDFs
Lectures/quiz_2.pdf … quiz_6.pdf   5 pop quizzes as delivered
Lectures/week8/quiz_week6_week8.tex + _answers.tex   quiz source + answer key
CourseInformation/
  Ders Bilgi Formu_prompt_eng.docx           official course information form
  Program Dışı Seçmeli Ders Öneri Formu_prompt_eng.docx   elective proposal form
  midterm?/midterm_exam.tex + _sample_solution.tex
Final/final_exam.tex, makeup_exam.tex
DersiSecenOgrenciler.xls / .csv               enrolled students
DersiSecenOgrenciler_with_midterm.csv         midterm results
```

Start by reading all fourteen `weekN.tex` files, the quiz source, the midterm, and both .docx forms. Then summarize back to me, in one page, what the course currently covers and where you see the weakest material. I want to see that summary before you write any slides.

### 3. Delivered syllabus (last year)

1. Introduction to Prompt Engineering
2. How LLMs Work (Non-technical Overview)
3. Principles of Good Prompt Design
4. Prompt Patterns & Frameworks
5. Controlling Style, Tone, and Format
6. Iterative Prompt Refinement
7. Mid-Semester Review
8. Evaluating AI Outputs
9. Multimodal Prompting
10. Prompting for Complex Problem Solving
11. Domain-Specific Applications (healthcare, legal, education, finance, engineering)
12. Ethics, Copyright, and Responsible Use
13. Emerging Trends (agentic AI, orchestration, tooling, AI security — overloaded)
14. Course Wrap-Up

### 4. What changes, and why

Three problems with the current version:

**Week 13 is overloaded.** It holds five sections — advanced architectures, agentic AI and orchestration, prompt engineering lifecycle and tooling, AI security and risks, strategic recommendations. That is roughly three weeks of material compressed into one session, and it is the material students most want.

**There is no coverage of grounding.** The course teaches students to write excellent prompts but never how to point a model at *their own* documents. For a cross-disciplinary elective this is the highest-value missing skill, and no-code tools now make it teachable without programming.

**Multimodal no longer merits a standalone week.** Every frontier model is natively multimodal; treating it as a special technique dates the course. Distribute it as examples inside Weeks 4 and 10.

Week 7 (Mid-Semester Review) is the lowest-value session on the calendar given that the midterm is a separate take-home assignment, so it becomes the slot for grounding.

### 5. Target syllabus

| Wk | Topic | Action |
|---|---|---|
| 1 | Introduction to Prompt Engineering | migrate unchanged |
| 2 | How LLMs Work — **extend**: context windows, tokenization, why hallucination happens, current model families | revise |
| 3 | Principles of Good Prompt Design | migrate unchanged |
| 4 | Prompt Patterns & Frameworks *(fold in multimodal examples)* | light edit |
| 5 | Controlling Style, Tone, and Format | migrate unchanged |
| 6 | Iterative Prompt Refinement | migrate unchanged |
| 7 | **Grounding AI in Your Own Sources** | **write new** |
| 8 | Evaluating AI Outputs & Verification | migrate, light strengthening |
| 9 | **AI Agents and Workflow Automation** | **write new** |
| 10 | Prompting for Complex Problem Solving *(fold in multimodal examples)* | light edit |
| 11 | Domain-Specific Applications | migrate unchanged |
| 12 | **Prompt Injection and AI Security** | **write new** |
| 13 | Ethics, Copyright, and Responsible Use | migrate from old wk12 |
| 14 | Project Showcase and Wrap-Up | revise for new project format |

**The three new sessions:**

**Week 7 — Grounding AI in Your Own Sources.** Why models fail on material they were not trained on. What retrieval does, conceptually — no vector-database implementation. Hands-on with no-code grounding tools (NotebookLM, Claude Projects, custom GPTs, or current equivalents). Source quality and how document structure affects answers. How to check whether an answer is actually supported by the source rather than plausible-sounding. Worked examples from at least three different disciplines.

**Week 9 — AI Agents and Workflow Automation.** What distinguishes an agent from a chatbot. Planning, tool use, and termination conditions. Building a multi-step automation with no-code tooling. Where agents reliably fail — compounding errors, silent failure, cost blowups — and how to design around it. When an agent is the wrong answer and a single prompt is better. Use automation examples drawn from the disciplines covered in Week 11.

**Week 12 — Prompt Injection and AI Security.** Direct and indirect prompt injection. Jailbreaking and why it works. Data leakage through shared context and chat history. Risks specific to the grounded systems built in Week 7 and the agent workflows from Week 9. Practical defenses at the user level. Safe handling of institutional, personal, and patient/client data. Include a live in-class exercise where students attempt to subvert a grounded assistant built in Week 7 — this should be the memorable session of the semester.

### 6. Assessment structure (changed from last year)

Last year: midterm (take-home assignment) plus written final. New structure:

| Component | Weight | Notes |
|---|---|---|
| Pop-up quizzes — 5 given, **best 4 count** | 20% | unannounced, ~10 min, in class |
| Midterm | 30% | keep the take-home assignment format from last year — it worked |
| **Term project**, replacing the final exam | 50% | presented Week 14 |

**Term project specification** — students build and document a grounded, prompt-driven AI workflow addressing a problem from *their own* discipline. Five deliverables:

1. Working artifact — a grounded assistant, automation, or agent workflow
2. Prompt and design documentation — what was tried, what failed, what changed
3. Evaluation evidence — how they know it works, using Week 8 methods
4. Risk statement — injection and privacy considerations from Week 12
5. Week 14 presentation

Grade on problem framing, prompt and grounding quality, evaluation rigor, and risk awareness — explicitly **not** on technical sophistication, so that a law student and an engineering student can both earn full marks. Individual or pairs.

I need a **written project brief** for students and a **grading rubric** as separate documents.

### 7. Technical requirements — match the existing setup exactly

Slides are **Beamer**, compiled with **pdfLaTeX** via **latexmk**. Use the newer preamble style found in `week13.tex`, not the older `week1.tex` one:

```latex
\documentclass{beamer}
\usetheme{Madrid}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{hyperref}
\usepackage{tikz}
\usepackage{booktabs}
\title{Prompt Engineering and Large Language Models}
\author{Mehmet Ali Akyol, PhD}
\institute{Ankara Medipol University}
\date{\today}
```

Conventions to follow:
- Title frame carries the week number and title, as in `week13.tex`
- Second frame is always an overview — "Today: What We'll Explore"
- `\section{}` per major topic; sections appear in the navigation bar
- Every week ends with a Wrap-up frame and, where the old course had one, an Assignment frame
- Quizzes and exams use `article` class, not Beamer — follow `quiz_week6_week8.tex`
- Quizzes are **12 multiple-choice questions**, four options each, with a separate answer key

**Compile every `.tex` you produce** and fix errors until it builds cleanly. Do not hand me source that has not compiled.

### 8. Content quality bar

- **Every week needs at least one in-class activity.** The existing course does this well — preserve the pattern.
- **Teach transferable concepts, illustrate with current tools.** A student should understand *grounding*, not just "how to use NotebookLM." Name specific tools in examples, but never build a learning outcome around one vendor.
- **Cite sources for factual and statistical claims.** Week 13 does this (McKinsey, Gartner) — maintain that standard. Flag any statistic you cannot source rather than inventing one.
- **Verify currency.** Model capabilities, pricing, and tool availability change fast. Search the web for anything version-dependent rather than relying on your training data, and tell me explicitly which claims you could not verify.
- **Respect the audience.** Non-technical students, mixed disciplines. No code in required material. If you show code, mark it optional and explain it in plain language.
- **Examples should span disciplines** — not all software examples. Rotate through healthcare, law, education, business, and engineering.

### 9. Deliverables and order of work

Work in this order and **stop for my approval after each numbered step**:

1. **Read everything in §2.** Produce the one-page summary of current coverage and weaknesses. Stop.
2. **Set up the new structure.** Create `archive/2025-2026/` and move the old semester into it untouched. Create the new working tree. Confirm nothing is lost. Stop.
3. **Migrate the unchanged weeks** (1, 3, 5, 6, 8, 11) into the new structure, updating only the title block and any factually stale claim. List what you changed. Stop.
4. **Revise weeks 2, 4, 10, 14.** Stop.
5. **Write week 7** (Grounding). Stop for review before continuing — I want to check tone and depth on the first new session before you write the other two.
6. **Write weeks 9 and 12** (Agents, Security). Stop.
7. **Produce assessment materials**: 5 quizzes with answer keys mapped to the new week structure, the midterm assignment, the project brief, and the grading rubric. Stop.
8. **Update the administrative forms** — `Ders Bilgi Formu` and `Program Dışı Seçmeli Ders Öneri Formu` — with the new title, description, learning outcomes, weekly plan, and assessment structure, in both Turkish and English where the form requires it.

Also produce updated **learning outcomes**. Keep the existing four and add three covering grounding, agent workflow design, and security risk mitigation.

### 10. Ask me these before starting

1. Which semester and academic year is this for? (affects dates and what counts as "current")
2. Should quizzes stay 12 questions, or change length?
3. Do you want the midterm to stay a take-home assignment, or become an in-class written exam?
4. Should the term project be individual, pairs, or your choice?
5. Are there tools your students cannot access from campus, or that the university blocks?
6. Did anything in last year's delivery go badly — a week that fell flat, an activity that did not work, a quiz that was too hard? I have the material but not the experience of teaching it.

Question 6 matters most. You have data I do not: `DersiSecenOgrenciler_with_midterm.csv` shows how students actually performed, and I would rather fix a week you know was weak than one I merely suspect.

## PROMPT — copy to here

---

## Notes for you, not for the prompt

**On archiving.** The prompt has the assistant create `archive/2025-2026/` and move the old semester there intact before touching anything. Your compiled PDFs are the record of what was actually delivered — keep them even though they can be regenerated, since the `.tex` will drift.

**Consider a git repo first.** `git init && git add -A && git commit` in this folder before you start gives you a free undo across the whole rebuild. There's a `.code-workspace` file here so you're already in VS Code — thirty seconds of setup, and it removes the risk of an agent overwriting a week you wanted.

**The step-by-step stops are deliberate.** An agent given "rebuild my course" in one shot will produce fourteen weeks of plausible, uniform, slightly generic slides. Reviewing after week 7 costs you ten minutes and catches tone problems before they get replicated across three sessions.

**Question 6 is the highest-value input you can give.** Nothing in the folder tells me which sessions actually landed. If you remember that Week 9 dragged or that the Week 11 domain tour felt rushed, say so in the first message — it's worth more than anything I inferred from reading the slides.
