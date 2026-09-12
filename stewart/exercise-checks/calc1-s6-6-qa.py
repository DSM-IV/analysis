import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s6-6.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,85))
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
arcsec=lambda x:mp.acos(1/x) if x>0 else 2*mp.pi-mp.acos(1/x)
arccsc=lambda x:mp.asin(1/x) if x>0 else mp.pi-mp.asin(1/x)
for v in map(mp.mpf,['-4','-2','2','4']):
 near(mp.diff(arcsec,v),1/(v*mp.sqrt(v*v-1)),f'20 arcsec book branch at {v}')
 near(mp.diff(arccsc,v),-1/(v*mp.sqrt(v*v-1)),f'21 arccsc book branch at {v}')
 near(mp.diff(lambda q:mp.asin(1/q),v),-1/(abs(v)*mp.sqrt(v*v-1)),f'32 ordinary arcsine chain at {v}')
for v in map(mp.mpf,['-5','-3','3','5']):near(mp.diff(lambda q:arcsec(q/2)/2,v),1/(v*mp.sqrt(v*v-4)),f'70 antiderivative both branches {v}')
for v in map(mp.mpf,['-2','-.5','.5','2']):near((mp.pi/2-mp.atan(v))+(mp.pi/2-mp.atan(1/v)),mp.pi/2 if v>0 else 3*mp.pi/2,f'33 piecewise constant {v}')
x=s.symbols('x',real=True)
for aa in [s.Rational(1,3),-s.Rational(1,3)]:
 f=s.atan(x/aa)+s.log((x-aa)/(x+aa))/2
 assert s.simplify(s.diff(f,x)-2*aa*x*x/(x**4-aa**4))==0
checks.append('37 derivative for positive and negative parameter')
p=5-2*mp.sqrt(5);f=lambda q:mp.atan((3-q)/2)+mp.atan(q/5)
near(mp.diff(f,p),0,'49 optimum derivative');assert f(p)>max(f(0),f(3)) and mp.diff(f,p,2)<0;checks.append('49 global endpoint comparison')
for v in map(mp.mpf,['-.9','-.4','.2','.8']):near(mp.cos(3*mp.asin(v)),(1-4*v*v)*mp.sqrt(1-v*v),f'57 triple-angle identity {v}')
for c in [mp.mpf('.2'),mp.mpf('.7'),mp.mpf('.95')]:
 a=mp.sqrt(1-c*c);f=lambda q:q-c*mp.asin(q);peak=max(abs(1-c*mp.pi/2),a-c*mp.acos(c))
 near(max(f(-1),f(1),f(a),f(-a)),peak,f'58 endpoint/interior absolute extrema c={c}')
near(mp.quad(lambda q:8/(1+q*q),[1/mp.sqrt(3),mp.sqrt(3)]),4*mp.pi/3,'61 independent quadrature')
near(mp.quad(lambda q:mp.asin(q)/mp.sqrt(1-q*q),[0,mp.mpf('.5')]),mp.pi**2/72,'63 independent quadrature')
near(mp.quad(lambda q:1/(1+16*q*q),[0,mp.sqrt(3)/4]),mp.pi/12,'64 independent quadrature')
near(mp.pi*mp.quad(lambda q:1/(q*q+4),[0,2]),mp.pi**2/8,'76 volume quadrature')
near(mp.quad(mp.asin,[0,1]),mp.pi/2-1,'77 original vertical integral quadrature')
for v in map(mp.mpf,['-7','-2','0','.7','2','7']):
 k=int(mp.floor((v+mp.pi/2)/mp.pi));near(mp.asin(mp.sin(v)),(-1)**k*(v-k*mp.pi),f'80 triangular wave {v}')
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
report={'section':'6.6','count':84,'sourcePDFPages':[530,531,532],'sourceVisualReview':'All three exercise pages and the inverse secant/cosecant definitions on PDF527 visually inspected.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'oddAnswerAppendix':'A87 checked; principal ranges and exact odd answers agree.','principalRange':'The book uses quadrant III for negative arcsec/arccsc. Exercise83 explicitly changes to quadrant II.','browserVisualReview':'80 SVG inspected in Chrome: restricted identity and triangular principal arcsine graph render clearly.','status':'passed'}
(ROOT/'exercise-checks/calc1-s6-6-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report)
