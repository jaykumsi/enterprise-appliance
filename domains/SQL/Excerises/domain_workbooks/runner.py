"""Run workbook answer SQL on a disposable LocalDB copy (WB_<domain>) and format the expected result.

Every item runs inside a transaction that is rolled back, so the practice data never changes.
Only databases named WB_<domain> (created by this tool from data_setup.sql) are ever used.
"""
import datetime, decimal, re, struct, subprocess
from pathlib import Path
import pyodbc

SERVER = r'(localdb)\MSSQLLocalDB'
ROOT = Path(__file__).resolve().parent.parent
import sys as _sys; _sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from company_paths import domain_dir, domain_dirs, DOMAINS_ROOT, ASSIGNMENTS_INDEX
NOTE = ('_Your query may be written differently and still be correct. Compare the number of rows and the values; '
        'if the question has no ORDER BY, your rows may come back in a different order._')
SHOWN = 6


def _dto(b):
    t = struct.unpack('<6hI2h', b)
    return '%04d-%02d-%02d %02d:%02d:%02d.%03d %+03d:%02d' % (t[0], t[1], t[2], t[3], t[4], t[5], t[6] // 1000000, t[7], abs(t[8]))


def connect(db):
    assert re.fullmatch(r'WB_[a-z_]+', db), db
    c = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={db};Trusted_Connection=yes', autocommit=True)
    c.add_output_converter(-155, _dto)
    c.timeout = 60
    return c


class Session:
    """A connection to WB_<domain> that can run state-changing scripts and restore the data afterwards."""

    def __init__(self, domain):
        self.domain, self.schema = domain, domain
        self.conn = connect('WB_' + domain)
        self.base = fingerprint(self.conn.cursor(), self.schema)

    def run(self, sql):
        res = execute(self.conn, sql)
        if res[0] == 'error' and '(3998)' in res[1]:
            # The script dooms an outer transaction (XACT_ABORT, THROW in a trigger, ...): run it for real, then reload.
            res = execute(self.conn, sql, wrap=False)
            self.restore(force=True)
        else:
            self.restore()
        return res

    def restore(self, force=False):
        if force or fingerprint(self.conn.cursor(), self.schema) != self.base:
            self.conn.close()
            reload(self.domain)
            self.conn = connect('WB_' + self.domain)


def reload(domain):
    """(Re)create WB_<domain> from the domain's canonical data_setup.sql."""
    db = 'WB_' + domain
    subprocess.run(['sqlcmd', '-S', SERVER, '-b', '-Q',
                    f"IF DB_ID('{db}') IS NOT NULL BEGIN ALTER DATABASE [{db}] SET SINGLE_USER WITH ROLLBACK IMMEDIATE; DROP DATABASE [{db}]; END; CREATE DATABASE [{db}];"],
                   check=True, capture_output=True)
    setup = domain_dir(domain) / 'data_setup.sql'
    subprocess.run(['sqlcmd', '-S', SERVER, '-d', db, '-b', '-i', str(setup)],
                   check=True, capture_output=True)


def fingerprint(cur, schema):
    cur.execute("SELECT COUNT(*) FROM sys.objects WHERE is_ms_shipped = 0")
    objs = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM sys.database_principals WHERE principal_id > 4 AND is_fixed_role = 0")
    users = cur.fetchone()[0]
    cur.execute(f"SELECT t.name, SUM(p.rows) FROM sys.tables t JOIN sys.partitions p ON p.object_id = t.object_id AND p.index_id IN (0,1) "
                f"WHERE SCHEMA_NAME(t.schema_id) = '{schema}' GROUP BY t.name ORDER BY t.name")
    return (objs, users, tuple(map(tuple, cur.fetchall())))


def fmt(v):
    if v is None:
        return 'NULL'
    if isinstance(v, bool):
        return '1' if v else '0'
    if isinstance(v, bytes):
        t = '0x' + v.hex().upper()
    elif isinstance(v, decimal.Decimal) and v == v.to_integral_value():
        t = str(int(v))
    else:
        t = str(v)
    t = re.sub(r'([\\`*_|])', lambda m: '\\' + m.group(1), t.replace('\n', ' '))
    if len(t) > 90:
        t = t[:87] + '\u2026'
    return t


def batches(sql):
    return [b for b in re.split(r'^\s*GO\s*;?\s*$', sql, flags=re.M | re.I) if b.strip()]


def execute(conn, sql, wrap=True):
    """Run sql in a rolled-back transaction. Returns ('rows', cols, rows) / ('none',) / ('error', msg)."""
    cur = conn.cursor()
    last = ('none',)
    try:
        cur.execute('SET XACT_ABORT OFF; BEGIN TRANSACTION;' if wrap else 'SET XACT_ABORT OFF;')
        for b in batches(sql):
            cur.execute(b)
            while True:
                if cur.description:
                    last = ('rows', [d[0] for d in cur.description], [tuple(r) for r in cur.fetchall()])
                if not cur.nextset():
                    break
    except pyodbc.Error as e:
        last = ('error', str(e))
    finally:
        try:
            cur.execute('IF @@TRANCOUNT > 0 ROLLBACK;')
        except pyodbc.Error:
            pass
        try:
            cur.execute('REVERT;')
        except pyodbc.Error:
            pass
    return last


def render(res):
    if res[0] == 'none':
        return '**Expected result:** the statement completes without returning rows.'
    if res[0] == 'error':
        raise RuntimeError(res[1])
    _, cols, rows = res
    n = len(rows)
    if n == 0:
        return '**Expected result:** 0 rows (an empty result is the correct answer here).\n\n' + NOTE
    head = f'**Expected result:** {n} row' + ('' if n == 1 else 's') + (f', first {SHOWN} shown' if n > SHOWN else '')
    t = '| ' + ' | '.join(c or '(No column name)' for c in cols) + ' |\n|' + '---|' * len(cols) + '\n'
    t += ''.join('| ' + ' | '.join(fmt(v) for v in r) + ' |\n' for r in rows[:SHOWN])
    return head + '\n\n' + t + '\n\n' + NOTE
