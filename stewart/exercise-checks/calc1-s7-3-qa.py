import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s7-3.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,51))
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
for z in map(mp.mpf,['3','4','-3','-4']):
 F=lambda x:mp.sqrt(4*x*x-25)-5*mp.acos(5/(2*abs(x)))
 near(mp.diff(F,z),mp.sqrt(4*z*z-25)/z,f'7 both domain branches {z}')
for z in map(mp.mpf,['4','5','-4','-5']):
 F=lambda x:mp.acos(3/abs(x))/6-mp.sqrt(x*x-9)/(2*x*x)
 near(mp.diff(F,z),mp.sqrt(z*z-9)/z**3,f'19 both domain branches {z}')
for z in map(mp.mpf,['2','3','-2','-3']):
 F=lambda x:mp.sqrt(x*x-2)*(x*x+1)/(6*x**3)
 near(mp.diff(F,z),1/(z**4*mp.sqrt(z*z-2)),f'42 both domain branches {z}')
near(mp.quad(lambda x:x*x*mp.sqrt(4-x*x),[0,2]),mp.pi,'21 parameter a=2')
near(mp.quad(lambda x:mp.sqrt(1-4*x*x),[mp.mpf(1)/4,mp.sqrt(3)/4]),mp.pi/24,'22 exact symmetric angle interval')
near(mp.quad(lambda x:mp.sqrt(x-x*x),[0,1]),mp.pi/8,'30 shifted semicircle')
for z in map(mp.mpf,['-.3','.3','1.2']):
 U=lambda x:x-1
 F=lambda x:U(x)**3*mp.sqrt(4-U(x)**2)/4-mp.mpf(2)/3*(4-U(x)**2)**mp.mpf('1.5')+4*mp.asin(U(x)/2)
 near(mp.diff(F,z),z*z*mp.sqrt(3+2*z-z*z),f'31 completed-square derivative {z}')
near(mp.quad(lambda x:mp.sqrt(x*x-1)/x,[1,7])/6,(4*mp.sqrt(3)-mp.acos(mp.mpf(1)/7))/6,'39 average')
near(3*mp.quad(lambda x:mp.sqrt(x*x-4),[2,3]),mp.mpf(9)/2*mp.sqrt(5)-6*mp.log((3+mp.sqrt(5))/2),'40 hyperbola area')
near(81*mp.pi*mp.quad(lambda x:1/(x*x+9)**2,[0,3]),3*mp.pi*(mp.pi+2)/8,'43 disks')
near(2*mp.pi*mp.quad(lambda x:(1-x)*x*mp.sqrt(1-x*x),[0,1]),2*mp.pi/3-mp.pi**2/8,'44 offset shells')
near(mp.quad(lambda x:mp.sqrt(8-x*x)-x*x/2,[-2,2]),2*mp.pi+mp.mpf(4)/3,'46 circle-parabola area')
near(mp.pi*mp.quad(lambda x:(3+mp.sqrt(1-x*x))**2-(3-mp.sqrt(1-x*x))**2,[-1,1]),6*mp.pi**2,'47 torus R3 r1')
near(mp.quad(lambda x:2/(x*x+4)**mp.mpf('1.5'),[-1,3]),(3/mp.sqrt(13)+1/mp.sqrt(5))/2,'48 electric-field kernel')
for R in [mp.mpf('1.5'),mp.mpf(2),mp.mpf(5)]:
 d=mp.sqrt(R*R-1)
 near(mp.quad(lambda x:d+mp.sqrt(1-x*x)-mp.sqrt(R*R-x*x),[-1,1]),mp.pi/2-R*R*mp.asin(1/R)+d,f'49 lune R={R},r=1')
near(mp.quad(lambda y:2*mp.sqrt(25-y*y),[-5,2])/(25*mp.pi),mp.mpf('.5')+2*mp.sqrt(21)/(25*mp.pi)+mp.asin(mp.mpf('.4'))/mp.pi,'50 submerged fraction')
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:
    assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
    assert not re.search(r'\\(?:quad|qquad)[A-Za-z]',v),(e['number'],key,v)
    assert 'G_{'not in v and 'otherwise'not in v,(e['number'],'unsimplified CAS')
report={'section':'7.3','count':50,'sourcePDFPages':[580,581],'sourceVisualReview':'Both exercise pages visually inspected, including the lune geometry and parameter bounds.','authorChecks':'Primitives5–36 and42 differentiated independently on admissible points; negative domain branches checked where applicable. Definite integrals numerically compared.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'browserVisualReview':'49 lune and50 submerged tank cross section checked in Chrome.','status':'passed'}
(ROOT/'exercise-checks/calc1-s7-3-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('PASS',len(E),'exercises',len(checks),'independent checks')
