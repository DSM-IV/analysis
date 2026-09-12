import json
from pathlib import Path
import sympy as s
x,h=s.symbols('x h',real=True);checks=[]
def eq(n,L,R,method):
 q=s.simplify(L-R);assert q==0,(n,q);checks.append(dict(number=n,method=method,residual=str(q)))
for t,v,w in [(5,694,s.Rational(-444,10)),(10,444,s.Rational(-388,10)),(20,111,s.Rational(-278,10)),(25,28,s.Rational(-222,10)),(30,0,s.Rational(-50,3))]:eq(1,s.Rational(v-250,t-15),w,'independent table difference')
for aa,bb,delta,w in [(3438,7398,40,99),(4559,5622,10,s.Rational(1063,10)),(5622,6536,10,s.Rational(914,10))]:eq(2,s.Rational(bb-aa,delta),w,'independent table difference')
for n,expr,at,want in [(3,1/(1-x),2,1),(4,s.cos(s.pi*x),s.Rational(1,2),-s.pi),(5,275-16*x*x,4,-128),(6,10*x-s.Rational(186,100)*x*x,1,s.Rational(628,100)),(8,2*s.sin(s.pi*x)+3*s.cos(s.pi*x),1,-2*s.pi),(9,s.sin(10*s.pi/x),1,-10*s.pi)]:
 eq(n,s.diff(expr,x).subs(x,at),want,'independent analytic derivative')
 if n in [3,5,6]:eq(n,s.limit((expr.subs(x,at+h)-expr.subs(x,at))/h,h,0),want,'independent difference quotient limit')
for aa,bb,dt,w in [('20.6','79.2',2,'29.3'),('46.5','79.2',1,'32.7'),('79.2','124.8',1,'45.6'),('79.2','176.7',2,'48.75')]:eq(7,(s.Rational(bb)-s.Rational(aa))/dt,s.Rational(w),'independent position differences')
eq(7,(s.Rational('32.7')+s.Rational('25.9'))/2,s.Rational('29.3'),'centered slope average')
root=Path(__file__).resolve().parents[1];(root/'exercise-checks/s1-4-independent.json').write_text(json.dumps({'section':'1.4','passed':len(checks),'checks':checks},ensure_ascii=False,indent=2)+'\n');print(len(checks),'checks passed')
