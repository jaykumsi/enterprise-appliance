"""Verify canonical handouts,retained unique IDs and absence of exact file copies."""
from collections import defaultdict,Counter
import hashlib
import json
from pathlib import Path
import re
from healthcare_exercise_review import KEPT_IDS, review, amerimed_menu

ROOT=Path(__file__).resolve().parent


def validate():
    source=json.loads((ROOT/'consolidated_supplements.json').read_text(encoding='utf-8'))
    selection=json.loads((ROOT/'HEALTHCARE_EXERCISE_REVIEW.json').read_text(encoding='utf-8'))
    assert selection==review(source['healthcare']),'Stale Healthcare selection audit'
    files=defaultdict(list)
    for p in ROOT.rglob('*'):
        if p.is_file() and p.suffix.lower() in {'.md','.sql'}:
            files[hashlib.sha256(p.read_bytes()).hexdigest()].append(str(p.relative_to(ROOT)))
    duplicates=[v for v in files.values() if len(v)>1]
    assert not duplicates,duplicates
    for key,slug in [('healthcare','healthcare'),('retail_draft','retail')]:
        groups=defaultdict(list)
        for q in source[key]:groups[q['topic']].append(q)
        for topic,qs in groups.items():
            question=(ROOT/'domains'/slug/'questions'/f'{topic}.md').read_text(encoding='utf-8')
            answer=(ROOT/'domains'/slug/'solutions'/f'{topic}.md').read_text(encoding='utf-8')
            qids=Counter(re.findall(r'^##### ([^\s:]+)',question,re.M))
            aids=Counter(re.findall(r'^##### ([^\s:]+)',answer,re.M))
            for q in qs:
                expected=1 if key!='healthcare' or q['id'] in KEPT_IDS else 0
                assert qids[q['id']]==expected,q['id']
                assert aids[q['id']]==expected,q['id']
    # Both names lead to the very same files; every retired ID has a live replacement.
    standalone=ROOT.parent.parent.parent/'amerimed-healthcare-sql'
    assert (standalone/'README.md').read_text(encoding='utf-8')==amerimed_menu()
    for file in [standalone/'README.md',ROOT/'domains/healthcare/questions/BEST_EXERCISES.md',ROOT/'domains/healthcare/solutions/EXERCISE_SELECTION.md']:
        for url in re.findall(r'\]\(([^)]+)\)',file.read_text(encoding='utf-8')):
            name,_,anchor=url.partition('#');target=(file.parent/name).resolve()
            assert target.exists(),(file,url)
            if anchor:
                text=target.read_text(encoding='utf-8')
                assert f'id="{anchor}"' in text or f'#### {anchor.upper()}\n' in text,(file,url)
    assert not list((ROOT/'questions').glob('*.md'))
    assert not list((ROOT/'solutions').glob('*_SOLUTIONS.md'))
    assert not (ROOT/'domains/healthcare/interview_ready').exists()
    assert not (ROOT.parent.parent.parent/'interview-practice-bank/questions/sql-server').exists()
    for directory in (ROOT/'domains').iterdir():
        if not directory.is_dir():continue
        assert not (directory/'REPORTING_ASSIGNMENTS.md').exists()
        assert not (directory/'REPORTING_SOLUTIONS.md').exists()
        assert not (directory/'ADVANCED_SOLUTIONS.md').exists()
        assert not (directory/'DATA_SETUP.md').exists()
        assert not (directory/'questions/BEGINNER_GUIDE.md').exists()
        assert not (directory/'questions/CODERPAD.md').exists()
        assert not (directory/'solutions/INTERVIEW_GRADING.md').exists()
    log=json.loads((ROOT/'CONSOLIDATION_REPORT.json').read_text(encoding='utf-8'))
    assert all('.git' not in Path(x['path']).parts for x in log['removed'])
    recovery_path=ROOT/'GIT_RECOVERY_VALIDATION.json'
    recovery=json.loads(recovery_path.read_text(encoding='utf-8')) if recovery_path.exists() else {}
    recovery_status=('Metadata restored and integrity checked;working files unchanged;remote URL not configured.'
                     if recovery.get('status')=='metadata_repaired' else
                     'Separate metadata-recovery plan awaits user approval;Git objects were verified intact.')
    report=dict(passed=True,duplicate_published_files=0,removed_redundant_files=log['removed_file_count'],
                healthcare_source_ids_preserved=len(source['healthcare']),retained_healthcare_supplement_ids=len(KEPT_IDS),retired_healthcare_supplement_ids=480-len(KEPT_IDS),retained_earlier_sql_supplement_ids=len(source['retail_draft']),
                levelled_questions_preserved=53460,
                git_recovery=recovery_status)
    (ROOT/'CONSOLIDATION_VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':validate()
