# Application tracker

<purpose>
Defines how applications are tracked, so every action sets stages the same way. Read this before adding or updating a row in the tracker.
</purpose>

- File: `job-search/tracker.csv` in this repo. The default branch holds the approved version; changes reach it only through a PR the candidate merges. One row per application.
- Headers (keep them exactly as written):

| Header | What goes in it |
|---|---|
| `Company` | Company name |
| `Role` | Role title, as the req writes it |
| `Source` | Where the req came from (for example LinkedIn, referral, company site) |
| `Link` | The req's URL, blank if there is none |
| `Applied date` | Applied date, `MM/DD/YYYY`, the candidate's time zone |
| `Status` | The stage (see Stages) |
| `Req` | GitHub link to the saved `req.md` copy of the job req, blank if none is saved |
| `Resume` | GitHub link to the application's `resume.md`, blank if none |
| `Cover Letter` | GitHub link to the application's `cover-letter.md`, blank if none |
| `Reached out to recruiter` | Yes or No |
| `Notes` | Free text: evidence for stage changes, location, pay, and similar |

## Adding or updating a row
- Edit the file with a CSV library (Python `csv` with `newline=''`), not by hand, so values with commas or line breaks stay quoted. A role like `Director, Product Management` must be in quotes or it breaks the row.
- Address columns by header name, never by position.
- Before adding a row, look for an existing row with the same company and role (or the same req link). Update that row instead of adding a duplicate.
- New rows go at the end of the file. Never delete rows or reorder them.
- **Required check before every commit that touches `tracker.csv`**, including merge commits and conflict fixes. Run this from the repo root and commit only if it prints `OK`:

  ```
  python3 -c "import csv,sys; r=list(csv.reader(open('job-search/tracker.csv',newline='',encoding='utf-8'))); bad=[(i+1,len(x),x[0]) for i,x in enumerate(r) if len(x)!=len(r[0])]; print('OK' if not bad else bad); sys.exit(1 if bad else 0)"
  ```

  If it lists rows, each one has a comma or quote that isn't escaped. Fix those rows with the CSV library and run the check again. GitHub only shows the file as a table when every row has the same number of columns as the header.
- Put the `tracker.csv` change in the same PR as the application files it links to. Never push it to the default branch directly.

## Stages
Active, in order:
1. **Researching**: req received, not applied yet
2. **Applied**
3. **Recruiter screen**
4. **Hiring manager interview**
5. **Interview loop**: panel, case study, or take-home
6. **Final round / references**
7. **Offer**

Closing:
- **Accepted**, **Declined**
- **Rejected**: note the stage where it happened, for example "Rejected (Recruiter screen)"
- **Withdrawn**: The candidate pulled out
- **No response**: Applied with no reply after 4 weeks

Older rows may also use **Not Available** (posting closed), **Not Applying**, **Already Applied**, and **Pending Application**. Leave those as they are; use the stages above for new changes.

## Rules
- The Research action never touches the tracker. The Build action adds a row (or updates the role's existing row) with stage **Applied** as soon as the PDFs are saved and the application files are on GitHub. Fill in company, role, source, the req link if there is one, and the date.
- **Req**, **Resume**, and **Cover Letter** hold links to the application's markdown files on GitHub, in this form (`HEAD` always points at the default branch):
  - Req: `https://github.com/<owner>/<repo>/blob/HEAD/job-search/applications/<company>-<role>/req.md`
  - Resume: `https://github.com/<owner>/<repo>/blob/HEAD/job-search/applications/<company>-<role>/resume.md`
  - Cover Letter: `https://github.com/<owner>/<repo>/blob/HEAD/job-search/applications/<company>-<role>/cover-letter.md`
- Only move a stage forward based on evidence: an email, or the candidate saying so. Note the evidence (sender and date) in the row's Notes.
