"""Render one AmeriMed-style student page per domain from items/<domain>.json.

The AmeriMed page (template/amerimed_page.html) is the design source: same layout, scripts and styles, with the
domain's company, colours, icon, setup steps, table guide and questions swapped in. Student mode only: pages show the
expected result for each question, never the answer SQL.

Usage: python render_pages.py [--hub URL] <domain> [...]
Output: pages/<domain>.html
"""
import html
import json
import re
import sys
from pathlib import Path

import runner
import site_chrome
from build_items import samples
from translate import MODELS, Translator
from wb_domains import DOMAINS
from written_answers import Q as WRITTEN_Q

HERE = Path(__file__).resolve().parent
TEMPLATE = (HERE / 'template' / 'amerimed_page.html').read_text(encoding='utf-8')
LEVEL = {'B': 'Beginner', 'I': 'Intermediate', 'A': 'Advanced'}
CHALLENGE_NOTES = ('Ten multi-step problems in the style of real data interviews. Each one combines several skills at once: '
                   'window functions, CTEs, self-joins, anti-joins and aggregation that must not double-count. Expect these to '
                   'take a while. Plan the steps first, build the query one CTE at a time and check the rows after each step. '
                   'The approach hint is shown with the expected result, so try on your own before you open it.')

ICONS = {  # 24x24 stroke paths, drawn white on the domain colour
    'bank': 'M3 10h18M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18M12 3l9 5H3z',
    'chart': 'M3 3v18h18M7 15l4-4 3 3 6-6M16 8h4v4',
    'fuel': 'M12 3c3.5 4.2 6 7.6 6 10.5A6 6 0 0 1 6 13.5C6 10.6 8.5 7.2 12 3z',
    'flask': 'M9 3h6M10 3v6L4.5 19a2 2 0 0 0 1.8 3h11.4a2 2 0 0 0 1.8-3L14 9V3M7 15h10',
    'cart': 'M6 6h15l-1.6 8.5H7.5zM6 6 5 3H2M9 20.5h.01M18 20.5h.01',
    'box': 'M21 8l-9-5-9 5 9 5zM3 8v8l9 5 9-5V8M12 13v8',
    'truck': 'M2 6h12v10H2zM14 9h4.5L22 12.5V16h-8M6.5 19.5h.01M17.5 19.5h.01',
    'factory': 'M3 21V11l6 3.5V11l6 3.5V6l6 3v12zM3 21h18',
    'bag': 'M5 8h14l-1.2 12.2a2 2 0 0 1-2 1.8H8.2a2 2 0 0 1-2-1.8zM9 8V6a3 3 0 0 1 6 0v2',
}
PLACE = {'banking': 'Bank', 'brokerage': 'Brokerage', 'oil': 'Energy Shipping', 'pharma': 'Drug Maker',
         'retail': 'Retail Store', 'retail_inventory': 'Warehouse Stock', 'retail_logistics': 'Delivery Network',
         'retail_manufacturing': 'Factory', 'retail_supply_chain': 'Supply Chain', 'ecommerce': 'Online Marketplace'}


def words(table):
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', table).lower()


def rgb(hexcolor):
    h = hexcolor.lstrip('#')
    return ', '.join(str(int(h[i:i + 2], 16)) for i in (0, 2, 4))


def logo(cfg, color):
    path = ICONS[cfg['icon']]
    return (f'<rect x="1" y="1" width="46" height="46" rx="12" fill="{color}"/>'
            f'<g transform="translate(9 9) scale(1.25)" fill="none" stroke="#ffffff" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round"><path d="{path}"/></g>')


def favicon(cfg):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">{logo(cfg, cfg["color"])}</svg>'
    return 'data:image/svg+xml,' + svg.replace('"', "'").replace('#', '%23').replace('<', '%3C').replace('>', '%3E')


def table_guide(slug, cfg):
    m = MODELS[slug]
    rows = []
    for t in m['tables']:
        cols = []
        for c in t['columns']:
            label = c['name'] + (' (PK)' if c['name'] == t['key'] else '')
            if c['name'] == m['map']['Category'] and t['name'] == m['base'][0]:
                label += ' (A · B · C)'
            if c['name'] == m['map']['Status'] and t['name'] == m['base'][0]:
                label += ' (Open · Closed · Pending)'
            cols.append(label)
        rows.append(f'<tr><td>{t["name"]}</td><td>{html.escape(", ".join(cols))}</td></tr>')
    return '<div class="tbl"><table class="tbl-mini">' + ''.join(rows) + '</table></div>'


