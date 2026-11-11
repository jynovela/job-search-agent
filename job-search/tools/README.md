# PDF tools

These scripts render the candidate's resume and cover letter from markdown into their existing layout: Liberation Serif (Times New Roman metrics), US Letter. The resume follows `job-search/resume-build-rules.md`. They need `reportlab`, `pypdf`, and `pdfplumber` (`python3 -m pip install reportlab pypdf pdfplumber`).

- `render_resume.py <resume.md> <out.pdf>`: renders the resume, starts page 2 at the company set in `config.json`, and warns about anything other than 2 pages, bullets over 3 lines, intros over 2 lines, and widow words
- `verify_resume.py <out.pdf>`: checks the rendered PDF (2 pages, the page split in `config.json`, bullet and date alignment, no bold dates, widow words, banned punctuation, PDF title and file name) and prints OK or the problems
- `render_cover_letter.py <letter.md> <out.pdf>`: justifies the paragraphs and warns when the result runs over 1 page
- `example-resume.md` and `example-cover-letter.md`: a sample for a made-up candidate, the reference for the markdown format
- `config.json`: your name (used in the PDF metadata and file-name check) and the company where page 2 starts

File names:
- `<Company> - <Role> - <Name> - Resume - <Mon YYYY>.pdf`
- `<Company> - <Role> - <Name> - Cover Letter - <Mon YYYY>.pdf`
