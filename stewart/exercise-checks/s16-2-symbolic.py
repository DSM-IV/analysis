import sympy as s
import mpmath as m
x,y,z,t=s.symbols('x y z t',real=True)
calc={}
def scalar(n,f,r,a,b):
 speed=s.sqrt(sum(s.diff(q,t)**2 for q in r));q=s.simplify(f.subs(dict(zip([x,y,z],r)),simultaneous=True)*speed);calc[n]=(r,a,b,q)
def vector(n,F,r,a,b):
 q=s.simplify(sum(f.subs(dict(zip([x,y,z],r)),simultaneous=True)*s.diff(v,t) for f,v in zip(F,r)));calc[n]=(r,a,b,q)
scalar(1,y,(t*t,2*t),0,3);scalar(2,x/y,(t**3,t**4),1,2);scalar(3,x*y**4,(4*s.cos(t),4*s.sin(t)),-s.pi/2,s.pi/2);scalar(4,x*s.exp(y),(2+3*t,4*t),0,1)
vector(5,(s.S(0),x*x*y+s.sin(x)),(t,t*t),0,s.pi);vector(6,(s.exp(x),s.S(0)),(t**3,t),-1,1)
scalar(9,x*x*y,(s.cos(t),s.sin(t),t),0,s.pi/2);scalar(10,y*y*z,(3-2*t,1+t,2+3*t),0,1);scalar(11,x*s.exp(y*z),(t,2*t,3*t),0,1);scalar(12,x*x+y*y+z*z,(t,s.cos(2*t),s.sin(2*t)),0,2*s.pi)
vector(13,(s.S(0),x*y*s.exp(y*z),s.S(0)),(t,t*t,t**3),0,1);vector(14,(-y,x*s.log(x),y*s.exp(z)),(s.exp(t),2*t,s.log(t)),1,2);vector(15,(z,x*y,y*y),(s.sin(t),s.cos(t),s.tan(t)),-s.pi/4,s.pi/4);vector(16,(y,z,x),(s.sqrt(t),t,t*t),1,4);vector(17,(z*z,x*x,y*y),(1+3*t,t,2*t),0,1)
vector(21,(x*y*y,-x*x),(t**3,t*t),0,1);vector(22,(x+y*y,x*z,y+z),(t*t,t**3,-2*t),0,2);vector(23,(s.sin(x),s.cos(y),x*z),(t**3,-t*t,t),0,1);vector(24,(x*z,z**3,y),(s.exp(t),s.exp(2*t),s.exp(-t)),-1,1)
vector(25,(s.sqrt(x+y),y/x),(s.sin(t)**2,s.sin(t)*s.cos(t)),s.pi/6,s.pi/3);vector(26,(y*z*s.exp(x),z*x*s.exp(y),x*y*s.exp(z)),(s.sin(t),s.cos(t),s.tan(t)),0,s.pi/4);scalar(27,x*y*s.atan(z),(t*t,t**3,s.sqrt(t)),1,2);scalar(28,z*s.log(x+y),(1+3*t,2+t*t,t**4),-1,1)
vector(29,(x-y,x*y),(2*s.cos(t),2*s.sin(t)),0,3*s.pi/2);vector(31,(s.exp(x-1),x*y),(t*t,t**3),0,1);vector(32,(x,-z,y),(2*t,3*t,-t*t),-1,1)
vector(42,(x*x,y*s.exp(x)),(1+t*t,t),0,1);vector(43,(x-y*y,y-z*z,z-x*x),(2*t,t,1-t),0,1)
for n,(r,a,b,q) in calc.items():
 if n in [25,26,27,28]:
  m.mp.dps=35;v=m.quad(s.lambdify(t,q,'mpmath'),[m.mpf(str(s.N(a,35))),m.mpf(str(s.N(b,35)))]);print(n,'numeric',m.nstr(v,20),flush=True)
 else:
  v=s.simplify(s.integrate(q,(t,a,b)));print(n,'integrand',s.latex(q),'answer',s.latex(v),flush=True)
q=3*s.sqrt(2)*s.exp(-7*t)*s.cos(4*t)**3*s.sin(4*t)**2
# cos³u sin²u = (2cos u-cos3u-cos5u)/16
q2=3*s.sqrt(2)*s.exp(-7*t)*(2*s.cos(4*t)-s.cos(12*t)-s.cos(20*t))/16
assert s.trigsimp(s.expand_trig(q-q2))==0
v=s.integrate(q2,(t,0,2*s.pi));print(33,s.simplify(v),flush=True)
