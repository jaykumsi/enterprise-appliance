"""Check question/schema consistency without connecting to a database."""
import json
import re
from pathlib import Path

from domain_projects import MODELS
from domain_question_wording import QUERY_TOPICS, clarify_question

ROOT = Path(__file__).resolve().parent
import sys as _sys; _sys.path.insert(0, str(Path(__file__).resolve().parent))
from company_paths import domain_dir, domain_dirs, DOMAINS_ROOT, ASSIGNMENTS_INDEX


def validate():
    rows = json.loads((ROOT / 'curriculum.json').read_text(encoding='utf-8'))
    models = {m['title']: m for m in MODELS}
    checked = 0
    for model in MODELS:
        directory = domain_dir(model['slug'])
        schema = (directory / 'schema_solution.sql').read_text(encoding='utf-8')
        ddl = (directory / 'questions' / 'DDL.md').read_text(encoding='utf-8')
        guide = (directory / 'questions' / 'DOMAIN_GUIDE.md').read_text(encoding='utf-8')
        for table in model['tables']:
            qname = f'[{model["slug"]}].[{table["name"]}]'
            block = schema.split(f'CREATE TABLE {qname} (', 1)[1].split('\n);', 1)[0]
            declared = re.findall(r'^    \[([^]]+)\] (.+),$', block, re.M)
            expected = [(c['name'], c['type'] + ' ' + c['rule']) for c in table['columns']]
            assert declared == expected, (qname, 'schema differs from model')
            question = ddl.split(f'Create the `{qname}` table with these columns:', 1)[1].split('Add these constraints:', 1)[0]
            columns = re.findall(r'^\| (\w+) \| ([^|]+) \| ([^|]+) \|$', question, re.M)[1:]
            assert [c[0] for c in columns] == [c[0] for c in expected], qname
            for column, (name, declaration) in zip(columns, expected):
                assert column[1].strip() == declaration.split(' ', 1)[0], (qname, name)
                assert column[2].strip().split(';')[0] == declaration.split(' ', 1)[1], (qname, name)
            section = guide.split(f'### {table["name"]}\n', 1)[1].split('\n### ', 1)[0]
            for c in table['columns']:
                assert f'| {c["name"]} | {c["type"]} | {c["rule"]} |' in section, (qname, c['name'])
    for row in rows:
        if row['topic'] not in QUERY_TOPICS:
            continue
        model = models[row['domain']]
        assert clarify_question(row, model) == row['prompt'], row['id']
        prose = re.sub(r'`[^`]*`', '', row['prompt'])
        assert not re.search(r'\b(category|categories|party|parties|label|labels|quantity|amounts?|record IDs?)\b', prose), row['id']
        for path in (domain_dir(model['slug']) / 'questions' / f'{row["topic"]}.md',):
            assert row['prompt'] in path.read_text(encoding='utf-8'), (row['id'], path)
        if 'Source columns:' in row['prompt']:
            inputs = re.findall(r'`(\w+)`', row['prompt'].split('Source columns:', 1)[1].split('.', 1)[0])
            fact = next(t for t in model['tables'] if t['name'] == model['base'][0])
            assert set(inputs) <= {c['name'] for c in fact['columns']}, row['id']
        checked += 1
    print(f'PASS: {checked} query questions across {len(MODELS)} domains; 45 table definitions; question copies and source columns agree.')


if __name__ == '__main__':
    validate()
