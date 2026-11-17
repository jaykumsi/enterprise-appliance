"""Select supplementary AmeriMed cases; both names publish one Healthcare bank.

The 480 original records remain private build inputs. Retired historical IDs have
an explicit replacement, rather than disappearing or inflating the hard quota.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
KEEP = {
    'AGGREGATES': 'I06 I07 I10 A02',
    'ANALYTICAL_FUNCTIONS': 'I10',
    'CONSTRAINTS': 'I02 I04 I07 I08 A02',
    'CTE': 'A10',
    'DATABASE_SCHEMA_USER': 'I03 I04 I05 I06 I08 A01 A03 A10',
    'DATATYPES': 'I01 I03 I05 I06 I07 I09',
    'DATE_FUNCTIONS': 'I05 A06 A07',
    'DDL': 'I04 I05 I10 A02 A04 A09 A10',
    'DML': 'I03 I09 A02 A03 A10',
    'DQL': 'I04',
    'INTRODUCTION': 'I05 I06 A01',
    'JOINS': 'I02',
    'OPERATORS': 'I01 A01 A07',
    'SET_OPERATIONS': 'I06 I10 A01',
    'STRING_FUNCTIONS': 'I08',
    'SUBQUERIES': 'I07 A01 A03',
}
KEPT_IDS = {f'{topic}-{code}' for topic, codes in KEEP.items() for code in codes.split()}
SPECIAL_RETIREMENTS = {
    'ANALYTICAL_FUNCTIONS-A02': ('DML-A03', 'Legitimate repeated prescriptions must not be deleted as duplicate clinical records. Practise exact-row cleanup in staging only.'),
    'CONSTRAINTS-B09': ('CONSTRAINTS-I08', 'Patient and doctor display names are not unique business identities. Use the optional NationalID filtered unique index instead.'),
    'DATABASE_SCHEMA_USER-A05': ('DATABASE_SCHEMA_USER-I08', 'The old prompt asks for controlled INSERT but its answer performs UPDATE; use the consistent access-control lab.'),
    'DATATYPES-A03': (None, 'The old LEN-based migration check omits trailing spaces; prefer the current migration lab with explicit storage requirements.'),
    'DML-I08': (None, 'The title promises oldest-first deletion but DELETE TOP has no ordering. Prefer the current DML practical assessment.'),
    'INTRODUCTION-A09': (None, 'Matching counts alone does not prove the two query results contain the same rows. Prefer the current query comparison assessment.'),
    'SET_OPERATIONS-A02': (None, 'Grand-total equality alone cannot establish row-level reconciliation; use the current explicit reconciliation contract.'),
}


def selected_case(original):
    """Correct retained contracts without changing the historical source record."""
    row = dict(original)
    # Strip the original repeated prompt before replacing any student wording.
    prefix = '**Question:** ' + row['body']
    if row['answer'].startswith(prefix):
        row['answer'] = row['answer'][len(prefix):].lstrip()
    if row['id'] == 'AGGREGATES-I06':
        row['body'] = ('Use healthcare.Patients and healthcare.Encounters to report Region and TotalCharge for regions with encounters, '
            'then one grand total labelled ALL REGIONS. SUM ignores unknown charges; an all-unknown group remains NULL. '
            'Order ordinary regions alphabetically and put the grand total last. Source columns: Patients.PatientID, Patients.Region, Encounters.PatientID, Encounters.Charge.')
        row['answer'] = row['answer'].replace('GROUP BY ROLLUP (p.Region);',
            'GROUP BY ROLLUP (p.Region)\nORDER BY GROUPING(p.Region), p.Region;').replace('| ALL REGION |', '| ALL REGIONS |')
        row['self_check'] = row['self_check'].replace('| ALL REGION |', '| ALL REGIONS |')
    elif row['id'] == 'ANALYTICAL_FUNCTIONS-I10':
        row['body'] = ('For each healthcare.Medications row return MedicationName, UnitCost and PctRank, using PERCENT_RANK by UnitCost ascending rounded to decimal(4,2). '
            'Equal costs receive the same rank; do not add MedicationID to the window ordering. A tied maximum need not rank 1. '
            'Order the report by UnitCost, MedicationID. Source columns: Medications.MedicationID, Medications.MedicationName, Medications.UnitCost.')
        row['answer'] = row['answer'].replace('ORDER BY UnitCost;', 'ORDER BY UnitCost, MedicationID;')
        row['answer'] = row['answer'].split('**Expected result:**')[0].rstrip()
        row['self_check'] = ''
    elif row['id'] == 'DDL-A04':
        row['body'] = ('Create system-versioned healthcare.PriceList with MedicationID int NOT NULL PRIMARY KEY, Price decimal(12,2) NOT NULL, '
            'ValidFrom datetime2(7) GENERATED ALWAYS AS ROW START NOT NULL and ValidTo datetime2(7) GENERATED ALWAYS AS ROW END NOT NULL. '
            'Define PERIOD FOR SYSTEM_TIME (ValidFrom, ValidTo), enable SYSTEM_VERSIONING, and name the history table healthcare.PriceListHistory. '
            'No foreign key or additional default is required. Return name and temporal_type_desc for the two tables from sys.tables, in name order.')
        row['answer'] = row['answer'].replace("WHERE name LIKE 'PriceList%';", "WHERE schema_id = SCHEMA_ID('healthcare') AND name IN ('PriceList','PriceListHistory')\nORDER BY name;")
    elif row['id'] == 'DDL-A10':
        row['body'] = ('Create healthcare.seqInvoice AS int starting at 5000 and incrementing by 10. '
            'For input n = 1, 2, 3, allocate sequence values in n order and return n, InvoiceNo ordered by n. '
            'Use a fresh sequence; explain why gaps are allowed and why this differs from a table IDENTITY.')
        row['answer'] = row['answer'].replace('NEXT VALUE FOR healthcare.seqInvoice AS InvoiceNo',
            'NEXT VALUE FOR healthcare.seqInvoice OVER (ORDER BY n) AS InvoiceNo').replace('AS v(n);','AS v(n)\nORDER BY n;')
    elif row['id'] == 'SUBQUERIES-A03':
        row['title'] = 'Repeated prescribing without deleting history'
        row['body'] = ('Return PatientID and PatientName for patients with more than one prescription row for the same MedicationID across their encounters. '
            'Use EXISTS and return each patient once, ordered by PatientID. Repeated prescribing may include refills; do not infer clinical duplication or delete prescriptions. '
            'Source columns: Patients.PatientID, Patients.PatientName, Encounters.PatientID, Encounters.EncounterID, Prescriptions.EncounterID, Prescriptions.MedicationID.')
        row['answer'] = row['answer'].replace('If any such group exists, the patient had a refill.',
            'If any such group exists, the patient has repeated prescribing for that medication; this alone does not establish a refill or a duplicate record.')
    return row


def review(rows):
    """Classify every historical ID and resolve replacements to published IDs."""
    primary = {}
    with (ROOT / 'domain_interview_questions.jsonl').open(encoding='utf-8') as stream:
        for line in stream:
            q = json.loads(line)
            if q['domain'] == 'healthcare':
                primary.setdefault((q['topic'], q['level']), q['id'])
    assert KEPT_IDS <= {r['id'] for r in rows}
    decisions = []
    for row in rows:
        eid = row['id']
        if eid in KEPT_IDS:
            decisions.append(dict(id=eid, topic=row['topic'], decision='keep', replacement=eid,
                reason='Retain as applied SQL Server or clinical-data practice alongside the stronger levelled bank. Historical tier letters do not determine current interview difficulty.'))
        else:
            level = {'B': 'Beginner', 'I': 'Intermediate', 'A': 'Advanced'}[eid.rsplit('-', 1)[1][0]]
            topic = row['topic'] if row['topic'] != 'SUBQUERIES' else 'JOINS'
            replacement, reason = SPECIAL_RETIREMENTS.get(eid, (None,
                'Prefer the current levelled contract with its explicit deliverables and assessment rules; do not publish another overlapping historical exercise.'))
            replacement = replacement or primary[topic, level]
            replacement_topic = replacement.removeprefix('HEALTHCARE-').rsplit('-', 2)[0] if replacement.startswith('HEALTHCARE-') else replacement.rsplit('-', 1)[0]
            decisions.append(dict(id=eid, topic=row['topic'], decision='retire', replacement=replacement,
                replacement_topic=replacement_topic, reason=reason))
    assert len(decisions) == 480 and len({r['id'] for r in decisions}) == 480
    return dict(policy='One canonical Healthcare/AmeriMed bank. Preserve all 5,940 levelled questions; publish only selected historical applied labs. Original records remain private regeneration inputs.',
        primary_questions=5940, historical_records_reviewed=480,
        retained_applied_cases=len(KEPT_IDS), retired_historical_cases=480-len(KEPT_IDS), decisions=decisions)


def publish_review(put, rows):
    report = review(rows)
    put(ROOT / 'HEALTHCARE_EXERCISE_REVIEW.json', json.dumps(report, indent=2) + '\n')
    student = ROOT / 'domains/healthcare/questions'
    topics = sorted({r['topic'] for r in rows})
    path = ['# Healthcare and AmeriMed: interview practice route', '',
        'AmeriMed and Healthcare use this same question bank. Complete the Beginner, Intermediate and Advanced sections in every subtopic; the 5,940 levelled questions remain the assessed curriculum.', '',
        '## Interview preparation', '',
        '1. Work through the [topic menu](README.md) and [table definitions](DOMAIN_GUIDE.md).',
        '2. Solve the [hard challenge sampler](INTERVIEW_CHALLENGES.md), including correction chains, exact allocation, temporal reasoning and multi-table reconciliation.',
        '3. Take the [mixed mock](MIXED_MOCK.md), then the [hard mock](HARD_MOCK.md), using the [timed interview rules](../../../CODERPAD.md).',
        '4. Explain your result grain, NULL handling, tie rules, complexity and failure cases to an instructor. Repeat any failed assessment on changed input data.', '',
        '## Selected applied cases', '',
        f'{len(KEPT_IDS)} older cases add SQL Server feature demonstrations and clinical-data practice. These are supplementary labs, not the Advanced interview quota. Original B/I/A letters are historical IDs only. Use the large fixture and reset it between exercises that change data. Instructor answers for these historical cases have not been included in the native report-validation claim.', '',
        '| Topic | Selected cases |', '|---|---|']
    by_id = {r['id']: r for r in rows}
    for topic in topics:
        ids = sorted(eid for eid in KEPT_IDS if by_id[eid]['topic'] == topic)
        path.append('| ' + topic.replace('_', ' ').title() + ' | ' + ' · '.join(f'[{eid}]({topic}.md#legacy-{eid.lower()})' for eid in ids) + ' |')
    put(student / 'BEST_EXERCISES.md', '\n'.join(path) + '\n')
    audit = ['# Healthcare historical exercise selection', '',
        f'Reviewed all 480 historical records: kept {len(KEPT_IDS)} supplementary applied cases and retired {480-len(KEPT_IDS)} from published handouts. The original private input remains available for regeneration and traceability. All 5,940 levelled questions remain.', '',
        'The replacement is the preferred starting assessment in the corresponding topic and level, not a claim that two exercises are textually identical. Kept historical cases use the large fixture and require instructor review; their original tier letters do not certify Advanced difficulty.', '',
        '| Historical ID | Decision | Preferred exercise | Reason |', '|---|---|---|---|']
    for r in report['decisions']:
        topic = r.get('replacement_topic', r['topic'])
        eid = r['replacement']
        anchor = eid.lower() if eid.startswith('HEALTHCARE-') else 'legacy-' + eid.lower()
        audit.append(f'| {r["id"]} | {r["decision"]} | [{eid}](../questions/{topic}.md#{anchor}) | {r["reason"]} |')
    put(ROOT / 'domains/healthcare/solutions/EXERCISE_SELECTION.md', '\n'.join(audit) + '\n')
    return report


def amerimed_menu():
    prefix = '../SQL/Excerises/domains/healthcare/'
    topics = sorted(KEEP)
    lines = ['# AmeriMed Healthcare SQL assignments', '',
        'AmeriMed and Healthcare share one maintained set of questions and instructor answers. Every link below opens the canonical Healthcare file; edits there apply to both names.', '',
        '**132 subtopics · 15 Beginner + 15 Intermediate + 15 Advanced per subtopic · 5,940 levelled questions.**', '',
        f'[Start here]({prefix}questions/README.md) · [Best practice route]({prefix}questions/BEST_EXERCISES.md) · [Tables and sample data]({prefix}questions/DOMAIN_GUIDE.md) · [Large practice data instructions]({prefix}questions/PRACTICE_DATA.md)', '',
        f'[Hard challenge sampler]({prefix}questions/INTERVIEW_CHALLENGES.md) · [Mixed mock]({prefix}questions/MIXED_MOCK.md) · [Hard mock]({prefix}questions/HARD_MOCK.md)', '',
        '| Topic | Student questions | Instructor answers |', '|---|---|---|']
    topics = sorted(set(topics) | {'DATA_SETUP'})
    for topic in topics:
        lines.append(f'| {topic.replace("_", " ").title()} | [Questions]({prefix}questions/{topic}.md) | [Answers]({prefix}solutions/{topic}.md) |')
    lines += ['', f'[Instructor selection audit]({prefix}solutions/EXERCISE_SELECTION.md). Keep instructor files private when sharing assignments.', '',
        'Repository metadata is retained for its history. Assignment files are maintained in the linked canonical domain.']
    return '\n'.join(lines) + '\n'
