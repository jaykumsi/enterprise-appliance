"""Translate the 480 AmeriMed items into one domain, run every answer on WB_<domain>, and save items + a flag report.

Usage: python build_items.py <domain> [<domain> ...]
Output: items/<domain>.json  (private: contains answer SQL)  and a printed summary of flagged items.
"""
import json
import re
import sys
from pathlib import Path

import runner
from translate import LEFTOVER, Translator, has, needs
import fallback_hc, fallback_hc2, fallback_hc3, fallback_hc4, fallback_hc5  # noqa: F401  (register replacement items)
FB = fallback_hc.FB
FORCE = {'CONSTRAINTS-B06', 'CONSTRAINTS-B07', 'DML-A09', 'DML-A10', 'CONSTRAINTS-A05', 'CONSTRAINTS-I06',
         'CONSTRAINTS-B10', 'CONSTRAINTS-I03', 'CTE-A06', 'DML-A08'}
# Anti-join questions: "never had any" is legitimately empty when every party is active.
ACCEPT_EMPTY = {'JOINS-B06', 'JOINS-B10', 'SET_OPERATIONS-B05', 'SET_OPERATIONS-B06', 'SET_OPERATIONS-I10',
                'SUBQUERIES-B04', 'SUBQUERIES-I02', 'OPERATORS-I06', 'ANALYTICAL_FUNCTIONS-A04', 'SUBQUERIES-I07'}  # always use the replacement outside healthcare
from wb_domains import DOMAINS

HERE = Path(__file__).resolve().parent
HC_AMOUNTS = json.loads((HERE / 'items' / 'healthcare_amounts.json').read_text())
SPECIAL = ('changes every time', 'depends on your own', 'not run here')


def hc_items():
    d = json.loads((runner.ROOT / 'consolidated_supplements.json').read_text(encoding='utf-8'))['healthcare']
    out = []
    for x in d:
        a = x['answer'] or ''
        out.append(dict(
            id=x['id'], topic=x['topic'], title=x['title'], q=x['body'],
            sql='\n\n'.join(s.strip() for s in re.findall(r'```sql\n(.*?)```', a, re.S)),
            how=(re.search(r'\*\*How it works:\*\*\s*(.*?)(?:\n\n\*\*Expected|\Z)', a, re.S) or [None, ''])[1].strip(),
            check=x['self_check']))
    return out


def load_overrides(slug):
    p = HERE / 'overrides' / f'{slug}.json'
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}


def stats(sess, slug):
    mp = Translator(slug).model['map']
    E = Translator(slug).model['base'][0]
    cur = sess.conn.cursor()
    cur.execute(f'SELECT AVG(CAST({mp["Amount"]} AS float)) FROM {slug}.{E}')
    ratio = cur.fetchone()[0] / 152.7625
    cur.execute(f'SELECT CAST({mp["Amount"]} AS float) FROM {slug}.{E} WHERE {mp["Amount"]} IS NOT NULL ORDER BY 1')
    dom = [r[0] for r in cur.fetchall()]
    return {'amt': ratio, 'q': (HC_AMOUNTS, dom)}


def samples(sess, slug, tr):
    cfg, mp, E = DOMAINS[slug], tr.model['map'], tr.model['base'][0]
    cur = sess.conn.cursor()

    def one(sql):
        cur.execute(sql)
        r = cur.fetchone()
        return r[0] if r else None
    out = {'HEA': one(f"SELECT {mp['Label']} FROM {slug}.{E} WHERE {mp['RecordID']} = 1"),
           'PT': one(f"SELECT {cfg['P'][3]} FROM {slug}.{cfg['P'][0]} WHERE {cfg['P'][1]} = 1")}
    if cfg['M']:
        out['MED'] = one(f"SELECT {cfg['M'][3]} FROM {slug}.{cfg['M'][0]} WHERE {cfg['M'][1]} = 1")
    if cfg['D']:
        out['LIC'] = one(f"SELECT {cfg['D'][3]} FROM {slug}.{cfg['D'][0]} WHERE {cfg['D'][1]} = 1")
    if cfg['L'] and cfg['L'][2]:
        out['RX'] = one(f"SELECT TOP (1) {cfg['L'][2]} FROM {slug}.{cfg['L'][0]} ORDER BY 1")
    return out


