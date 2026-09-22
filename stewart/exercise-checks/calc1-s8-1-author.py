from calc1_helpers import *
from calc1_plot_helpers import plots
x,y,u=s.symbols('x y u',positive=True);Q=s.Rational;pi=s.pi;sq=s.sqrt;log=s.log;ex=s.exp
b=CalcBook('8.1',[603,604,605]);records=[]
def add(n,st,steps,ans,ck=None,parts=[]):
 b.add(n,603 if n<=36 else 604 if n<=49 else 605,('호의 길이','Arc length'),st,steps,ans,parts=parts);b.verify(n,*(ck or('길이 요소의 제곱을 미분식과 대조하고 독립 수치구적 또는 끝점 거리로 확인했다.','Checked the squared arc-length factor against the derivative and verified by independent quadrature or endpoint distance.')));b.save()
def ma(n,eq,steps,ans,ck=None,parts=[]):add(n,(M(eq)+'호의 길이를 구하거나 증명하라.',M(eq)+'Find arc length or prove the stated relation.'),fs(*steps),same(M(ans)),ck,parts)
def arc(n,f,q,a,c,spd=None,F=None,setup=False):
 a,c=s.sympify(a),s.sympify(c);d=s.diff(f,q);sp=s.sqrt(1+d*d)if spd is None else s.sympify(spd)
 if spd is not None:assert s.trigsimp(s.factor(sp**2-1-d*d))==0,(n,sp,d)
 I=s.Integral(sp,(q,a,c));steps=fs(('dy/dx'if q==x else'dx/dy')+'='+s.latex(d),r'ds=\sqrt{1+('+s.latex(d)+')^2}\,d'+str(q)+'='+s.latex(sp)+'d'+str(q),r'L='+s.latex(I));val=None
 if not setup:
  if F is None:F=s.integrate(sp,q)
  assert not F.has(s.Integral),(n,F)
  delta=s.simplify(s.trigsimp(s.diff(F,q)-sp))
  if delta!=0:
   ff=s.lambdify(q,sp,'mpmath');FF=s.lambdify(q,F,'mpmath');pt=mp.mpf(str(((a+c)/2).evalf(30)));assert abs(mp.diff(FF,pt)-ff(pt))<mp.mpf('1e-20'),(n,delta)
  val=s.simplify(s.limit(F,q,c,dir='-')-s.limit(F,q,a,dir='+'));num=mp.quad(s.lambdify(q,sp,'mpmath'),[mp.mpf(str(a.evalf(30))),mp.mpf(str(c.evalf(30)))]);assert abs(complex(val.evalf())-complex(num))<1e-7,(n,val,num);steps+=fs(r'\int ds='+s.latex(F),r'L='+s.latex(val));records.append({'number':n,'value':str(val),'numeric':str(num)})
 eq=('y='if q==x else'x=')+s.latex(f)+',\quad'+s.latex(a)+r'\le '+str(q)+r'\le '+s.latex(c)
 add(n,(M(eq)+('길이 적분만 세우고 계산하지 말라.'if setup else'정확한 호의 길이를 구하라.'),M(eq)+('Set up, but do not evaluate, the length integral.'if setup else'Find the exact arc length.')),steps,same(M('L='+s.latex(I if setup else val))))
 return val
