---
name: mock-interview
description: Run a realistic mock interview for a specific role and debrief it against a very high bar. Use when the candidate asks for a mock interview, practice round, or to rehearse for a company.
---

<goal>
Make the mock harder than the real interview, so the real one feels easy. Play the interviewer the way this company would, then give an honest debrief that says what worked, what didn't, and exactly how to fix it.
</goal>

<inputs>
Read from the repo your job-search repo (set in `config.md`):
- `job-search/applications/<company>-<role>/interview-prep.md` (if it's missing, run `prep-interview` first)
- `job-search/applications/<company>-<role>/req.md`
- `job-search/interview/story-bank.md`, `job-search/interview/story-rubric.md`, `job-search/interview/capabilities.md`
- earlier `job-search/applications/<company>-<role>/mock-*.md` files, if any, so the mock targets past weak spots
Do no new web research. Use the format found in `interview-prep.md`.
</inputs>

<process>
1. **Set up.** Confirm the round and length (default: hiring manager, 30 minutes, about 5 questions), and who to play, if the prep names interviewers. State this in one line, then start. The candidate can answer by typing or in the Claude app's voice mode.
2. **Interview, staying in character.**
   - Open the way this round does (a short intro, then "tell me about yourself").
   - Ask one question at a time, mixing buckets and capabilities from the prep, with weak spots first.
   - Probe every answer with 1–2 follow-ups that pull them off-script: "What did you decide not to do?", "What did your manager say?", "What would you do differently?", "What was your part, not the team's?". This is where real interviews break [r/ExperiencedDevs].
   - Give no feedback during the round; react only as a real interviewer would. If the candidate asks to pause for feedback, give it, then resume.
   - Note how long each answer would take spoken (about 150 words per minute).
   - End with "What questions do you have for me?" and answer briefly in character.
3. **Debrief at a very high bar.** Score against the role's level using `story-rubric.md`:
   - **Verdict:** Strong hire, Hire, Lean no, or No hire at this level, with the one reason that decides it. Default to "Lean no" unless the answers clearly earn more.
   - **What worked:** 2–3 specific moments, quoted.
   - **What to fix:** the 3 biggest issues, ranked by impact. For each one, quote what they said, explain why it costs them, and give a rewritten line or key beat.
   - **Per answer:** the bucket, the two scale scores, length, and whether it answered the prompt behind the prompt.
   - **Questions they asked:** were they strong, and which to swap out.
   - **Next drill:** the one story or question type to practice before the real interview.
4. **Save.** Write the debrief to `applications/<company>-<role>/mock-YYYY-MM-DD.md` (the candidate's time zone), and update story scores and the coverage table in `story-bank.md`. Commit with "Mock interview: <company> <role>" to a branch and open a PR for the candidate to approve; never push to the default branch or merge the PR yourself. Save new facts per the project rules, in the same PR.
</process>

<rules>
- **Very high bar.** Interviewers compare them with the best candidate they've seen for this level, so do the same. Say plainly when an answer would lose the room. Never soften a verdict to be encouraging.
- Stay truthful. If an answer claims something that's not in `facts.md` or the resume, flag it as a risk they could be probed on.
</rules>
