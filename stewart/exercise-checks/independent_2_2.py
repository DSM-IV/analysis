"""Independently entered formulas and data, without importing the author module."""
import sympy as s,json,math
from pathlib import Path
x,h=s.symbols('x h',real=True);m,b=s.symbols('m b');checks=[]
def eq(n,v,w,method):
 residual=s.simplify(v-w);assert residual==0,(n,residual);checks.append(dict(number=n,method=method,residual='0'))
items=[(17,x*x,2*x),(18,x**3,3*x*x),(19,3*x-8,3),(20,m*x+b,m),(21,s.Rational(5,2)*x*x+6*x,5*x+6),(22,4+8*x-5*x*x,8-10*x),(23,4*x**3+3*x,12*x*x+3),(24,x**3-5*x+1,3*x*x-5),(25,1/(x*x-4),-2*x/(x*x-4)**2),(26,x/(x+2),2/(x+2)**2),(27,(x+1)/(4*x-1),-5/(4*x-1)**2),(28,x**4,4*x**3),(29,1/s.sqrt(1+x),-1/(2*(1+x)**s.Rational(3,2))),(30,1/(1+s.sqrt(x)),-1/(2*s.sqrt(x)*(1+s.sqrt(x))**2)),(31,1+s.sqrt(x+3),1/(2*s.sqrt(x+3))),(32,x+1/x,1-1/x**2),(33,x**4+2*x,4*x**3+2)]
for n,f,de in items:
 eq(n,s.diff(f,x),de,'independently entered analytic derivative')
 for a in [s.Rational(1,2),3]:eq(n,s.limit((f.subs(x,a+h)-f.subs(x,a))/h,h,0),s.sympify(de).subs(x,a),'pointwise defining difference quotient')
for n,f,ders in [(51,3*x*x+2*x+1,[6*x+2,6]),(52,x**3-3*x,[3*x*x-3,6*x]),(53,2*x*x-x**3,[4*x-3*x*x,4-6*x,-6,0])]:
 for k,v in enumerate(ders,1):eq(n,s.diff(f,x,k),v,'independently entered higher derivative')
for n,ts,ys,expected in [(34,[2000,2002,2004,2006,2008,2010,2012,2014],[5500,4897,7470,9138,10897,11561,13035,13945],[-301.5,492.5,1060.25,856.75,605.75,534.5,596,455]),(35,[14,21,28,35,42,49],[41,54,64,72,78,83],[13/7,23/14,18/14,1,11/14,5/7]),(36,[15.5,17.7,20,22.4,24.4],[37.2,31,19.8,9.7,-9.8],[-6.2/2.2,-17.4/4.5,-21.3/4.7,-29.6/4.4,-19.5/2])]:
 for i,v in enumerate(expected):
  lo=max(0,i-1);hi=min(len(ts)-1,i+1);actual=(ys[hi]-ys[lo])/(ts[hi]-ts[lo]);assert abs(actual-v)<1e-10,(n,i,actual,v);checks.append(dict(number=n,method='independently transcribed centered/endpoint secant',argument=ts[i],value=actual))
eq(43,(1-1/(2*s.sqrt(-x))).subs(x,-1),s.Rational(1,2),'negative branch tangent')
eq(44,s.diff((1-x*x)**s.Rational(2,3),x).subs(x,0),0,'smooth central point')
for a in [-8,-1,1,8]:
 u=s.real_root(s.Integer(a),3);eq(55,1/(3*u*u),s.Rational(1,3)/s.Integer(a)**s.Rational(2,3)if a>0 else s.Rational(1,3)/s.Integer(-a)**s.Rational(2,3),'real cube-root derivative')
eq(59,s.limit(s.Abs(h),h,0),0,'origin defining quotient')
eq(62,s.limit(h,h,0,dir='+'),0,'right quadratic quotient at zero')
eq(63,s.limit((1/(1-h)-1)/h,h,0,dir='+'),1,'right derivative at four')
eq(63,s.limit(((5-(4+h))-1)/h,h,0,dir='-'),-1,'left derivative at four')
eq(65,3+3**2/s.Integer(2),s.Rational(15,2),'first distance junction')
eq(65,s.Rational(15,2)+5,s.Rational(25,2),'second distance junction')
eq(65,s.Rational(25,2)+4*5,s.Rational(65,2),'third distance junction')
assert round(math.degrees(math.atan(2)))==63;checks.append(dict(number=66,method='inclination angle',degrees=math.degrees(math.atan(2))))
# An independently expressed local velocity sketch verifies the plotted a(10),j(10).
u=s.symbols('u');v=54+10*u-5*u*u-2*u**3
eq(54,s.diff(v,u).subs(u,0),10,'illustrative velocity first derivative')
eq(54,s.diff(v,u,2).subs(u,0),-10,'illustrative velocity second derivative')
report={'section':'2.2','passed':len(checks),'checks':checks,'graphicalReview':{'sourcePages':[165,166,167,168,169,170,171],'notes':['39: independent source cross-read confirms only -4 and 0; steep right branch is not a vertical tangent.','46: enlarged source tangent at 1 is slightly positive, not exactly zero; less than blue height at -1.','54: local quartic fits to calibrated graph support positive acceleration and negative jerk; values are explicitly uncertain.']}}
Path(__file__).with_name('s2-2-independent.json').write_text(json.dumps(report,indent=2)+'\n');print(len(checks),'independent checks passed')
