import sympy as s,json
from pathlib import Path
x,h=s.symbols('x h',real=True);checks=[]
def eq(n,v,w,method):
 r=s.simplify(v-w);assert r==0,(n,r);checks.append({'number':n,'method':method,'residual':'0'})
items=[(3,x*x+3*x,-1,1),(4,x**3+1,1,3),(5,2*x*x-5*x+1,3,7),(6,x*x-2*x**3,1,-4),(7,(x+2)/(x-3),2,-5),(8,s.sqrt(1-3*x),-1,-s.Rational(3,4)),(9,3+4*x*x-2*x**3,1,2),(9,3+4*x*x-2*x**3,2,-8),(10,2*s.sqrt(x),1,1),(10,2*s.sqrt(x),9,s.Rational(1,3)),(19,s.sqrt(4*x+1),6,s.Rational(2,5)),(20,5*x**4,-1,-20),(21,x*x/(x+6),3,s.Rational(5,9)),(22,1/s.sqrt(2*x+2),1,-s.Rational(1,8)),(29,3*x*x-x**3,1,3),(30,x**4-2,1,4),(31,5*x/(1+x*x),2,-s.Rational(3,5)),(32,4*x*x-x**3,2,4),(32,4*x*x-x**3,3,-3),(35,80*x-6*x*x,4,32),(36,10+45/(x+1),4,-s.Rational(9,5))]
for n,f,a,v in items:
 eq(n,s.diff(f,x).subs(x,a),v,'independently entered analytic derivative')
 eq(n,s.limit((f.subs(x,a+h)-f.subs(x,a))/h,h,0),v,'independent difference quotient limit')
eq(11,16*s.Rational(5,2)**2,100,'impact equation');eq(11,32*s.Rational(5,2),80,'impact velocity')
t=s.Rational(500,93);eq(12,10*t-s.Rational(186,100)*t*t,0,'positive return time');eq(12,10-s.Rational(372,100)*t,-10,'return velocity')
for a,v in [(1,-2),(2,-s.Rational(1,4)),(3,-s.Rational(2,27))]:eq(13,-2/s.Integer(a)**3,v,'specific velocity')
for aa,bb,v in [(4,8,0),(6,8,1),(8,10,3),(8,12,4)]:
 f=x*x/2-6*x+23;eq(14,(f.subs(x,bb)-f.subs(x,aa))/(bb-aa),v,'secant velocity')
f=x**3/3-2*x*x+3*x
for a,v in [(0,3),(1,0),(2,-1)]:eq(39,s.diff(f,x).subs(x,a),v,'constructed derivative constraint')
f=2/s.pi*s.sin(s.pi*x/2)
for a,v in [(0,1),(1,0),(2,-1),(3,0),(4,1)]:eq(40,s.diff(f,x).subs(x,a),v,'sine-arc derivative constraint')
for n,l,r,a in [(40,x/(x+1),f,0),(40,f,(x-4)/(5-x),4),(41,1/(x+5)+(x+2)/9-s.Rational(1,3),(x+2)**2/4,-2),(41,(x+2)**2/4,1+x-3*x*x/25,0)]:
 eq(n,l.subs(x,a),r.subs(x,a),'junction value agreement');eq(n,s.diff(l,x).subs(x,a),s.diff(r,x).subs(x,a),'junction derivative agreement')
f=2*x/(4-x*x)-s.Rational(5,2)*x;eq(42,f.subs(x,-x),-f,'odd symmetry');eq(42,s.diff(f,x).subs(x,0),-2,'origin slope');eq(42,f.subs(x,1),-s.Rational(11,6),'hole limit')
C=5000+10*x+x*x/20
for hh,v in [(5,s.Rational(2025,100)),(1,s.Rational(2005,100))]:eq(49,(C.subs(x,100+hh)-C.subs(x,100))/hh,v,'cost difference quotient')
N={2008:16680,2010:16858,2012:18066}
eq(56,s.Rational(N[2010]-N[2008],2),89,'growth interval');eq(56,s.Rational(N[2012]-N[2010],2),604,'growth interval');eq(56,s.Rational(N[2012]-N[2008],4),s.Rational(693,2),'centered growth')
f=s.sin(x)-s.sin(1000*x)/1000;eq(59,s.limit(f/x,x,0),0,'independent origin derivative limit')
f=x**3-2*x*x+2;dd=s.Rational(2,5)
for lo,hi,v in [(1-dd,1,-s.Rational(124,100)),(1,1+dd,-s.Rational(44,100)),(1-dd,1+dd,-s.Rational(84,100))]:eq(60,(f.subs(x,hi)-f.subs(x,lo))/(hi-lo),v,'three independently entered secant slopes')
eq(60,(s.Rational('16432.7')-s.Rational('7596.1'))/8,s.Rational('1104.575'),'source table centered difference')
Path(__file__).with_name('s2-1-independent.json').write_text(json.dumps({'section':'2.1','passed':len(checks),'checks':checks},indent=2)+'\n');print(len(checks),'checks passed')
