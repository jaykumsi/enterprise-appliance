# Domain workbooks (AmeriMed-style pages for every domain)

Builds one student workbook page per domain (16 topics × 10 Beginner / 10 Intermediate / 10 Advanced = 480 questions)
from the AmeriMed healthcare workbook, plus a hub page that links all nine.

| Domain | Company | Page |
|---|---|---|
| hub | SQL Assignments by Domain | https://claude.ai/artifact/TThNAbyikVuhdmT9KgZDMU |
| healthcare | AmeriMed Healthcare (original) | https://claude.ai/artifact/CXX9mdkQoRXVCDQVVXe8LZ |
| banking | Harborstone Bank | https://claude.ai/artifact/V3aRGRAaw6dZPsoT4RiXJf |
| brokerage | Ridgeline Securities | https://claude.ai/artifact/3uNmMizam1Vx6vNQ1sQUT2 |
| oil | Permian Ridge Energy | https://claude.ai/artifact/LWKJBtBDDJUdvUzjxmYEhs |
| pharma | Novacrest Pharmaceuticals | https://claude.ai/artifact/M9fGeCrvKo739tG6oLcpuN |
| retail | Maple & Main Stores | https://claude.ai/artifact/WnQYTiNXBhEtzEWhLrFUSe |
| retail_inventory | Maple & Main Merchandising | https://claude.ai/artifact/JtGcBZek4mp5qh7BJPLizG |
| retail_logistics | Maple & Main Distribution | https://claude.ai/artifact/JKUzw82CbPnQmzD8VoAXjQ |
| retail_manufacturing | Maple & Main Private Label | https://claude.ai/artifact/HdfHkXQGFWkMkC1mbpKv6v |

## How it is built

1. `build_items.py <domain>`: translates each AmeriMed item (from `../consolidated_supplements.json`) into the domain's
   tables, columns and nouns (`translate.py`, config in `wb_domains.py`), runs every answer on a disposable LocalDB copy
   `WB_<domain>` loaded from `../domains/<domain>/data_setup.sql` (each item in a rolled-back transaction; the database is
   reloaded if anything changes), and writes `items/<domain>.json`. That file holds the answer SQL: keep it private.
2. Questions that need a table the domain lacks (AmeriMed's Doctors, Medications, Prescriptions, or the parent links that
   only healthcare fills) use a replacement written once in `fallback_hc*.py` with the same topic, level and skill.
   A translated question that errors or comes back unexpectedly empty is retried with its replacement.
3. `render_pages.py --hub <hub url> <domain>...`: builds `pages/<domain>.html` from `template/amerimed_page.html`
   (student mode: expected results only, no answer SQL).
4. `render_hub.py pages/links.json`: builds `pages/hub.html`.

Rebuild everything: `python build_items.py <domains>` then the two render steps, then republish the pages.
The `WB_<domain>` LocalDB databases are scratch copies created by `runner.reload()`; they can be dropped at any time.
