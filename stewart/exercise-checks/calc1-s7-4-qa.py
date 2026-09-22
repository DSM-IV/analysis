import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s7-4.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,79))
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
def near(a,b,name,tol=mp.mpf('1e-28')):
 assert abs(a-b)<tol,(name,a,b);checks.append(name)
x=s.symbols('x',real=True)
f73=(4*x**3-27*x*x+5*x-32)/(30*x**5-13*x**4+50*x**3-286*x*x-299*x-70)
f74=(12*x**5-7*x**3-13*x*x+8)/(100*x**6-80*x**5+116*x**4-80*x**3+41*x*x-20*x+4)
for n,f in [(73,f73),(74,f74)]:
 A=s.apart(f,x);F=s.integrate(A,x);assert s.cancel(A-f)==0;assert s.simplify(s.diff(F,x)-f)==0;checks.append(f'{n} exact CAS decomposition and primitive')
for z in map(mp.mpf,['-3','-.2','.2','2','3']):
 F=lambda x:mp.mpf(5)/4*mp.log(abs(abs(x)**(mp.mpf(4)/5)-1))
 root=mp.sign(z)*abs(z)**(mp.mpf(1)/5)
 near(mp.diff(F,z),1/(z-root),f'48 real fifth-root branch x={z}')
near(mp.quad(lambda x:1/(x*x-2*x-3),[0,2]),-mp.log(3)/2,'59 signed area')
near(mp.quad(lambda x:1/(1+mp.sin(x)-mp.cos(x)),[mp.pi/3,mp.pi/2]),mp.log((1+mp.sqrt(3))/2),'66 tangent-half-angle definite')
near(mp.quad(lambda x:mp.sin(2*x)/(2+mp.cos(x)),[0,mp.pi/2]),2-4*mp.log(mp.mpf(3)/2),'67 tangent-half-angle definite')
near(mp.quad(lambda x:1/(x**3+x),[1,2]),mp.log(mp.mpf(8)/5)/2,'68 rational area')
near(mp.quad(lambda x:(x*x+1)/(3*x-x*x),[1,2]),-1+11*mp.log(2)/3,'69 rational area')
near(mp.pi*mp.quad(lambda x:1/(x*x+3*x+2)**2,[0,1]),mp.pi*(mp.mpf(2)/3+2*mp.log(3)-4*mp.log(2)),'70a disk volume')
near(2*mp.pi*mp.quad(lambda x:x/(x*x+3*x+2),[0,1]),2*mp.pi*(2*mp.log(3)-3*mp.log(2)),'70b shell volume')
T=lambda P:mp.log(10000/P)+11*mp.log((P-9000)/1000)
near(T(mp.mpf(10000)),0,'71 initial condition')
near(mp.diff(T,mp.mpf(11000)),(mp.mpf(11000)+900)/(11000*(mp.mpf('.1')*11000-900)),'71 time-population derivative')
F72=lambda x:mp.log((x*x+mp.sqrt(2)*x+1)/(x*x-mp.sqrt(2)*x+1))/(4*mp.sqrt(2))+(mp.atan(mp.sqrt(2)*x+1)+mp.atan(mp.sqrt(2)*x-1))/(2*mp.sqrt(2))
for z in map(mp.mpf,['-3','-.7','0','.7','3']):near(mp.diff(F72,z),1/(z**4+1),f'72 continuous arctan sum {z}')
N,D=s.fraction(f74);assert s.factor(D)==(5*x-2)**2*(2*x*x+1)**2
realroots=[float(s.re(z))for z in s.nroots(N)if abs(float(s.im(z)))<1e-9];assert max(abs(a-b)for a,b in zip(realroots,[-.778246212566209,.802942437812254,1]))<1e-10;checks.append('74 primitive extrema from numerator roots')
fdnum=s.fraction(s.cancel(s.diff(f74,x)))[0];roots=[float(s.re(z))for z in s.nroots(fdnum,maxsteps=200)if abs(float(s.im(z)))<1e-9];assert max(abs(a-b)for a,b in zip(roots,[-1.63603110032221,.877151258215353,1.83595399590579]))<1e-10;checks.append('74 primitive inflections from f derivative')
for n in range(2,7):
 aa=mp.mpf('1.3');z=mp.mpf('.6')
 deriv=mp.diff(lambda x:x/(2*aa*aa*(n-1)*(x*x+aa*aa)**(n-1)),z)+(mp.mpf(2*n-3)/(2*aa*aa*(n-1)))/(z*z+aa*aa)**(n-1)
 near(deriv,1/(z*z+aa*aa)**n,f'76 recurrence n={n}')
for n in range(1,7):
 aa=s.Rational(3,2);A=1/(aa**n*(x-aa))-sum(1/(aa**(n-k+1)*x**k)for k in range(1,n+1));assert s.cancel(A-1/(x**n*(x-aa)))==0;checks.append(f'77 exact finite sum n={n}')
A,B=s.symbols('A B');f=(A*x*x+B*x+1)/(x*x*(x+1)**3);assert s.residue(f,x,0)==B-3;assert s.residue(f,x,-1)==3-B;checks.append('78 simple-pole residues vanish iff B=3')
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:
    assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
    assert not re.search(r'\\(?:quad|qquad)[A-Za-z]',v),(e['number'],key,v)
    assert 'G_{'not in v and 'otherwise'not in v,(e['number'],'unsimplified CAS')
report={'section':'7.4','count':78,'sourcePDFPages':[590,591,592],'sourceVisualReview':'All three exercise pages visually checked, including radical extent41–50, population model71, CAS expressions73–74 and rational-primitive condition78.','authorChecks':'Rational fractions recombined exactly and integrated termwise; primitive derivatives symbolic; rationalizing substitutions numerically checked.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'browserVisualReview':'74 pole-separated f/F plots and two shallow-extrema zooms checked in Chrome.','status':'passed'}
(ROOT/'exercise-checks/calc1-s7-4-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('PASS',len(E),'exercises',len(checks),'independent checks')
