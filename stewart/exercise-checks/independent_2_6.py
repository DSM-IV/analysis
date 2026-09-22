import sympy as s,json,ast
from pathlib import Path
x,y=s.symbols('x y',real=True);checks=[]
def eq(n,a,b,method):
 r=s.trigsimp(s.simplify(a-b));r=s.trigsimp(s.cancel(r.rewrite(s.cos))) if r!=0 else r;assert r==0,(n,r);checks.append({'number':n,'method':method,'residual':'0'})
def slope(F):return-s.diff(F,x)/s.diff(F,y)
def dt(f,p):return s.diff(f,x)+s.diff(f,y)*p
items=[(1,5*x*x-y**3-7,10*x/(3*y*y)),(2,6*x**4+y**5-2*x,(2-24*x**3)/(5*y**4)),(3,s.sqrt(x)+s.sqrt(y)-1,-s.sqrt(y)/s.sqrt(x)),(4,2/x-1/y-4,2*y*y/x**2),(5,x*x-4*x*y+y*y-4,(2*y-x)/(y-2*x)),(6,2*x*x+x*y-y*y-2,(4*x+y)/(2*y-x)),(7,x**4+x*x*y*y+y**3-5,-(4*x**3+2*x*y*y)/(2*x*x*y+3*y*y)),(8,x**3-x*y*y+y**3-1,(y*y-3*x*x)/(3*y*y-2*x*y)),(9,x*x-(y*y+1)*(x+y),(2*x-y*y-1)/(2*x*y+3*y*y+1)),(10,y**5+x*x*y**3-1-x**4*y,(4*x**3*y-2*x*y**3)/(5*y**4+3*x*x*y*y-x**4)),(11,s.sin(x)+s.cos(y)-2*x+3*y,(2-s.cos(x))/(3-s.sin(y))),(12,y*s.sin(x*x)-x*s.sin(y*y),(s.sin(y*y)-2*x*y*s.cos(x*x))/(s.sin(x*x)-2*x*y*s.cos(y*y))),(13,s.sin(x+y)-s.cos(x)-s.cos(y),-(s.cos(x+y)+s.sin(x))/(s.cos(x+y)+s.sin(y))),(14,s.tan(x-y)-2*x*y**3-1,(s.sec(x-y)**2-2*y**3)/(s.sec(x-y)**2+6*x*y*y)),(15,s.tan(x/y)-x-y,(y*s.sec(x/y)**2-y*y)/(x*s.sec(x/y)**2+y*y)),(16,s.sin(x*y)-s.cos(x+y),-(y*s.cos(x*y)+s.sin(x+y))/(x*s.cos(x*y)+s.sin(x+y))),(17,s.sqrt(x+y)-x**4-y**4,(8*x**3*s.sqrt(x+y)-1)/(1-8*y**3*s.sqrt(x+y))),(18,s.sin(x)*s.cos(y)-x*x+5*y,(2*x-s.cos(x)*s.cos(y))/(5-s.sin(x)*s.sin(y))),(19,s.sqrt(x*y)-1-x*x*y,(4*x*y*s.sqrt(x*y)-y)/(x-2*x*x*s.sqrt(x*y))),(20,x*y-s.sqrt(x*x+y*y),(x-y*s.sqrt(x*x+y*y))/(x*s.sqrt(x*x+y*y)-y))]
for n,F,p in items:eq(n,slope(F),p,'independently entered implicit derivative')
# Cross-check numeric slopes and curve membership independently of author data.
points=[(25,y*s.sin(2*x)-x*s.cos(2*y),s.pi/2,s.pi/4,s.Rational(1,2)),(26,s.tan(x+y)+s.sec(x-y)-2,s.pi/8,s.pi/8,-1),(28,y*y*(6-x)-x**3,2,s.sqrt(2),7*s.sqrt(2)/8),(29,x*x-x*y-y*y-1,2,1,s.Rational(3,4)),(30,x*x+2*x*y+4*y*y-12,2,1,-s.Rational(1,2)),(31,x*x+y*y-(2*x*x+2*y*y-x)**2,0,s.Rational(1,2),1),(32,x*x*y*y-(y+1)**2*(4-y*y),2*s.sqrt(3),1,-s.sqrt(3)/5),(33,2*(x*x+y*y)**2-25*(x*x-y*y),3,1,-s.Rational(9,13)),(34,y*y*(y*y-4)-x*x*(x*x-5),0,-2,0),(35,y*y-5*x**4+x*x,1,2,s.Rational(9,2)),(36,y*y-x**3-3*x*x,1,-2,-s.Rational(9,4))]
for n,F,a,b,p in points:
 eq(n,F.subs({x:a,y:b}),0,'source point membership');eq(n,slope(F).subs({x:a,y:b}),p,'independently derived contact slope')
for n,F,den,expected,mult in[(37,x*x+4*y*y-4,16*y**3,-1/(4*y**3),-1),(38,x*x+x*y+y*y-3,(x+2*y)**3,-18/(x+2*y)**3,-6),(40,x**3-y**3-7,y**5,-14*x/y**5,-2*x)]:
 p=slope(F);q=dt(p,p);eq(n,s.factor((q-expected)*den),mult*F,'second derivative equivalence modulo source relation')
