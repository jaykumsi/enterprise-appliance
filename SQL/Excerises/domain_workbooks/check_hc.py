import json,re,sys
sys.path.insert(0,'.')
import runner
d=json.load(open('../consolidated_supplements.json',encoding='utf-8'))['healthcare']
S=runner.Session('healthcare')
ok=bad=skip=0
for x in d:
    sc=x['self_check']
    if not sc or any(k in sc for k in ['changes every','depends on your own','not run here']):
        skip+=1;continue
    sql='\n'.join(re.findall(r'```sql\n(.*?)```',x['answer'],re.S))
    res=S.run(sql)
    try: out=runner.render(res)
    except RuntimeError as e: out='ERROR '+str(e)[:300]
    if out.strip()==sc.strip(): ok+=1
    else:
        bad+=1
        e=sc.split('\n');g=out.split('\n')
        diff=[(a,b) for a,b in zip(e,g) if a!=b][:2]
        print(x['id'], len(e),len(g), diff if diff else (e[:3],g[:3]))
print(ok,bad,skip)
