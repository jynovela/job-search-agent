#!/usr/bin/env python3
"""Render a tailored resume from markdown to PDF, following job-search/resume-build-rules.md.

Usage: python3 render_resume.py resume.md "<Company> - <Role> - <Name> - Resume - <Mon YYYY>.pdf"

Markdown format (see tools/example-resume.md):
  # Name
  Headline line (with or without _underscores_)
  contact line
  ## SECTION
  ### Company (note) | City, ST [| Dates]   (dates on the company line only when it has several titles)
  #### Title | Dates
  plain paragraph = role intro (or the summary); "- " = bullet
  EARLIER CAREER lines: **Title**, Company (Mon YYYY – Mon YYYY)
  EDUCATION: **Degree** line, then _School, City | Mon YYYY_ line

Page 2 starts with the company named "page2_starts_with" in tools/config.json
(or the 4th company if that is missing). Your name also comes from config.json.
Prints layout warnings (bullets over 3 lines, intros over 2, widow words, markup
inside bullets). Run verify_resume.py on the PDF afterwards.
"""
import json
import os
import re
import sys
from xml.sax.saxutils import escape

from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, PageBreak,
                                PageTemplate, Paragraph, Table, TableStyle)
from reportlab.platypus.flowables import HRFlowable

CONFIG = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json"), encoding="utf-8"))
PAGE2 = CONFIG.get("page2_starts_with") or ""

IN = 72
LM = RM = 0.6 * IN          # left and right margins
TM = BM = 0.5 * IN          # top and bottom margins
W = letter[0] - LM - RM     # 7.3 in of text
HANG = 0.1 * IN             # bullet column and hanging indent
BODY = 10.5
LINE = 1.107                # single spacing: Liberation Serif's natural line height

FONT_DIRS = [
    "/usr/share/fonts/truetype/liberation",
    "/usr/share/fonts/liberation",
    os.path.expanduser("~/Library/Fonts"),
    "/Library/Fonts",
]


def register_fonts():
    """Liberation Serif has Times New Roman's exact metrics and is embedded in the PDF."""
    files = {"TNR": "Regular", "TNR-B": "Bold", "TNR-I": "Italic", "TNR-BI": "BoldItalic"}
    for d in FONT_DIRS:
        paths = {k: os.path.join(d, f"LiberationSerif-{v}.ttf") for k, v in files.items()}
        if all(os.path.exists(p) for p in paths.values()):
            for k, p in paths.items():
                pdfmetrics.registerFont(TTFont(k, p))
            pdfmetrics.registerFontFamily("TNR", normal="TNR", bold="TNR-B",
                                          italic="TNR-I", boldItalic="TNR-BI")
            return
    sys.exit("Liberation Serif not found. Install fonts-liberation (apt) or the Liberation fonts.")


def style(size, font="TNR", align=TA_LEFT, before=0, **kw):
    return ParagraphStyle(font + str(size), fontName=font, fontSize=size,
                          leading=round(size * LINE, 2), alignment=align, spaceBefore=before, **kw)


S = {}
warnings = []


def curly(text):
    """Curly apostrophes and quotes, then XML-escape for reportlab."""
    text = re.sub(r"(\w)'", "\\1\u2019", text).replace("'", "\u2018")
    text = re.sub(r'(^|[\s(\[])"', "\\1\u201c", text).replace('"', "\u201d")
    return escape(text)


def markup(text):
    """**bold** and _italic_ for header, earlier career and education lines."""
    text = curly(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    return re.sub(r"(?<![\w*])[_*](.+?)[_*](?![\w*])", r"<i>\1</i>", text)


def line_words(p, width):
    p.wrap(width, 10000)
    out = []
    for ln in p.blPara.lines:
        words = ln[1] if isinstance(ln, tuple) else [w.text for w in ln.words]
        out.append(" ".join(words).split())
    return out


def check(p, width, label, max_lines):
    lines = line_words(p, width)
    if len(lines) > max_lines:
        warnings.append(f"{label}: {len(lines)} lines (max {max_lines})")
    if len(lines) > 1 and len(lines[-1]) < 4:
        warnings.append(f"{label}: widow, last line is \"{' '.join(lines[-1])}\"")


def no_pad(t, valign):
    t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                           ("VALIGN", (0, 0), (-1, -1), valign)]))
    return t


def with_date(left_html, date, left_style, before):
    """Left text plus an italic, non-bold date ending exactly on the right margin."""
    dw = pdfmetrics.stringWidth(date, "TNR-I", BODY) + 2
    t = no_pad(Table([[Paragraph(left_html, left_style), Paragraph(curly(date), S["date"])]],
                     colWidths=[W - dw, dw]), "BOTTOM")
    t.spaceBefore = before
    return t


def bullet(text, label):
    """The ▪ sits in its own 0.1 in column, so every line of text starts at the same x."""
    if re.search(r"\*\*|(?<!\w)_\w", text):
        warnings.append(f"{label}: bold or italic markup inside a bullet was removed")
        text = text.replace("**", "")
        text = re.sub(r"(?<!\w)_(.+?)_(?!\w)", r"\1", text)
    p = Paragraph(curly(text), S["body"])
    check(p, W - HANG, label, 3)
    return no_pad(Table([[Paragraph("\u25aa", S["body"]), p]], colWidths=[HANG, W - HANG]), "TOP")


def heading(name):
    return [Paragraph(curly(name.upper()), S["section"]),
            HRFlowable(width="100%", thickness=0.5, color="black", spaceBefore=1, spaceAfter=6)]