arc(1,3-2*x,x,-1,3,sq(5),sq(5)*x)
for lang in['ko','en']:b.E[1]['steps'][lang].append(M(r'\sqrt{(3-(-1))^2+((-3)-5)^2}=\sqrt{80}=4\sqrt5'))
arc(2,sq(4-x*x),x,0,2,2/sq(4-x*x),2*s.asin(x/2))
for lang in['ko','en']:b.E[2]['steps'][lang].append(M(r'\text{Quarter-circle of radius2: }L=(1/4)(2\pi\cdot2)=\pi'))
for n,f,q,a,c in [(3,x**3,x,0,2),(4,ex(x),x,1,3),(5,x-log(x),x,1,4),(6,y*y+y,y,0,3),(7,s.sin(y),y,0,pi/2),(8,ex(y*y),y,-1,1)]:arc(n,f,q,a,c,setup=True)
rows=[(9,Q(2,3)*x**Q(3,2),x,0,2,sq(1+x),Q(2,3)*(1+x)**Q(3,2)),(10,(x+4)**Q(3,2),x,0,4,sq(9*x+40)/2,(9*x+40)**Q(3,2)/27),(11,Q(2,3)*(1+x*x)**Q(3,2),x,0,1,1+2*x*x,x+Q(2,3)*x**3),(12,(x*x-4)**Q(3,2)/6,x,2,3,(x*x-2)/2,x**3/6-x),(13,x**3/3+1/(4*x),x,1,2,x*x+1/(4*x*x),x**3/3-1/(4*x)),(14,y**4/8+1/(4*y*y),y,1,2,y**3/2+1/(2*y**3),y**4/8-1/(4*y*y)),(15,log(s.sin(2*x))/2,x,pi/8,pi/6,1/s.sin(2*x),log(s.tan(x))/2),(16,log(s.cos(x)),x,0,pi/3,1/s.cos(x),log(s.sec(x)+s.tan(x))),(17,log(s.sec(x)),x,0,pi/4,s.sec(x),log(s.sec(x)+s.tan(x))),(18,ex(y)+ex(-y)/4,y,0,1,ex(y)+ex(-y)/4,ex(y)-ex(-y)/4),(19,sq(y)*(y-3)/3,y,1,9,(y+1)/(2*sq(y)),y**Q(3,2)/3+sq(y)),(20,3+s.cosh(2*x)/2,x,0,1,s.cosh(2*x),s.sinh(2*x)/2),(21,x*x/4-log(x)/2,x,1,2,x/2+1/(2*x),x*x/4+log(x)/2),(22,sq(x-x*x)+s.asin(sq(x)),x,0,1,1/sq(x),2*sq(x)),(23,log(1-x*x),x,0,Q(1,2),(1+x*x)/(1-x*x),-x+log((1+x)/(1-x))),(24,1-ex(-x),x,0,2,sq(1+ex(-2*x)),x+log(1+sq(1+ex(-2*x)))-sq(1+ex(-2*x))),(25,x*x/2,x,-1,1,sq(1+x*x),(x*sq(1+x*x)+s.asinh(x))/2),(26,(y-4)**Q(3,2),y,5,8,sq(9*y-32)/2,(9*y-32)**Q(3,2)/27)]
for row in rows:arc(*row)
for lang,txt in[('ko','원문의 구간이 생략되어 전체 실수 정의역0≤x≤1을 사용한다. 왼쪽 끝은 이상적분이지만 수렴한다.'),('en','With no interval specified, use the full real domain0≤x≤1. The left endpoint is improper but convergent.')]:b.E[22]['steps'][lang].insert(0,txt)
for n,txt in [(25,r'P=(-1,1/2),\ Q=(1,1/2)'),(26,r'x^2=(y-4)^3,\quad P=(1,5),\ Q=(8,8)')]:
 for lang in['ko','en']:b.E[n]['statement'][lang]+=M(txt)
def plotcurve(n,f,a,c,title=None,extra=[]):
 fn=s.lambdify(x,f,'math');ys=[fn(float(a)+(float(c)-float(a))*j/200)for j in range(201)];mi,ma=min(ys),max(ys);pad=(ma-mi)*.12 or .1
 plots(b,n,[(title or f'8.1.{n} Curve',float(a),float(c),mi-pad,ma+pad,[('curve',fn)]+extra)])
nums=[(27,x*x+x**3,1,2),(28,x+s.cos(x),0,pi/2),(29,x**Q(1,3),1,4),(30,x*s.tan(x),0,1),(31,x*ex(-x),1,2),(32,log(x*x+4),-2,2)]
for n,f,a,c in nums:
 sp=s.sqrt(1+s.diff(f,x)**2);ff=s.lambdify(x,sp,'mpmath');L=mp.quad(ff,[float(a),float(c)]);fv=s.lambdify(x,f,'mpmath');poly=sum(mp.sqrt((float(c-a)/4)**2+(fv(float(a+(c-a)*j/4))-fv(float(a+(c-a)*(j-1)/4)))**2)for j in range(1,5));poly=float(poly)
 add(n,(M('y='+s.latex(f)+',\quad'+s.latex(a)+r'\le x\le '+s.latex(c))+'그래프를 보고 길이를 대략 추정한 뒤 소수4자리까지 계산하라.',M('y='+s.latex(f)+',\quad'+s.latex(a)+r'\le x\le '+s.latex(c))+'Graph and visually estimate length, then compute it to4decimal places.'),fs(r'y^\prime='+s.latex(s.diff(f,x)),r'\text{Coarse 4-chord visual estimate}\approx'+f'{poly:.2f}',r'L='+s.latex(s.Integral(sp,(x,a,c))),r'L\approx'+f'{float(L):.4f}'),same(M(r'L\approx'+f'{float(L):.4f}')));plotcurve(n,f,a,c);records.append({'number':n,'numeric':str(L)})
