import sympy as s,json
from pathlib import Path
x,y,z,a,b,c,r,t,k,q,tau=s.symbols('x y z a b c r t k q tau',real=True)
coords=(x,y,z)
def curl(F):return s.Matrix([s.diff(F[2],y)-s.diff(F[1],z),s.diff(F[0],z)-s.diff(F[2],x),s.diff(F[1],x)-s.diff(F[0],y)])
res=[]
def check(label,expr):
 assert all(s.simplify(v)==0 for v in (list(expr)if isinstance(expr,s.MatrixBase)else[expr])),label
 res.append(label)
rr=s.sqrt(x*x+y*y+z*z);F=s.Matrix([x,y,z])/rr**3
check('1 radial field divergence away from origin',sum(s.diff(F[i],coords[i])for i in range(3)))
check('2 Green integrand',s.diff(-2*x**3,x)-s.diff(y**3-y,y)-(1-6*x*x-3*y*y))
check('2 independent ellipse boundary integral',s.integrate((y**3-y).subs(y,s.sin(t)/s.sqrt(3))*(-s.sin(t)/s.sqrt(6))-2*(s.cos(t)/s.sqrt(6))**3*s.cos(t)/s.sqrt(3),(t,0,2*s.pi))-s.pi/(6*s.sqrt(2)))
n=s.Matrix([a,b,c]);check('3 constant-normal curl',curl(n.cross(s.Matrix(coords))/2)-n)
u,v=s.symbols('u v',real=True)
for cc in [0,1,s.Rational(1,2)]:
 for ww in [s.asin(cc),s.pi-s.asin(cc)]:
  xx=s.sin(u);yy=s.sin(ww-u);check(f'4 trace c={cc}, w={ww}',s.trigsimp(xx*xx+yy*yy+2*s.cos(ww)*xx*yy-cc**2))
F=s.Matrix([s.Function('F'+str(i))(*coords)for i in range(3)]);G=s.Matrix([s.Function('G'+str(i))(*coords)for i in range(3)])
grad=lambda f:s.Matrix([s.diff(f,w)for w in coords]);direc=lambda H,J:s.Matrix([sum(H[j]*s.diff(J[i],coords[j])for j in range(3))for i in range(3)])
check('5 arbitrary C1 component identity',grad(F.dot(G))-direc(F,G)-direc(G,F)-F.cross(curl(G))-G.cross(curl(F)))
Xu=s.Matrix([1-q*k*s.cos(v),-q*tau*s.sin(v),q*tau*s.cos(v)]);Xv=s.Matrix([0,-q*s.sin(v),q*s.cos(v)]);cr=Xu.cross(Xv)
check('7b Frenet area factor squared',cr.dot(cr)-q*q*(1-q*k*s.cos(v))**2)
check('7b angle integration',s.integrate(q*(1-q*k*s.cos(v)),(v,0,2*s.pi))-2*s.pi*q)
check('7d helix length',s.integrate(s.sqrt(s.sin(t)**2+s.cos(t)**2+1),(t,0,4*s.pi))-4*s.pi*s.sqrt(2))
R=Path(__file__).resolve().parents[1];(R/'exercise-checks/s16-11-report.json').write_text(json.dumps({'sourceVisualPages':[1288,1289],'checks':res,'manualProofReview':[1,2,3,4,5,6,7]},indent=2)+'\n');print('PASS:',len(res),'independent symbolic identities')
