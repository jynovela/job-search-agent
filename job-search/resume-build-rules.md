# Full resume build rules (approved by the candidate, Oct 14 2026)

These rules add to the HARD STYLE RULES (now in `writing-check.md` and `voice.md`) and the TAILORING INSTRUCTIONS (now in the `tailor-resume` skill). They do not replace them.

## 1. Page and fonts
- US Letter (8.5 x 11 in). Margins 0.6 in left and right, 0.5 in top and bottom. Text width 7.3 in.
- Times New Roman everywhere, black. The PDF is built with Liberation Serif, which has the exact same letter widths as Times New Roman and looks the same.
- Exactly two pages. Page 1 holds the header, the summary, and the most recent roles (the "flexible" roles in section 6). Page 2 starts with the company named `page2_starts_with` in `tools/config.json`. If page 1 overflows, cut a bullet from a flexible role before cutting the summary.

## 2. Each element, top to bottom
| Element | Font | Alignment | Space before |
|---|---|---|---|
| Name | 20 pt bold, thin 0.5 pt line under it across the full text width | left | none |
| Headline "<Title> \| A, B & C" | 11 pt italic | left | 6 pt |
| Contact line | 11 pt regular, " \| " separators | left | 2 pt |
| Section heading (PROFESSIONAL SUMMARY, PROFESSIONAL EXPERIENCE, EARLIER CAREER, EDUCATION) | 14 pt bold caps, thin 0.5 pt line under it across the full text width | left | 10 pt |
| Summary paragraph | 10.5 pt regular | justified | 6 pt after the line |
| Company line "Company (note) \| City, ST" | 12 pt bold, except the note in parentheses (e.g. "(Company closed)"), which is 12 pt regular | left | 10 pt |
| Job title | 10.5 pt bold italic | left, date on the same line | 2 pt |
| Dates "Mon YYYY – Mon YYYY" | 10.5 pt italic, not bold | right-aligned tab at the right margin | |
| Role intro | 10.5 pt regular, no indent | justified | none |
| Bullets | 10.5 pt regular | justified | none |
| Earlier career lines | 10.5 pt regular, only the title (Head of Pricing, Associate) in bold, dates in parentheses | left | none |
| Degree line | 10.5 pt bold | left | 10 pt between degrees |
| School line "School, City \| Mon YYYY" | 10.5 pt italic | left | none |
Line spacing is 1.0 (single) everywhere. Only a company with several titles under it gets dates on the company line.

## 3. Alignment
- Every ▪ bullet sits at the same spot, exactly on the left margin, in line with company names, titles and intros.
- Bullet text starts at a 0.1 in hanging indent, and every wrapped line of that bullet starts at that same 0.1 in. No line in a bullet ever starts under the ▪. The ▪ sits in its own fixed 0.1 in column, so the first line and the wrapped lines start at exactly the same point.
- Every date ends exactly on the right margin, flush with the right edge of the justified text.
- Company lines, titles, intros, headings and education all start exactly on the left margin. No leading spaces.
- The section heading lines span the same width as the text.

## 4. Extra formatting rules
1. No widow words. A bullet's last line must hold at least 4 words. If it doesn't, reword to finish a line earlier or fill it out.
2. Bullets are at most 3 lines, and role intros at most 2 lines.
3. Never split a company block across pages. A company line, its title and its first bullet stay together.
4. Same spacing before every company block, and no extra blank lines anywhere.
5. All job titles the same size, 10.5 pt.
6. Curly apostrophes and quotes everywhere.
7. Numbers as digits everywhere ("3 years", not "three years"), "%" with no space, en dash with spaces in date ranges.
8. Bold and italics only in the name, headline, headings, company lines, titles, dates, earlier career and education. Never inside a bullet.
9. Email and LinkedIn are clickable links in the PDF, with no underline or color change.
10. The PDF has real, selectable text with embedded fonts so applicant tracking systems can read it, and its document title matches the file name.

## 5. Headline and summary
- Headline is always "<Current or target title> | A, B & C", three areas from the posting that the candidate has real evidence for, in the posting's words.
- Summary is rewritten every time, 90 to 140 words, 4 to 6 sentences.
- Sentence 1 is "[Professional identity, e.g. Product leader, Backend engineer, Marketing manager] with [N]+ years [doing 3 or 4 posting areas] at [employers]." Drop an employer that is irrelevant to the posting.
- Sentences 2 to 5 take one company each ("At [Company],", "As [title] of [Company],", "Earlier,"), each with one or two real numbers picked for the posting.
- An optional closer for hands-on roles names how the candidate works day to day (for example the tools they build with), taken from `master-resume.md`.
- People-leadership roles add the management facts from `master-resume.md` (team size, reports, performance reviews).
- Education and language lines are optional. Add them only when the role values them.

## 6. What stays fixed and what moves
- Fixed, copy verbatim. Contact line, company names and notes, locations, titles, dates, EARLIER CAREER and EDUCATION, and any older role that `master-resume.md` marks as fixed.
- Semi-fixed roles keep a set number of bullets (listed in `master-resume.md`), with wording that leans toward the role.
- Flexible roles (usually the 2 or 3 most recent) each get an intro plus 3 or 4 bullets from the pool of approved bullets.
- Any bullet from the candidate's past resumes counts as approved. Always use its newest wording.

## 7. Process and delivery
- Build the PDF with the generator in `job-search/tools` in the repo (`render_resume.py` renders the resume markdown and warns about long bullets, long intros and widow words, and `verify_resume.py` checks the PDF for pages, alignment, bold dates, widow words, banned punctuation and the file name). The sample is `job-search/tools/example-resume.md`.
- Ask questions first, wait for answers, then deliver the finished resume and the cover letter together.
- Deliver the resume as a PDF attached in the thread and saved to the candidate's Downloads folder, named "[Company name] - [Role name] - <Name> - Resume - [Mon YYYY].pdf", for example "Acme - Lead PM, AI Strategy - <Name> - Resume - Oct 2026.pdf". The cover letter is never pasted in the chat. Its PDF is attached in the thread and saved to Downloads.
- With the PDF, list in a few lines what changed from the base so the candidate can check facts quickly.
- Before sending, render the PDF and check it. Exactly two pages, page 1 ends after the last flexible role, bullets and dates aligned as in section 3, no widow words, HARD STYLE RULES pass line by line, every employer, title, date and number matches the base.