def build(slug):
    sess = runner.Session(slug)
    tr = Translator(slug, stats(sess, slug))
    tr.set_samples(samples(sess, slug, tr))
    ov = load_overrides(slug)
    cfg = DOMAINS[slug]
    hc_runs = json.loads((HERE / 'items' / 'healthcare_rows.json').read_text()) if (HERE / 'items' / 'healthcare_rows.json').exists() else {}
    items, flags = [], []
    def make(x, src, o):
        if o:
            return dict(id=x['id'], topic=x['topic'], title=o.get('title', ''), q=o.get('q', ''), sql=o.get('sql', ''),
                        how=o.get('how', ''), check=x['check'], src='override')
        sql, texts = tr.scale_amounts(src['sql'], dict(title=src['title'], q=src['q'], how=src['how']))
        if x['id'] == 'CONSTRAINTS-I09':  # the format check uses the domain's real code length
            n = str(len(tr.codes['PT'][0]) + tr.codes['PT'][1])
            sql = sql.replace('= 10', '= ' + n)
            texts['q'] = texts['q'].replace('exactly 10', 'exactly ' + n)
        return dict(id=x['id'], topic=x['topic'], title=tr.prose(texts['title']), q=tr.text(texts['q']),
                    sql=tr.code(sql), how=tr.text(texts['how']), check=x['check'],
                    src='fallback' if src is not x else 'auto')

    def run(x, it, src):
        f = []
        blob = ' '.join([it['title'], it['q'], it['how'], it['sql']])
        if LEFTOVER.search(blob):
            f.append('leftover:' + ','.join(sorted(set(m.group(0) for m in LEFTOVER.finditer(blob)))))
        hc_check = x['check']
        if src is not x and not src['sql']:
            hc_check = None
        if not hc_check:
            it['a'] = None
        elif any(k in hc_check for k in SPECIAL):
            it['a'] = hc_check.split('\n')[0]
        else:
            res = sess.run(it['sql'])
            if res[0] == 'error':
                f.append('error:' + re.sub(r'^.*\[SQL Server\]', '', res[1])[:160])
                it['a'] = None
            else:
                it['a'] = runner.render(res).replace('WB\\_' + slug, cfg['db'])
                if res[0] == 'rows' and not res[2] and hc_runs.get(x['id'], 1) > 0 \
                        and 'empty result' not in it['how'] and x['id'] not in ACCEPT_EMPTY:
                    f.append('empty')
                it['rows'] = len(res[2]) if res[0] == 'rows' else -1
        return f

    for x in hc_items():
        o = ov.get(x['id'])
        src = x
        need = needs(x['title'], x['q'], x['sql'], x['how'])
        if x['id'] in FORCE or any(not has(cfg, k) for k in need):
            if x['id'] not in FB:
                raise SystemExit(f"{slug}: {x['id']} needs {need} but has no replacement")
            src = dict(x, **FB[x['id']])
        it = make(x, src, o)
        f = run(x, it, src)
        if (any(g.startswith('error') for g in f) or 'empty' in f) and src is x and not o and x['id'] in FB:
            src = dict(x, **FB[x['id']])           # the original relies on healthcare-only data: use the replacement
            it2 = make(x, src, o)
            f2 = run(x, it2, src)
            if not any(g.startswith('error') for g in f2) and 'empty' not in f2:
                it, f = it2, f2
        if o and o.get('accept_empty'):
            f = [g for g in f if g != 'empty']
        if f:
            flags.append((x['id'], f))
        it['flags'] = f
        items.append(it)
    (HERE / 'items').mkdir(exist_ok=True)
    (HERE / 'items' / f'{slug}.json').write_text(json.dumps(items, indent=1, ensure_ascii=False), encoding='utf-8')
    return items, flags


if __name__ == '__main__':
    for slug in sys.argv[1:]:
        items, flags = build(slug)
        print(f'== {slug}: {len(items)} items, {len(flags)} flagged')
        for i, f in flags:
            print(' ', i, '|', ' ; '.join(f))
