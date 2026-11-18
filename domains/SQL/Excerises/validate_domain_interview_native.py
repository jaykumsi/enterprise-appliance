"""Native read-only query validation in one explicitly owned disposable database.

The only persistent write is creating/seeding this new validation database.
Existing unmarked databases are never overwritten or reset.
"""
import argparse
from collections import Counter
from datetime import date,datetime
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import pyodbc
from domain_interview_focus import QUERY_TOPICS
from domain_interview_queries import recipes,instantiate

ROOT=Path(__file__).resolve().parent
DATABASE='Tinitiate_DomainInterview_20261118_v2'  # v2: Retail Supply Chain and E-commerce replace Retail Inventory/Manufacturing
MARKER='TinitiateDomainInterviewValidation_v1'


def encode(value):
    if isinstance(value,Decimal):return str(value)
    if isinstance(value,(date,datetime)):return value.isoformat()
    if isinstance(value,bytes):return value.hex()
    raise TypeError(type(value).__name__)


def connection():
    base=r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=(localdb)\MSSQLLocalDB;Trusted_Connection=yes;Encrypt=no;TrustServerCertificate=yes;'
    master=pyodbc.connect(base+'DATABASE=master;',autocommit=True,timeout=10)
    cursor=master.cursor()
    exists=cursor.execute('SELECT DB_ID(?)',DATABASE).fetchone()[0] is not None
    if not exists:
        cursor.execute('CREATE DATABASE ['+DATABASE+']')
    master.close()
    con=pyodbc.connect(base+'DATABASE='+DATABASE+';',autocommit=True,timeout=10)
    cur=con.cursor();cur.execute('SET NOCOUNT ON; SET DATEFIRST 7;')
    marker=cur.execute("SELECT CAST(value AS nvarchar(100)) FROM sys.extended_properties WHERE class=0 AND name=?",MARKER).fetchone()
    if exists and (not marker or marker[0]!=MARKER):
        raise RuntimeError('Refusing to reuse an existing database without the exact validation ownership marker.')
    if not exists:
        setup=(ROOT/'setup/01_create_and_seed.sql').read_text(encoding='utf-8')
        for batch in re.split(r'^\s*GO\s*$',setup,flags=re.M|re.I):
            if batch.strip():cur.execute(batch)
        cur.execute('EXEC sys.sp_addextendedproperty @name=?,@value=?',MARKER,MARKER)
    return con


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--full',action='store_true',help='Run every levelled query against the independent Python oracle.')
    args=parser.parse_args()
    reference_hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in
        ('domain_interview_focus.py','domain_interview_queries.py','domain_interview_reconciliation.py',
         'domain_interview_oracle.py','domain_interview_domain_oracle.py','domain_interview_edge_tests.py')}
    models=json.loads((ROOT/'domain_models.json').read_text(encoding='utf-8'))
    records=json.loads((ROOT/'curriculum.json').read_text(encoding='utf-8'))
    topics=list(dict.fromkeys((r['topic'],r['subtopic']) for r in records if r['topic'] in QUERY_TOPICS))
    con=connection();cur=con.cursor()
    failures=[];focus_rows=[];executed=0
    for model in models:
        for topic,subtopic in topics:
            item=instantiate(model,topic,subtopic,recipes()[0])
            label=f'{model["slug"]}/{topic}/{subtopic}'
            try:
                data=[list(row) for row in cur.execute(item['witness_sql']).fetchall()]
                focus_rows.append(dict(domain=model['slug'],topic=topic,subtopic=subtopic,rows=data))
                executed+=1
            except Exception as exc:
                failures.append(dict(id=label,phase='analysis_population',error=str(exc)))
        for n,recipe in enumerate(recipes(),1):
            if model['slug']!='retail' and n!=45:continue
            item=instantiate(model,'DQL','Select',recipe)
            try:
                data=[list(row) for row in cur.execute(item['sql']).fetchall()]
                executed+=1
            except Exception as exc:
                failures.append(dict(id=f'{model["slug"]}/{recipe["level"]}/{recipe["title"]}',phase='report_smoke',error=str(exc)))
        print(f'Native smoke: {model["slug"]},failures={len(failures)}',flush=True)
    (ROOT/'DOMAIN_INTERVIEW_FOCUS_RESULTS.json').write_text(json.dumps(focus_rows,default=encode,indent=2)+'\n',encoding='utf-8')
    report=dict(database=DATABASE,engine='SQL Server LocalDB',phase='native_smoke',
                executed_queries=executed,analysis_populations=len(focus_rows),errors=failures,
                reference_source_sha256=reference_hashes,
                full_expected_result_comparison=False)
    if args.full and not failures:
        from domain_interview_oracle import validate_all
        report.update(validate_all(con,models,topics,focus_rows))
    (ROOT/'DOMAIN_INTERVIEW_NATIVE_VALIDATION.json').write_text(json.dumps(report,default=encode,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='errors'},default=encode,indent=2))
    for error in report.get('errors',[]):print(json.dumps(error))
    if report.get('errors'):raise SystemExit(1)


if __name__=='__main__':main()
