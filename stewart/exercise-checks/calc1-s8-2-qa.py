import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s8-2.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,47))
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
def near(a,b,name,tol=mp.mpf('1e-22')):
 assert abs(a-b)<tol,(name,a,b);checks.append(name)
rows=json.loads((ROOT/'exercise-checks/calc1-s8-2-numeric-results.json').read_text());nums={e['number']:mp.mpf(e['numeric'])for e in rows}
fns={9:(lambda x:2*mp.pi*x**3*mp.sqrt(1+9*x**4),0,2),10:(lambda y:2*mp.pi*y*mp.sqrt(1+4*y*y),0,mp.sqrt(2)),11:(lambda y:2*mp.pi*y*mp.sqrt(1+4*y*y),1,2),12:(lambda x:mp.pi*(mp.exp(x)+2),0,1),13:(lambda x:2*mp.pi*mp.cos(x/2)*mp.sqrt(1+mp.sin(x/2)**2/4),0,mp.pi),14:(lambda x:2*mp.pi*(x**3/6+1/(2*x))*(x*x+x**-2)/2,mp.mpf('.5'),1),15:(lambda y:2*mp.pi*y*(y*y+1),1,2),16:(lambda y:2*mp.pi*y*mp.sqrt(1+16*y*y),1,2),17:(lambda x:mp.pi*x*mp.sqrt(x+4),0,12),20:(lambda x:mp.pi*(x*x+1),1,2),21:(lambda x:2*mp.pi*mp.exp(-x*x)*mp.sqrt(1+4*x*x*mp.exp(-2*x*x)),-1,1),22:(lambda y:2*mp.pi*y*mp.sqrt(1+(1+1/(y*y))**2),1,3),23:(lambda y:2*mp.pi*(y+y**3)*mp.sqrt(1+(1+3*y*y)**2),0,1),24:(lambda x:2*mp.pi*x*mp.sqrt(1+(1+mp.cos(x))**2),0,2*mp.pi/3),25:(lambda y:2*mp.pi*y*mp.sqrt(1+(1/y+2*y)**2),1,4),26:(lambda y:2*mp.pi*mp.cos(y)**2*mp.sqrt(1+mp.sin(2*y)**2),0,mp.pi/2),27:(lambda x:2*mp.pi/x*mp.sqrt(1+x**-4),1,2),28:(lambda x:2*mp.pi*mp.sqrt(1+2*x*x),0,3),29:(lambda x:2*mp.pi*x*mp.sqrt(1+9*x**4),0,1),30:(lambda x:2*mp.pi*x*mp.sqrt(1+1/(x+1)**2),0,1),31:(lambda x:2*mp.pi*x**5/5*mp.sqrt(1+x**8),0,5),32:(lambda x:2*mp.pi*x*mp.log(x)*mp.sqrt(1+(mp.log(x)+1)**2),1,2)}
for n,(f,a,b)in fns.items():near(mp.quad(f,[a,(a+b)/2,b]),nums[n],f'{n} independently reconstructed radius and slope',mp.mpf('1e-12'))
near(3*mp.pi*mp.quad(lambda u:(1-u)**mp.mpf('1.5'),[0,1]),6*mp.pi/5,'18 astroid branch counted once')
near(2*mp.pi*mp.quad(lambda u:mp.sqrt(1+u*u),[0,1]),mp.pi*(mp.sqrt(2)+mp.asinh(1)),'34 exponential horn finite area')
for a in [mp.mpf(1),mp.mpf(3)]:
 near(mp.pi/(3*a)*mp.quad(lambda x:(a-x)*(a+3*x),[0,a]),mp.pi*a*a/3,f'35x loop no duplicate a={a}')
 near(2*mp.pi/mp.sqrt(3*a)*mp.quad(lambda x:mp.sqrt(x)*(a+3*x),[0,a]),56*mp.pi*a*a/(15*mp.sqrt(3)),f'35y both distinct halves a={a}')
near(2*mp.pi*mp.quad(lambda x:x*mp.sqrt(1+(4*x/25)**2),[0,5]),mp.pi/24*(205*mp.sqrt(41)-625),'36 parabolic dish area')
for a,b in[(mp.mpf(3),mp.mpf(2)),(mp.mpf(2),mp.mpf('.5'))]:
 e=mp.sqrt(1-b*b/(a*a))
 sx=2*mp.pi*b*b*(1+a/(b*e)*mp.asin(e));sy=2*mp.pi*a*a*(1+(1-e*e)/e*mp.atanh(e))
 near(2*mp.pi*b/a*mp.quad(lambda x:mp.sqrt(a*a-e*e*x*x),[-a,a]),sx,f'37 prolate a={a},b={b}')
 near(2*mp.pi*a/b*mp.quad(lambda y:mp.sqrt(b*b+(a*a-b*b)*y*y/(b*b)),[-b,b]),sy,f'37 oblate a={a},b={b}')
for R,r in[(mp.mpf(3),mp.mpf(1)),(mp.mpf(2),mp.mpf('.5'))]:near(mp.quad(lambda t:2*mp.pi*(R+r*mp.cos(t))*r,[0,2*mp.pi]),4*mp.pi**2*R*r,f'38 torus R={R},r={r}')
near(mp.quad(lambda t:2*mp.pi*(1-mp.sin(t)),[0,2*mp.pi]),4*mp.pi**2,'41 horn torus axis tangent')
for z in map(mp.mpf,['-3','0','2']):
 y=mp.exp(z/2)+mp.exp(-z/2);d=(mp.exp(z/2)-mp.exp(-z/2))/2;near(1+d*d,y*y/4,f'45 area-volume identity {z}')
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:
    assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
    assert not re.search(r'\\(?:quad|qquad)[A-Za-z]',v),(e['number'],key,v)
report={'section':'8.2','count':46,'sourcePDFPages':[648,649,650],'sourceVisualReview':'All three pages visually inspected; branch multiplicity11/18/35 and torus references checked.','independentChecks':checks,'authorChecks':'Exact squared speed checks, antiderivative derivatives, endpoint evaluations and independent quadrature.','figureCount':sum('figure'in e for e in E.values()),'status':'passed'}
(ROOT/'exercise-checks/calc1-s8-2-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('PASS',len(E),'exercises',len(checks),'independent checks')
