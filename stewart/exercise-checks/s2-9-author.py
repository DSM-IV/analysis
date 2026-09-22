"""Source-checked §2.9; symbolic derivatives and numerical error boundaries."""
import json, math, html, sys
from pathlib import Path
import sympy as s
import mpmath as mp
from early_helpers import Book, pair, same, fs, ROOT
mp.mp.dps=45
x=s.symbols('x',real=True); R=s.Rational
b=Book('2.9',[196,197,198]); checks=[]
def tex(v):return s.latex(s.simplify(v))
def M(t):return r'\('+t+r'\)'
def add(n,eq,k,e,lines,ans,notes=None,parts=''):
 pg=196 if n<=6 else 197 if n<=46 else 198
 steps=fs(*lines)
 if notes:steps.append(notes)
 b.add(n,pg,('선형근사와 미분','Linear approximations and differentials'),(M(eq)+' '+k,M(eq)+' '+e),steps,same(M(ans)),parts=list(parts),check=('도함수, 기준점의 값과 단위를 대조하고 근사와 정확한 변화를 구별했다.','Checked derivatives, base values and units, distinguishing approximation from exact change.'))
 b.E[n]['conceptHref']='../../calc1/index.html'
def plot(n,funcs,lo,hi,segments=()):
 data=[(label,[(lo+(hi-lo)*j/240,float(f(lo+(hi-lo)*j/240)))for j in range(241)])for label,f in funcs]
 pts=[p for _,ls in data for p in ls]+[p for _,a,c in segments for p in (a,c)];mn=min(y for _,y in pts);mx=max(y for _,y in pts);pad=(mx-mn)*.15 or 1;mn-=pad;mx+=pad
 X=lambda v:65+500*(v-lo)/(hi-lo);Y=lambda v:325-270*(v-mn)/(mx-mn)
 out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 630 410"><rect width="630" height="410" fill="#f8fafc"/>',f'<text x="30" y="25" font-size="16">Exercise 2.9.{n}</text>']
 if mn<=0<=mx:out.append(f'<path d="M65 {Y(0)}H565" stroke="#64748b"/>')
 if lo<=0<=hi:out.append(f'<path d="M{X(0)} 55V325" stroke="#64748b"/>')
 for j,(label,ls)in enumerate(data):
  color=['#2563eb','#dc2626','#16a34a'][j%3];out.append('<polyline points="'+' '.join(f'{X(a):.3f},{Y(c):.3f}'for a,c in ls)+f'" stroke="{color}" fill="none" stroke-width="2"/><text x="{65+j*185}" y="390" fill="{color}" font-size="13">{html.escape(label)}</text>')
 for j,(label,a,c)in enumerate(segments):
  out.append(f'<path d="M{X(a[0])},{Y(a[1])}L{X(c[0])},{Y(c[1])}" stroke="#7c3aed" stroke-width="3"/><text x="{X(c[0])+5}" y="{Y(c[1])-8+j*13}" font-size="13">{label}</text>')
 for j in range(5):
  a=lo+(hi-lo)*j/4;c=mn+(mx-mn)*j/4;out.append(f'<text x="{X(a)-10}" y="347" font-size="11">{a:.3g}</text><text x="8" y="{Y(c)+3}" font-size="11">{c:.3g}</text>')
 out.append('</svg>');name=f's2-9-{n}.svg';(ROOT/'assets'/name).write_text(''.join(out));b.E[n]['figure']={'src':'../exercise-content/assets/'+name,'alt':pair('함수와 선형근사 또는 오차의 자체 그래프','Original graph of the function and linear approximation or error'),'caption':pair('주어진 식으로 직접 계산한 그래프.','Graph computed directly from the stated formulas.')}
def linear(f,a):
 L=s.simplify(f.subs(x,a)+s.diff(f,x).subs(x,a)*(x-a));assert s.simplify(L.subs(x,a)-f.subs(x,a))==0;assert s.simplify(s.diff(L,x)-s.diff(f,x).subs(x,a))==0;return L
for n,f,a in [(1,x**3-x*x+3,-2),(2,s.cos(2*x),s.pi/6),(3,x**R(1,3),8),(4,2/s.sqrt(x*x-5),3)]:
 L=linear(f,a);add(n,'f(x)='+tex(f)+r',\quad a='+tex(a),'기준점에서의 선형화를 구하라.','Find the linearization at the base point.',["f'(x)="+tex(s.diff(f,x)),r'L(x)=f(a)+f\prime(a)(x-a)', 'L(x)='+tex(L)],'L(x)='+tex(L));checks.append([n,str(L)])
