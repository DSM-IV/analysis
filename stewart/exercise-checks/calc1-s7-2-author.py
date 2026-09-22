from calc1_helpers import *
from calc1_plot_helpers import plots
x,y,t,th,ph,u=s.symbols('x y t theta phi u',real=True);Q=s.Rational;pi=s.pi
si=s.sin;co=s.cos;ta=s.tan;se=s.sec;ct=s.cot;cs=s.csc;log=s.log
b=CalcBook('7.2',[536,537,538]);checks=[]
def pg(n):return 536 if n<=20 else 537 if n<=74 else 538
def add(n,st,steps,ans,ck,parts=[]):
 b.add(n,pg(n),('삼각함수 적분','Trigonometric integrals'),st,steps,ans,parts=parts);b.verify(n,*ck);b.save()
def ma(n,eq,steps,ans,ck,parts=[]):add(n,(M(eq)+'계산하거나 증명하라.',M(eq)+'Evaluate or prove.'),fs(*steps),same(M(ans)),ck,parts)
def integ(n,f,F,q,steps,lo=None,hi=None):
 f,F=s.sympify(f),s.sympify(F)
 ff=s.lambdify(q,f,'mpmath');ffF=s.lambdify(q,F,'mpmath')
 for p in ['.21','.43','.67']:
  pt=mp.mpf(p);z=mp.diff(ffF,pt)-ff(pt);assert abs(z)<mp.mpf('1e-24')*max(1,abs(ff(pt))),(n,z)
 I=s.Integral(f,q if lo is None else(q,lo,hi));ans=s.latex(F)+'+C';out=list(steps)+fs('F('+s.latex(q)+')='+s.latex(F))
 if lo is not None:
  val=s.simplify(F.subs(q,hi)-F.subs(q,lo));num=mp.quad(ff,[float(lo),float(hi)]);assert abs(float(val)-float(num))<1e-8*max(1,abs(float(num))),(n,val,num)
  ans=s.latex(val);out+=fs(s.latex(I)+'=F('+s.latex(hi)+')-F('+s.latex(lo)+')='+ans)
 add(n,(M(s.latex(I))+'적분을 구하라.',M(s.latex(I))+'Evaluate the integral.'),out,same(M(ans)),('원시함수의 독립 수치미분을 세 입력에서 원 함수와 비교했다. 정적분은 끝점 차와 별도 수치구적으로 대조했다.','Compared independent numerical differentiation of the primitive with the integrand at three inputs; definite integrals also checked by endpoint subtraction and numerical quadrature.'));checks.append(n);return F
def sub(n,f,q,U,P,lo=None,hi=None,extra=[]):
 G=s.integrate(P,u);assert not G.has(s.Integral);F=G.subs(u,U)
 return integ(n,f,F,q,extra+fs('u='+s.latex(U)+r',\quad du='+s.latex(s.diff(U,q))+r'\,d'+s.latex(q),s.latex(s.Integral(f,q))+'='+s.latex(s.Integral(P,u)),s.latex(s.Integral(P,u))+'='+s.latex(G)),lo,hi)
