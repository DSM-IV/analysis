from calc1_helpers import *
from calc1_plot_helpers import plots
x,t,y,z,w,th,Rr,Mm,r,ss=s.symbols('x t y z w theta R M r s',real=True)
a,beta=s.symbols('a beta',nonzero=True,real=True);Q=s.Rational;pi=s.pi
b=CalcBook('7.1',[528,529,530]);checks=[]
def pg(n):return 528 if n<=24 else 529 if n<=70 else 530
def add(n,st,steps,ans,ck,parts=[]):
 b.add(n,pg(n),('부분적분','Integration by parts'),st,steps,ans,parts=parts);b.verify(n,*ck);b.save()
def ma(n,eq,steps,ans,ck,parts=[]):add(n,(M(eq)+'계산하거나 증명하라.',M(eq)+'Evaluate or prove.'),fs(*steps),same(M(ans)),ck,parts)
def ib(n,f,u,v,q=x,lo=None,hi=None,F=None,extra=[]):
 f,u,v=map(s.sympify,[f,u,v]);dv=s.diff(v,q);du=s.diff(u,q)
 assert s.simplify(f-u*dv)==0,(n,'decomposition')
 if F is None:F=s.integrate(f,q)
 assert not F.has(s.Integral),(n,F)
 err=s.trigsimp(s.simplify(s.diff(F,q)-f))
 if err!=0:
  for pt in [.31,.63]:assert abs(complex(err.subs({q:pt,a:1.3,beta:1.4}).evalf()))<1e-8,(n,err)
 steps=list(extra)+fs('u='+s.latex(u)+r',\quad dv='+s.latex(dv)+r'\,d'+s.latex(q),'du='+s.latex(du)+r'\,d'+s.latex(q)+r',\quad v='+s.latex(v),r'\int u\,dv=uv-\int v\,du='+s.latex(u*v)+'-'+s.latex(s.Integral(v*du,q)),r'F('+s.latex(q)+')='+s.latex(F))
 if lo is None: I=s.Integral(f,q);ans=s.latex(F)+'+C'
 else:
  I=s.Integral(f,(q,lo,hi));val=s.simplify(F.subs(q,hi)-F.subs(q,lo));ans=s.latex(val);steps+=fs(s.latex(I)+'=F('+s.latex(hi)+')-F('+s.latex(lo)+')='+ans)
  if not (f.free_symbols-{q}):
   num=mp.quad(s.lambdify(q,f,'mpmath'),[float(lo),float(hi)]);assert abs(float(num)-float(val.evalf()))<1e-7*max(1,abs(float(num))),(n,num,val)
 if n in [1,2,3,4]:prompt=('지정된 u,dv로 부분적분하라.','Use the specified u and dv:')
 else:prompt=('부분적분하여 적분을 구하라.','Evaluate using integration by parts.')
 st=(M(s.latex(I))+prompt[0],M(s.latex(I))+prompt[1])
 if n<=4:st=tuple(vv+M('u='+s.latex(u)+r',\quad dv='+s.latex(dv)+r'\,d'+s.latex(q))for vv in st)
 if n in [12,18]:steps.append(('매개변수가0이면 원래 피적분함수로 돌아가 별도로 계산한다.','For a zero parameter, return to the original integrand and integrate separately.'));ans+=r';\quad '+('\\beta=0: C'if n==12 else'a=0: x^2/2+C')
 add(n,st,steps,same(M(ans)),('원시함수를 미분해 피적분함수를 회복하고 정적분은 끝점 차와 독립 수치구적으로 검산했다.','Differentiated the primitive to recover the integrand; definite integrals also checked by endpoint subtraction and independent quadrature.'))
 checks.append(n);return F