def facts(slug, cfg):
    """Row counts and the first rows a student sees in step 4."""
    cur = runner.connect('WB_' + slug).cursor()
    counts = []
    for t in MODELS[slug]['tables']:
        cur.execute(f'SELECT COUNT(*) FROM {slug}.{t["name"]}')
        counts.append((t['name'], cur.fetchone()[0]))
    P = cfg['P']
    cur.execute(f'SELECT TOP (1) {P[1]}, {P[2]}, {P[4]} FROM {slug}.{P[0]} ORDER BY {P[1]}')
    first = cur.fetchone()
    return counts, first


def page_data(slug, tr):
    tmpl = json.loads(re.search(r'^const DATA = (\[.*\]);$', TEMPLATE, re.M).group(1))
    items = json.loads((HERE / 'items' / f'{slug}.json').read_text(encoding='utf-8'))
    by_topic = {}
    for it in items:
        by_topic.setdefault(it['topic'], []).append(it)
    out = []
    for t in tmpl:
        topic = t['items'][0]['id'].rsplit('-', 1)[0]
        rows = []
        for it in by_topic[topic]:
            lvl = it['id'].rsplit('-', 1)[1][0]
            q = WRITTEN_Q.get(slug, {}).get(it['id'], it['q'])
            rows.append(dict(id=it['id'], sub=LEVEL[lvl], lvl=lvl, title=it['title'], q=q, a=it.get('a')))
        notes = join_notes(slug) if t['key'] == 'joins' else tr.prose(t['notes'])
        out.append(dict(key=t['key'], name=t['name'], track=t['track'], notes=notes, items=rows))
    return out


def challenge_topic(slug):
    items = json.loads((HERE / 'items' / f'{slug}_challenges.json').read_text(encoding='utf-8'))
    rows = [dict(id=it['id'], sub='Interview challenges', lvl='X', title=it['title'], q=it['q'], a=it['a']) for it in items]
    return dict(key='interview-challenges', name='Interview Challenges', track='advanced', notes=CHALLENGE_NOTES, items=rows)


def add_challenges(s, slug):
    """Append the Interview Challenges topic to a rendered page and teach its script the extra 'Challenge' level."""
    m = re.search(r'^const DATA = (\[.*\]);$', s, re.M)
    data = json.loads(m.group(1))                     # JSON reads the page's "<\/" escapes natively
    data = [d for d in data if d['key'] != 'interview-challenges'] + [challenge_topic(slug)]
    total = sum(len(d['items']) for d in data)
    js = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    s = s[:m.start()] + 'const DATA = ' + js + ';' + s[m.end():]

    def rep(old, new):
        nonlocal s
        assert old in s, old[:80]
        s = s.replace(old, new)
    rep('A: { name: "Advanced", color: "var(--rose)" } };',
        'A: { name: "Advanced", color: "var(--rose)" }, X: { name: "Challenge", color: "var(--violet)" } };')
    rep('const lv = Object.entries(LEVELS).map(([k, L]) =>',
        'const lv = Object.entries(LEVELS).filter(([k]) => d.items.some(i => i.lvl === k)).map(([k, L]) =>')
    rep('<span class="sw"></span>Advanced</button>',
        '<span class="sw"></span>Advanced</button>\n          <button class="seg-btn" type="button" role="tab" data-level="X" '
        'aria-selected="false" style="--tc:var(--violet)"><span class="sw"></span>Challenge</button>')
    rep('Questions: <strong>480</strong>', f'Questions: <strong>{total}</strong>')
    rep('Topics: <strong>16</strong>', f'Topics: <strong>{len(data)}</strong>')
    rep('Browse all 16 topics', f'Browse all {len(data)} topics')
    rep('Curriculum &bull; 16 Topics', f'Curriculum &bull; {len(data)} Topics')
    rep('Search all 480 questions', f'Search all {total} questions')
    return s


def join_notes(slug):
    """Describe the domain's own relationships, from the foreign keys in domain_models.json."""
    m = MODELS[slug]
    links = []
    for t in m['tables']:
        for fk in t.get('fks', []):
            if fk['parent'] != t['name']:
                links.append(f"{t['name']}.{fk['column']} → {fk['parent']}")
    E = m['base'][0]
    return (f"Combine rows from two or more tables. The links are: {'; '.join(links)}. "
            f"{E} also has a self-reference ({m['map']['ParentID']}), which is empty in this data set.")


