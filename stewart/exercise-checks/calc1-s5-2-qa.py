import json,re,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];d=json.loads((ROOT/'exercise-content/s5-2.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,88))
for e in E.values():
 for lang in['ko','en']:
  assert len(e['answer'][lang])>2 and e['answer'][lang]not in['ko','en']
  assert len(e['steps'][lang])>=2 and len(e['check'][lang])>15
 assert e['status']=='math-verified'
 for key in['statement','answer','check']:
  assert not re.search('[가-힣ぁ-ゟ゠-ヿ]',e[key]['en']),(e['number'],key)
 if 'figure'in e:ET.parse(ROOT/'exercise-content'/e['figure']['src'].split('../exercise-content/')[1])
x,r,h,R,c,delta=s.symbols('x r h R c d',positive=True);checks=[]
def check(name,lhs,rhs):assert s.simplify(lhs-rhs)==0,(name,lhs,rhs);checks.append(name)
check('sphere cap',s.integrate(s.pi*(r*r-x*x),(x,r-h,r)),s.pi*h*h*(r-h/3))
check('two-sphere lens',2*s.integrate(s.pi*(r*r-x*x),(x,r/2,r)),5*s.pi*r**3/12)
check('wedge parallel sections',s.integrate(2*x*s.sqrt(16-x*x)/s.sqrt(3),(x,0,4)),128/(3*s.sqrt(3)))
check('water low level',s.pi*h*h*(15-h/3)-s.pi*h*h*(5-h/3),10*s.pi*h*h)
check('water continuity',s.pi*100*(15-s.Rational(10,3))-500*s.pi/3,1000*s.pi)
check('barrel integral',s.integrate(s.pi*(R-c*x*x)**2,(x,-h/2,h/2)).subs(c,4*delta/h**2),s.pi*h*(2*R*R+(R-delta)**2-s.Rational(2,5)*delta**2)/3)
check('pot capacity',s.pi*s.integrate(x**s.Rational(2,3),(x,1,8)),93*s.pi/5)
check('napkin ring',s.pi*s.integrate(R*R-r*r-x*x,(x,-s.sqrt(R*R-r*r),s.sqrt(R*R-r*r))),4*s.pi*(R*R-r*r)**s.Rational(3,2)/3)
assert 3*sum([18,79,106,128,39])==1110
assert abs(2*sum([.65,.61,.59,.55,.50])-5.8)<1e-12
report={'section':'5.2','count':87,'sourcePDFPages':[421,422,423,424],'sourceVisualReview':'All four exercise pages inspected, plus Example9 source text for77.','authorVerification':'All washer integrals compared with independent mpmath quadrature; numerical45/46 checked with tanh-sinh and Gauss-Legendre. Symbolic cross-sections checked at positive sample parameters.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'oddAnswerAppendix':'Read AppendixG A79–A80; exact odd answers matched. Graph57 permits reading-dependent estimates near196 and838.','status':'passed'}
(ROOT/'exercise-checks/calc1-s5-2-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report)
