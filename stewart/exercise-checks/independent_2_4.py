import sympy as s,json
from pathlib import Path
x=s.symbols('x',real=True);a,b=s.symbols('a b',real=True);checks=[]
def eq(n,left,right,method):
 z=s.trigsimp(s.simplify(left-right));assert z==0,(n,z);checks.append({'number':n,'method':method,'residual':'0'})
items=[(1,3*s.sin(x)-2*s.cos(x),3*s.cos(x)+2*s.sin(x)),(2,s.tan(x)-4*s.sin(x),s.sec(x)**2-4*s.cos(x)),(3,x*x+s.cot(x),2*x-s.csc(x)**2),(4,2*s.sec(x)-s.csc(x),2*s.sec(x)*s.tan(x)+s.csc(x)*s.cot(x)),(5,x*x*s.sin(x),2*x*s.sin(x)+x*x*s.cos(x)),(6,3*x+x*x*s.cos(x),3+2*x*s.cos(x)-x*x*s.sin(x)),(7,s.sec(x)*s.tan(x),s.sec(x)*s.tan(x)**2+s.sec(x)**3),(8,s.sin(x)*s.cos(x),s.cos(x)**2-s.sin(x)**2),(9,(x-s.cos(x))*s.sin(x),(1+s.sin(x))*s.sin(x)+(x-s.cos(x))*s.cos(x)),(10,x*s.cos(x)+2*s.tan(x),s.cos(x)-x*s.sin(x)+2*s.sec(x)**2),(11,s.cos(x)**2,-2*s.sin(x)*s.cos(x)),(12,x*(a*s.cos(x)+b*s.cot(x)),a*s.cos(x)+b*s.cot(x)-a*x*s.sin(x)-b*x*s.csc(x)**2),(13,s.sin(x)/(1+s.cos(x)),1/(1+s.cos(x))),(14,s.cos(x)/(1-s.sin(x)),1/(1-s.sin(x))),(15,x/(2-s.tan(x)),(2-s.tan(x)+x*s.sec(x)**2)/(2-s.tan(x))**2),(16,s.cot(x)/x**2,-s.csc(x)**2/x**2-2*s.cot(x)/x**3),(17,(1+s.sec(x))/(1-s.sec(x)),2*s.sec(x)*s.tan(x)/(1-s.sec(x))**2),(18,s.sin(x)/(1+s.tan(x)),(s.cos(x)*(1+s.tan(x))-s.sin(x)*s.sec(x)**2)/(1+s.tan(x))**2),(19,x*s.sin(x)/(1+x),(s.sin(x)+x*(1+x)*s.cos(x))/(1+x)**2),(20,x/(s.sec(x)+s.tan(x)),(s.sec(x)-s.tan(x))*(1-x*s.sec(x))),(21,x*s.cos(x)*s.sin(x),s.cos(x)*s.sin(x)+x*(s.cos(x)**2-s.sin(x)**2)),(22,x*x*s.sin(x)*s.tan(x),2*x*s.sin(x)*s.tan(x)+x*x*s.cos(x)*s.tan(x)+x*x*s.sin(x)*s.sec(x)**2)]
for n,f,de in items:eq(n,s.diff(f,x),de,'independently entered derivative expression')
for n,f,at,slope in[(27,s.sin(x)+s.cos(x),0,1),(28,x+s.sin(x),s.pi,0),(29,x+s.tan(x),s.pi,2),(30,(1+s.sin(x))/s.cos(x),s.pi,1),(31,2*x*s.sin(x),s.pi/2,2),(32,3*x+6*s.cos(x),s.pi/3,3-3*s.sqrt(3))]:eq(n,s.diff(f,x).subs(x,at),slope,'tangent slope at source point')
eq(35,s.diff(s.sin(x)/x,x,2),((2-x*x)*s.sin(x)-2*x*s.cos(x))/x**3,'second derivative')
eq(36,s.diff(s.sec(x),x,2).subs(x,s.pi/4),3*s.sqrt(2),'secant second derivative')
eq(37,(s.tan(x)-1)/s.sec(x),s.sin(x)-s.cos(x),'simplification identity')
eq(38,-2*s.sqrt(3)/2+4/s.Integer(2),2-s.sqrt(3),'product value');eq(38,(-4*s.sqrt(3)/2+1)/16,(1-2*s.sqrt(3))/16,'quotient value')
for z in[2*s.pi/3,4*s.pi/3]:eq(39,1+2*s.cos(z),0,'horizontal tangent arguments')
for z,val in[(7*s.pi/6,-s.sqrt(3)/3),(11*s.pi/6,s.sqrt(3)/3)]:eq(40,s.cos(z)/(2+s.sin(z)),val,'horizontal contact ordinate');eq(40,s.diff(s.cos(x)/(2+s.sin(x)),x).subs(x,z),0,'zero tangent slope')
eq(41,8*s.sin(2*s.pi/3),4*s.sqrt(3),'spring position');eq(41,8*s.cos(2*s.pi/3),-4,'spring velocity')
f=2*s.cos(x)+3*s.sin(x);v=s.diff(f,x);eq(42,f*f+v*v,13,'energy/amplitude identity');eq(43,10*s.cos(s.pi/3),5,'ladder angle sensitivity')
mu,W=s.symbols('mu W',positive=True);F=mu*W/(mu*s.sin(x)+s.cos(x));de=mu*W*(s.sin(x)-mu*s.cos(x))/(mu*s.sin(x)+s.cos(x))**2;eq(44,s.diff(F,x),de,'force derivative');eq(44,de.subs(x,s.atan(mu)),0,'stationary angle')
lims=[(45,s.sin(5*x)/(3*x),0,s.Rational(5,3)),(46,s.sin(x)/s.sin(s.pi*x),0,1/s.pi),(47,s.sin(3*x)/s.sin(x),0,3),(48,s.sin(3*x)**2/x,0,0),(49,s.sin(x)*(1-s.cos(x))/x**2,0,0),(50,(1-s.sec(x))/(2*x),0,0),(51,s.tan(2*x)/x,0,2),(52,s.sin(x)/s.tan(7*x),0,s.Rational(1,7)),(53,s.sin(3*x)/(5*x**3-4*x),0,-s.Rational(3,4)),(54,s.sin(3*x)*s.sin(5*x)/x**2,0,15),(55,s.sin(x)/(x+s.tan(x)),0,s.Rational(1,2)),(56,s.sin(s.sin(x))/s.sin(x),0,1),(57,(s.cos(x)-1)/(2*x*x),0,-s.Rational(1,4)),(58,s.sin(x*x)/x,0,0),(59,(1-s.tan(x))/(s.sin(x)-s.cos(x)),s.pi/4,-s.sqrt(2)),(60,s.sin(x-1)/(x*x+x-2),1,s.Rational(1,3))]
for n,f,at,val in lims:
 for direction in['+','-']:eq(n,s.limit(f,x,at,dir=direction),val,'independent one-sided limit '+direction)
