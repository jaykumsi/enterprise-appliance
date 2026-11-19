"""Build one practice/assessment source of truth using Python stdlib only."""
from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from ladders import LADDERS
from subjects import SUBJECTS
from problem_variants import ALIASES, PROBLEMS

ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parent
LEVELS = [('Beginner', 'B'), ('Intermediate', 'I'), ('Advanced', 'A')]
PREFIX = dict(python='PY', postgresql='PG', java='JAVA', nodejs='NODE', web='WEB',
              aws='AWS', azure='AZ', gcp='GCP', snowflake='SNOW',
              **{'data-engineering': 'DE', 'sql-server': 'SQL'})
RUNTIMES = {
    'python': 'Python; language-level code with injected I/O where needed',
    'postgresql': 'PostgreSQL; native database exercises need a PostgreSQL runtime',
    'java': 'Java; Spring/JPA tasks need configured dependencies or a framework-free service-boundary model',
    'nodejs': 'JavaScript/TypeScript on Node.js; inject databases and HTTP clients',
    'web': 'Browser/React for UI tasks; a code-only pad can assess the state model but cannot verify rendering/accessibility',
    'data-engineering': 'Python reference model; PySpark/Parquet/Airflow native checks need their respective runtimes',
    'aws': 'Local Python/Java/JavaScript model; native Athena query tasks need Athena or a declared compatible dialect',
    'azure': 'Local Python/Java/JavaScript model; native SQL/Spark tasks need their respective runtime',
    'gcp': 'Local Python/Java/JavaScript model; BigQuery/Spark native tasks need their respective runtime',
    'snowflake': 'Native Snowflake for SQL; Python/Java/JavaScript for explicitly described local models',
    'sql-server': 'Native SQL Server; T-SQL and engine-specific types are not directly executable in a PostgreSQL pad',
}
PORTABLE_FIXTURE = '''-- Fresh scratch database only. Portable relational practice fixture.
CREATE TABLE Customers(CustomerID INTEGER PRIMARY KEY, CustomerName VARCHAR(80) NOT NULL, Region VARCHAR(10) NOT NULL);
CREATE TABLE Orders(OrderID INTEGER PRIMARY KEY, CustomerID INTEGER NOT NULL REFERENCES Customers(CustomerID), AmountCents INTEGER NULL, Status VARCHAR(10) NOT NULL, CreatedAt VARCHAR(30) NOT NULL);
INSERT INTO Customers VALUES (1,'Ada','North'),(2,'Ben','South'),(3,'Cy','North'),(4,'Dee','West');
INSERT INTO Orders VALUES
(1,1,100,'Open','2024-01-01T00:00:00Z'),
(2,1,100,'Closed','2024-01-02T00:00:00Z'),
(3,2,200,'Open','2024-01-02T00:00:00Z'),
(4,2,NULL,'Pending','2024-01-03T00:00:00Z'),
(5,3,0,'Open','2024-02-01T00:00:00Z');
'''

