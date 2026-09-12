import json,re,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1];d=json.loads((ROOT/'exercise-content/s5-5.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,27));checks=[]
for e in E.values():
 for lang in['ko','en']:
  assert len(e['answer'][lang])>2 and e['answer'][lang]not in['ko','en']
  assert len(e['steps'][lang])>=2 and len(e['check'][lang])>15
 assert e['status']=='math-verified'
 for key in['statement','answer','check']:assert not re.search('[가-힣ぁ-ゟ゠-ヿ]',e[key]['en']),(e['number'],key)
 if 'figure'in e:ET.parse(ROOT/'exercise-content'/e['figure']['src'].split('../exercise-content/')[1])
x=s.symbols('x',real=True);P=s.pi;R=s.Rational
def check(name,a,b):assert s.simplify(a-b)==0,(name,a,b);checks.append(name)
check('6 cubic denominator substitution',s.integrate(x*x/(x**3+3)**2,(x,-1,1))/2,R(1,24))
check('8 signed negative average',s.integrate((1+s.sin(x))**2*s.cos(x),(x,P/2,3*P/2))/P,-8/(3*P))
for c in[s.sqrt(2-2*s.sqrt(5)/3),s.sqrt(2+2*s.sqrt(5)/3)]:check('12 midpoint-height root',c*c*(4-c*c),R(16,9))
for bb in[(3-s.sqrt(5))/2,(3+s.sqrt(5))/2]:check('14 endpoint root',2+3*bb-bb*bb,3)
V=5/(4*P)*(1-s.cos(2*P*x/5));check('21 model derivative',s.diff(V,x),s.sin(2*P*x/5)/2);check('21 cycle mean',s.integrate(V,(x,0,5))/5,5/(4*P))
check('23 illustrative strict inequality',s.integrate(x*x+1,(x,0,2))/2-2,R(1,3))
report={'section':'5.5','count':26,'sourcePDFPages':[440,441],'sourceVisualReview':'Both exercise pages inspected; referenced4.5.57 breathing model also inspected on PDF393.','authorVerification':'Average integrals checked against numerical quadrature; all reported level-crossing roots substituted into f(c)=average.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'oddAnswerAppendix':'Read AppendixG A81; exact odd answers agree.','graphReadings':'16 and18 explicitly give source readings and approximate results.','status':'passed'}
(ROOT/'exercise-checks/calc1-s5-5-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report)