rows=[(1,x*s.exp(2*x),x,s.exp(2*x)/2,x),(2,s.sqrt(x)*s.log(x),s.log(x),Q(2,3)*x**Q(3,2),x),(3,x*s.cos(4*x),x,s.sin(4*x)/4,x),(4,s.asin(x),s.asin(x),x,x),(5,t*s.exp(2*t),t,s.exp(2*t)/2,t),(6,y*s.exp(-y),y,-s.exp(-y),y),(7,x*s.sin(10*x),x,-s.cos(10*x)/10,x),(8,(pi-x)*s.cos(pi*x),pi-x,s.sin(pi*x)/pi,x),(9,w*s.log(w),s.log(w),w*w/2,w),(10,s.log(x)/x**2,s.log(x),-1/x,x),(11,(x*x+2*x)*s.cos(x),x*x+2*x,s.sin(x),x),(12,t*t*s.sin(beta*t),t*t,-s.cos(beta*t)/beta,t),(13,s.acos(x),s.acos(x),x,x),(14,s.log(s.sqrt(x)),s.log(s.sqrt(x)),x,x),(15,t**4*s.log(t),s.log(t),t**5/5,t),(16,s.atan(2*y),s.atan(2*y),y,y),(17,t/s.sin(t)**2,t,-s.cot(t),t),(18,x*s.cosh(a*x),x,s.sinh(a*x)/a,x),(19,s.log(x)**2,s.log(x)**2,x,x),(20,z/10**z,z,-10**(-z)/s.log(10),z),(21,s.exp(3*x)*s.cos(x),s.cos(x),s.exp(3*x)/3,x),(22,s.exp(x)*s.sin(pi*x),s.sin(pi*x),s.exp(x),x),(23,s.exp(2*th)*s.sin(3*th),s.sin(3*th),s.exp(2*th)/2,th),(24,s.exp(-th)*s.cos(2*th),s.cos(2*th),-s.exp(-th),th),(25,z**3*s.exp(z),z**3,s.exp(z),z),(26,s.asin(x)**2,s.asin(x)**2,x,x),(27,(1+x*x)*s.exp(3*x),1+x*x,s.exp(3*x)/3,x)]
for n,f,u,v,q in rows:
 F=None
 if n==2:F=Q(2,3)*x**Q(3,2)*s.log(x)-Q(4,9)*x**Q(3,2)
 if n==17:F=-t*s.cot(t)+s.log(s.Abs(s.sin(t)))
 if n==26:F=x*s.asin(x)**2+2*s.asin(x)*s.sqrt(1-x*x)-2*x
 ib(n,f,u,v,q,F=F)
for n,f,u,v,q,lo,hi in[(28,th*s.sin(3*pi*th),th,-s.cos(3*pi*th)/(3*pi),th,0,Q(1,2)),(29,x*3**x,x,3**x/s.log(3),x,0,1),(30,x*s.exp(x)/(1+x)**2,x*s.exp(x),-1/(1+x),x,0,1),(31,y*s.sinh(y),y,s.cosh(y),y,0,2),(32,w*w*s.log(w),s.log(w),w**3/3,w,1,2),(33,s.log(Rr)/Rr**2,s.log(Rr),-1/Rr,Rr,1,5),(34,t*t*s.sin(2*t),t*t,-s.cos(2*t)/2,t,0,2*pi),(35,x*s.sin(x)*s.cos(x),x,-s.cos(2*x)/4,x,0,pi),(36,s.atan(1/x),s.atan(1/x),x,x,1,s.sqrt(3)),(37,Mm*s.exp(-Mm),Mm,-s.exp(-Mm),Mm,1,5),(38,s.log(x)**2/x**3,s.log(x)**2,-1/(2*x*x),x,1,2),(39,s.sin(x)*s.log(s.cos(x)),s.log(s.cos(x)),-s.cos(x),x,0,pi/3),(40,r**3/s.sqrt(4+r*r),r*r,s.sqrt(4+r*r),r,0,1),(41,s.cos(x)*s.sinh(x),s.cos(x),s.cosh(x),x,0,pi),(42,s.exp(ss)*s.sin(t-ss),s.sin(t-ss),s.exp(ss),ss,0,t)]:
 ib(n,f,u,v,q,s.sympify(lo),s.sympify(hi),F=(s.exp(x)/(1+x)if n==30 else None))
# Substitution exercises: display the transformed integral and a worked parts step.
subs=[(43,s.exp(s.sqrt(x)),r'u=\sqrt x,\ dx=2u\,du',r'2\int ue^u du=2e^u(u-1)',2*s.exp(s.sqrt(x))*(s.sqrt(x)-1),x,None,None),(44,s.cos(s.log(x)),r'u=\ln x,\ dx=e^u du',r'J=\int e^u\cos u\,du=e^u\cos u+\int e^u\sin u\,du=e^u(\cos u+\sin u)-J',x*(s.cos(s.log(x))+s.sin(s.log(x)))/2,x,None,None),(45,th**3*s.cos(th*th),r'u=\theta^2,\ \theta^3d\theta=u\,du/2',r'\tfrac12\int u\cos u\,du=\tfrac12(u\sin u+\cos u)',(th*th*s.sin(th*th)+s.cos(th*th))/2,th,s.sqrt(pi/2),s.sqrt(pi)),(46,s.exp(s.cos(t))*s.sin(2*t),r'u=\cos t,\ \sin2t\,dt=-2u\,du',r'-2\int ue^u du=-2e^u(u-1)',-2*s.exp(s.cos(t))*(s.cos(t)-1),t,0,pi),(47,x*s.log(1+x),r'u=1+x,\ x=u-1',r'\int(u-1)\ln u\,du=(u^2/2-u)\ln u-u^2/4+u',((x*x-1)/2)*s.log(1+x)-(1+x)**2/4+1+x,x,None,None),(48,s.asin(s.log(x))/x,r'u=\ln x,\ du=dx/x',r'\int\arcsin u\,du=u\arcsin u+\sqrt{1-u^2}',s.log(x)*s.asin(s.log(x))+s.sqrt(1-s.log(x)**2),x,None,None)]
for n,f,sub,step,F,q,lo,hi in subs:
 assert s.trigsimp(s.simplify(s.diff(F,q)-f))==0
 I=s.Integral(f,q if lo is None else(q,lo,hi));val=F if lo is None else s.simplify(F.subs(q,hi)-F.subs(q,lo))
 add(n,(M(s.latex(I))+'먼저 치환한 뒤 부분적분하라.',M(s.latex(I))+'Substitute first, then integrate by parts.'),fs(sub,step,s.latex(F))+([]if lo is None else fs('F('+s.latex(hi)+')-F('+s.latex(lo)+')='+s.latex(val))),same(M(s.latex(val)+('+C'if lo is None else''))),('치환 후 미분인자와 적분 경계를 보존했고, 원시함수를 원 변수로 미분하여 확인했다.','Preserved the differential and endpoint changes; differentiated the primitive in the original variable.'));checks.append(n)
