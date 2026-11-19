"""Extra beginner SUBSTRING practice and explained instructor answers."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
import sys as _sys; _sys.path.insert(0, str(Path(__file__).resolve().parent))
from company_paths import domain_dir, domain_dirs, DOMAINS_ROOT, ASSIGNMENTS_INDEX

GUIDE = """## Read this first

`SUBSTRING(text, start, length)` takes characters from text.

- `start` is the first position to include. SQL Server starts counting at **1**.
- `length` is how many characters to take, not the ending position.
- For positive start positions, ending position = start + length - 1.
- Spaces count as characters. Trim only when the question asks you to.

```text
Text:      A L P H A - O N E
Position:  1 2 3 4 5 6 7 8 9
```

### Worked example 1: take three characters

```sql
SELECT SUBSTRING(N'ALPHA-ONE', 2, 3) AS Result;
```

Result: `LPH`. Start at position 2; take positions 2, 3 and 4. The third argument is a count of 3.

### Worked example 2: extract positions 3 through 5

Length = 5 - 3 + 1 = 3.

```sql
SELECT SUBSTRING(N'ALPHA-ONE', 3, 3) AS Result;
```

Result: `PHA`. Using 5 as the length would take positions 3 through 7 instead.

### Worked example 3: extract after a hyphen

```sql
SELECT SUBSTRING(N'ALPHA-ONE', CHARINDEX(N'-', N'ALPHA-ONE') + 1, 100) AS Result;
```

CHARINDEX returns 6. Start at 6 + 1 = 7 to skip the hyphen. Result: `ONE`.
The length 100 is deliberately larger than the remaining text: SQL Server returns the available characters without padding.
For a real column, choose a length that covers its declared maximum. Check for a missing hyphen before subtracting 1 to extract a prefix.

### Common mistakes to discuss

| Mistake | How to explain it |
|---|---|
| Starting at 0 | Count from 1 for these exercises. Start 0 has special behavior; it is not the first character position. |
| Passing the ending position as length | Calculate end - start + 1. |
| Forgetting leading spaces | Display the raw value inside brackets and count the spaces. |
| Assuming a long length adds spaces | It returns only the available text. |
| Subtracting 1 when CHARINDEX returns 0 | A negative length raises an error; handle a missing delimiter first. |
| Treating NULL as empty text | NULL is unknown. Empty text has a known length of zero. |

For each exercise, write down the start, length and predicted result before running SQL.
"""


def exercises(m):
    mp=m['map']; key=mp['RecordID']; label=mp['Label']; table=f'[{m["slug"]}].[{m["base"][0]}]'
    items = [
        ('First characters', 'Extract the first four characters of ABCDEFGH.', "SELECT SUBSTRING(N'ABCDEFGH', 1, 4) AS Result;", [('ABCD',)], 'Start 1 and count 4 includes positions 1 through 4.'),
        ('Middle characters', 'Extract three characters of ABCDEFGH starting at position 3.', "SELECT SUBSTRING(N'ABCDEFGH', 3, 3) AS Result;", [('CDE',)], 'Positions 3, 4 and 5 contain C, D and E.'),
        ('Start and end positions', 'Extract positions 4 through 7 of ABCDEFGH. Calculate the length first.', "SELECT SUBSTRING(N'ABCDEFGH', 4, 7 - 4 + 1) AS Result;", [('DEFG',)], 'Length is 7 - 4 + 1 = 4. It is not 7.'),
        ('One character', 'Return only the hyphen from ALPHA-ONE using numeric start and length.', "SELECT SUBSTRING(N'ALPHA-ONE', 6, 1) AS Result;", [('-',)], 'The hyphen is the sixth character; length 1 selects it alone.'),
        ('Long requested length', 'Predict and return SUBSTRING of ABCDE starting at 4 with length 20. Does it add spaces?', "SELECT SUBSTRING(N'ABCDE', 4, 20) AS Result;", [('DE',)], 'Only D and E remain. The function does not pad the result.'),
        ('Beyond the end and zero length', 'Return two results from ABCDE: start 8 with length 2, and start 2 with length 0. Explain each.', "SELECT SUBSTRING(N'ABCDE', 8, 2) AS BeyondEnd, SUBSTRING(N'ABCDE', 2, 0) AS ZeroLength;", [('', '')], 'Both return empty text. One begins beyond the string; the other requests no characters. Neither result is NULL.'),
        ('Spaces change positions', 'For the text with two leading and two trailing spaces, "  ALPHA-ONE  ", return the first five raw characters and the first five characters after TRIM.', "SELECT SUBSTRING(N'  ALPHA-ONE  ', 1, 5) AS RawResult,\n       SUBSTRING(TRIM(N'  ALPHA-ONE  '), 1, 5) AS TrimmedResult;", [('  ALP', 'ALPHA')], 'The first two raw positions are spaces, leaving room for only ALP. After trimming, A is position 1.'),
        ('Extract a code segment', 'From RX-2024-015, extract the four-digit year and the three-digit final code using fixed positions. Keep the leading zero in 015.', "SELECT SUBSTRING(N'RX-2024-015', 4, 4) AS YearText,\n       SUBSTRING(N'RX-2024-015', 9, 3) AS CodeText;", [('2024', '015')], 'The year occupies positions 4–7 and the final code 9–11. Keep the result as text to retain the leading zero.'),
        ('NULL input', 'Apply SUBSTRING with start 1 and length 3 to a NULL nvarchar value. Return the raw result and another result with the fallback text Missing.', "SELECT SUBSTRING(CAST(NULL AS nvarchar(20)), 1, 3) AS RawResult,\n       COALESCE(SUBSTRING(CAST(NULL AS nvarchar(20)), 1, 3), N'Missing') AS DisplayResult;", [(None, 'Missing')], 'SUBSTRING of NULL returns NULL. COALESCE supplies the requested display value without changing the original data.'),
        ('Safe delimiter extraction', 'For ALPHA-ONE, SOLO and -START, return the prefix before the first hyphen and the suffix after it. If there is no hyphen, return the entire text as the prefix and NULL as the suffix. Keep an empty prefix for -START.', """;WITH Samples AS (
    SELECT 1 AS SampleID, N'ALPHA-ONE' AS TextValue
    UNION ALL SELECT 2, N'SOLO'
    UNION ALL SELECT 3, N'-START'
), Positions AS (
    SELECT *, CHARINDEX(N'-', TextValue) AS HyphenPosition FROM Samples
)
SELECT SampleID,
       SUBSTRING(TextValue, 1, CASE WHEN HyphenPosition > 0 THEN HyphenPosition - 1 ELSE 100 END) AS Prefix,
       CASE WHEN HyphenPosition > 0 THEN SUBSTRING(TextValue, HyphenPosition + 1, 100) END AS Suffix
