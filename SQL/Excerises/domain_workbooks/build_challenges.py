"""Run every Interview Challenge on WB_<domain> and write items/<domain>_challenges.json (private: holds answer SQL).

Usage: python build_challenges.py [-v] <domain> [...]      (-v prints the first rows of each result)
"""
import json
import sys
from pathlib import Path

import runner
from challenges import challenges

HERE = Path(__file__).resolve().parent


def build(domain, verbose=False):
    sess = runner.Session(domain)
    out, problems = [], []
    for n, (title, q, sql, hint) in enumerate(challenges(domain), 1):
        cid = f'CHALLENGE-X{n:02d}'
        res = sess.run(sql)
        if res[0] != 'rows':
            problems.append((cid, title, res[1] if res[0] == 'error' else 'no result set'))
            continue
        rows = res[2]
        if not rows:
            problems.append((cid, title, 'EMPTY'))
        a = f'**Approach hint:** {hint}\n\n' + runner.render(res)
        out.append(dict(id=cid, topic='CHALLENGES', title=title, q=q, sql=sql, how=hint, a=a, rows=len(rows)))
        print(f'  {cid} {len(rows):4d} rows  {title}')
        if verbose:
            print('       ', res[1])
            for r in rows[:4]:
                print('       ', [runner.fmt(v) for v in r])
    (HERE / 'items' / f'{domain}_challenges.json').write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding='utf-8')
    return problems


if __name__ == '__main__':
    args = sys.argv[1:]
    verbose = '-v' in args
    for d in [a for a in args if a != '-v']:
        print('==', d)
        for p in build(d, verbose):
            print('  PROBLEM', p)
