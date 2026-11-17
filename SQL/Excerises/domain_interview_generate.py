"""Generate 15 questions per level for all132 subtopics in each domain.

Foundation IDs/files remain intact. New domain-prefixed IDs identify the
complete levelled contracts;assessment exports reuse those exact contracts.
"""
from collections import Counter,defaultdict
import csv
import hashlib
import json
from pathlib import Path
import re

from domain_interview_focus import QUERY_TOPICS
from domain_interview_queries import instantiate,recipes
from domain_interview_labs import extension

ROOT=Path(__file__).resolve().parent
MARKER='<!-- DOMAIN_LEVELLED_INTERVIEW_START -->'
LEVELS=[('Beginner','B'),('Intermediate','I'),('Advanced','A')]


def write(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(text,encoding='utf-8')


def logical_core(row,model):
    text=row['prompt']
    text=re.sub(r'\]\(\.\./domains/[^/]+/README\.md\)','](DOMAIN_GUIDE.md)',text)
    if row['topic']=='INTRODUCTION':
        text=(f'Use `[{model["slug"]}].[{model["base"][0]}]` and `[{model["slug"]}].[{model["base"][1]}]` to demonstrate {row["subtopic"].lower()} through a concrete failure and a corrected native/local implementation. '
              'Use at least two rows with distinct stable keys. Return the failure outcome,the corrected outcome and an assertion proving the business rule. Definition lists alone do not satisfy this task.')
    return text


def prompt_query(model,subtopic,item,recipe):
    mp=model['map'];pk,fk=mp['RecordID'],mp['PartyID']
    task=recipe['task'] if item['task']=='DOMAIN_SPECIFIC' else item['task']
    # State the business invariant,not the intended implementation strategy.
    if recipe['level']=='Advanced':
        task=task.replace('do not join transactions and loans before aggregating.','each transaction and each loan must contribute exactly once.')
        task=task.replace('Aggregate repeated usage at order/material grain first;include usage outside the recipe.','Repeated usage records are additive;include usage outside the recipe.')
        task=task.replace('Pre-aggregate execution rows before testing each order for overfill;','An overfilled order counts once even when it has multiple executions;')
    return '\n\n'.join([
        f'**Analysis population — {subtopic}:** {item["focus_rule"]}',
        f'**Task:** {task}',
        '**Required results:** Return two result sets. First,an analysis audit with '+
        f'`{pk}`,`{fk}`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `{pk}`. '+
        f'The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `{mp["Category"]}` for the representative source ID. '+
        'Second,return the business report with these exact columns: '+', '.join('`'+x+'`' for x in item['output'])+'. '+
        '`MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.',
        '**Final report order:** '+item['sort']+'.',
        '**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.',
        '**Rules that will be tested:** '+item['edge'],
        '**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. '+
        'Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. '+
        ('For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.' if recipe['level']=='Advanced' else 'Use the small baseline first;the same contract must work on the large practice data.'),
        'Source columns: '+item['source_columns']+'.'
    ])


def prompt_lab(model,row,level,n,lab):
    core=logical_core(row,model)
    return '\n\n'.join([
        '**Core task:** '+core,
        '**Interview case:** '+lab['task'],
        '**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). '+
        'For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.',
        '**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. '+
        'No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.',
        '**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. '+
        'An explanation without the concrete case,implementation and observed evidence is incomplete.'
    ])


def generate(models,records):
    all_recipes=recipes();assert Counter(r['level'] for r in all_recipes)==dict(Beginner=15,Intermediate=15,Advanced=15)
    expected_path=ROOT/'DOMAIN_INTERVIEW_EXPECTED.json'
    expected={}
    native_path=ROOT/'DOMAIN_INTERVIEW_NATIVE_VALIDATION.json'
    native=json.loads(native_path.read_text(encoding='utf-8')) if native_path.exists() else {}
    fresh_native=bool(native.get('full_expected_result_comparison')) and all(
        (ROOT/name).exists() and hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
        for name,digest in native.get('reference_source_sha256',{}).items()) and bool(native.get('reference_source_sha256'))
    if expected_path.exists() and fresh_native:
        for x in json.loads(expected_path.read_text(encoding='utf-8')):
            expected[(x['domain'],x['topic'],x['subtopic'],x['level'],x['number'])]=x
    coverage=[];question_count=0;query_count=0;domain_index=['# SQL assignments by domain','',
        'This is the canonical SQL interview-practice entry point. Each of the nine domains retains all132 syllabus subtopics. Every subtopic has15 Beginner,15 Intermediate and15 Advanced questions. Existing foundation IDs remain available in the topic books.','',
        '**Levelled questions:53,460.** They are domain/subtopic-specific compositions,not53,460 unrelated interview algorithms. Advanced analytical questions use15 demanding business-report patterns with subtopic-specific analysis rules. Schema/type/security labs use15 different practical failure/migration scenarios.','',
        '| Domain | Subtopics | Beginner | Intermediate | Advanced | Student assignments |','|---|---:|---:|---:|---:|---|']
    bankpath=ROOT/'domain_interview_questions.jsonl'
    with bankpath.open('w',encoding='utf-8',newline='\n') as bank:
        for model in models:
            s=model['slug'];directory=ROOT/'domains'/s;student=directory/'questions';teacher=directory/'solutions'
            by_topic=defaultdict(lambda:defaultdict(list))
            for r in records:
                if r['domain']==model['title']:by_topic[r['topic']][r['subtopic']].append(r)
            assert sum(map(len,by_topic.values()))==132
            index=[f'# {model["title"]}: assignments and interview practice','',
                   '**132 subtopics ×(15 Beginner +15 Intermediate +15 Advanced) =5,940 levelled questions.** Existing660 foundation exercises are retained in the same topic books.','',
                   '[Table definitions and sample data](DOMAIN_GUIDE.md) · [Practice instructions](BEGINNER_GUIDE.md) · [Large dataset](PRACTICE_DATA.md) · [Timed interview rules](CODERPAD.md) · [Hard challenge sampler](INTERVIEW_CHALLENGES.md) · [Hard mock](HARD_MOCK.md) · [Mixed mock](MIXED_MOCK.md)','',
                   'Start with Beginner in each subtopic. Intermediate combines concepts. Advanced requires multi-stage reasoning and adversarial edge cases;the question does not prescribe the solving algorithm.','',
                   '| Topic | Subtopics | Beginner | Intermediate | Advanced | Earlier foundations |','|---|---:|---:|---:|---:|---:|']
            tindex=[f'# {model["title"]}: instructor index','',
                    'Question IDs and filenames match the student copy. Query references have an independently checked small-fixture result artifact when native validation has completed. Practical labs include a core reference and an explicit grading model;their open-ended extensions are not falsely labelled as32,400 automatically tested SQL solutions.','',
                    '| Student topic | Instructor answers | Levelled | Foundations |','|---|---|---:|---:|']
            domain_rows=[]
            for topic,subs in by_topic.items():
                qpath=student/f'{topic}.md';apath=teacher/f'{topic}.md'
                foundation_q=qpath.read_text(encoding='utf-8').split(MARKER)[0].rstrip()
                foundation_a=apath.read_text(encoding='utf-8').split(MARKER)[0].rstrip()
                qlines=[foundation_q,'',MARKER,'','## Levelled interview practice','',
                        'Each subtopic below has15 questions per level. Each ID identifies the complete task,analysis rule or core case,and edge conditions. The earlier questions retain their original IDs as foundation practice.','']
                alines=[foundation_a,'',MARKER,'','## Levelled interview answers','',
                        'Keep answers private. For query tasks,grade both analysis audit and report. Expected small-fixture rows are stored in `DOMAIN_INTERVIEW_EXPECTED.json`;large-data outputs differ. For practical labs,the reference core alone does not solve the new case:require the listed case-specific evidence and rubric.','']
                first_id=None
                for sid,(sub,anchors) in enumerate(subs.items(),1):
                    anchors.sort(key=lambda x:x['id'])
                    qlines += [f'### {sub}: progression',''];alines += [f'### {sub}: progression','']
                    for level,code in LEVELS:
                        qlines += [f'**{level}:15 questions**',''];alines += [f'**{level}:15 questions**','']
                        for n in range(1,16):
                            eid=f'{s.upper()}-{topic}-{sid:02d}-{code}{n:02d}'
                            if first_id is None:first_id=eid
                            anchor=anchors[(n-1)%len(anchors)]
                            if topic in QUERY_TOPICS:
                                recipe=next(r for j,r in enumerate([x for x in all_recipes if x['level']==level],1) if j==n)
                                item=instantiate(model,topic,sub,recipe)
                                prompt=prompt_query(model,sub,item,recipe);title=recipe['title'];query_count+=1
                                reference=dict(kind='runnable_query',sql=item['sql'],witness_sql=item['witness_sql'])
                                answer='The two result sets must match complete values,nulls,multiplicity and required ordering. '+item['edge']
                            else:
                                lab=extension(level,n-1);prompt=prompt_lab(model,anchor,level,n,lab);title=lab['title']
                                reference=dict(kind='practical_lab_rubric',sql=anchor.get('sql',''),core_model=anchor.get('answer',''))
                                answer=lab['rubric']+' Core checkpoint: '+anchor['check']
                            row=dict(id=eid,domain=s,topic=topic,subtopic=sub,level=level,number=n,title=title,
                                     prompt=prompt,reference=reference,grading=answer,legacy_core_id=anchor['id'],
                                     timebox_minutes={'Beginner':15,'Intermediate':30,'Advanced':60}[level])
                            bank.write(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n')
                            domain_rows.append({k:v for k,v in row.items() if k not in {'reference'}})
                            question_count+=1
                            qlines += [f'#### {eid}','',f'**{title}** · {level} · Suggested coding time:{row["timebox_minutes"]} minutes','',prompt,'']
                            teacher_prompt=prompt.replace('](DOMAIN_GUIDE.md)','](../questions/DOMAIN_GUIDE.md)').replace('](BEGINNER_GUIDE.md)','](../questions/BEGINNER_GUIDE.md)')
                            alines += [f'#### {eid}','',f'**{title}**','',f'[Canonical question](../questions/{topic}.md#{eid.lower()})','','**Assessment model:** '+answer,'']
                            if reference['kind']=='runnable_query':
                                alines += ['**Analysis audit reference**','', '```sql',reference['witness_sql'],'```','', '**Business report reference**','', '```sql',reference['sql'],'```','']
                                check=expected.get((s,topic,sub,level,n))
                                if check:
                                    alines += [f'**Small-fixture expected report:** {check["row_count"]} rows. First five rows (decimal/date values are serialized as text):','',
                                               '```json',json.dumps(check['expected_rows'][:5],ensure_ascii=False),'```','']
                            else:
                                alines += [f'**Core reference:** Find `{anchor["id"]}` in this topic\'s earlier foundation answers. Also require the case-specific evidence above.','']
                    coverage.append(dict(domain=s,topic=topic,subtopic=sub,subtopic_index=sid,Beginner=15,Intermediate=15,Advanced=15,foundations=len(anchors),first_id=f'{s.upper()}-{topic}-{sid:02d}-B01'))
                write(qpath,'\n'.join(qlines)+'\n');write(apath,'\n'.join(alines)+'\n')
                k=len(subs);index.append(f'| [{topic.replace("_"," ")}]({topic}.md#{first_id.lower()}) | {k} | {15*k} | {15*k} | {15*k} | {5*k} |')
                tindex.append(f'| [{topic}](../questions/{topic}.md) | [Answers]({topic}.md) | {45*k} | {5*k} |')
            index += ['','## Additional practice','',
                      '- [Domain reporting assignments](REPORTING_ASSIGNMENTS.md):6 earlier integration tasks.',
                      '- [Earlier advanced bridge exercises](ADVANCED_QUERIES.md):5 retained IDs;use the Advanced levelled questions for the new hard standard.',
                      '- [Extra substring practice](SUBSTRING_PRACTICE.md):12 focused drills.','',
                      'The132 subtopics are unchanged. Shared student guides are maintained once at the curriculum root. Share student materials with access to those guides;keep instructor files private.','']
            tindex += ['', '[Timed interview grading](INTERVIEW_GRADING.md) · [Native validation report](../../../DOMAIN_INTERVIEW_NATIVE_VALIDATION.json)','']
            write(student/'README.md','\n'.join(index));write(teacher/'README.md','\n'.join(tindex))
            write(student/'CODERPAD.md',student_guide(model))
            write(teacher/'INTERVIEW_GRADING.md',teacher_guide(model))
            write(student/'INTERVIEW_CHALLENGES.md',sampler(model,domain_rows))
            project=directory/'README.md'
            text=project.read_text(encoding='utf-8')
            project_marker='<!-- DOMAIN_INTERVIEW_ENTRY -->'
            if text.startswith(project_marker):text=text.split('<!-- END_DOMAIN_INTERVIEW_ENTRY -->',1)[1].lstrip()
            notice=f'{project_marker}\n**Start with the [levelled {model["title"]} assignments](questions/README.md):132 subtopics,15 Beginner +15 Intermediate +15 Advanced per subtopic.** The project brief below supplies the schema and earlier foundation path.\n<!-- END_DOMAIN_INTERVIEW_ENTRY -->\n\n'
            write(project,notice+text)
            domain_index.append(f'| {model["title"]} |132|1980|1980|1980|[Open assignments]({s}/questions/README.md)|')
            print(f'Generated {s}:5,940 levelled questions across132 subtopics',flush=True)
    assert question_count==53460 and query_count==32400
    with (ROOT/'DOMAIN_INTERVIEW_COVERAGE.csv').open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(coverage[0]));writer.writeheader();writer.writerows(coverage)
    write(ROOT/'domains/README.md','\n'.join(domain_index)+'\n')
    shared=ROOT/'COVERAGE.md'
    previous=shared.read_text(encoding='utf-8').split(MARKER)[0].rstrip()
    write(shared,previous+'\n\n'+MARKER+'\n\n## Domain interview progression\n\nAll132 original subtopics are retained in every domain. Each domain/subtopic pair has15 Beginner,15 Intermediate and15 Advanced questions:53,460 levelled questions,plus the5,940 earlier foundation exercises. The levelled set contains32,400 runnable query references and21,060 practical lab cases with core references and grading models.\n\nSee [domain assignments](domains/README.md) and `DOMAIN_INTERVIEW_COVERAGE.csv` for the exact per-subtopic counts. Timed mocks reuse existing IDs and are not additional counted questions.\n')
    from export_domain_interview import generate_mocks
    generate_mocks(models)
    from consolidate_sql_materials import consolidate
    consolidate()
    return dict(levelled_questions=question_count,runnable_query_references=query_count,
                practical_lab_rubrics=question_count-query_count,domain_subtopic_pairs=len(coverage))


def sampler(model,rows):
    # One real question from each distinct hard report pattern. These are
    # references to canonical records,not additional counted questions.
    preferred=[('DQL','Select'),('ANALYTICAL_FUNCTIONS','LAG()'),('AGGREGATES','Sum'),('DATE_FUNCTIONS','Timezones'),
               ('DQL','Where'),('CTE','Recursive CTEs'),('CTE','Creating a CTE'),('JOINS','Left Join'),
               ('AGGREGATES','Sum'),('DATE_FUNCTIONS','Date Part Function (DATEPART)'),('SET_OPERATIONS','Union'),
               ('OPERATORS','IN Operator'),('CTE','Recursive CTEs'),('ANALYTICAL_FUNCTIONS','LAG()'),('JOINS','Left Join')]
    lines=[f'# {model["title"]}: hard interview sampler','',
           'These are15 existing Advanced question IDs from the full bank,not extra questions. Each links to the exact assignment used for practice and interview export.','',
           '| Question | Focus | Challenge |','|---|---|---|']
    for n,(topic,sub) in enumerate(preferred,1):
        q=next(q for q in rows if q['topic']==topic and q['subtopic']==sub and q['level']=='Advanced' and q['number']==n)
        lines.append(f'| [{q["id"]}]({topic}.md#{q["id"].lower()}) | {sub} | {q["title"]} |')
    lines += ['', 'For a hard mock,select two different challenge patterns and allow120 minutes coding plus20 minutes discussion. Do not select the same pattern under two different subtopics and call it an unseen test. An instructor may supply a new independently checked fixture while keeping the contract unchanged.','', '[All assignments](README.md) · [Interview rules](CODERPAD.md)','']
    return '\n'.join(lines)


def student_guide(model):
    return f'''# {model['title']}: live SQL interview practice

Use the same question ID and complete task from the topic book. The analysis population,outputs,ordering and edge rules are part of the question;do not copy only its title.

1. Explain the input grain and output grain before coding.
2. Derive the query without opening solutions. The prompt names the result,not the solving algorithm.
3. Run the small fixture and independent boundary cases,then the large dataset.
4. Explain nulls,ties,duplicates,calendar boundaries and one-to-many joins.
5. Debug an interviewer-supplied counterexample and defend correctness/scaling.

Suggested time per question:Beginner15,Intermediate30,Advanced60 minutes. Setup happens before the timer. These are practice targets,not course deadlines.

For query tasks,submit both the analysis audit and the business report. For schema/type/security/DML labs,submit implementation,actual before/after evidence and the requested disposition/assertion tables. A vague design paragraph does not pass.

Use native SQL Server2017+ for these T-SQL assignments. A PostgreSQL/MySQL pad requires a deliberate dialect adaptation and new runtime checks;changing the editor language does not translate SQL. Cloud accounts are not required. No CoderPad upload has been performed.

CoderPad lets organizations prepare their own questions;there is no universal company-independent “CoderPad difficulty formula.” This course uses a live-coding format with explicit contracts,adversarial cases and consistent grading. See [CoderPad example questions](https://coderpad.io/resources/docs/interview/question-bank/example-questions/) and [database setup](https://coderpad.io/resources/docs/interview/databases/).

A suggested progression gate is12/15 independently correct per level/subtopic,including8 timed attempts and no unresolved correctness failure. After completing the assigned track,pass two different mixed-topic mocks at80/100 or higher. These are proposed training gates,not an employment or interview-outcome guarantee.

[Assignment index](README.md) · [Schema and sample rows](DOMAIN_GUIDE.md) · [Hard sampler](INTERVIEW_CHALLENGES.md)
'''


def teacher_guide(model):
    return f'''# {model['title']}: interview grading

Use canonical IDs from the student topic books. `domain_interview_questions.jsonl` at the curriculum root is the export source,including private references. Never distribute that file or this solutions folder.

Query questions have two result sets. Grade the analysis audit first,then compare the complete report against the independent expected artifact. Never accept only matching row counts or grand totals. The generated preview displays at most five expected rows;the complete expected rows are in DOMAIN_INTERVIEW_EXPECTED.json and native execution evidence is in DOMAIN_INTERVIEW_NATIVE_VALIDATION.json.

Respect the numeric contract:counts,IDs and exact totals must agree;means,medians,percentages and weighted prices allow absolute difference0.000003. The Python oracle's mathematical expected values may contain more fractional digits than the SQL reference's displayed decimals. Do not compare serialized numeric strings as text.

Practical labs use the core SQL/model reference plus a case-specific rubric. These are open native/design demonstrations,not fully enumerated automated solutions. Require concrete inputs,before/after state,precise rejection/acceptance and assertions. Review the chosen case before administering it. A copied core without the new case cannot pass.

| Criterion | Points |
|---|---:|
| Analysis/core contract and business report/case correctness |45|
| Adversarial cases and complete result comparison |25|
| Algorithm,query grain and scaling argument |15|
| Explanation and debugging |10|
| Clear SQL and exact output contract |5|

A wrong monetary total,split cutoff tie,phantom activity row,wrong time boundary,unbounded cycle,tenant/scope leak or lost/duplicated accepted effect blocks a pass until corrected. Accept equivalent SQL;do not require the reference method.

Advanced patterns deliberately recur under different subtopic transformations and domains. Select different patterns for a mixed mock;repeating a memorized pattern with a renamed column is not independent readiness evidence. Include a new independently calculated adversarial fixture and require the candidate to repair one plausible wrong shortcut.

Native validation covers the runnable query references and explicit adversarial populations recorded in the report. It does not mean all open-ended lab extensions have been independently executed or every possible submitted solution is automatically graded.

[Instructor index](README.md)
'''


if __name__=='__main__':
    from domain_projects import MODELS
    print(generate(MODELS,json.loads((ROOT/'curriculum.json').read_text(encoding='utf-8'))))