for n,f,u,v,win in[(49,x*s.exp(-2*x),x,-s.exp(-2*x)/2,(-1,3,-8,3)),(50,x**Q(3,2)*s.log(x),s.log(x),Q(2,5)*x**Q(5,2),(.05,3,-1,8)),(51,x**3*s.sqrt(1+x*x),x*x,(1+x*x)**Q(3,2)/3,(-2,2,-15,15)),(52,x*x*s.sin(2*x),x*x,-s.cos(2*x)/2,(-4,4,-16,16))]:
 F=ib(n,f,u,v)
 for lang,txt in [('ko','적분상수 C=0으로 두고 피적분함수와 원시함수를 함께 그려 기울기의 부호를 비교하라.'),('en','Set C=0 and graph the integrand and primitive together, comparing the signs of the slopes.')]:b.E[n]['statement'][lang]+=txt
 plots(b,n,[('Integrand f and primitive F (C=0)',*win,[('f',s.lambdify(x,f,'math')),('F',s.lambdify(x,F,'math'))])]);b.save()
print('7.1 authored',len(b.E))
proofcheck=('각 부분적분의 경계항과 재귀식의 초기값을 확인하고, 얻은 식을 미분하거나 낮은 차수에 대입해 검산했다.','Checked boundary terms and recurrence base cases, then differentiated the result or substituted low powers.')
ma(53,r'(a)\int\sin^2x\,dx;\quad(b)\int\sin^4x\,dx',[r'I_n=-\cos x\sin^{n-1}x/n+(n-1)I_{n-2}/n',r'I_2=-\sin x\cos x/2+x/2=x/2-\sin2x/4',r'I_4=-\cos x\sin^3x/4+3I_2/4=3x/8-\sin2x/4+\sin4x/32'],r'(a)x/2-\sin2x/4+C;\quad(b)3x/8-\sin2x/4+\sin4x/32+C',proofcheck,['a','b'])
ma(54,r'J_n=\int\cos^nx\,dx:\ (a)\text{recurrence};\ (b)J_2;\ (c)J_4',[r'u=\cos^{n-1}x,\ dv=\cos x\,dx',r'J_n=\cos^{n-1}x\sin x+(n-1)\int\cos^{n-2}x\sin^2x\,dx',r'nJ_n=\cos^{n-1}x\sin x+(n-1)J_{n-2}',r'J_2=x/2+\sin2x/4,\quad J_4=3x/8+\sin2x/4+\sin4x/32'],r'(a)J_n=\cos^{n-1}x\sin x/n+(n-1)J_{n-2}/n;\quad(b)x/2+\sin2x/4+C;\quad(c)3x/8+\sin2x/4+\sin4x/32+C',proofcheck,list('abc'))
ma(55,r'I_n=\int_0^{\pi/2}\sin^nx\,dx:\ (a)\text{recurrence};\ (b)I_3,I_5;\ (c)I_{2n+1}',[r'[-\cos x\sin^{n-1}x/n]_0^{\pi/2}=0\quad(n\ge2)',r'I_n=(n-1)I_{n-2}/n,\quad I_1=1',r'I_3=(2/3)I_1=2/3,\quad I_5=(4/5)(2/3)=8/15',r'I_{2n+1}=\prod_{k=1}^n\frac{2k}{2k+1}'],r'(a)I_n=\frac{n-1}{n}I_{n-2};\quad(b)2/3,8/15;\quad(c)\frac{2\cdot4\cdots2n}{3\cdot5\cdots(2n+1)}',proofcheck,list('abc'))
ma(56,r'I_{2n}=\int_0^{\pi/2}\sin^{2n}x\,dx',[r'I_{2n}=\frac{2n-1}{2n}I_{2n-2},\quad I_0=\pi/2',r'I_{2n}=\left(\prod_{k=1}^n\frac{2k-1}{2k}\right)I_0'],r'I_{2n}=\frac{1\cdot3\cdots(2n-1)}{2\cdot4\cdots2n}\frac\pi2',proofcheck)
for n,eq,steps,ans in[(57,r'L_n=\int(\ln x)^n dx',[r'u=(\ln x)^n,\ dv=dx,\ du=n(\ln x)^{n-1}dx/x,\ v=x',r'L_n=x(\ln x)^n-n\int(\ln x)^{n-1}dx'],r'L_n=x(\ln x)^n-nL_{n-1}'),(58,r'E_n=\int x^ne^x dx',[r'u=x^n,\ dv=e^x dx,\ du=nx^{n-1}dx,\ v=e^x',r'E_n=x^ne^x-n\int x^{n-1}e^x dx'],r'E_n=x^ne^x-nE_{n-1}'),(59,r'T_n=\int\tan^nx\,dx,\quad n\ne1',[r'u=\tan^{n-2}x,\ dv=\sec^2x\,dx',r'T_n+T_{n-2}=\int\tan^{n-2}x\sec^2x\,dx=\tan^{n-1}x-(n-2)(T_n+T_{n-2})',r'(n-1)(T_n+T_{n-2})=\tan^{n-1}x'],r'T_n=\frac{\tan^{n-1}x}{n-1}-T_{n-2}'),(60,r'S_n=\int\sec^nx\,dx,\quad n\ne1',[r'u=\sec^{n-2}x,\ dv=\sec^2x\,dx',r'S_n=\sec^{n-2}x\tan x-(n-2)\int\sec^{n-2}x\tan^2x\,dx',r'S_n=\sec^{n-2}x\tan x-(n-2)(S_n-S_{n-2})'],r'S_n=\frac{\tan x\sec^{n-2}x}{n-1}+\frac{n-2}{n-1}S_{n-2}')]:ma(n,eq,steps,ans,proofcheck)
ma(61,r'\int(\ln x)^3dx',[r'L_3=x\ln^3x-3L_2,\quad L_2=x\ln^2x-2L_1',r'L_1=x\ln x-x',r'L_3=x(\ln^3x-3\ln^2x+6\ln x-6)'],r'x(\ln^3x-3\ln^2x+6\ln x-6)+C',proofcheck)
ma(62,r'\int x^4e^xdx',[r'E_4=x^4e^x-4E_3,\quad E_3=x^3e^x-3E_2',r'E_2=x^2e^x-2E_1,\quad E_1=xe^x-e^x',r'E_4=e^x(x^4-4x^3+12x^2-24x+24)'],r'e^x(x^4-4x^3+12x^2-24x+24)+C',proofcheck)
area(b,63,529,('y=x²lnx와 y=4lnx 사이 유계 영역의 넓이를 구하라.','Find the bounded area between y=x²lnx and y=4lnx.'),[(1,2,4*s.log(x),x*x*s.log(x))],x,extra=fs(r'(x^2-4)\ln x=0\Rightarrow x=1,2\quad(x>0)'));b.save()
area(b,64,529,('y=x²e⁻ˣ와 y=xe⁻ˣ 사이 유계 영역의 넓이를 구하라.','Find the bounded area between y=x²e⁻ˣ and y=xe⁻ˣ.'),[(0,1,x*s.exp(-x),x*x*s.exp(-x))],x,extra=fs(r'x(x-1)e^{-x}=0\Rightarrow x=0,1'));b.save()
rl=mp.findroot(lambda q:mp.asin(q/2)-2+q*q,(-1.9,-1.5));rh=mp.findroot(lambda q:mp.asin(q/2)-2+q*q,(1,1.5));rh66=mp.findroot(lambda q:mp.log(q+1)-3+q,2)
for n,lo,hi,up,dn in[(65,rl,rh,2-x*x,s.asin(x/2)),(66,mp.mpf(0),rh66,3*x-x*x,x*s.log(x+1))]:
 area(b,n,529,(M('y='+s.latex(up)+r',\quad y='+s.latex(dn))+'그래프로 교점을 추정하고 둘러싸인 넓이를 수치적으로 구하라.',M('y='+s.latex(up)+r',\quad y='+s.latex(dn))+'Estimate intersections graphically and calculate the bounded area numerically.'),[(s.Float(str(lo),30),s.Float(str(hi),30),up,dn)],x,numeric=True,extra=fs(fr'x_1\approx{float(lo):.9f},\quad x_2\approx{float(hi):.9f}'));b.save()
