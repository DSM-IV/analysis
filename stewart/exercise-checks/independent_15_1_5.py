"""Numerical quadrature independently verifies selected symbolic computations."""
import json,sympy as s,mpmath as mp
from pathlib import Path
root=Path(__file__).resolve().parents[1]
mp.mp.dps=24
out=[]
for sec in range(1,6):
 data=json.loads((root/f'exercise-checks/s15-{sec}-report.json').read_text());checks=[q for q in data['checks'] if q['method']=='exact sequential symbolic integration']
 indices=sorted(set([0,len(checks)-1]+list(range(0,len(checks),max(1,len(checks)//12)))))
 for ix in indices:
  q=checks[ix];names=set()
  for li in q['limits']:names.add(li[0])
  loc={nm:s.Symbol(nm,real=True) for nm in names}
  expr=s.sympify(q['integrand'],locals=loc);lims=[(loc[v],s.sympify(lo,locals=loc),s.sympify(hi,locals=loc)) for v,lo,hi in q['limits']];expected=s.sympify(q['value'],locals=loc)
  syms=set().union(expr.free_symbols,expected.free_symbols,*[lo.free_symbols|hi.free_symbols for v,lo,hi in lims])-set(loc.values())
  params={ss:s.Rational({'a':1,'b':2,'h':3,'k':1,'R':2}.get(str(ss),1)) for ss in syms};expr=expr.subs(params);lims=[(v,lo.subs(params),hi.subs(params)) for v,lo,hi in lims];expected=expected.subs(params)
  # Some one-variable symbolic results still depend on a fixed parameter x or y.
  remaining=(expr.free_symbols|expected.free_symbols|set().union(*[lo.free_symbols|hi.free_symbols for v,lo,hi in lims]))-set(loc.values())
  subst={ss:s.Rational(1,2) for ss in remaining};expr=expr.subs(subst);expected=expected.subs(subst);lims=[(v,lo.subs(subst),hi.subs(subst)) for v,lo,hi in lims]
  def rec(i,env):
   if i<0:return mp.mpf(str(s.N(expr.subs(env),27)))
   v,lo,hi=lims[i];lv=mp.mpf(str(s.N(lo.subs(env),27)).replace('oo','inf'));hv=mp.mpf(str(s.N(hi.subs(env),27)).replace('oo','inf'))
   if i==0:
    fn=s.lambdify(v,expr.subs(env),'mpmath');return mp.quad(fn,[lv,hv])
   return mp.quad(lambda z:rec(i-1,{**env,v:z}),[lv,hv])
  numeric=rec(len(lims)-1,{});want=mp.mpf(str(s.N(expected,27)));err=abs(numeric-want);assert err<mp.mpf('1e-9')*max(1,abs(want)),(sec,ix,numeric,want)
  out.append({'section':f'15.{sec}','symbolicCheckIndex':ix,'integrand':q['integrand'],'parameters':{str(k):str(v) for k,v in params.items()},'numerical':str(numeric),'symbolicNumerical':str(want),'absoluteError':str(err)})
(root/'exercise-checks/s15-1-5-independent-report.json').write_text(json.dumps({'method':'independent24dps mpmath quadrature versus exact SymPy values','verified':len(out),'checks':out},indent=2)+'\n')
print('Independent quadrature passed',len(out))
