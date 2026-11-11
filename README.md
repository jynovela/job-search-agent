# Job search agent

A job-search agent for Claude Projects. It researches companies, tailors resumes for ATS filters and hiring managers, writes cover letters, keeps an application tracker, and prepares you for interviews. Every claim it writes comes from your own source-of-truth files, and every change goes through a pull request you approve.

## How it works

The agent runs three separate actions, each with its own skills, and each action reads only the files it needs.

| Action | When | Skills |
|---|---|---|
| Research | You paste a job req or share a CSV of jobs | `research-company` |
| Build | You ask for a resume, cover letter, or "why this company" answer | `tailor-resume`, `write-cover-letter`, `humanize-writing` |
| Interview prep | You prepare for an interview or want a mock | `story-bank`, `prep-interview`, `mock-interview` |

`job-tracker-review` audits the tracker, and `routines/daily-application-check.md` is a daily routine that reads your email and moves applications forward.

## What's in `job-search/`

- `project-instructions.md`: the agent itself. Paste it into your Claude Project's instructions.
- `skills/`: the 8 skills. Upload each folder as a skill.
- `tools/`: Python scripts that render the resume and cover letter PDFs and check the resume layout (2 pages, aligned dates, no widow words, banned punctuation). Set your name in `tools/config.json`.
- `resume-build-rules.md`, `writing-check.md`, `tracker.md`: the rules for layout, writing quality, and tracking.
- `interview/`: general guides to the capabilities PM interviews test, story types, a story rubric, and a product sense guide, plus a blank story bank.
- Templates you fill in: `config.md`, `master-resume.md`, `facts.md`, `voice.md`, `personal-stories.md`, and `tracker.csv`.
- `companies/` and `applications/`: empty. The agent fills them as you apply.

## Setup

1. Copy this repo into a **private** repo of your own. Your filled-in files hold personal details, so keep them out of public view.
2. Fill in `config.md`, `tools/config.json`, `master-resume.md`, and `facts.md`. The richer the master resume, the better the tailoring.
3. Create a Claude Project, paste `project-instructions.md` into its instructions, add your repo, and upload the skills.
4. Optional: connect Gmail and install the daily routine.
5. Install the PDF dependencies with `python3 -m pip install reportlab pypdf pdfplumber`. The renderer uses Liberation Serif, which has the same letter widths as Times New Roman.

Try the tools on the samples (a made-up candidate):

```
cd job-search
python3 tools/render_resume.py tools/example-resume.md "Example Corp - Principal PM - Alex Rivera - Resume - Nov 2026.pdf"
python3 tools/verify_resume.py "Example Corp - Principal PM - Alex Rivera - Resume - Nov 2026.pdf"
```

## Ground rules the agent follows

- Never invent or inflate. Every employer, title, date, number, and skill comes from your files or from you in the conversation. Missing numbers become visible placeholders.
- It saves what you teach it. Answers and corrections go back into `facts.md`, `master-resume.md`, `voice.md`, or `personal-stories.md`, so each application improves on the last.
- It works through pull requests. It never pushes to the default branch and never merges.