sub(1,si(x)**3*co(x)**2,x,co(x),-(1-u*u)*u*u)
sub(2,co(y)**6*si(y)**3,y,co(y),-u**6*(1-u*u))
sub(3,co(x)**9*si(x)**5,x,si(x),(1-u*u)**4*u**5,0,pi/2)
sub(4,si(x)**5,x,co(x),-(1-u*u)**2,0,pi/4)
sub(5,si(2*t)**5*co(2*t)**2,t,co(2*t),-(1-u*u)**2*u*u/2)
sub(6,co(t/2)**3*si(t/2)**2,t,si(t/2),2*(1-u*u)*u*u)
for n,f,F,q,step,lo,hi in[(7,co(th)**2,th/2+si(2*th)/4,th,r'\cos^2\theta=(1+\cos2\theta)/2',0,pi/2),(8,si(2*th)**2,th/2-si(4*th)/8,th,r'\sin^2(2\theta)=(1-\cos4\theta)/2',0,pi/4),(9,co(2*t)**4,3*t/8+si(4*t)/8+si(8*t)/64,t,r'\cos^4(2t)=(3+4\cos4t+\cos8t)/8',0,pi),(10,si(t)**2*co(t)**4,t/16+si(2*t)/64-si(4*t)/64-si(6*t)/192,t,r'\sin^2t\cos^4t=(2+\cos2t-2\cos4t-\cos6t)/32',0,pi),(11,si(x)**2*co(x)**2,x/8-si(4*x)/32,x,r'\sin^2x\cos^2x=(1-\cos4x)/8',0,pi/2),(12,(2-si(th))**2,Q(9,2)*th+4*co(th)-si(2*th)/4,th,r'(2-\sin\theta)^2=9/2-4\sin\theta-\cos2\theta/2',0,pi/2)]:integ(n,f,F,q,fs(step),lo,hi)
sub(13,s.sqrt(co(th))*si(th)**3,th,co(th),-u**Q(1,2)*(1-u*u))
# Real cube root: powers with even numerator are absolute-value powers.
f14=(1+s.real_root(si(t),3))*co(t)**3;F14=si(t)-si(t)**3/3+Q(3,4)*s.Abs(si(t))**Q(4,3)-Q(3,10)*s.Abs(si(t))**Q(10,3)
integ(14,f14,F14,t,fs(r'u=\sin t,\quad\cos^3t\,dt=(1-u^2)du',r'\int(1+\sqrt[3]u)(1-u^2)du=u-u^3/3+3|u|^{4/3}/4-3|u|^{10/3}/10'))
sub(15,si(x)*se(x)**5,x,co(x),-u**-5)
sub(16,cs(th)**5*co(th)**3,th,si(th),(1-u*u)/u**5)
sub(17,ct(x)*co(x)**2,x,si(x),(1-u*u)/u)
# Fix the logarithm to cover each component of sin(x) != 0.
integ(17,ct(x)*co(x)**2,log(s.Abs(si(x)))-si(x)**2/2,x,fs(r'u=\sin x,\quad\cos^2x=1-u^2',r'\int(1/u-u)du=\ln|u|-u^2/2'))
sub(18,ta(x)**2*co(x)**3,x,si(x),u*u)
sub(19,si(x)**2*si(2*x),x,si(x),2*u**3)
integ(20,si(x)*co(x/2),-co(3*x/2)/3-co(x/2),x,fs(r'\sin x\cos(x/2)=[\sin(3x/2)+\sin(x/2)]/2'))
sub(21,ta(x)*se(x)**3,x,se(x),u*u)
sub(22,ta(th)**2*se(th)**4,th,ta(th),u*u*(1+u*u))
integ(23,ta(x)**2,ta(x)-x,x,fs(r'\tan^2x=\sec^2x-1'))
sub(24,ta(x)**2+ta(x)**4,x,ta(x),u*u)
sub(25,ta(x)**4*se(x)**6,x,ta(x),u**4*(1+u*u)**2)
sub(26,se(th)**6*ta(th)**6,th,ta(th),u**6*(1+u*u)**2,0,pi/4)
sub(27,ta(x)**3*se(x),x,se(x),u*u-1)
sub(28,ta(x)**5*se(x)**3,x,se(x),(u*u-1)**2*u*u)
sub(29,ta(x)**3*se(x)**6,x,se(x),(u*u-1)*u**5)
integ(30,ta(t)**4,ta(t)**3/3-ta(t)+t,t,fs(r'\tan^4t=\tan^2t(\sec^2t-1)',r'\int\tan^4t\,dt=\tan^3t/3-\int(\sec^2t-1)dt'),0,pi/4)
integ(31,ta(x)**5,ta(x)**4/4-ta(x)**2/2-log(s.Abs(co(x))),x,fs(r'\tan^5x=\tan^3x(\sec^2x-1)',r'\int\tan^3x\,dx=\tan^2x/2+\ln|\cos x|'))
integ(32,ta(x)**2*se(x),(se(x)*ta(x)-log(s.Abs(se(x)+ta(x))))/2,x,fs(r'\tan^2x\sec x=\sec^3x-\sec x',r'\int\sec^3x\,dx=[\sec x\tan x+\ln|\sec x+\tan x|]/2'))
integ(33,(1-ta(x)**2)/se(x)**2,si(2*x)/2,x,fs(r'(1-\tan^2x)/\sec^2x=\cos^2x-\sin^2x=\cos2x'))
sub(34,ta(x)*se(x)**2/co(x),x,se(x),u*u)
integ(35,si(x)**3/co(x),-log(s.Abs(co(x)))+co(x)**2/2,x,fs(r'u=\cos x,\quad\sin^3x\,dx=-(1-u^2)du',r'\int(-1/u+u)du=-\ln|u|+u^2/2'),0,pi/4)
sub(36,(si(th)+ta(th))/co(th)**3,th,co(th),-u**-3-u**-4)
integ(37,ct(x)**2,-ct(x)-x,x,fs(r'\cot^2x=\csc^2x-1'),pi/6,pi/2)
integ(38,ct(x)**3,-ct(x)**2/2-log(s.Abs(si(x))),x,fs(r'\cot^3x=\cot x(\csc^2x-1)',r'\int\cot x\csc^2x\,dx=-\cot^2x/2'),pi/4,pi/2)
sub(39,ct(ph)**5*cs(ph)**3,ph,cs(ph),-(u*u-1)**2*u*u,pi/4,pi/2)
sub(40,cs(th)**4*ct(th)**4,th,ct(th),-(1+u*u)*u**4,pi/4,pi/2)
integ(41,cs(x),log(s.Abs(cs(x)-ct(x))),x,fs(r'\csc x=\frac{\csc x(\csc x-\cot x)}{\csc x-\cot x}',r'u=\csc x-\cot x,\quad du=\csc x(\csc x-\cot x)dx'))
integ(42,cs(x)**3,(-cs(x)*ct(x)+log(s.Abs(cs(x)-ct(x))))/2,x,fs(r'I=\int\csc x\csc^2x\,dx=-\csc x\cot x-\int\csc x\cot^2x\,dx',r'2I=-\csc x\cot x+\int\csc x\,dx'),pi/6,pi/3)
integ(43,si(8*x)*co(5*x),-co(3*x)/6-co(13*x)/26,x,fs(r'\sin8x\cos5x=(\sin3x+\sin13x)/2'))
integ(44,si(2*th)*si(6*th),si(4*th)/8-si(8*th)/16,th,fs(r'\sin2\theta\sin6\theta=(\cos4\theta-\cos8\theta)/2'))
integ(45,co(5*t)*co(10*t),si(5*t)/10+si(15*t)/30,t,fs(r'\cos5t\cos10t=(\cos5t+\cos15t)/2'),0,pi/2)
sub(46,t*co(t*t)**5,t,si(t*t),(1-u*u)**2/2)
integ(47,si(1/t)**2/t**2,-1/(2*t)+si(2/t)/4,t,fs(r'u=1/t,\quad du=-dt/t^2',r'-\int\sin^2u\,du=-u/2+\sin2u/4'))
sub(48,se(y)**2*co(ta(y))**3,y,si(ta(y)),1-u*u)
integ(49,s.sqrt(1+co(2*x)),s.sqrt(2)*si(x),x,fs(r'\sqrt{1+\cos2x}=\sqrt2|\cos x|=\sqrt2\cos x\quad(0\le x\le\pi/6)'),0,pi/6)
integ(50,s.sqrt(1-co(4*th)),-co(2*th)/s.sqrt(2),th,fs(r'\sqrt{1-\cos4\theta}=\sqrt2|\sin2\theta|=\sqrt2\sin2\theta\quad(0\le\theta\le\pi/4)'),0,pi/4)
integ(51,t*si(t)**2,t*t/4-t*si(2*t)/4-co(2*t)/8,t,fs(r'\int t\sin^2t\,dt=t^2/4-\tfrac12\int t\cos2t\,dt',r'\int t\cos2t\,dt=t\sin2t/2+\cos2t/4'))
integ(52,x*se(x)*ta(x),x*se(x)-log(s.Abs(se(x)+ta(x))),x,fs(r'u=x,\ dv=\sec x\tan xdx\Rightarrow\int u\,dv=x\sec x-\int\sec xdx'))
integ(53,x*ta(x)**2,x*ta(x)+log(s.Abs(co(x)))-x*x/2,x,fs(r'\int x\tan^2x\,dx=\int x\sec^2x\,dx-x^2/2',r'\int x\sec^2x\,dx=x\tan x-\int\tan xdx=x\tan x+\ln|\cos x|'))
integ(54,x*si(x)**3,-Q(3,4)*x*co(x)+Q(3,4)*si(x)+x*co(3*x)/12-si(3*x)/36,x,fs(r'\sin^3x=(3\sin x-\sin3x)/4',r'\int x\sin(kx)dx=-x\cos(kx)/k+\sin(kx)/k^2'))
integ(55,1/(co(x)-1),ct(x/2),x,fs(r'\cos x-1=-2\sin^2(x/2)',r'\int dx/(\cos x-1)=-\tfrac12\int\csc^2(x/2)dx'))
integ(56,1/(se(th)+1),th-ta(th/2),th,fs(r'1/(\sec\theta+1)=\cos\theta/(1+\cos\theta)=1-\tfrac12\sec^2(\theta/2)'))
for n,f,F,steps,win in[(57,x*si(x*x)**2,x*x/4-si(2*x*x)/8,fs(r'u=x^2,\quad xdx=du/2',r'\tfrac12\int\sin^2u\,du=u/4-\sin2u/8'),(-3,3,-3,3)),(58,si(x)**5*co(x)**3,si(x)**6/6-si(x)**8/8,fs(r'u=\sin x,\quad\cos^3x\,dx=(1-u^2)du',r'\int u^5(1-u^2)du=u^6/6-u^8/8'),(-pi,pi,-.3,.3)),(59,si(3*x)*si(6*x),si(3*x)/6-si(9*x)/18,fs(r'\sin3x\sin6x=(\cos3x-\cos9x)/2'),(-pi,pi,-1.2,1.2)),(60,se(x/2)**4,2*ta(x/2)+Q(2,3)*ta(x/2)**3,fs(r'u=\tan(x/2),\quad\sec^2(x/2)dx=2du',r'2\int(1+u^2)du=2u+2u^3/3'),(-2,2,-15,15))]:
 integ(n,f,F,x,steps)
 for lang,txt in [('ko','C=0으로 두고 피적분함수와 원시함수를 함께 그려 기울기를 비교하라.'),('en','Set C=0 and graph the integrand and primitive together to compare their slopes.')]:b.E[n]['statement'][lang]+=txt
 plots(b,n,[('Integrand f and primitive F (C=0)',*map(float,win),[('f',s.lambdify(x,f,'math')),('F',s.lambdify(x,F,'math'))])])
