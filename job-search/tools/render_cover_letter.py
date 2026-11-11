#!/usr/bin/env python3
"""Render a cover letter from markdown to PDF in the cover letter layout, with justified paragraphs.

Usage: python3 render_cover_letter.py letter.md "Company - Role - <Name> - Cover Letter - Mon YYYY.pdf"

Markdown format: blocks separated by a blank line. The first block is the date,
then "Dear <Company> Hiring Team,", the body paragraphs, and the sign-off block:
  Sincerely,
  <Full Name>
  <email> | <phone>
Single line breaks inside a block are kept (used for the sign-off).
"""
import os
import sys

from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_resume import CONFIG, markup, register_fonts  # noqa: E402

MARGIN = 49.2  # matches the Oct 2026 cover letters


def build(md_path, pdf_path):
    register_fonts()
    body = ParagraphStyle("body", fontName="TNR", fontSize=11, leading=12.2, alignment=TA_JUSTIFY)
    lines = ParagraphStyle("lines", parent=body, alignment=TA_LEFT)  # sign-off and other multi-line blocks
    blocks = [b.strip() for b in open(md_path, encoding="utf-8").read().split("\n\n") if b.strip()]
    story = []
    for b in blocks:
        rows = b.splitlines()
        story.append(Paragraph("<br/>".join(markup(l.strip()) for l in rows), body if len(rows) == 1 else lines))
        story.append(Spacer(1, 12))
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, leftMargin=MARGIN - 6, rightMargin=MARGIN - 6,
                            topMargin=72, bottomMargin=60, title=os.path.basename(pdf_path)[:-4],
                            author=CONFIG["full_name"])
    doc.build(story)
    from pypdf import PdfReader
    pages = len(PdfReader(pdf_path).pages)
    print(f"{pdf_path}: {pages} page(s)")
    if pages > 1:
        print("warning: cover letter is over one page; cut it", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    build(sys.argv[1], sys.argv[2])
