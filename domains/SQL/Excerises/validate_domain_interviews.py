"""Check all domain-level counts,handout separation,exports and native provenance."""
from collections import Counter,defaultdict
import argparse
import csv
import hashlib
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent


def validate(require_native=True):
    models=json.loads((ROOT/'domain_models.json').read_text(encoding='utf-8'))
    foundation=json.loads((ROOT/'curriculum.json').read_text(encoding='utf-8'))
    expected_subs={(r['topic'],r['subtopic']) for r in foundation};assert len(expected_subs)==132
    groups=defaultdict(Counter);ids=set();book_ids=defaultdict(set);queries=labs=0;prompts={}
    manifests=list((ROOT/'domains').glob('*/questions/*.manifest.json'))
    export_ids={i for p in manifests for i in json.loads(p.read_text(encoding='utf-8'))['question_ids']}
    with (ROOT/'domain_interview_questions.jsonl').open(encoding='utf-8') as stream:
        for line in stream:
            q=json.loads(line);eid=q['id'];assert eid not in ids,eid;ids.add(eid)
            groups[(q['domain'],q['topic'],q['subtopic'])][q['level']]+=1
            book_ids[(q['domain'],q['topic'])].add(eid)
            assert q['prompt'] and q['grading']
            assert not re.search(r'\b(TODO|TBD|lorem ipsum)\b',q['prompt'],re.I),eid
            if q['reference']['kind']=='runnable_query':
                queries+=1;assert q['reference']['sql'] and q['reference']['witness_sql'],eid
                assert 'Source columns:' in q['prompt'],eid
                model=next(m for m in models if m['slug']==q['domain'])
                actual={(model['slug'],t['name'],c['name']) for t in model['tables'] for c in t['columns']}
                sources=re.findall(r'\[([^]]+)\]\.\[([^]]+)\]\.\[([^]]+)\]',q['prompt'].split('Source columns:',1)[1])
                assert sources and set(sources)<=actual,(eid,'invalid source columns',set(sources)-actual)
            else:
                labs+=1;assert 'practical design/native-demonstration' in q['prompt'],eid
            if eid in export_ids:prompts[eid]=q['prompt']
    assert len(ids)==53460 and queries==32400 and labs==21060
    assert len(groups)==1188
    for m in models:
        observed={(t,s) for (d,t,s) in groups if d==m['slug']};assert observed==expected_subs,m['slug']
    assert all(count==Counter(Beginner=15,Intermediate=15,Advanced=15) for count in groups.values())
    for (d,topic),wanted in book_ids.items():
        for folder in ('questions','solutions'):
            file=ROOT/'domains'/d/folder/f'{topic}.md';text=file.read_text(encoding='utf-8')
            found=set(re.findall(r'^#### ([A-Z_]+-[A-Z_]+-\d{2}-[BIA]\d{2})$',text,re.M))
            assert found==wanted,(file,len(found),len(wanted))
            if folder=='questions':
                block=text.split('<!-- DOMAIN_LEVELLED_INTERVIEW_START -->',1)[1]
                assert '```sql' not in block,(file,'answer SQL block in new student questions')
                assert not re.search(r'\bBEGIN\s+TRAN(?:SACTION)?\b|\bROLLBACK\s+TRAN',block,re.I),file
    checked_links=0
    for model in models:
        student=ROOT/'domains'/model['slug']/'questions'
        for file in student.glob('*.md'):
            text=re.sub(r'```[\s\S]*?```|`[^`]*`','',file.read_text(encoding='utf-8'))
            for link in re.findall(r'\]\(([^)]+)\)',text):
                if link.startswith(('https://','http://','#')):continue
                target=(file.parent/link.split('#',1)[0]).resolve()
                assert target.is_relative_to(student.resolve()) or target in {(ROOT/'BEGINNER_GUIDE.md').resolve(),(ROOT/'CODERPAD.md').resolve()},(file,'student-folder escape',link)
                assert target.exists(),(file,'broken link',link);checked_links+=1
                assert 'solutions' not in target.parts,(file,'answer link')
    for path in manifests:
        manifest=json.loads(path.read_text(encoding='utf-8'));export=path.with_name(path.name.replace('.manifest.json','.md')).read_text(encoding='utf-8')
        for eid in manifest['question_ids']:
            assert eid in ids,(path,'unknown ID',eid)
            if manifest.get('layout')=='canonical_references':
                assert eid in export and f'#{eid.lower()}' in export,(path,'missing canonical link',eid)
            else:assert prompts[eid] in export,(path,'prompt mismatch',eid)
            assert hashlib.sha256(prompts[eid].encode()).hexdigest()==manifest['canonical_prompt_sha256'][eid],path
        assert 'Assessment model:' not in export and 'Business report reference' not in export,path
    coverage=list(csv.DictReader((ROOT/'DOMAIN_INTERVIEW_COVERAGE.csv').open(encoding='utf-8',newline='')))
    assert len(coverage)==1188
    for c in coverage:assert [int(c[x]) for x in ('Beginner','Intermediate','Advanced')]==[15,15,15]
    native=json.loads((ROOT/'DOMAIN_INTERVIEW_NATIVE_VALIDATION.json').read_text(encoding='utf-8'))
    if require_native:
        assert native.get('full_expected_result_comparison') and not native['errors'],'Native differential run incomplete/failed'
        assert native['report_results_compared']==queries
        assert native['analysis_populations']==720
        for name,digest in native.get('reference_source_sha256',{}).items():
            assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,('Native evidence is stale',name)
        assert native.get('reference_source_sha256'),'Native provenance hashes missing'
    summary=dict(passed=True,domains=9,subtopics_per_domain=132,domain_subtopic_pairs=1188,
                 levelled_questions=len(ids),per_level={x:sum(v[x] for v in groups.values()) for x in ('Beginner','Intermediate','Advanced')},
                 runnable_queries=queries,practical_lab_rubrics=labs,student_local_links_checked=checked_links,
                 exact_canonical_mock_handouts_checked=len(manifests),
                 native_evidence_checked=require_native,
                 native_query_results_compared=native.get('report_results_compared') if require_native else None,
                 native_adversarial_populations=native.get('adversarial_populations') if require_native else None,
                 native_adversarial_results_compared=native.get('adversarial_result_comparisons') if require_native else None,
                 labs_native_executed=False,
                 note=('Native query comparisons and schema-valid student contracts pass. ' if require_native else 'Structure-only check;native evidence was not checked in this run. ')+
                      'Open-ended lab extensions require instructor case review and demonstration;not all53,460 questions are automatically graded.')
    report_name='DOMAIN_INTERVIEW_VALIDATION.json' if require_native else 'DOMAIN_INTERVIEW_STRUCTURE_VALIDATION.json'
    (ROOT/report_name).write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--structure-only',action='store_true')
    validate(not parser.parse_args().structure_only)