# Shells: radius and height are explicit; check by direct numerical integration.
for n,rad,h,q,lo,hi,desc in[(67,x,s.cos(pi*x/2),x,0,1,('y=cos(πx/2), y=0, 0≤x≤1을 y축 둘레로 회전','Rotate y=cos(πx/2), y=0, 0≤x≤1 about the y-axis')),(68,x,s.exp(x)-s.exp(-x),x,0,1,('y=eˣ,y=e⁻ˣ,x=1 사이 영역을 y축 둘레로 회전','Rotate the region between y=eˣ,y=e⁻ˣ,x=1 about the y-axis')),(69,1-x,s.exp(-x),x,-1,0,('y=e⁻ˣ,y=0,−1≤x≤0을 x=1 둘레로 회전','Rotate the region under y=e⁻ˣ on−1≤x≤0 about x=1')),(70,y,s.log(y),y,1,3,('y=eˣ,x=0,y=3 사이 영역을 x축 둘레로 회전','Rotate the region between y=eˣ,x=0,y=3 about the x-axis'))]:
 val=s.simplify(2*pi*s.integrate(rad*h,(q,lo,hi)));num=2*mp.pi*mp.quad(s.lambdify(q,rad*h,'mpmath'),[lo,hi]);assert abs(float(val)-float(num))<1e-8
 add(n,(desc[0]+'하여 원통껍질법으로 부피를 구하라.',desc[1]+'; find volume using cylindrical shells.'),fs(r'\rho='+s.latex(rad)+r',\quad h='+s.latex(h),r'V=2\pi'+s.latex(s.Integral(rad*h,(q,lo,hi))),r'\int u\,dv=uv-\int v\,du',r'V='+s.latex(val)),same(M('V='+s.latex(val))),('반지름은 회전축까지 거리, 높이는 경계 차로 잡았고 수치구적이 일치한다.','The radius is distance to the axis and height is the boundary difference; independent quadrature agrees.'))
 area_svg(b,n,[(s.S(lo),s.S(hi),h,s.S(0))],q,f'7.1.{n} Shell height as a function of position');b.save()
