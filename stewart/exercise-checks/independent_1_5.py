import json
from pathlib import Path
import sympy as s
x=s.symbols('x',real=True);checks=[]
def ck(n,expr,at,want,side='+'):
 got=s.limit(expr,x,at,dir=side)
 assert got==want or s.simplify(got-want)==0,(n,got,want)
 checks.append(dict(number=n,method='independent exact limit',direction=side,result=str(got)))
for n,e,a,w in [(19,(x*x-3*x)/(x*x-9),3,s.Rational(1,2)),(21,s.sin(x)/(x+s.tan(x)),0,s.Rational(1,2)),(22,((2+x)**5-32)/x,0,80),(23,s.sin(3*x)/s.tan(2*x),0,s.Rational(3,2)),(24,(1+x**9)/(1+x**15),-1,s.Rational(3,5)),(26,(5**x-1)/x,0,s.log(5)),(40,(s.cos(2*x)-s.cos(x))/x**2,0,-s.Rational(3,2)),(41,x*x-2**x/1000,0,-s.Rational(1,1000)),(42,(s.tan(x)-x)/x**3,0,s.Rational(1,3))]:
 for side in ['-','+']:ck(n,e,a,w,side)
ck(25,x**x,0,1)
for side,sign in [('-',-1),('+',1)]:
 ck(13,x*s.sqrt(1+x**-2),0,sign,side)
 ck(14,(3**(1/x)-2)/(3**(1/x)+1),0,-2 if sign<0 else 1,side)
 ck(20,(x*x-3*x)/(x*x-9),-3,-sign*s.oo,side)
 ck(37,(x-1)/(2*x+4),-2,-sign*s.oo,side)
 ck(38,(x*x+1)/(3*x-2*x*x),0,sign*s.oo,side)
 ck(38,(x*x+1)/(3*x-2*x*x),s.Rational(3,2),-sign*s.oo,side)
 ck(39,1/(x**3-1),1,sign*s.oo,side)
a=s.asin(s.pi/4)
for q in [-s.pi+a,-a,a,s.pi-a]:
 assert s.simplify(abs(2*s.sin(q))-s.pi/2)==0
 assert s.simplify(s.cos(q)**2)==1-s.pi**2/16
 checks.append(dict(number=43,method='pole equation and nonzero crossing slope',root=str(q)))
k=s.symbols('k',integer=True,positive=True)
assert s.simplify(s.tan(k*s.pi))==0
assert s.simplify(s.tan(k*s.pi+s.pi/4))==1
checks.append(dict(number=44,method='two exact sequences with different values',values=[0,1]))
p=Path(__file__).with_name('s1-5-independent.json');p.write_text(json.dumps({'section':'1.5','passed':len(checks),'checks':checks},indent=2)+'\n');print(len(checks),'checks passed')
