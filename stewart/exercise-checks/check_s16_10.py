"""Independent exact integrals and high precision checks for Chapter 16 Review."""
import sympy as s,json,mpmath as m
from pathlib import Path
x,y,z,t,r=s.symbols('x y z t r',real=True)
results=[]
def ck(n,value,want,method):
 assert s.simplify(value-want)==0,(n,value,want)
 results.append({'number':n,'method':method,'result':str(s.simplify(value)),'pass':True});print(n,'PASS',s.simplify(value),flush=True)
def line(F,rr,lo,hi):
 rr=s.Matrix(rr); vv=s.Matrix(F).subs(dict(zip([x,y,z],rr)),simultaneous=True)
 return s.integrate(s.trigsimp(s.expand(vv.dot(rr.diff(t)))),(t,lo,hi))
ck(2,s.integrate(t*s.sqrt(1+4*t*t),(t,0,1)),(5*s.sqrt(5)-1)/12,'direct arc-length integral')
ck(3,s.integrate(9*s.sqrt(10)*s.sin(t)*s.cos(t)**2,(t,0,s.pi)),6*s.sqrt(10),'direct helix scalar integral')
ck(4,line([y,x+y*y,0],[3*s.cos(t),2*s.sin(t),0],0,2*s.pi),0,'ellipse parametrization')
ck(5,line([y**3,x*x,0],[1-t*t,t,0],-1,1),s.Rational(4,15),'parabola parametrization')
ck(6,s.integrate(4*t**6+2*t*s.exp(t*t)+3*t**9,(t,0,1)),s.E-s.Rational(9,70),'direct substituted integrand')
ck(7,line([x*y,y*y,y*z],[1+2*t,4*t,-1+3*t],0,1),s.Rational(110,3),'segment parametrization')
ck(8,line([x*y,x*x,0],[s.sin(t),1+t,0],0,s.pi),s.pi/4,'direct planar curve')
ck(9,line([s.exp(z),x*z,x+y],[t*t,t**3,-t],0,1),s.Rational(11,12)-4/s.E,'direct spatial curve')
ck('10a',line([z,x,y],[3-3*t,s.pi*t/2,3*t],0,1),(3*s.pi-9)/2,'straight segment')
ck('10b',line([z,x,y],[3*s.cos(t),t,3*s.sin(t)],0,s.pi/2),-3*s.pi/4,'helix')
for n,p,F in [(11,x*s.exp(x*y)+s.exp(y),[(1+x*y)*s.exp(x*y),s.exp(y)+x*x*s.exp(x*y),0]),(12,x*s.sin(y)+s.cos(z),[s.sin(y),x*s.cos(y),-s.sin(z)]),(13,x**4*y*y-x*x*y**3+y**4,[4*x**3*y*y-2*x*y**3,2*x**4*y-3*x*x*y*y+4*y**3,0]),(14,x*s.exp(y)+y*s.exp(z),[s.exp(y),x*s.exp(y)+s.exp(z),y*s.exp(z)]),(37,x**3*y*z-3*x*y+z*z,[3*x*x*y*z-3*y,x**3*z-3*x,x**3*y+2*z])]:
 assert all(s.simplify(s.diff(p,v)-f)==0 for v,f in zip([x,y,z],F)),n
 results.append({'number':n,'method':'differentiate potential against all source components','pass':True})
ck(15,line([x*y*y,-x*x*y,0],[t,t*t,0],-1,1)+line([x*y*y,-x*x*y,0],[1-2*t,1,0],0,1),0,'both boundary pieces')
ck(16,s.integrate(2*y,(y,0,3*x),(x,0,1)),3,'Green integral')
ck(17,line([x*x*y,-x*y*y,0],[2*s.cos(t),2*s.sin(t),0],0,2*s.pi),-8*s.pi,'circle parametrization')
ck(25,s.integrate(2*x*s.sqrt(5+4*x*x),(x,0,1)),(27-5*s.sqrt(5))/6,'graph surface area')
ck(27,s.integrate(2*s.pi*r**3*s.sqrt(1+4*r*r),(r,0,2)),s.pi*(391*s.sqrt(17)+1)/60,'polar area integral')
ck(28,4*s.sqrt(3)*s.integrate(r**3,(r,0,2),(t,0,2*s.pi)),32*s.sqrt(3)*s.pi,'symmetry and radial integral')
ck(29,-2*4*s.pi*2**3/3,-64*s.pi/3,'divergence volume integral')
ck(30,s.integrate(r**3,(r,0,1),(t,0,2*s.pi)),s.pi/2,'direct surface integral after odd terms cancel')
ck(31,line([x*x,y*y,z*z],[s.cos(t),s.sin(t),0],0,2*s.pi),0,'direct boundary integral')
ck(32,line([x*x*y*z,y*z*z,z**3*s.exp(x*y)],[2*s.cos(t),2*s.sin(t),1],0,2*s.pi),-4*s.pi,'direct boundary integral')
pts=[(1,0,0),(0,1,0),(0,0,1)];v=0
for a,b in zip(pts,pts[1:]+pts[:1]):v+=line([x*y,y*z,z*x],[aa+t*(bb-aa) for aa,bb in zip(a,b)],0,1)
ck(33,v,-s.Rational(1,2),'three direct segment integrals')
ck(34,s.integrate(3*(r*r+z*z)*r,(r,0,1),(t,0,2*s.pi),(z,0,2)),11*s.pi,'cylindrical divergence integral')
ck(35,3*4*s.pi/3,4*s.pi,'unit-ball integral')
ck(38,line([2*x-2*y/(x*x+y*y),2*y+2*x/(x*x+y*y),0],[s.cos(t),s.sin(t),0],0,2*s.pi),4*s.pi,'unit-circle representative of winding class')
ck(39,3*(2**3-1),21,'remaining volume')
m.mp.dps=45
p1=2*m.mpf(3)**7/7*m.quad(lambda v:1/(1+v**4),[-3,0,3])
p2=2*(2*m.mpf(3)**5/5)*m.quad(lambda u:u*u/(1+u**4),[0,1,3])
v1=p1+p2
m.mp.dps=65
v2=2*m.mpf(3)**7/7*m.quad(lambda v:1/(1+v**4),[-3,-1,0,1,3])+2*(2*m.mpf(3)**5/5)*m.quad(lambda u:u*u/(1+u**4),[0,.5,1,2,3])
assert abs(v1-v2)<m.mpf('1e-35')
results.append({'number':'26d','method':'separated integrals at 45 and 65 digits, different interval splits','value':str(v2),'rounded':'1524.0190','pass':True})
print('26d PASS',v2)
# The source Review 24b integrand genuinely has a non-integrable endpoint.
rem=2*s.sin(t)*s.cot(s.sin(t))*s.cos(t)-s.csc(s.sin(t))**2*s.cos(t)
ck('24b',s.limit(t*t*rem,t,0),-1,'nonintegrable -1/t^2 leading term: ordinary integral undefined')
Path(__file__).with_name('s16-10-report.json').write_text(json.dumps({'section':'16.10','checks':results,'sourceVisualPages':[1285,1286,1287],'errata':[{'number':24,'part':'b','issue':'cot/csc terms undefined at zeros of sin(t); ordinary line integral diverges'}],'manualProofReview':[1,18,19,20,21,22,23,36,40,41]},indent=2)+'\n')
