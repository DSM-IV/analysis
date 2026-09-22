import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s7-7.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,51))
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
def near(a,b,name,tol=mp.mpf('1e-25')):
 assert abs(a-b)<tol,(name,a,b);checks.append(name)
x=s.symbols('x',real=True)
# Extrema of exp(cos x) derivatives reduce to polynomial roots in c=cos x.
c=s.symbols('c');p2=1-c*c-c;p4=c**4+6*c**3+5*c*c-5*c-3
for p,K,label in [(p2,3,'23 second'),(p4,11,'23 fourth')]:
 roots=s.polys.polytools.intervals(p+s.diff(p,c),eps=s.Rational(1,10**12))
 pts=[-1.,1.]+[float((ab[0]+ab[1])/2)for ab,m in roots if ab[0]>-1 and ab[1]<1]
 fn=s.lambdify(c,s.exp(c)*p,'math');assert max(abs(fn(z))for z in pts)<K;checks.append(label+' bound from isolated stationary roots')
for k,K in [(2,2.2),(4,18.1)]:
 der=s.diff(s.sqrt(4-x**3),x,k);critical=s.factor(s.together(s.diff(der,x))).as_numer_denom()[0];roots=s.polys.polytools.intervals(critical,eps=s.Rational(1,10**12));pts=[-1.,1.]+[float((ab[0]+ab[1])/2)for ab,m in roots if ab[0]>=-1 and ab[1]<=1];fn=s.lambdify(x,der,'math');assert max(abs(fn(z))for z in pts)<K;checks.append(f'24 derivative order{k} bound from all stationary roots')
# Independently form each sum from explicit weight vectors.
def calc(f,a,b,n,rule):
 a,b=mp.mpf(a),mp.mpf(b);h=(b-a)/n
 if rule=='M':return h*mp.fsum(f(a+(mp.mpf(j)+mp.mpf('.5'))*h)for j in range(n))
 w=[1]+[4 if j%2 else 2 for j in range(1,n)]+[1]if rule=='S'else[mp.mpf('.5')]+[1]*(n-1)+[mp.mpf('.5')]
 return h*mp.fsum(w[j]*f(a+j*h)for j in range(n+1))/(3 if rule=='S'else 1)
rows=json.loads((ROOT/'exercise-checks/calc1-s7-7-numeric-results.json').read_text())
fns={5:(lambda x:x*mp.sin(x),0,mp.pi),6:(lambda x:x/mp.sqrt(1+x*x),0,2),7:(lambda x:mp.sqrt(1+x**3),0,1),8:(lambda x:mp.sin(mp.sqrt(x)),1,4),9:(lambda x:mp.sqrt(mp.expm1(x)),0,1),10:(lambda x:mp.sign(1-x*x)*abs(1-x*x)**(mp.mpf(1)/3),0,2),11:(lambda x:mp.exp(x+mp.cos(x)),-1,2),12:(lambda x:mp.exp(1/x),1,3),13:(lambda x:mp.sqrt(x)*mp.cos(x),0,4),14:(lambda x:1/mp.log(x),2,3),15:(lambda x:x*x/(1+x**4),0,1),16:(lambda x:mp.sin(x)/x,1,3),17:(lambda x:mp.log(1+mp.exp(x)),0,4),18:(lambda x:mp.sqrt(x+x**3),0,1)}
for row in rows:
 n=row['number']
 if n in fns:
  f,a,b=fns[n]
  for rule,val in row['approximations'].items():near(calc(f,a,b,row['n'],rule),mp.mpf(val),f'{n} independent {rule} weights')
 else:
  K=mp.mpf(row['K4']);L=2*mp.pi if n==23 else 2;N=row['n'];assert N%2==0 and K*L**5/(180*N**4)<mp.mpf('.0001');assert K*L**5/(180*(N-2)**4)>=mp.mpf('.0001');checks.append(f'{n} minimal even n for chosen bound')
near(calc(lambda x:mp.mpf(1),0,1,6,'S'),1,'Simpson normalization')
near(calc(lambda x:x**3-6*x*x+4*x,0,8,4,'S'),128,'48 cubic exactness')
for f in [lambda x:mp.exp(x),lambda x:mp.sin(x*x)]:
 T=calc(f,0,2,6,'T');M=calc(f,0,2,6,'M');near((T+M)/2,calc(f,0,2,12,'T'),'49 refinement identity');near((T+2*M)/3,calc(f,0,2,12,'S'),'50 refinement identity')
near(calc(lambda x:2+mp.cos(2*mp.pi*x)-mp.cos(4*mp.pi*x),0,2,2,'T'),4,'45 trapezoids exact counterexample')
near(calc(lambda x:2+mp.cos(2*mp.pi*x)-mp.cos(4*mp.pi*x),0,2,2,'M'),0,'45 midpoint counterexample')
near(calc(lambda x:1+mp.cos(mp.pi*x),0,2,2,'S'),mp.mpf(4)/3,'46 Simpson counterexample')
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:
    assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
    assert not re.search(r'\\(?:quad|qquad)[A-Za-z]',v),(e['number'],key,v)
report={'section':'7.7','count':50,'sourcePDFPages':[614,615,616,617],'sourceVisualReview':'All four exercise pages visually inspected; graph-read values explicitly disclosed. Source36 graph unit seconds conflicts with stated hours; solution follows text.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'browserVisualReview':'Derivative bound diagram23 viewed in Chrome: curves and horizontal bounds clear.','status':'passed'}
(ROOT/'exercise-checks/calc1-s7-7-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('PASS',len(E),'exercises',len(checks),'independent checks')