FROM Positions ORDER BY SampleID;""", [(1,'ALPHA','ONE'), (2,'SOLO',None), (3,'','START')], 'Find the delimiter first. Prefix length is position - 1; suffix starts at position + 1. The CASE inside the length argument prevents a negative length when there is no hyphen.'),
        ('Apply to the domain table', f'From `{table}`, return `{key}`, the raw `{label}`, and the first three characters after trimming `{label}`. Order by `{key}`. Do not update the stored data.', f'SELECT {key}, {label}, SUBSTRING(TRIM({label}), 1, 3) AS Prefix\nFROM {table} ORDER BY {key};', None, 'TRIM produces an expression for this SELECT; it does not change the table. With the small fixture, IDs 1–3 yield Alp, bet and Gam.'),
        ('Split the domain reference safely', f'From `{table}`, trim `{label}`, find its first hyphen, and return `{key}`, ReferencePrefix and ReferenceSuffix. Use the full trimmed reference as prefix and NULL suffix if a hyphen is missing. Order by `{key}`.', f""";WITH Cleaned AS (
    SELECT {key}, TRIM({label}) AS CleanReference FROM {table}
), Positions AS (
    SELECT *, CHARINDEX(N'-', CleanReference) AS HyphenPosition FROM Cleaned
)
SELECT {key},
       SUBSTRING(CleanReference, 1,
           CASE WHEN HyphenPosition > 0 THEN HyphenPosition - 1 ELSE 80 END) AS ReferencePrefix,
       CASE WHEN HyphenPosition > 0
            THEN SUBSTRING(CleanReference, HyphenPosition + 1, 80) END AS ReferenceSuffix
FROM Positions ORDER BY {key};""", None, f'The declared maximum length of {label} is 80 characters. The CTEs expose intermediate steps so students can inspect them. Small-fixture IDs 1–3 return Alpha/One, beta/Two and Gamma/Three.'),
    ]
    return [dict(id=f'{m["slug"].upper()}-SUB-{i:02d}', title=t, prompt=p, sql=s, expected=e, explanation=x)
            for i,(t,p,s,e,x) in enumerate(items,1)]


def generate(models):
    for m in models:
        directory=domain_dir(m['slug']); rows=exercises(m)
        questions=[f'# {m["title"]}: extra SUBSTRING practice', '', '[Question index](README.md)', '', GUIDE, '', '## Practice exercises', '']
        solutions=[f'# {m["title"]}: SUBSTRING practice solutions', '', '[Instructor index](README.md) · [Student practice](../questions/SUBSTRING_PRACTICE.md)', '',
                   'Ask students to count positions and predict the result first. Literal examples are independent of the dataset. Table examples use the small fixture for the stated sample results.', '']
        for r in rows:
            heading=f'### {r["id"]}: {r["title"]}'
            questions += [heading,'',r['prompt'],'']
            solutions += [heading,'',r['prompt'],'','```sql',r['sql'],'```','','**Explanation:** '+r['explanation'],'']
            if r['expected'] is not None:
                solutions += ['**Expected rows** (JSON: `null` means SQL NULL; `""` means empty text; spaces inside strings are significant):','','```json',json.dumps(r['expected'],ensure_ascii=False,indent=2),'```','']
        (directory/'questions'/'SUBSTRING_PRACTICE.md').write_text('\n'.join(questions),encoding='utf-8')
        (directory/'solutions'/'SUBSTRING_PRACTICE.md').write_text('\n'.join(solutions),encoding='utf-8')
        for folder in ['questions','solutions']:
            index=directory/folder/'README.md';text=index.read_text(encoding='utf-8')
            entry='\n[Extra SUBSTRING practice: 12 exercises](SUBSTRING_PRACTICE.md)\n'
            if entry.strip() not in text:index.write_text(text+entry,encoding='utf-8')
            page=directory/folder/'STRING_FUNCTIONS.md';text=page.read_text(encoding='utf-8')
            link='[Extra SUBSTRING practice with gradual difficulty](SUBSTRING_PRACTICE.md)'
            if link not in text:
                first,rest=text.split('\n',1);page.write_text(first+'\n\n'+link+'\n'+rest,encoding='utf-8')


if __name__=='__main__':
    from domain_projects import MODELS
    generate(MODELS)