for n,f,vals in [(5,s.sqrt(1-x),[R(1,10),R(1,100)]),(6,(1+x)**R(1,3),[-R(1,20),R(1,10)])]:
 L=linear(f,0);lines=['f(x)='+tex(f),r'L(x)=f(0)+f\prime(0)x='+tex(L)]+['f('+tex(v)+r')\approx L('+tex(v)+')='+tex(L.subs(x,v))for v in vals]
 add(n,'f(x)='+tex(f)+r',\quad a=0','선형화를 구하고 '+', '.join(M(tex(f.subs(x,v))) for v in vals)+'을 근사하라. 함수와 접선도 그려라.','Linearize, estimate '+', '.join(M(tex(f.subs(x,v))) for v in vals)+', and graph the function and tangent.',lines,'L(x)='+tex(L)+r';\quad '+r',\ '.join(tex(L.subs(x,v))for v in vals));plot(n,[('f(x)',s.lambdify(x,f,'math')),('L(x)',s.lambdify(x,L,'math'))],-.5,.5)
# Find the component near the expansion point by bisection, retaining exact inequality globally.
for n,f,L,left,right in [(7,(1+2*x)**R(1,4),1+x/2,-.499,2),(8,(1+x)**-3,1-3*x,-.9,1),(9,(1+2*x)**-4,1-8*x,-.49,1),(10,s.tan(x),x,-1.5,1.5)]:
 assert s.simplify(linear(f,0)-L)==0
 err=s.lambdify(x,f-L,'mpmath');g=lambda t:abs(err(t))-mp.mpf('.1')
 def bisect(a,c):
  for _ in range(180):
   mid=(a+c)/2
   if g(a)*g(mid)<=0:c=mid
   else:a=mid
  return (a+c)/2
 lo=bisect(mp.mpf(left),mp.mpf(0));hi=bisect(mp.mpf(0),mp.mpf(right));assert abs(g(lo))<mp.mpf('1e-35') and abs(g(hi))<mp.mpf('1e-35')
 note=('표시한 구간은 영을 포함하는 정의역 가지에서의 근사 범위다.','The displayed interval is the accuracy range on the domain branch containing zero.')
 lines=[r'L(x)=f(0)+f\prime(0)x='+tex(L),r'|f(x)-L(x)|<0.1',f'{float(lo):.9f}<x<{float(hi):.9f}']
 ans=lines[-1]
 if n==9:
  # A disconnected interval on x < -1/2 also meets the absolute-error criterion.
  roots=[]
  for sign in [-1,1]:
   poly=s.together(f-L-sign*R(1,10)).as_numer_denom()[0]
   roots.append(next(float(s.re(z))for z in s.nroots(poly,maxsteps=300)if abs(float(s.im(z)))<1e-10 and float(s.re(z))<-.5))
  roots.sort();lines.append(f'{roots[0]:.9f}<x<{roots[1]:.9f}');ans=r'x\in('+f'{roots[0]:.9f},{roots[1]:.9f}'+r')\cup('+f'{float(lo):.9f},{float(hi):.9f}'+')';note=('절대오차만을 기준으로 하면 특이점 왼쪽의 별도 구간도 포함된다. 끝점은 오차가 정확히 영점일이므로 제외한다.','For the global absolute-error criterion, include the disconnected interval left of the pole. Endpoints have error exactly 0.1 and are excluded.')
 if n==10:
  lines.append(r'\bigcup_{k\in\mathbb Z}(a_k,b_k),\quad \tan a_k-a_k=-0.1,\quad\tan b_k-b_k=0.1,\quad a_k,b_k\in(k\pi-\pi/2,k\pi+\pi/2)');ans=r'k=0:\ '+ans+r';\quad\text{all branches: }\bigcup_{k\in\mathbb Z}(a_k,b_k)';note=('각 가지에서 tan(x)−x는 도함수 tan²(x)가 음이 아니므로 증가하고 양 끝에서 무한대로 발산하여 두 경계가 유일하다. 선형화의 국소적 의미는 영을 포함하는 구간에 있다.','On each branch tan(x)−x increases, since its derivative is tan²(x), and ranges from negative to positive infinity, so both endpoints are unique. The interval around zero is the local linearization range.')
 add(n,'f(x)='+tex(f)+r',\quad L(x)='+tex(L),'영에서의 선형화를 확인하고 절대오차가 영점일보다 작은 범위를 구하라.','Verify the linearization at zero and find where the absolute error is less than 0.1.',lines,ans,note);plot(n,[('f(x)-L(x)',s.lambdify(x,f-L,'math')),('+0.1',lambda t:.1),('-0.1',lambda t:-.1)],float(lo)*1.08,float(hi)*1.08);checks.append([n,str(lo),str(hi)])