b.save();print('7.2 authored',len(b.E))
ma(61,r'I=\int_0^{\pi/4}\tan^6x\sec xdx,\quad J=\int_0^{\pi/4}\tan^8x\sec xdx',[r'\frac d{dx}(\tan^7x\sec x)=7\tan^6x\sec^3x+\tan^8x\sec x',r'=7\tan^6x\sec x+8\tan^8x\sec x',r'\sqrt2=[\tan^7x\sec x]_0^{\pi/4}=7I+8J'],r'J=(\sqrt2-7I)/8',('원래 두 적분을 직접 수치구적으로 계산해 선형관계를 확인했다.','Direct numerical quadrature of both original integrals verifies the linear relation.'))
ma(62,r'(a)T_{2n}=\int\tan^{2n}x\,dx\ \text{recurrence};\quad(b)T_8',[r'\tan^{2n}x=\tan^{2n-2}x(\sec^2x-1)',r'T_{2n}=\frac{\tan^{2n-1}x}{2n-1}-T_{2n-2}',r'T_2=\tan x-x,\quad T_8=\tan^7x/7-\tan^5x/5+\tan^3x/3-\tan x+x'],r'(a)T_{2n}=\tan^{2n-1}x/(2n-1)-T_{2n-2};\quad(b)\tan^7x/7-\tan^5x/5+\tan^3x/3-\tan x+x+C',('n=1 초기값을 고정하고 최종식을 미분하여 tan⁸x를 확인했다.','Fixed the n=1 base case and differentiated the final expression to recover tan⁸x.'),['a','b'])
ma(63,r'f(x)=\sin^2x\cos^3x,\quad[-\pi,\pi]\quad\text{average value}',[r'\bar f=\frac1{2\pi}\int_{-\pi}^{\pi}\sin^2x\cos^3x\,dx',r'u=\sin x:\quad F(x)=\sin^3x/3-\sin^5x/5',r'F(\pi)-F(-\pi)=0'],r'0',('함수는 짝함수지만 평균0이다. 양·음 부분의 상쇄를 끝점 계산과 수치구적으로 확인했다.','The function is even but has mean zero; endpoint evaluation and numerical quadrature confirm cancellation.'))
add(64,('∫sinx cosx dx를(a)u=cosx,(b)u=sinx,(c)배각공식,(d)부분적분으로 구하고 답의 모양이 다른 이유를 설명하라.','Evaluate ∫sinx cosx dx using(a)u=cosx,(b)u=sinx,(c)the double-angle identity and(d)integration by parts; explain the differing forms.'),fs(r'(a)du=-\sin xdx\Rightarrow-\int udu=-\cos^2x/2+C',r'(b)du=\cos xdx\Rightarrow\int udu=\sin^2x/2+C',r'(c)\sin x\cos x=\sin2x/2\Rightarrow-\cos2x/4+C',r'(d)u=\sin x,\ dv=\cos xdx:\quad I=\sin^2x-I\Rightarrow I=\sin^2x/2+C')+[('sin²x+cos²x=1과 cos2x=1−2sin²x에 의해 답 사이의 차는 상수이며 적분상수에 흡수된다.','By sin²x+cos²x=1 and cos2x=1−2sin²x, the answers differ only by constants absorbed into C.')],same(M(r'(a)-\cos^2x/2+C;\quad(b),(d)\sin^2x/2+C;\quad(c)-\cos2x/4+C')),('네 식의 미분이 모두 sinx cosx이고 식 사이의 차가 상수임을 확인했다.','All four derivatives equal sinx cosx and the expressions differ by constants.'),list('abcd'))
area(b,65,537,('0≤x≤π에서 y=sin²x와 y=sin³x 사이 넓이를 구하라.','Find the area between y=sin²x and y=sin³x on0≤x≤π.'),[(0,pi,si(x)**2,si(x)**3)],x,extra=fs(r'0\le\sin x\le1\Rightarrow\sin^2x\ge\sin^3x'));b.save()
area(b,66,537,('0≤x≤π/4에서 y=tanx와 y=tan²x 사이 넓이를 구하라.','Find the area between y=tanx and y=tan²x on0≤x≤π/4.'),[(0,pi/4,ta(x),ta(x)**2)],x,extra=fs(r'0\le\tan x\le1\Rightarrow\tan x\ge\tan^2x'));b.save()
for n,f,hi,F,identity in[(67,co(x)**3,2*pi,si(x)-si(x)**3/3,r'\cos^3x=(3\cos x+\cos3x)/4'),(68,si(2*pi*x)*co(5*pi*x),s.S(2),co(3*pi*x)/(6*pi)-co(7*pi*x)/(14*pi),r'\sin2\pi x\cos5\pi x=[\sin7\pi x-\sin3\pi x]/2')]:
 integ(n,f,F,x,fs(identity),0,hi)
 for lang,txt in [('ko','먼저 그래프의 양·음 넓이로 값을 추측하고 위 항등식으로 증명하라.'),('en','First guess from positive and negative graph areas, then prove the value using the identity above.')]:b.E[n]['statement'][lang]+=txt
 plots(b,n,[('Signed area cancels over the interval',0,float(hi),-1.2,1.2,[('integrand',s.lambdify(x,f,'math'))])])
