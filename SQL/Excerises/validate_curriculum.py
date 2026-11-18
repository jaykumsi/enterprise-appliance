"""Validate book structure and portable query semantics without a SQL Server engine.

SQLite checks are supplemental and explicitly do not validate T-SQL runtime behavior.
Run validate_syntax.ps1 for Microsoft's T-SQL grammar check.
"""
from collections import Counter
from pathlib import Path
import json
import re
import sqlite3

ROOT=Path(__file__).resolve().parent
ROWS=json.loads((ROOT/'curriculum.json').read_text(encoding='utf-8'))
MODELS=json.loads((ROOT/'domain_models.json').read_text(encoding='utf-8'))
REPORTS=json.loads((ROOT/'domain_reports.json').read_text(encoding='utf-8'))
EXPECTED_COUNTS={
    'INTRODUCTION':10,'DATABASE_SCHEMA_USER':3,'DATATYPES':26,'DDL':3,'CONSTRAINTS':5,
    'DML':3,'DATA_SETUP':2,'DQL':6,'OPERATORS':13,'SET_OPERATIONS':4,'JOINS':5,
    'STRING_FUNCTIONS':16,'DATE_FUNCTIONS':17,'AGGREGATES':5,'ANALYTICAL_FUNCTIONS':9,'CTE':5}
DOMAINS=[m['title'] for m in MODELS]

def structural():
    expected_total=sum(EXPECTED_COUNTS.values())*5*len(DOMAINS)
    assert len(ROWS)==expected_total
    assert len({r['id'] for r in ROWS})==expected_total
    assert set(r['topic'] for r in ROWS)==set(EXPECTED_COUNTS)
    for topic,count in EXPECTED_COUNTS.items():
        selected=[r for r in ROWS if r['topic']==topic]
        subs=set(r['subtopic'] for r in selected)
        assert len(subs)==count,(topic,len(subs))
        for sub in subs:
            group=[r for r in selected if r['subtopic']==sub]
            assert len(group)==5*len(DOMAINS)
            assert Counter(r['domain'] for r in group)=={d:5 for d in DOMAINS}
            assert all('day' not in r for r in group)
            assert len({r['prompt'] for r in group})==len(group)
            assert all(r['check'] and (r['sql'] or r['answer']) for r in group)
        for model in MODELS:
            q=(ROOT/'domains'/model['slug']/'questions'/f'{topic}.md').read_text(encoding='utf-8')
            a=(ROOT/'domains'/model['slug']/'solutions'/f'{topic}.md').read_text(encoding='utf-8')
            ids={r['id'] for r in selected if r['domain']==model['title']}
            assert ids<=set(re.findall(r'^### (\S+)',q,re.M)),(model['slug'],topic)
            assert ids<=set(re.findall(r'^### (\S+)',a,re.M)),(model['slug'],topic)
            assert not re.search(r'\bDay \d+\b',q+'\n'+a)
    readme=(ROOT/'source'/'README.md').read_text(encoding='utf-8-sig')
    linked=set(re.findall(r'\]\((sqlserver-[^)]+\.md)\)',readme))
    assert len(linked)==16
    assert all((ROOT/'source'/f).is_file() for f in linked)
    datatypes=(ROOT/'source'/'sqlserver-datatypes.md').read_text(encoding='utf-8-sig')
    named_types=set(re.findall(r'\* \*\*([A-Z][A-Z0-9]*(?:\(n\))?)\*\* -',datatypes))
    covered_types={r['subtopic'] for r in ROWS if r['topic']=='DATATYPES'}
    assert named_types==covered_types,(named_types-covered_types,covered_types-named_types)
    assert len(MODELS)==9
    for model in MODELS:
        assert len(model['tables'])>=5
        names={t['name'] for t in model['tables']}
        edges=set()
        for table in model['tables']:
            assert table['key'] in {c['name'] for c in table['columns']}
            for fk in table['fks']:
                assert fk['parent'] in names
                edges.add((table['name'],fk['parent']))
        seen={model['tables'][0]['name']}
        while True:
            expanded=seen|{b for a,b in edges if a in seen}|{a for a,b in edges if b in seen}
            if expanded==seen:break
            seen=expanded
        assert seen==names,(model['slug'],'disconnected model')
    for file in [ROOT/'README.md',ROOT/'COVERAGE.md',ROOT/'DATA_DICTIONARY.md',ROOT/'INSTRUCTOR_GUIDE.md',*ROOT.glob('questions/*.md'),*ROOT.glob('solutions/*.md'),*ROOT.glob('domains/**/*.md')]:
        prose=re.sub(r'```.*?```|`[^`]*`','',file.read_text(encoding='utf-8'),flags=re.S)
        for link in re.findall(r'\]\(([^)]+)\)',prose):
            if link.startswith(('http://','https://','#')): continue
            assert (file.parent/link.split('#')[0]).exists(),(file,link)

