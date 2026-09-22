import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s7-2.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,79))
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
for q in map(mp.mpf,['-2','-.7','.4','2','3.6']):
 F=lambda t:mp.sin(t)-mp.sin(t)**3/3+mp.mpf(3)/4*abs(mp.sin(t))**(mp.mpf(4)/3)-mp.mpf(3)/10*abs(mp.sin(t))**(mp.mpf(10)/3)
 f=(1+mp.sign(mp.sin(q))*abs(mp.sin(q))**(mp.mpf(1)/3))*mp.cos(q)**3
 near(mp.diff(F,q),f,f'14 real cube-root derivative t={q}')
for q in map(mp.mpf,['-.4','2','3.5']):
 near(mp.diff(lambda t:mp.log(abs(mp.sin(t)))-mp.sin(t)**2/2,q),mp.cos(q)**3/mp.sin(q),f'17 negative-log-argument branches {q}')
 near(mp.diff(lambda t:mp.tan(t)**4/4-mp.tan(t)**2/2-mp.log(abs(mp.cos(t))),q),mp.tan(q)**5,f'31 logarithm branches {q}')
I=mp.quad(lambda x:mp.tan(x)**6/mp.cos(x),[0,mp.pi/4]);J=mp.quad(lambda x:mp.tan(x)**8/mp.cos(x),[0,mp.pi/4]);near(J,(mp.sqrt(2)-7*I)/8,'61 linear relation')
near(mp.quad(lambda x:mp.sin(x)**2*mp.cos(x)**3,[-mp.pi,0,mp.pi]),0,'63 even function with zero mean')
near(mp.quad(lambda x:mp.sin(x)**2-mp.sin(x)**3,[0,mp.pi]),mp.pi/2-mp.mpf(4)/3,'65 area')
near(mp.quad(lambda x:mp.tan(x)-mp.tan(x)**2,[0,mp.pi/4]),mp.log(2)/2-1+mp.pi/4,'66 area')
near(mp.pi*mp.quad(lambda x:(1-mp.sin(x))**2-(1-mp.cos(x))**2,[0,mp.pi/4]),mp.pi*(2*mp.sqrt(2)-mp.mpf(5)/2),'71 shifted washer')
V72=mp.pi*(mp.sqrt(3)+2*mp.log(2+mp.sqrt(3))-mp.pi/6-mp.sqrt(3)/8-mp.sqrt(3))
near(mp.pi*mp.quad(lambda x:(1/mp.cos(x)+1)**2-(mp.cos(x)+1)**2,[0,mp.pi/3]),V72,'72 shifted washer')
near(mp.sqrt(60*mp.quad(lambda t:(155*mp.sin(120*mp.pi*t))**2,[0,mp.mpf(1)/60])),155/mp.sqrt(2),'74 RMS')
for m,n in [(1,1),(1,3),(2,4),(5,5)]:
 near(mp.quad(lambda x:mp.sin(m*x)*mp.cos(n*x),[-mp.pi,0,mp.pi]),0,f'75 sine-cosine {m},{n}')
 near(mp.quad(lambda x:mp.sin(m*x)*mp.sin(n*x),[-mp.pi,0,mp.pi]),mp.pi if m==n else 0,f'76 sine orthogonality {m},{n}')
 near(mp.quad(lambda x:mp.cos(m*x)*mp.cos(n*x),[-mp.pi,0,mp.pi]),mp.pi if m==n else 0,f'77 cosine orthogonality {m},{n}')
for m,am in [(1,2),(2,-3),(3,5)]:near(mp.quad(lambda x:(2*mp.sin(x)-3*mp.sin(2*x)+5*mp.sin(3*x))*mp.sin(m*x),[-mp.pi,0,mp.pi])/mp.pi,am,f'78 recovered coefficient {m}')
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:
    assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
    assert not re.search(r'\\(?:quad|qquad)[A-Za-z]',v),(e['number'],key,v)
    assert 'G_{'not in v and 'otherwise'not in v,(e['number'],'unsimplified CAS')
report={'section':'7.2','count':78,'sourcePDFPages':[573,574,575],'sourceVisualReview':'All three exercise pages rendered and inspected; real cube-root14, square-root49–50, cosine-squared velocity73 verified visually.','authorChecks':'All1–60 primitives independently differentiated at three points; definite integrals compared with numerical quadrature.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'browserVisualReview':'57 integrand/primitive graph inspected in Chrome.','status':'passed'}
(ROOT/'exercise-checks/calc1-s7-2-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('PASS',len(E),'exercises',len(checks),'independent checks')
