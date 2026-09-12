#!/usr/bin/env python3
"""Independent mathematical checks for Stewart 9e §§16.6–16.7.
Run with /opt/homebrew/bin/python3 stewart/exercise-checks/s16-6-7-verify.py.
Requires SymPy and mpmath. Source images: PDF pages1255–1257,1267–1269.
"""
import json
from pathlib import Path
import sympy as s
import mpmath as m
x,y,z,u,v,t=s.symbols('x y z u v t',real=True)
checks=[]
def exact(name,got,want):
 delta=s.simplify(got-want)
 assert delta==0,(name,got,want,delta)
 checks.append({'exercise':name,'kind':'symbolic','result':str(s.simplify(got))})
# Parametric coordinate/normal checks, independently deriving the cross product.
for n,r,uv,N in [
 (33,s.Matrix([u+v,3*u*u,u-v]),{u:1,v:1},s.Matrix([3,-1,3])),
 (34,s.Matrix([u*u+1,v**3+1,u+v]),{u:2,v:1},s.Matrix([3,4,-12])),
 (35,s.Matrix([u*s.cos(v),u*s.sin(v),v]),{u:1,v:s.pi/3},s.Matrix([s.sqrt(3),-1,2])),
 (36,s.Matrix([s.sin(u),s.cos(u)*s.sin(v),s.sin(v)]),{u:s.pi/6,v:s.pi/6},s.Matrix([1,2*s.sqrt(3),-3])),
 (37,s.Matrix([u*u,2*u*s.sin(v),u*s.cos(v)]),{u:1,v:0},s.Matrix([1,0,-2])),
 (38,s.Matrix([1-u*u-v*v,-v,-u]),{u:1,v:1},s.Matrix([1,-2,-2]))]:
 exact(f'16.6.{n} tangent u',r.diff(u).subs(uv).dot(N),0)
 exact(f'16.6.{n} tangent v',r.diff(v).subs(uv).dot(N),0)
for n,got,want in[
 (43,s.integrate(s.sqrt(1+x+y),(x,0,1),(y,0,1)),s.Rational(4,15)*(9*s.sqrt(3)-8*s.sqrt(2)+1)),
 (44,s.integrate(x*s.sqrt(2+16*x*x),(x,0,1)),13*s.sqrt(2)/12),
 (46,2*s.integrate(s.sqrt(2+4*z*z),(z,0,2)),6*s.sqrt(2)+s.asinh(2*s.sqrt(2))),
 (49,s.integrate(v*v+2*u*u,(u,0,1),(v,0,2)),4),
 (57,3*s.integrate(s.sqrt(5+(3+8*y)**2),(y,0,1)),s.Rational(3,16)*(30*s.sqrt(14)+5*s.log((11+3*s.sqrt(14))/(3+s.sqrt(14)))))]:
 if n==57:
  assert abs(float((got-want).evalf()))<1e-12
  checks.append({'exercise':'16.6.57','kind':'symbolic expression and 12-digit comparison','result':str(want)})
 else:exact(f'16.6.{n}',got,want)
# Multiple coverage: polar representation of geometric cone vs supplied disk.
cone=s.sqrt(2)*2*s.pi*s.integrate(t**3,(t,0,1))
param=4*s.sqrt(2)*2*s.pi*s.integrate(t**7,(t,0,1))
exact('16.7.8 geometric area integral',cone,s.pi/s.sqrt(2))
exact('16.7.8 double coverage',param,2*cone)
for n,got,want in[
 (9,s.integrate(x*x*y*(1+2*x+3*y),(x,0,3),(y,0,2)),171),
 (10,s.integrate(3*x*(4-2*x-2*y),(y,0,2-x),(x,0,2)),4),
 (12,s.integrate(y*s.sqrt(1+x+y),(x,0,1),(y,0,1)),(-8+16*s.sqrt(2)+36*s.sqrt(3))/105),
 (13,s.pi*s.integrate(t**3*s.sqrt(1+4*t*t),(t,0,1)),s.pi*(25*s.sqrt(5)+1)/120),
 (22,s.integrate(v*s.sin(v)-u*s.sin(v)*s.cos(v)+u*u*s.cos(v),(u,0,1),(v,0,s.pi)),s.pi),
 (23,s.integrate(2*x*x*y+2*y*y*(4-x*x-y*y)+x*(4-x*x-y*y),(x,0,1),(y,0,1)),s.Rational(713,180)),
 (24,-2*s.pi*s.integrate(t*t+t**4,(t,1,3)),-s.Rational(1712,15)*s.pi),
 (28,s.integrate(-x*y*s.sin(y)**2-x**3*s.sin(y)*s.cos(y)+x*y,(x,0,2),(y,0,s.pi)),s.pi**2/2),
 (34,s.integrate(x*y*(x*x-y*y)*s.sqrt(1+4*x*x+4*y*y),(x,0,1),(y,0,2)),-441*s.sqrt(21)/80-5*s.sqrt(5)/48+289*s.sqrt(17)/60),
 (41,2*s.integrate((10-z)*z**3,(z,1,4)),s.Rational(4329,5)),
 (42,10*s.integrate(25-z*z,(z,4,5)),s.Rational(140,3))]:exact(f'16.7.{n}',got,want)
