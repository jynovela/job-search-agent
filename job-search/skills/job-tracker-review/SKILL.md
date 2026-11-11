---
name: job-tracker-review
description: Review and fix job tracker CSV entries and application files. Use when reviewing tracker quality, fixing data issues, or doing a systematic audit of entries.
---

<goal>
Audit a range of tracker entries for critical data issues, fix them, and open a PR. Cover: fake links, missing cover-letter.md files, req title format mismatches, and CSV column alignment.
</goal>

<process>
1. **Identify the entry range.** Get line numbers via `grep` on the company names or issue descriptions. CSV lines are pipe-delimited with an auto-numbered first column; the entry number is the line index (row 1 = header, so entry N is at line N+1).

2. **Check for critical issues** in this priority order:
   a. **Fake/placeholder links** — grep for `abc123`, `placeholder`, or clearly invalid URLs in the Link column (column D). Replace with the actual source URL from the company research or req.md.
   b. **Missing cover-letter.md files** — check each application directory for `cover-letter.md`. If the Cover Letter column (column I) is empty, create the file. Look at an existing cover letter for format reference: short letter, 3-5 paragraphs, evidence from the candidate's most relevant roles, closes with interest in the company.
   c. **Req title format mismatches** — the standard format is `Company — Role` (Company first, em dash `—`, then role title). Check req files with `head -1`. Fix files that use `Role — Company` or other inverted formats.
   d. **CSV column alignment** — entries with notes sometimes have different comma patterns. Pattern `,,No,` means: empty cover letter, reached-out="No", empty notes. Pattern `,,,text` means: empty cover letter, empty reached-out, notes start with text. Be careful when patching.

3. **Fix the tracker CSV.** Use `patch` with exact line content from `sed -n "Np"` to get the precise string. For missing cover letters, insert the GitHub blob link into column I (after resume, before Reached out). For fake links, replace the URL in column D.

4. **Create missing cover-letter.md files** in each application directory. Use the same format: open with interest + relevant experience, 2-3 evidence paragraphs, connection to company, close with specific interest question. Adapt evidence to the specific role's domain (fintech payments, AI platforms, compliance, etc.).

5. **Fix req title formats.** Change `Role — Company` to `Company — Role` in each affected req.md first line.

6. **Create PR.** `git checkout -b fix/tracker-critical-issues`, stage all changes, commit with a descriptive message, push, and create a PR to the active branch (usually `claude/project-thread-<id>`). Title: "Fix tracker critical issues: fake link, missing cover letters, req title format".

</process>

<pitfalls>
- **CSV patching requires exact content.** Always use `terminal(command='sed -n "Np"')` to get the precise line string before calling patch. A single extra comma or whitespace difference causes the fuzzy match to fail.
- **Cover letter column has variable trailing format.** Entries ending with `,,No,` (empty notes) differ from entries ending with `,,,text` (notes present, empty reached-out). The cover letter link goes in the empty field before the `No` or before the double-comma-empty.
- **Fake links are not always obvious.** Check for `abc123`, shortcodes that don't look like real job IDs, or URLs that redirect to landing pages instead of the actual posting.
- **Cover letter content must match the role's domain.** Don't paste the same evidence verbatim every time. Adapt which project details are emphasized to the company's actual product area (payments, compliance, AI platform, billing, etc.).
- **Req title format is `Company — Role`, not `Company - Role`.** Use the em dash `—` (U+2014), not the hyphen `-`.
</pitfalls>
