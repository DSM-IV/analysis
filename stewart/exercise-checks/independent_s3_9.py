"""Independent physical-model, boundary and numerical-integral checks."""
import sympy as s,mpmath as mp,json
from pathlib import Path
x=s.symbols('x');R=s.Rational;checks=[]
def eq(n,z):assert s.simplify(z)==0,(n,z);checks.append(n)
L,m,rho,g,E,I=s.symbols('L m rho g E I');f=g/(E*I)*(m*(L*x*x/2-x**3/6)+rho*(L*L*x*x/4-L*x**3/6+x**4/24))
eq('70ODE',E*I*s.diff(f,x,2)-m*g*(L-x)-rho*g*(L-x)**2/2);eq('70height0',f.subs(x,0));eq('70slope0',s.diff(f,x).subs(x,0));eq('70tip',f.subs(x,L)-g/(E*I)*(m*L**3/3+rho*L**4/8))
f=10*x+R(9,2)*x*x-R(3,20)*x**3;eq('73position10',f.subs(x,10)-400);eq('73speed10',s.diff(f,x).subs(x,10)-55);eq('73landing',400+55*(R(130,11)-10)-500)
positions=[10*x**3,270+270*(x-3)-16*(x-3)**2,914-178*(x-17)+16*(x-17)**2,424-18*(x-22)]
for j,t in enumerate([3,17,22]):
 eq('78position continuity'+str(t),(positions[j]-positions[j+1]).subs(x,t));eq('78velocity continuity'+str(t),s.diff(positions[j]-positions[j+1],x).subs(x,t))
eq('78maximum time',s.diff(positions[1],x).subs(x,R(183,16)));eq('78maximum height',positions[1].subs(x,R(183,16))-R(22545,16));eq('78landing',positions[3].subs(x,R(410,9)))
eq('79acceleration time',R(264)/R(12,5)-110);eq('79a distance miles',R(264)*110/2/5280+60-R(251,4));eq('79b distance miles',R(264)*(1200-110)/5280-R(109,2));eq('79c time',R(60)*5280/264+110-1310);eq('79d distance',R(264)*(2250-110)/5280-107)
eq('56 minimum', (x*x-2*x**R(3,2)+1).subs(x,R(9,4))+R(11,16))
mp.mp.dps=35
for n,fn,upper in[(57,lambda z:mp.sin(z)/(1+z*z),2*mp.pi),(58,lambda z:mp.sqrt(z**4-2*z*z+2)-2,mp.mpf(3))]:
 h=upper/1200;trap=h*(fn(0)/2+sum(fn(j*h)for j in range(1,1200))+fn(upper)/2);exact=mp.quad(fn,[0,upper/2,upper]);assert abs(trap-exact)<mp.mpf('0.00001');checks.append(str(n)+' displayed numerical integral versus high-precision quadrature')
Path(__file__).with_name('s3-9-independent.json').write_text(json.dumps({'section':'3.9','passed':len(checks),'checks':checks},indent=2)+'\n');print('PASS',len(checks),'independent checks')
