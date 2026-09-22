import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s6-2-alt.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,92))
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
for a,b in[(2,3),(-2,-3)]:near(mp.log(mp.sqrt(a*b)),(mp.log(abs(a))+mp.log(abs(b)))/2,f'1 expansion signs {a},{b}')
for x in map(mp.mpf,['-4','-1','4','6']):near(mp.log(mp.sqrt(3*x/(x-3))),(mp.log(3)+mp.log(abs(x))-mp.log(abs(x-3)))/2,f'2 expansion both branches {x}')
for x in map(mp.mpf,['.2','1','3']):near(mp.log((x+2)**3)/3+(mp.log(x)-mp.log((x*x+3*x+2)**2))/2,mp.log(mp.sqrt(x)/(x+1)),f'5 combined logarithm {x}')
for x in map(mp.mpf,['3','5']):near(mp.diff(lambda q:mp.log(mp.log(mp.log(q))),x),1/(x*mp.log(x)*mp.log(mp.log(x))),f'44 triple logarithm {x}')
near(mp.diff(lambda q:mp.log(q)/q,mp.e,2),-mp.exp(-3),'46 second derivative at e')
f=lambda q:(q+1)**4*(q-5)**3/(q-3)**8
for x in map(mp.mpf,['-2','.2','4','6']):near(mp.diff(f,x),f(x)*(4/(x+1)+3/(x-5)-8/(x-3)),f'64 logarithmic derivative sign intervals {x}')
for x in[-1,5]:near(mp.diff(f,x),0,f'64 zero extension {x}')
f=lambda q:(q**3+1)**4*mp.sin(q)**2/(mp.sign(q)*mp.root(abs(q),3))
for x in map(mp.mpf,['-2','-.4','.4','2']):near(mp.diff(f,x),f(x)*(12*x*x/(x**3+1)+2/mp.tan(x)-1/(3*x)),f'66 real cube root derivative {x}')
near(mp.diff(f,-1),0,'66 zero extension at -1')
near(mp.quad(lambda q:1/(q*mp.log(q)),[mp.e,6]),mp.log(mp.log(6)),'72 quadrature')
mid=sum(mp.mpf('.05')/(1+(mp.mpf(i)+mp.mpf('.5'))*mp.mpf('.05'))for i in range(10));assert mp.mpf(1)/3<mid<mp.log(mp.mpf('1.5'))<mp.mpf(5)/12;checks.append('85 area bounds and midpoint underestimate')
near(mp.quad(lambda q:mp.sqrt(2)-q/2,[1,2]),mp.sqrt(2)-mp.mpf(3)/4,'86 tangent trapezoid');assert mp.sqrt(2)-mp.mpf(3)/4>mp.mpf('.66');checks.append('86 lower bound above .66')
for n in[2,5,20]:assert sum(mp.mpf(1)/k for k in range(2,n+1))<mp.log(n)<sum(mp.mpf(1)/k for k in range(1,n));checks.append(f'87 strict harmonic bounds n={n}')
for e in E.values():
 assert e['id']==f'stewart9-exercise-6.2-alt-{e["number"]}'
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
report={'section':'6.2*','count':91,'sourcePDFPages':[495,496],'sourceVisualReview':'Both exercise pages visually inspected; Example1 secant endpoints checked in PDF488–490.','reuseMethod':'Identical exercises were individually matched to the standard development, copied with new IDs/pages and local figure files; changes in triple logarithms, implicit differentiation, tangent data and products authored separately.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'oddAnswerAppendix':'A84–A85 checked.81 repeats the same unit error as standard6.4.91:45,974J instead of45.974J; solution preserves correct SI conversion.','browserVisualReview':'86 tangent, secant and reciprocal curve inspected in Chrome.','status':'passed'}
(ROOT/'exercise-checks/calc1-s6-2-alt-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report)
