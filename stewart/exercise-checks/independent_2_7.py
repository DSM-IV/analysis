import sympy as s,json,math,mpmath as mp
from pathlib import Path
t,x,r=s.symbols('t x r',real=True);checks=[]
def eq(n,a,b,why):
 v=s.trigsimp(s.simplify(a-b));assert v==0,(n,v);checks.append({'number':n,'method':why,'residual':'0'})
fs=[t**3-9*t*t+24*t,t**4/s.Integer(100)-t**3/s.Integer(25),s.sin(s.pi*t/2),9*t/(t*t+9)]
vs=[3*(t-2)*(t-4),t*t*(t-3)/25,s.pi/2*s.cos(s.pi*t/2),9*(9-t*t)/(t*t+9)**2]
acc=[6*(t-3),3*t*(t-2)/25,-s.pi**2/4*s.sin(s.pi*t/2),18*t*(t*t-27)/(t*t+9)**3]
turns=[[0,2,4,6],[0,3,6],[0,1,3,5,6],[0,3,6]];distances=[44,s.Rational(243,50),6,s.Rational(9,5)]
for n,(f,v,a,ts,dd)in enumerate(zip(fs,vs,acc,turns,distances),1):
 eq(n,s.diff(f,t),v,'independently entered velocity');eq(n,s.diff(v,t),a,'independently entered acceleration');eq(n,sum(abs(f.subs(t,ts[i+1])-f.subs(t,ts[i]))for i in range(len(ts)-1)),dd,'distance from turning-point partition')
 for at in ts[1:-1]:eq(n,v.subs(t,at),0,'direction-change velocity zero')
 for at in[1]:checks.append({'number':n,'method':'one-second velocity and acceleration','velocity':str(v.subs(t,at)),'acceleration':str(a.subs(t,at))})
signcases={1:[(1,-1),(s.Rational(5,2),1),(s.Rational(7,2),-1),(5,1)],2:[(1,1),(s.Rational(5,2),-1),(4,1)],3:[(s.Rational(1,2),-1),(s.Rational(3,2),1),(s.Rational(5,2),-1),(s.Rational(7,2),1)],4:[(1,-1),(4,1),(6,-1)]}
for n,pairs in signcases.items():
 for at,sign in pairs:eq(n,s.sign((vs[n-1]*acc[n-1]).subs(t,at)),sign,'speed-change sign test')
verts=[(0,0),(1,3),(3,3),(5,0),(7,0),(8,-3)]
for i,expected in enumerate([3,0,-s.Rational(3,2),0,-3]):eq(8,s.Rational(verts[i+1][1]-verts[i][1],verts[i+1][0]-verts[i][0]),expected,'source line-segment acceleration')
h=2+s.Rational(245,10)*t-s.Rational(49,10)*t*t;v=s.diff(h,t);eq(9,h.subs(t,s.Rational(5,2)),s.Rational(261,8),'maximum height');eq(9,v.subs(t,2),s.Rational(49,10),'two-second velocity');eq(9,v.subs(t,4),-s.Rational(147,10),'four-second velocity');hit=(s.Rational(245,10)+s.sqrt(s.Rational(63945,100)))/s.Rational(98,10);eq(9,h.subs(t,hit),0,'impact-time substitution');eq(9,v.subs(t,hit),-s.sqrt(s.Rational(63945,100)),'impact velocity')
h=80*t-16*t*t;eq(10,h.subs(t,s.Rational(5,2)),100,'maximum height')
for at,vel in[(2,16),(3,-16)]:eq(10,h.subs(t,at),96,'height at crossing');eq(10,s.diff(h,t).subs(t,at),vel,'crossing velocity')
h=15*t-s.Rational(186,100)*t*t;v=s.diff(h,t);eq(11,v.subs(t,2),s.Rational(756,100),'Mars velocity');eq(11,v*v+s.Rational(744,100)*h,225,'Mars height-velocity identity')
f=t**4-4*t**3-20*t*t+20*t
for at in[0,5]:eq(12,s.diff(f,t).subs(t,at),20,'velocity20 time')
eq(12,s.diff(f,t,2).subs(t,1+s.sqrt(39)/3),0,'zero acceleration')
eq(13,s.diff(x*x,x).subs(x,15),30,'wafer area derivative');eq(14,s.diff(x**3,x).subs(x,3),27,'cube volume derivative')
for b,v in[(3,5*s.pi),(s.Rational(5,2),s.Rational(9,2)*s.pi),(s.Rational(21,10),s.Rational(41,10)*s.pi)]:eq(15,s.pi*(b*b-4)/(b-2),v,'circle average rate')
for at,val in[(1,7200),(3,21600),(5,36000)]:eq(16,s.diff(s.pi*(60*t)**2,t).subs(t,at),val*s.pi,'ripple area rate')
for at,val in[(1,8),(2,16),(3,24)]:eq(17,s.diff(4*s.pi*r*r,r).subs(r,at),val*s.pi,'sphere surface-area rate')
for b,val in[(8,172*s.pi),(6,s.Rational(364,3)*s.pi),(s.Rational(51,10),s.Rational(7651,75)*s.pi)]:eq(18,s.Rational(4,3)*s.pi*(b**3-125)/(b-5),val,'sphere average volume rate')
eq(18,s.diff(s.Rational(4,3)*s.pi*r**3,r).subs(r,5),100*s.pi,'sphere instantaneous volume rate')
for at,val in[(1,6),(2,12),(3,18)]:eq(19,s.diff(3*x*x,x).subs(x,at),val,'rod density')
for at,val in[(5,s.Rational(875,4)),(10,s.Rational(375,2)),(20,125),(40,0)]:eq(20,-s.diff(5000*(1-t/40)**2,t).subs(t,at),val,'tank positive outflow')
I=s.diff(t**3-2*t*t+6*t+2,t);eq(21,I.subs(t,s.Rational(1,2)),s.Rational(19,4),'current at half-second');eq(21,I.subs(t,1),5,'current at one second');eq(21,s.diff(I,t).subs(t,s.Rational(2,3)),0,'current minimum time');eq(22,-2*(s.Rational(20000,10000))**3,-16,'inverse-cube force-gradient scaling')
v,c,m0,a=s.symbols('v c m0 a',positive=True);eq(23,s.diff(m0*v/s.sqrt(1-v*v/c**2),v)*a,m0*a/(1-v*v/c**2)**s.Rational(3,2),'relativistic momentum derivative')
D=7+5*s.cos(s.Rational(503,1000)*(t-s.Rational(27,4)));eq(24,s.diff(D,t),-s.Rational(503,200)*s.sin(s.Rational(503,1000)*(t-s.Rational(27,4))),'tidal derivative')
for at in[3,6,9,12]:checks.append({'number':24,'method':'source-time evaluation','time':at,'rate':float(s.diff(D,t).subs(t,at))})
a,k=s.symbols('a k',positive=True);f=a*a*k*t/(a*k*t+1);eq(26,s.diff(f,t),a*a*k/(a*k*t+1)**2,'reaction quotient derivative');eq(26,s.diff(f,t),k*(a-f)**2,'reaction remaining-concentration identity')
mp.mp.dps=50
for n,xx,yy,dg,at,expect in[(27,list(range(0,111,10)),[1650,1750,1860,2070,2300,2560,3040,3710,4450,5280,6080,6870],3,[20,80,85],[14.1598031598,71.7235727236,76.2427757428]),(28,list(range(0,66,5)),['23.0','23.8','24.4','24.5','24.2','24.7','25.2','25.5','25.9','26.3','27.0','28.0','28.8','29.4'],4,[40],[.108979794715])]:
 mat=mp.matrix([[mp.mpf(z)**i for i in range(dg+1)]for z in xx]);vec=mp.matrix([mp.mpf(z)for z in yy]);coeff,resid=mp.qr_solve(mat,vec)
 for z,e in zip(at,expect):
  rate=sum(i*coeff[i]*mp.mpf(z)**(i-1)for i in range(1,dg+1));assert abs(rate-e)<1e-9;checks.append({'number':n,'method':'independent50-digit QR least-squares fit','argument':z,'derivative':str(rate)})
 eq(n,s.Integer(len(xx)),12 if n==27 else 14,'source table row count')