t,u,th=s.symbols('t u theta',real=True)
for n,v,f in [(11,x,(x*x-3)**-2),(12,t,s.sqrt(1-t**4)),(13,u,(1+2*u)/(1+3*u)),(14,th,th**2*s.sin(2*th)),(15,x,1/(x*x-3*x)),(16,th,s.sqrt(1+s.cos(th))),(17,t,s.sqrt(t-s.cos(t))),(18,x,s.sin(x)/x)]:
 d=s.diff(f,v);assert s.simplify(s.limit((f.subs(v,v+s.Symbol('h'))-f)/s.Symbol('h'),s.Symbol('h'),0)-d)==0
 add(n,'y='+tex(f),'미분 dy를 구하라.','Find the differential dy.',[r'dy=\frac{dy}{d'+s.latex(v)+r'}\,d'+s.latex(v)],'dy='+tex(d)+r'\,d'+s.latex(v),('분모가 영이 되지 않고 도함수가 존재하는 정의역에서 적용한다.','Apply on the domain where denominators are nonzero and the derivative exists.'));checks.append([n,str(d)])
for n,f,a,h in [(19,s.tan(x),s.pi/4,-R(1,10)),(20,s.cos(s.pi*x),R(1,3),-R(1,50)),(21,s.sqrt(3+x*x),1,-R(1,10)),(22,(x+1)/(x-1),2,R(1,20))]:
 d=s.diff(f,x);val=s.simplify(d.subs(x,a)*h);add(n,'y='+tex(f)+r',\quad x='+tex(a)+r',\quad dx='+tex(h),'(a) 미분식을 구하고 (b) 주어진 값에서 계산하라.','(a) Find dy and (b) evaluate it at the specified values.',[r'dy='+tex(d)+r'\,dx',r'dy\big|_{x='+tex(a)+'}='+tex(val)],r'\text{(a)}\ dy='+tex(d)+r'\,dx;\quad\text{(b)}\ '+tex(val),parts='ab')
for n,f,a,h in [(23,x*x-4*x,3,R(1,2)),(24,x-x**3,0,-R(3,10)),(25,s.sqrt(x-2),3,R(4,5)),(26,x**3,1,R(1,2))]:
 L=linear(f,a);delta=s.simplify(f.subs(x,a+h)-f.subs(x,a));dy=s.simplify(s.diff(f,x).subs(x,a)*h)
 add(n,'y='+tex(f)+r',\quad x='+tex(a)+r',\quad dx=\Delta x='+tex(h),'실제 변화와 미분을 계산하고 dx, dy, Δy를 도식화하라.','Compute the actual change and differential, and diagram dx, dy and Δy.',[r'\Delta y=f(x+dx)-f(x)='+tex(delta),r'dy=f\prime(x)dx='+tex(dy)],r'\Delta y='+tex(delta)+r',\quad dy='+tex(dy))
 A=float(a);H=float(h);F=float(f.subs(x,a));offset=abs(H)*.07
 seg=[('dx',(A,F),(A+H,F)),('dy',(A+H,F),(A+H,float(L.subs(x,a+h)))),('Delta y',(A+H+offset,F),(A+H+offset,float(f.subs(x,a+h))))]
 plot(n,[('f(x)',s.lambdify(x,f,'math')),('L(x)',s.lambdify(x,L,'math'))],min(A,A+H)-abs(H)*.25,max(A,A+H)+abs(H)*.4,seg);checks.append([n,str(delta),str(dy)])
