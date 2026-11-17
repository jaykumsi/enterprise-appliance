"""Independent Python result oracle for the levelled relational reports."""
from collections import defaultdict
from datetime import date,timedelta
from decimal import Decimal,getcontext,ROUND_FLOOR
from functools import cmp_to_key
import hashlib
import json
from pathlib import Path
from statistics import median

getcontext().prec=50
ROOT=Path(__file__).resolve().parent


def canonical(s):return None if s is None else str(s).casefold().rstrip(' ')
def known_sum(rows):
    values=[r['v'] for r in rows if r['v'] is not None]
    return sum(values,Decimal(0)) if values else None
def month(d):return d.replace(day=1)
def month_add(d,n):
    x=d.year*12+d.month-1+n
    return date(x//12,x%12+1,1)
def events(rows):
    return [dict(id=r[0],owner=r[1],day=r[2] if isinstance(r[2],date) else date.fromisoformat(r[2][:10]),
                 v=None if r[3] is None else Decimal(str(r[3])),seg=r[4],parent=r[5],kind=r[6] if len(r)>6 else r[4]) for r in rows]
def grouped(e,fn):
    out=defaultdict(list)
    for r in e:out[fn(r)].append(r)
    return out
def row(**kwargs):return kwargs


def calculate(level,index,e,owners):
    out=[];by_owner=grouped(e,lambda r:r['owner']);by_id={r['id']:r for r in e}
    for rs in by_owner.values():rs.sort(key=lambda r:(r['day'],r['id']))
    def emit(**kw):out.append(kw)
    def simple(rs,cols):
        for r in rs:emit(**{a:r[b] for a,b in cols})
    if level=='Beginner':
        cols=[('EventID','id'),('OwnerID','owner'),('ActivityDate','day'),('MetricValue','v'),('Segment','seg')]
        if index==0:simple(e,cols)
        elif index==1:simple([r for r in e if r['v'] is not None],cols[:2]+cols[3:4])
        elif index==2:simple([r for r in e if r['v'] is None],[cols[0],cols[2]])
        elif index==3:simple([r for r in e if r['v'] is not None and r['v']>=100],[cols[0],cols[3]])
        elif index==4:simple(sorted([r for r in e if r['v'] is not None],key=lambda r:(-r['v'],r['id']))[:5],[cols[0],cols[3]])
        elif index in (5,6):
            for owner in (by_owner if index==5 else owners):
                rs=by_owner.get(owner,[])
                emit(OwnerID=owner,EventCount=len(rs),KnownCount=sum(r['v'] is not None for r in rs),TotalValue=known_sum(rs) if rs else Decimal(0))
        elif index==7:
            for _,rs in grouped(e,lambda r:canonical(r['seg'])).items():emit(Segment=rs[0]['seg'],EventCount=len(rs),KnownCount=sum(r['v'] is not None for r in rs),TotalValue=known_sum(rs))
        elif index==8:
            for (owner,_),rs in grouped(e,lambda r:(r['owner'],canonical(r['seg']))).items():emit(OwnerID=owner,Segment=rs[0]['seg'])
        elif index==9:
            for m,rs in grouped(e,lambda r:month(r['day'])).items():emit(MonthStart=m,EventCount=len(rs),KnownCount=sum(r['v'] is not None for r in rs),TotalValue=known_sum(rs))
        elif index==10:
            for (owner,d),rs in grouped(e,lambda r:(r['owner'],r['day'])).items():emit(OwnerID=owner,ActivityDate=d,EventCount=len(rs),TotalValue=known_sum(rs))
        elif index==11:
            for owner in owners:
                if not by_owner.get(owner):emit(OwnerID=owner)
        elif index==12:
            for r in e:
                if r['parent'] in by_id:emit(EventID=r['id'],ParentID=r['parent'],ChildValue=r['v'],ParentValue=by_id[r['parent']]['v'])
        elif index==13:
            for _,rs in grouped(e,lambda r:canonical(r['seg'])).items():emit(Segment=rs[0]['seg'],EventCount=len(rs),InRangeCount=sum(r['v'] is not None and 100<=r['v']<=200 for r in rs))
        else:emit(EventCount=len(e),UnknownCount=sum(r['v'] is None for r in e),NegativeCount=sum(r['v'] is not None and r['v']<0 for r in e),ZeroCount=sum(r['v']==0 for r in e),PositiveCount=sum(r['v'] is not None and r['v']>0 for r in e))
    elif level=='Intermediate':
        if index in (0,1):
            for owner,rs in by_owner.items():
                vs=sorted([r for r in rs if r['v'] is not None],key=lambda r:(-r['v'],r['id']));rank={v:j+1 for j,v in enumerate(sorted({r['v'] for r in vs},reverse=True))}
                for j,r in enumerate(vs,1):
                    pos=j if index==0 else rank[r['v']]
                    if pos<=2:emit(OwnerID=owner,EventID=r['id'],MetricValue=r['v'],**{('Position' if index==0 else 'ValueRank'):pos})
        elif index==2:
            for owner,rs in by_owner.items():
                prefix=[]
                for r in rs:
                    prefix.append(r);emit(EventID=r['id'],OwnerID=owner,ActivityDate=r['day'],MetricValue=r['v'],RunningValue=known_sum(prefix),RunningKnownCount=sum(x['v'] is not None for x in prefix))
        elif index==3:
            for owner,rs in by_owner.items():
                prev=None
                for r in rs:emit(EventID=r['id'],OwnerID=owner,MetricValue=r['v'],PreviousValue=prev,Delta=None if prev is None or r['v'] is None else r['v']-prev);prev=r['v']
        elif index==4:
            for _,rs in grouped([r for r in e if r['v'] is not None and r['v']>0],lambda r:canonical(r['seg'])).items():
                totals={o:known_sum(v) for o,v in grouped(rs,lambda r:r['owner']).items()};total=sum(totals.values());rank={v:j+1 for j,v in enumerate(sorted(set(totals.values()),reverse=True))}
                for o,v in totals.items():
                    if rank[v]<=2:emit(Segment=rs[0]['seg'],OwnerID=o,TotalValue=v,ValueRank=rank[v],SegmentTotal=total,SharePercent=100*v/total)
        elif index==5:
            for owner,rs in by_owner.items():
                if {'a','b','c'}<={canonical(r['kind']) for r in rs}:emit(OwnerID=owner,EventCount=len(rs),TotalValue=known_sum(rs))
        elif index==6:
            for r in e:
                vals=[p['v'] for p in by_owner[r['owner']] if r['day']-timedelta(days=30)<=p['day']<r['day'] and p['v'] is not None]
                emit(EventID=r['id'],OwnerID=r['owner'],PriorKnownCount=len(vals),PriorAverage=sum(vals)/len(vals) if vals else None)
        elif index==7:
            for owner in owners:
                rs=[r for r in by_owner.get(owner,[]) if r['v'] is not None];emit(OwnerID=owner,FirstEventID=rs[0]['id'] if rs else None,LastEventID=rs[-1]['id'] if rs else None)
        elif index==8:
            for owner in owners:
                for n in range(12):
                    m=date(2024,n+1,1);rs=[r for r in by_owner.get(owner,[]) if month(r['day'])==m]
                    emit(OwnerID=owner,MonthStart=m,EventCount=len(rs),KnownCount=sum(r['v'] is not None for r in rs),TotalValue=known_sum(rs) if rs else Decimal(0))
        elif index==9:
            for owner,rs in by_owner.items():
                totals=[(vs[0]['seg'],known_sum(vs)) for vs in grouped(rs,lambda r:canonical(r['seg'])).values()];known=[x for x in totals if x[1] is not None]
                for seg,v in known:
                    if v==max(t for _,t in known):emit(OwnerID=owner,Segment=seg,TotalValue=v)
        elif index==10:
            for (owner,d,v),rs in grouped(e,lambda r:(r['owner'],r['day'],r['v'])).items():
                if len(rs)>=2:emit(OwnerID=owner,ActivityDate=d,MetricValue=v,Multiplicity=len(rs))
        elif index==11:
            for owner,rs in by_owner.items():
                vals=[r for r in rs if r['v'] is not None and r['v']>0];total=known_sum(vals);running=Decimal(0)
                for r in vals:
                    running+=r['v']
                    if running>=Decimal('.8')*total:emit(OwnerID=owner,EventID=r['id'],RunningValue=running,TotalValue=total);break
        elif index==12:
            for owner in owners:
                vals=[r['v'] for r in by_owner.get(owner,[]) if r['v'] is not None];emit(OwnerID=owner,KnownCount=len(vals),MedianValue=median(vals) if vals else None)
        elif index==13:
            for r in e:
                p=by_id.get(r['parent']);g=by_id.get(p['parent']) if p else None
                emit(EventID=r['id'],ParentEventID=p['id'] if p else None,GrandparentEventID=g['id'] if g else None,MetricValue=r['v'],ParentValue=p['v'] if p else None,GrandparentValue=g['v'] if g else None)
        else:
            for owner in owners:
                days=sorted({r['day'] for r in by_owner.get(owner,[])});pairs=[(x,y,(y-x).days) for x,y in zip(days,days[1:])]
                best=min(pairs,key=lambda t:(-t[2],t[0])) if pairs else (None,None,None)
                emit(OwnerID=owner,StartDate=best[0],EndDate=best[1],GapDays=best[2])
    else:
        if index==0:
            for owner in owners:
                rs=by_owner.get(owner,[]);sessions=[]
                for r in rs:
                    if not sessions or (r['day']-sessions[-1][-1]['day']).days>30:sessions.append([])
                    sessions[-1].append(r)
                prev=None
                if not sessions:emit(OwnerID=owner,SessionNo=0,StartDate=None,EndDate=None,EventCount=0,KnownCount=0,TotalValue=Decimal(0),PreviousValue=None,GrowthPercent=None)
                for n,ss in enumerate(sessions,1):
                    total=known_sum(ss);growth=None if total is None or prev in (None,0) else 100*(total-prev)/prev
                    emit(OwnerID=owner,SessionNo=n,StartDate=ss[0]['day'],EndDate=ss[-1]['day'],EventCount=len(ss),KnownCount=sum(r['v'] is not None for r in ss),TotalValue=total,PreviousValue=prev,GrowthPercent=growth);prev=total
        elif index==1:
            for r in e:
                vals=[p['v'] for p in by_owner[r['owner']] if r['day']-timedelta(days=30)<=p['day']<r['day'] and p['v'] is not None];m=median(vals) if vals else None
                emit(EventID=r['id'],OwnerID=r['owner'],MetricValue=r['v'],PriorKnownCount=len(vals),PriorMedian=m,IsAnomaly=int(m is not None and r['v'] is not None and r['v']>2*m))
        elif index==2:
            for _,rs in grouped([r for r in e if r['v'] is not None and r['v']>0],lambda r:canonical(r['seg'])).items():
                totals={o:known_sum(vs) for o,vs in grouped(rs,lambda r:r['owner']).items()};total=sum(totals.values());cum=Decimal(0)
                for rank,value in enumerate(sorted(set(totals.values()),reverse=True),1):
                    previous=cum;members=[o for o,v in totals.items() if v==value];cum+=value*len(members)
                    if previous<Decimal('.8')*total:
                        for owner in members:emit(Segment=rs[0]['seg'],OwnerID=owner,TotalValue=value,ValueRank=rank,CumulativeValue=cum,SegmentTotal=total)
        elif index==3:
            cohorts=defaultdict(list)
            for owner,rs in by_owner.items():
                m=month(rs[0]['day'])
                if m.year==2024:cohorts[m].append(owner)
            for cohort,members in cohorts.items():
                for n in range(6):
                    m=month_add(cohort,n);active=sum(any(month(r['day'])==m for r in by_owner[o]) for o in members)
                    emit(CohortMonth=cohort,MonthOffset=n,ActivityMonth=m,CohortSize=len(members),ActiveOwners=active,RetentionPercent=Decimal(100)*active/len(members))
        elif index==4:
            for owner in owners:
                days=sorted({r['day'] for r in by_owner.get(owner,[])});candidates=[]
                for p,start in enumerate(days):
                    for q in range(p,len(days)):
                        end=days[q];active=q-p+1;missing=(end-start).days+1-active
                        if missing<=1:candidates.append((active,start,end,missing))
                best=min(candidates,key=lambda t:(-t[0],t[1],t[2])) if candidates else (0,None,None,0)
                emit(OwnerID=owner,StartDate=best[1],EndDate=best[2],ActiveDays=best[0],MissingDays=best[3])
        elif index==5:
            for r in e:
                path=[r['id']];current=r
                while current['parent'] in by_id and current['parent'] not in path and len(path)<=100:
                    current=by_id[current['parent']];path.append(current['id'])
                emit(EventID=r['id'],TerminalEventID=current['id'],RootEventID=current['id'] if current['parent'] is None else None,Depth=len(path)-1,CycleFlag=int(current['parent'] in path),BoundaryFlag=int(current['parent'] is not None and current['parent'] not in by_id),VisitPath='/'+'/'.join(map(str,path))+'/')
        elif index==6:
            children=grouped(e,lambda r:r['parent'])
            for root in children.get(None,[]):
                candidates=[];todo=[(root,0,{root['id']})]
                while todo:
                    r,depth,path=todo.pop()
                    if r['day']<=date(2024,12,31):candidates.append((r,depth))
                    for c in children.get(r['id'],[]):
                        if c['id'] not in path and depth<100:todo.append((c,depth+1,path|{c['id']}))
                best=max(candidates,key=lambda t:(t[0]['day'],t[0]['id'])) if candidates else None
                emit(RootEventID=root['id'],SelectedEventID=best[0]['id'] if best else None,ActivityDate=best[0]['day'] if best else None,MetricValue=best[0]['v'] if best else None,Depth=best[1] if best else None)
        elif index==7:
            for owner,rs in by_owner.items():
                supply=[[r,r['v']] for r in rs if canonical(r['kind'])=='a' and r['v'] is not None and r['v']>0];demand=[[r,r['v']] for r in rs if canonical(r['kind'])=='b' and r['v'] is not None and r['v']>0];p=q=0
                while p<len(supply) and q<len(demand):
                    value=min(supply[p][1],demand[q][1]);emit(OwnerID=owner,SupplyEventID=supply[p][0]['id'],DemandEventID=demand[q][0]['id'],AllocatedValue=value,UnmatchedValue=Decimal(0));supply[p][1]-=value;demand[q][1]-=value
                    if supply[p][1]==0:p+=1
                    if demand[q][1]==0:q+=1
                for r,v in supply:
                    if v>0:emit(OwnerID=owner,SupplyEventID=r['id'],DemandEventID=None,AllocatedValue=Decimal(0),UnmatchedValue=v)
                for r,v in demand:
                    if v>0:emit(OwnerID=owner,SupplyEventID=None,DemandEventID=r['id'],AllocatedValue=Decimal(0),UnmatchedValue=v)
        elif index==8:
            for _,rs in grouped([r for r in e if r['v'] is not None and r['v']>0],lambda r:canonical(r['seg'])).items():
                totals={o:known_sum(vs) for o,vs in grouped(rs,lambda r:r['owner']).items()};total=sum(totals.values());base={o:int((10000*v/total).to_integral_value(rounding=ROUND_FLOOR)) for o,v in totals.items()};remaining=10000-sum(base.values());order=sorted(totals,key=lambda o:(-(10000*totals[o]-base[o]*total),o));bonus=set(order[:remaining])
                for o,v in totals.items():emit(Segment=rs[0]['seg'],OwnerID=o,TotalValue=v,BasisPoints=base[o]+int(o in bonus),SegmentTotal=total)
        elif index==9:
            for owner in owners:
                days=[date(2023,12,31)]+sorted({r['day'] for r in by_owner.get(owner,[]) if r['day'].year==2024})+[date(2025,1,1)]
                for x,y in zip(days,days[1:]):
                    if (y-x).days>1:emit(OwnerID=owner,StartDate=x+timedelta(days=1),EndDate=y-timedelta(days=1),MissingDays=(y-x).days-1)
        elif index==10:
            for owner,rs in by_owner.items():
                candidates=[]
                for ia,a in enumerate(rs):
                    if canonical(a['kind'])!='a':continue
                    for ib in range(ia+1,len(rs)):
                        b=rs[ib]
                        if canonical(b['kind'])!='b':continue
                        for ic in range(ib+1,len(rs)):
                            c=rs[ic]
                            if canonical(c['kind'])=='c':candidates.append((ic,-ib,-ia,a,b,c))
                if candidates:
                    _,_,_,a,b,c=min(candidates,key=lambda x:x[:3]);emit(OwnerID=owner,FirstEventID=a['id'],SecondEventID=b['id'],ThirdEventID=c['id'],StartDate=a['day'],EndDate=c['day'])
        elif index==11:
            for owner,rs in by_owner.items():
                for d in sorted({r['day'] for r in rs}):
                    found={}
                    for seg in ('a','b','c'):
                        candidates=[r for r in rs if canonical(r['kind'])==seg and d-timedelta(days=29)<=r['day']<=d]
                        if candidates:found[seg]=max(candidates,key=lambda r:(r['day'],r['id']))
                    if len(found)==3:emit(OwnerID=owner,TriggerDate=d,AEventID=found['a']['id'],BEventID=found['b']['id'],CEventID=found['c']['id']);break
        elif index==12:
            children=grouped(e,lambda r:r['parent'])
            for start in e:
                found={};cycle=False;todo=[(start,{start['id']})]
                while todo:
                    node,path=todo.pop()
                    for child in children.get(node['id'],[]):
                        if child['id'] in path:cycle=True;continue
                        found[child['id']]=child;todo.append((child,path|{child['id']}))
                vals=list(found.values());emit(EventID=start['id'],DescendantCount=len(vals),KnownCount=sum(r['v'] is not None for r in vals),TotalValue=known_sum(vals) if vals else Decimal(0),CycleFlag=int(cycle))
        elif index==13:
            for owner in owners:
                rs=by_owner.get(owner,[]);candidates=[]
                known=[r['v'] for r in rs if r['v'] is not None];nknown=len(known);known_total=sum(known,Decimal(0))
                for p,start in enumerate(rs):
                    if start['v'] is None:continue
                    total=Decimal(0)
                    for q in range(p,len(rs)):
                        if rs[q]['v'] is None:break
                        total+=nknown*rs[q]['v']-known_total;candidates.append((total,p,q))
                best=min(candidates,key=lambda x:(-x[0],x[1],x[2])) if candidates else None
                emit(OwnerID=owner,StartEventID=rs[best[1]]['id'] if best else None,EndEventID=rs[best[2]]['id'] if best else None,BlockScore=best[0] if best else None,EventCount=best[2]-best[1]+1 if best else 0)
        else:raise NotImplementedError('Domain reconciliation is computed separately.')
    return out


def sorted_result(recipe,records):
    specs=[x.strip().split() for x in recipe['order'].split(',')]
    def cmp(a,b):
        for spec in specs:
            x,y=a[spec[0]],b[spec[0]]
            if isinstance(x,str) and isinstance(y,str):x,y=canonical(x),canonical(y)
            c=0 if x==y else (-1 if x is None else 1 if y is None else (1 if x>y else -1))
            if c:return -c if len(spec)>1 and spec[1]=='DESC' else c
        return 0
    return [tuple(r[c] for c in recipe['columns']) for r in sorted(records,key=cmp_to_key(cmp))]


def compare(actual,expected,columns,label):
    if len(actual)!=len(expected):raise AssertionError(f'{label}:row count {len(actual)} != {len(expected)}')
    for n,(ar,er) in enumerate(zip(actual,expected)):
        for col,av,ev in zip(columns,ar,er):
            if av is None or ev is None:
                if av is not ev:raise AssertionError((label,n,col,av,ev))
            elif isinstance(ev,(Decimal,int,float)) and not isinstance(ev,bool):
                if abs(Decimal(str(av))-Decimal(str(ev)))>Decimal('.000003'):raise AssertionError((label,n,col,str(av),str(ev)))
            elif col=='Segment':
                if canonical(av)!=canonical(ev):raise AssertionError((label,n,col,av,ev))
            elif av!=ev:raise AssertionError((label,n,col,av,ev))


def query_from_population(recipe,rows_source='#InterviewE',owners_source='#InterviewOwners'):
    ctes=[('E',f'SELECT * FROM {rows_source}'),('Owners',f'SELECT OwnerID FROM {owners_source}')]+recipe['ctes']+[('Report',recipe['report'])]
    return ';WITH '+',\n'.join(f'{n} AS ({q})' for n,q in ctes)+'\nSELECT '+','.join('['+x+']' for x in recipe['columns'])+' FROM Report ORDER BY '+recipe['order']+' OPTION(MAXRECURSION 32767);'


def validate_all(con,models,topics,focus_rows):
    from domain_interview_queries import recipes,instantiate
    from domain_interview_domain_oracle import reconciliation
    cur=con.cursor();all_recipes=recipes();failures=[];counts=0;cached={};expected_manifest=[]
    for profile in focus_rows:
        model=next(m for m in models if m['slug']==profile['domain'])
        owners=[r[0] for r in next(t for t in model['tables'] if t['name']==model['base'][1])['rows']]
        e=events(profile['rows']);level_index=defaultdict(int)
        for recipe in all_recipes:
            n=level_index[recipe['level']];level_index[recipe['level']]+=1
            label=f'{profile["domain"]}/{profile["topic"]}/{profile["subtopic"]}/{recipe["level"]}{n+1:02d}'
            try:
                item=instantiate(model,profile['topic'],profile['subtopic'],recipe)
                actual=[tuple(r) for r in cur.execute(item['sql']).fetchall()]
                if [c[0] for c in cur.description]!=item['output']:raise AssertionError('Output columns mismatch')
                if recipe['level']=='Advanced' and n==14:
                    expected=sorted_result({**recipe,'columns':item['output'],'order':item['sort']},reconciliation(model,{r['id'] for r in e}))
                    columns=item['output']
                else:
                    key=(recipe['level'],n,json.dumps(profile['rows'],default=lambda x:str(x),sort_keys=True))
                    if key not in cached:cached[key]=sorted_result(recipe,calculate(recipe['level'],n,e,owners))
                    expected=cached[key];columns=recipe['columns']
                compare(actual,expected,columns,label);counts+=1
                expected_manifest.append(dict(domain=profile['domain'],topic=profile['topic'],subtopic=profile['subtopic'],level=recipe['level'],number=n+1,columns=item['output'],row_count=len(actual),expected_rows=[list(r) for r in expected]))
            except Exception as exc:
                failures.append(dict(id=label,error=str(exc)))
                if len(failures)>20:break
        if failures and len(failures)>20:break
        if counts%450==0:print(f'Native differential checks:{counts},failures={len(failures)}',flush=True)
    from domain_interview_edge_tests import validate_edges
    edge_report=validate_edges(con,all_recipes)
    failures+=edge_report.pop('errors')
    def enc(x):
        if isinstance(x,(date,Decimal)):return str(x)
        raise TypeError(type(x).__name__)
    (ROOT/'DOMAIN_INTERVIEW_EXPECTED.json').write_text(json.dumps(expected_manifest,default=enc,separators=(',',':'))+'\n',encoding='utf-8')
    return dict(phase='native_differential',full_expected_result_comparison=not failures,
                report_results_compared=counts,unique_python_oracle_calculations=len(cached),errors=failures,**edge_report)
