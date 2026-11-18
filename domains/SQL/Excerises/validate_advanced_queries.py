"""Supplemental SQLite checks; SQL Server runtime verification is separate."""
from datetime import datetime, timedelta
import json
import re

from advanced_queries import ROOT, exercises
from domain_projects import MODELS
from validate_curriculum import load_fixture


def parse_date(value):
    return datetime.strptime(str(value), '%Y%m%d')


def dateadd(unit, count, value):
    dt = parse_date(value)
    if unit == 'day':
        dt += timedelta(days=count)
    else:
        month = dt.year * 12 + dt.month - 1 + count
        dt = dt.replace(year=month // 12, month=month % 12 + 1)
    return dt.strftime('%Y%m%d')


def portable(sql):
    sql = re.sub(r"CAST\('(\d{8})' AS date\)", r"'\1'", sql)
    sql = re.sub(r'\b(DATEADD|DATEDIFF)\((day|month),', r"\1('\2',", sql)
    return re.sub(r'\s+OPTION \(MAXRECURSION 12\)', '', sql)


def validate():
    con = load_fixture()
    con.create_function('DATEADD', 3, dateadd)
    con.create_function('DATEDIFF', 3, lambda unit, start, end: (parse_date(end) - parse_date(start)).days)
    con.create_function('DATEFROMPARTS', 3, lambda y, m, d: f'{y:04d}{m:02d}{d:02d}')
    artifact = json.loads((ROOT / 'advanced_queries.json').read_text(encoding='utf-8'))
    generated = [r for m in MODELS for r in exercises(m)]
    assert artifact == generated
    for model in MODELS:
        rows = exercises(model)
        result = [con.execute(portable(row['sql'])).fetchall() for row in rows]
        monthly, streaks, ranks, rolling, coverage = result
        assert len(monthly) == 60
        assert sum(r[3] for r in monthly) == 11
        assert sum(r[5] or 0 for r in monthly) == 1500
        assert monthly[0][5:] == (300, None, None)
        assert monthly[1][5:] == (0, 300, -100.0)
        assert monthly[2][5:] == (0, 0, None)
        assert all(r[5] == 0 for r in monthly if r[0] == 5)
        assert [(r[0], *r[2:]) for r in streaks] == [
            (1, '20240101', '20240102', 2), (2, '20240102', '20240103', 2),
            (4, '20240229', '20240301', 2)]
        assert len(ranks) == 7
        assert [(r[0], r[1], r[3], r[4], r[5]) for r in ranks] == [
            ('A', 1, 100, 1, 180), ('A', 4, 80, 2, 180),
            ('B', 1, 320, 1, 520), ('B', 4, 150, 2, 520),
            ('C', 2, 400, 1, 1000), ('C', 3, 300, 2, 1000), ('C', 4, 300, 2, 1000)]
        assert [(r[0], r[4], r[5]) for r in rolling] == [(2, 1, 100), (6, 1, 50), (8, 1, 0), (9, 2, 75)]
        assert [(r[0], *r[2:]) for r in coverage] == [(4, 4, 4, 530)]
        mp = model['map']; fact = f'[{model["slug"]}].[{model["base"][0]}]'
        con.execute('SAVEPOINT edge_cases')
        # All-NULL month must differ from an empty month; same-day rows must
        # not extend a streak or enter the prior-days comparison.
        con.execute(f"UPDATE {fact} SET {mp['Amount']}=NULL WHERE {mp['PartyID']}=1")
        edge = con.execute(portable(rows[0]['sql'])).fetchall()
        assert edge[0][3:6] == (2, 0, None)
        assert edge[1][5:] == (0, None, None)
        con.execute(f"UPDATE {fact} SET {mp['EventDate']}='20240102' WHERE {mp['RecordID']}=11")
        edge = con.execute(portable(rows[1]['sql'])).fetchall()
        assert edge[0][2:] == ('20240101', '20240102', 2)
        con.execute(f"UPDATE {fact} SET {mp['Amount']}=0 WHERE {mp['Category']}='B'")
        edge = con.execute(portable(rows[2]['sql'])).fetchall()
        assert all(r[6] is None for r in edge if r[0] == 'B')
        con.execute('ROLLBACK TO edge_cases'); con.execute('RELEASE edge_cases')
    print('PASS: 45 advanced solutions across 9 domains; exact fixture results and NULL, zero and duplicate-date checks. SQLite supplemental checks only.')


if __name__ == '__main__':
    validate()
