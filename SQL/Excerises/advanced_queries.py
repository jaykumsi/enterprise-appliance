"""Generate advanced SQL Server exercises from the verified domain schemas."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def exercises(model):
    mp = model['map']
    fact, master, name = model['base']
    f = f'[{model["slug"]}].[{fact}]'
    p = f'[{model["slug"]}].[{master}]'
    key, fk, amount, category, date = (mp[k] for k in ('RecordID', 'PartyID', 'Amount', 'Category', 'EventDate'))
    items = [
        ('Monthly activity with missing months and growth',
         f'For every `{p}` row, return all twelve months of 2024, including months with no `{fact}` rows. '
         f'Use `{date}` for month boundaries and `{amount}` for totals. Return `{fk}`, `{name}`, MonthStart, EventCount, '
         'KnownValueCount, TotalValue, PreviousMonthValue and GrowthPercent. A month with no rows has total zero; '
         'a month containing only unknown values has total NULL. Sum known values for mixed months. '
         'Growth is 100 * (current - previous) / previous; return NULL when either total is unknown, '
         'there is no previous month, or the previous total is zero. Partition LAG by the master key. '
         f'Use a calendar CTE and order by `{fk}`, MonthStart.',
         f""";WITH Months AS (
    SELECT CAST('20240101' AS date) AS MonthStart
    UNION ALL
    SELECT DATEADD(month, 1, MonthStart)
    FROM Months WHERE MonthStart < CAST('20241201' AS date)
), Activity AS (
    SELECT {fk}, DATEFROMPARTS(YEAR({date}), MONTH({date}), 1) AS MonthStart,
           COUNT(*) AS EventCount, COUNT({amount}) AS KnownValueCount,
           SUM({amount}) AS TotalValue
    FROM {f}
    WHERE {date} >= '20240101' AND {date} < '20250101'
    GROUP BY {fk}, DATEFROMPARTS(YEAR({date}), MONTH({date}), 1)
), Filled AS (
    SELECT p.{fk}, p.{name}, m.MonthStart,
           COALESCE(a.EventCount, 0) AS EventCount,
           COALESCE(a.KnownValueCount, 0) AS KnownValueCount,
           CASE WHEN a.EventCount IS NULL THEN 0 ELSE a.TotalValue END AS TotalValue
    FROM {p} p CROSS JOIN Months m
    LEFT JOIN Activity a ON a.{fk} = p.{fk} AND a.MonthStart = m.MonthStart
), Compared AS (
    SELECT *, LAG(TotalValue) OVER (PARTITION BY {fk} ORDER BY MonthStart) AS PreviousMonthValue
    FROM Filled
)
SELECT *, 100.0 * (TotalValue - PreviousMonthValue) / NULLIF(PreviousMonthValue, 0) AS GrowthPercent
FROM Compared
ORDER BY {fk}, MonthStart
OPTION (MAXRECURSION 12);""",
         'Small fixture: 60 rows, 11 events in 2024, total known value 1500. Master 5 has twelve zero totals. Master 1 January total is 300; February growth is -100%; March growth is NULL because February was zero.'),
        ('Consecutive active-date streaks',
         f'Find consecutive calendar-date streaks per `{fk}` in `{f}` using `{date}`. '
         'Deduplicate same-day activity before using ROW_NUMBER and a gaps-and-islands grouping key. '
         f'Return `{fk}`, `{name}`, StreakStart, StreakEnd and ActiveDays for streaks of at least two days. '
         'Multiple rows on one date count as one active day. NULL monetary values still count as activity. '
         f'Order by `{fk}`, StreakStart.',
         f""";WITH ActiveDates AS (
    SELECT DISTINCT {fk}, {date} FROM {f}
), Numbered AS (
    SELECT {fk}, {date},
           DATEDIFF(day, '20000101', {date})
           - ROW_NUMBER() OVER (PARTITION BY {fk} ORDER BY {date}) AS IslandKey
    FROM ActiveDates
), Streaks AS (
    SELECT {fk}, MIN({date}) AS StreakStart, MAX({date}) AS StreakEnd, COUNT(*) AS ActiveDays
    FROM Numbered GROUP BY {fk}, IslandKey HAVING COUNT(*) >= 2
)
SELECT s.{fk}, p.{name}, s.StreakStart, s.StreakEnd, s.ActiveDays
FROM Streaks s JOIN {p} p ON p.{fk} = s.{fk}
ORDER BY s.{fk}, s.StreakStart;""",
         'Small fixture: three two-day streaks: master 1 Jan 1–2; master 2 Jan 2–3; master 4 Feb 29–Mar 1. Master 4 Mar 10 and master 2 Jan 1, 2025 are isolated, so they are excluded.'),
        ('Top contributors with ties and category share',
         f'Aggregate known `{amount}` by `{category}` and `{fk}` in `{f}`, join `{p}` for `{name}`, '
         'then return the top two distinct total-value ranks per category using DENSE_RANK. Include every tie. '
         'Calculate each master’s percentage of the complete category total before filtering ranks. '
         'Exclude groups with no known values; keep known zero totals. Return CategoryTotal and SharePercent '
         f'alongside `{category}`, `{fk}`, `{name}`, TotalValue and ValueRank. Use NULL percentage for zero category totals. '
         f'Order by `{category}`, ValueRank, `{fk}`.',
         f""";WITH Totals AS (
    SELECT {category}, {fk}, SUM({amount}) AS TotalValue
    FROM {f} GROUP BY {category}, {fk} HAVING COUNT({amount}) > 0
), Ranked AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY {category} ORDER BY TotalValue DESC) AS ValueRank,
           SUM(TotalValue) OVER (PARTITION BY {category}) AS CategoryTotal
    FROM Totals
)
SELECT r.{category}, r.{fk}, p.{name}, r.TotalValue, r.ValueRank, r.CategoryTotal,
       100.0 * r.TotalValue / NULLIF(r.CategoryTotal, 0) AS SharePercent