eq(61,s.diff(s.sin(x),x,99),-s.cos(x),'99th derivative');eq(62,s.diff(x*s.sin(x),x,35),-x*s.cos(x)-35*s.sin(x),'35th product derivative')
y=-s.Rational(3,10)*s.sin(x)-s.Rational(1,10)*s.cos(x);eq(63,s.diff(y,x,2)+s.diff(y,x)-2*y,s.sin(x),'differential equation residual')
eq(66,s.pi*s.sin(x)**2/(2*s.sin(x)*s.cos(x)),s.pi/2*s.tan(x),'area ratio after double-angle expansion with x=theta/2');eq(66,s.limit(s.pi/2*s.tan(x/2),x,0,dir='+'),0,'area-ratio limit');eq(67,s.limit(x/(2*s.sin(x/2)),x,0,dir='+'),1,'arc/chord limit')
f=x/s.sqrt(1-s.cos(2*x));eq(68,s.limit(f,x,0,dir='-'),-1/s.sqrt(2),'left radical limit');eq(68,s.limit(f,x,0,dir='+'),1/s.sqrt(2),'right radical limit')
Path(__file__).with_name('s2-4-independent.json').write_text(json.dumps({'section':'2.4','passed':len(checks),'checks':checks},indent=2)+'\n');print(len(checks),'independent checks passed')
