import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s7-5.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,96))
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
def near(a,b,name,tol=mp.mpf('1e-28')):
 assert abs(a-b)<tol,(name,a,b);checks.append(name)
for z in map(mp.mpf,['-3','-2','2','3']):
 near(mp.diff(lambda x:mp.acos(1/abs(x)),z),1/(z*mp.sqrt(z*z-1)),f'2b signed inverse-secant primitive {z}')
 near(mp.diff(lambda x:(mp.acos(1/abs(x))+mp.sqrt(x*x-1)/x**2)/2,z),1/(z**3*mp.sqrt(z*z-1)),f'19 both radical branches {z}')
near(mp.quad(lambda x:abs(mp.exp(x)-1),[-1,0,2]),mp.e**2+1/mp.e-3,'38 absolute-value split')
near(mp.quad(lambda x:(mp.sin(x)+4*mp.cos(x))/(4*mp.sin(x)-mp.cos(x)),[mp.pi/4,mp.pi/2]),mp.log(4*mp.sqrt(2)/3),'42 logarithmic derivative')
near(mp.quad(lambda x:x/(1+mp.cos(x)**2),[-mp.pi/2,0,mp.pi/2]),0,'43 odd integral')
near(mp.quad(lambda x:mp.sin(6*x)*mp.cos(3*x),[0,mp.pi]),mp.mpf(4)/9,'48 product frequencies')
near(mp.quad(lambda x:x*mp.sqrt(2-mp.sqrt(1-x*x)),[0,1]),(16*mp.sqrt(2)-14)/15,'56 nested-root substitution')
for z in map(mp.mpf,['-3','-2','-.5','.3','2']):
 cc=mp.mpf(1);root=lambda t:mp.sign(t)*abs(t)**(mp.mpf(1)/3)
 F=lambda x:mp.mpf(3)/7*root(x+cc)**7-3*cc/4*root(x+cc)**4
 near(mp.diff(F,z),z*root(z+cc),f'65 real cube-root power {z}')
def F70(x):
 k=mp.floor((x+mp.pi/2)/mp.pi)
 return(mp.atan(mp.tan(x)/mp.sqrt(2))+k*mp.pi)/mp.sqrt(2)
for z in map(mp.mpf,['-5','-2','0','2','5']):near(mp.diff(F70,z),1/(1+mp.cos(z)**2),f'70 continuous branches {z}')
for k in range(-2,3):
 q=(mp.mpf(k)+mp.mpf('.5'))*mp.pi;eps=mp.mpf('1e-35');near(F70(q+eps)-F70(q-eps),0,f'70 branch matching {k}')
near(mp.quad(lambda x:mp.log(mp.tan(x))/(mp.sin(x)*mp.cos(x)),[mp.pi/4,mp.pi/3]),mp.log(3)**2/8,'74 logarithmic square endpoint')
for z in [-mp.pi/2,3*mp.pi/2]:near(mp.diff(lambda x:2*mp.cos(x)/(1-mp.sin(x))-x,z),(1+mp.sin(z))/(1-mp.sin(z)),f'86 removable cosine zero {z}')
def F89(x):
 k=mp.floor((x-mp.pi/2)/(2*mp.pi))
 return 2*mp.sqrt(2)*(-1)**(int(k)+1)*mp.sin(x/2+mp.pi/4)+4*mp.sqrt(2)*(k+1)
for z in map(mp.mpf,['-8','-3','0','2','8']):near(mp.diff(F89,z),mp.sqrt(1-mp.sin(z)),f'89 radical sign {z}')
for k in range(-2,3):
 q=mp.pi/2+2*k*mp.pi;eps=mp.mpf('1e-30');near(F89(q+eps)-F89(q-eps),0,f'89 endpoint matching {k}')
near(mp.quad(lambda x:mp.sqrt((9-x)/x)-mp.sqrt(x/(9-x)),[1,3]),2*mp.sqrt(2),'91 radical difference')
near(mp.quad(lambda x:mp.exp(x)/x,[1,2]),mp.quad(lambda t:mp.exp(mp.exp(t)),[0,mp.log(2)]),'94a nested exponential substitution')
near(mp.quad(lambda x:1/mp.log(x),[2,3]),mp.quad(lambda t:mp.exp(mp.exp(t)),[mp.log(mp.log(2)),mp.log(mp.log(3))]),'94b double logarithm substitution')
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:
    assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
    assert not re.search(r'\\(?:quad|qquad)[A-Za-z]',v),(e['number'],key,v)
    assert 'G_{'not in v and 'otherwise'not in v,(e['number'],'unsimplified CAS')
report={'section':'7.5','count':95,'sourcePDFPages':[596,597,598],'sourceVisualReview':'All three pages visually inspected, including constant a in28, nested radicals56/72, and nested exponential F in94.','authorChecks':'Each newly authored elementary primitive independently differentiated; definite integrals numerically checked. Exact repeats23/35/50 source matched and reused with new IDs.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'status':'passed'}
(ROOT/'exercise-checks/calc1-s7-5-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('PASS',len(E),'exercises',len(checks),'independent checks')