FROM Ranked r JOIN {p} p ON p.{fk} = r.{fk}
WHERE r.ValueRank <= 2
ORDER BY r.{category}, r.ValueRank, r.{fk};""",
         'Small fixture: 7 rows. Category A total=180, B=520, C=1000. Category C includes both masters tied at rank 2. In B, master 1 total=320 and master 4 total=150; their shares use denominator 520, including the filtered-out master 3 total of 50.'),
        ('Trailing 30-calendar-day comparison',
         f'For every `{f}` row, compute the average known `{amount}` for the same `{fk}` '
         f'over dates from `{date}` minus 30 days inclusive to `{date}` exclusive. Exclude all same-day rows, '
         'not just the current row. Include the count of prior known values. Return only rows whose current value '
         f'is strictly more than 1.5 times that average. Return `{key}`, `{fk}`, `{date}`, `{amount}`, '
         'PriorKnownCount and PriorAverage. Use a self join and grouped CTE; preserve decimal arithmetic. '
         f'Order by `{fk}`, `{date}`, `{key}`. Explain why ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING would answer a different question.',
         f""";WITH History AS (
    SELECT currentRow.{key}, COUNT(priorRow.{amount}) AS PriorKnownCount,
           AVG(CAST(priorRow.{amount} AS decimal(19,4))) AS PriorAverage
    FROM {f} currentRow
    LEFT JOIN {f} priorRow ON priorRow.{fk} = currentRow.{fk}
        AND priorRow.{date} >= DATEADD(day, -30, currentRow.{date})
        AND priorRow.{date} < currentRow.{date}
    GROUP BY currentRow.{key}
)
SELECT f.{key}, f.{fk}, f.{date}, f.{amount}, h.PriorKnownCount, h.PriorAverage
FROM {f} f JOIN History h ON h.{key} = f.{key}
WHERE h.PriorKnownCount > 0 AND f.{amount} > 1.5 * h.PriorAverage
ORDER BY f.{fk}, f.{date}, f.{key};""",
         'Small fixture: event IDs 2, 6, 8 and 9 qualify. Prior averages are 100, 50, 0 and 75 respectively. A known zero average is valid; missing history is not.'),
        ('Masters covering every required category',
         f'Find `{p}` rows with at least one `{f}` row in each required `{category}` value A, B and C '
         f'during 2024, based on `{date}`. Use a required-category CTE and nested NOT EXISTS (relational division). '
         f'Count activity regardless of whether `{amount}` is NULL. Separately aggregate 2024 activity and join it '
         f'to the qualifying masters. Return `{fk}`, `{name}`, EventCount, KnownValueCount and TotalValue. '
         'Sum only known values; retain NULL if all values are unknown. Avoid multiplying rows by the required-category list. '
         f'Order by `{fk}`.',
         f""";WITH RequiredTypes AS (
    SELECT 'A' AS RequiredType UNION ALL SELECT 'B' UNION ALL SELECT 'C'
), YearActivity AS (
    SELECT * FROM {f} WHERE {date} >= '20240101' AND {date} < '20250101'
), Totals AS (
    SELECT {fk}, COUNT(*) AS EventCount, COUNT({amount}) AS KnownValueCount,
           SUM({amount}) AS TotalValue
    FROM YearActivity GROUP BY {fk}
)
SELECT p.{fk}, p.{name}, t.EventCount, t.KnownValueCount, t.TotalValue
FROM {p} p JOIN Totals t ON t.{fk} = p.{fk}
WHERE NOT EXISTS (
    SELECT 1 FROM RequiredTypes required
    WHERE NOT EXISTS (
        SELECT 1 FROM YearActivity f
        WHERE f.{fk} = p.{fk} AND f.{category} = required.RequiredType
    )
)
ORDER BY p.{fk};""",
         'Small fixture: only master 4 qualifies, with 4 events, 4 known values and total 530. Master 5 has no activity and does not qualify.'),
    ]
    return [dict(id=f'{model["slug"].upper()}-ADV-{i:02d}', domain=model['title'], title=title,
                 prompt=prompt, sql=sql, check=check)
            for i, (title, prompt, sql, check) in enumerate(items, 1)]


def generate(models):
    all_rows = []
    question_index = ['# Advanced query exercises', '',
                      'Five advanced exercises per domain. Select your domain below; prerequisites are joins, aggregates, CTEs and window functions.', '']
    solution_index = ['# Advanced query instructor solutions', '',
                      'Expected results use the small sample data. Student questions are in each domain’s questions folder.', '']
    for model in models:
        rows = exercises(model)
        all_rows.extend(rows)
        question_index.append(f'- [{model["title"]}](../domains/{model["slug"]}/questions/ADVANCED_QUERIES.md)')
        solution_index.append(f'- [{model["title"]}](../domains/{model["slug"]}/ADVANCED_SOLUTIONS.md)')
        directory = ROOT / 'domains' / model['slug']
        q = [f'# {model["title"]}: advanced queries', '',
             'Use the existing domain tables. Prerequisites: joins, grouped aggregates, CTEs and window functions. '
             'Submit SQL, results and an explanation of row counts, NULL handling and tie handling. '
             'These are read-only SQL Server 2017+ exercises. Use the small sample data first, then the large practice dataset; '
             'fixed expected results in the instructor key apply only to the small sample.', '',
             '[All topics](README.md) · [Table definitions](DOMAIN_GUIDE.md)', '']
        a = [f'# {model["title"]}: advanced query solutions', '',
             'Expected results below use schema_solution.sql and seed.sql. Large-data results will differ. '
             'Run each query independently. Equivalent correct approaches are acceptable.', '']
        for row in rows:
            q += [f'## {row["id"]}: {row["title"]}', '', row['prompt'], '']
            a += [f'## {row["id"]}: {row["title"]}', '', '```sql', row['sql'], '```', '',
                  '**Check:** ' + row['check'], '']
        (directory / 'questions' / 'ADVANCED_QUERIES.md').write_text('\n'.join(q), encoding='utf-8')
        (directory / 'ADVANCED_SOLUTIONS.md').write_text('\n'.join(a), encoding='utf-8')
        index = directory / 'questions' / 'README.md'
        text = index.read_text(encoding='utf-8')
        entry = '| [Advanced queries](ADVANCED_QUERIES.md) | 5 |'
        if entry not in text:
            text = text.replace('| [Reporting assignments](REPORTING_ASSIGNMENTS.md) | 6 |',
                                '| [Reporting assignments](REPORTING_ASSIGNMENTS.md) | 6 |\n' + entry)
            index.write_text(text, encoding='utf-8')
    (ROOT / 'advanced_queries.json').write_text(json.dumps(all_rows, indent=2) + '\n', encoding='utf-8')
    (ROOT / 'questions' / 'ADVANCED_QUERIES.md').write_text('\n'.join(question_index) + '\n', encoding='utf-8')
    (ROOT / 'solutions' / 'ADVANCED_QUERIES_SOLUTIONS.md').write_text('\n'.join(solution_index) + '\n', encoding='utf-8')


if __name__ == '__main__':
    from domain_projects import MODELS
    generate(MODELS)
