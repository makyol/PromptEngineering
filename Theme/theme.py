"""
Shared deck theme for "Prompt Engineering and Large Language Models".

Every lecture deck is generated with these helpers so all 14 weeks look
identical. Layouts are drawn explicitly on blank slides rather than using
PowerPoint's built-in placeholders, which gives full control over the look.

Every slide-building function takes a `notes` argument holding the verbatim
speaker script. Notes are mandatory: build_deck() refuses to save a deck with
an unscripted content slide.

Usage:
    from theme import *
    prs = new_deck()
    title_slide(prs, 1, "Introduction", "Prompt Engineering and Generative AI")
    content_slide(prs, "A heading", ["point one", "point two"], notes="...")
    save(prs, "week01.pptx")
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

# ---------------------------------------------------------------- palette
# Neutral academic palette. NOT official Ankara Medipol branding — if the
# university publishes brand colours, replace INK and ACCENT here and every
# deck picks them up on rebuild.
INK        = RGBColor(0x1F, 0x29, 0x37)   # titles, dark bands
BODY       = RGBColor(0x33, 0x3D, 0x4B)   # body text
MUTED      = RGBColor(0x6B, 0x77, 0x87)   # captions, footers
ACCENT     = RGBColor(0x0F, 0x76, 0x6E)   # teal — structure, rules, bullets
WARN       = RGBColor(0xB4, 0x53, 0x09)   # amber — activities, cautions
PANEL      = RGBColor(0xF1, 0xF5, 0xF9)   # light panel fill
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)

# ---------------------------------------------------------------- type
# Calibri ships with Microsoft Office on both macOS and Windows, so decks
# render identically on any machine that can open them.
FONT_HEAD = "Calibri Light"
FONT_BODY = "Calibri"

SZ_TITLE_SLIDE = Pt(40)
SZ_TITLE       = Pt(30)
SZ_SECTION     = Pt(34)
SZ_BODY        = Pt(19)
SZ_SUB         = Pt(16)
SZ_CALLOUT     = Pt(32)
SZ_FOOT        = Pt(10)

# ---------------------------------------------------------------- geometry
W, H = Inches(13.333), Inches(7.5)
MARGIN   = Inches(0.85)
TOP_RULE = Inches(1.55)      # y of the accent rule under a slide title
BODY_TOP = Inches(1.95)
BODY_W   = W - 2 * MARGIN

_COURSE = "Prompt Engineering and Large Language Models"


# ================================================================ internals
def _txbox(slide, x, y, w, h):
    box = slide.shapes.add_textbox(x, y, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    return tf


def _style(run, *, size, color, font=FONT_BODY, bold=False, italic=False):
    run.font.size = size
    run.font.color.rgb = color
    run.font.name = font
    run.font.bold = bold
    run.font.italic = italic


def _rect(slide, x, y, w, h, color):
    from pptx.enum.shapes import MSO_SHAPE
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    shp.line.fill.background()
    shp.shadow.inherit = False
    return shp


def _blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def _notes(slide, text):
    slide.notes_slide.notes_text_frame.text = (text or "").strip()


def _slide_title(slide, text):
    tf = _txbox(slide, MARGIN, Inches(0.62), BODY_W, Inches(0.9))
    p = tf.paragraphs[0]
    _style(p.add_run(), size=SZ_TITLE, color=INK, font=FONT_HEAD, bold=True)
    p.runs[0].text = text
    _rect(slide, MARGIN, TOP_RULE, Inches(1.15), Pt(3), ACCENT)


def _footer(slide, week, prs):
    n = len(prs.slides)
    tf = _txbox(slide, MARGIN, H - Inches(0.55), BODY_W, Inches(0.3))
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = f"Week {week}  ·  {_COURSE}"
    _style(r, size=SZ_FOOT, color=MUTED)
    # slide number, right aligned
    tf2 = _txbox(slide, W - MARGIN - Inches(1.0), H - Inches(0.55), Inches(1.0), Inches(0.3))
    p2 = tf2.paragraphs[0]
    p2.alignment = PP_ALIGN.RIGHT
    r2 = p2.add_run()
    r2.text = str(n)
    _style(r2, size=SZ_FOOT, color=MUTED)


def _parse_item(it):
    """Normalise a bullet spec to (level, text, style).

    Accepts, in either order of convenience:
        "text"                     -> level 0
        (1, "text")                -> explicit level
        (1, "text", "bold")        -> explicit level + style
        ("text", None)             -> level 0, no style
        ("text", None, "bold")     -> level 0, styled
    Style is whichever trailing element is a string: 'bold' or 'plain'.
    """
    if not isinstance(it, tuple):
        return 0, it, None
    if isinstance(it[0], int):
        lvl, text = it[0], it[1]
        rest = it[2:]
    else:
        lvl, text = 0, it[0]
        rest = it[1:]
    style = next((r for r in rest if isinstance(r, str)), None)
    return lvl, text, style


def _bullets(tf, items, first=True):
    """items: see _parse_item for accepted forms."""
    for it in items:
        lvl, text, style = _parse_item(it)

        p = tf.paragraphs[0] if (first and not tf.paragraphs[0].runs) else tf.add_paragraph()
        first = False
        p.level = lvl
        p.space_after = Pt(10 if lvl == 0 else 5)
        p.line_spacing = 1.15

        if text == "":
            continue

        marker = "" if style == "plain" else ("—  " if lvl else "•  ")
        r = p.add_run()
        r.text = f"{marker}{text}"
        _style(
            r,
            size=SZ_BODY if lvl == 0 else SZ_SUB,
            color=BODY if lvl else INK,
            bold=(style == "bold"),
        )
    return first


# ================================================================ public API
def new_deck():
    prs = Presentation()
    prs.slide_width, prs.slide_height = W, H
    prs._pe_week = None
    return prs


def title_slide(prs, week, title, subtitle, *, notes=""):
    """Opening slide: dark band, week number, title."""
    prs._pe_week = week
    s = _blank(prs)
    _rect(s, Emu(0), Emu(0), W, Inches(4.55), INK)
    _rect(s, MARGIN, Inches(1.5), Inches(1.15), Pt(4), ACCENT)

    tf = _txbox(s, MARGIN, Inches(0.95), BODY_W, Inches(0.45))
    r = tf.paragraphs[0].add_run()
    r.text = f"WEEK {week}"
    _style(r, size=Pt(15), color=ACCENT, bold=True)
    r.font._rPr.set("spc", "220")

    tf = _txbox(s, MARGIN, Inches(1.95), Inches(10.6), Inches(1.5))
    r = tf.paragraphs[0].add_run()
    r.text = title
    _style(r, size=SZ_TITLE_SLIDE, color=WHITE, font=FONT_HEAD, bold=True)

    tf = _txbox(s, MARGIN, Inches(3.35), Inches(10.6), Inches(0.6))
    r = tf.paragraphs[0].add_run()
    r.text = subtitle
    _style(r, size=Pt(19), color=RGBColor(0xC3, 0xD0, 0xDB))

    tf = _txbox(s, MARGIN, Inches(5.15), BODY_W, Inches(1.4))
    for i, line in enumerate(
        [_COURSE, "Mehmet Ali Akyol, PhD", "Ankara Medipol University"]
    ):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(4)
        r = p.add_run()
        r.text = line
        _style(r, size=Pt(15) if i else Pt(16), color=MUTED if i else INK, bold=(i == 0))
    _notes(s, notes)
    return s


def section_slide(prs, number, title, *, notes=""):
    """Divider between major topics."""
    s = _blank(prs)
    _rect(s, Emu(0), Emu(0), Inches(0.32), H, ACCENT)
    tf = _txbox(s, Inches(1.4), Inches(3.0), Inches(11.0), Inches(0.5))
    r = tf.paragraphs[0].add_run()
    r.text = f"PART {number}"
    _style(r, size=Pt(14), color=ACCENT, bold=True)
    tf = _txbox(s, Inches(1.4), Inches(3.5), Inches(11.0), Inches(1.2))
    r = tf.paragraphs[0].add_run()
    r.text = title
    _style(r, size=SZ_SECTION, color=INK, font=FONT_HEAD, bold=True)
    _notes(s, notes)
    return s


def content_slide(prs, title, bullets, *, notes=""):
    s = _blank(prs)
    _slide_title(s, title)
    tf = _txbox(s, MARGIN, BODY_TOP, BODY_W, H - BODY_TOP - Inches(0.8))
    _bullets(tf, bullets)
    _footer(s, prs._pe_week, prs)
    _notes(s, notes)
    return s


def two_col_slide(prs, title, left_head, left, right_head, right, *, notes=""):
    s = _blank(prs)
    _slide_title(s, title)
    colw = (BODY_W - Inches(0.8)) / 2
    for x, head, items in (
        (MARGIN, left_head, left),
        (MARGIN + colw + Inches(0.8), right_head, right),
    ):
        tf = _txbox(s, x, BODY_TOP, colw, Inches(0.45))
        r = tf.paragraphs[0].add_run()
        r.text = head
        _style(r, size=Pt(18), color=ACCENT, bold=True)
        tf = _txbox(s, x, BODY_TOP + Inches(0.6), colw, H - BODY_TOP - Inches(1.4))
        _bullets(tf, items)
    _footer(s, prs._pe_week, prs)
    _notes(s, notes)
    return s


def callout_slide(prs, statement, sub="", *, notes=""):
    """One big idea, nothing else. Use sparingly — it lands because it's rare."""
    s = _blank(prs)
    _rect(s, Emu(0), Emu(0), W, H, PANEL)
    _rect(s, MARGIN, Inches(2.55), Inches(1.15), Pt(4), ACCENT)
    tf = _txbox(s, MARGIN, Inches(2.95), Inches(11.2), Inches(2.0))
    r = tf.paragraphs[0].add_run()
    r.text = statement
    _style(r, size=SZ_CALLOUT, color=INK, font=FONT_HEAD, bold=True)
    if sub:
        tf = _txbox(s, MARGIN, Inches(4.85), Inches(11.2), Inches(0.8))
        r = tf.paragraphs[0].add_run()
        r.text = sub
        _style(r, size=Pt(18), color=BODY)
    _footer(s, prs._pe_week, prs)
    _notes(s, notes)
    return s


