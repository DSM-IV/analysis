"""Independent symbolic stationarity and boundary checks for optimization."""
import sympy as s,json,math
from pathlib import Path
x=s.symbols('x',positive=True);R=s.Rational
cases=[(3,x+100/x,10),(4,x*x+(16-x)**2,8),(7,x*(50-x),25),(8,2*x+2000/x,s.sqrt(1000)),(9,x/(1+x*x),1),(10,100*x/(x*x+x+4),2),(11,375*x-R(5,2)*x*x,75),(12,x*(3-2*x)**2,R(1,2)),(13,3*x+3000000/x,1000),(14,2*x*(1200-4*x),150),(15,x*(250-R(3,2)*x),R(250,3)),(16,30*x+160000/x,40*s.sqrt(30)/3),(18,x*x+128000/x,40),(19,(1200*x-x**3)/4,20),(20,x*(4-2*x)*(3-3*x),1-1/s.sqrt(3)),(21,20*x*x+180/x,R(9,2)**R(1,3)),(22,32*x*x+180/x,R(45,16)**R(1,3)),(23,x*x*(108-4*x),18),(24,s.pi*x*x*(108-2*s.pi*x),36/s.pi),(26,(x-3)**2+x,R(5,2)),(29,16*x*x*(1-x*x),1/s.sqrt(2)),(32,(1+x)**2*(1-x*x),R(1,2)),(33,x**3*(2-x),R(3,2)),(36,2*x*(4-x*x),2/s.sqrt(3)),(37,2*s.pi*x*(1-x*x),1/s.sqrt(3)),(38,x*(1-x)**2,R(1,3)),(40,30*x-(2+s.pi/2)*x*x,30/(4+s.pi)),(41,(x+8)*(384/x+12),16),(42,(x-2)*(180/x-3),2*s.sqrt(30)),(43,x*x/16+s.sqrt(3)*(10-x)**2/36,40*s.sqrt(3)/(9+4*s.sqrt(3))),(44,x*x/16+(10-x)**2/(4*s.pi),40/(4+s.pi)),(45,16*x-x*x,8),(46,8/s.sin(x)+4/s.cos(x),s.atan(2**R(1,3))),(47,(1-x*x)*x,1/s.sqrt(3)),(48,s.pi**2*x**4+6561/x**2,(81/(s.pi*s.sqrt(2)))**R(1,3)),(49,x*(1-x)**2,R(1,3)),(51,x/(x+1)**2,1),(52,x**3/(x-1),R(3,2)),(53,-R(3,2)/s.tan(x)+3*s.sqrt(3)/(2*s.sin(x)),s.acos(1/s.sqrt(3))),(54,400*x*x+225*(x-1)**2,R(9,25)),(57,400000*x+800000*s.sqrt((6-x)**2+4),6-2/s.sqrt(3)),(59,1/x**2+3/(10-x)**2,10/(1+3**R(1,3))),(60,5*x*x/(2*(x-3)),6),(62,120*x*x-15*x**4,2),(63,4*x*x+36/x**2,s.sqrt(3)),(64,(4+x*x)**2/(4*x),2/s.sqrt(3)),(65,16000/x+200+4*s.sqrt(x),400),(66,-16000+1200*x-R(54,10)*x*x-R(4,1000)*x**3,100),(67,57000*x-3000*x*x,R(19,2)),(68,(x-6)*(40-2*x),13),(69,380*x-x*x/8-35000,1520),(70,(16+x)*(240-8*x),7),(71,x*x*(1-2*x),R(1,3)),(79,x**3/(x-4),6),(81,s.atan(3*x)-s.atan(x),1/s.sqrt(3)),(82,100*s.sin(x)*(1+s.cos(x)),s.pi/3)]
records=[]
for n,f,c in cases:
 df=s.diff(f,x);v=s.simplify(df.subs(x,c));assert v==0 or abs(float(v.evalf()))<1e-20,(n,v)
 curvature=float(s.diff(f,x,2).subs(x,c).evalf());assert abs(curvature)>1e-10
 records.append({'exercise':n,'stationaryResidual':str(v),'secondDerivative':curvature,'objectiveAtSolution':str(s.simplify(f.subs(x,c)))})
assert s.simplify(next(f for n,f,c in cases if n==20).subs(x,1-1/s.sqrt(3))-4*s.sqrt(3)/3)==0
D,z=s.symbols('D z',positive=True);I=2*(z+D+25)/((z+D+25)**2-100*z)
assert s.simplify(s.diff(I,z)-2*(100*(D+25)-(z+D+25)**2)/((z+D+25)**2-100*z)**2)==0
assert s.solve(2/(D+25)-1/D-1/(D+100),D)==[50]
report=json.loads(Path(__file__).with_name('s3-7-report.json').read_text());import mpmath as mp;mp.mp.dps=40
for key in['58','75height']:
 r=mp.mpf(report['numericalChecks'][key]);f=(lambda t:t/mp.sqrt(t*t+1)-2*(6-t)/mp.sqrt((6-t)**2+4))if key=='58' else(lambda t:t/mp.sqrt(t*t+4)+t/mp.sqrt(t*t+9)-1)
 assert abs(f(r))<mp.mpf('1e-35')
# Bisection independently recovers all three sine-distance stationary candidates.
f=lambda t:t-4+(mp.sin(t)-2)*mp.cos(t)
for a,b,expect in zip([2,4,5.5],[3,5.5,7],report['numericalChecks']['28']):
 a=mp.mpf(a);b=mp.mpf(b);assert f(a)*f(b)<0
 for j in range(150):
  mid=(a+b)/2
  if f(a)*f(mid)<=0:b=mid
  else:a=mid
 assert abs((a+b)/2-mp.mpf(expect))<mp.mpf('1e-35')
Path(__file__).with_name('s3-7-independent.json').write_text(json.dumps({'section':'3.7','symbolicCases':records,'additionalChecks':['20 exact maximum volume','86 derivative in squared centered coordinate','86 global switch d^2=50','58 numerical stationarity','75 numerical stationarity','28 three independent bisections']},indent=2)+'\n')
print('PASS',len(records),'symbolic extrema and additional boundary/numerical checks')