for n,f,c in[(33,x*s.sin(x),2*pi),(34,ex(-x*x),2)]:
 sp=s.sqrt(1+s.diff(f,x)**2);ff=s.lambdify(x,sp,'mpmath');h=mp.mpf(str(s.N(c,30)))/10;S=h/3*(ff(0)+ff(10*h)+4*sum(ff(j*h)for j in[1,3,5,7,9])+2*sum(ff(j*h)for j in[2,4,6,8]));L=mp.quad(ff,[0,float(c)/2,float(c)])
 ma(n,'y='+s.latex(f)+r',\quad0\le x\le '+s.latex(c)+r';\quad\text{Simpson }n=10\text{ and numerical comparison}',[r'L='+s.latex(s.Integral(sp,(x,0,c))),r'h='+s.latex(c/10),r'S_{10}=\frac h3[g_0+4g_1+2g_2+\cdots+4g_9+g_{10}],\quad g=\sqrt{1+(y^\prime)^2}',r'S_{10}\approx'+f'{float(S):.8f}'+r',\quad L\approx'+f'{float(L):.8f}',r'L-S_{10}\approx'+f'{float(L-S):.8f}'],r'S_{10}\approx'+f'{float(S):.8f}'+r',\quad L\approx'+f'{float(L):.8f}');records.append({'number':n,'simpson':str(S),'numeric':str(L)})
for n,f,c in[(35,x*(4-x)**Q(1,3),4),(36,x+s.sin(x),2*pi)]:
 fv=s.lambdify(x,f,'math');extras=[];steps=[];vals=[]
 for N in[1,2,4]:
  xx=[float(c)*j/N for j in range(N+1)];yy=[fv(z)for z in xx];ch=sum(math.hypot(xx[j]-xx[j-1],yy[j]-yy[j-1])for j in range(1,N+1));vals.append((N,ch));steps+=fs(r'L_{\rm poly,'+str(N)+'}='+f'{ch:.8f}')
  def interp(z,xx=xx,yy=yy):
   for j in range(len(xx)-1):
    if xx[j]<=z<=xx[j+1]:return yy[j]+(z-xx[j])*(yy[j+1]-yy[j])/(xx[j+1]-xx[j])
   return yy[-1]
  extras.append((f'{N} chords',interp))
 sp=s.sqrt(1+s.diff(f,x)**2)
 if n==35:L=mp.quad(lambda u:mp.sqrt(9*u**4+16*(1-u**3)**2),[0,mp.root(4,3)]);steps+=fs(r'u=\sqrt[3]{4-x}:\quad x=4-u^3,\ y=4u-u^4',r'L=\int_0^{\sqrt[3]4}\sqrt{9u^4+16(1-u^3)^2}\,du')
 else:L=mp.quad(s.lambdify(x,sp,'mpmath'),[0,mp.pi,2*mp.pi])
 add(n,(M('y='+s.latex(f)+r',\quad0\le x\le '+s.latex(c))+'(a)그래프 (b)등분하여1,2,4개 선분으로 근사한 길이와 경로 (c)길이 적분 (d)소수4자리 값과 비교를 구하라.',M('y='+s.latex(f)+r',\quad0\le x\le '+s.latex(c))+'(a)Graph.(b)Find and illustrate polygonal lengths for1,2,4equal subintervals.(c)Set up length integral.(d)Compute to4decimal places and compare.'),steps+fs(r'L='+s.latex(s.Integral(sp,(x,0,c))),r'L\approx'+f'{float(L):.4f}')+[('각 현의 길이는 대응 호보다 작다. 분할을 세분하면 근삿값은 감소하지 않지만 같은 직선 위에 새 점이 생기면 같을 수 있다.','Each chord is no longer than its arc. Refinement cannot decrease polygonal length, though it can leave it unchanged when the new point is collinear.')],same(M(',\quad '.join(r'L_{\rm poly,'+str(N)+'}='+f'{v:.6f}'for N,v in vals)+r';\quad L\approx'+f'{float(L):.4f}')),parts=list('abcd'));plotcurve(n,f,0,c,extra=extras);records.append({'number':n,'numeric':str(L),'polygonal':vals})