def activity_slide(prs, title, steps, *, minutes=None, notes=""):
    """In-class activity. Amber accent so it reads as 'stop talking, start doing'."""
    s = _blank(prs)
    tf = _txbox(s, MARGIN, Inches(0.62), BODY_W, Inches(0.4))
    r = tf.paragraphs[0].add_run()
    r.text = "IN-CLASS ACTIVITY" + (f"  ·  {minutes} MINUTES" if minutes else "")
    _style(r, size=Pt(13), color=WARN, bold=True)

    tf = _txbox(s, MARGIN, Inches(1.05), BODY_W, Inches(0.8))
    r = tf.paragraphs[0].add_run()
    r.text = title
    _style(r, size=SZ_TITLE, color=INK, font=FONT_HEAD, bold=True)
    _rect(s, MARGIN, Inches(1.95), Inches(1.15), Pt(3), WARN)

    tf = _txbox(s, MARGIN, Inches(2.35), BODY_W, H - Inches(3.2))
    _bullets(tf, steps)
    _footer(s, prs._pe_week, prs)
    _notes(s, notes)
    return s


def concepts_slide(prs, items, *, notes=""):
    """Closes every build week: what must be definable and diagnosable on the exam."""
    s = _blank(prs)
    _slide_title(s, "Concepts You Must Be Able to Define and Diagnose")
    _rect(s, MARGIN, BODY_TOP, BODY_W, H - BODY_TOP - Inches(0.9), PANEL)
    tf = _txbox(s, MARGIN + Inches(0.45), BODY_TOP + Inches(0.35),
                BODY_W - Inches(0.9), H - BODY_TOP - Inches(1.6))
    _bullets(tf, items)
    _footer(s, prs._pe_week, prs)
    _notes(s, notes)
    return s


