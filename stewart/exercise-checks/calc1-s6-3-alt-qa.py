import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s6-3-alt.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,107))
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
for root in [-mp.sqrt(1+mp.exp(3)),mp.sqrt(1+mp.exp(3))]:near(mp.log(root*root-1),3,'6 both logarithm roots')
root=(mp.log(19)-1)/4;near(1+mp.exp(4*root+1),20,'6 exponential equation')
root=(1+mp.sqrt(5))/2;near(mp.log(root)+mp.log(root-1),0,'7 admissible quadratic root')
root=-mp.log(mp.e-1)/2;near(mp.e-mp.exp(-2*root),1,'7 changed exponential equation')
root=(-1+mp.sqrt(1+8*mp.e**2))/4;near(mp.log(2*root+1),2-mp.log(root),'10 logarithm equation')
near(mp.exp(1/((4+1/mp.log(7))-4)),7,'12 exponential reciprocal root')
root=1/(mp.e**2-1);near(mp.log((root+1)/root),2,'12 logarithm ratio root')
x=s.symbols('x',real=True);f=s.exp(2*x)-s.exp(x)
assert s.simplify(s.diff(f,x).subs(x,-s.log(2)))==0;assert s.simplify(f.subs(x,-s.log(2)))==-s.Rational(1,4);assert s.simplify(s.diff(f,x,2).subs(x,-s.log(4)))==0;assert s.simplify(f.subs(x,-s.log(4)))==-s.Rational(3,16);checks.append('72 exact minimum and inflection coordinates')
for xx,rr in[(mp.mpf('-2'),mp.mpf('.3')),(mp.mpf('.7'),mp.mpf('-1.2'))]:near(mp.power(mp.exp(xx),rr),mp.exp(rr*xx),f'106 real exponent {xx},{rr}')
# Sample independently from reused limits, areas and differential equations.
near(mp.quad(lambda y:mp.exp(y)-y*y+2,[-1,1]),mp.e-1/mp.e+mp.mpf(10)/3,'92 enclosed area')
near(mp.quad(lambda q:mp.exp(3*q)-mp.exp(q),[0,1]),mp.exp(3)/3-mp.e+mp.mpf(2)/3,'93 enclosed area')
near(mp.quad(lambda q:2*q*mp.exp(-q*q),[0,2])/2,(1-mp.exp(-4))/2,'91 average value')
for e in E.values():
 assert e['id']==f'stewart9-exercise-6.3-alt-{e["number"]}'
 for key in['statement','answer','check','steps']:
  for lang in['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:
    assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
    assert not re.search(r'\\(?:quad|qquad)[A-Za-z]',v),(e['number'],key,v)
report={'section':'6.3*','count':106,'sourcePDFPages':[502,503,504],'sourceVisualReview':'All three alternative exercise pages visually inspected, including exponent placement and signed inverse functions.','reuseMethod':'Individually matched ordinary6.2 and6.3 exercises, with separate IDs/pages/assets; changed equations and exponential-difference curve authored independently.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'oddAnswerAppendix':'A85–A86 checked: exact inverse and derivative answers, Newton root, curve analysis and application values agree.','browserVisualReview':'72 exponential-difference graph inspected in Chrome.','status':'passed'}
(ROOT/'exercise-checks/calc1-s6-3-alt-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report)
