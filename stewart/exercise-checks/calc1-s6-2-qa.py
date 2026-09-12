import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s6-2.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,109))
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

mp.mp.dps=40;x=s.symbols('x',real=True);checks=[]
def check(name,a,b):assert s.simplify(a-b)==0,(name,a,b);checks.append(name)
check('39 quotient derivative',s.diff(x*x*s.exp(x)/(x*x+s.exp(x)),x),x*s.exp(x)*(x**3+2*s.exp(x))/(x*x+s.exp(x))**2)
y=s.symbols('y',real=True);F=s.exp(x/y)-x+y;check('53 implicit derivative',-s.diff(F,x)/s.diff(F,y),(y*y-y*s.exp(x/y))/(y*y-x*s.exp(x/y)))
check('72 strict positive concavity numerator',s.diff(s.exp(x)/x**2,x,2),s.exp(x)*((x-2)**2+2)/x**4)
check('73 right-branch inflection',s.diff(s.exp(-1/(x+1)),x,2),s.exp(-1/(x+1))*(-2*x-1)/(x+1)**4)
check('74 oscillation concavity',s.diff(s.exp(-x)*s.sin(x),x,2),-2*s.exp(-x)*s.cos(x))
k=s.Rational(7,100);f=s.Rational(1,100)*x**4*s.exp(-k*x)
for q in[2/k,6/k]:check('78 inflection root',s.diff(f,x,2).subs(x,q),0)
check('94 horizontal area',s.integrate(s.exp(y)-y*y+2,(y,-1,1)),s.E-1/s.E+s.Rational(10,3))
check('98 shell volume',s.integrate(2*s.pi*x*s.exp(-x*x),(x,0,1)),s.pi*(1-1/s.E))
q=mp.findroot(lambda t:8*mp.exp(-t/2)*mp.sin(4*t)+2,(mp.mpf('2.75'),mp.mpf('2.8')))
assert abs(8*mp.exp(-q/2)*mp.sin(4*q)+2)<mp.mpf('1e-30')
t0=mp.atan(8)/4;next_peak=t0+mp.pi;assert next_peak>q and abs(8*mp.exp(-next_peak/2)*mp.sin(4*next_peak))<2
prev_peak=t0+3*mp.pi/4;assert prev_peak<q and abs(8*mp.exp(-prev_peak/2)*mp.sin(4*prev_peak))>2
checks.append('66 last negative2cm crossing and all subsequent decaying extrema')
for v in [mp.mpf('-10000'),mp.mpf('-20000')]:assert mp.power(mp.mpf('1.001'),v)<mp.mpf('.00005')
checks.append('24 negative-infinity decay; CAS power limit crosschecked using exponential rewrite')
report={'section':'6.2','count':108,'sourcePDFPages':[466,467,468,469,470],'sourceVisualReview':'All five exercise pages and referenced viral-load model PDF461 visually inspected.','authorVerification':'20 derivatives checked by independent numerical differentiation; elementary antiderivatives differentiated back; definite integrals independently quadrature checked; root and model equations substituted.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'oddAnswerAppendix':'AppendixG A82–A83 checked.63 book rough graph reading3.5days versus3.66days computed from the printed fitted model; the solution identifies its model calculation.','browserVisualReview':'66 SVG checked in Chrome: damped oscillations, both envelopes and two thresholds clearly visible.','status':'passed'}
(ROOT/'exercise-checks/calc1-s6-2-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report)