ma(71,r'y=\ln x,\ y=0,\ x=2:\ (a)y\text{-axis};\ (b)x\text{-axis}',[r'(a)V_y=2\pi\int_1^2x\ln x\,dx=2\pi[x^2\ln x/2-x^2/4]_1^2',r'(b)V_x=\pi\int_1^2(\ln x)^2dx=\pi[x(\ln^2x-2\ln x+2)]_1^2'],r'(a)4\pi\ln2-3\pi/2;\quad(b)2\pi(\ln2-1)^2',('각 회전축에 맞는 껍질·원판 적분을 세우고 원시함수의 미분으로 확인했다.','Used shells and disks for the respective axes and checked the primitive derivatives.'),['a','b'])
ma(72,r'f(x)=x\sec^2x,\quad[0,\pi/4]\quad\text{average value}',[r'\bar f=\frac4\pi\int_0^{\pi/4}x\sec^2x\,dx',r'\int x\sec^2x\,dx=x\tan x+\ln|\cos x|',r'\bar f=\frac4\pi(\pi/4-\ln2/2)'],r'1-2\ln2/\pi',proofcheck)
ma(73,r'S(x)=\int_0^x\sin(\pi t^2/2)dt,\quad\int S(x)dx',[r'u=S(x),\ dv=dx,\quad S\prime(x)=\sin(\pi x^2/2)',r'\int S(x)dx=xS(x)-\int x\sin(\pi x^2/2)dx',r'\int x\sin(\pi x^2/2)dx=-\cos(\pi x^2/2)/\pi'],r'xS(x)+\cos(\pi x^2/2)/\pi+C',('곱의 미분에서 생기는 xS′ 항과 코사인 항의 미분이 상쇄된다.','The xS′ product-derivative term cancels the derivative of the cosine term.'))
h=lambda T:-mp.mpf('9.8')*T*T/2+3000*(T+(mp.mpf(30000)/160-T)*mp.log(1-mp.mpf(160)*T/30000))
add(74,('로켓 속도 v(t)=−gt−vₑln((m−rt)/m), g=9.8m/s²,m=30000kg,r=160kg/s,vₑ=3000m/s이다. 발사 높이0에서 (a)60초 후, (b)연료6000kg 소비 후 높이를 구하라.','A rocket has v(t)=−gt−vₑln((m−rt)/m), with g=9.8m/s²,m=30000kg,r=160kg/s,vₑ=3000m/s. Starting at height0, find altitude(a)after60s and(b)after consuming6000kg of fuel.'),fs(r'H(T)=\int_0^Tv(t)dt=-gT^2/2+v_e[T+(m/r-T)\ln(1-rT/m)]',r'(a)T=60;\quad(b)T=6000/160=37.5',fr'H(60)\approx{float(h(60)):.4f}\mathrm m,\quad H(37.5)\approx{float(h(mp.mpf("37.5"))):.4f}\mathrm m'),same(M(fr'(a){float(h(60)):.2f}\mathrm m;\quad(b){float(h(mp.mpf("37.5"))):.2f}\mathrm m')),('H(0)=0과 H′=v를 확인했다. 두 시간은 연료 소진 시각187.5초 이전이다.','Checked H(0)=0 and H′=v; both times precede the187.5s fuel-exhaustion time.'),['a','b'])
ma(75,r'v(t)=t^2e^{-t}\mathrm{m/s},\quad t\ge0',[r'D(t)=\int_0^t u^2e^{-u}du\quad(v\ge0)',r'\int u^2e^{-u}du=-e^{-u}(u^2+2u+2)',r'D(t)=2-(t^2+2t+2)e^{-t}'],r'2-(t^2+2t+2)e^{-t}\mathrm m',('D(0)=0, D′=v≥0이며 t→∞에서 이동거리가2m로 수렴한다.','D(0)=0, D′=v≥0, and total travel tends to2m as t→∞.'))
ma(76,r'f(0)=g(0)=0,\quad f^{\prime\prime},g^{\prime\prime}\text{ continuous}',[r'\int_0^a fg^{\prime\prime}dx=[fg\prime]_0^a-\int_0^a f\prime g\prime dx',r'\int_0^a f\prime g\prime dx=[f\prime g]_0^a-\int_0^af^{\prime\prime}gdx',r'\int_0^afg^{\prime\prime}dx=f(a)g\prime(a)-f\prime(a)g(a)+\int_0^af^{\prime\prime}gdx'],r'\int_0^afg^{\prime\prime}dx=f(a)g\prime(a)-f\prime(a)g(a)+\int_0^af^{\prime\prime}gdx',('0에서 두 경계항은 f(0)=g(0)=0으로 사라진다. 두 번 부분적분해 부호가 다시 양수가 된다.','Both lower boundary terms vanish because f(0)=g(0)=0; two integrations by parts restore the positive integral sign.'))
ma(77,r'f(1)=2,\ f(4)=7,\ f\prime(1)=5,\ f\prime(4)=3,\quad\int_1^4xf^{\prime\prime}(x)dx',[r'\int_1^4xf^{\prime\prime}dx=[xf\prime]_1^4-\int_1^4f\prime dx',r'=(4\cdot3-1\cdot5)-(7-2)=2'],r'2',('미적분학 기본정리로 도함수의 적분을 함수값 차로 바꾸어 확인했다.','Applied the Fundamental Theorem to replace the derivative integral by the endpoint difference.'))
add(78,('연속인 f′에 대해 (a)∫f dx=xf−∫xf′dx를 보이고, (b)역함수 g를 써서 정적분 공식을 유도하라. (c)양의 함수와 b>a>0에 대해 넓이 그림으로 해석하고 (d)∫₁ᵉlnx dx를 계산하라.','For continuous f′,(a)derive ∫f dx=xf−∫xf′dx.(b)Derive the definite-integral identity using inverse g.(c)Interpret it geometrically for positive functions and b>a>0.(d)Evaluate ∫₁ᵉlnx dx.'),fs(r'(a)u=f(x),\ dv=dx\Rightarrow\int fdx=xf-\int xf\prime dx',r'(b)y=f(x),\quad x=g(y),\quad dy=f\prime(x)dx',r'\int_a^bf(x)dx=bf(b)-af(a)-\int_{f(a)}^{f(b)}g(y)dy')+[('증가함수라면 큰 직사각형 넓이 bf(b)에서 작은 직사각형 af(a)를 뺀 영역을 곡선이 세로 적분과 가로 적분으로 나눈다. 감소함수에서는 가로 적분의 방향이 반대이므로 부호 있는 넓이로 해석한다.','For an increasing function, the curve partitions the area bf(b)−af(a) into vertical and horizontal integrals. For a decreasing function, the horizontal integral reverses orientation and is a signed area.')]+fs(r'(d)\int_1^e\ln xdx=e-\int_0^1e^ydy=e-(e-1)=1'),same(M(r'\int_a^bf=bf(b)-af(a)-\int_{f(a)}^{f(b)}g;\quad(d)1')),('치환 적분의 끝점 순서를 그대로 보존하여 증가·감소 역함수 모두에 적용했다.','Preserved the oriented transformed limits, covering both increasing and decreasing inverse functions.'),list('abcd'))
ma(79,r'(a)\int\frac{u}{v^2}dv=-\frac uv+\int\frac1vdu;\quad(b)\int\frac{\ln x}{x^2}dx',[r'd(u/v)=du/v-u\,dv/v^2\quad(v\ne0)',r'\int u\,dv/v^2=-u/v+\int du/v',r'(b)u=\ln x,\ v=x:\quad-\ln x/x+\int dx/x^2=-(\ln x+1)/x'],r'(a)\text{identity proved};\quad(b)-(\ln x+1)/x+C',proofcheck,['a','b'])
add(80,('Iₙ=∫₀^{π/2}sinⁿx dx라 하자.(a)I₂ₙ₊₂≤I₂ₙ₊₁≤I₂ₙ,(b)I₂ₙ₊₂/I₂ₙ,(c)I₂ₙ₊₁/I₂ₙ의 극한,(d)Wallis 곱 공식을 유도하라.(e)넓이1인 정사각형에 넓이1인 직사각형을 오른쪽, 위쪽에 번갈아 붙일 때 전체 가로/세로 비의 극한을 구하라.','Let Iₙ=∫₀^{π/2}sinⁿx dx.(a)Show I₂ₙ₊₂≤I₂ₙ₊₁≤I₂ₙ.(b)Find I₂ₙ₊₂/I₂ₙ.(c)Find the limit of I₂ₙ₊₁/I₂ₙ.(d)Derive the Wallis product.(e)Starting with a unit square, alternately attach area-one rectangles on the right and top; find the limiting overall width/height ratio.'),fs(r'(a)0\le\sin x\le1\Rightarrow\sin^{2n+2}x\le\sin^{2n+1}x\le\sin^{2n}x',r'(b)I_{2n+2}/I_{2n}=(2n+1)/(2n+2)',r'(c)\frac{2n+1}{2n+2}\le\frac{I_{2n+1}}{I_{2n}}\le1\Rightarrow\lim\frac{I_{2n+1}}{I_{2n}}=1',r'(d)\frac{I_{2n+1}}{I_{2n}}=\frac2\pi\prod_{k=1}^n\frac{(2k)^2}{(2k-1)(2k+1)}',r'\lim_{n\to\infty}\prod_{k=1}^n\frac{(2k)^2}{(2k-1)(2k+1)}=\pi/2')+[('넓이가 j에서 j+1로 늘어날 때 오른쪽에 붙이면 비가 (j+1)/j배, 위에 붙이면 j/(j+1)배가 된다. 한 쌍 후 비는 Wallis 유한곱이고, 중간 비와의 비율도1로 간다.','When total area grows from j to j+1, a right attachment multiplies the ratio by(j+1)/j, while a top attachment multiplies it by j/(j+1). After each pair the ratio equals a finite Wallis product; intervening ratios have the same limit.')],same(M(r'(b)\frac{2n+1}{2n+2};\quad(c)1;\quad(d),(e)\pi/2')),('I₀=π/2,I₁=1 및 첫 두 직사각형 비2,4/3을 확인했고, 두 부분수열의 동일 극한을 사용했다.','Checked I₀=π/2,I₁=1 and the first two rectangle ratios2,4/3; both subsequences have the same limit.'),list('abcde'))
add(81,('0<a<b인 증가 양의 곡선 y=f(x), 역함수 g와 c=f(a),d=f(b)를 생각하라. y축 회전체의 가로 단면으로 V=πb²d−πa²c−∫cᵈπg(y)²dy를 유도하고, 치환·부분적분으로 껍질공식 V=∫aᵇ2πxf(x)dx를 증명하라.','For an increasing positive curve y=f(x),0<a<b, inverse g, and c=f(a),d=f(b), use horizontal slices about the y-axis to obtain V=πb²d−πa²c−∫cᵈπg(y)²dy, then substitute and integrate by parts to derive V=∫aᵇ2πxf(x)dx.'),fs(r'V=\pi(b^2-a^2)c+\int_c^d\pi[b^2-g(y)^2]dy',r'=\pi b^2d-\pi a^2c-\int_c^d\pi g(y)^2dy',r'y=f(x)\Rightarrow\int_c^d\pi g(y)^2dy=\pi\int_a^b x^2 f\prime(x)dx',r'=\pi[x^2f(x)]_a^b-\int_a^b2\pi xf(x)dx',r'V=\int_a^b2\pi xf(x)dx'),same(M(r'V=\int_a^b2\pi xf(x)dx')),('0≤y≤c에서는 안쪽 반지름a, c≤y≤d에서는 g(y)이다. 경계항이 정확히 상쇄됨을 확인했다.','The inner radius is a for0≤y≤c and g(y) for c≤y≤d; the endpoint terms cancel exactly.'))
b.save();print('7.1 COMPLETE',len(b.E))
# Explicit instructions for the recurrence and identity proofs.
for n in [53,54,55,56,57,58,59,60,61,62]:
 b.E[n]['statement']['ko']+='부분적분으로 감소공식을 유도하거나 해당 감소공식을 반복 적용하라.'
 b.E[n]['statement']['en']+='Derive the recurrence by parts or apply the relevant recurrence repeatedly.'