for n,up,dn,axis,lo,hi in[(69,si(x),s.S(0),'x',pi/2,pi),(70,si(x)**2,s.S(0),'x',s.S(0),pi),(71,co(x),si(x),'1',s.S(0),pi/4),(72,se(x),co(x),'-1',s.S(0),pi/3)]:
 if axis=='x':outer,inner=up,dn
 elif axis=='1':outer,inner=1-dn,1-up
 else:outer,inner=up+1,dn+1
 f=s.trigsimp(outer**2-inner**2);val=s.simplify(pi*s.integrate(f,(x,lo,hi)));num=mp.pi*mp.quad(s.lambdify(x,f,'mpmath'),[float(lo),float(hi)]);assert abs(float(val)-float(num))<1e-8
 add(n,(M('y='+s.latex(up)+r',\quad y='+s.latex(dn)+r',\quad '+s.latex(lo)+r'\le x\le'+s.latex(hi))+(('x축'if axis=='x'else'y='+axis)+' 둘레로 회전한 부피를 구하라.'),M('y='+s.latex(up)+r',\quad y='+s.latex(dn)+r',\quad '+s.latex(lo)+r'\le x\le'+s.latex(hi))+'Find volume of revolution about '+('the x-axis.'if axis=='x'else'y='+axis+'.')),fs('R='+s.latex(outer)+r',\quad r='+s.latex(inner),r'V=\pi'+s.latex(s.Integral(f,(x,lo,hi))),r'V='+s.latex(val)),same(M('V='+s.latex(val))),('회전축 위치에 따라 바깥·안 반지름을 정하고, 제곱 차의 양수 조건 및 수치적분을 확인했다.','Chose outer/inner radii from the axis location, checked their nonnegative squared difference, and cross-checked numerical integration.'))
 area_svg(b,n,[(lo,hi,up,dn)],x,f'7.2.{n} Region before rotation');b.save()