r=s.symbols('r',real=True);v=s.Rational(250000,27)*(s.Rational(1,10000)-r*r)
for at,val in[(0,s.Rational(25,27)),(s.Rational(1,200),s.Rational(25,36)),(s.Rational(1,100),0)]:eq(29,v.subs(r,at),val,'blood-flow speed')
for at,val in[(0,0),(s.Rational(1,200),-s.Rational(2500,27)),(s.Rational(1,100),-s.Rational(5000,27))]:eq(29,s.diff(v,r).subs(r,at),val,'blood-flow gradient')
L,T,rho=s.symbols('L T rho',positive=True);f=s.sqrt(T/rho)/(2*L)
for var,expected in[(L,-f/L),(T,f/(2*T)),(rho,-f/(2*rho))]:eq(30,s.diff(f,var),expected,'string parameter derivative')
for n,F,der,delta in[(31,2000+3*x+x*x/100+x**3/5000,11,s.Rational(55351,5000)),(32,84+s.Rational(16,100)*x-s.Rational(6,10000)*x*x+s.Rational(3,1000000)*x**3,s.Rational(13,100),s.Rational(130303,1000000))]:eq(n,s.diff(F,x).subs(x,100),der,'marginal cost');eq(n,F.subs(x,101)-F.subs(x,100),delta,'exact next-item cost')
R=(40+24*x**s.Rational(2,5))/(1+4*x**s.Rational(2,5));eq(34,s.diff(R,x),-s.Rational(272,5)*x**s.Rational(-3,5)/(1+4*x**s.Rational(2,5))**2,'pupil sensitivity');eq(34,s.limit(R,x,0,dir='+'),40,'darkness limit');eq(35,(s.Rational(1,10)*10-8*s.Rational(15,100))/(10*s.Rational(821,10000)),-s.Rational(200,821),'gas temperature rate')
for C,W in[(0,0),(500,50)]:eq(37,s.Rational(5,100)*C-s.Rational(1,1000)*C*W,0,'caribou equilibrium');eq(37,-s.Rational(5,100)*W+s.Rational(1,10000)*C*W,0,'wolf equilibrium')
b,c,beta=s.symbols('b c beta',positive=True);f=a+b*(1+c*t)**(-beta);eq(38,s.diff(f,t),-b*c*beta*(1+c*t)**(-beta-1),'retention derivative')
Path(__file__).with_name('s2-7-independent.json').write_text(json.dumps({'section':'2.7','passed':len(checks),'checks':checks},indent=2)+'\n');print(len(checks),'independent checks passed')
