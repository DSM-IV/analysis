"""Independent exact boundary integrations for §16.8 (source visually checked)."""
import sympy as s,json
from pathlib import Path
x,y,z,t=s.symbols('x y z t',real=True)
v=s.Matrix([x,y,z])
fields={2:[x*x*s.sin(z),y*y,x*y],3:[z*s.exp(y),x*s.cos(y),x*z*s.sin(y)],4:[s.atan(x*x*y*z*z),x*x*y,x*x*z*z],5:[x*y*z,x*y,x*x*y*z],6:[s.exp(x*y),s.exp(x*z),x*x*z],7:[x+y*y,y+z*z,z+x*x],8:[1,x+y*z,x*y-s.sqrt(z)],9:[x*y,y*z,z*x],10:[2*y,x*z,x+y],11:[-y*x*x,x*y*y,s.exp(x*y)],12:[z*s.exp(x),z-y**3,x-z**3],13:[x*x*y,x**3,s.exp(z)*s.atan(z)],14:[x**3-z,x*y,y+z*z],15:[x*x*z,x*y*y,z*z],16:[x*x*y,x**3/3,x*y],17:[-y,x,-2],18:[-2*y*z,y,3*x],19:[y,z,x],21:[z*z,2*x*y,4*y*y],22:[y+s.sin(x),z*z+s.cos(y),x**3]}
expected={2:0,3:16*s.pi,4:0,5:0,6:0,7:-1,8:s.Rational(1,24),9:-s.Rational(17,20),10:s.pi,11:8*s.pi,12:-4*s.pi,13:s.pi/2,14:-s.pi/4,15:81*s.pi/2,16:s.pi,17:-32*s.pi,18:8*s.pi,19:-s.pi,21:3,22:s.pi}
c=s.cos(t);q=s.sin(t)
curves={2:[c,q,0],3:[4*c,0,-4*q],4:[2,2*c,2*q],6:[c,0,-q],10:[c,q,q+2],11:[2*c,2*q,0],12:[3,2*c,2*q],13:[c,q,q],14:[(1+c)/2,q/2,(1+c)/2],15:[3*c,3*q,1-3*c-3*q],16:[c,q,q*q-c*c],17:[4*c,-4*q,4],18:[2*c,2*q,1],19:[c,0,-q],22:[q,c,2*q*c]}
polygons={5:[(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1)],7:[(1,0,0),(0,1,0),(0,0,1)],8:[(0,0,1),(s.Rational(1,3),0,0),(0,s.Rational(1,2),0)],21:[(0,0,0),(1,0,0),(1,2,1),(0,2,1)]}
def path_integral(F,r,a,b):
 r=s.Matrix(r); f=s.Matrix(F).subs(dict(zip(v,r)),simultaneous=True)
 return s.integrate(s.trigsimp(s.expand(f.dot(r.diff(t)))),(t,a,b))
results=[]
for n,F in fields.items():
 if n in curves:
  # Exact differentials are removed to avoid unnecessary integration of their
  # non-elementary primitives along a closed path.
  if n==13:F=[x*x*y,x**3,0]
  if n==22:F=[y,z*z,x**3]
  ans=path_integral(F,curves[n],0,2*s.pi)
 elif n in polygons:
  pts=polygons[n];ans=0
  if n==8:F=[1,x+y*z,x*y] # removed gradient -sqrt(z) k integrates to zero
  for a,b in zip(pts,pts[1:]+pts[:1]):ans+=path_integral(F,[aa+t*(bb-aa) for aa,bb in zip(a,b)],0,1)
 elif n==9:
  ans=path_integral(F,[t,0,1-t*t],0,1)+path_integral(F,[c,q,0],0,s.pi/2)+path_integral(F,[0,1-t,1-(1-t)**2],0,1)
 else:raise AssertionError(n)
 assert s.simplify(ans-expected[n])==0,(n,ans,expected[n])
 results.append({'number':n,'method':'independent oriented boundary integral','result':str(s.simplify(ans)),'pass':True})
 print(n,'PASS',s.simplify(ans),flush=True)
root=Path(__file__).resolve().parent
(root/'s16-8-report.json').write_text(json.dumps({'section':'16.8','sourcePages':[1274,1275,1276],'checks':results,'proofReview':[1,20,23,24]},indent=2)+'\n')
