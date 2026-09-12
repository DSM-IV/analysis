import sympy as s
x,y,z=s.symbols('x y z',positive=True)
F=[s.Matrix(v) for v in [(x*y*y*z*z,x*x*y*z*z,x*x*y*y*z),(0,x**3*y*z**2,y**4*z**3),(x*y*s.exp(z),0,y*z*s.exp(x)),(s.sin(y*z),s.sin(z*x),s.sin(x*y)),(s.sqrt(x)/(1+z),s.sqrt(y)/(1+x),s.sqrt(z)/(1+y)),(s.log(2*y+3*z),s.log(x+3*z),s.log(x+2*y)),(s.exp(x)*s.sin(y),s.exp(y)*s.sin(z),s.exp(z)*s.sin(x)),(s.atan(x*y),s.atan(y*z),s.atan(z*x))]]
def curl(f):return s.Matrix([s.diff(f[2],y)-s.diff(f[1],z),s.diff(f[0],z)-s.diff(f[2],x),s.diff(f[1],x)-s.diff(f[0],y)])
def div(f):return sum(s.diff(a,b) for a,b in zip(f,[x,y,z]))
for i,f in enumerate(F,1):
 assert s.simplify(div(curl(f)))==0
 print(i,'curl=',list(curl(f)),'div=',div(f))
for f,p in [(s.Matrix((2*x*y**3*z**2,3*x*x*y*y*z*z,2*x*x*y**3*z)),x*x*y**3*z*z),(s.Matrix((s.log(y),x/y+s.log(z),y/z)),x*s.log(y)+y*s.log(z)),(s.Matrix((y*z*s.sin(x*y),x*z*s.sin(x*y),-s.cos(x*y))),-z*s.cos(x*y)),(s.Matrix((s.exp(z)*s.cos(x),s.exp(y)*s.cos(z),s.exp(z)*s.sin(x)-s.exp(y)*s.sin(z))),s.exp(z)*s.sin(x)+s.exp(y)*s.cos(z))]:
 assert all(s.simplify(f[i]-s.diff(p,v))==0 for i,v in enumerate([x,y,z]))
print('4 potentials and 8 divergence-of-curl checks passed')