arc(37,ex(x),x,0,2,sq(1+ex(2*x)),sq(1+ex(2*x))+log(ex(x)/(1+sq(1+ex(2*x)))))
G=u*(32*u*u+9)*sq(16*u*u+9)/128-Q(81,512)*s.asinh(4*u/3);val38=s.simplify(G.subs(u,1)-G.subs(u,0))
ma(38,r'y=x^{4/3},\quad(0,0)\text{ to }(1,1)',[r'L=\int_0^1\sqrt{1+\tfrac{16}9x^{2/3}}dx',r'u=x^{1/3}\Rightarrow L=3\int_0^1u^2\sqrt{1+16u^2/9}\,du',r'\int3u^2\sqrt{1+16u^2/9}\,du='+s.latex(G)],s.latex(val38))
ma(39,r'x^{2/3}+y^{2/3}=1',[r'x=\cos^3t,\quad y=\sin^3t,\quad0\le t\le\pi/2',r'\sqrt{(dx/dt)^2+(dy/dt)^2}=3\sin t\cos t',r'L=4\int_0^{\pi/2}3\sin t\cos t\,dt=4\cdot3/2'],r'L=6')
ma(40,r'y^3=x^2;\quad(a)\text{sketch};\ (b)(0,0)\to(1,1);\ (c)(-1,1)\to(8,4)',[r'(a)y=|x|^{2/3}\text{ has a cusp at the origin}',r'(b)L=\int_0^1\sqrt{1+\tfrac49x^{-2/3}}dx=\int_0^1\sqrt{1+\tfrac94y}\,dy',r'\int\sqrt{1+\tfrac94y}dy=\frac1{27}(4+9y)^{3/2}',r'L_{(0,0)\to(1,1)}=(13\sqrt{13}-8)/27',r'(c)L=\int_0^1\sqrt{1+\tfrac94y}\,dy+\int_0^4\sqrt{1+\tfrac94y}\,dy'],r'(b)\frac{13\sqrt{13}-8}{27};\quad(c)\frac{13\sqrt{13}+80\sqrt{10}-16}{27}',parts=list('abc'))
plots(b,40,[('8.1.40 Cusp and two branches',-1,8,-.2,4.4,[('y=|x|^(2/3)',lambda x:abs(x)**(2/3))])])
ma(41,r'y=2x^{3/2},\quad P_0=(1,2):\text{ arc-length function}',[r'y^\prime=3\sqrt x,\quad ds=\sqrt{1+9x}\,dx',r's(x)=\int_1^x\sqrt{1+9t}\,dt=\frac2{27}[(1+9x)^{3/2}-10^{3/2}]'],r's(x)=\frac2{27}[(1+9x)^{3/2}-10\sqrt{10}],\quad x\ge0')
ma(42,r'y=\ln\sin x,\quad0<x<\pi,\quad P_0=(\pi/2,0)',[r'y^\prime=\cot x,\quad\sqrt{1+\cot^2x}=\csc x\quad(0<x<\pi)',r's(x)=\int_{\pi/2}^x\csc t\,dt=[\ln\tan(t/2)]_{\pi/2}^x=\ln\tan(x/2)',r'x<\pi/2:\quad s(x)=-\int_x^{\pi/2}\csc t\,dt<0',r'\text{Signed arc-length function is negative to the left; geometric distance is }|s(x)|'],r's(x)=\ln\tan(x/2)',parts=['a','b'])
plots(b,42,[('8.1.42 Curve and signed arc length',.05,float(pi)-.05,-4,4,[('ln(sin x)',lambda x:math.log(math.sin(x))),('s(x)=ln(tan(x/2))',lambda x:math.log(math.tan(x/2)))])])
ma(43,r'y=\arcsin x+\sqrt{1-x^2},\quad P_0=(0,1)',[r'y^\prime=\frac{1-x}{\sqrt{1-x^2}},\quad1+(y^\prime)^2=\frac2{1+x}',r's(x)=\int_0^x\frac{\sqrt2}{\sqrt{1+t}}dt',r's(x)=2\sqrt2(\sqrt{1+x}-1)'],r's(x)=2\sqrt2(\sqrt{1+x}-1),\quad-1\le x\le1')
x44=((mp.mpf('13.5')+5*mp.sqrt(5))**(mp.mpf(2)/3)-5)/3;y44=mp.mpf(2)/9*(3*x44+4)**mp.mpf('1.5')+mp.mpf(2)/9
ma(44,r's(x)=\int_0^x\sqrt{3t+5}dt,\quad f\text{ increasing},\ f(0)=2',[r'(a)\sqrt{1+(f^\prime)^2}=\sqrt{3x+5}\Rightarrow f^\prime=\sqrt{3x+4}',r'f(x)=\frac29(3x+4)^{3/2}+C,\quad f(0)=2\Rightarrow C=2/9',r'(b)s(x)=\frac29[(3x+5)^{3/2}-5\sqrt5]=3',r'x=\frac{(27/2+5\sqrt5)^{2/3}-5}3'],r'(a)f(x)=\frac29[(3x+4)^{3/2}+1];\quad(b)('+f'{float(x44):.3f},{float(y44):.3f}'+')',parts=['a','b'])
L45=mp.quad(lambda x:mp.sqrt(1+(2*x/45)**2),[0,90]);ma(45,r'y=180-x^2/45\text{ meters: falling prey path}',[r'y=0\Rightarrow x=90,\quad y^\prime=-2x/45',r'L=\int_0^{90}\sqrt{1+4x^2/2025}dx',r'u=2x/45\Rightarrow L=\frac{45}4[u\sqrt{1+u^2}+\operatorname{arsinh}u]_0^4'],r'L\approx'+f'{float(L45):.1f}'+r'\ \mathrm m')
L46=mp.quad(lambda x:mp.sqrt(1+((x-50)/20)**2),[0,50,80]);ma(46,r'y=150-(x-50)^2/40,\quad0\le x\le80\ \mathrm{ft}',[r'y^\prime=-(x-50)/20',r'L=\int_0^{80}\sqrt{1+(x-50)^2/400}dx',r'u=(x-50)/20\Rightarrow L=10[u\sqrt{1+u^2}+\operatorname{arsinh}u]_{-5/2}^{3/2}'],r'L\approx'+f'{float(L46):.6f}'+r'\ \mathrm{ft}')
L47=mp.quad(lambda x:mp.sqrt(1+(mp.pi/7*mp.cos(mp.pi*x/7))**2),[0,7,14,21,28]);ma(47,r'\text{Corrugated panel: projected width28in, peak-to-trough2in, two waves}',[r'\text{Amplitude}=1,\quad\text{period}=14\Rightarrow y=\sin(\pi x/7)',r'w=\int_0^{28}\sqrt{1+(\pi/7)^2\cos^2(\pi x/7)}dx',r'w\approx'+f'{float(L47):.8f}'],r'w\approx'+f'{float(L47):.4g}'+r'\ \mathrm{in}')
ma(48,r'y=a\cosh(x/a),\quad a>0,\quad c\le x\le d',[r'(a)y^\prime=\sinh(x/a),\quad\sqrt{1+(y^\prime)^2}=\cosh(x/a)',r'L=\int_c^d\cosh(x/a)dx=a[\sinh(d/a)-\sinh(c/a)]',r'(b)A=\int_c^da\cosh(x/a)dx=a^2[\sinh(d/a)-\sinh(c/a)]=aL'],r'L=a[\sinh(d/a)-\sinh(c/a)],\quad A/L=a\quad(c<d)',parts=['a','b'])
a49=mp.findroot(lambda a:2*a*mp.sinh(25/a)-51,(50,90));H49=20+a49*(mp.cosh(25/a49)-1)
ma(49,r'y=c+a\cosh(x/a),\quad-25\le x\le25,\quad L=51ft,\quad y_{\min}=20ft',[r'L=2a\sinh(25/a)=51',r'a\approx'+f'{float(a49):.9f}',r'c+a=20\Rightarrow c=20-a',r'H=20+a[\cosh(25/a)-1]'],r'H\approx'+f'{float(H49):.6f}'+r'\ \mathrm{ft}')
L50=2*mp.quad(lambda x:mp.sqrt(1+(mp.mpf('20.96')*mp.mpf('.03291765')*mp.sinh(mp.mpf('.03291765')*x))**2),[0,mp.mpf('91.20')]);ma(50,r'y=211.49-20.96\cosh(0.03291765x),\quad|x|\le91.20\ \mathrm m',[r'y^\prime=-(20.96)(0.03291765)\sinh(0.03291765x)',r'L=2\int_0^{91.20}\sqrt{1+[(20.96)(0.03291765)\sinh(0.03291765x)]^2}dx',r'L\approx'+f'{float(L50):.6f}'],r'L\approx'+str(round(float(L50)))+r'\ \mathrm m')
ma(51,r'f(x)=\tfrac14e^x+e^{-x}:\quad\text{arc length equals area on every interval}',[r'f^\prime=\tfrac14e^x-e^{-x}',r'f^2-(f^\prime)^2=4(\tfrac14e^x)e^{-x}=1',r'f>0\Rightarrow\sqrt{1+(f^\prime)^2}=f',r'L=\int_a^b\sqrt{1+(f^\prime)^2}dx=\int_a^bf(x)dx=A'],r'L=A')
ma(52,r'x^n+y^n=1,\quad n=2,4,6,8,10:\quad\text{graph, length integral, and limiting length}',[r'n=2k:\quad y=(1-x^{2k})^{1/(2k)}\quad(0\le x\le1)',r'y^\prime=-x^{2k-1}(1-x^{2k})^{1/(2k)-1}',r'L_{2k}=4\int_0^1\sqrt{1+x^{4k-2}(1-x^{2k})^{1/k-2}}dx',r'c_k=2^{-1/(2k)};\quad8\sqrt{(1-c_k)^2+c_k^2}\le L_{2k}\le8',r'c_k\to1\Rightarrow L_{2k}\to8'],r'L_{2k}=4\int_0^1\sqrt{1+x^{4k-2}(1-x^{2k})^{1/k-2}}dx;\quad\lim_{k\to\infty}L_{2k}=8')
# Equal physical scales for the closed superellipse family.
import html
out=['<svg xmlns="http://www.w3.org/2000/svg" width="560" height="580" viewBox="0 0 560 580"><rect width="100%" height="100%" fill="#f8fafc"/><text x="280" y="28" text-anchor="middle" font-family="sans-serif">8.1.52 Fat circles approach a square</text>']
colors=['#2563eb','#e11d48','#059669','#9333ea','#d97706']
for N,col in zip([2,4,6,8,10],colors):
 pts=[]
 for j in range(801):
  th=2*math.pi*j/800;xx=math.copysign(abs(math.cos(th))**(2/N),math.cos(th));yy=math.copysign(abs(math.sin(th))**(2/N),math.sin(th));pts.append(f'{280+210*xx:.3f},{270-210*yy:.3f}')
 out.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="2"/>');out.append(f'<text x="{60+100*([2,4,6,8,10].index(N))}" y="530" fill="{col}" font-family="sans-serif">n={N}</text>')
