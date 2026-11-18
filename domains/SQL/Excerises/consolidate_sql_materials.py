"""Consolidate published SQL handouts;retain unique material and removal provenance.

Only explicitly mapped files inside the training workspace can be removed.
Machine-readable source records remain build inputs,not alternate handouts.
"""
from collections import defaultdict
import hashlib
import json
import os
from pathlib import Path
import re
from healthcare_exercise_review import KEPT_IDS, publish_review, amerimed_menu, selected_case

# Fictional company per domain, shown at the top of each domain README.
COMPANIES = {
    'healthcare': 'Fictional company: **AmeriMed Healthcare**.',
    'banking': 'Fictional company: **Harborstone Bank**.',
    'brokerage': 'Fictional company: **Ridgeline Securities**.',
    'oil': 'Fictional company: **Permian Ridge Energy**.',
    'pharma': 'Fictional company: **Novacrest Pharmaceuticals**.',
    'retail': 'Fictional company: **Maple & Main Stores**, the store division of Maple & Main.',
    'retail_supply_chain': 'Fictional company: **Maple & Main Supply Chain**, the Maple & Main division that buys, makes and stocks products (it combines the former Merchandising and Private Label divisions).',
    'retail_logistics': 'Fictional company: **Maple & Main Distribution**, the Maple & Main division that runs distribution centers, shipments and carriers.',
    'ecommerce': 'Fictional company: **Everyday Bazaar**, a high-volume online marketplace with tens of thousands of orders a year.',
}

ROOT=Path(__file__).resolve().parent
WORKSPACE=ROOT.parent.parent.parent
SOURCE=ROOT/'consolidated_supplements.json'
REPORT=ROOT/'CONSOLIDATION_REPORT.json'
SUPPLEMENT='<!-- CONSOLIDATED_UNIQUE_MATERIAL -->'


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def safe(path):
    path=path.resolve()
    if not path.is_relative_to(WORKSPACE.resolve()):raise ValueError(f'Outside workspace:{path}')
    if any(part in {'.git','.codex','.agents','.aws'} for part in path.parts):
        raise ValueError(f'Protected metadata is outside cleanup scope:{path}')
    return path
def put(path,text):
    safe(path);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text,encoding='utf-8')
