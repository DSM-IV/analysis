import sympy as s,mpmath as mp,json
from pathlib import Path
mp.mp.dps=70
x=s.symbols('x',real=True);checks=[]
def exact(n,expr,want,method):
 v=s.simplify(expr-want);assert v==0,(n,v);checks.append({'number':n,'method':method,'residual':'0'})
for n,f,a,L in [(13,3*x*x+(x+2)**5,-1,4),(14,(x*x+5*x)/(2*x+1),2,s.Rational(14,5)),(15,2*s.sqrt(3*x*x+1),1,4),(16,(4*x*x-2*x+7)**s.Rational(1,3),-2,3),(35,x*s.sqrt(20-x*x),2,8),(36,s.sin(s.tan(s.cos(x))),s.pi/2,0),(37,x*x*s.tan(x),s.pi/4,s.pi**2/16),(38,x**3/s.sqrt(x*x+x-2),2,4)]:
 exact(n,s.limit(f,x,a),L,'independently entered symbolic limit')
for n,original,extension,a,value in [(22,(x*x-x)/(x*x-1),x/(x+1),1,s.Rational(1,2)),(24,(2*x*x-5*x-3)/(x-3),2*x+1,3,7),(25,(x-3)/(x*x-9),1/(x+3),3,s.Rational(1,6)),(26,(x*x-7*x+12)/(x-3),x-4,3,-1),(51,(x**4-1)/(x-1),x**3+x*x+x+1,1,4),(51,(x**3-x*x-2*x)/(x-2),x*x+x,2,6)]:
 exact(n,original,extension,'independent cancellation identity');exact(n,s.limit(original,x,a),value,'independent extension limit')
exact(47,4*s.Rational(2,3)+4,8-2*s.Rational(2,3),'junction equality')
a=b=s.Rational(1,2)
exact(48,4*a-2*b+3,4,'left junction');exact(48,9*a-3*b+3,6-a+b,'right junction')
for n,f,a,b in [(55,-x**3+4*x+1,-1,0),(56,2/x-x+s.sqrt(x),2,3),(57,s.cos(x)-x,0,1),(58,s.sin(x)-x*x+x,1,2),(64,x*x-3+1/x,s.Rational(1,4),1),(64,x*x-3+1/x,1,2),(70,x**3-x+1,-2,-1)]:
 fa=f.subs(x,a);fb=f.subs(x,b);assert s.N(fa*fb)<0;checks.append({'number':n,'method':'independent IVT endpoint signs','values':[str(fa),str(fb)]})
raw=json.loads(Path(__file__).parents[1].joinpath('exercise-content/s1-8.json').read_text())
checksreport=json.loads(Path(__file__).with_name('s1-8-report.json').read_text())
funcs={59:lambda z:mp.cos(z)-z**3,60:lambda z:z**5-z*z+2*z+3,61:lambda z:z**5-z*z-4,62:lambda z:mp.sqrt(z-5)-1/(z+3)}
for item in checksreport['checks']:
 n=item['number'];fn=funcs[n]
 for key in ['bracket','roundingBracket']:
  a,b=map(lambda v:mp.mpf(str(v)),item[key]);assert fn(a)*fn(b)<0
  # independent bisection, rather than the author's secant-based root solver
  lo,hi=a,b
  for _ in range(100):
   mid=(lo+hi)/2
   if fn(lo)*fn(mid)<=0:hi=mid
   else:lo=mid
  root=(lo+hi)/2
  assert abs(root-mp.mpf(str(item['root'])))<mp.mpf('1e-12')
  checks.append({'number':n,'method':'independent 70-digit bisection of '+key,'root':str(root)})
alpha=(s.sqrt(5)-1)/2;P=x**3+2*x*x-1;Q=x**3+x-2
exact(74,P,(x+1)*(x*x+x-1),'denominator factorization')
exact(74,Q,(x-1)*(x*x+x+2),'denominator factorization')
exact(74,P.subs(x,alpha),0,'inner interval boundary')
assert Q.subs(x,alpha).evalf()<0;exact(74,P.subs(x,1),2,'positive opposite boundary')
checks.append({'number':74,'method':'pole-free interval signs','interval':'((sqrt(5)-1)/2,1)','signP':'+','signQ':'-'})
Path(__file__).with_name('s1-8-independent.json').write_text(json.dumps({'section':'1.8','passed':len(checks),'checks':checks},indent=2)+'\n');print(len(checks),'checks passed')