def load_fixture():
    con=sqlite3.connect(':memory:')
    con.create_function('YEAR',1,lambda x:int(str(x)[:4]))
    con.create_function('MONTH',1,lambda x:int(str(x)[4:6]))
    con.create_function('LEN',1,lambda x:None if x is None else len(str(x).rstrip(' ')))
    con.create_collation('Latin1_General_100_CI_AS',lambda a,b:(a.casefold()>b.casefold())-(a.casefold()<b.casefold()))
    setup=(ROOT/'setup'/'01_create_and_seed.sql').read_text(encoding='utf-8')
    for schema in [m['slug'] for m in MODELS]:
        con.execute(f"ATTACH DATABASE ':memory:' AS [{schema}]")
    inserts=re.findall(r'INSERT INTO (\[[^\]]+\]\.\[[^\]]+\]) \(([^)]+)\) VALUES\n(.*?);',setup,re.S)
    assert len(inserts)==sum(len(m['tables']) for m in MODELS)
    con.execute('PRAGMA foreign_keys=ON')
    for m in MODELS:
        for t in m['tables']:
            definitions=[f"[{c['name']}] {'NUMERIC' if c['type'].startswith(('int','decimal','bit')) else 'TEXT'} {c['rule']}" for c in t['columns']]
            definitions.append(f"PRIMARY KEY ([{t['key']}])")
            definitions += [f'UNIQUE ({u})' for u in t['unique']]
            definitions += [f'CHECK ({c})' for c in t['checks']]
            definitions += [f"FOREIGN KEY ([{f['column']}]) REFERENCES [{f['parent']}] ([{f['key']}])" for f in t['fks']]
            con.execute(f"CREATE TABLE [{m['slug']}].[{t['name']}] ("+','.join(definitions)+')')
    for tab,columns,values in inserts:
        con.execute(f'INSERT INTO {tab} ({columns}) VALUES '+re.sub(r"\bN(?=')",'',values))
    for m in MODELS:assert con.execute(f"PRAGMA [{m['slug']}].foreign_key_check").fetchall()==[]
    return con

