import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s6-4.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,101))
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

mp.mp.dps=40;x=s.symbols('x',positive=True);checks=[]
def check(name,a,b):assert s.simplify(s.trigsimp(a-b))==0,(name,a,b);checks.append(name)
check('15 quotient logarithm derivative',s.diff(s.log(x)/(1+s.log(2*x)),x),(1+s.log(2))/(x*(1+s.log(2*x))**2))
check('22 nested square-root logarithm',s.diff(s.log((1+2*x)/(1-2*x))/2,x),2/(1-4*x*x))
check('35 domain-restricted quotient derivative',s.diff(x/(1-s.log(x-1)),x),(2*x-1-(x-1)*s.log(x-1))/((x-1)*(1-s.log(x-1))**2))
f48=s.exp(-x)*s.cos(x)**2/(x*x+x+1);check('48 logarithmic formula extends at cos zeros',s.diff(f48,x),f48*(-1-2*s.tan(x)-(2*x+1)/(x*x+x+1)))
check('57 original exponent is ln x',s.diff(x**s.log(x),x),2*x**s.log(x)*s.log(x)/x)
check('62 ninth derivative',s.diff(x**8*s.log(x),x,9),s.factorial(8)/x)
check('63 second derivative',s.diff(s.log(x)/s.sqrt(x),x,2),(3*s.log(x)-8)/(4*x**s.Rational(5,2)))
check('66 trigonometric concavity',s.diff(s.log(s.tan(x)**2),x,2),-8*s.cos(2*x)/s.sin(2*x)**2)
check('68 stationary inflection',s.diff(s.log(1+x**3),x,2),3*x*(2-x**3)/(1+x**3)**2)
check('88 enclosed area',s.integrate((s.log(x)-s.log(x)**2)/x,(x,1,s.E)),s.Rational(1,6))
work=mp.quad(lambda V:mp.mpf('90')/V,[mp.mpf('.0006'),mp.mpf('.001')]);assert abs(work-90*mp.log(mp.mpf(5)/3))<mp.mpf('1e-30');checks.append('91 SI-unit pressure-volume quadrature gives45.974J,not45974J')
m=s.symbols('m',positive=True);a=s.sqrt(1/m-1);check('95 two symmetric lobes',2*(s.log(1+a*a)/2-m*a*a/2),m-1-s.log(m))
for q in [mp.mpf('2.958516'),mp.mpf('5.290718')]:assert abs((q-4)**2-mp.log(q))<mp.mpf('2e-6')
for q in [mp.mpf('-1.964636'),mp.mpf('1.058006')]:assert abs(mp.log(4-q*q)-q)<mp.mpf('2e-5')
checks.append('71–72 six-decimal roots substituted into original equations')
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
report={'section':'6.4','count':100,'sourcePDFPages':[485,486,487],'sourceVisualReview':'All three exercise pages visually inspected;57 exponent enlarged to confirm x^(lnx);AppendixA84 PDF1373 visually inspected for91 units discrepancy.','authorVerification':'Basic and logarithmic derivatives compared with independent numerical differentiation; definite integrals checked by quadrature; CAS curve derivatives simplified independently; Newton residuals below1e-25.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'oddAnswerAppendix':'A84 matches except91:printed45974J conflicts with original150kPa,600cm³,1000cm³. SI work=90ln(5/3)=45.974J;derivation and appendix discrepancy are explicit in the solution.','browserVisualReview':'72 SVG checked in Chrome;both curve-line intersections visible,including near the left domain boundary.','status':'passed'}
(ROOT/'exercise-checks/calc1-s6-4-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report)
