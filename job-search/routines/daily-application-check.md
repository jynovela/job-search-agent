# Routine: daily application check

- **Schedule:** once a day, 8:00 AM the candidate's time zone
- **Needs:** Gmail connector (<email>) and access to the GitHub repo your job-search repo (set in `config.md`) to push a branch and open a PR
- **Where:** the job-search Claude project, posting its message in the project

## Prompt (paste as the routine's prompt)

<task>
Keep the candidate's job application tracker current from their email, and tell them when an application moves forward.
</task>

<context>
- Tracker: `job-search/tracker.csv` in the GitHub repo your job-search repo (set in `config.md`), default branch. Follow `job-search/tracker.md`. The stage is the `Status` column, the applied date is `Applied date` (MM/DD/YYYY), and notes go in `Notes`. Address columns by header name and edit with a CSV library so quoted values stay intact.
- Dates are the candidate's time zone (set in `config.md`), never UTC.
- Active stages, in order: Researching, Applied, Recruiter screen, Hiring manager interview, Interview loop, Final round / references, Offer.
- Closing stages: Accepted, Declined, Rejected (note the stage, e.g. "Rejected (Recruiter screen)"), Withdrawn, No response.
</context>

<process>
1. Read every row whose stage is active.
2. In Gmail, search messages from the last 2 days that relate to those companies or to the applicant tracking systems they use (Greenhouse, Lever, Workday, Ashby, and similar). Search by company name, by role title, and with words like "application", "interview", "next steps", "schedule", "offer", "unfortunately".
3. For each relevant email, decide the stage it shows:
   - a request to schedule a call with a recruiter → Recruiter screen
   - a call with the hiring manager → Hiring manager interview
   - a panel, case study, or take-home → Interview loop
   - references or a final interview → Final round / references
   - an offer → Offer
   - a rejection → Rejected (with the stage)
   - a plain receipt confirmation → no change
4. Move a row only forward, never back, and only on clear evidence. When an email is ambiguous, leave the stage alone and list it under "Needs a look".
5. Write the new stage to the tracker. In the notes column, add the date, the sender, and a 5–10 word summary.
6. Mark any row still at Applied with no reply for 4 weeks since its applied date as No response.
7. **Notify the candidate with a message in the project only if** an application moved past Applied, reached Offer, or something needs a look. Keep it to one short line per company:
   "<Company>, <Role>: Applied → Recruiter screen. <Sender> wants to schedule a call (email from <date>)."
   Add any "Needs a look" items after those lines.
   Rejections and No response updates go to the tracker only, with no message.
8. If any row changed, commit `tracker.csv` to a new branch and open one PR for the candidate to approve, and include the PR link in any message you post. Never push to the default branch or merge the PR. If nothing changed, finish without committing or posting.
</process>

<constraints>
- Never reply to, archive, or label emails. Read only.
- Never commit to the default branch or merge a PR; the candidate approves every tracker change.
- Never delete tracker rows or change columns other than Status and Notes.
</constraints>
