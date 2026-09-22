import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s6-4-alt.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,72))
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

mp.mp.dps=55;checks=[]
def near(a,b,name,tol=mp.mpf('1e-35')):
 assert abs(a-b)<tol,(name,a,b)
 checks.append(name)
near(mp.mpf(2)**36/63360,mp.mpf(1073741824)/990,'19 inch-to-mile exact conversion')
x=s.symbols('x',positive=True)
for n,f,F in[(46,x**5+5**x,x**6/6+5**x/s.log(5)),(47,s.log(x)/(x*s.log(10)),s.log(x)**2/(2*s.log(10))),(49,3**s.sin(x)*s.cos(x),3**s.sin(x)/s.log(3)),(50,2**x/(2**x+1),s.log(2**x+1)/s.log(2))]:
 assert s.simplify(s.diff(F,x)-f)==0;checks.append(f'{n} symbolic primitive derivative')
for q in map(mp.mpf,['.2','.4']):
 near(mp.diff(lambda z:mp.tan(4**(z*z)),q),2*q*mp.log(4)*4**(q*q)/mp.cos(4**(q*q))**2,f'29 independent derivative at {q}')
 near(mp.diff(lambda z:(1+10**mp.log(z))**6,q),6*(1+10**mp.log(q))**5*10**mp.log(q)*mp.log(10)/q,f'30 independent derivative at {q}')
 near(mp.diff(lambda z:z**mp.cos(z),q),q**mp.cos(q)*(-mp.sin(q)*mp.log(q)+mp.cos(q)/q),f'44 independent derivative at {q}')
near(mp.quad(lambda z:2**z-5**z,[-1,0])+mp.quad(lambda z:5**z-2**z,[0,1]),16/(5*mp.log(5))-1/(2*mp.log(2)),'51 split absolute area')
near(mp.pi*mp.quad(lambda z:10**(-2*z),[0,1]),99*mp.pi/(200*mp.log(10)),'52 disk volume')
r=mp.mpf('.6')
for _ in range(8):r-=(2**r-1-3**(-r))/(2**r*mp.log(2)+3**(-r)*mp.log(3))
near(2**r-1,3**(-r),'53 Newton residual')
near(10*mp.log10(mp.mpf('1e-7')/mp.mpf('1e-12')),50,'59 intensity inversion')
near(mp.diff(lambda z:10*mp.log10(z/mp.mpf('1e-12')),mp.mpf('1e-7')),mp.mpf('1e8')/mp.log(10),'59 loudness derivative')
a=mp.mpf('.38');avg=8*(a**20-1)/(20*mp.log(a))
near(mp.quad(lambda z:8*a**z,[0,20])/20,avg,'60 average intensity')
assert 8*a**20<avg<8
for t in [20,50,100]:near(mp.diff(lambda z:mp.mpf('1.43653e9')*mp.mpf('1.01395')**z,t),mp.mpf('1.43653e9')*mp.mpf('1.01395')**t*mp.log(mp.mpf('1.01395')),f'62 population derivative t={t}')
for e in E.values():
 assert e['id']==f'stewart9-exercise-6.4-alt-{e["number"]}'
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:
    assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
    assert not re.search(r'\\(?:quad|qquad)[A-Za-z]',v),(e['number'],key,v)
report={'section':'6.4*','count':71,'sourcePDFPages':[513,514,515],'sourceVisualReview':'All three alternative exercise pages visually inspected during authoring.','reuseMethod':'Individually matched standard 6.2–6.4 problems, preserved prior verification; changed prompts independently authored.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'status':'passed'}
(ROOT/'exercise-checks/calc1-s6-4-alt-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report)
