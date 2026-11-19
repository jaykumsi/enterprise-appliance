# Domain workbooks (AmeriMed-style pages for every domain)

Builds one student workbook page per domain (16 topics × 10 Beginner / 10 Intermediate / 10 Advanced = 480 questions)
from the AmeriMed healthcare workbook, plus a hub page that links all nine.

| Domain | Company | Student workbook (share with students) | Instructor answer key (PRIVATE) |
|---|---|---|---|
| hub | SQL Assignments by Domain | https://claude.ai/artifact/TThNAbyikVuhdmT9KgZDMU | (none: the hub never links answer keys) |
| healthcare | AmeriMed Healthcare | https://claude.ai/artifact/CXX9mdkQoRXVCDQVVXe8LZ | https://claude.ai/artifact/5SZGPX2UFKzjskMMEupYSG |
| banking | Harborstone Bank | https://claude.ai/artifact/V3aRGRAaw6dZPsoT4RiXJf | https://claude.ai/artifact/QJPfAnuK6yL18xrP6He9u1 |
| brokerage | Ridgeline Securities | https://claude.ai/artifact/3uNmMizam1Vx6vNQ1sQUT2 | https://claude.ai/artifact/DRGrRnFqoEiiq5fePDiFz1 |
| pharma | Novacrest Pharmaceuticals | https://claude.ai/artifact/M9fGeCrvKo739tG6oLcpuN | https://claude.ai/artifact/5rTwciovgjoapuTmk7Dg18 |
| oil | Permian Ridge Energy | https://claude.ai/artifact/LWKJBtBDDJUdvUzjxmYEhs | https://claude.ai/artifact/ERyMjdnq8oKyh8Y1hYzzNY |
| ecommerce | Everyday Bazaar | https://claude.ai/artifact/6CFXh4beobRHibannRFYqu | https://claude.ai/artifact/NrsQtWJFeQmdQZ5GShEaaN |
| retail | Maple & Main Stores | https://claude.ai/artifact/WnQYTiNXBhEtzEWhLrFUSe | https://claude.ai/artifact/Wn92vMFWQHH9fmWJBrRVPt |
| retail_supply_chain | Maple & Main Supply Chain | https://claude.ai/artifact/JtGcBZek4mp5qh7BJPLizG | https://claude.ai/artifact/Eim1cYkgTm7qsYqV7tXXQF |
| retail_logistics | Maple & Main Distribution | https://claude.ai/artifact/JKUzw82CbPnQmzD8VoAXjQ | https://claude.ai/artifact/MftThQnGGDgvZGLg3b1iBd |

Retired from the hub and menus (2026-11-18): retail_inventory and retail_manufacturing were merged into retail_supply_chain,
which reuses the Merchandising page URLs. The old Private Label pages (student and instructor) were deleted.

**Data source.** retail_supply_chain and ecommerce are full domains of the `domains/` curriculum (models in
`../domain_projects.py`, large data in `../large_data_extra.py`); every workbook loads `domains/<company>/sql/data_setup.sql` (see `../company_paths.py`).
Everyday Bazaar's test-ID and STRING_AGG fixes for the large data live in `overrides/ecommerce.json`.
Loading WB_ecommerce takes about a minute.

## How it is built

1. `build_items.py <domain>`: translates each AmeriMed item (from `../consolidated_supplements.json`) into the domain's
   tables, columns and nouns (`translate.py`, config in `wb_domains.py`), runs every answer on a disposable LocalDB copy
   `WB_<domain>` loaded from `domains/<company>/sql/data_setup.sql` (see `../company_paths.py`) (each item in a rolled-back transaction; the database is
   reloaded if anything changes), and writes `items/<domain>.json`. That file holds the answer SQL: keep it private.
2. Questions that need a table the domain lacks (AmeriMed's Doctors, Medications, Prescriptions, or the parent links that
   only healthcare fills) use a replacement written once in `fallback_hc*.py` with the same topic, level and skill.
   A translated question that errors or comes back unexpectedly empty is retried with its replacement.
3. `render_pages.py --hub <hub url> <domain>...`: builds `pages/<domain>.html` from `template/amerimed_page.html`
   (student mode: expected results only, no answer SQL).
4. `render_hub.py pages/links.json`: builds `pages/hub.html`.

**Interview Challenges (17th topic, 10 per domain).** `challenges.py` holds the questions, answer SQL and approach hints
(shared patterns such as month-to-date, Pareto, gaps and islands, cohorts and NTILE tiers, plus domain-specific ones).
`build_challenges.py <domains>` runs them on `WB_<domain>` and writes `items/<domain>_challenges.json` (private: answer
SQL). `render_pages.py` appends the topic with a "Challenge" level; the hint is shown together with the expected result.
`render_pages.py healthcare` rebuilds the AmeriMed page from the template, adding only this topic.

**Instructor solution guides (PRIVATE, never link from the hub or share with students).** `render_instructor.py <domains>`
turns each rendered student page into `pages/<domain>_instructor.html`: same page in instructor mode, every question with
its answer SQL, how it works and expected result (written questions get a model answer; the few design answers that do
not translate from AmeriMed are hand-written in `written_answers.py`, which also fixes their question wording).

The instructor answer-key links are in the table at the top of this file.

**Header and footer.** `site_chrome.py` puts the hub's Tinitiate AI header (charcoal bar, Workbooks menu) and black
footer on every workbook page; `render_pages.py` and `render_instructor.py` both call it. The student menu reads
`pages/links.json`; the instructor menu reads `pages/instructor_links.json` (instructor pages only, never student pages).

Rebuild everything: `python build_items.py <domains>` then the two render steps, then republish the pages.
The `WB_<domain>` LocalDB databases are scratch copies created by `runner.reload()`; they can be dropped at any time.