def closing_slide(prs, *, notes=""):
    s = _blank(prs)
    _rect(s, Emu(0), Emu(0), W, H, INK)
    tf = _txbox(s, MARGIN, Inches(2.7), Inches(11.2), Inches(1.0))
    r = tf.paragraphs[0].add_run()
    r.text = "Questions?"
    _style(r, size=Pt(44), color=WHITE, font=FONT_HEAD, bold=True)
    _rect(s, MARGIN, Inches(3.9), Inches(1.15), Pt(4), ACCENT)
    tf = _txbox(s, MARGIN, Inches(4.3), Inches(11.2), Inches(1.0))
    for i, line in enumerate(["Mehmet Ali Akyol, PhD", "mehmetali.akyol@gmail.com"]):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(5)
        r = p.add_run()
        r.text = line
        _style(r, size=Pt(17), color=WHITE if i == 0 else RGBColor(0xC3, 0xD0, 0xDB))
    _notes(s, notes)
    return s


def save(prs, path, *, require_notes=True):
    """Save, refusing to emit a deck with unscripted content slides."""
    if require_notes:
        missing = [
            i + 1
            for i, s in enumerate(prs.slides)
            if not s.notes_slide.notes_text_frame.text.strip()
        ]
        if missing:
            raise SystemExit(f"Refusing to save {path}: slides missing notes: {missing}")
    prs.save(path)
    words = sum(
        len(s.notes_slide.notes_text_frame.text.split()) for s in prs.slides
    )
    n = len(prs.slides)
    print(f"{path}: {n} slides, {words} words of script (~{words/130:.0f} min speaking)")
