"""Inspect, export, select and validate the canonical bank. No external writes."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def read_bank():
    return json.loads((ROOT/'bank.json').read_text(encoding='utf-8'))


def render_question(q):
    lines=[f'## {q["id"]} — {q["subtopic"]}', '',
           f'{q["subject_name"]} / {q["topic"]} / {q["level"]}', '',
           f'Runtime: {q["runtime"]}. Suggested time: {q["timebox_minutes"]} minutes.', '',
           '**Core problem**', '',q['core'], '',
           '**Acceptance example / baseline**','',q['acceptance_example'],'',
           '**Interview requirement**','',q['extension'],'',
           'Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.','']
    path=ROOT/q['fixture']
    if q['fixture'].startswith('fixtures/'):
        if q['subject']=='sql-server' and (q['topic']=='DATA_SETUP' or (q['topic']=='DDL' and q['subtopic']=='Create')):
            lines += ['**Instructor setup note:** This build/load assessment uses a fresh scratch namespace. The core states its table/row requirements. Do not preload the solved CREATE/INSERT fixture. The instructor retains the setup and checks independently.','']
        else:
            lines += ['**Fixture — instructor may preload this before the timer**','',
                      '```sql',path.read_text(encoding='utf-8').strip(),'```','']
    else:
        lines += ['**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.','']
    if q['subject']=='sql-server':
        lines += ['**Retail table contract**','',(ROOT/'fixtures/retail_contract.md').read_text(encoding='utf-8').strip(),'']
    return '\n'.join(lines)


def within_bank(path):
    result=path.resolve()
    if not result.is_relative_to(ROOT):
        raise ValueError('Output must stay inside interview-practice-bank.')
    return result


def save_export(path,questions,title):
    path=within_bank(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    content=f'# {title}\n\nThese questions use the same IDs,core contracts and extensions as the practice bank.\n\n'
    content+='\n\n'.join(render_question(q) for q in questions)
    path.write_text(content,encoding='utf-8')
    manifest=dict(title=title,question_ids=[q['id'] for q in questions],
                  bank_sha256=hashlib.sha256((ROOT/'bank.json').read_bytes()).hexdigest(),
                  total_suggested_minutes=sum(q['timebox_minutes'] for q in questions),
                  native_execution_verified=False,
                  note='Review/run in the intended runtime before administration. No CoderPad upload was performed.')
    path.with_suffix('.manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    return manifest


def choose_mock(bank,subject,level,seed,count,exclude=()):
    rng=random.Random(seed)
    if level=='Mixed':
        if count!=3:
            raise ValueError('A Mixed mock uses exactly three questions: one per level.')
        chosen=[]
        used_subtopics=set()
        for selected_level in ('Beginner','Intermediate','Advanced'):
            candidates=[q for q in bank['questions'] if q['subject']==subject and q['level']==selected_level
                        and q['id'] not in exclude and q['subtopic_id'] not in used_subtopics]
            if not candidates:
                raise ValueError('No eligible distinct subtopic remains for the mixed mock.')
            question=rng.choice(candidates)
            chosen.append(question)
            used_subtopics.add(question['subtopic_id'])
        return chosen
    pool=defaultdict(list)
    for q in bank['questions']:
        if q['subject']==subject and q['level']==level and q['id'] not in exclude:
            pool[q['subtopic_id']].append(q)
    if len(pool)<count:
        raise ValueError(f'Need {count} distinct eligible subtopics; found {len(pool)}.')
    keys=rng.sample(sorted(pool),count)
    return [rng.choice(pool[key]) for key in keys]


def samples(bank):
    index={q['id']:q for q in bank['questions']}
    save_export(ROOT/'exports/python-question.md',[index['PY-FUNDAMENTALS-01-B01']],'Python beginner sample')
    save_export(ROOT/'exports/python-mock.md',choose_mock(bank,'python','Intermediate',21,3),'Python intermediate mock - seed 21')
    lines=['# Sample interview handouts','',
           'Each sample uses the same records as student practice. Review the selected tasks and prepare independent expected results before administering. Setup happens before the timer. No sample has been uploaded to CoderPad.','',
           '| Subject | Mixed mock | Levels | Coding time |','|---|---|---|---:|']
    for subject,meta in bank['subjects'].items():
        selected=choose_mock(bank,subject,'Mixed',22,3)
        filename=f'{subject}-mixed.md'
        save_export(ROOT/'exports'/filename,selected,f'{meta["name"]} mixed mock - seed 22')
        lines.append(f'| {meta["name"]} | [{subject}]({filename}) | 1 Beginner + 1 Intermediate + 1 Advanced | 90 minutes |')
    (ROOT/'exports/README.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    return dict(handouts=len(bank['subjects'])+2,mixed_mock_subjects=len(bank['subjects']))


def validate(bank):
    errors=[]
    questions=bank['questions']
    ids=[q['id'] for q in questions]
    if len(ids)!=len(set(ids)): errors.append('Duplicate question IDs.')
    by_sub=defaultdict(list)
    for q in questions:
        by_sub[q['subtopic_id']].append(q)
        for key in ('core','extension','acceptance_example','runtime','fixture','assessment'):
            if not q.get(key): errors.append(f'{q["id"]}: empty {key}')
        if q['fixture'].startswith('fixtures/') and not (ROOT/q['fixture']).is_file():
            errors.append(f'{q["id"]}: missing fixture')
        if q['native_execution_verified']:
            errors.append(f'{q["id"]}: unsupported execution-verification claim')
        if re.search(r'\b(TODO|TBD|lorem ipsum)\b',q['core']+' '+q['extension'],re.I):
            errors.append(f'{q["id"]}: unfinished placeholder')
        if q['subject']=='sql-server' and q['topic']=='INTRODUCTION' and 'Name two relevant database concepts' in q['core']:
            errors.append(f'{q["id"]}: legacy definition-recall question retained')
    for sub,rows in by_sub.items():
        if Counter(q['level'] for q in rows)!=Counter(Beginner=15,Intermediate=15,Advanced=15):
            errors.append(f'{sub}: incorrect level counts')
        if len(set(q['core']+'\n'+q['extension'] for q in rows))!=45:
            errors.append(f'{sub}: duplicate complete question')
    # Ensure every original SQL leaf is retained, not just total counts.
    source=json.loads((ROOT.parent/'domains/SQL/Excerises/curriculum.json').read_text(encoding='utf-8'))
    original={(r['topic'],r['subtopic']) for r in source}
    actual={(q['topic'],q['subtopic']) for q in questions if q['subject']=='sql-server'}
    if actual and original-actual: errors.append(f'Missing original SQL leaves: {sorted(original-actual)}')
    coverage=list(csv.DictReader((ROOT/'coverage.csv').open(encoding='utf-8',newline='')))
    if {c['subtopic_id'] for c in coverage}!=set(by_sub): errors.append('Coverage index disagrees with bank.')
    # All local Markdown file links must resolve.
    for path in ROOT.rglob('*.md'):
        markdown=path.read_text(encoding='utf-8')
        markdown=re.sub(r'```[\s\S]*?```','',markdown)
        markdown=re.sub(r'`[^`]*`','',markdown)
        for target in re.findall(r'\]\(([^)]+)\)',markdown):
            if target.startswith(('https://','http://','#')): continue
            local=target.split('#',1)[0].strip('<>')
            if not (path.parent/local).resolve().exists(): errors.append(f'{path.relative_to(ROOT)}: broken link {target}')
    index={q['id']:q for q in questions}
    current_hash=hashlib.sha256((ROOT/'bank.json').read_bytes()).hexdigest()
    manifests=list((ROOT/'exports').glob('*.manifest.json'))
    for path in manifests:
        manifest=json.loads(path.read_text(encoding='utf-8'))
        if manifest['bank_sha256']!=current_hash:
            errors.append(f'{path.name}: stale bank hash; regenerate samples or export again')
        handout=path.with_name(path.name.replace('.manifest.json','.md'))
        if not handout.is_file():
            errors.append(f'{path.name}: missing handout')
            continue
        content=handout.read_text(encoding='utf-8')
        for qid in manifest['question_ids']:
            if qid not in index or render_question(index[qid]) not in content:
                errors.append(f'{path.name}: handout differs from canonical question {qid}')
    # Validate portable fixture with independent SQL result assertions.
    db=sqlite3.connect(':memory:')
    db.execute('PRAGMA foreign_keys=ON')
    db.executescript((ROOT/'fixtures/portable.sql').read_text(encoding='utf-8'))
    cases=[
        ('filter','SELECT OrderID,AmountCents FROM Orders WHERE AmountCents>=200 AND Status=\'Open\' ORDER BY OrderID',[(3,200)]),
        ('zero-preserving join','SELECT c.CustomerID,COUNT(o.OrderID) FROM Customers c LEFT JOIN Orders o ON o.CustomerID=c.CustomerID GROUP BY c.CustomerID ORDER BY c.CustomerID',[(1,2),(2,2),(3,1),(4,0)]),
        ('conditional counts',"SELECT CustomerID,COUNT(*),SUM(CASE WHEN Status='Open' THEN 1 ELSE 0 END) FROM Orders GROUP BY CustomerID ORDER BY CustomerID",[(1,2,1),(2,2,1),(3,1,1)]),
        ('anti-join',"SELECT CustomerID FROM Customers c WHERE NOT EXISTS(SELECT 1 FROM Orders o WHERE o.CustomerID=c.CustomerID AND o.Status='Open') ORDER BY CustomerID",[(4,)]),
        ('ranking','SELECT CustomerID,OrderID FROM (SELECT CustomerID,OrderID,ROW_NUMBER() OVER(PARTITION BY CustomerID ORDER BY AmountCents DESC,OrderID) n FROM Orders WHERE AmountCents IS NOT NULL) x WHERE n=1 ORDER BY CustomerID',[(1,1),(2,3),(3,5)]),
        ('keyset',"SELECT OrderID FROM Orders WHERE CreatedAt>'2024-01-02T00:00:00Z' OR (CreatedAt='2024-01-02T00:00:00Z' AND OrderID>2) ORDER BY CreatedAt,OrderID LIMIT 2",[(3,),(4,)]),
    ]
    for name,query,expected in cases:
        actual_rows=db.execute(query).fetchall()
        if actual_rows!=expected: errors.append(f'Portable fixture {name}: {actual_rows} != {expected}')
    db.close()
    # Export must contain the exact canonical text and no instructor solution.
    for subject in bank['subjects']:
        for selected_level in ('Intermediate','Mixed'):
            a=choose_mock(bank,subject,selected_level,7,3)
            b=choose_mock(bank,subject,selected_level,7,3)
            if [q['id'] for q in a]!=[q['id'] for q in b]: errors.append(f'{subject}: mock nondeterminism')
            if len({q['subtopic_id'] for q in a})!=3: errors.append(f'{subject}: repeated mock subtopic')
            if selected_level=='Mixed' and {q['level'] for q in a}!={'Beginner','Intermediate','Advanced'}:
                errors.append(f'{subject}: incorrect mixed levels')
    summary=dict(passed=not errors,errors=errors,subjects=len(bank['subjects']),
                 subtopics=len(by_sub),questions=len(questions),
                 per_level=dict(Counter(q['level'] for q in questions)),
                 original_sql_subtopics_preserved=len(original),portable_sql_assertions=len(cases),
                 current_canonical_handouts_checked=len(manifests),
                 native_sql_server_postgresql_snowflake_or_cloud_execution=False,
                 generated_question_solutions_complete=False,
                 note='Structural and export checks plus six portable SQL result assertions; not an independent expert review or execution of every question.')
    (ROOT/'validation.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    return summary


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='cmd',required=True)
    listing=sub.add_parser('list')
    listing.add_argument('--subject')
    listing.add_argument('--level',choices=['Beginner','Intermediate','Advanced'])
    listing.add_argument('--topic')
    export=sub.add_parser('export')
    export.add_argument('--ids',required=True,help='Comma-separated exact question IDs.')
    export.add_argument('--out',required=True,type=Path)
    mock=sub.add_parser('mock')
    mock.add_argument('--subject',required=True)
    mock.add_argument('--level',required=True,choices=['Beginner','Intermediate','Advanced','Mixed'])
    mock.add_argument('--count',type=int,default=3)
    mock.add_argument('--seed',type=int,default=1)
    mock.add_argument('--exclude',default='',help='Comma-separated question IDs already seen.')
    mock.add_argument('--out',required=True,type=Path)
    sub.add_parser('validate')
    sub.add_parser('samples',help='Regenerate example handouts for all subjects from current bank.')
    args=parser.parse_args()
    bank=read_bank()
    if args.cmd=='samples':
        print(json.dumps(samples(bank),indent=2))
        return
    if args.cmd=='validate':
        report=validate(bank)
        print(json.dumps(report,indent=2))
        raise SystemExit(0 if report['passed'] else 1)
    if args.cmd=='list':
        pool=[q for q in bank['questions'] if (not args.subject or q['subject']==args.subject)
              and (not args.level or q['level']==args.level) and (not args.topic or q['topic']==args.topic)]
        # One subtopic line keeps listing usable for a large bank.
        grouped=defaultdict(list)
        for q in pool: grouped[(q['subject'],q['topic'],q['subtopic'])].append(q)
        for (subject,topic,name),rows in grouped.items():
            print(f'{subject} / {topic} / {name}: {len(rows)} questions; first ID {rows[0]["id"]}')
        if not pool: raise SystemExit('No matching questions.')
        return
    if args.cmd=='export':
        index={q['id']:q for q in bank['questions']}
        requested=args.ids.split(',')
        if len(requested)!=len(set(requested)): parser.error('Duplicate requested question ID.')
        missing=[i for i in requested if i not in index]
        if missing: parser.error(f'Unknown IDs: {missing}')
        chosen=[index[i] for i in requested]
        title='Interview question handout'
    else:
        if args.subject not in bank['subjects']: parser.error('Unknown subject; see catalog.md.')
        if args.count<=0: parser.error('--count must be positive.')
        chosen=choose_mock(bank,args.subject,args.level,args.seed,args.count,args.exclude.split(','))
        title=f'{bank["subjects"][args.subject]["name"]} {args.level} mock — seed {args.seed}'
    output=args.out if args.out.is_absolute() else ROOT/args.out
    print(json.dumps(save_export(output,chosen,title),indent=2))


if __name__=='__main__':
    main()
