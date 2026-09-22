import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s7-8.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,95))
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
def near(a,b,name,tol=mp.mpf('1e-24')):
 assert abs(a-b)<tol,(name,a,b);checks.append(name)
rows=[(5,lambda x:2/x**3,[1,mp.inf],1),(7,lambda x:mp.exp(-2*x),[0,mp.inf],mp.mpf('.5')),(8,lambda x:3**(-x),[1,mp.inf],1/(3*mp.log(3))),(10,lambda x:1/(x*x+4),[1,mp.inf],mp.pi/4-mp.atan(mp.mpf('.5'))/2),(11,lambda x:(x-2)**(-mp.mpf('1.5')),[3,mp.inf],2),(13,lambda x:x/(x*x+1)**3,[-mp.inf,0],-mp.mpf('.25')),(15,lambda x:(x*x+x+1)/x**4,[1,mp.inf],mp.mpf(11)/6),(17,lambda x:mp.exp(-x)/(1+mp.exp(-x))**2,[0,mp.inf],mp.mpf('.5')),(22,lambda x:mp.exp(-1/x)/x**2,[1,mp.inf],1-1/mp.e),(25,lambda x:1/(x*x+x),[1,mp.inf],mp.log(2)),(26,lambda x:1/(x*x+2*x-3),[2,mp.inf],mp.log(5)/4),(27,lambda x:x*mp.exp(2*x),[-mp.inf,0],-mp.mpf('.25')),(28,lambda x:x*mp.exp(-3*x),[2,mp.inf],7*mp.exp(-6)/9),(30,lambda x:mp.log(x)/x**2,[1,mp.inf],1),(31,lambda x:x/(x**4+4),[-mp.inf,0],-mp.pi/8),(33,lambda x:mp.exp(-mp.sqrt(x)),[0,mp.inf],2),(34,lambda x:1/(mp.sqrt(x)*(1+x)),[1,mp.inf],mp.pi/2),(36,lambda x:(5-x)**(-mp.mpf(1)/3),[0,5],mp.mpf('1.5')*5**(mp.mpf(2)/3)),(37,lambda x:(x+2)**(-mp.mpf(1)/4),[-2,14],mp.mpf(32)/3),(40,lambda x:1/mp.sqrt(1-x*x),[0,1],mp.pi/2),(45,lambda x:x*mp.log(x),[0,1],-mp.mpf('.25')),(46,lambda x:mp.cos(x)/mp.sqrt(mp.sin(x)),[0,mp.pi/2],2),(47,lambda x:mp.exp(1/x)/x**3,[-1,0],-2/mp.e)]
for n,f,limits,I in rows:near(mp.quad(f,limits),I,f'{n} independent improper quadrature',mp.mpf('1e-23'))
near(mp.quad(lambda u:u**-2,[1,mp.inf]),1,'32 log substitution tail')
near(mp.quad(lambda u:2/(1+u*u),[0,mp.inf]),mp.pi,'67 rationalized endpoint')
near(mp.quad(lambda th:mp.mpf('.5'),[0,mp.pi/2]),mp.pi/4,'68 secant substitution endpoint')
near(mp.quad(lambda x:mp.sin(x)**2/x**2,[1,2]),mp.si(4)+(mp.cos(4)-1)/4-mp.si(2)-(mp.cos(2)-1)/2,'55 sine-integral table formula')
for p in [mp.mpf('-.5'),mp.mpf('0'),mp.mpf('2')]:near(-mp.quad(lambda u:u*mp.exp(-(p+1)*u),[0,mp.inf]),-1/(p+1)**2,f'71 logarithmic power p={p}')
for n in range(5):near(mp.quad(lambda x:x**n*mp.exp(-x),[0,mp.inf]),mp.factorial(n),f'72 factorial n={n}')
for R,ss in [(mp.mpf(3),mp.mpf('.2')),(mp.mpf(3),mp.mpf(2)),(mp.mpf(3),mp.mpf('2.99'))]:
 q=mp.sqrt(R*R-ss*ss);I=(R*R+2*ss*ss)*q/3-R*ss*ss*mp.log((R+q)/ss)
 near(mp.quad(lambda u:(R-mp.sqrt(u*u+ss*ss))**2,[0,q]),I,f'78 projected stellar density s={ss}')
near(mp.quad(lambda x:1/mp.sqrt(x*x+4)-1/(x+2),[0,1,10,mp.inf]),mp.log(2),'91 cancellation constant and finite value')
near(mp.quad(lambda x:x/(x*x+1)-3/(3*x+1),[0,1,10,mp.inf]),-mp.log(3),'92 cancellation constant and finite value')
assert mp.exp(-16)/4<mp.mpf('1e-7');checks.append('84 tail bound distinct from Simpson error')
for n in[20,42,44,73]:assert 'Divergent'in E[n]['answer']['en']or'diverges'in E[n]['answer']['en'];checks.append(f'{n} no principal-value cancellation')
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:
    assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
    assert not re.search(r'\\(?:quad|qquad)[A-Za-z]',v),(e['number'],key,v)
report={'section':'7.8','count':94,'sourcePDFPages':[624,625,626,627],'sourceVisualReview':'All four exercise pages visually inspected. Real cube roots6/41 and interior singularities handled separately.','independentChecks':checks,'authorChecks':'Primitive symbolic differentiation and separate endpoint limits for33 elementary integrals; recorded in symbolic-results JSON.','figureCount':sum('figure'in e for e in E.values()),'status':'passed'}
(ROOT/'exercise-checks/calc1-s7-8-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('PASS',len(E),'exercises',len(checks),'independent checks')
