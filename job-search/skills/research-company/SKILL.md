---
name: research-company
description: Save a company's mission and values and one job req to GitHub, for one CSV row or one pasted req. Use for the Research action when the candidate shares a job list or pastes a req; it never builds a resume or letter.
---

<goal>
Save the two things the Build action needs for one role, and nothing more: the company's mission and values in `job-search/companies/<slug>.md`, and the req in `job-search/applications/<company>-<role>/req.md`. One execution handles one CSV row or one pasted req. Read no other files in `job-search/`.
</goal>

<process>
1. **Check for saved research.** Derive a slug from the company name (lowercase, hyphens: `acme-corp`) and look for `job-search/companies/<slug>.md` in the repo.
   - If it exists, check whether it has all the sections from the template: "Mission, Culture, and values", "General company info", "Products", and "Recent News". If any section is missing or thin, do step 2 to fill it in.
   - If the file doesn't exist, do step 2.
2. **Company Research** Make one lookup of the company's own mission, values, about, or careers page. After you are done, expand the research to get a better context for the company: news, funding, products, competitors, or culture. Record the source URL, and skip anything you can't confirm.
3. **Save the req.** Write `job-search/applications/<company>-<role>/req.md` (short role slug, e.g. `acme-activation-platform`) from the text the candidate pasted, or from the row's link. Include the link, location, pay if listed, date received (today, in the candidate's time zone), and the posting's About, Responsibilities, and Qualifications. If the req can't be read or the role looks closed, don't guess: report it as skipped and stop.
4. **Add the req to the company file.** Under **Reqs**, add one entry: role title, date, link, and 2–3 lines on what this team needs, based on the req only.
5. **Save.** Keep the company file under about 4 KB: summarize, never paste web pages. Commit with the message "Research <company>: <role>" to a branch and open a PR for the candidate to approve. Never push to the default branch or merge the PR yourself.
6. **Report** one line: done, already saved, or skipped and why. Don't continue to any other skill.
</process>

<template>
```markdown
# <Company>
researched: YYYY-MM-DD

## Mission, Culture, and values
Their own words where short; link the source.

## General company info
Funding, competitors, industry, size

## Products
Core offerings, Target Audience, Product Market Fit, Top Competitors

## Recent News
Most relevant events; link to source.

## Reqs
- <Role> (YYYY-MM-DD, link): what this team needs, in 2–3 lines.

## Sources
- URLs
```
</template>