INTRO_CORES = [
    ('Relational database fundamentals', 'Orders repeat a customer address on every row. Given o1:c1/OldRoad and o2:c1/NewRoad,design Customers and Orders with a stable CustomerID and write SQL that updates one current address without rewriting historical order IDs. Demonstrate which conflicting address needs an explicit migration decision.'),
    ('Structured Data Storage and Control', 'A staging batch contains (id=a,qty=2,date=2024-02-29),(id=b,qty=-1,date=2024-02-30). Design typed target columns and validation SQL separating valid rows from rejected rows with field reasons. Do not silently fix the invalid quantity or date.'),
    ('Advanced Querying and Data Operations', 'Using retail.Orders and retail.Customers from the SQL Server fixture,return CustomerID,order count and known OrderTotal sum for every customer including zero-order customers. Keep an all-unknown sum distinct from zero; order by CustomerID.'),
    ('Security and Regulatory Support', 'Design a local order access check for authenticated users: customer sees own orders,authenticated support sees only masked customer names,unauthenticated sees none. Given customer c1 and order belonging c2,return denial. Provide SQL/view boundaries plus a test showing raw names cannot leak through an alternate query path.'),
    ('Performance and Scalability', 'A workload retrieves one CustomerID in an OrderDate range sorted by OrderDate,OrderID. Propose an index over retail.Orders and an actual-plan experiment over a reproducible expanded fixture. Verify all returned IDs match an unoptimized reference; never invent a timing result.'),
    ('Analytics and Business Intelligence', 'Using retail.Orders,calculate monthly known OrderTotal sums in 2024 and reconcile their total with an independent full-year sum. Use half-open date boundaries and return months in ascending order. Explain missing-month output with an explicit calendar if adding zero rows.'),
    ('Transactional Workloads', 'Model placing an order and its two order items. A rejected second item must not leave an apparently complete order. Return an explicit operation-state trace and database postcondition queries; use a local simulator if transaction syntax is not yet taught.'),
    ('Data Warehousing and BI', 'Given one fact order o1 for100 and two customer dimension versions,c1-v1 and c1-v2,write an enrichment that selects the correct effective version rather than doubling the fact. Supply half-open validity intervals and reconcile fact count and amount.'),
    ('Digital Content Management', 'Model document revisions (doc,version,checksum,current). A new current revision must preserve old content; two competing updates based on the same old current cannot both win. Implement a local version-precondition model and show one conflict.'),
    ('Enterprise Applications', 'Model inventory A:1 and two simultaneous reservation requests for one unit each. Implement a state transition guaranteeing one success and stock never negative. Provide an interleaving showing why separate read-then-write is unsafe.'),
]


def slug(text):
    return re.sub(r'[^A-Z0-9]+', '-', text.upper()).strip('-')


def sql_course():
    records = json.loads((WORKSPACE / 'domains/SQL/Excerises/curriculum.json').read_text(encoding='utf-8'))
    groups = defaultdict(list)
    for r in records:
        if r['domain'] == 'Retail':
            groups[(r['topic'], r['subtopic'])].append(r)
    rows, references = [], {}
    for (topic, subtopic), anchors in groups.items():
        anchors.sort(key=lambda r: r['id'])
        sid = anchors[0]['id'].split('-')[1]
        family = ('design' if topic in {'INTRODUCTION', 'DATATYPES'} else
                  'mutation' if topic in {'DDL', 'DML', 'CONSTRAINTS', 'DATA_SETUP', 'DATABASE_SCHEMA_USER'} else 'query')
        if topic == 'INTRODUCTION':
            core = dict(INTRO_CORES)[subtopic]
            choices = [dict(core=core, legacy_id=None)]
        else:
            choices = [dict(core=re.sub(r'\[[^\]]+\]\(\.\./domains/retail/README\.md\)',
                                       'the Retail table contract supplied with this question',r['prompt']),
                            legacy_id=r['id']) for r in anchors]
        # Database/principal work has different privilege requirements from row mutations.
        if topic == 'DATABASE_SCHEMA_USER':
            family = 'design'
            definitions = {
                'Database': 'Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.',
                'Schema': 'In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.',
                'User': 'In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.',
            }
            choices = [dict(core=definitions[subtopic], legacy_id=None)]
        # Type exercises remain native demonstrations. CURSOR is an iteration
        # construct, not a persistent user-table column type.
        if topic == 'DATATYPES' and subtopic == 'CURSOR':
            choices = [dict(core='Using a SQL Server local forward-only read-only cursor,iterate retail.Orders in OrderID order and accumulate count and known OrderTotal sum while ignoring unknown totals. Return count,sum and visited IDs. CLOSE and DEALLOCATE on success and failure; compare totals with a set-based reference. Do not define CURSOR as a persistent table-column type.', legacy_id=None)]
        example='Use fixtures/sqlserver_retail.sql and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.'
        if topic=='DDL' and subtopic=='Create':
            example='Use a fresh scratch database. The target table initially does not exist; after creation it is empty and its metadata must match every supplied column/key/constraint requirement. Create required parent tables first. Do not preload the solved setup.'
        elif topic=='DATA_SETUP':
            example='Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.'
        rows.append(dict(topic=topic, subtopic=subtopic, family=family,
                         source_id=f'{topic}-{sid}', choices=choices,
                         example=example))
        for r in anchors:
            references[r['id']] = {k: r.get(k, '') for k in ('id','prompt','sql','answer','check')}
    # Explicit subquery coverage from the healthcare interview bank, with one
    # canonical relational fixture instead of a second set of domain copies.
    extras = [
        ('Scalar subqueries', 'Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.'),
        ('Correlated subqueries', 'Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer\'s average known total. Sort by OrderID; retain ties only if they strictly exceed the average.'),
        ('Existence and relational division', 'Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.'),
    ]
    for i, (subtopic, core) in enumerate(extras, 1):
        rows.append(dict(topic='SUBQUERIES', subtopic=subtopic, family='query',
                         source_id=f'SUBQUERIES-{i:02d}', choices=[dict(core=core,legacy_id=None)],
                         example='Use fixtures/sqlserver_retail.sql. For an empty required-product set,all five fixture customers qualify.'))
    return dict(name='SQL Server', source='Existing domains/SQL/Excerises/curriculum.json: all 132 original subtopics; explicit subquery extensions from healthcare interview coverage.', rows=rows), references


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')