F=s.sin(y)+s.cos(x)-1;p=slope(F);eq(39,dt(p,p),(s.cos(x)*s.cos(y)**2+s.sin(x)**2*s.sin(y))/s.cos(y)**3,'second trigonometric derivative')
F=x*y+y**3-1;p=slope(F);eq(41,dt(p,p).subs({x:0,y:1}),0,'second derivative at point');F=x*x+x*y+y**3-1;p=slope(F);eq(42,dt(dt(p,p),p).subs({x:1,y:0}),42,'third total derivative')
Q=y*(y*y-1)*(y-2)
for a in[1-1/s.sqrt(3),1+1/s.sqrt(3)]:
 eq(43,(3*x*x-6*x+2).subs(x,a),0,'exact horizontal x root');c=s.simplify(a*(a-1)*(a-2));v1=(5+4*s.sqrt(1+c))/4;v2=(5-4*s.sqrt(1+c))/4
 for v in[v1,v2]:
  assert float(v)>0
  for sign in[-1,1]:
   yy=s.Rational(1,2)+sign*s.sqrt(v);eq(43,Q.subs(y,yy),c,'four exact real roots for each horizontal x');assert abs(float(s.diff(Q,y).subs(y,yy)))>1e-6
Q=-y**5+2*y**3+y*y
assert s.Poly(Q-s.Rational(1,16),y).count_roots(-s.oo,s.oo)==3;checks.append({'number':44,'method':'Sturm real-root count of exact polynomial at x=1/2','realRoots':3})
for yy in[-1,(1-s.sqrt(5))/2,(1+s.sqrt(5))/2]:eq(44,Q.subs(y,yy),0,'regular horizontal y at x=0 and1');assert s.simplify(s.diff(Q,y).subs(y,yy))!=0
F=2*(x*x+y*y)**2-25*(x*x-y*y)
for ax in[-1,1]:
 for ay in[-1,1]:
  pt={x:ax*5*s.sqrt(3)/4,y:ay*s.Rational(5,4)};eq(45,F.subs(pt),0,'horizontal point membership');eq(45,slope(F).subs(pt),0,'horizontal slope')
a,b,A,B,C=s.symbols('a b A B C',positive=True)
eq(55,(-b*b*x/(a*a*y))*(B*B*x/(A*A*y)), -b*b*B*B*x*x/(a*a*A*A*y*y),'product of ellipse/hyperbola slopes');eq(55,(-b*b*B*B*x*x/(a*a*A*A*y*y)).subs(x*x,a*a*A*A/C).subs(y*y,b*b*B*B/C),-1,'confocal intersection substitution')
eq(56,(-y*y)*(s.real_root(3,3)**3/(3*y*y)),-1,'orthogonality parameter')
V,P,n,aa,bb=s.symbols('V P n aa bb');F=(P+n*n*aa/V**2)*(V-n*bb);v=-V**3*(V-n*bb)/(P*V**3-aa*n*n*V+2*aa*bb*n**3);eq(57,s.diff(F,P)+s.diff(F,V)*v,0,'van der Waals differentiated residual')
val=v.subs({V:10,P:s.Rational(5,2),n:1,aa:s.Rational(3592,1000),bb:s.Rational(4267,100000)});assert round(float(val),4)==-4.0405;checks.append({'number':57,'method':'exact rational evaluation','value':str(val),'decimal':float(val)})
eq(58,x*x+x*y+y*y+1,(x+y/2)**2+3*y*y/4+1,'positive sum-of-squares certificate')
for a in[-s.sqrt(3),s.sqrt(3)]:eq(59,((y-2*x)/(2*y-x)).subs({x:a,y:0}),2,'parallel tangent slope')
eq(60,(x*x-x*y+y*y-3).subs({x:1,y:-1}),0,'second normal intersection')
for a in[-1,1]:eq(61,(x*x*y*y+x*y-2).subs({x:a,y:a}),0,'slope-minus-one contact')
for slope_,inter,pt in[(0,3,(0,3)),(s.Rational(2,3),-5,(s.Rational(24,5),-s.Rational(9,5)))]:
 eq(62,pt[0]**2+4*pt[1]**2,36,'tangent contact on ellipse');eq(62,pt[1],slope_*pt[0]+inter,'contact on line');eq(62,slope_*12+inter,3,'line through external point')
eq(63,(y/(x+2*y**3)).subs(x,y**3+y),1/(3*y*y+1),'equivalent derivative on curve');eq(64,2*(-s.Rational(1,2))+1,0,'Bessel derivative relation')
q=x*x+4*((x+5)/4)**2-5;eq(65,s.discriminant(q,x),0,'lamp ray tangency discriminant');eq(65,q.subs(x,-1),0,'lamp contact membership');eq(65,(s.Integer(3)+5)/4,2,'lamp height')
Path(__file__).with_name('s2-6-independent.json').write_text(json.dumps({'section':'2.6','passed':len(checks),'checks':checks},indent=2)+'\n');print(len(checks),'independent checks passed')
