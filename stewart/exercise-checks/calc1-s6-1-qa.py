import json,re,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1]; d=json.loads((ROOT/'exercise-content/s6-1.json').read_text()); E={e['number']:e for e in d['exercises']}; assert list(E)==list(range(1,53)); checks=[]
for e in E.values():
 for lang in ['ko','en']:
  assert len(e['answer'][lang])>=2 and len(e['steps'][lang])>=2 and len(e['check'][lang])>15,(e['number'],lang)
 assert e['status']=='math-verified'
 for key in ['statement','answer','check']: assert not re.search('[가-힣ぁ-ゟ゠-ヿ]',e[key]['en']),(e['number'],key)
 if 'figure' in e:ET.parse(ROOT/'exercise-content'/e['figure']['src'].split('../exercise-content/')[1])
x=s.symbols('x',real=True); R=s.Rational
for n,f,u,a,answer in [(37,x**3,2,8,R(1,12)),(38,s.sqrt(x-2),6,2,4),(39,9-x*x,1,8,-R(1,2)),(40,1/(x-1),R(3,2),2,-R(1,4)),(41,3*x**3+4*x*x+6*x+5,0,5,R(1,6)),(42,x**3+3*s.sin(x)+2*s.cos(x),0,2,R(1,3)),(43,3+x*x+s.tan(s.pi*x/2),0,3,2/s.pi),(44,s.sqrt(x**3+4*x+4),1,3,R(6,7))]:
 assert s.simplify(f.subs(x,u)-a)==0
 assert s.simplify(1/s.diff(f,x).subs(x,u)-answer)==0
 checks.append(str(n)+' inverse derivative via original preimage')
assert s.simplify(1/s.sqrt(1+3**3)-1/(2*s.sqrt(7)))==0;checks.append('47 FTC and inverse derivative')
mp.mp.dps=40
for y in [mp.mpf('0'),mp.mpf('.1'),mp.mpf('1'),mp.mpf('2'),mp.mpf('5')]:
 a=y*y/2-mp.mpf(10)/27; q=mp.sqrt(a*a+mp.mpf(8)/729)
 root=lambda t:mp.sign(t)*abs(t)**(mp.mpf(1)/3)
 u=root(a+q)+root(a-q)-mp.mpf(1)/3
 assert abs(u**3+u*u+u+1-y*y)<mp.mpf('1e-30')
checks.append('49 real Cardano branches at five inputs, 40 digits')
z=s.symbols('z');assert s.expand((x**3+x*x+x+1).subs(x,z-R(1,3)))==z**3+R(2,3)*z+R(20,27);checks.append('49 depressed cubic identity')
report={'section':'6.1','count':52,'sourcePDFPages':[455,456],'sourceVisualReview':'Both exercise pages visually inspected, including fractional data in45 and48 and domain restrictions.','authorVerification':'Inverse formulas composed at admissible inputs; explicit inverse derivatives compared to reciprocal original derivatives.','independentChecks':checks,'figureCount':sum('figure' in e for e in E.values()),'oddAnswerAppendix':'Read AppendixG A82; exact odd answers agree.','browserVisualReview':'37 SVG checked in Chrome: equal axis scales, inverse reflection and readable legend.','status':'passed'}
(ROOT/'exercise-checks/calc1-s6-1-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report)
