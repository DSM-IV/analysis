import json,math
from pathlib import Path
import mpmath as mp
import sympy as s
mp.mp.dps=50
root=Path(__file__).resolve().parents[1];report=json.loads((root/'exercise-checks/s1-2-report.json').read_text());checks=[]
data={29:[(4000,14.1),(6000,13),(8000,13.4),(12000,12.5),(16000,12),(20000,12.4),(30000,10.5),(45000,9.4),(60000,8.2)],30:[(50,2),(400,6),(500,5),(900,10),(1100,26),(1600,42),(1800,37),(2000,38),(3000,50)],31:[(50.1,178.5),(48.3,173.6),(45.2,164.8),(44.7,163.7),(44.5,168.3),(42.7,165),(39.5,155.4),(38,155.8)],32:[(0,8.24),(2,8.44),(4,8.95),(6,10.40),(8,11.26),(10,11.54),(12,11.88),(14,12.52),(16,12.90)],33:[(0,60083),(5,66533),(10,70099),(15,76784),(20,84077),(25,87302),(30,94071)],34:[(.387,.241),(.723,.615),(1,1),(1.523,1.881),(5.203,11.861),(9.541,29.457),(19.190,84.008),(30.086,164.784)],36:[(4,5),(40,9),(3459,40),(4411,39),(29418,84),(44218,76)]}
for r in report['checks']:
 n=r['number'];points=[(mp.mpf(str(u)),mp.mpf(str(v))) for u,v in data[n]]
 if n in [34,36]:points=[(mp.log(u),mp.log(v)) for u,v in points]
 ux=[u for u,v in points];vy=[v for u,v in points];r11=mp.sqrt(sum(u*u for u in ux));q1=[u/r11 for u in ux];r12=sum(q1);w=[1-r12*q for q in q1];r22=mp.sqrt(sum(q*q for q in w));q2=[q/r22 for q in w];bhat=sum(q*v for q,v in zip(q2,vy))/r22;mhat=(sum(q*v for q,v in zip(q1,vy))-r12*bhat)/r11;coef=[mhat,bhat];err=max(abs(coef[0]-r['slope']),abs(coef[1]-r['intercept']));assert err<mp.mpf('1e-8'),(n,err)
 checks.append(dict(number=n,method='independent 50-digit QR least squares',coefficientMaxError=str(err),slope=str(coef[0]),intercept=str(coef[1])))
def eq(n,L,R):
 residual=s.nsimplify(s.simplify(L-R));assert residual==0,(n,residual);checks.append(dict(number=n,method='independent substitution or scaling',residual=str(residual)))
x=s.symbols('x');eq(7,(2*x-3).subs(x,2),1)
for z,v in [(0,18),(3,0),(4,2)]:eq(11,2*(z-3)**2,v)
for z,v in [(-2,2),(0,1),(1,s.Rational(-5,2))]:eq(12,-z*z-s.Rational(5,2)*z+1,v)
for z,v in [(-1,0),(0,0),(2,0),(1,6)]:eq(13,-3*z*(z+1)*(z-2),v)
eq(14,s.Rational(2,100)*200+s.Rational(850,100),s.Rational(25,2))
eq(15,s.Rational(417,10000)*200,s.Rational(834,100))
eq(18,(16-10)/6*60,60);eq(18,s.Rational(7,6)*60,70)
for z,v in [(100,2200),(300,4800)]:eq(19,13*z+900,v)
for z,v in [(480,380),(800,460),(1500,635)]:eq(20,s.Rational(z,4)+260,v)
eq(21,15+s.Rational(434,1000)*(s.Rational(85000,434)),100)
eq(22,s.Rational(35,10000)/s.Rational(8,1000)**2,s.Rational(875,16))
eq(23,1/s.Rational(1,2)**2,4)
eq(24,s.Rational(671,1000)*39,s.Rational(26169,1000))
eq(25,2**3,8);eq(25,(2*x)**2/x**2,4)
for z,v in [(100,'5.67'),(200,'90.72'),(300,'459.27')]:eq(26,s.Rational(567,10**10)*z**4,s.Rational(v))
area=(mp.mpf(4)/mp.mpf('.7'))**(mp.mpf(10)/3);res=abs(mp.mpf('.7')*area**mp.mpf('.3')-4);assert res<mp.mpf('1e-45');checks.append(dict(number=35,method='independent 50-digit inverse power substitution',residual=str(res)))
(root/'exercise-checks/s1-2-independent.json').write_text(json.dumps({'section':'1.2','passed':len(checks),'checks':checks},ensure_ascii=False,indent=2)+'\n');print(len(checks),'passed')
