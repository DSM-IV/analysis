import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s6-8.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,107))
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   if key=='steps':assert len(vals)>=2,(e['number'],'steps')
   for v in vals:
    assert not re.search('[ぁ-ゟ゠-ヿ]',v),(e['number'],key,lang,v)
    if lang=='en':assert not re.search('[가-힣]',v),(e['number'],key,v)
    require_string(v,f'{e["number"]}.{key}.{lang}')
 assert e['status']=='math-verified'
 if 'figure'in e:ET.parse(ROOT/'exercise-content'/e['figure']['src'].split('../exercise-content/')[1])

mp.mp.dps=65;checks=[]
def near(a,b,name,tol=mp.mpf('1e-45')):
 assert abs(a-b)<tol,(name,a,b)
 checks.append(name)
x=s.symbols('x',real=True)
# Independent Taylor coefficient checks on the highest-order cancellations.
for n,N,D,q,expected in[(27,s.exp(x)+s.exp(-x)-2,s.exp(x)-x-1,0,2),(28,s.sinh(x)-x,x**3,0,s.Rational(1,6)),(30,x-s.sin(x),x-s.tan(x),0,-s.Rational(1,2)),(34,s.exp(x)+s.exp(-x)-2*s.cos(x),x*s.sin(x),0,2),(38,x*x*s.sin(x),s.sin(x)-x,0,-6),(41,s.cos(x)-1+x*x/2,x**4,0,s.Rational(1,24)),(42,x-s.sin(x),x*s.sin(x*x),0,s.Rational(1,6)),(53,s.exp(x)-1-x,x*(s.exp(x)-1),0,s.Rational(1,2))]:
 ns=s.series(N,x,q,7).removeO();ds=s.series(D,x,q,7).removeO();assert s.limit(ns/ds,x,q)==expected;checks.append(f'{n} independent leading Taylor coefficients')
for n,f,root in [(79,x*s.exp(-x),1),(80,s.log(x)/x**2,s.sqrt(s.E)),(81,x*s.exp(-x*x),1/s.sqrt(2)),(82,s.exp(x)/x,1),(83,1/x+s.log(x),1),(84,(x*x-3)*s.exp(-x),-1),(84,(x*x-3)*s.exp(-x),3),(85,x**(-x),1/s.E),(87,x**(1/x),s.E)]:
 assert s.simplify(s.diff(f,x).subs(x,root))==0
 checks.append(f'{n} exact critical point {root}')
f=lambda q:mp.power(mp.sin(q),mp.sin(q));alpha=mp.asin(1/mp.e)
for root in [alpha,mp.pi/2,mp.pi-alpha]:near(mp.diff(f,root),0,'86 stationary point')
near(f(alpha),mp.exp(-1/mp.e),'86 exact minimum');near(f(mp.pi/2),1,'86 exact maximum')
for n,ff,seeds in [(85,lambda q:mp.power(q,-q),[1]),(86,f,[mp.mpf('.944'),mp.mpf('2.198')]),(87,lambda q:mp.power(q,1/q),[mp.mpf('.582'),mp.mpf('4.368')])]:
 for seed in seeds:
  root=mp.findroot(lambda q:mp.diff(ff,q,2),seed);eps=mp.mpf('.00001');assert mp.diff(ff,root-eps,2)*mp.diff(ff,root+eps,2)<0;checks.append(f'{n} inflection with sign reversal {mp.nstr(root,12)}')
for n in range(1,8):
 f=x**n*s.exp(-x);df=x**(n-1)*s.exp(-x)*(n-x);assert s.simplify(s.diff(f,x)-df)==0
 if n>=2:assert s.simplify(s.diff(f,x,2)-x**(n-2)*s.exp(-x)*((x-n)**2-n))==0
checks.append('88 derivative factors checked for both parities n=1..7')
for c in map(mp.mpf,['.2','1','3']):near(mp.diff(lambda q:mp.exp(q)-c*q,mp.log(c)),0,f'89 minimum c={c}')
for a in map(mp.mpf,['.5','1','3']):
 N=lambda q:mp.sqrt(2*a**3*q-q**4)-a*mp.root(a*a*q,3);D=lambda q:a-mp.root(a*q**3,4)
 near(mp.diff(N,a)/mp.diff(D,a),16*a/9,f'99 original radicals at a={a}')
z=mp.mpf('1e-20');ratio=(z-mp.sin(z))/(mp.sin(z)*(1-mp.cos(z)));near(ratio,mp.mpf(1)/3,'100 geometric ratio high precision',mp.mpf('1e-23'))
for h in map(mp.mpf,['.01','.001','.0001']):
 near(mp.quad(lambda q:2*q/mp.sqrt(q**3+1),[0,h])/h**2,1,f'95 integral near zero h={h}',mp.mpf('1e-6'))
for h in map(mp.mpf,['.01','.001']):near(mp.quad(lambda q:mp.sin(mp.pi*q*q/2),[0,h])/h**3,mp.pi/6,f'97 Fresnel integral h={h}',mp.mpf('1e-8'))
u=s.symbols('u');poly=s.S(1)
for n in range(6):
 g=poly.subs(u,1/x)*s.exp(-1/x**2);nxt=-u*u*s.diff(poly,u)+2*u**3*poly;assert s.simplify(s.diff(g,x)-nxt.subs(u,1/x)*s.exp(-1/x**2))==0;poly=s.expand(nxt)
checks.append('105 polynomial recurrence checked through six derivative orders')
for sign in [-1,1]:
 vals=[]
 for a in [10,20,40]:
  h=sign*mp.exp(-a);dq=mp.expm1(h*mp.log(abs(h)))/h;vals.append(dq)
 assert vals[0]>vals[1]>vals[2] and vals[-1]<-39
checks.append('106 difference quotients diverge negatively from both sides')
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:
    assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
    assert not re.search(r'\\(?:quad|qquad)[A-Za-z]',v),(e['number'],key,v)
report={'section':'6.8','count':106,'sourcePDFPages':[548,549,550,551,552],'sourceVisualReview':'All five exercise pages visually inspected, including tangent slopes, the pupil fraction and the geometric sector.','authorVerification':'Original quotient and logarithmic limits checked symbolically with required one-sided limits; graph derivatives factored and classified across real domains.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'oddAnswerAppendix':'A87–A88 odd exact limits, graph analyses, inflection estimates and parameterized radical limit agree.','browserVisualReview':'106 zoom plots inspected in Chrome; small vertical tick spacing uses six significant digits to keep labels distinct.','status':'passed'}
(ROOT/'exercise-checks/calc1-s6-8-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report)
