# Prompt Engineering and Large Language Models

İstem Mühendisliği ve Büyük Dil Modelleri — Ankara Medipol University
Program dışı seçmeli ders · Fall 2026–2027 · 2+0, 2 credits, 2 AKTS · English

Mehmet Ali Akyol, PhD

## Layout

| Path | Contents |
|---|---|
| `Lectures/week01…week14/` | Lecture decks (`.pptx`, 16:9, verbatim speaker notes) |
| `Assessment/Quizzes/` | 5 pop quizzes (10 MCQs each) + answer keys, LaTeX |
| `Assessment/Midterm/` | In-class written midterm + solution, LaTeX |
| `Assessment/Final/` | Final exam, makeup, solutions, LaTeX |
| `Theme/` | Shared pptx theme and build tooling |
| `Forms/` | Field-by-field TR/EN content for the official forms |
| `CourseInformation/` | Instructor credentials and supporting documents |
| `PROGRAM DIŞI SEÇMELİ DERS BAŞVURU BELGELERİ/` | Blank university templates (current versions) |
| `archive/2025-2026/` | Previous delivery, preserved unchanged |
| `docs/superpowers/specs/` | Design spec for this rebuild |

## Course structure

Weeks 1–5 baseline · Weeks 6–13 build · Week 14 synthesis

| Wk | Topic | Artifact |
|---|---|---|
| 1 | Introduction: Prompt Engineering and Generative AI | — |
| 2 | A Brief History of AI, NLP, and LLMs | — |
| 3 | How LLMs Work | — |
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

## Assessment

Midterm 40% (in-class written) · Final 60% · Quizzes +10 bonus points (all 5 count)

## Building

```bash
latexmk -pdf Assessment/Quizzes/quiz01.tex   # exams and quizzes
```

Decks are generated with `python-pptx`; see `Theme/`.

Full rationale, constraints, and content standards:
[`docs/superpowers/specs/2026-08-07-course-rebuild-design.md`](docs/superpowers/specs/2026-08-07-course-rebuild-design.md)