def clean(text):return re.sub(r'\s+',' ',re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',text)).strip()
def html_data(path):
    text=path.read_text(encoding='utf-8');p=text.index('const DATA = ')+len('const DATA = ')
    return json.JSONDecoder().raw_decode(text[p:])[0]
def blocks(path):
    text=path.read_text(encoding='utf-8');matches=list(re.finditer(r'^### ([A-Z_]+-[BIA]\d{2}): ([^\n]+)\n',text,re.M));out={}
    for n,m in enumerate(matches):
        body=text[m.end():matches[n+1].start() if n+1<len(matches) else len(text)].strip()
        body=re.sub(r'\n## (?:Beginner|Intermediate|Advanced)\s*$','',body).strip()
        out[m[1]]=dict(id=m[1],title=m[2],body=body)
    return out


def capture():
    data=json.loads(SOURCE.read_text(encoding='utf-8')) if SOURCE.exists() else dict(healthcare=[],retail_draft=[],private_notes={})
    legacy=ROOT/'domains/healthcare/interview_ready'
    if not data['healthcare'] and legacy.exists():
        hp=ROOT/'domains/healthcare';student={r['id']:r for t in html_data(hp/'healthcare_sql_assignments.html') for r in t['items']}
        teacher={r['id']:r for t in html_data(hp/'healthcare_questions_answers.html') for r in t['items']}
        assert len(student)==480 and set(student)==set(teacher)
        for p in sorted((legacy/'questions').glob('*.md')):
            qs=blocks(p);answers=blocks(legacy/'solutions'/p.name)
            assert set(qs)==set(answers)
            for eid,q in qs.items():
                assert eid in student and eid in teacher
                # Keep original prose/SQL/explanations,plus HTML-only self-checks.
                data['healthcare'].append(dict(topic=p.stem,**q,answer=answers[eid]['body'],
                    self_check=(student[eid].get('a') or '').replace('\\n','\n')))
        assert len(data['healthcare'])==480
    oldbank=WORKSPACE/'interview-practice-bank/bank.json'
    if not data['retail_draft'] and oldbank.exists():
        data['retail_draft']=[q for q in json.loads(oldbank.read_text(encoding='utf-8'))['questions'] if q['subject']=='sql-server']
        assert len(data['retail_draft'])==6075
    # Retired domains (merged into retail_supply_chain on 2026-11-18) keep no private notes.
    for retired in ('retail_inventory','retail_manufacturing'):
        data['private_notes'].pop(retired,None)
    # Preserve private capstone notes and setup information once.
    for directory in (ROOT/'domains').iterdir():
        if not directory.is_dir() or not (directory/'questions/README.md').exists():continue
        notes=data['private_notes'].setdefault(directory.name,[])
        p=directory/'REPORTING_SOLUTIONS.md'
        if p.exists() and '## Capstone validation' in p.read_text(encoding='utf-8'):
            note=p.read_text(encoding='utf-8').split('## Capstone validation',1)[1].strip()
            if note not in notes:notes.append(note)
        project=directory/'README.md'
        if project.exists():
            text=project.read_text(encoding='utf-8')
            if '<!-- END_DOMAIN_INTERVIEW_ENTRY -->' in text:text=text.split('<!-- END_DOMAIN_INTERVIEW_ENTRY -->',1)[1]
            guide=(directory/'questions/DOMAIN_GUIDE.md').read_text(encoding='utf-8')
            existing={clean(b) for b in re.split(r'\n\s*\n',guide)}
            # A compact navigation page is not a historical project brief.
            if '## 6. Confidence checkpoint and capstone' in text:
                for b in re.split(r'\n\s*\n',text):
                    if b.strip() and clean(b) not in existing and not b.startswith('| Topic |'):
                        if b.strip() not in notes:notes.append(b.strip())
    put(SOURCE,json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    return data


def append_unique(path,text):
    old=path.read_text(encoding='utf-8') if path.exists() else '# '+path.stem.replace('_',' ')+'\n'
    old=old.split(SUPPLEMENT)[0].rstrip()
    put(path,old+'\n\n'+SUPPLEMENT+'\n\n'+text.strip()+'\n')


def merge(data):
    publish_review(put,data['healthcare'])
    groups=defaultdict(list)
    for q in data['healthcare']:groups[q['topic']].append(q)
    for topic,rows in groups.items():
        q=['## Selected AmeriMed applied practice','',
           'Selected cases supplement the assessed levelled bank. B/I/A in these older IDs are historical labels, not current difficulty ratings. [Practice route](BEST_EXERCISES.md). Historical self-checks use the large fixture and are outside the native report-validation claim. Use a fresh large-fixture practice copy for each case that changes data or permissions; changes persist.','']
        a=['## Selected AmeriMed applied answer key','',
           'Historical references require instructor review on the large fixture. These are not newly validated levelled references. [Selection audit](EXERCISE_SELECTION.md).','']
        for r in rows:
            if r['id'] not in KEPT_IDS:continue
            r=selected_case(r)
            q += [f'<a id="legacy-{r["id"].lower()}"></a>','',f'##### {r["id"]}: {r["title"]}','',r['body'],'']
            if r['self_check']:q += [r['self_check'],'']
            answer=r['answer']
            prefix='**Question:** '+r['body']
            if answer.startswith(prefix):answer=answer[len(prefix):].lstrip()
            a += [f'##### {r["id"]}: {r["title"]}','',f'[Question](../questions/{topic}.md)', '',answer,'']
        append_unique(ROOT/'domains/healthcare/questions'/f'{topic}.md','\n'.join(q))
        append_unique(ROOT/'domains/healthcare/solutions'/f'{topic}.md','\n'.join(a))
    groups=defaultdict(list)
    for r in data['retail_draft']:groups[r['topic']].append(r)
    refs=json.loads((ROOT/'curriculum.json').read_text(encoding='utf-8'));refindex={r['id']:r for r in refs}
    for topic,rows in groups.items():
        q=['## Retained earlier SQL draft exercises','',
           'Unique earlier draft contracts are consolidated here rather than kept in a second SQL bank. They supplement the15/15/15 levelled set;their new extensions were not supplied with complete validated solutions. Use the domain guide for table requirements.','']
        a=['## Earlier SQL draft: assessment notes','',
           'Core references below do not solve all draft extensions. Use the validated levelled set for scored query assessments.','']
        for r in rows:
            example=r['acceptance_example'].replace('fixtures/sqlserver_retail.sql','the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql)')
            q += [f'##### {r["id"]}','',r['core'],'','**Extension:** '+r['extension'],'','**Acceptance example:** '+example,'']
            core=refindex.get(r.get('legacy_core_id'),{})
            a += [f'##### {r["id"]}','',f'[Question](../questions/{topic}.md)','','**Assessment:** '+r['assessment'],'']
            if core.get('sql'):a += ['**Core reference only**','','```sql',core['sql'],'```','']
            if core.get('answer'):a += [core['answer'],'']
        append_unique(ROOT/'domains/retail/questions'/f'{topic}.md','\n'.join(q))
        append_unique(ROOT/'domains/retail/solutions'/f'{topic}.md','\n'.join(a))
    notes_by_text=defaultdict(list)
    for slug,notes in data['private_notes'].items():
        for note in notes:notes_by_text[note].append(slug)
    private=['# Preserved setup and capstone notes','',
             'Unique notes from the consolidated domain copies. File names refer to the selected domain.','']
    for note,slugs in notes_by_text.items():
        private += ['**Domains:** '+', '.join(sorted(set(slugs)))+'','',
                    re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',note),'']
    put(ROOT/'CONSOLIDATED_INSTRUCTOR_NOTES.md','\n'.join(private))
    # Published answers point to the question instead of repeating its text.
    for p in (ROOT/'domains').glob('*/solutions/*.md'):
        text=p.read_text(encoding='utf-8')
        text=re.sub(r'^#### ([A-Z_]+-[A-Z_]+-\d{2}-[BIA]\d{2})\n\n(\*\*[^\n]+\*\*)\n\n[\s\S]*?(?=\*\*Assessment model:\*\*)',
                    lambda m:f'#### {m[1]}\n\n{m[2]}\n\n[Canonical question](../questions/{p.name}#{m[1].lower()})\n\n',text,flags=re.M)
        text=re.sub(r'(\*\*Question\*\*\n\n)[\s\S]*?(\n\n\*\*Reference answer\*\*)',
                    lambda m:m[1]+f'[Canonical questions](../questions/{p.name})'+m[2],text)
        put(p,text)
    for slug in ('healthcare','retail'):
        for role in ('questions','solutions'):
            index=ROOT/'domains'/slug/role/'README.md'
            text=index.read_text(encoding='utf-8').split('<!-- CONSOLIDATED_NAV -->')[0].rstrip()
            if slug=='healthcare':
                target='BEST_EXERCISES.md' if role=='questions' else 'EXERCISE_SELECTION.md'
                text+=f'\n\n<!-- CONSOLIDATED_NAV -->\n## Healthcare and AmeriMed\n\nBoth names use this same bank. [Reviewed exercise selection]({target}). Selected older applied cases appear once in the matching topic files, including [Subqueries](SUBQUERIES.md). The full 5,940 levelled questions remain the assessed curriculum.\n'
            else:
                text+='\n\n<!-- CONSOLIDATED_NAV -->\n## Consolidated supplements\n\nThe earlier unique questions now appear in the matching topic files. [Subqueries](SUBQUERIES.md) is retained as an additional topic.\n'
            put(index,text)


def consolidate():
    data=capture();merge(data)
    old_report=json.loads(REPORT.read_text(encoding='utf-8')) if REPORT.exists() else dict(removed=[])
    removed={r['path']:r for r in old_report['removed']};mapping={};plans=[]
    def remove(path,target,why):
        if any(part in {'.git','.codex','.agents','.aws'} for part in path.parts):
            raise ValueError(f'Refusing to touch protected metadata:{path}')
        path=safe(path);target=safe(target)
        if path==target:return
        mapping[path]=target
        if path.is_file():plans.append((path,target,why))
    shared_student=list((ROOT/'domains').glob('*/questions/CODERPAD.md'))
    if shared_student:
        bodies=[p.read_text(encoding='utf-8').split('\n',1)[1] for p in shared_student]
        assert len(set(bodies))==1,'Domain-specific interview rules need merging before deletion'
        body=bodies[0].replace('(README.md)','(domains/README.md)').replace('(DOMAIN_GUIDE.md)','(domains/README.md)').replace('(INTERVIEW_CHALLENGES.md)','(domains/README.md)')
        put(ROOT/'CODERPAD.md','# SQL interview practice\n'+body)
    shared_teacher=list((ROOT/'domains').glob('*/solutions/INTERVIEW_GRADING.md'))
    if shared_teacher:
        bodies=[p.read_text(encoding='utf-8').split(SUPPLEMENT)[0].split('\n',1)[1] for p in shared_teacher]
        assert len(set(bodies))==1,'Domain-specific grading rules need merging before deletion'
        put(ROOT/'INTERVIEW_GRADING.md','# SQL interview grading\n'+bodies[0].replace('(README.md)','(solutions/README.md)')+'\n[Preserved setup and capstone notes](CONSOLIDATED_INSTRUCTOR_NOTES.md)\n')
    for directory in (ROOT/'domains').iterdir():
        if not directory.is_dir() or not (directory/'questions/README.md').exists():continue
        q=directory/'questions';a=directory/'solutions'
        remove(q/'BEGINNER_GUIDE.md',ROOT/'BEGINNER_GUIDE.md','Identical common guide')
        remove(q/'CODERPAD.md',ROOT/'CODERPAD.md','Common interview rules stored once')
        remove(a/'INTERVIEW_GRADING.md',ROOT/'INTERVIEW_GRADING.md','Common grading rules stored once;unique notes preserved')
        for old,target in [('REPORTING_ASSIGNMENTS.md',q/'REPORTING_ASSIGNMENTS.md'),('REPORTING_SOLUTIONS.md',a/'REPORTING_ASSIGNMENTS.md'),('ADVANCED_SOLUTIONS.md',a/'ADVANCED_QUERIES.md')]:
            p=directory/old
            if p.exists():
                src=p.read_text(encoding='utf-8');dst=target.read_text(encoding='utf-8')
                src_ids=set(re.findall(r'\b[A-Z_]+-(?:REPORT|ADV)-\d{2}\b',src));assert src_ids<=set(re.findall(r'\b[A-Z_]+-(?:REPORT|ADV)-\d{2}\b',dst))
                if 'SOLUTIONS' in old:
                    assert all(x.strip() in dst for x in re.findall(r'```sql\n(.*?)```',src,re.S)),p
            remove(p,target,'Merged report/answer copy;capstone notes retained privately')
        p=directory/'DATA_SETUP.md'
        if p.exists():
            text=p.read_text(encoding='utf-8');sql=re.search(r'```sql\n(.*?)```',text,re.S)
            assert sql and sql[1].strip()==(directory/'data_setup.sql').read_text(encoding='utf-8').strip(),p
        remove(p,q/'PRACTICE_DATA.md','Instructions retained once;embedded SQL already has data_setup.sql')
        # Keep a short entry index,not a second copy of the entire domain guide.
        put(directory/'README.md',f'# {directory.name.replace("_"," ").title()}\n\n{COMPANIES[directory.name]}\n\n[Student assignments](questions/README.md) · [Table definitions and sample rows](questions/DOMAIN_GUIDE.md) · [Instructor answers](solutions/README.md)\n\nSmall fixture: `schema_solution.sql` then `seed.sql`. Large fixture: `data_setup.sql`,in a separate empty practice database. [Large-data instructions](questions/PRACTICE_DATA.md).\n')
    # Combined books repeat IDs already published in individual domains.
    foundation=json.loads((ROOT/'curriculum.json').read_text(encoding='utf-8'))
    for topic in set(r['topic'] for r in foundation):
        for role,filename in [('questions',topic+'.md'),('solutions',topic+'_SOLUTIONS.md')]:
            path=ROOT/role/filename
            if path.exists():
                alltext='\n'.join((ROOT/'domains'/m['slug']/role/(topic+'.md')).read_text(encoding='utf-8') for m in json.loads((ROOT/'domain_models.json').read_text(encoding='utf-8')))
                wanted={r['id'] for r in foundation if r['topic']==topic}
                assert all(i in alltext for i in wanted),(path,'Missing retained IDs')
            remove(path,ROOT/('domains/README.md' if role=='questions' else 'solutions/README.md'),'Combined book repeats retained domain topic books')
    remove(ROOT/'questions/ADVANCED_QUERIES.md',ROOT/'domains/README.md','Redundant combined navigation')
    remove(ROOT/'solutions/ADVANCED_QUERIES_SOLUTIONS.md',ROOT/'solutions/README.md','Redundant combined navigation')
    legacy=ROOT/'domains/healthcare/interview_ready'
    for topic in {r['topic'] for r in data['healthcare']}:
        for role in ('questions','solutions'):
            remove(legacy/role/(topic+'.md'),ROOT/'domains/healthcare'/role/(topic+'.md'),'All480 unique healthcare IDs,answers and self-checks merged')
    for name in ('README.md','STUDENT_ASSIGNMENTS.md'):
        remove(legacy/name,ROOT/'domains/healthcare/questions/README.md','Combined healthcare handout merged into topic files')
    for name in ('healthcare_sql_assignments.html','healthcare_questions_answers.html'):
        remove(ROOT/'domains/healthcare'/name,ROOT/'domains/healthcare'/('solutions/README.md' if 'answers' in name else 'questions/README.md'),'HTML data merged into canonical topic files')
    standalone=WORKSPACE/'amerimed-healthcare-sql'
    if standalone.exists():
        public=[standalone/name for name in ('README.md','STUDENT_ASSIGNMENTS.md','index.html','data_setup.sql')]
        public += [standalone/'questions'/(topic+'.md') for topic in {r['topic'] for r in data['healthcare']}]
        for p in public:
            target=(ROOT/'domains/healthcare/data_setup.sql' if p.suffix=='.sql' else ROOT/'domains/healthcare/questions'/ (p.name if p.parent.name=='questions' else 'README.md'))
            if p.exists() and p.suffix=='.sql':assert sha(p)==sha(target),'Distinct standalone fixture must not be deleted'
            remove(p,target,'Standalone healthcare copy merged into canonical healthcare domain')
    # The earlier cross-subject SQL draft is merged into Retail;other subjects stay.
    broad=WORKSPACE/'interview-practice-bank'
    for p in (broad/'questions/sql-server').glob('*.md'):
        topic=p.stem.replace('-','_').upper();remove(p,ROOT/'domains/retail/questions'/f'{topic}.md','Unique SQL draft exercises merged into Retail')
    for p in [broad/'exports/sql-server-mixed.md',broad/'exports/sql-server-mixed.manifest.json',broad/'fixtures/sqlserver_retail.sql',broad/'fixtures/retail_contract.md',broad/'instructor/legacy_core_references.json']:
        remove(p,ROOT/'domains/retail/questions/README.md','Superseded SQL-only draft derivative')
    # Rewrite links against resolved old targets before removing anything.
    for file in [*ROOT.rglob('*.md'),*broad.glob('*.md'),WORKSPACE/'README.md']:
        if file.resolve() in mapping or not file.exists():continue
        text=file.read_text(encoding='utf-8')
        def link(match):
            label,url=match[1],match[2]
            if url.startswith(('https://','http://','#')):return match[0]
            base,sep,fragment=url.partition('#');target=(file.parent/base).resolve()
            if target not in mapping:return match[0]
            dest=mapping[target];new=os.path.relpath(dest,file.parent).replace('\\','/')
            return f'[{label}]({new}{sep+fragment if sep else ""})'
        changed=re.sub(r'\[([^]\n]+)\]\(([^)\n]+)\)',link,text)
        if changed!=text:put(file,changed)
    for source,target in mapping.items():
        if not source.exists() and target.exists():
            rel=str(source.relative_to(WORKSPACE)).replace('\\','/')
            removed.setdefault(rel,dict(path=rel,sha256=None,canonical=str(target.relative_to(WORKSPACE)).replace('\\','/'),reason='Consolidated destination verified;source already absent'))
    for path,target,why in plans:
        assert target.exists(),(path,'Missing merge destination',target)
        # Verify all imported unique blocks before removal of source copies.
        if 'interview_ready' in path.parts or path.is_relative_to(standalone):
            assert len(data['healthcare'])==480
        rel=str(path.relative_to(WORKSPACE)).replace('\\','/')
        removed[rel]=dict(path=rel,sha256=sha(path),canonical=str(target.relative_to(WORKSPACE)).replace('\\','/'),reason=why)
        put(REPORT,json.dumps(dict(removed=list(removed.values()),status='cleanup_in_progress'),indent=2)+'\n')
        path.unlink()
    # Remove only empty directories;never recursively remove a computed path.
    for parent in [legacy,standalone/'questions',ROOT/'questions',broad/'questions/sql-server']:
        if parent.exists():
            for d in sorted((p for p in parent.rglob('*') if p.is_dir()),key=lambda p:len(p.parts),reverse=True):
                safe(d)
                if not any(d.iterdir()):d.rmdir()
            if not any(parent.iterdir()):safe(parent).rmdir()
    # Retain the repository boundary and Git history,with one short pointer.
    if (standalone/'.git').is_dir():
        put(standalone/'README.md',amerimed_menu())
    report=dict(removed=list(removed.values()),removed_file_count=len(removed),
                healthcare_questions_preserved=480,earlier_sql_draft_questions_preserved=6075,
                healthcare_applied_cases_published=len(KEPT_IDS),healthcare_historical_cases_retired=480-len(KEPT_IDS),
                levelled_questions_unchanged=53460,scope='SQL assignments and their superseded published copies;other training subjects unchanged')
    report['git_metadata_repair_pending']=(standalone/'.git').exists() and not (standalone/'.git/HEAD').exists()
    put(REPORT,json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='removed'},indent=2))
    return report


if __name__=='__main__':consolidate()
