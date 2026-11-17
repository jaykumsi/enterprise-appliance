"""Generate larger, connected teaching fixtures without changing answer-key data."""
from pathlib import Path
import sqlite3
import json
import re

ROOT = Path(__file__).resolve().parent
MASTERS = {
    'retail': {'Customers', 'Products'},
    'banking': {'Branches', 'Customers', 'Accounts'},
    'pharma': {'Suppliers', 'Products', 'Warehouses'},
    'healthcare': {'Patients', 'Doctors', 'Medications'},
    'oil': {'Sites', 'Carriers', 'Products'},
    'retail_manufacturing': {'Products', 'Materials'},
    'retail_logistics': {'Customers', 'Carriers'},
    'retail_inventory': {'Warehouses', 'Products', 'Suppliers'},
    'brokerage': {'Clients', 'Securities', 'BrokerageAccounts'},
}


def expand(model):
    from realistic_data import build
    return build(model)


def validate(model):
    """Check actual rows against modeled constraints in a portable SQL engine."""
    db = sqlite3.connect(':memory:')
    db.execute('PRAGMA foreign_keys=ON')
    db.create_function('LEN', 1, lambda v: len(v.rstrip()) if v is not None else None)
    for table in model['tables']:
        columns = []
        for c in table['columns']:
            typ = 'INTEGER' if c['type'] in ('int', 'bit') else 'NUMERIC' if c['type'].startswith('decimal') else 'TEXT'
            columns.append(f'[{c["name"]}] {typ} {c["rule"]}')
        columns.append(f'PRIMARY KEY ([{table["key"]}])')
        columns += [f'UNIQUE ({u})' for u in table['unique']]
        columns += [f'CHECK ({c})' for c in table['checks']]
        columns += [f'FOREIGN KEY ([{f["column"]}]) REFERENCES [{f["parent"]}] ([{f["key"]}])' for f in table['fks']]
        db.execute(f'CREATE TABLE [{table["name"]}] (' + ','.join(columns) + ')')
        for row in table['rows']:
            for c, value in zip(table['columns'], row):
                size = re.fullmatch(r'n?varchar\((\d+)\)', c['type'])
                assert not size or value is None or len(value) <= int(size[1]), (table['name'], c['name'], value)
            db.execute(f'INSERT INTO [{table["name"]}] VALUES (' + ','.join('?' for _ in row) + ')', row)
        minimum = 50 if table['name'] in MASTERS[model['slug']] else 100
        assert len(table['rows']) >= minimum
    assert not db.execute('PRAGMA foreign_key_check').fetchall()
    db.close()


