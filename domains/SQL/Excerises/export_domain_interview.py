"""Export exact canonical domain questions and complete small-fixture inputs."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
import sys as _sys; _sys.path.insert(0, str(Path(__file__).resolve().parent))
from company_paths import domain_dir, domain_dirs, DOMAINS_ROOT, ASSIGNMENTS_INDEX


def choose(ids):
    wanted=set(ids);found={}
    with (ROOT/'domain_interview_questions.jsonl').open(encoding='utf-8') as stream:
        for line in stream:
            q=json.loads(line)
            if q['id'] in wanted:found[q['id']]=q
            if len(found)==len(wanted):break
    missing=wanted-set(found)
    if missing:raise ValueError(f'Unknown question IDs:{sorted(missing)}')
    if len(ids)!=len(wanted):raise ValueError('Duplicate requested question IDs.')
    return [found[i] for i in ids]


def fixture(model):
    lines=[f'## {model["title"]}: input schema and small baseline','',
           'The data is fictional. These are inputs,not expected query outputs. Query tests may use a different independently checked fixture with the same schema.','']
    for table in model['tables']:
        lines += [f'### [{model["slug"]}].[{table["name"]}]','',
                  '| Column | Type | Required rule |','|---|---|---|']
        for c in table['columns']:lines.append(f'| {c["name"]} | {c["type"]} | {c["rule"]} |')
        lines += ['',f'Primary key:`{table["key"]}`.']
        if table['unique']:lines += ['Unique rules:'+json.dumps(table['unique'])+'.']
        if table['checks']:lines += ['Checks:'+json.dumps(table['checks'])+'.']
        if table['fks']:lines += ['Foreign keys:'+json.dumps(table['fks'])+'.']
        lines += ['', 'Column order:'+','.join(c['name'] for c in table['columns'])+'.','',
                  '```json',json.dumps(table['rows'],ensure_ascii=False),'```','']
    return '\n'.join(lines)


def save(path,questions,models,title):
    path=path.resolve()
    if not any(path.is_relative_to(d) for d in domain_dirs()):raise ValueError('Student exports must stay under a company sql folder (domains/<company>/sql).')
    path.parent.mkdir(parents=True,exist_ok=True)
    lines=[f'# {title}','',
           'These are the exact practice-bank contracts with unchanged IDs. Setup is outside coding time. '+
           'Query solutions must return both analysis audit and report. Practical labs require the stated observed evidence. No CoderPad upload has been performed.','']
    for q in questions:
        lines += [f'## {q["id"]}','',f'{q["level"]} · {q["subtopic"]} · {q["title"]}','',q['prompt'],'']
    for s in dict.fromkeys(q['domain'] for q in questions):lines += [fixture(next(m for m in models if m['slug']==s))]
    path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    manifest=dict(title=title,question_ids=[q['id'] for q in questions],
                  canonical_prompt_sha256={q['id']:hashlib.sha256(q['prompt'].encode()).hexdigest() for q in questions},
                  coding_minutes=sum(q['timebox_minutes'] for q in questions),
                  note='Same canonical practice and interview prompts;manual editor/pad setup required.')
    path.with_suffix('.manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    return manifest


def generate_mocks(models):
    wanted={}
    for m in models:
        p=m['slug'].upper()
        wanted[m['slug']]=dict(hard=[f'{p}-CTE-03-A06',f'{p}-JOINS-02-A15'],
                               mixed=[f'{p}-OPERATORS-01-B15',f'{p}-ANALYTICAL_FUNCTIONS-06-I07',f'{p}-AGGREGATES-02-A09'])
    allids=[i for d in wanted.values() for ids in d.values() for i in ids]
    found={q['id']:q for q in choose(allids)}
    for m in models:
        directory=domain_dir(m['slug'])/'questions'
        for key,filename in [('hard','HARD_MOCK.md'),('mixed','MIXED_MOCK.md')]:
            selected=[found[i] for i in wanted[m['slug']][key]]
            lines=[f'# {m["title"]}: {key} SQL mock','',
                   'This test selects canonical assignments. Open each linked question;its complete contract applies. Question text and schema are stored once in the topic files and domain guide.','',
                   f'Coding time: {sum(q["timebox_minutes"] for q in selected)} minutes. Setup is outside the timer.','',
                   '| Assignment | Level | Challenge |','|---|---|---|']
            for q in selected:lines.append(f'| [{q["id"]}]({q["topic"]}.md#{q["id"].lower()}) | {q["level"]} | {q["title"]} |')
            lines += ['','[Input schema and baseline rows](DOMAIN_GUIDE.md) · [Assessment instructions](CODERPAD.md) · [All assignments](README.md)','']
            path=directory/filename;path.write_text('\n'.join(lines),encoding='utf-8')
            manifest=dict(layout='canonical_references',question_ids=[q['id'] for q in selected],
                          canonical_prompt_sha256={q['id']:hashlib.sha256(q['prompt'].encode()).hexdigest() for q in selected},
                          coding_minutes=sum(q['timebox_minutes'] for q in selected))
            path.with_suffix('.manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ids',required=True,help='Comma-separated canonical IDs.')
    parser.add_argument('--out',required=True,type=Path)
    args=parser.parse_args()
    models=json.loads((ROOT/'domain_models.json').read_text(encoding='utf-8'))
    out=args.out if args.out.is_absolute() else ROOT/args.out
    print(json.dumps(save(out,choose(args.ids.split(',')),models,'SQL interview handout'),indent=2))


if __name__=='__main__':main()