ma(73,r'v(t)=\sin(\omega t)\cos^2(\omega t),\quad f(0)=0',[r'u=\cos(\omega t),\quad du=-\omega\sin(\omega t)dt',r'f(t)=-\cos^3(\omega t)/(3\omega)+C',r'f(0)=0\Rightarrow C=1/(3\omega)'],r'f(t)=\frac{1-\cos^3(\omega t)}{3\omega}\ (\omega\ne0);\quad f(t)=0\ (\omega=0)',('미분하여 속도를 회복하고 초기위치0을 확인했다. 각진동수가0이면 속도 자체가0이다.','Differentiation recovers velocity and the initial position is zero; at zero angular frequency the velocity itself vanishes.'))
add(74,('교류 전압 E(t)=155sin(120πt)V이다.(a)한 주기 동안 제곱의 평균에 제곱근을 취해 RMS 전압을 구하라.(b)RMS가220V인 A sin(120πt)의 진폭 A를 구하라.','For alternating voltage E(t)=155sin(120πt)V,(a)find RMS voltage by taking the square root of the mean square over one period.(b)Find the amplitude A of A sin(120πt) with RMS220V.'),fs(r'T=1/60,\quad E_{\rm RMS}=\sqrt{\frac1T\int_0^TA^2\sin^2(120\pi t)dt}',r'\frac1T\int_0^T\sin^2(120\pi t)dt=1/2\Rightarrow E_{\rm RMS}=|A|/\sqrt2',r'(a)155/\sqrt2\approx109.6016;\quad(b)A=220\sqrt2\approx311.1270'),same(M(r'(a)155/\sqrt2\approx109.60\mathrm V;\quad(b)220\sqrt2\approx311.13\mathrm V')),('제곱근을 평균보다 먼저 취하지 않았고, 진폭과 RMS의 비가√2임을 확인했다.','Took the mean before the square root and verified the amplitude-to-RMS ratio√2.'),['a','b'])
ma(75,r'\int_{-\pi}^{\pi}\sin(mx)\cos(nx)dx,\quad m,n\in\mathbb N',[r'h(-x)=\sin(-mx)\cos(-nx)=-h(x)',r'\int_{-\pi}^\pi h(x)dx=\int_0^\pi[h(x)+h(-x)]dx=0'],r'0',('양의 정수 조건보다 강하게 모든 실수 m,n에 대해 홀짝성 증명이 성립한다.','The parity proof actually holds for all real m,n, hence for the specified positive integers.'))
for n,typ,sign in[(76,'sin','-'),(77,'cos','+')]:
 ma(n,fr'\int_{{-\pi}}^\pi\{typ}(mx)\{typ}(nx)dx,\quad m,n\in\mathbb N',[fr'\{typ}(mx)\{typ}(nx)=[\cos((m-n)x){sign}\cos((m+n)x)]/2',r'\int_{-\pi}^{\pi}\cos(kx)dx=[\sin(kx)/k]_{-\pi}^\pi=0\quad(k\in\mathbb Z\setminus\{0\})',r'm\ne n:\quad m-n,m+n\ne0\Rightarrow I=0',r'm=n:\quad I=\tfrac12\int_{-\pi}^{\pi}1dx=\pi'],r'\begin{cases}0&m\ne n,\\\pi&m=n.\end{cases}',('m=n에서는0으로 나누지 않고 상수 주파수 항을 별도로 적분했다.','Handled m=n separately by integrating the constant-frequency term instead of dividing by zero.'))
ma(78,r'f(x)=\sum_{n=1}^Na_n\sin(nx),\quad 1\le m\le N',[r'\int_{-\pi}^{\pi}f(x)\sin(mx)dx=\sum_{n=1}^Na_n\int_{-\pi}^{\pi}\sin(nx)\sin(mx)dx',r'\int_{-\pi}^{\pi}\sin(nx)\sin(mx)dx=\pi\delta_{nm}',r'\int_{-\pi}^{\pi}f(x)\sin(mx)dx=\pi a_m'],r'a_m=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin(mx)dx',('합이 유한하므로 항별 적분은 바로 가능하고 직교성으로 m번째 항만 남는다.','The finite sum can be integrated termwise; orthogonality leaves only the mth term.'))
# Keep the real cube root legible and preserve the original domain.
b.E[14]['statement']=pair(M(r'\int(1+\sqrt[3]{\sin t})\cos^3t\,dt')+'실수 세제곱근으로 적분하라.',M(r'\int(1+\sqrt[3]{\sin t})\cos^3t\,dt')+'Integrate using the real cube root.')
b.save();print('7.2 COMPLETE',len(b.E))
