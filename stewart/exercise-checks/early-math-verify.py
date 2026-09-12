"""Independent algebra, numerical quadrature, schema, and asset checks."""
from pathlib import Path
import json,sys,re,math
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));import build_exercises as builder
x,y,z,t,r,c,a,b=s.symbols('x y z t r c a b',real=True);checks=[]
def test(label,value):
 assert bool(value),label
 checks.append({'check':label,'passed':True})
def eq(label,actual,expected):test(label,s.simplify(actual-expected)==0)
eq('12.6.38 completing squares',(x-2)**2-y*y-(z+1)**2,x*x-y*y-z*z-4*x-2*z+3)
eq('12.6.39 completing squares',(x-2)**2-y*y+(z-1)**2-5,x*x-y*y+z*z-4*x-2*z)
eq('12.6.40 completing squares',4*(x-3)**2+(y-4)**2+(z+2)**2-1,4*x*x+y*y+z*z-24*x-8*y+4*z+55)
eq('12.6.55 projected ellipse',x*x+y*y+y*y,x*x+2*y*y)
eq('14.1.1 diagonal restriction',x**3/(2*x-x*x),x*x/(2-x))
eq('14.1.52 circle algebra',x*x+(y-1/(2*c))**2-1/(4*c*c),x*x+y*y-y/c)
eq('14.1.73 completed square',-4*(y+5*x/4)**2-x**4+s.Rational(25,4)*x*x+3*x,3*x-x**4-4*y*y-10*x*y)
eq('14.1.74 maximum value',(x*y*s.exp(-x*x-y*y)).subs({x:1/s.sqrt(2),y:1/s.sqrt(2)}),1/(2*s.E))
eq('14.1.79 rotated diagonalization',(1+c/2)*(x+y)**2/2+(1-c/2)*(x-y)**2/2,x*x+y*y+c*x*y)
eq('14.2.23 path y²',((x*y*y)/(x*x+y**4)).subs(x,y*y),s.Rational(1,2))
eq('14.2.36 curved path',((x*y**3)/(x*x+y**6)).subs(x,y**3),s.Rational(1,2))
eq('14.2.53 radial limit',s.limit((s.exp(-r*r)-1)/(r*r),r,0),-1)
eq('14.2.55 sinc limit',s.limit(s.sin(r*r)/(r*r),r,0),1)
f=(x**3*y-x*y**3)/(x*x+y*y);mix=s.diff(f,x,y);expected=(x**6+9*x**4*y*y-9*x*x*y**4-y**6)/(x*x+y*y)**3
eq('14.3.101 mixed surface formula',mix,expected)
eq('14.3.101 fx on y-axis',s.diff(f,x).subs(x,0),-y)
eq('14.3.101 fy on x-axis',s.diff(f,y).subs(y,0),x)
eq('14.3.58 mixed third derivative',s.diff(s.sin(2*x+5*y),y,x,y),-50*s.cos(2*x+5*y))
eq('14.3.61 mixed root derivative',s.diff(s.sqrt(x+y*y),x,x,y),3*y/(4*(x+y*y)**s.Rational(5,2)))
eq('14.3.63 mixed rational derivative',s.diff(x/(y+2*z),x,y,z),4/(y+2*z)**3)
eq('14.3.67 efficient mixed derivative',s.diff(x*y*y*z**3+s.asin(x*s.sqrt(z)),x,z,y),6*y*z*z)
eq('14.3.68 vanished mixed derivative',s.diff(s.sqrt(1+x*z)+s.sqrt(1-x*y),y,x,z),0)
eq('14.3.78 harmonic logarithm',s.diff(s.log(s.sqrt(x*x+y*y)),x,2)+s.diff(s.log(s.sqrt(x*x+y*y)),y,2),0)
eq('14.3.79 inverse radius harmonic',sum(s.diff(1/s.sqrt(x*x+y*y+z*z),q,2)for q in[x,y,z]),0)
D=s.symbols('D',positive=True);T=s.symbols('T',positive=True);g=s.exp(-x*x/(4*D*T))/s.sqrt(4*s.pi*D*T)
eq('14.3.81 Gaussian diffusion',s.diff(g,T),D*s.diff(g,x,2))
eq('14.3.91 kinetic identity',s.diff(s.Rational(1,2)*x*y*y,x)*s.diff(s.Rational(1,2)*x*y*y,y,2),s.Rational(1,2)*x*y*y)
eq('14.3.99 axis derivative',s.diff(x**(-2),x).subs(x,1),-2)
test('14.3.39 source logarithm is not real at supplied point',1-s.sqrt(1+4+4)<0)
V=s.Matrix
A=V([1,0,1]);B=V([2,3,0]);C=V([-1,1,4]);Q=V([0,3,2]);eq('12.Review.10 volume',abs((B-A).dot((C-A).cross(Q-A))),6)
eq('12.Review.11 triangle area',V([1,0,-1]).cross(V([0,4,3])).norm()/2,s.sqrt(41)/2)
eq('12.Review.22 distance',((1+t)**2+(2-t)**2+(-1+2*t)**2).subs(t,s.Rational(1,2)),s.Rational(9,2))
eq('12.Review.25 plane pencil',(x-z-1)+(y+2*z-3),x+y+z-4)
eq('12.Review.38 squared distance equation',(y-1)**2-4*(x*x+(y+1)**2+z*z),-(4*x*x+3*(y+s.Rational(5,3))**2+4*z*z-s.Rational(16,3)))
rad=s.sqrt(3)-s.Rational(3,2);eq('12.Plus.1 sphere contact',s.sqrt(3)*(s.Rational(1,2)-rad),2*rad)
pc=V([(c*c-1)/(1+c*c),2*c/(1+c*c),0]);dc=V([2*c,1-c*c,-1-c*c]);X=pc+t*dc
eq('12.Plus.3 first plane',c*X[0]+X[1]+X[2],c)
eq('12.Plus.3 second plane',X[0]-c*X[1]+c*X[2],-1)
eq('12.Plus.3 hyperboloid',X[0]**2+X[1]**2-X[2]**2,1)
eq('12.Plus.3 volume',s.integrate(s.pi*(1+t*t),(t,0,1)),4*s.pi/3)
eq('12.Plus.5 series',2+3/(1-s.Rational(5,6)),20)
eq('12.Plus.6 point on sphere',V([-1,1,4]).__sub__(V([5,4,1])).norm()**2,54)
eq('12.Plus.6 internal tangency',V([5,4,1]).__sub__(V([1,2,3])).norm()+3*s.sqrt(6),5*s.sqrt(6))
eq('12.Plus.7 threshold identity',(s.sin(x)-s.tan(y)*s.cos(x))/(s.cos(x)+s.tan(y)*s.sin(x)),s.tan(x-y))
num=mp.quad(lambda yy:4*mp.sqrt(.25-yy*yy)*(1-2*yy),[0,.5]);test('12.Plus.8 independent numerical volume',abs(num-(mp.pi/4-mp.mpf(1)/3))<mp.mpf('1e-14'))
counts={'12-6':55,'12-7':38,'12-8':8,'14-1':81,'14-2':59,'14-3':101};assets=0
for key,count in counts.items():
 path=ROOT/'exercise-content'/f's{key}.json';doc=json.loads(path.read_text());builder.validate_document(doc,path)
 test(key+' complete numbering',[e['number']for e in doc['exercises']]==list(range(1,count+1)))
 for ex in doc['exercises']:
  for field in['statement','answer','hint','check','topic']:test(key+'.'+str(ex['number'])+' '+field+' English language separation',not re.search('[가-힣]',ex[field]['en']))
  if 'figure'in ex:
   import xml.etree.ElementTree as ET
   p=ROOT/'exercise-content'/'assets'/Path(ex['figure']['src']).name;ET.parse(p);assets+=1
result={'summary':{'passed':len(checks),'exercises':sum(counts.values()),'svg_assets':assets},'checks':checks}
(ROOT/'exercise-checks'/'early-math-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result['summary']))
