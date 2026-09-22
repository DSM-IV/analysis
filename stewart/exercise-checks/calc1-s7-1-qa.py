import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s7-1.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,82))
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
def near(a,b,name,tol=mp.mpf('1e-30')):
 assert abs(a-b)<tol,(name,a,b);checks.append(name)
x=s.symbols('x',positive=True)
for n,f,F in [(2,s.sqrt(x)*s.log(x),s.Rational(2,3)*x**s.Rational(3,2)*s.log(x)-s.Rational(4,9)*x**s.Rational(3,2)),(53,s.sin(x)**4,3*x/8-s.sin(2*x)/4+s.sin(4*x)/32),(54,s.cos(x)**4,3*x/8+s.sin(2*x)/4+s.sin(4*x)/32),(61,s.log(x)**3,x*(s.log(x)**3-3*s.log(x)**2+6*s.log(x)-6)),(62,x**4*s.exp(x),s.exp(x)*(x**4-4*x**3+12*x**2-24*x+24))]:
 assert s.trigsimp(s.expand_trig(s.diff(F,x)-f)).simplify()==0;checks.append(f'{n} independent exact derivative')
for n in range(2,12):near(mp.quad(lambda t:mp.sin(t)**n,[0,mp.pi/2]),mp.mpf(n-1)/n*mp.quad(lambda t:mp.sin(t)**(n-2),[0,mp.pi/2]),f'55 recurrence n={n}')
near(mp.quad(lambda t:(4-t*t)*mp.log(t),[1,2]),-mp.mpf(29)/9+16*mp.log(2)/3,'63 bounded area')
near(mp.quad(lambda t:(t-t*t)*mp.exp(-t),[0,1]),3/mp.e-1,'64 bounded area')
near(2*mp.pi*mp.quad(lambda t:t*(mp.exp(t)-mp.exp(-t)),[0,1]),4*mp.pi/mp.e,'68 shell volume')
near(2*mp.pi*mp.quad(lambda t:(1-t)*mp.exp(-t),[-1,0]),2*mp.pi*mp.e,'69 offset axis volume')
near(2*mp.pi*mp.quad(lambda t:t*mp.log(t),[1,3]),mp.pi*(9*mp.log(3)-4),'70 horizontal shells')
near(mp.pi*mp.quad(lambda t:mp.log(t)**2,[1,2]),2*mp.pi*(mp.log(2)-1)**2,'71b disks')
near(4/mp.pi*mp.quad(lambda t:t/mp.cos(t)**2,[0,mp.pi/4]),1-2*mp.log(2)/mp.pi,'72 average')
for T in [mp.mpf(60),mp.mpf('37.5')]:
 H=-mp.mpf('9.8')*T*T/2+3000*(T+(mp.mpf(30000)/160-T)*mp.log(1-mp.mpf(160)*T/30000))
 near(mp.quad(lambda q:-mp.mpf('9.8')*q-3000*mp.log(1-mp.mpf(160)*q/30000),[0,T]),H,f'74 rocket t={T}')
near(mp.quad(lambda t:t*t*mp.exp(-t),[0,3]),2-17*mp.exp(-3),'75 distance')
w=h=mp.mpf(1);P=mp.mpf(1)
for k in range(1,21):
 w+=1/h;h+=1/w;P*=mp.mpf((2*k)**2)/((2*k-1)*(2*k+1));near(w/h,P,f'80 rectangle pair {k}')
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:
    assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
    assert not re.search(r'\\(?:quad|qquad)[A-Za-z]',v),(e['number'],key,v)
    assert 'G_{'not in v and 'otherwise'not in v,(e['number'],'unsimplified CAS')
report={'section':'7.1','count':81,'sourcePDFPages':[565,566,567],'sourceVisualReview':'All exercise pages inspected as rendered images; checked Greek parameters, negative exponents and the square-root lower bound in45.','authorChecks':'Primitives1–52 differentiated symbolically or on real admissible points; definite integrals numerically cross-checked where no free parameter remains.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'browserVisualReview':'78 inverse-area partition and80 Wallis rectangles visually checked in Chrome.','status':'passed'}
(ROOT/'exercise-checks/calc1-s7-1-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('PASS',len(E),'exercises',len(checks),'independent checks')