def portable_queries():
    con=load_fixture()
    for model in MODELS:
        schema=model['slug'];fact,master,_=model['base'];mp=model['map']
        t=f'[{schema}].[{fact}]'; p=f'[{schema}].[{master}]'
        amt=mp['Amount'];qty=mp['Quantity'];cat=mp['Category'];fk=mp['PartyID']
        assert con.execute(f'SELECT COUNT(*),COUNT({amt}),SUM({amt}),SUM({qty}),MIN({amt}),MAX({amt}) FROM {t}').fetchone()==(12,11,1700,30,0,300)
        assert con.execute(f'SELECT {cat},SUM({amt}) FROM {t} GROUP BY {cat} ORDER BY {cat}').fetchall()==[('A',180),('B',520),('C',1000)]
        for join,n in [('INNER',12),('LEFT',13),('RIGHT',12),('FULL',13)]:
            # RIGHT here preserves the fact table, unlike the book's reversed RIGHT JOIN.
            assert con.execute(f'SELECT COUNT(*) FROM {p} p {join} JOIN {t} f ON p.{fk}=f.{fk}').fetchone()[0]==n
    supported={'DQL','OPERATORS','SET_OPERATIONS','JOINS','AGGREGATES','ANALYTICAL_FUNCTIONS','CTE'}
    outputs={}
    skipped=[]
    for row in ROWS:
        if row['topic'] not in supported: continue
        sql=row['sql']
        # These forms have intentionally different SQLite grammar/semantics.
        if re.search(r'\bTOP\b|\bDATEADD\b|CROSS JOIN \(VALUES',sql,re.I):
            skipped.append(row['id']); continue
        sql=re.sub(r"CONVERT\(date,'(\d{8})',112\)",r"'\1'",sql,flags=re.I)
        sql=re.sub(r'\s+OPTION \(MAXRECURSION 100\)','',sql,flags=re.I)
        sql=re.sub(r"\bN(?=')",'',sql)
        try:
            result=con.execute(sql).fetchall()
        except sqlite3.Error as error:
            raise AssertionError((row['id'],str(error),sql)) from error
        outputs[row['id']]=result
    # Independently specified representative result checks, including boundaries/ties.
    checks={
        'DQL-02-01':[(1,'Open'),(4,'Open'),(7,'Open'),(10,'Open')],
        'DQL-02-11':[(4,None)],
        'DQL-03-01':[('A',4),('B',4),('C',4)],
        'DQL-04-06':[('Closed',520),('Pending',1000)],
        'JOINS-01-16':[],
        'JOINS-02-16':[(5,None,None)],
        'JOINS-04-16':[(5,None,None)],
        'JOINS-05-16':[(60,)],
        'CTE-03-01':[(1,None,0),(2,1,1),(3,1,1),(4,2,2),(5,2,2),(6,3,2),(7,3,2),(8,4,3),(9,4,3),(10,5,3),(11,5,3),(12,6,3)],
        'CTE-04-11':[(200,3),(300,2)],
        'CTE-04-21':[(5,'Customers Unused')],
    }
    for eid,expected in checks.items():
        assert outputs[eid]==expected,(eid,outputs[eid],expected)
    domain_results={}
    for r in REPORTS:
        sql=re.sub(r'CONVERT\(date,d.DeliveredAt\)',"REPLACE(SUBSTR(d.DeliveredAt,1,10),'-','')",r['sql'],flags=re.I)
        domain_results[r['id']]=con.execute(sql).fetchall()
    for m in MODELS:
        prefix=m['slug'].upper()
        result=domain_results[prefix+'-REPORT-01']
        assert len(result)==5 and result[-1][-2:]==(0,None)
        assert sum(r[2] for r in result)==12
        assert sum(r[3] or 0 for r in result)==1700
        assert [r[0:2] for r in domain_results[prefix+'-REPORT-03']]==[(2,1),(3,2),(6,3),(9,4)]
    assert domain_results['RETAIL-REPORT-05'][0]==(1,100,100,100,0)
    assert domain_results['RETAIL-REPORT-05'][3]==(4,None,0,0,None)
    assert domain_results['BANKING-REPORT-05'][0]==(1,420,15000)
    assert sum(r[2] for r in domain_results['BANKING-REPORT-05'])==58000
    assert domain_results['PHARMA-REPORT-05'][0][-2:]==(100,50)
    assert sum(r[-1] for r in domain_results['PHARMA-REPORT-04'])==150
    assert domain_results['HEALTHCARE-REPORT-05'][0][-2:]==(100,2)
    assert domain_results['OIL-REPORT-05'][0][-3:]==(100,100,0)
    supply=domain_results['RETAIL_SUPPLY_CHAIN-REPORT-05']
    assert supply==[('PO-1','Canvas tote','Completed',10,30,30.5,3),('PO-2','Travel pouch','Completed',5,20,20,0),
                    ('PO-3','Canvas tote','InProgress',8,24,8,0),('PO-4','Travel pouch','Planned',6,24,0,0)]
    assert len(domain_results['RETAIL_SUPPLY_CHAIN-REPORT-04'])==12
    assert sum(r[3]=='Made' for r in domain_results['RETAIL_SUPPLY_CHAIN-REPORT-04'])==6
    assert [r[0] for r in domain_results['RETAIL_LOGISTICS-REPORT-05']]==[3]
    assert domain_results['RETAIL_LOGISTICS-REPORT-04'][-1][-2:]==(None,None)
    ledger=domain_results['RETAIL_SUPPLY_CHAIN-REPORT-06']
    assert len(ledger)==12 and all(r[-1]==0 for r in ledger)
    assert sum(r[2] for r in ledger)==120 and sum(r[-2] for r in ledger)==130
    assert sum(r[-1] for r in domain_results['ECOMMERCE-REPORT-04'])==850
    settle=domain_results['ECOMMERCE-REPORT-05']
    assert settle[0]==(1,100,100,100,0) and settle[3]==(4,None,0,0,None) and settle[4]==(5,50,50,0,50)
    assert domain_results['ECOMMERCE-REPORT-06'][-1]==(5,'Unused seller','Toys & Games',0,0,0)
    assert abs(sum(r[-1] for r in domain_results['BROKERAGE-REPORT-04'])-702.6)<0.000001
    assert abs(domain_results['BROKERAGE-REPORT-05'][0][-1]-100.6)<0.000001
    assert domain_results['BROKERAGE-REPORT-05'][1][2:4]==(1.5,0.5)
    assert domain_results['BROKERAGE-REPORT-05'][3][-1] is None
    assert all(r[3]>=0 for r in domain_results['BROKERAGE-REPORT-05'])
    # Execute invalid writes against the translated schema to independently check integrity.
    integrity_checks=0
    for m in MODELS:
        for t in m['tables']:
            qn=f"[{m['slug']}].[{t['name']}]";key=t['key']
            bads=[f'INSERT INTO {qn} SELECT * FROM {qn} WHERE {key}=1']
            required=next(c['name'] for c in t['columns'][1:] if c['rule'].startswith('NOT NULL'))
            bads.append(f'UPDATE {qn} SET {required}=NULL WHERE {key}=1')
            for f in t['fks']:bads.append(f"UPDATE {qn} SET {f['column']}=999 WHERE {key}=1")
            for sql in bads:
                con.execute('SAVEPOINT invalid_case')
                try:
                    con.execute(sql)
                except sqlite3.IntegrityError:integrity_checks+=1
                else:raise AssertionError(('invalid write accepted',sql))
                finally:
                    con.execute('ROLLBACK TO invalid_case');con.execute('RELEASE invalid_case')
    constraint_answers_checked=0
    for row in (r for r in ROWS if r['topic']=='CONSTRAINTS'):
        # Exercise the actual invalid DML from each answer, not a regenerated mutation.
        sql=re.search(r'BEGIN TRY\n ((?:UPDATE|INSERT).*?);\n THROW 51001',row['sql'],re.S)[1]
        sql=re.sub(r"\bN(?=')",'',sql)
        con.execute('SAVEPOINT answer_case')
        try:con.execute(sql)
        except sqlite3.IntegrityError:constraint_answers_checked+=1
        else:raise AssertionError(('constraint answer accepted invalid data',row['id'],sql))
        finally:
            con.execute('ROLLBACK TO answer_case');con.execute('RELEASE answer_case')
    report={'portableQueriesExecuted':len(outputs),'portableQueriesSkipped':len(skipped),
            'independentExactResultChecks':len(checks),'fixtureDomainsChecked':len(MODELS),
            'connectedTablesChecked':sum(len(m['tables']) for m in MODELS),'domainReportsExecuted':len(domain_results),'rejectedInvalidWrites':integrity_checks,
            'constraintAnswerMutationsRejected':constraint_answers_checked,
            'scope':'SQLite supplemental relational checks; not SQL Server runtime verification.',
            'translations':['map SQL Server schema types to SQLite affinities','remove Unicode literal N prefix','convert constant CONVERT(date,...,112) to fixture date text','convert logistics delivery date to comparable YYYYMMDD text','remove MAXRECURSION hint','register YEAR/MONTH and comparison collation'],
            'skippedForms':['TOP','DATEADD','CROSS JOIN VALUES alias'],
            'sqlServerRuntimeExecuted':False}
    (ROOT/'PORTABLE_VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    return report

if __name__=='__main__':
    structural()
    report=portable_queries()
    print(f'PASS: {len(ROWS):,} question/answer pairs; 132 subtopics; {sum(len(m['tables']) for m in MODELS)} connected tables; no day labels; source datatype coverage and local links.')
    print(json.dumps(report,indent=2))