def render(slug, hub=None):
    cfg = DOMAINS[slug]
    m = MODELS[slug]
    E, P = m['base'][0], cfg['P']
    tr = Translator(slug)
    sess = runner.Session(slug)
    tr.set_samples(samples(sess, slug, tr))
    counts, first = facts(slug, cfg)
    n = cfg['n']
    ev, evs = n['ev']
    pt, pts = n['pt']
    co, short, db = cfg['company'], cfg['short'], cfg['db']
    table_list = [words(t) for t, _ in counts]
    tables_text = ', '.join(table_list[:-1]) + ' and ' + table_list[-1]
    count_text = ', '.join(f'{t} {c}' for t, c in counts)
    count_words = ', '.join(f'{c} {words(t)}' for t, c in counts[:-1]) + f' and {counts[-1][1]} {words(counts[-1][0])}'

    s = TEMPLATE
    s = s[s.index('<title>'):s.rindex('</body>')]           # drop the publish skeleton that wrapped the saved copy
    data = json.dumps(page_data(slug, tr), ensure_ascii=False).replace('</', '<\\/')
    s = re.sub(r'^const DATA = \[.*\];$', lambda _: 'const DATA = ' + data + ';', s, count=1, flags=re.M)

    def rep(old, new, count=1):
        nonlocal s
        assert s.count(old) >= 1, old[:80]
        s = s.replace(old, new) if count == 0 else s.replace(old, new, count)

    # ---- identity, colours, icon ----
    rep('<title>Healthcare SQL Assignments</title>', f'<title>{html.escape(co)} SQL Assignments</title>')
    s = re.sub(r'<link rel="icon" href="[^"]*">', f'<link rel="icon" href="{favicon(cfg)}">', s, count=1)
    rep('--teal: #2dd4bf;   /* healthcare primary */', f'--teal: {cfg["color"]};   /* {slug} primary */')
    rep('--teal: #0d9488;', f'--teal: {cfg["light"]};', 0)
    rep('rgba(20, 184, 166,', f'rgba({rgb(cfg["color"])},', 0)
    s = re.sub(r'<symbol id="i-logo" viewBox="0 0 48 48">.*?</symbol>',
               lambda _: f'<symbol id="i-logo" viewBox="0 0 48 48">{logo(cfg, "var(--teal)")}</symbol>', s, count=1, flags=re.S)
    rep('aria-label="Amerimed Healthcare SQL Workbook"', f'aria-label="{html.escape(co)} SQL Workbook"')
    rep('<span class="brand-name">Amerimed</span>', f'<span class="brand-name">{html.escape(short)}</span>')
    if hub:
        rep('<nav class="nav-links" aria-label="Sections">',
            f'<nav class="nav-links" aria-label="Sections">\n        <a class="nav-btn" href="{hub}" target="_blank" rel="noopener">'
            f'<svg class="i"><use href="#i-grid"/></svg>All domains</a>')
        rep('<nav aria-label="Footer links">',
            f'<nav aria-label="Footer links">\n          <a class="nav-btn" href="{hub}" target="_blank" rel="noopener">'
            f'<svg class="i" style="color:var(--teal)"><use href="#i-grid"/></svg>All domains</a>')

    # ---- hero ----
    rep('Tinitiate AI Academy &bull; Healthcare SQL Track', f'Tinitiate AI Academy &bull; {html.escape(cfg["industry"])} SQL Track')
    rep('SQL Server on a Real Hospital Schema', f'SQL Server on a Real {PLACE[slug]} Schema')
    rep("questions on Amerimed's patients, doctors, encounters, medications and prescriptions",
        f"questions on {html.escape(short)}'s {tables_text}")

    # ---- start here ----
    rep('CREATE DATABASE AmerimedPractice;', f'CREATE DATABASE {db};')
    rep('<b>AmerimedPractice</b>', f'<b>{db}</b>', 0)
    rep('Load the Amerimed data', f'Load the {html.escape(short)} data')
    rep('Patients 100, Doctors 50, Medications 50, Encounters 240, Prescriptions 164', count_text)
    rep('SELECT TOP (5) PatientID, PatientName, Region\nFROM healthcare.Patients;',
        f'SELECT TOP (5) {P[1]}, {P[2]}, {P[4]}\nFROM {slug}.{P[0]};')
    rep('You should see 5 patients, starting with <b>1 · Olivia Bennett · North</b>.',
        f'You should see 5 {pts}, starting with <b>{first[0]} · {html.escape(first[1])} · {first[2]}</b>.')
    rep('<li><code>FROM healthcare.Patients</code> names the table: <i>healthcare</i> is the schema (a folder), <i>Patients</i> is the table.</li>',
        f'<li><code>FROM {slug}.{P[0]}</code> names the table: <i>{slug}</i> is the schema (a folder), <i>{P[0]}</i> is the table.</li>')
    rep('Start with <a href="#introduction">Introduction</a>', 'Start with <a href="#introduction">Introduction</a>')

    # ---- FAQ ----
    rep("SELECT * FROM healthcare.TableName;", f"SELECT * FROM {slug}.TableName;")
    rep("Invalid object name 'healthcare.Patients'", f"Invalid object name '{slug}.{P[0]}'")
    rep('Choose AmerimedPractice in the drop-down', f'Choose {db} in the drop-down')
    rep("Ambiguous column name 'PatientID'", f"Ambiguous column name '{P[1]}'")
    rep('<code>p.PatientID</code>', f'<code>p.{P[1]}</code>')
    s = re.sub(r'<p>Create a fresh database \(for example <code>AmerimedPractice2</code>\).*?</code></pre>',
               lambda _: (f'<p>Create a fresh database (for example <code>{db}2</code>), select it and run <code>data_setup.sql</code> again. '
                          'Questions in the DDL, Constraints and DML topics change the data, so it helps to keep a second practice '
                          'database just for them and reload it whenever you want a clean start.</p>'), s, count=1, flags=re.S)
    rep('such as Patients.</dd>', f'such as {P[0]}.</dd>')
    rep("A row is one record (one patient). A column is one piece of information (the patient's region).",
        f"A row is one record (one {pt}). A column is one piece of information (the {pt}'s region).")
    rep('All Amerimed tables are in the <i>healthcare</i> schema.', f'All {html.escape(short)} tables are in the <i>{slug}</i> schema.')
    rep('such as PatientID.</dd>', f'such as {P[1]}.</dd>')
    rep('such as Encounters.PatientID.</dd>', f'such as {E}.{P[1]}.</dd>')
    s = re.sub(r'<dt>Encounter</dt><dd>[^<]*</dd>',
               lambda _: (f'<dt>{ev[0].upper() + ev[1:]}</dt><dd>One row in {E}: a {ev} at {html.escape(short)}. '
                          f'{m["map"]["Category"]} is A, B or C, and {m["map"]["Status"]} is Open, Closed or Pending.</dd>'), s, count=1)

    # ---- before you start ----
    rep('create a new database (for example <code>AmerimedPractice</code>)', f'create a new database (for example <code>{db}</code>)')
    s = re.sub(r'Open <code>data_setup.sql</code> from the healthcare folder and run it once\. It creates the <code>healthcare</code> schema with [^<]*\.',
               lambda _: f'Open <code>data_setup.sql</code> from the {slug} folder and run it once. It creates the <code>{slug}</code> schema with {count_words}.', s, count=1)
    s = re.sub(r'<li>For DDL, Constraints and DML questions, wrap your work in .*?</li>',
               lambda _: ('<li>DDL, Constraints and DML questions change the data. Run <code>data_setup.sql</code> again in a fresh '
                          'database when you want to start clean.</li>'), s, count=1, flags=re.S)
    s = re.sub(r'<div class="tbl"><table class="tbl-mini">.*?</table></div>', lambda _: table_guide(slug, cfg), s, count=1, flags=re.S)
    rep('learn the five tables', f'learn the {len(counts)} tables'.replace(' 5 ', ' five '))

    # ---- footer + script ----
    rep('on the Amerimed healthcare dataset.', f'on the {html.escape(co)} {cfg["industry"].lower()} dataset.')
    rep('Amerimed Healthcare SQL Workbook</p>', f'{html.escape(co)} SQL Workbook</p>')
    rep('"amerimed-done-"', f'"{slug.replace("_", "-")}-done-"')
    rep('Try a table name such as Encounters', f'Try a table name such as {E}')

    s = add_challenges(s, slug)
    leftovers = re.findall(r'[^\n]{0,40}(?:Amerimed|healthcare|Healthcare|Patient|patient|Encounter|encounter|BEGIN TRAN)[^\n]{0,40}',
                           s[:s.index('const DATA')] + s[s.index('const MODE'):])
    if leftovers:
        print(slug, 'LEFTOVER IN PAGE CHROME:', leftovers[:8])
    s = site_chrome.apply(s, slug)
    out = HERE / 'pages' / f'{slug}.html'
    out.parent.mkdir(exist_ok=True)
    out.write_text(s, encoding='utf-8')
    return out


def render_healthcare():
    """The AmeriMed page is the template itself: keep it as is and only add the Interview Challenges topic."""
    s = TEMPLATE[TEMPLATE.index('<title>'):TEMPLATE.rindex('</body>')]
    s = add_challenges(s, 'healthcare')
    s = site_chrome.apply(s, 'healthcare')
    out = HERE / 'pages' / 'healthcare.html'
    out.write_text(s, encoding='utf-8')
    return out


if __name__ == '__main__':
    args = sys.argv[1:]
    hub = None
    if args[:1] == ['--hub']:
        hub, args = args[1], args[2:]
    for d in args:
        p = render_healthcare() if d == 'healthcare' else render(d, hub)
        print(d, p.stat().st_size // 1024, 'KB')