out+=['<path d="M45 270H515M280 35V505" stroke="#94a3b8"/><text x="280" y="560" text-anchor="middle" font-family="sans-serif">Square [-1,1] × [-1,1]: perimeter 8</text></svg>'];fn='s8-1-52.svg';(ROOT/'assets'/fn).write_text(''.join(out));b.E[52]['figure']={'src':'../exercise-content/assets/'+fn,'alt':pair('n=2,4,6,8,10의 닫힌 초타원','Closed superellipses for n=2,4,6,8,10'),'caption':pair('가로·세로 눈금의 물리적 크기를 같게 그렸다. 곡선은 정사각형 경계로 접근한다.','Both axes have equal physical scales. The curves approach the boundary of a square.')}
ma(53,r'y=\int_1^x\sqrt{t^3-1}\,dt,\quad1\le x\le4',[r'y^\prime=\sqrt{x^3-1}\quad\text{by the Fundamental Theorem}',r'\sqrt{1+(y^\prime)^2}=\sqrt{x^3}=x^{3/2}',r'L=\int_1^4x^{3/2}dx=\frac25[x^{5/2}]_1^4=\frac25(32-1)'],r'L=62/5')
(Path(__file__).parent/'calc1-s8-1-numeric-results.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n');b.save();print('8.1 COMPLETE',len(b.E))
