"""Independently sample each integration order against geometric inequalities."""
import json, math, random
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[1]
report=json.loads((root/'exercise-checks/s15-6-report.json').read_text())
x,y,z=s.symbols('x y z')
regions={
 33:(lambda x,y,z:0<=y<=4-x*x-4*z*z,[-2.2,2.2,-.2,4.2,-1.2,1.2]),
 34:(lambda x,y,z:-2<=x<=2 and y*y+z*z<=9,[-2.2,2.2,-3.2,3.2,-3.2,3.2]),
 35:(lambda x,y,z:x*x<=y and z>=0 and y+2*z<=4,[-2.2,2.2,-.2,4.2,-.2,2.2]),
 36:(lambda x,y,z:x<=2 and y<=2 and z>=0 and x+y>=2+2*z,[-.2,2.2,-.2,2.2,-.2,1.2]),
 37:(lambda x,y,z:0<=x<=y*y and y>=0 and z>=0 and y+z<=1,[-.1,1.1,-.1,1.1,-.1,1.1]),
 38:(lambda x,y,z:x>=0 and y>=0 and z>=0 and y<=1-x and z<=1-x*x,[-.1,1.1,-.1,1.1,-.1,1.1]),
 39:(lambda x,y,z:0<=z<=y<=x<=1,[-.1,1.1]*3),
 40:(lambda x,y,z:0<=x<=z<=1 and 0<=y<=z,[-.1,1.1]*3)}
rng=random.Random(156)
checks=[]
for record in report['checks']:
    n=record['number']
    if n not in regions:continue
    predicate,box=regions[n]
    compiled=[]
    for order in record['orders']:
        compiled.append([(str(v),s.lambdify((x,y,z),s.sympify(lo),'math'),s.lambdify((x,y,z),s.sympify(hi),'math')) for v,lo,hi in reversed(order)])
    for _ in range(2000):
        p=[rng.uniform(box[2*j],box[2*j+1]) for j in range(3)]
        expected=predicate(*p)
        coords=dict(zip(('x','y','z'),p))
        for order in compiled:
            actual=True
            for v,lo,hi in order:
                if not lo(*p)<=coords[v]<=hi(*p):actual=False;break
            assert actual==expected,(n,p,expected,order)
    checks.append({'number':n,'sampleCount':2000,'orders':6,'passed':True})
    print('PASS',n,': 2000 points × 6 orders')
(root/'exercise-checks/s15-6-order-sampling.json').write_text(json.dumps({'seed':156,'checks':checks,'limitation':'Sampling supplements the analytic equivalent-inequality proofs; it is not itself a proof.'},indent=2)+'\n')
