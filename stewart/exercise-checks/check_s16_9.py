"""Exact independent integrations for the well-defined §16.9 fluxes."""
import sympy as s,json
from pathlib import Path
x,y,z,r,t,R,a,b,c=s.symbols('x y z r t R a b c',real=True,positive=True)
checks=[]
def ck(n,value,want,method):
 assert s.simplify(value-want)==0,(n,value,want)
 checks.append({'number':n,'method':method,'result':str(s.simplify(value)),'pass':True});print(n,'PASS',s.simplify(value),flush=True)
ck(1,s.integrate(3+3*x,(x,0,1)),s.Rational(9,2),'volume integral')
ck(2,s.integrate(10*s.pi*z*z,(z,0,9)),2430*s.pi,'horizontal slices')
ck(3,4*s.pi*4**3/3,256*s.pi/3,'ball volume')
ck(4,9*s.pi*s.integrate(2*x,(x,0,2)),36*s.pi,'cylinder slices')
ck(5,s.integrate(2*x*y*z**3,(x,0,3),(y,0,2),(z,0,1)),s.Rational(9,2),'box integral')
ck(6,s.integrate(6*x*y*z,(x,0,a),(y,0,b),(z,0,c)),3*a*a*b*b*c*c/4,'box integral')
ck(7,9*s.integrate(r**3,(r,0,1),(t,0,2*s.pi)),9*s.pi/2,'cylindrical integral')
ck(8,12*s.pi*s.integrate(r**4,(r,0,2)),384*s.pi/5,'spherical integral')
ck(9,s.diff(x*s.exp(y),x)+s.diff(z-s.exp(y),y)+s.diff(-x*y,z),0,'identically zero divergence')
ck(10,s.integrate(x*x*(2-x-y**3),(x,-1,1),(y,-1,1)),s.Rational(8,3),'FORMAL ONLY: ordinary surface integral undefined at tan poles')
ck(11,12*s.pi*s.integrate(r**3*(1-r*r),(r,0,1)),s.pi,'cylindrical integral')
ck(12,s.integrate(3*r*s.sin(t)*(2-r*s.sin(t))*r,(r,0,2),(t,0,2*s.pi)),-12*s.pi,'polar projected integral')
ck(13,s.integrate(2*x*z,(z,0,(4-x)/2),(x,0,4),(y,0,3)),16,'triangular prism integral')
ck(14,s.integrate(y+2*z,(z,0,1-x),(x,y*y,1),(y,-1,1)),s.Rational(32,105),'smooth part plus reflected square-root flux cancellation')
ck(15,s.integrate(1+x,(z,0,c*(1-x/a-y/b)),(y,0,b*(1-x/a)),(x,0,a)),a*b*c*(a+4)/24,'tetrahedron integral')
ck(16,20*s.pi*s.integrate(r**4,(r,0,R)),4*s.pi*R**5,'spherical integral')
ck(17,8*s.pi*s.integrate(r**3,(r,0,1)),2*s.pi,'half-ball integral')
d=s.cos(x)*s.cos(y)**2+3*s.sin(y)**2*s.cos(y)*s.cos(z)**4+5*s.sin(z)**4*s.cos(z)*s.cos(x)**6
ck(18,s.integrate(d,(x,0,s.pi/2),(y,0,s.pi/2),(z,0,s.pi/2)),19*s.pi**2/64,'symbolic triple integral')
ck(19,2*s.pi/s.Integer(5)+s.pi/4,13*s.pi/20,'closed half-ball minus base')
ck(20,s.integrate((2-r*r)*r,(r,0,1),(t,0,2*s.pi)),3*s.pi/2,'direct surface flux after odd terms cancel')
ck(26,s.integrate(s.cos(t)**2*s.sin(t),(t,0,s.pi))*2*s.pi,4*s.pi/3,'direct scalar sphere integral')
p=Path(__file__).with_name('s16-9-report.json');p.write_text(json.dumps({'section':'16.9','checks':checks,'logicalReview':[21,22,23,24,25,27,28,29,30,31,32,33,34],'errata':[{'number':10,'issue':'tan(z) has poles on the stated boundary; the ordinary flux does not exist'}]},indent=2)+'\n')
