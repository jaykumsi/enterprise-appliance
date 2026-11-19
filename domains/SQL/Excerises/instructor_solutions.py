"""Build domain-specific instructor keys alongside the student handouts."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
import sys as _sys; _sys.path.insert(0, str(Path(__file__).resolve().parent))
from company_paths import domain_link, domain_dir, domain_dirs, DOMAINS_ROOT, ASSIGNMENTS_INDEX

TEACHING_NOTES = {
    'INTRODUCTION': 'Ask the student to explain the concept using this domain’s tables and a concrete example. Accept equivalent explanations that address the stated risk and limitations.',
    'DATABASE_SCHEMA_USER': 'Separate database, schema and user responsibilities. Check the active database and permissions before diagnosing a syntax error. Run administrative batches independently.',
    'DATATYPES': 'Check precision, scale, length and NULL behavior. Ask the student to predict the converted value before executing. Distinguish conversion failure, truncation and rounding.',
    'DDL': 'Compare column names, types and nullability first, then keys and constraints. Create parent tables before children. A table with the correct columns can still be missing required constraints.',
    'CONSTRAINTS': 'These exercises deliberately attempt invalid writes. An expected constraint error means the rule worked. Confirm the original rows remain unchanged; do not remove the constraint to make the write succeed.',
    'DATA_SETUP': 'Load parents before children and compare the listed column order with each value list. Duplicate-key errors often mean the data was already loaded. Do not rerun inserts blindly.',
    'DML': 'Preview the target rows with SELECT using the same WHERE condition. Compare affected-row counts and unchanged rows. Reset the fixture between independent exercises.',
    'DQL': 'Explain the logical flow: FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY. Check filtering before aggregation, NULL handling, aliases and tie ordering. DISTINCT applies to the full selected combination.',
    'OPERATORS': 'Evaluate the predicate on a matching row, a nonmatching row and a NULL value. Use IS NULL instead of = NULL. Parenthesize mixed AND/OR conditions and inspect both date boundaries.',
    'JOINS': 'Identify the preserved table and join keys before reading the SELECT list. One-to-many joins can repeat parent rows. A right-table filter in WHERE can remove unmatched LEFT JOIN rows; compare ON versus WHERE explicitly.',
    'SET_OPERATIONS': 'Both inputs need compatible column counts and types. UNION removes duplicate complete rows; UNION ALL keeps them. INTERSECT and EXCEPT compare the selected values, not hidden keys.',
    'STRING_FUNCTIONS': 'Inspect the raw text and whitespace before comparing results. LEN excludes trailing spaces. Check one-based positions, absent delimiters, NULL propagation and whether trimming is requested.',
    'DATE_FUNCTIONS': 'Identify the source date/time column and type. DATEDIFF counts boundaries, not complete elapsed periods. Distinguish attaching an offset from converting an instant; current-time results vary between runs.',
    'AGGREGATES': 'Check the grouping keys and resulting row grain. COUNT(*) counts rows; COUNT(column) counts known values. SUM/AVG ignore NULL values, while an all-NULL input stays NULL. Inspect integer versus decimal arithmetic.',
    'ANALYTICAL_FUNCTIONS': 'Explain PARTITION BY, window ORDER BY and the frame separately. ROW_NUMBER breaks ties; RANK leaves gaps; DENSE_RANK does not. Compute a window result in a CTE before filtering it. Window ordering does not guarantee final output order.',
    'CTE': 'Run each CTE’s SELECT separately to inspect intermediate rows. A CTE is scoped to one statement. For recursion, verify the anchor, join direction and termination; a recursion limit does not prevent cycles in the data.',
    'REPORTING_ASSIGNMENTS': 'State what one output row represents. Aggregate independent child tables before joining them to avoid multiplying totals. Compare row counts and totals to the source tables, including parents with no children.',
    'ADVANCED_QUERIES': 'Inspect each CTE independently. Check empty periods versus all-NULL periods, tied ranks, zero denominators and inclusive/exclusive date boundaries. Fixed expected results use the small fixture, not the large practice data.',
}


def workbook_answer_keys(models):
    """Instructor answer keys for the online workbooks (private claude.ai pages), next to each student workbook."""
    import importlib.util
    wb = ROOT / 'domain_workbooks'
    keys_path, links_path = wb / 'pages' / 'instructor_links.json', wb / 'pages' / 'links.json'
    if not keys_path.exists():
        return []
    keys = json.loads(keys_path.read_text(encoding='utf-8'))
    links = json.loads(links_path.read_text(encoding='utf-8')) if links_path.exists() else {}
    spec = importlib.util.spec_from_file_location('wb_domains', wb / 'wb_domains.py')
    cfg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cfg)
    company = {'healthcare': 'AmeriMed Healthcare', **{k: v['company'] for k, v in cfg.DOMAINS.items()}}
    lines = ['', '## Online workbook answer keys (PRIVATE)', '',
             "Each company's online workbook has an instructor answer key with all 490 questions, answer SQL, an explanation and the "
             'expected result. The pages are private on claude.ai: share a key only with other instructors, never with students, and '
             'do not link it from student pages.', '',
             '| Domain | Company | Instructor answer key | Student workbook |', '|---|---|---|---|']
    for m in models:
        if m['slug'] in keys:
            student = f"[Student page]({links[m['slug']]})" if m['slug'] in links else ''
            lines.append(f"| {m['title']} | {company[m['slug']]} | [Answer key]({keys[m['slug']]}) | {student} |")
    return lines


def generate(models, records):
    reports = json.loads((ROOT / 'domain_reports.json').read_text(encoding='utf-8'))
    advanced = json.loads((ROOT / 'advanced_queries.json').read_text(encoding='utf-8'))
    master_index = ['# Instructor solutions by domain', '',
                    'Choose a domain, then open the solution file matching the student question filename. '
                    'Question IDs are identical in both copies. Each answer includes its question, reference SQL '
                    'or model explanation, and validation guidance.', '',
                    'Share the questions folder with students; retain the solutions folder for instructors.', '']
    for model in models:
        directory = domain_dir(model['slug']) / 'solutions'
        directory.mkdir(exist_ok=True)
        selected = [r for r in records if r['domain'] == model['title']]
        topics = list(dict.fromkeys(r['topic'] for r in selected))
        index = [f'# {model["title"]}: instructor solutions', '',
                 'Match the student filename and question ID. The files below include reference answers, '
                 'expected results or grading guidance, and teaching notes for diagnosing mistakes.', '',
                 '**Data:** fixed counts and totals assume the small original sample. Large practice data has different results. '
                 'Run answers individually. For exercises that modify data or schema, reset between independent tasks.', '',
                 '| Student questions | Instructor solutions | Answers |', '|---|---|---:|']
        for topic in topics + ['REPORTING_ASSIGNMENTS', 'ADVANCED_QUERIES']:
            if topic == 'REPORTING_ASSIGNMENTS':
                rows = [r for r in reports if r['domain'] == model['title']]
            elif topic == 'ADVANCED_QUERIES':
                rows = [r for r in advanced if r['domain'] == model['title']]
            else:
                rows = [r for r in selected if r['topic'] == topic]
            lines = [f'# {model["title"]}: {topic.replace("_", " ")} — instructor solutions', '',
                     f'[Instructor index](README.md) · [Student questions](../questions/{topic}.md)', '',
                     '## Teaching and troubleshooting', '', TEACHING_NOTES[topic], '',
                     'Expected counts refer to the small original fixture. Run each answer independently; '
                     'reset the fixture before independent mutation exercises. Equivalent SQL is acceptable '
                     'when values, duplicates, NULL handling and required ordering agree.', '']
            for row in rows:
                title = row.get('title', row.get('subtopic', ''))
                prompt = re.sub(r'\]\([^)\s]*/sql/README\.md\)', '](../questions/DOMAIN_GUIDE.md)', row['prompt'])
                prompt = prompt.replace('](../BEGINNER_GUIDE.md)', '](../questions/BEGINNER_GUIDE.md)').replace('](../README.md)', '](../questions/DOMAIN_GUIDE.md)')
                lines += [f'### {row["id"]}' + (f' — {title}' if title else ''), '',
                          '**Question**', '', f'[Canonical question](../questions/{topic}.md) — `{row["id"]}`', '', '**Reference answer**', '']
                if row.get('sql'):
                    lines += ['```sql', row['sql'], '```', '']
                if row.get('answer'):
                    lines += [row['answer'], '']
                lines += ['**Check and explain:** ' + row['check'], '']
            (directory / f'{topic}.md').write_text('\n'.join(lines), encoding='utf-8')
            index.append(f'| [{topic}](../questions/{topic}.md) | [Solutions]({topic}.md) | {len(rows)} |')
        index += ['', '## Reference handouts', '',
                  'DOMAIN_GUIDE.md, BEGINNER_GUIDE.md, PRACTICE_DATA.md and README.md are reference/navigation handouts, '
                  'not additional exercise sets. Table definitions and fixture-loading instructions are in '
                  '[the domain guide](../questions/DOMAIN_GUIDE.md). The complete schema answer is '
                  '[schema_solution.sql](../schema_solution.sql), and the small sample inserts are [seed.sql](../seed.sql).', '']
        (directory / 'README.md').write_text('\n'.join(index), encoding='utf-8')
        master_index.append(f'- [{model["title"]}]({domain_link(model["slug"], ROOT / 'solutions')}/solutions/README.md)')
    master_index += workbook_answer_keys(models)
    (ROOT / 'solutions' / 'README.md').write_text('\n'.join(master_index) + '\n', encoding='utf-8')
    from substring_practice import generate as generate_substring
    generate_substring(models)


if __name__ == '__main__':
    from domain_projects import MODELS
    generate(MODELS, json.loads((ROOT / 'curriculum.json').read_text(encoding='utf-8')))
