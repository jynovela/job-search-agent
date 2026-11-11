#!/usr/bin/env python3
"""Check a rendered resume PDF against job-search/resume-build-rules.md.

Usage: python3 verify_resume.py "<file>.pdf"

Checks: exactly 2 pages, the page split set in tools/config.json,
every line starting on the left margin or the bullet indent, dates flush with the
right margin and not bold, widow words, bold or italics inside bullets, banned
punctuation (em dash, semicolon, list colon, straight quotes), and the PDF title
matching the file name. Prints "OK" or one line per problem.
"""
import json
import os
import re
import sys

import pdfplumber
from pypdf import PdfReader

CONFIG = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json"), encoding="utf-8"))

LEFT, INDENT, RIGHT = 43.2, 50.4, 568.8
DATE = re.compile(r"[A-Z][a-z]{2} \d{4} – (?:[A-Z][a-z]{2} \d{4}|Present)\)?$")


def main(path):
    out = []
    pdf = pdfplumber.open(path)
    if len(pdf.pages) != 2:
        out.append(f"{len(pdf.pages)} pages, must be exactly 2")
    for i, page in enumerate(pdf.pages):
        lines = page.extract_text_lines()
        for k, l in enumerate(lines):
            text, chars = l["text"], l["chars"]
            x0 = round(chars[0]["x0"], 1)
            if text.startswith("▪"):
                x0 = round(chars[0]["x0"], 1)
                rest = [c for c in chars[1:] if c["text"].strip()]
                if x0 != LEFT or round(rest[0]["x0"], 1) != INDENT:
                    out.append(f"p{i+1} bullet misaligned: {text[:40]}")
                if any("Bold" in c["fontname"] or "Italic" in c["fontname"] for c in rest):
                    out.append(f"p{i+1} bold or italic inside a bullet: {text[:40]}")
            elif x0 not in (LEFT, INDENT):
                out.append(f"p{i+1} line starts at x={x0}, not the margin: {text[:40]}")
            # a wrapped bullet line that ends the bullet must hold 4+ words
            if x0 == INDENT and len(text.split()) < 4:
                nxt = lines[k + 1] if k + 1 < len(lines) else None
                if nxt is None or round(nxt["chars"][0]["x0"], 1) != INDENT:
                    out.append(f"p{i+1} widow: \"{text}\"")
            m = DATE.search(text)
            if m and not text.startswith("▪") and not text.endswith(")"):
                if abs(chars[-1]["x1"] - RIGHT) > 0.3:
                    out.append(f"p{i+1} date not flush right: {text[-22:]}")
                date_chars = chars[len(text) - len(m.group(0)):]
                if any("Bold" in c["fontname"] for c in date_chars):
                    out.append(f"p{i+1} date is bold: {m.group(0)}")
        p1, p2 = CONFIG.get("page1_must_include"), CONFIG.get("page2_starts_with")
        if i == 0 and p1 and not any(p1 in l["text"] for l in lines):
            out.append(p1 + " is not on page 1")
        if i == 1 and p2 and lines and not lines[0]["text"].startswith(p2):
            out.append("page 2 does not start with " + p2 + ": " + lines[0]["text"][:40])

    text = "\n".join(p.extract_text() for p in pdf.pages)
    for bad, label in [("—", "em dash"), (";", "semicolon"), (": ", "colon"), ("'", "straight apostrophe"),
                       ('"', "straight quote")]:
        for m in re.finditer(re.escape(bad), text):
            ctx = text[max(0, m.start() - 30):m.end() + 10].replace("\n", " ")
            if bad == ";" and any(w in ctx for w in CONFIG.get("verbatim_semicolon_markers", [])):
                continue   # degree lines are copied verbatim
            out.append(f"{label}: ...{ctx}...")

    title = (PdfReader(path).metadata or {}).get("/Title", "")
    name = os.path.basename(path)[:-4]
    if title != name:
        out.append(f"PDF title \"{title}\" does not match file name \"{name}\"")
    if f" - {CONFIG['file_name']} - Resume - " not in os.path.basename(path):
        out.append(f"file name must be \"<Company> - <Role> - {CONFIG['file_name']} - Resume - <Mon YYYY>.pdf\"")

    print(os.path.basename(path) + ":", "OK" if not out else "")
    for o in out:
        print("  " + o)
    return 0 if not out else 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