def generate(models):
    from domain_projects import ddl, insert, qname
    index = ['# Large teaching data setups', '',
             'SQL Server 2017+. Each domain has a ready-to-run setup matching its DDL Create exercises.', '',
             'Use a separate practice database for this larger dataset. Existing small seed files and answer-key totals still use the original sample rows.', '',
             'Each master has at least 50 rows and each transaction/detail table has at least 100 rows. All data is fictional: plausible people, product catalogs, locations and business activity, with varied dates, amounts and relationships. Financial values are illustrative, not market quotes. Related totals, quantities and dates are validated by the generator.', '',
             '| Domain | Setup instructions | Total rows |', '|---|---|---:|']
    report = []
    for original in models:
        model = expand(original)
        validate(model)
        slug = model['slug']
        directory = ROOT / 'domains' / slug
        counts = [(t['name'], 'Master' if t['name'] in MASTERS[slug] else 'Transaction / detail', len(t['rows'])) for t in model['tables']]
        body = ['-- Instructor setup: select your practice database before running.',
                '-- Fictional business data. Amounts are illustrative; timestamps are UTC.',
                '-- ' + model['fixture_notes'],
                '-- Creates missing tables; existing tables must match the original DDL and be empty.',
                '-- Stops on populated tables. Does not delete or overwrite existing data.',
                'SET NOCOUNT ON;', 'SET XACT_ABORT ON;',
                "IF @@TRANCOUNT <> 0 THROW 51000, 'Use a connection with no open transaction.', 1;",
                'BEGIN TRANSACTION;', 'BEGIN TRY',
                f"IF SCHEMA_ID(N'{slug}') IS NULL EXEC(N'CREATE SCHEMA [{slug}] AUTHORIZATION dbo;');"]
        for table in model['tables']:
            name = qname(model, table)
            body += [f"IF OBJECT_ID(N'{slug}.{table['name']}', N'U') IS NULL", 'BEGIN', ddl(model, table), 'END;',
                     f"IF EXISTS (SELECT 1 FROM {name}) THROW 51000, 'Tables must be empty. Use a fresh practice database.', 1;"]
        for table in model['tables']:
            body.append(f"-- {table['name']}: {len(table['rows'])} rows")
            # SQL Server limits INSERT ... VALUES to 1,000 row constructors.
            for start in range(0, len(table['rows']), 1000):
                body.append(insert(model, table, table['rows'][start:start + 1000]))
        for table in model['tables']:
            name = qname(model, table)
            body += [f"ALTER TABLE {name} WITH CHECK CHECK CONSTRAINT ALL;",
                     f"IF (SELECT COUNT(*) FROM {name}) <> {len(table['rows'])} THROW 51000, 'Unexpected row count.', 1;"]
        body += ['COMMIT TRANSACTION;', 'END TRY', 'BEGIN CATCH', 'IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;', 'THROW;', 'END CATCH;']
        body += ['\nUNION ALL\n'.join(f"SELECT N'{name}' AS TableName, COUNT(*) AS [RowCount] FROM [{slug}].[{name}]" for name, _, _ in counts) + ';']
        (directory / 'data_setup.sql').write_text('\n'.join(body) + '\n', encoding='utf-8')
        guide = [f'# {model["title"]}: large practice data', '',
                 '1. Select a new practice database in SQL Server Management Studio.',
                 '2. For CREATE practice, complete the Create section of DDL.md first. Leave the tables empty.',
                 '3. Ask your instructor to load the large dataset. The setup can also create any missing tables.',
                 '4. Check the row counts below, then practice SELECT, joins, GROUP BY, date functions and parent-child queries.', '',
                 'The setup stops if any domain table already contains rows. To repeat the lesson, use another empty practice database. Ask the instructor to reload after exercises that change data or tables.', '',
                 '| Table | Role | Rows |', '|---|---|---:|']
        guide += [f'| {name} | {role} | {count} |' for name, role, count in counts]
        guide += ['', 'Fictional, realistic business records with varied dates, quantities, prices and activity. Contact emails use example.com. Timestamps are UTC. Amounts are illustrative training values, not market quotes or clinical guidance.', '', model['fixture_notes'], '',
                  'This is an additional practice dataset. The small sample rows and fixed expected results in existing assignments still refer to the original dataset; totals and row counts will differ here.', '']
        (directory / 'questions' / 'PRACTICE_DATA.md').write_text('\n'.join(guide), encoding='utf-8')
        setup_guide = list(guide)
        setup_guide[0] = f'# {model["title"]}: data setup'
        setup_guide[4] = '3. Copy the complete SQL block below into SQL Server Management Studio and execute it. It creates missing tables and loads the data.'
        setup_guide += ['## Complete SQL setup', '',
                        'Run the entire block together. It loads parent tables first and checks row counts and constraints. You can also use the identical [SQL file](data_setup.sql).', '',
                        '```sql', '\n'.join(body), '```', '']
        (directory / 'DATA_SETUP.md').write_text('\n'.join(setup_guide), encoding='utf-8')
        index.append(f'| {model["title"]} | [{slug}](domains/{slug}/DATA_SETUP.md) | {sum(c for _, _, c in counts)} |')
        report.append({'domain': slug, 'tables': [{'name': n, 'role': r, 'rows': c} for n, r, c in counts]})
    (ROOT / 'LARGE_DATA_SETUP.md').write_text('\n'.join(index) + '\n', encoding='utf-8')
    (ROOT / 'LARGE_DATA_VALIDATION.json').write_text(json.dumps({'validation': 'Portable constraint, key, foreign-key, string-length, minimum-count and cross-table business consistency checks passed', 'sql_server_runtime_executed': False, 'domains': report}, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    from domain_projects import MODELS
    generate(MODELS)
