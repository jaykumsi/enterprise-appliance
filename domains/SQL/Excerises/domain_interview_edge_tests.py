"""Adversarial normalized populations executed on native SQL Server temp tables."""
from datetime import date,timedelta
from decimal import Decimal
import random
from domain_interview_oracle import events,calculate,sorted_result,compare,query_from_population


def cases():
    base=date(2024,1,1)
    def e(n,day,value,seg='A',parent=None,owner=1):return [n,owner,base+timedelta(days=day),None if value is None else Decimal(str(value)),seg,parent]
    yield 'empty',[]
    yield 'unknown_and_inactive',[e(1,0,None),e(2,1,None,'B',1),e(3,40,None,'C',2)]
    yield 'zero_denominators',[e(1,0,0),e(2,1,0,'B'),e(3,2,0,'C',owner=2)]
    yield 'signed_and_unknown_breaks',[e(1,0,-5),e(2,1,-2),e(3,2,None),e(4,3,-1),e(5,4,4),e(6,5,-1)]
    yield 'same_day_order_and_repeated_values',[e(1,0,10,'A'),e(2,0,10,'B'),e(3,0,10,'C'),e(4,1,20,'B'),e(5,1,None,'C')]
    yield 'thirty_and_thirty_one_day_boundaries',[e(1,0,10),e(2,29,20,'B'),e(3,30,40,'C'),e(4,60,80),e(5,91,160)]
    yield 'one_hole_not_one_per_gap',[e(1,0,1),e(2,2,1),e(3,4,1),e(4,5,1),e(5,6,1)]
    yield 'cycles_ids_one_and_eleven',[e(1,0,2,parent=11),e(11,1,3,parent=1),e(2,2,None,parent=1),e(3,3,5,parent=99)]
    yield 'branched_corrections_cutoff',[e(1,0,10),e(2,2,20,parent=1),e(3,2,None,parent=1),e(4,366,50,parent=2),e(5,367,70,owner=2)]
    yield 'fifo_partial_many_to_many',[e(1,0,7,'A'),e(2,1,8,'A'),e(3,2,3,'B'),e(4,3,6,'B'),e(5,4,10,'B')]
    yield 'equal_remainders',[e(1,0,1,owner=1),e(2,0,1,owner=2),e(3,0,1,owner=3)]
    yield 'pareto_boundary_complete_ties',[e(1,0,80,owner=1),e(2,0,10,owner=2),e(3,0,10,owner=3),e(4,0,0,owner=4)]
    yield 'leap_and_year_boundaries',[e(1,-1,1),e(2,59,2,'B'),e(3,365,3,'C'),e(4,366,4,owner=2)]
    yield 'latest_compatible_funnel',[e(1,0,1,'B'),e(2,1,1,'A'),e(3,2,1,'B'),e(4,3,1,'A'),e(5,4,1,'B'),e(6,5,1,'C')]
    yield 'transformed_text_is_not_category_role',[e(1,0,5,'token-one')+['A'],e(2,1,3,'token-two')+['B'],e(3,2,1,'token-three')+['C']]
    yield 'four_decimal_remainders',[e(1,0,'.0002',owner=1),e(2,0,'.0001',owner=2),e(3,0,'.0003',owner=3)]
    yield 'fractional_fifo_and_centered_scores',[e(1,0,'.0001','A'),e(2,1,'.0002','A'),e(3,2,'.0002','B'),e(4,3,'.0002','B'),e(5,40,'.0001','C')]
    yield 'fractional_session_growth',[e(1,0,'.0001'),e(2,31,'.0002'),e(3,62,'.0003')]
    rng=random.Random(193)
    for k in range(12):
        rows=[]
        for n in range(1,18):
            rows.append(e(n,rng.choice([-2,0,1,2,3,29,30,31,59,60,365,366]),rng.choice([None,-3,0,1,2,3,10,100]),rng.choice(['A','B','C']),rng.choice([None,*range(1,n)]) if n>1 else None,rng.randint(1,4)))
        yield f'deterministic_generated_{k:02d}',rows


def validate_edges(con,recipes):
    cur=con.cursor()
    cur.execute('CREATE TABLE #InterviewE(EventID int PRIMARY KEY,OwnerID int NOT NULL,ActivityDate date NOT NULL,MetricValue decimal(28,4) NULL,Segment nvarchar(100) NULL,ParentID int NULL,Kind nvarchar(100) NULL); CREATE TABLE #InterviewOwners(OwnerID int PRIMARY KEY); INSERT #InterviewOwners VALUES(1),(2),(3),(4),(5);')
    count=0;failures=[];case_count=0
    for name,rows in cases():
        case_count+=1;cur.execute('DELETE FROM #InterviewE')
        if rows:cur.executemany('INSERT #InterviewE VALUES(?,?,?,?,?,?,?)',[r+[r[4]] if len(r)==6 else r for r in rows])
        e=events(rows);level_index={}
        for recipe in recipes:
            n=level_index.get(recipe['level'],0);level_index[recipe['level']]=n+1
            if recipe['level']=='Advanced' and n==14:continue
            label=f'edge/{name}/{recipe["level"]}{n+1:02d}'
            try:
                expected=sorted_result(recipe,calculate(recipe['level'],n,e,[1,2,3,4,5]))
                actual=[tuple(r) for r in cur.execute(query_from_population(recipe)).fetchall()]
                compare(actual,expected,recipe['columns'],label);count+=1
            except Exception as exc:failures.append(dict(id=label,error=str(exc)))
    return dict(adversarial_populations=case_count,adversarial_result_comparisons=count,errors=failures)