def fixture_for(subject, row):
    if subject == 'sql-server':
        return 'fixtures/sqlserver_retail.sql'
    if 'fixture Orders' in row['core'] or 'fixture Customers' in row['core']:
        return 'fixtures/portable.sql'
    return 'inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O'


def main():
    # SQL is published only in each company's domains/<company>/sql folder.
    courses = dict(SUBJECTS)
    bank = dict(schema_version=1, title='Interview practice and assessment bank',
                levels=[x[0] for x in LEVELS], questions_per_subtopic_per_level=15,
                review_status='structurally validated; selected native/runtime exercises require instructor execution before use',
                subjects={}, questions=[])
    coverage, progress, books = [], [], defaultdict(list)
    for subject, course in courses.items():
        bank['subjects'][subject] = {k: course[k] for k in ('name','source')}
        topic_ordinals = Counter()
        for row in course['rows']:
            topic = row['topic']
            topic_ordinals[topic] += 1
            ordinal = topic_ordinals[topic]
            sub_id = f'{PREFIX[subject]}-{slug(topic)}-{ordinal:02d}'
            fixtures = fixture_for(subject, row)
            coverage.append(dict(subject=subject,topic=topic,subtopic=row['subtopic'],subtopic_id=sub_id,
                                 Beginner=15,Intermediate=15,Advanced=15,total=45,
                                 family=row['family'],source=course['source'],legacy_subtopic=row.get('source_id','')))
            for level, code in LEVELS:
                progress.append(dict(student='',subject=subject,topic=topic,subtopic=row['subtopic'],level=level,
                                     assigned=15,attempted=0,independently_correct=0,timed_correct=0,
                                     mean_score='',mock_score='',next_action='',evidence_ids=''))
                for index, extension in enumerate(LADDERS[row['family']][level], 1):
                    example=row['example']
                    if 'choices' in row:
                        anchor = row['choices'][(index-1) % len(row['choices'])]
                        core, legacy_id = anchor['core'], anchor['legacy_id']
                    elif row['family']=='code' and row['subtopic'] in ALIASES:
                        variant=PROBLEMS[ALIASES[row['subtopic']]][index-1]
                        core,example,legacy_id=variant['core'],variant['example'],None
                    else:
                        core, legacy_id = row['core'], None
                    qid = f'{sub_id}-{code}{index:02d}'
                    q = dict(id=qid,subject=subject,subject_name=course['name'],topic=topic,
                             subtopic=row['subtopic'],subtopic_id=sub_id,level=level,
                             core=core,extension=extension,acceptance_example=example,
                             fixture=fixtures,runtime=RUNTIMES[subject],family=row['family'],
                             legacy_core_id=legacy_id,
                             timebox_minutes={'Beginner':15,'Intermediate':30,'Advanced':45}[level],
                             assessment='Run implementation against independently derived expected outputs; grade extension as well as core. See instructor/ASSESSMENT.md.',
                             native_execution_verified=False)
                    bank['questions'].append(q)
                    books[(subject, topic)].append(q)
    for (subject, topic), questions in books.items():
        lines = [f'# {courses[subject]["name"]}: {topic}', '',
                 '[Master index](../../catalog.md)', '',
                 'Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.', '',
                 'Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.', '',
                 f'Runtime: {RUNTIMES[subject]}.', '',
                 'For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.', '']
        current_sub = current_level = None
        for q in questions:
            if q['subtopic'] != current_sub:
                current_sub, current_level = q['subtopic'], None
                lines += [f'## {current_sub}', '']
            if q['level'] != current_level:
                current_level = q['level']
                lines += [f'### {current_level}', '']
            lines += [f'#### {q["id"]}', '', f'**Core:** {q["core"]}', '',
                      f'**Acceptance example / fixture:** {q["acceptance_example"]}', '',
                      f'**Question:** {q["extension"]}', '',
                      f'Fixture: `{q["fixture"]}`. Suggested time: {q["timebox_minutes"]} minutes.', '']
        write(ROOT / 'questions' / subject / f'{slug(topic).lower()}.md', '\n'.join(lines))
    fixtures = ROOT / 'fixtures'
    write(fixtures / 'portable.sql', PORTABLE_FIXTURE)
    write(ROOT/'bank.json', json.dumps(bank,ensure_ascii=False,indent=2)+'\n')
    for filename, rows in [('coverage.csv',coverage),('progress.csv',progress)]:
        with (ROOT/filename).open('w',encoding='utf-8',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    lines=['# Master question index','',f'{len(courses)} subjects/shared tracks · {len(coverage)} subtopics · {len(bank["questions"]):,} questions. Every subtopic has 15 questions at each of three levels.','',
           'SQL is maintained once in [the domain assignments](../domains/SQL/Excerises/DOMAIN_ASSIGNMENTS.md).\n\nRead [Student guide](STUDENT_GUIDE.md),[track mapping](TRACKS.md),[CoderPad instructions](CODERPAD.md) and [validation limits](VALIDATION.md).','',
           '| Subject | Subtopics | Beginner | Intermediate | Advanced | Total |','|---|---:|---:|---:|---:|---:|']
    for subject,course in courses.items():
        count=len(course['rows'])
        lines.append(f'| {course["name"]} | {count} | {count*15} | {count*15} | {count*15} | {count*45} |')
    for subject,course in courses.items():
        lines += ['',f'## {course["name"]}','',course['source'],'',
                  '| Topic book | Subtopic | B | I | A |','|---|---|---:|---:|---:|']
        for c in coverage:
            if c['subject']==subject:
                link=f'questions/{subject}/{slug(c["topic"]).lower()}.md'
                lines.append(f'| [{c["topic"]}]({link}) | {c["subtopic"]} | 15 | 15 | 15 |')
    write(ROOT/'catalog.md','\n'.join(lines)+'\n')
    print(json.dumps(dict(subjects=len(courses),subtopics=len(coverage),questions=len(bank['questions']),
                          topic_books=len(books),bank_sha256=hashlib.sha256((ROOT/'bank.json').read_bytes()).hexdigest()),indent=2))


if __name__ == '__main__':
    main()
