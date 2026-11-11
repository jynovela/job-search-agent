---
name: write-cover-letter
description: Write the candidate's cover letter, their short "why this company" answer, or both, for a specific job req, and render the letter as a PDF. Use in the Build action when the candidate asks for a cover letter or a "why do you want to work here" answer.
---

<goal>
Make only what the candidate asked for: the letter, the "why" answer, or both. Skip the steps for a piece they didn't request.

The letter answers the hiring manager's unspoken question: "Why should we consider this person for this role?" The resume lists the evidence; the letter tells the story behind 2–3 pieces of it, ties them to this company's needs, and sounds like the candidate. Clarity beats cleverness.
</goal>

<inputs>
Read from the repo your job-search repo (set in `config.md`):
- `job-search/voice.md`, before writing a word
- `job-search/applications/<company>-<role>/req.md` and `job-search/companies/<slug>.md`, both saved by the Research action. Do no web research here.
- `job-search/personal-stories.md`
- `job-search/facts.md`, plus the tailored resume: from this request, else `applications/<company>-<role>/resume.md`, else `master-resume.md`
- `job-search/writing-check.md`, for step 5
- `job-search/tools/example-cover-letter.md`, which shows the renderer's format
</inputs>

<process>
1. **Plan.** From the req and the research, name the employer's top 2–3 needs and pick 2–3 of the candidate's results that match them. Find one real hook in the saved research or the req: the mission, a value, or what the team is building, that connects to the candidate.
2. **Find the personal angle.** Look in `personal-stories.md` for a story tagged with this company's themes. If none fits, ask the candidate **one** light question tied to this company, for example: "Have you used <product>?", "What drew you to this posting?", or "Anything about <their mission or news> that connects to you?" Save their answer to `personal-stories.md` with a date and tags. If they skip it, anchor the interest in the role and the team instead.
3. **Write the letter**, one page and 3–5 paragraphs, about 250–400 words in the body:
   - **Format (the candidate's rules):** today's date in full at the top, in the candidate's time zone ("October 14, 2026"). No header block with their contact details. No recipient block. Open with "Dear <Company> Hiring Team,". Sign off with "Sincerely," then "<Full Name>" and then "<email> | <phone>" on separate lines.
   - **Opening:** name the role by its title only, with no req number and no source, then give the personal hook and why this role. The hook must be one of: (a) a personal user story if the candidate has used their product, (b) a genuine belief shaped by their experience if not a consumer product, or (c) a specific company detail — product name, feature, recent event, or company metric.
   - **Evidence (1–2 paragraphs):** expand on 2–3 results with context the resume can't give: challenge, what they did, result, and why it matters here. **Order by relevance to this posting, not chronology.** Don't restate the resume line by line. **Each letter's evidence section must differ from other letters for the same candidate** — pick the achievements that best match this posting's stated requirements, not the same 2-3 bullets every time.
   - **Value paragraph (required):** "From the posting, <Company> wants [what they need]". Then offer exactly **three** ideas as possibilities:
     - "One possibility is [specific, actionable thing related to their workflow or product area]"
     - "Another is [another specific thing]"
     - "It might help to [additional suggestion]"
     All ideas must reference real company context — specific products, workflows, metrics, or team structures from the posting or company research. **Never name their past companies in this paragraph.** Only acknowledge a gap if there's a real gap and it is critical to the role. Make it one plain sentence and don't emphasize it.
   - **Close:** end with a specific sentence about why this work excites them (not repeating the company's mission — be personal), then "Thank you for your time and consideration."
   - Never ask the candidate for the hiring manager's name, the posting source, or a req number.
4. **Write the "why this company" answer:** 100–150 words for an application form field. Use first person, put the company-specific reason first, then the fit with their experience, in plain words. Reuse the hook from the letter, but don't copy its sentences.
5. **Writing check.** Run `writing-check.md` on both texts and fix everything it finds.
6. **Render** with `python3 job-search/tools/render_cover_letter.py letter.md "<Company> - <Role> - <Name> - Cover Letter - <Mon YYYY>.pdf"`. Body paragraphs are justified. It must be 1 page, and if the script warns otherwise, cut.
7. **Keep the markdown.** The final letter markdown becomes `job-search/applications/<company>-<role>/cover-letter.md` and the "why" answer `why.md`; the Build action adds them to the execution's PR and links the letter from the tracker.
8. **Show the candidate** the "why" answer in full and attach the letter's PDF (never paste the letter text in chat), plus one line of writing-check results. Then return to the Build action for delivery and tracking.
</process>
