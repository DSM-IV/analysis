"""Independent checks of source-specific algebra and difficult borderline cases."""
import sympy as s,json,math
from pathlib import Path
x=s.symbols('x',real=True);R=s.Rational;checks=[]
def eq(name,z):assert s.simplify(z)==0,(name,z);checks.append(name)
f=(2*x**3+3*x*x-12*x+7)/9
for c,v in[(-2,3),(1,0)]:eq('67value'+str(c),f.subs(x,c)-v);eq('67stationary'+str(c),s.diff(f,x).subs(x,c))
f=(1+x)/(1+x*x);eq('68factor',s.diff(f,x,2)-2*(x-1)*(x*x+4*x+1)/(1+x*x)**3)
for c in[1,-2-s.sqrt(3),-2+s.sqrt(3)]:eq('68line'+str(c),f.subs(x,c)-(c+3)/4)
q=2*x/(x*x+3)**2;eq('80derivative',s.diff(q,x)-6*(1-x*x)/(x*x+3)**3);eq('80threshold',q.subs(x,1)-R(1,8))
for n,f,expected in[(22,s.cos(x)**2-2*s.sin(x),-2*(s.cos(2*x)-s.sin(x))),(51,2*s.cos(x)+s.cos(x)**2,-2*(s.cos(x)+s.cos(2*x))),(57,s.sin(2*x)+s.sin(4*x),-4*s.sin(2*x)*(1+8*s.cos(2*x)))]:eq(str(n)+' trig second derivative',s.trigsimp(s.diff(f,x,2)-expected))
for n,poly,count in[(59,24*x**6+64*x**5+115*x**4+115*x**3+92*x*x+32*x-1,2),(60,3*x**9+3*x**8+36*x**7-7*x**6+81*x**5+21*x**4-278*x**3+195*x*x-744*x+236,3)]:
 assert s.Poly(poly,x).count_roots(-s.oo,s.oo)==count;checks.append(str(n)+' complete Sturm real-root count')
# Opposite-monotonicity product examples retain positive, convex factors.
for f,g in[(s.exp(2*x),s.exp(-x)),(s.exp(x),(10-x*x)*s.exp(-x)),(s.exp(x),x*s.exp(-x))]:
 for c in[R(21,10),R(5,2),R(29,10)]:
  assert all(float(v.subs(x,c))>0 for v in[f,g,s.diff(f,x),-s.diff(g,x),s.diff(f,x,2),s.diff(g,x,2)])
 checks.append('71 product factor conditions '+str(g))
# Piecewise constructions: all intended smooth joins and specified horizontal slopes.
forms={31:[(2/s.pi-s.pi*x*x/4,2/s.pi*s.cos(s.pi*x/2),0),(2/s.pi*s.cos(s.pi*x/2),2/s.pi-s.pi*(x-4)**2/4,4)],33:[(1-s.exp(x-2),-6/s.pi*s.cos(s.pi*(x-5)/6),2),(-6/s.pi*s.cos(s.pi*(x-5)/6),1-s.exp(8-x),8)],34:[(x+1,-s.log(2-x)-x/2+s.log(3)-R(1,2),-1),(-s.log(x-2)+(x-2)/2,1-s.log(2)-(x-4)**2,4)],35:[(2/s.pi*(1-s.cos(s.pi*x/2)),4/s.pi-s.pi*(x-6)**2/4,6)]}
for n,joins in forms.items():
 for l,r,c in joins:
  eq(f'{n} continuous join {c}',l.subs(x,c)-r.subs(x,c))
  if(n,c)!=(34,-1):eq(f'{n} first derivative join {c}',s.diff(l,x).subs(x,c)-s.diff(r,x).subs(x,c))
p=Path(__file__).with_name('s3-3-independent.json');p.write_text(json.dumps({'section':'3.3','passed':len(checks),'checks':checks},indent=2)+'\n');print('PASS',len(checks),'independent checks')
