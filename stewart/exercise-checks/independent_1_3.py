import math,json
from pathlib import Path
import sympy as s
checks=[];xs=[-30,-21,-20,-4,-2,-1,-.5,0,.5,1,2,3,4,5,10,25,26,30]
cbrt=lambda z:math.copysign(abs(z)**(1/3),z)
R=lambda z:True
nz=lambda z:abs(z)>1e-10
positive=lambda z:z>0
pairs={35:(lambda z:z**3+5,R,cbrt,R),36:(lambda z:1/z,nz,lambda z:2*z+1,R),37:(lambda z:1/math.sqrt(z),positive,lambda z:z+1,R),38:(lambda z:z/(z+1),lambda z:nz(z+1),lambda z:2*z-1,R),39:(lambda z:2/z,nz,math.sin,R),40:(lambda z:math.sqrt(max(0,5-z)),lambda z:z<=5,lambda z:math.sqrt(max(0,z-1)),lambda z:z>=1)}
expected={35:[(lambda z:z+5,R),(lambda z:cbrt(z**3+5),R),(lambda z:(z**3+5)**3+5,R),(lambda z:math.copysign(abs(z)**(1/9),z),R)],36:[(lambda z:1/(2*z+1),lambda z:nz(2*z+1)),(lambda z:2/z+1,nz),(lambda z:z,nz),(lambda z:4*z+3,R)],37:[(lambda z:1/math.sqrt(z+1),lambda z:z>-1),(lambda z:1/math.sqrt(z)+1,positive),(lambda z:z**.25,positive),(lambda z:z+2,R)],38:[(lambda z:(2*z-1)/(2*z),nz),(lambda z:(z-1)/(z+1),lambda z:nz(z+1)),(lambda z:z/(2*z+1),lambda z:nz(z+1)and nz(2*z+1)),(lambda z:4*z-3,R)],39:[(lambda z:2/math.sin(z),lambda z:nz(math.sin(z))),(lambda z:math.sin(2/z),nz),(lambda z:z,nz),(lambda z:math.sin(math.sin(z)),R)],40:[(lambda z:math.sqrt(max(0,5-math.sqrt(z-1))),lambda z:1<=z<=26),(lambda z:math.sqrt(max(0,math.sqrt(5-z)-1)),lambda z:z<=4),(lambda z:math.sqrt(max(0,5-math.sqrt(5-z))),lambda z:-20<=z<=5),(lambda z:math.sqrt(max(0,math.sqrt(z-1)-1)),lambda z:z>=2)]}
for n,(f,df,g,dg)in pairs.items():
 for part,(outer,do,inner,di),(want,dwant)in zip('abcd',[(f,df,g,dg),(g,dg,f,df),(f,df,f,df),(g,dg,g,dg)],expected[n]):
  maxerr=0;valid=0
  for z in xs:
   actualdomain=di(z)and do(inner(z));assert actualdomain==dwant(z),(n,part,z,actualdomain,dwant(z))
   if actualdomain:
    got=outer(inner(z));val=want(z);err=abs(got-val)/max(1,abs(val));assert err<1e-9,(n,part,z,err);maxerr=max(maxerr,err);valid+=1
  checks.append(dict(number=n,part=part,method='independent nested evaluation plus domain-boundary probes',testedInputs=len(xs),validInputs=valid,maxRelativeError=maxerr))
x=s.symbols('x',real=True)
def eq(n,left,right):
 r=s.simplify(left-right);assert r==0,(n,r);checks.append(dict(number=n,method='independent symbolic identity',residual=str(r)))
eq(19,x*x-2*x+5,(x-1)**2+4)
f=1/(x-1);g=1/x-2
for val,res in [(f+g,(-2*x*x+4*x-1)/(x*(x-1))),(f-g,(2*x*x-2*x+1)/(x*(x-1))),(f*g,(1-2*x)/(x*(x-1))),(f/g,x/((x-1)*(1-2*x)))]:eq(34,val,res)
eq(59,s.pi*(60*x)**2,3600*s.pi*x*x)
eq(60,s.Rational(4,3)*s.pi*(2*x)**3,s.Rational(32,3)*s.pi*x**3)
eq(61,(30*x)**2+36,900*x*x+36)
eq(62,(350*x)**2+1,122500*x*x+1)
eq(64,4*(32-7),100)
eq(66,s.Rational(104,100)**4,s.Rational(116985856,100000000))
eq(67,(2*x+1)**2+6,4*x*x+4*x+7);eq(67,3*(x*x+x-1)+5,3*x*x+3*x+2)
eq(68,4*(x+4)-17,4*x-1)
eq(71,(2**x+2**(-x))/2+x*x+9+(2**x-2**(-x))/2-6*x,2**x+(x-3)**2)
F={1:3,2:1,3:5,4:6,5:2,6:4};G={1:5,2:3,3:4,4:1,5:3,6:2}
for n,computed,want in [(55,[F[G[3]],G[F[2]],F[G[5]],G[F[5]]],[6,5,5,3]),(56,[G[G[G[2]]],F[F[F[1]]],F[F[G[1]]],G[F[G[3]]]],[1,2,1,2])]:
 assert computed==want;checks.append(dict(number=n,method='independent table lookups',values=computed))
root=Path(__file__).resolve().parents[1];(root/'exercise-checks/s1-3-independent.json').write_text(json.dumps({'section':'1.3','passed':len(checks),'checks':checks},ensure_ascii=False,indent=2)+'\n');print(len(checks),'checks passed')
