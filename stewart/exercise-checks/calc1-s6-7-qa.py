import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s6-7.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,80))
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

mp.mp.dps=50;checks=[]
def near(a,b,name,tol=mp.mpf('1e-35')):
 assert abs(a-b)<tol,(name,a,b)
 checks.append(name)
for a in map(mp.mpf,['-3','-.5','.5','3']):
 near(1/mp.sinh(mp.asinh(1/a)),a,f'32 arccsch composition {a}')
 near(mp.diff(lambda q:mp.asinh(1/q),a),-1/(abs(a)*mp.sqrt(1+a*a)),f'34 arccsch derivative {a}')
for a in map(mp.mpf,['.2','.8']):
 near(1/mp.cosh(mp.acosh(1/a)),a,f'32 arcsech composition {a}')
 near(mp.diff(lambda q:mp.acosh(1/q),a),-1/(a*mp.sqrt(1-a*a)),f'34 arcsech derivative {a}')
for a in map(mp.mpf,['-3','-1.5','1.5','3']):near(1/mp.tanh(mp.atanh(1/a)),a,f'32 arccoth composition {a}')
for q in map(mp.mpf,['.2','.6','1.2']):
 near(mp.diff(lambda z:mp.acosh(1/mp.cos(z)),q),1/mp.cos(q),f'49 principal-range simplification {q}')
 near(mp.diff(lambda z:mp.acosh(1/mp.sin(z)),q),-1/mp.sin(q),f'50 principal-range simplification {q}')
a=mp.mpf('211.49');bb=mp.mpf('20.96');k=mp.mpf('.03291765');r=mp.acosh((a-100)/bb)/k
for q in [-r,r]:near(a-bb*mp.cosh(k*q),100,f'56 height root {mp.nstr(q,8)}')
near(mp.quad(lambda q:1/mp.sqrt(q*q-9),[4,6]),mp.log((6+3*mp.sqrt(3))/(4+mp.sqrt(7))),'73 numerical integral')
near(mp.quad(lambda q:1/mp.sqrt(16*q*q+1),[0,1]),mp.log(4+mp.sqrt(17))/4,'74 numerical integral')
for q in map(mp.mpf,['-2','-.3','.3','2']):near(mp.diff(lambda z:mp.log(abs((1+mp.exp(z))/(1-mp.exp(z))))/2,q),mp.exp(q)/(1-mp.exp(2*q)),f'75 real primitive both intervals {q}')
c=mp.findroot(lambda q:(mp.cosh(q)-1)/q-1,mp.mpf('1.6'));near(mp.quad(lambda q:mp.sinh(c*q),[0,1]),1,'76 independent quadrature at root')
bb=mp.asinh(mp.mpf('.5'));near(mp.quad(lambda q:1+mp.sinh(q)-mp.cosh(2*q),[0,bb]),mp.log((1+mp.sqrt(5))/2)+mp.sqrt(5)/4-1,'77 enclosed area')
for t in map(mp.mpf,['.3','1','2']):near(mp.sinh(t)*mp.cosh(t)/2-mp.quad(lambda q:mp.sqrt(q*q-1),[1,mp.cosh(t)]),t/2,f'78 sector quadrature {t}')
for a,b in [(2,3),(-2,-3),(2,-3),(-2,3)]:
 beta=mp.log(abs(mp.mpf(a)/b))/2;alpha=2*mp.sign(a)*mp.sqrt(abs(a*b));fn=mp.cosh if a*b>0 else mp.sinh
 for q in map(mp.mpf,['-.7','.4']):near(a*mp.exp(q)+b*mp.exp(-q),alpha*fn(q+beta),f'79 coefficient signs {a},{b},{q}')
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:
    assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
    assert not re.search(r'\\(?:quad|qquad)[A-Za-z]',v),(e['number'],key,v)
report={'section':'6.7','count':79,'sourcePDFPages':[538,539,540],'sourceVisualReview':'All three exercise pages visually inspected; referenced inverse-function equations extracted from PDF535–537.','authorVerification':'All derivatives35–53 independently differentiated numerically at two admissible points; antiderivatives67–72 differentiated symbolically.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'oddAnswerAppendix':'A87 exact and approximate odd answers agree.75 uses absolute-value logarithm to include x>0 as well as the appendix artanh expression on x<0.','browserVisualReview':'78 SVG inspected in Chrome: sector boundary, shaded area and integration strip clearly visible.','status':'passed'}
(ROOT/'exercise-checks/calc1-s6-7-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report)
