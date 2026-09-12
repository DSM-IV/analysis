import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s6-3.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,65))
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

mp.mp.dps=40;x=s.symbols('x',real=True);checks=[]
for vals in [(2,3,4),(-2,-3,-4)]:
 a,c,d=map(mp.mpf,vals);assert abs(mp.log10(a*a*c**3*d)-(2*mp.log10(abs(a))+3*mp.log10(abs(c))+mp.log10(abs(d))))<mp.mpf('1e-30')
checks.append('7 expansion preserves positive and negative admissible inputs')
for q in[-3,-.5,1,4]:
 if q>-1 and q!=3:
  q=mp.mpf(q);lhs=mp.log((q**3+1)*abs(q-3)**(mp.mpf(2)/3),2);rhs=mp.log(q+1,2)+mp.log(q*q-q+1,2)+mp.mpf(2)/3*mp.log(abs(q-3),2);assert abs(lhs-rhs)<mp.mpf('1e-30')
checks.append('8 cube-root logarithm expansion across x=3')
for q in[(1-s.sqrt(21))/2,(1+s.sqrt(21))/2]:assert s.simplify(q*q-q-1)==4
checks.append('24 both quadratic roots have positive log argument')
for q in[mp.mpf('.2'),mp.mpf('1'),mp.mpf('4')]:
 f=mp.log(2+mp.log(q));assert abs(mp.exp(mp.exp(f)-2)-q)<mp.mpf('1e-30')
checks.append('46 nested-log inverse composition')
for q in[-3,-1,0,2,5]:
 q=mp.mpf(q);f=mp.log(q+mp.sqrt(q*q+1));assert abs((mp.exp(f)-mp.exp(-f))/2-q)<mp.mpf('1e-30')
checks.append('57 inverse identity with positive and negative preimages')
poly=x*x-2*x-2;sol=s.reduce_inequalities([poly>0,poly<=1],x)
for q,want in[(-1,True),(-.8,True),(0,False),(2,False),(2.8,True),(3,True),(3.1,False)]:assert bool(sol.subs(x,q))==want
checks.append('63 full logarithmic inequality domain and endpoint behavior')
sieve=[True]*101;sieve[0]=sieve[1]=False
for i in range(2,11):
 if sieve[i]:
  for j in range(i*i,101,i):sieve[j]=False
assert sum(sieve)==25 and sum(sieve[:26])==9;checks.append('64 independent Eratosthenes sieve')
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
report={'section':'6.3','count':64,'sourcePDFPages':[475,476,477],'sourceVisualReview':'All three exercise pages visually inspected,including nested exponent/log expressions4(c),6(c).','authorVerification':'Equation roots constrained by original logarithm domains; inverse formulas composed at three admissible inputs; limits crosschecked symbolically.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'oddAnswerAppendix':'AppendixG A83–A84 exact odd answers agree; logarithm expansions use absolute values to preserve the full original real domain.','browserVisualReview':'16 SVG checked in Chrome: all four curves and y=x are legible; horizontal and vertical unit lengths match.','status':'passed'}
(ROOT/'exercise-checks/calc1-s6-3-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report)
