---
name: tailor-resume
description: Tailor the candidate's resume to a specific job req and render it as a PDF. Use in the Build action when the candidate asks for a resume for a role whose research and req are saved.
---

<goal>
Tailoring is advertising, not reinvention. The candidate stays the same person: the job is to make the parts of their real experience that matter to this role easy to find in a few seconds, for both the ATS and a recruiter skimming the top third of the page.
</goal>

<inputs>
Read from the repo your job-search repo (set in `config.md`):
- `job-search/resume-build-rules.md`, the candidate's approved layout, structure, and delivery rules, which override this skill wherever they differ
- `job-search/master-resume.md`, the pool of bullets
- `job-search/facts.md`, which overrides any wording in the master
- `job-search/applications/<company>-<role>/req.md` and `job-search/companies/<slug>.md`, both saved by the Research action. Do no web research here.
- `job-search/writing-check.md`, for step 6
- `job-search/tools/render_resume.py`, `tools/verify_resume.py`, and `tools/example-resume.md`, which show the exact markdown format the renderer expects
</inputs>

<process>
1. **Analyze the req.** Read it in order of weight: qualifications, then responsibilities, then the overview. Write down:
   - the core problem the role solves, and the top 3 needs (items listed first or repeated matter most)
   - the 10–15 ATS keywords: the exact job title, hard skills, tools, methods, domain terms, and acronyms, in the posting's own spelling
2. **Build a match map.** Pair each need with the candidate's best evidence from the master, using bullet IDs such as `ACME-EVAL`. Mark each as strong, partial (reframe it honestly in the posting's terms), or gap. A gap is never filled with an inflated claim; flag it for the cover letter if the candidate asked for one.
3. **Ask clarifying questions, once, and wait.** Gather everything you need in one short message: missing numbers, whether the candidate has a skill the req asks for that isn't in the files, and anything the match map left unclear. Wait for their answers before drafting, then deliver the resume (and the cover letter, if they asked for one). Save each answer right away, per the project rules. If nothing is unclear, skip this step and say so.
4. **Write the resume** as markdown in the renderer's format:
   - **Headline:** "<Current or target title> | A, B & C", three areas from the posting that the candidate has real evidence for, in the posting's words. Keep their real titles everywhere else.
   - **Summary:** rewrite it for every req, 90 to 140 words in 4 to 6 sentences, following section 5 of `resume-build-rules.md` (the fixed opening sentence, then one company per sentence with one or two real numbers picked for the posting).
   - **Experience:** follow section 6 of `resume-build-rules.md`. Flexible roles each get an intro plus 3 or 4 bullets from the approved pool, with the bullets that match the req first. Fixed roles, Earlier Career, and Education are copied verbatim. Semi-fixed roles keep their set number of bullets, with wording leaning toward the role. Start from each bullet's newest approved wording, and reword it in the posting's terms only where that describes the same work truthfully.
   - **Bullet shape:** action verb + what + result. Vary the verbs and shapes, use past tense for past roles and present tense for a current role. Bullets are at most 3 lines and intros at most 2, and a bullet's last line holds at least 4 words. No bold or italics inside bullets.
   - **No Skills section.** Every priority keyword appears in context in the summary or the bullets; the most important ones appear twice, none more than 3 times.
   - **Earlier career and education:** one line each, unless the req values them (pricing, consulting, ML teaching).
   - **Length:** exactly 2 pages. Page 2 starts with the company set in `tools/config.json`. If page 1 overflows, cut a flexible-role bullet before cutting the summary.
5. **Keyword check.** List the top keywords and where each one appears. Add any that are missing and that the candidate really has; list the rest as gaps.
6. **Writing check.** Run `writing-check.md` and fix everything it finds.
7. **Render and verify.** Run `python3 job-search/tools/render_resume.py resume.md "<Company> - <Role> - <Name> - Resume - <Mon YYYY>.pdf"`, then `python3 job-search/tools/verify_resume.py` on the PDF (install `reportlab`, `pypdf`, and `pdfplumber` with pip if missing). Fix every warning, usually by rewording a bullet to remove a widow word or a fourth line, and render again until the check prints OK. Look at both pages as images and confirm them against section 7 of `resume-build-rules.md`.
8. **Keep the markdown.** The final resume markdown becomes `job-search/applications/<company>-<role>/resume.md` in the repo; the Build action adds it to the execution's PR and links it from the tracker.
9. **Report to the candidate** with the PDF attached and a few lines listing what changed from the base (headline, summary, which bullets lead and why) so they can check facts quickly, plus the keyword gaps and the writing-check result. Continue to `write-cover-letter` only if the candidate asked for a cover letter or "why" answer in this request.
</process>

<self_review>
Before showing the resume, confirm:
- nothing is invented, official titles are unchanged, and placeholders are flagged
- every employer, title, date, and number matches the master, and the fixed blocks are verbatim
- `facts.md` was respected (a correction there always beats older wording in the master)
- the summary was rewritten for this req, with the title or a bridge headline, keywords, and 1–2 numbers
- the recruiter six-second test passes: the top third shows the title fit, the top skills, and the best result
</self_review>