for n,f in [(27,x**4-x+1),(28,(x**3+3)**2),(29,s.sqrt(5-x)),(30,1/(x*x+1))]:
 vals=[];lines=[r'\Delta y=f(1+h)-f(1),\quad dy=f\prime(1)h'];errors=[]
 for h in [R(1,20),R(1,100)]:
  de=f.subs(x,1+h)-f.subs(x,1);dy=s.diff(f,x).subs(x,1)*h;errors.append(abs(float(de-dy)));lines.append('h='+tex(h)+r':\quad\Delta y\approx'+f'{float(de):.10f}'+r',\quad dy='+tex(dy));vals.append([float(de),float(dy)])
 assert errors[1]<errors[0];add(n,'f(x)='+tex(f),'입력이 일에서 일점영오, 일점영일로 변할 때 Δy와 dy를 비교하라.','Compare Δy and dy for changes from 1 to 1.05 and from 1 to 1.01.',lines,r'|\Delta y-dy|:\ '+f'{errors[0]:.9g}'+r'\ \to\ '+f'{errors[1]:.9g}',('입력 변화가 작아질수록 이 두 경우의 절대오차가 감소한다.','The absolute error decreases between these two cases as the input change shrinks.'));checks.append([n,vals])
for n,f,a,z,label in [(31,x**4,2,R(1999,1000),'(1.999)^4'),(32,1/x,4,R(2001,500),'1/4.002'),(33,x**R(1,3),1000,1001,r'\sqrt[3]{1001}'),(34,s.sqrt(x),100,R(201,2),r'\sqrt{100.5}'),(35,s.tan(x),0,s.pi/90,r'\tan2^\circ'),(36,s.cos(x),s.pi/6,29*s.pi/180,r'\cos29^\circ'),(37,s.sec(x),0,R(2,25),r'\sec0.08'),(38,s.sqrt(x),4,R(201,50),r'\sqrt{4.02}')]:
 L=linear(f,a);v=s.simplify(L.subs(x,z));add(n,label,'선형근사로 값을 추정하고 기준점 선택을 설명하라.','Estimate by linearization and explain the base-point choice.',[r'f(x)='+tex(f)+r',\quad a='+tex(a),r'L(x)='+tex(L),'L('+tex(z)+')='+tex(v)+r'\approx'+f'{float(v):.10f}'],label+r'\approx'+tex(v),('삼각함수의 도함수에서는 각을 라디안으로 환산한다.','Angles used in trigonometric derivatives are measured in radians.') if n in [35,36] else None);checks.append([n,str(v)])
