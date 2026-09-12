import sympy as s,json
from pathlib import Path
x,h=s.symbols('x h',real=True);checks=[]
def limit(n,f,a,v,side='+'):
 got=s.limit(f,x,a,dir=side);assert got==v or s.simplify(got-v)==0,(n,got,v)
 checks.append({'number':n,'method':'independently entered exact limit','direction':side,'value':str(got)})
for n,f,a,v in [(3,4*x*x-5*x,5,75),(4,2*x**3+6*x*x-9,-3,-9),(5,(x*x+2*x)*(2*x**3-5),2,88),(6,(3*x*x+1)/(x*x-5*x+2),7,s.Rational(37,4)),(7,s.sqrt(9-x**3+2*x*x),-2,5),(8,(x+5)**s.Rational(1,3)*(2*x*x-3*x),3,18),(9,((2*x**5-x**4)/(5*x*x+4))**3,-1,-s.Rational(1,27)),(11,3*x-7,-2,-13),(12,8-x/2,6,5),(35,x/(s.sqrt(1+3*x)-1),0,s.Rational(2,3)),(36,(s.sqrt(3+x)-s.sqrt(3))/x,0,s.sqrt(3)/6),(43,s.Abs(x+4)-2*x,-4,8),(46,(2-s.Abs(x))/(2+x),-2,1),(66,(s.sqrt(6-x)-2)/(s.sqrt(3-x)-1),2,s.Rational(1,2)),(67,(3*x*x+15*x+18)/(x*x+x-2),-2,-1)]:
 for side in ['-','+']:limit(n,f,a,v,side)
for n,f,a,side,v in [(15,(x*x+5*x+4)/(x-2),2,'-',-s.oo),(15,(x*x+5*x+4)/(x-2),2,'+',s.oo),(16,(x*x+3*x)/(x*x-x-12),4,'-',-s.oo),(16,(x*x+3*x)/(x*x-x-12),4,'+',s.oo),(44,s.Abs(x+4)/(2*x+8),-4,'-',-s.Rational(1,2)),(44,s.Abs(x+4)/(2*x+8),-4,'+',s.Rational(1,2)),(45,(2*x-1)/s.Abs(2*x**3-x*x),s.Rational(1,2),'-',-4),(47,1/x-1/s.Abs(x),0,'-',-s.oo),(48,1/x-1/s.Abs(x),0,'+',0)]:limit(n,f,a,v,side)
for n,f,lo,up in [(37,x*x*s.cos(20*s.pi*x),-x*x,x*x),(38,s.sqrt(x**3+x*x)*s.sin(s.pi/x),-s.sqrt(x**3+x*x),s.sqrt(x**3+x*x)),(41,x**4*s.cos(2/x),-x**4,x**4),(42,s.sqrt(x)*(1+s.sin(2*s.pi/x)**2),s.sqrt(x),2*s.sqrt(x))]:
 for bound in [lo,up]:limit(n,bound,0,0)
for n,f in [(33,x**3),(34,x**-2)]:
 q=s.limit((f.subs(x,x+h)-f)/h,h,0);assert s.simplify(q-s.diff(f,x))==0
 checks.append({'number':n,'method':'difference quotient equals independently differentiated source function','value':str(q)})
r=s.symbols('r',positive=True);qx=r*r/2;qy=r*s.sqrt(1-r*r/4);rx=2*(1+s.sqrt(1-r*r/4))
for name,e in [('origin-circle',qx*qx+qy*qy-r*r),('fixed-circle',(qx-1)**2+qy*qy-1),('collinearity',r*qx+rx*(qy-r))]:
 assert s.simplify(e)==0
 checks.append({'number':68,'method':name,'residual':'0'})
assert s.limit(rx,r,0,dir='+')==4
checks.append({'number':68,'method':'rationalized geometric limit','value':'4'})
p=Path(__file__).with_name('s1-6-independent.json');p.write_text(json.dumps({'section':'1.6','passed':len(checks),'checks':checks},indent=2)+'\n');print(len(checks),'checks passed')
