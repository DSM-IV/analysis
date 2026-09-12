"""Independent substitutions and boundary checks against explicit derived results."""
import sympy as s,json
from pathlib import Path
x,a,h=s.symbols('x a h',real=True)
checks=[]
def eq(n,left,right,label):
 residual=s.nsimplify(s.simplify(left-right));assert residual==0,(n,label,residual);checks.append(dict(number=n,method=label,residual=str(residual)))
f=lambda u:3*u*u-u+2
expected=[12,16,3*a*a-a+2,3*a*a+a+2,3*a*a+5*a+4,6*a*a-2*a+4,12*a*a-2*a+2,3*a**4-a*a+2,(3*a*a-a+2)**2,3*a*a+6*a*h-a+3*h*h-h+2]
for raw,res in zip([f(2),f(-2),f(a),f(-a),f(a+1),2*f(a),f(2*a),f(a*a),f(a)**2,f(a+h)],expected):eq(33,raw,res,'independent substitution')
g=lambda u:u/s.sqrt(u+1)
for raw,res in [(g(0),0),(g(3),s.Rational(3,2)),(5*g(a),5*a/s.sqrt(a+1)),(g(4*a)/2,2*a/s.sqrt(4*a+1)),(g(a*a),a*a/s.sqrt(a*a+1)),(g(a)**2,a*a/(a+1)),(g(a+h),(a+h)/s.sqrt(a+h+1)),(g(x-a),(x-a)/s.sqrt(x-a+1))]:eq(34,raw,res,'independent substitution')
eq(35,((4+3*(3+h)-(3+h)**2)-(4+9-9))/h,-3-h,'difference quotient identity')
eq(36,((a+h)**3-a**3)/h,3*a*a+3*a*h+h*h,'difference quotient identity')
eq(37,(1/x-1/a)/(x-a),-1/(a*x),'difference quotient identity')
eq(38,(s.sqrt(x+2)-s.sqrt(3))/(x-1),1/(s.sqrt(x+2)+s.sqrt(3)),'conjugate identity')
for n,expr,fact in [(39,x*x-9,(x-3)*(x+3)),(40,x*x+4*x-21,(x+7)*(x-3)),(43,x*x-5*x,x*(x-5)),(46,x*x-4*x-5,(x-5)*(x+1))]:eq(n,expr,fact,'independent factorization')
for n,fn,vals in [(49,lambda z:z*z+2 if z<0 else z,[11,0,2]),(50,lambda z:5 if z<2 else s.Rational(1,2)*z-3,[5,5,-2]),(51,lambda z:z+1 if z<=-1 else z*z,[-2,0,4]),(52,lambda z:-1 if z<=1 else 7-2*z,[-1,-1,3])]:
 for z,v in zip([-3,0,2],vals):eq(n,fn(z),v,'branch inequality and substitution')
for n,fn,points in [(59,s.Rational(5,2)*x-s.Rational(11,2),[(1,-3),(5,7)]),(60,-s.Rational(5,3)*x+s.Rational(5,3),[(-5,10),(7,-10)])]:
 for z,v in points:eq(n,fn.subs(x,z),v,'endpoint substitution')
eq(65,2*x+2*(10-x),20,'restore perimeter')
eq(66,x*16/x,16,'restore area')
eq(67,(s.sqrt(3)*x/2)**2+(x/2)**2,x*x,'Pythagorean height check')
eq(68,2*x*x*4/x**2,8,'restore volume')
eq(69,x*x*(2/x**2),2,'restore volume')
eq(70,s.pi*(5/s.sqrt(s.pi*x))**2*x,25,'restore volume')
eq(71,(12-2)*(20-2),180,'unit cut example')
height=15-x/2-s.pi*x/4
eq(72,x+2*height+s.pi*x/2,30,'restore perimeter')
eq(72,x*height+s.pi*x*x/8,15*x-(4+s.pi)*x*x/8,'independent area expansion')
eq(74,10+s.Rational(6,100)*1200,82,'billing breakpoint')
eq(74,82+s.Rational(7,100)*800,138,'billing endpoint')
eq(75,s.Rational(1,10)*4000,400,'tax band calculation')
eq(75,1000+s.Rational(15,100)*6000,1900,'tax band calculation')
eq(30,s.Rational(1,2)+10*(s.Rational(1,10)+s.Rational(797,100))+40*s.Rational(797,100),400,'independent trapezoidal speed integral')
eq(31,(70+78)/2,74,'linear interpolation')
for n,fn,sign in [(81,x/(1+x*x),-1),(82,x*x/(1+x**4),1),(84,x*s.Abs(x),-1),(85,1+3*x*x-x**4,1)]:eq(n,fn.subs(x,-x),sign*fn,'symbolic parity identity')
root=Path(__file__).resolve().parents[1]
(root/'exercise-checks/s1-1-independent.json').write_text(json.dumps({'section':'1.1','checks':checks,'passed':len(checks)},ensure_ascii=False,indent=2)+'\n')
print(len(checks),'independent checks passed')