add(39,r'a=30\ \mathrm{cm},\quad |da|\le0.1\ \mathrm{cm}','정육면체 (a) 부피와 (b) 겉넓이의 최대 절대·상대·백분율 오차를 미분으로 추정하라.','Estimate maximum absolute, relative and percentage errors for (a) cube volume and (b) surface area using differentials.',[r'V=a^3,\quad |dV|=3a^2|da|=270\ \mathrm{cm^3}',r'|dV|/V=3|da|/a=0.01',r'S=6a^2,\quad |dS|=12a|da|=36\ \mathrm{cm^2}',r'|dS|/S=2|da|/a=1/150'],r'\text{(a)}\ 270\ \mathrm{cm^3},\ 0.01,\ 1\%;\quad\text{(b)}\ 36\ \mathrm{cm^2},\ 1/150,\ 2/3\%',parts='ab')
add(40,r'r=24\ \mathrm{cm},\quad |dr|\le0.2\ \mathrm{cm}','원판 넓이의 (a) 최대오차와 (b) 상대·백분율 오차를 미분으로 추정하라.','Estimate (a) maximum area error and (b) relative and percentage errors for the disk.',[r'A=\pi r^2,\quad |dA|=2\pi r|dr|=9.6\pi\ \mathrm{cm^2}',r'|dA|/A=2|dr|/r=1/60'],r'\text{(a)}\ 9.6\pi\ \mathrm{cm^2};\quad\text{(b)}\ 1/60,\ 5/3\%',parts='ab')
add(41,r'C=84\ \mathrm{cm},\quad |dC|\le0.5\ \mathrm{cm}','구의 대원 둘레를 측정했다. (a) 겉넓이와 (b) 부피의 최대오차와 상대오차를 추정하라.','The great-circle circumference of a sphere is measured. Estimate maximum and relative errors in (a) surface area and (b) volume.',[r'r=C/(2\pi),\quad S=C^2/\pi,\quad V=C^3/(6\pi^2)',r'|dS|=2C|dC|/\pi=84/\pi,\quad |dS|/S=2|dC|/C=1/84',r'|dV|=C^2|dC|/(2\pi^2)=1764/\pi^2,\quad |dV|/V=3|dC|/C=1/56'],r'\text{(a)}\ 84/\pi\ \mathrm{cm^2},\ 1/84;\quad\text{(b)}\ 1764/\pi^2\ \mathrm{cm^3},\ 1/56',parts='ab')
add(42,r'2r=50\ \mathrm m,\quad dr=0.05\ \mathrm{cm}','반구형 돔의 곡면에 칠하는 페인트의 부피를 추정하라.','Estimate the paint volume for the curved surface of a hemispherical dome.',[r'r=25\ \mathrm m,\quad dr=0.0005\ \mathrm m',r'V=\frac23\pi r^3,\quad dV=2\pi r^2dr=0.625\pi'],r'V_{\rm paint}\approx0.625\pi\ \mathrm{m^3}\approx1.9635\ \mathrm{m^3}')
add(43,r'V=\pi r^2h,\quad h\text{ constant}','(a) 안쪽 반지름 r, 두께 Δr인 얇은 원기둥 껍질의 근사 부피와 (b) 그 오차를 구하라.','Find (a) approximate volume of a thin cylindrical shell with inner radius r and thickness Δr, and (b) the approximation error.',[r'dV=2\pi rh\,dr',r'\Delta V=\pi h[(r+\Delta r)^2-r^2]=2\pi rh\Delta r+\pi h(\Delta r)^2'],r'\text{(a)}\ 2\pi rh\Delta r;\quad\text{(b)}\ \Delta V-dV=\pi h(\Delta r)^2',parts='ab')
add(44,r'a=20\ \mathrm{cm},\quad\theta=30^\circ,\quad|d\theta|\le1^\circ','직각삼각형에서 길이 a인 변의 맞은편 각이 θ다. 빗변의 (a) 오차와 (b) 백분율 오차를 추정하라.','The side of length a is opposite θ in a right triangle. Estimate (a) hypotenuse error and (b) percentage error.',[r'c=20\csc\theta,\quad dc=-20\csc\theta\cot\theta\,d\theta',r'|d\theta|=\pi/180,\quad c=40,\quad|dc|=2\pi\sqrt3/9',r'100|dc|/c=5\pi\sqrt3/9'],r'\text{(a)}\ 2\pi\sqrt3/9\ \mathrm{cm}\approx1.2092\ \mathrm{cm};\quad\text{(b)}\ 3.0230\%',parts='ab')
add(45,r'V=RI,\quad V\text{ constant}','저항 오차와 전류 오차의 상대적 크기가 일차근사에서 같음을 보여라.','Show that resistance and current have equal relative-error magnitudes to first order.',[r'I=V/R,\quad dI=-V\,dR/R^2',r'\frac{dI}{I}=-\frac{dR}{R}'],r'\frac{|dI|}{|I|}=\frac{|dR|}{|R|}\quad(R\ne0,\ I\ne0)')
add(46,r'F=kR^4','혈류량의 상대변화와 반지름 상대변화의 관계를 구하고, 반지름 오 퍼센트 증가의 효과를 추정하라.','Relate relative changes in flow and vessel radius, and estimate the effect of a five-percent radius increase.',[r'dF=4kR^3dR,\quad dF/F=4\,dR/R',r'dR/R=0.05\Rightarrow dF/F=0.20',r'\Delta F/F=1.05^4-1=0.21550625'],r'\Delta F/F\approx20\%\quad(\text{exact: }21.550625\%)')
add(47,r'c\text{ constant};\quad u=u(x),\ v=v(x)','미분의 상수·상수배·합·곱·몫·거듭제곱 법칙을 증명하라.','Prove the constant, scalar, sum, product, quotient and power rules for differentials.',[r'dF=F\prime(x)\,dx',r'\text{(a)}\ dc=0\,dx=0',r'\text{(b)}\ d(cu)=cu\prime dx=c\,du',r'\text{(c)}\ d(u+v)=(u\prime+v\prime)dx=du+dv',r'\text{(d)}\ d(uv)=(u\prime v+uv\prime)dx=v\,du+u\,dv',r'\text{(e)}\ d(u/v)=(vu\prime-uv\prime)dx/v^2=(v\,du-u\,dv)/v^2,\quad v\ne0',r'\text{(f)}\ d(x^n)=nx^{n-1}dx'],r'dc=0,\ d(cu)=c\,du,\ d(u+v)=du+dv,\ d(uv)=u\,dv+v\,du,\ d(u/v)=(v\,du-u\,dv)/v^2,\ d(x^n)=nx^{n-1}dx',parts='abcdef')
r=mp.findroot(lambda z:z/mp.sin(z)-1-mp.mpf('.02'),.34);err=100*((mp.pi/18)/mp.sin(mp.pi/18)-1)
add(48,r'\sin\theta\approx\theta','(a) 영에서 선형화를 확인하고 (b) 십 도에서의 백분율 오차와 (c) 상대오차가 이 퍼센트 미만인 영 근방의 각도 범위를 구하라.','(a) Verify linearization at zero, (b) find percentage error at ten degrees, and (c) find the range around zero with relative error below two percent.',[r'L(\theta)=\sin0+\cos0\,\theta=\theta',r'E=\frac{|\theta-\sin\theta|}{|\sin\theta|}',r'E(\pi/18)\times100\approx'+f'{float(err):.8f}'+r'\%',r'E=0.02\Rightarrow|\theta|\approx'+f'{float(r):.10f}'],r'\text{(a)}\ L=\theta;\quad\text{(b)}\ '+f'{float(err):.6f}'+r'\%;\quad\text{(c)}\ |\theta|<'+f'{float(r):.9f}'+r'\ \mathrm{rad}\approx'+f'{float(r*180/mp.pi):.6f}'+r'^\circ',('정확한 값 sin θ를 상대오차의 분모로 사용했다. 영에서는 그 비가 정의되지 않지만 극한값 영으로 연속 확장한다.','Relative error uses the exact value sin θ in the denominator. At zero the ratio is undefined but has continuous extension zero.'),parts='abc');plot(48,[('relative error',lambda z:float(z/mp.sin(z)-1) if z else 0),('2 percent',lambda z:.02)],-.45,.45);checks.append([48,str(r),str(err)])
add(49,r'f(1)=5,\quad f\prime(1)=2','원문 도함수 그래프는 일 근방에서 감소한다. (a) f(0.9), f(1.1)을 추정하고 (b) 과대·과소 여부를 판단하라.','The source derivative graph decreases near 1. (a) Estimate f(0.9) and f(1.1); (b) determine whether these are overestimates or underestimates.',[r'L(x)=5+2(x-1)',r'L(0.9)=4.8,\quad L(1.1)=5.2',r'f\prime\text{ decreasing}\Rightarrow f\text{ concave down}\Rightarrow f(x)<L(x)\ (x\ne1)'],r'\text{(a)}\ 4.8,\ 5.2;\quad\text{(b) both overestimates}',parts='ab')
add(50,r'g(2)=-4,\quad g\prime(x)=\sqrt{x^2+5}','(a) g(1.95), g(2.05)를 추정하고 (b) 과대·과소 여부를 판단하라.','(a) Estimate g(1.95) and g(2.05); (b) decide whether these are overestimates or underestimates.',[r'g\prime(2)=3,\quad L(x)=-4+3(x-2)',r'L(1.95)=-4.15,\quad L(2.05)=-3.85',r'g\prime\prime(x)=x/\sqrt{x^2+5}>0\quad(x>0)'],r'\text{(a)}\ -4.15,\ -3.85;\quad\text{(b) both underestimates}',parts='ab')
from final_sections_helpers import localize
localize(b)
assert sorted(b.E)==list(range(1,51));b.save()
sys.path.insert(0,str(ROOT.parent));from build_exercises import validate_document
validate_document(json.loads((ROOT/'s2-9.json').read_text()),ROOT/'s2-9.json')
(ROOT.parent/'exercise-checks/s2-9-report.json').write_text(json.dumps({'section':'2.9','sourceVisualPages':[233,234,235],'checks':checks,'notes':['9 includes disconnected accuracy interval','10 states all tangent branches','48 relative error uses exact sine denominator']},ensure_ascii=False,indent=2)+'\n')
print('2.9: 50 exercises; symbolic derivatives, linearizations and error boundaries checked')
