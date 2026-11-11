---
name: prep-interview
description: Build the candidate's prep pack for a specific interview, covering the capabilities the req and company values test, the company's known interview format, story mapping, and their questions to ask. Use when the candidate has an interview scheduled or asks to prepare for a specific role.
---

<goal>
One file, `job-search/applications/<company>-<role>/interview-prep.md`, that tells the candidate what this interview will test, how it is likely to run, which story answers each question, and where they are exposed.
</goal>

<inputs>
Read from the repo your job-search repo (set in `config.md`):
- `job-search/applications/<company>-<role>/req.md` and `job-search/companies/<slug>.md` (if they're missing, run the Research action for this role first)
- the capabilities file named in `job-search/config.md`, `job-search/interview/story-types.md`, `job-search/interview/story-bank.md`
- `job-search/applications/<company>-<role>/resume.md` if it exists, else `job-search/master-resume.md`, plus `job-search/facts.md`
</inputs>

<process>
0. **Check the capabilities file.** Read the file named in `config.md`. If it is missing or doesn't match this role's family (for example the req is for an engineering role and the file is for product managers), tell the candidate and offer to create `interview/<role>-capabilities.md` in the same shape as `interview/product-manager-capabilities.md`: capabilities by level and the rounds they show up in, each with a cited source. Save it in the same PR.
1. **Confirm the round.** Ask the candidate in one message which round this is (recruiter, hiring manager, loop, or final) and the interviewers' names, if known. Continue with what they give.
2. **Map the capabilities.** From the req's qualifications and responsibilities, plus the company's values, pick the 3–5 capabilities this role tests most. Use the capabilities file's terms for each, quote the req or value line it comes from, and say what kind of answer it needs (scale, scrappy vs. structured, technical depth).
3. **Research the format.** This is the one place outside Research where web search is allowed (the candidate, 2026-10-18), and only for interview format and prep:
   - the company's own interview guide or careers pages (e.g. Amazon Leadership Principles, writing exercises)
   - Glassdoor, Blind, or Reddit reports of interview rounds for this kind of role and question themes at this company, in the last two years
   - the interviewers' public LinkedIn profiles and posts, if the candidate gave names, to learn their background and what they care about
   Cite each finding's URL and say how many reports back it up. When nothing reliable turns up, say so and use the common round types in the capabilities file.
4. **Predict the questions.** List 10–15 likely questions across the capabilities and format, each tagged with its bucket from `story-types.md`.
5. **Map the stories.** For each capability and predicted question, name the primary and backup story from `story-bank.md` and the angle to use. Mark each gap: no story, or a story scoring below 4 at this level.
6. **Draft the ready answers for this company:**
   - "Tell me about yourself": 60–90 seconds of key beats, ending with why this role.
   - Values fit: one story linked to one named company value.
   - "Why this company / why now": reuse `why.md` if it exists.
7. **Write their questions to ask.** Write 10 questions tied to the team's priorities, challenges, and the interviewers' backgrounds, not ones the website answers.
8. **Save** `interview-prep.md`, commit with "Interview prep: <company> <role>" to a branch, and open a PR for the candidate to approve. Never push to the default branch or merge the PR yourself.
9. **Report to the candidate.** Send a short summary covering the format, the top 3 capabilities, and the gaps, with a link to the file. If there are gaps, offer to fill them with `story-bank` before running a mock with `mock-interview`.
</process>

<rules>
- Ground every claim about the company or its format in a cited source. Mark anything unverified as unverified.
- Never invent facts about the candidate. Stories come from the bank and facts come from `facts.md` and the resume.
</rules>
