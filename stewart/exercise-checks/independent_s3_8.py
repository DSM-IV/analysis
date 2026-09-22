"""Bracketed root verification independent of Newton iteration."""
from pathlib import Path
import json,mpmath as m,sympy as s
m.mp.dps=65;x=s.symbols('x');checks=[];report=json.loads(Path(__file__).with_name('s3-8-report.json').read_text())
P={13:lambda x:3*x**4-8*x**3+2,14:lambda x:-2*x**5+9*x**4-7*x**3-11*x,15:lambda x:m.cos(x)-x*x+4,16:lambda x:3*m.sin(x)-x,17:lambda x:m.sin(x)-x+1,18:lambda x:m.cos(2*x)-x**3,19:lambda x:x**4-x**3-1,20:lambda x:(x-1)**4-x,21:lambda x:x**3-m.cos(x),22:lambda x:x**3-5*x+3,23:lambda x:-2*x**7-5*x**4+9*x**3+5,24:lambda x:x**5-3*x**4+x**3-x*x-x+6,25:lambda x:x/(1+x*x)-m.sqrt(1-x),26:lambda x:m.cos(x*x-x)-x**4,33:lambda x:6*x**5-4*x**3+9*x*x-2,34:lambda x:m.cos(x)-x*m.sin(x),35:lambda x:(2-x*x)*m.sin(x)+4*x*m.cos(x),36:lambda x:m.sin(x)-x*m.cos(x),37:lambda x:2*x+4*(x-1)**3,38:lambda x:m.sin(x/2)-m.mpf('.4')*x,39:lambda x:375/x*(1-(1+x)**-60)-18000}
for rec in report['newtonRuns']:
 n=rec['exercise']
 if n not in P:continue
 f=P[n];v=m.mpf(rec['iterations'][-1]);delta=m.mpf('0.00001');a=v-delta;b=v+delta;assert f(a)*f(b)<0,(n,v)
 for j in range(180):
  c=(a+b)/2
  if f(a)*f(c)<=0:b=c
  else:a=c
 assert abs((a+b)/2-v)<m.mpf('1e-23'),(n,v)
 checks.append(str(n)+' Newton root agrees with independent bisection')
 if n==19:
  z=v**3;assert abs(1/z-(m.sign(z)*abs(z)**(m.mpf(1)/3)-1))<m.mpf('1e-23');checks.append('19 original real cube-root equation')
 if n==20:assert abs((v-1)**2-m.sqrt(v))<m.mpf('1e-23');checks.append('20 original unsquared equation')
for n,p,k in[(19,x**4-x**3-1,2),(20,(x-1)**4-x,2),(22,x**3-5*x+3,3),(23,-2*x**7-5*x**4+9*x**3+5,3),(24,x**5-3*x**4+x**3-x*x-x+6,3),(33,6*x**5-4*x**3+9*x*x-2,3)]:assert s.Poly(p,x).count_roots(-s.oo,s.oo)==k;checks.append(str(n)+' Sturm count')
Path(__file__).with_name('s3-8-independent.json').write_text(json.dumps({'section':'3.8','passed':len(checks),'checks':checks},indent=2)+'\n');print('PASS',len(checks),'independent checks')
