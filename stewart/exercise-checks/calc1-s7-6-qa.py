import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s7-6.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,49))
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
for z in [mp.mpf(-2),mp.mpf(2)]:
 near(mp.diff(lambda t:(mp.sqrt(t**6-5)-mp.sqrt(5)*mp.acos(mp.sqrt(5)/abs(t**3)))/3,z),mp.sqrt(z**6-5)/z,f'6 signed radical {z}')
 near(mp.diff(lambda y:-mp.sqrt(2*y*y-3)/y+mp.sqrt(2)*mp.log(abs(y+mp.sqrt(y*y-mp.mpf(3)/2))),z),mp.sqrt(2*z*z-3)/z**2,f'12 signed log {z}')
for z in [mp.mpf('.02'),mp.mpf('30')]:near(mp.diff(lambda x:mp.sqrt(mp.log(x)**2-9)-3*mp.acos(3/abs(mp.log(x))),z),mp.sqrt(mp.log(z)**2-9)/(z*mp.log(z)),f'28 disjoint log branches {z}')
near(mp.quad(lambda x:x**3*mp.sqrt(4*x*x-x**4),[0,2]),2*mp.pi,'24 quartic radical definite integral')
near(mp.pi*mp.quad(lambda x:mp.sin(x)**4,[0,mp.pi]),3*mp.pi**2/8,'35 volume radius squared')
near(2*mp.pi*mp.quad(lambda x:x*mp.asin(x),[0,1]),mp.pi**2/4,'36 arcsine shell volume')
u=s.symbols('u',real=True);a=s.symbols('a',positive=True);b=s.symbols('b',nonzero=True,real=True)
F=(a+b*u-a*a/(a+b*u)-2*a*s.log(a+b*u))/b**3
assert s.simplify(s.diff(F,u)-u*u/(a+b*u)**2)==0;checks.append('37 table53 symbolic differentiation')
F=u*(2*u*u-a*a)*s.sqrt(a*a-u*u)/8+a**4*s.asin(u/a)/8
assert s.simplify(s.diff(F,u)-u*u*s.sqrt(a*a-u*u))==0;checks.append('38 table31 symbolic differentiation')
root=lambda x:mp.sign(x)*abs(x)**(mp.mpf(1)/3)
F46=lambda x:mp.mpf(2)/5*(3*root(x)**2-4*root(x)+8)*mp.sqrt(1+root(x))
for z in map(mp.mpf,['-.8','-.1','.1','8']):near(mp.diff(F46,z),1/mp.sqrt(1+root(z)),f'46 real cube root {z}')
for z in map(mp.mpf,['-.8','-.2','.2','.8']):
 F=lambda x:mp.log(abs(x/(1+mp.sqrt(1-x*x))))
 near(mp.diff(F,z),1/(z*mp.sqrt(1-z*z)),f'47 absolute-log domain {z}')
 if z>0:near(F(z),-mp.acosh(1/z),f'47 positive CAS branch {z}')
for z in [mp.mpf('.2'),mp.exp(-1),mp.mpf(2)]:
 F=lambda x:(x*mp.log(x)*mp.sqrt(1+(x*mp.log(x))**2)+mp.asinh(x*mp.log(x)))/2
 near(mp.diff(F,z),(1+mp.log(z))*mp.sqrt(1+(z*mp.log(z))**2),f'48 composite primitive {z}')
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:
    assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
    assert not re.search(r'\\(?:quad|qquad)[A-Za-z]',v),(e['number'],key,v)
report={'section':'7.6','count':48,'sourcePDFPages':[602,603],'referencePDFPages':[1425,1426,1427,1428,1429],'sourceVisualReview':'Both exercise pages and all five integral-table pages visually inspected.','authorChecks':'Primitive derivatives and definite quadrature; actual SymPy CAS results recorded in calc1-s7-6-cas-results.json.','independentChecks':checks,'figureCount':0,'status':'passed'}
(ROOT/'exercise-checks/calc1-s7-6-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('PASS',len(E),'exercises',len(checks),'independent checks')