b.E[76]['statement']=pair(M(r'f(0)=g(0)=0,\quad f^{\prime\prime},g^{\prime\prime}\text{ continuous}')+'두 번 부분적분하여 다음 식을 증명하라.'+b.E[76]['answer']['ko'],M(r'f(0)=g(0)=0,\quad f^{\prime\prime},g^{\prime\prime}\text{ continuous}')+'Integrate by parts twice to prove:'+b.E[76]['answer']['en'])
def attach(n,svg,ko,en):
 fn=f's7-1-{n}.svg';(ROOT/'assets'/fn).write_text(svg);b.E[n]['figure']={'src':'../exercise-content/assets/'+fn,'alt':pair(ko,en),'caption':pair(ko,en)}
# Geometric partition for f(x)=x+1, a=1, b=3.
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="570" height="405" viewBox="0 0 570 405"><rect width="570" height="405" fill="#f8fafc"/><g font-family="sans-serif" font-size="14"><text x="30" y="27">7.1.78 Inverse-integral area partition</text>']
svg+=['<path d="M70,345 L370,345 L370,65 L70,65 Z" fill="#fde68a"/>','<path d="M70,345 L170,345 L170,205 L370,65 L370,345 Z" fill="#bfdbfe"/>','<rect x="70" y="205" width="100" height="140" fill="#f8fafc"/>','<path d="M170,205 L370,65" stroke="#1d4ed8" stroke-width="3"/>','<path d="M70,355 V45 M60,345 H420" stroke="#475569" fill="none"/>','<text x="170" y="366">a=1</text><text x="355" y="366">b=3</text><text x="23" y="209">c=2</text><text x="23" y="70">d=4</text>','<text x="245" y="290">vertical area</text><text x="83" y="112">horizontal area</text><text x="390" y="105">y=f(x)=x+1</text><text x="30" y="393">Blue + yellow = b f(b) - a f(a); g(y)=y-1.</text></g></svg>']
attach(78,''.join(svg),'증가함수 예에서 파랑 세로적분과 노랑 가로적분이 직사각형 넓이 차를 나눈다.','For an increasing example, the blue vertical and yellow horizontal integrals partition the rectangle-area difference.')
# Alternately attach unit-area rectangles; true aspect ratio in each stage.
w0=h0=1.;rects=[(0,0,1,1)];out=['<svg xmlns="http://www.w3.org/2000/svg" width="720" height="340" viewBox="0 0 720 340"><rect width="720" height="340" fill="#f8fafc"/><g font-family="sans-serif" font-size="13"><text x="20" y="25">7.1.80 Equal-area additions and width / height</text>']
for k in range(6):
 if k:
  if k%2:ww=1/h0;rects.append((w0,0,ww,h0));w0+=ww
  else:hh=1/w0;rects.append((0,h0,w0,hh));h0+=hh
 ox=20+(k%3)*235;oy=145+(k//3)*145;scale=90/max(w0,h0)
 for j,(xx,yy,ww,hh)in enumerate(rects):out.append(f'<rect x="{ox+xx*scale}" y="{oy-(yy+hh)*scale}" width="{ww*scale}" height="{hh*scale}" fill="{["#bfdbfe","#fde68a"][j%2]}" stroke="#475569"/>')
 out.append(f'<text x="{ox}" y="{oy+20}">Area {k+1}; ratio {w0/h0:.5f}</text>')
out.append('</g></svg>');attach(80,''.join(out),'각 추가 직사각형의 넓이는1이며, 가로/세로 비는 π/2로 수렴한다.','Each added rectangle has area1; the width/height ratio tends to π/2.')
area_svg(b,81,[(s.S(1),s.S(3),x+1,s.S(0))],x,'7.1.81 Region revolved about the y-axis')
b.save()
for n,eq in [(21,r'I=e^{3x}\cos x/3+e^{3x}\sin x/9-I/9'),(22,r'I=e^x\sin(\pi x)-\pi e^x\cos(\pi x)-\pi^2 I'),(23,r'I=e^{2\theta}\sin3\theta/2-3e^{2\theta}\cos3\theta/4-9I/4'),(24,r'I=-e^{-\theta}\cos2\theta+2e^{-\theta}\sin2\theta-4I')]:
 for lang in ['ko','en']:b.E[n]['steps'][lang].insert(-1,M(eq))
b.save()
