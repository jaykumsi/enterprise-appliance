"""Instructor solution guides: the student page for each domain with every answer filled in.

Reads the rendered student page pages/<domain>.html, replaces each question's expected result with the full answer
(answer SQL, how it works, expected result; or the model answer for written questions) and switches the page script to
instructor mode ("Show answer" buttons and an "All answers" toggle). Run render_pages.py first.

Usage: python render_instructor.py <domain> [...]
Output: pages/<domain>_instructor.html   (PRIVATE: contains every answer; never link it from the hub or student pages)
"""
import json
import re
import sys
from pathlib import Path

import runner
import site_chrome
from build_items import samples
from translate import Translator
from written_answers import A as DOMAIN_A

HERE = Path(__file__).resolve().parent
HC = {x['id']: x for x in json.loads((runner.ROOT / 'consolidated_supplements.json').read_text(encoding='utf-8'))['healthcare']}

# Written questions whose domain replacement (fallback_hc*.py) has no AmeriMed answer to translate.
WRITTEN = {
    'INTRODUCTION-B08': (
        'In a many-to-many relationship one row on each side can link to many rows on the other side, so neither table '
        'can hold the other\'s key in a single column. You add a third table (a junction or bridge table) whose rows are '
        'pairs of keys. Here you would create a Staff table and a junction table such as EncounterStaff(EncounterID, '
        'StaffID, Role) with a foreign key to each side and a composite primary key (EncounterID, StaffID), so one '
        'encounter can involve several staff members and one staff member can work on many encounters.'),
}

BANNER = ('<div style="background:#7c3aed;color:#fff;text-align:center;padding:10px 16px;font:700 14px/1.4 system-ui,sans-serif;'
          'letter-spacing:.06em;text-transform:uppercase">Instructor edition &bull; answer key with every solution &bull; '
          'do not share with students</div>')
BADGE = ('<span style="margin-left:8px;padding:2px 8px;border-radius:6px;background:#7c3aed;color:#fff;font-size:.68rem;'
         'font-weight:800;letter-spacing:.08em;vertical-align:middle">INSTRUCTOR</span>')


def written(slug, tr, qid):
    if qid in DOMAIN_A.get(slug, {}):
        return '**Model answer:** ' + DOMAIN_A[slug][qid]
    if qid in WRITTEN:
        text = WRITTEN[qid]
    else:
        src = HC.get(qid, {}).get('answer') or ''
        m = re.search(r'\*\*Answer:\*\*\s*(.*)', src, re.S)
        text = m.group(1).strip() if m else ''
    if not text:
        return None
    return '**Model answer:** ' + (text if tr is None else tr.text(text))


def domain_answers(slug):
    tr = None
    if slug != 'healthcare':
        tr = Translator(slug)
        tr.set_samples(samples(runner.Session(slug), slug, tr))
    out = {}
    if slug == 'healthcare':
        for qid, x in HC.items():
            a = re.sub(r'^\*\*Question:\*\*.*?\n\n', '', x['answer'] or '', count=1, flags=re.S).strip()
            out[qid] = re.sub(r'^\*\*Answer:\*\*', '**Model answer:**', a) if a else None
    else:
        for it in json.loads((HERE / 'items' / f'{slug}.json').read_text(encoding='utf-8')):
            if it['sql']:
                parts = [f"```sql\n{it['sql'].strip()}\n```"]
                if it.get('how'):
                    parts.append('**How it works:** ' + it['how'])
                if it.get('a'):
                    parts.append(it['a'])
                out[it['id']] = '\n\n'.join(parts)
            else:
                out[it['id']] = written(slug, tr, it['id'])
    for it in json.loads((HERE / 'items' / f'{slug}_challenges.json').read_text(encoding='utf-8')):
        out[it['id']] = f"```sql\n{it['sql'].strip()}\n```\n\n{it['a']}"
    return out


def render(slug):
    s = (HERE / 'pages' / f'{slug}.html').read_text(encoding='utf-8')
    m = re.search(r'^const DATA = (\[.*\]);$', s, re.M)
    data = json.loads(m.group(1))
    answers = domain_answers(slug)
    missing = []
    for t in data:
        for it in t['items']:
            a = answers.get(it['id'])
            if not a:
                missing.append(it['id'])
            it['a'] = a
    js = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    s = s[:m.start()] + 'const DATA = ' + js + ';' + s[m.end():]

    def rep(old, new):
        nonlocal s
        assert old in s, old[:80]
        s = s.replace(old, new, 1)
    rep('const MODE = "student";', 'const MODE = "instructor";')
    s = re.sub(r'<title>(.*?) SQL Assignments</title>', r'<title>\1 Instructor Key</title>', s, count=1)
    s = s.replace('<title>Healthcare Instructor Key</title>', '<title>AmeriMed Healthcare Instructor Key</title>', 1)
    # same Tinitiate AI header/footer as the hub, in its instructor variant (menu lists the other answer keys)
    s = site_chrome.apply(s, slug, instructor=True)
    i = s.index('<!--tn-header-->')
    s = s[:i] + BANNER + s[i:]
    s = re.sub(r'(<span class="eyebrow">.*?</svg>)Tinitiate AI Academy &bull; ', r'\1Instructor Answer Key &bull; ', s, count=1)
    rep('<h1>From First SELECT to Interview-Ready<br>', '<h1>Instructor Answer Key<br>')
    out = HERE / 'pages' / f'{slug}_instructor.html'
    out.write_text(s, encoding='utf-8')
    total = sum(len(t['items']) for t in data)
    return out, total, missing


if __name__ == '__main__':
    for d in sys.argv[1:]:
        p, n, miss = render(d)
        print(d, n, 'items', p.stat().st_size // 1024, 'KB', 'MISSING:' if miss else '', miss[:20])