def company_line(text, date):
    parts = [p.strip() for p in text.split("|")]
    if date is None and len(parts) == 3:
        date = parts.pop()
    name, place = parts[0], " | ".join(parts[1:])
    m = re.match(r"^(.*?)(\s\(.*\))?$", name)
    note = f"<font name='TNR'>{curly(m.group(2))}</font>" if m.group(2) else ""
    html = f"<b>{curly(m.group(1))}</b>{note}<b> | {curly(place)}</b>" if place else f"<b>{curly(m.group(1))}</b>{note}"
    if date:
        return with_date(html, date, S["company"], 10), m.group(1)
    p = Paragraph(html, S["company"])
    return p, m.group(1)


def build(md_path, pdf_path):
    register_fonts()
    S.update(
        name=style(20, "TNR-B"),
        headline=style(11, "TNR-I", before=6),
        contact=style(11, before=2),
        section=style(14, "TNR-B", before=10),
        body=style(BODY, align=TA_JUSTIFY),
        company=style(12, "TNR-B", before=10),
        title=style(BODY, "TNR-BI"),
        date=style(BODY, "TNR-I", align=TA_RIGHT),
        plain=style(BODY),
        degree=style(BODY, "TNR-B"),
    )
    lines = [l.rstrip() for l in open(md_path, encoding="utf-8").read().splitlines()]
    lines = [l for l in lines if l.strip() and l.strip() != "---"]

    story, header = [], []
    section, companies, block, company = None, 0, None, None
    degrees = 0

    def close_block():
        nonlocal block
        if block:
            story.append(KeepTogether(block["keep"]))
            story.extend(block["rest"])
            block = None

    def add(f):
        if block is None:
            story.append(f)
        elif block["open"]:
            block["keep"].append(f)
        else:
            block["rest"].append(f)

    for line in lines:
        s = line.strip()
        if s.startswith("# "):
            story += [Paragraph(curly(s[2:]), S["name"]),
                      HRFlowable(width="100%", thickness=0.5, color="black", spaceBefore=3, spaceAfter=0)]
        elif section is None and not s.startswith("#"):
            header.append(s)
            if len(header) == 1:
                story.append(Paragraph(curly(s.strip("_*")), S["headline"]))
            else:
                items = [x.strip() for x in s.split("|")]
                html = []
                for x in items:
                    href = "mailto:" + x if "@" in x else ("https://" + x if "linkedin.com" in x else None)
                    html.append(f'<a href="{href}" color="black">{curly(x)}</a>' if href else curly(x))
                story.append(Paragraph(" | ".join(html), S["contact"]))
        elif s.startswith("## "):
            close_block()
            section = s[3:].strip().upper()
            story += heading(section)
        elif s.startswith("### "):
            close_block()
            first, company = company_line(s[4:], None)
            companies += 1
            if (PAGE2 and company.startswith(PAGE2)) or (companies == 4 and not (PAGE2 and any(
                    l.strip().startswith("### " + PAGE2) for l in lines))):
                story.append(PageBreak())
            block = {"keep": [first], "rest": [], "open": True, "bullets": 0}
        elif s.startswith("#### "):
            parts = [p.strip() for p in s[5:].split("|")]
            first_role = block is not None and len(block["keep"]) == 1
            add(with_date(f"<b><i>{curly(parts[0])}</i></b>", parts[1] if len(parts) > 1 else "",
                          S["title"], 2 if first_role else 6))
        elif s.startswith(("- ", "* ", "\u25aa ")):
            label = f"{company or section} bullet"
            add(bullet(s[2:].strip(), label))
            if block is not None and block["open"]:
                block["open"] = False   # company line, title, intro and first bullet stay together
        elif section == "PROFESSIONAL SUMMARY":
            p = Paragraph(curly(s), S["body"])
            check(p, W, "summary", 99)
            words = len(s.split())
            if not 90 <= words <= 140:
                warnings.append(f"summary: {words} words (90 to 140)")
            story.append(p)
        elif section == "EDUCATION":
            if s.startswith("**"):
                story.append(Paragraph(markup(s), style(BODY, before=0 if degrees == 0 else 10)))
                degrees += 1
            else:
                story.append(Paragraph(markup(s if s.startswith("_") else f"_{s}_"), S["plain"]))
        elif section == "EARLIER CAREER" or block is None:
            story.append(Paragraph(markup(s), S["plain"]))
        else:
            p = Paragraph(curly(s), S["body"])
            check(p, W, f"{company} intro", 2)
            add(p)
    close_block()

    title = os.path.basename(pdf_path)
    title = title[:-4] if title.lower().endswith(".pdf") else title
    pages = []
    doc = BaseDocTemplate(pdf_path, pagesize=letter, leftMargin=LM, rightMargin=RM, topMargin=TM,
                          bottomMargin=BM, title=title, author=CONFIG["full_name"], subject="Resume")
    frame = Frame(LM, BM, W, letter[1] - TM - BM, 0, 0, 0, 0, id="f")
    doc.addPageTemplates([PageTemplate(frames=[frame], onPage=lambda c, d: pages.append(c.getPageNumber()))])
    doc.build(story)
    print(f"{pdf_path}: {len(pages)} page(s)")
    if len(pages) != 2:
        warnings.append(f"{len(pages)} pages, must be exactly 2")
    for w in warnings:
        print("warning:", w, file=sys.stderr)
    return len(pages)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    build(sys.argv[1], sys.argv[2])