m.mp.dps=20;q=m.quad
numeric={
 '16.6.52':2*m.pi*q(lambda r:r*m.sqrt(1+4*r*r*m.sin(r*r)**2),[0,1]),
 '16.6.53':2*m.pi*q(lambda r:r*m.sqrt(1+4*r*r/(r*r+2)**2),[0,1]),
 '16.6.54':4*q(lambda x:q(lambda y:m.sqrt(1+4*x*x/(1+y*y)**2+4*y*y*(1+x*x)**2/(1+y*y)**4),[0,1-x]),[0,1]),
 '16.6.55a':4*sum(m.sqrt(1+4*(x*x+y*y)/(1+x*x+y*y)**4)for x in[1,3,5]for y in[1,3]),
 '16.6.55b':q(lambda x:q(lambda y:m.sqrt(1+4*(x*x+y*y)/(1+x*x+y*y)**4),[0,1,2,4]),[0,1,2,4,6]),
 '16.6.56':8*q(lambda v:q(lambda u:9*m.cos(v)**4*m.sin(v)*m.cos(u)*m.sin(u)*m.sqrt(m.sin(v)**2+m.cos(v)**2*m.cos(u)**2*m.sin(u)**2),[0,m.pi/2]),[0,m.pi/2]),
 '16.6.58':4*q(lambda u:q(lambda v:u*m.sqrt(36+4*u*u*(9*m.cos(v)**2+4*m.sin(v)**2)),[0,m.pi/2]),[0,2]),
 '16.7.33':q(lambda x:q(lambda y:(x*x+y*y+x*x*m.exp(2*y))*m.sqrt(1+m.exp(2*y)*(1+x*x)),[0,1]),[0,1]),
 '16.7.35':4*q(lambda r:q(lambda t:(1.5*r*r*m.cos(t)**2)*(3*r*r*m.sin(t)**2)*(3-3*r*r)**2*m.sqrt(1+24*r*r*m.cos(t)**2+12*r*r*m.sin(t)**2)*3/m.sqrt(2)*r,[0,m.pi/2]),[0,1])}
expected=[4.1073,3.5618,2.6959,24.2055,24.2476,4.4506,115.6596,4.5822,3.4895]
for (name,val),want in zip(numeric.items(),expected):
 assert abs(float(val)-want)<.00005,(name,val,want)
 checks.append({'exercise':name,'kind':'20-digit quadrature','result':str(val),'rounded4':f'{float(val):.4f}'})
root=Path(__file__).resolve().parents[1]
for sec,count in[('16-6',64),('16-7',49)]:
 d=json.loads((root/f'exercise-content/s{sec}.json').read_text());assert [e['number']for e in d['exercises']]==list(range(1,count+1));assert d['scope']['numbers']==list(range(1,count+1))
 for e in d['exercises']:
  for key in['statement','hint','steps','answer','check']:assert set(e[key])=={'ko','en'}
report={'source':'Stewart Calculus,9e,English','pdfPages':[1255,1256,1257,1267,1268,1269],'counts':{'16.6':64,'16.7':49},'checks':checks,'visualQA':['16.6.12 SVG in Chrome','16.6.32 two views in Chrome','16.6.37 tangent plane overlay in Chrome','16.7.36 cylinder and vector field in Chrome'],'notes':['Source image corrected inherited 16.6.8 z=-v,16.6.11 sin(4v),16.6.12 non-sphere identity.','16.7.8 clearly distinguishes the geometric integral from the double-cover parameter integral.']}
(root/'exercise-checks/s16-6-7-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+chr(10))
print(f'{len(checks)} symbolic/numerical checks passed; 113 exercises structurally complete.')
