from calc1_helpers import *
from calc1_plot_helpers import plots
x=s.symbols('x',real=True);pi=mp.pi
b=CalcBook('7.7',[577,578,579,580]);records=[]
def v(z,d=6):return f'{float(z):.{d}f}'
def quad(f,a,c,n):
 a,c=mp.mpf(a),mp.mpf(c);h=(c-a)/n;ys=[f(a+j*h)for j in range(n+1)];L=h*sum(ys[:-1]);R=h*sum(ys[1:]);M=h*sum(f(a+(j+mp.mpf('.5'))*h)for j in range(n));T=(L+R)/2
 return {'L':L,'R':R,'T':T,'M':M,'S':h/3*(ys[0]+ys[-1]+4*sum(ys[1:-1:2])+2*sum(ys[2:-1:2]))if n%2==0 else None}
def add(n,st,steps,ans,ck=None,parts=[]):
 b.add(n,577 if n<=22 else 578 if n<=34 else 579 if n<=42 else 580,('수치적분','Approximate integration'),st,steps,ans,parts=parts)
 b.verify(n,*(ck or ('가중합을 고정밀도로 계산하고 독립 적분값 또는 직접 대수 전개로 확인했다.','Computed weighted sums at high precision and checked against independent integration or direct algebra.')));b.save()
def ma(n,eq,steps,ans,ck=None,parts=[]):add(n,(M(eq)+'계산하거나 설명하라.',M(eq)+'Compute or explain.'),fs(*steps),same(M(ans)),ck,parts)
form=r'h=(b-a)/n,\quad T_n=h[\tfrac12 f(a)+\sum_{j=1}^{n-1}f(a+jh)+\tfrac12f(b)],\quad M_n=h\sum_{j=0}^{n-1}f(a+(j+\tfrac12)h)'
sform=r'S_n=\frac h3[f(a)+4f(a+h)+2f(a+2h)+\cdots+4f(b-h)+f(b)]'
def table(rows,headers):return r'\begin{array}{'+'r'*len(headers)+'}'+'&'.join(headers)+r'\\\hline'+r'\\'.join('&'.join(str(t)for t in row)for row in rows)+r'\end{array}'
def dataplot(n,xs,ys,title):
 def fn(z):
  for i in range(len(xs)-1):
   if xs[i]<=z<=xs[i+1]:return ys[i]+(ys[i+1]-ys[i])*(z-xs[i])/(xs[i+1]-xs[i])
  return ys[-1]
 plots(b,n,[(title,min(xs),max(xs),min(0,min(ys))-.05*max(ys),max(ys)*1.12,[('sample interpolation',fn)],list(zip(xs,ys)))],caption=('원본에서 읽은 표본값을 이어 그린 자체 도표이며, 곡선의 정확한 식을 가정하지 않는다.','Original diagram reconstructed from read-off samples; no exact formula for the source curve is assumed.'))
add(1,('그림의 증가하고 위로 오목한 f에 대해 I=∫₀⁴f(x)dx이다. (a)L₂,R₂,M₂를 읽고 (b)과대·과소를 판단하라. (c)T₂도 구하여 비교하라. (d)모든 n에서 다섯 값을 순서대로 나열하라.','For the increasing, concave-down curve, let I=∫₀⁴f(x)dx. (a)Read L₂,R₂,M₂.(b)Classify them as under/overestimates.(c)Compute T₂ and compare.(d)Order all five quantities for any n.'),fs(r'f(0)\approx0.5,\ f(1)\approx1.7,\ f(2)\approx2.5,\ f(3)\approx3.2,\ f(4)\approx3.5',r'L_2=2(0.5+2.5)\approx6,\quad R_2=2(2.5+3.5)\approx12,\quad M_2=2(1.7+3.2)\approx9.8',r'T_2=(L_2+R_2)/2\approx9')+[('증가하므로 왼쪽합은 과소, 오른쪽합은 과대이다. 위로 오목하여 사다리꼴은 과소, 중점은 과대이다.','Increasing gives a lower left sum and upper right sum. Concavity down makes trapezoids lower and midpoints upper.')],same(M(r'L_2\approx6,\ R_2\approx12,\ M_2\approx9.8,\ T_2\approx9;\quad L_n<T_n<I<M_n<R_n')),('눈금 판독은 근삿값이다. 순서는 단조성과 엄격한 오목성으로 결정했다.','Graph readings are approximate; monotonicity and strict concavity determine the ordering.'),list('abcd'))
dataplot(1,[0,1,2,3,4],[.5,1.7,2.5,3.2,3.5],'7.7.1 Graph readings')
ma(2,r'\{L_n,R_n,T_n,M_n\}=\{0.7811,0.8675,0.8632,0.9540\},\quad f\downarrow,\ f^{\prime\prime}>0',[r'R_n<M_n<I<T_n<L_n',r'T_n=(0.7811+0.9540)/2=0.86755\approx0.8675'],r'R_n=0.7811,\ M_n=0.8632,\ T_n=0.8675,\ L_n=0.9540;\quad0.8632<I<0.8675',('표시된 수의 반올림 오차를 고려하여 평균을 확인했다.','The midpoint of the displayed extreme estimates agrees with T within their rounding precision.'),['a','b'])
dataplot(2,[0,.5,1,1.5,2],[1,.6,.35,.2,.1],'7.7.2 Decreasing convex schematic')
f=lambda x:mp.cos(x*x);r=quad(f,0,1,4)
ma(3,r'I=\int_0^1\cos(x^2)dx,\quad n=4',[form,r'f^{\prime\prime}(x)=-2\sin(x^2)-4x^2\cos(x^2)\le0\quad(0\le x\le1)',f'T_4={v(r["T"])},\\quad M_4={v(r["M"])}'],f'{v(r["T"])}<I<{v(r["M"])}',parts=['a','b'])
plots(b,3,[('7.7.3 Concavity of cos(x²)',0,1,.5,1.05,[('cos(x²)',lambda x:math.cos(x*x))])])
f=lambda x:mp.sin(x*x/2);r=quad(f,0,1,5)
add(4,(M(r'f(x)=\sin(x^2/2),\ I=\int_0^1f(x)dx')+'그래프를 [0,1]×[0,0.5]에 그려 (a)L₂,R₂,M₂,T₂의 과대·과소 (b)일반 n의 순서 (c)L₅,R₅,M₅,T₅와 최선의 값을 구하라.',M(r'f(x)=\sin(x^2/2),\ I=\int_0^1f(x)dx')+'Graph in [0,1]×[0,0.5].(a)Classify L₂,R₂,M₂,T₂.(b)Order them for general n.(c)Find L₅,R₅,M₅,T₅ and select the best.'),fs(r'f^\prime=x\cos(x^2/2)>0,\quad f^{\prime\prime}=\cos(x^2/2)-x^2\sin(x^2/2)>0',r'L_n<M_n<I<T_n<R_n',*[k+'_5='+v(r[k])for k in ['L','R','M','T']])+[('왼쪽·중점은 과소, 오른쪽·사다리꼴은 과대이다. 이 경우 실제 적분값과 비교하면 중점 M₅가 가장 정확하다.','Left and midpoint sums underestimate; right and trapezoidal sums overestimate. Comparison to the actual integral confirms M₅ is best here.')],same(M(',\quad '.join(k+'_5='+v(r[k])for k in ['L','R','M','T'])+r';\quad M_5\text{ best}')),parts=list('abc'))
plots(b,4,[('7.7.4 sin(x²/2)',0,1,0,.5,[('sin(x²/2)',lambda x:math.sin(x*x/2))])])
numrows=[(5,lambda x:x*mp.sin(x),0,pi,6,r'x\sin x',pi),(6,lambda x:x/mp.sqrt(1+x*x),0,2,8,r'x/\sqrt{1+x^2}',mp.sqrt(5)-1),(7,lambda x:mp.sqrt(1+x**3),0,1,4,r'\sqrt{1+x^3}',None),(8,lambda x:mp.sin(mp.sqrt(x)),1,4,6,r'\sin\sqrt x',None),(9,lambda x:mp.sqrt(mp.expm1(x)),0,1,10,r'\sqrt{e^x-1}',None),(10,lambda x:mp.sign(1-x*x)*abs(1-x*x)**(mp.mpf(1)/3),0,2,10,r'\sqrt[3]{1-x^2}',None),(11,lambda x:mp.exp(x+mp.cos(x)),-1,2,6,r'e^{x+\cos x}',None),(12,lambda x:mp.exp(1/x),1,3,8,r'e^{1/x}',None),(13,lambda x:mp.sqrt(x)*mp.cos(x),0,4,8,r'\sqrt y\cos y',None),(14,lambda x:1/mp.log(x),2,3,10,r'1/\ln t',None),(15,lambda x:x*x/(1+x**4),0,1,10,r'x^2/(1+x^4)',None),(16,lambda x:mp.sin(x)/x,1,3,4,r'\sin t/t',None),(17,lambda x:mp.log(1+mp.exp(x)),0,4,8,r'\ln(1+e^x)',None),(18,lambda x:mp.sqrt(x+x**3),0,1,10,r'\sqrt{x+x^3}',None)]
for n,f,a,c,N,expr,I in numrows:
 r=quad(f,a,c,N);keys=['M','S']if n<=6 else['T','M','S'];limhi=r'\pi'if n==5 else str(c);q='y'if n==13 else't'if n in[14,16]else'x';steps=fs(form,sform,'h='+v((c-a)/N),*[k+'_{'+str(N)+'}='+v(r[k])for k in keys]);ans=',\quad '.join(k+'_{'+str(N)+'}='+v(r[k])for k in keys)
 if I is not None:steps+=fs('I='+v(I),*[r'E_'+k+'=I-'+k+'_{'+str(N)+'}='+v(I-r[k])for k in keys]);ans+=r';\quad '+',\quad '.join('E_'+k+'='+v(I-r[k])for k in keys)
 add(n,(M(r'\int_'+str(a)+'^{'+limhi+'}'+expr+'d'+q+',\quad n='+str(N))+('중점·Simpson 근사와 실제 오차를 구하라.'if n<=6 else'사다리꼴·중점·Simpson 근사를 구하라.'),M(r'\int_'+str(a)+'^{'+limhi+'}'+expr+'d'+q+',\quad n='+str(N))+('Find midpoint/Simpson estimates and actual errors.'if n<=6 else'Find trapezoidal/midpoint/Simpson estimates.')),steps,same(M(ans)),parts=list('ab'if n<=6 else'abc'));records.append({'number':n,'n':N,'approximations':{k:str(r[k])for k in keys}})
# Error bounds and required mesh sizes.
def need(K,L,eps,rule):
 d,p=(12,2)if rule=='T'else(24,2)if rule=='M'else(180,4);z=(K*L**(p+1)/(d*eps))**(mp.mpf(1)/p);n=int(mp.floor(z))+1
 if rule=='S'and n%2:n+=1
 return n
for n,f,a,c,N,K,expr,Kwhy in [(19,lambda x:mp.cos(x*x),0,1,8,6,r'\cos(x^2)',r'|f^{\prime\prime}|=|{-2\sin(x^2)-4x^2\cos(x^2)}|\le6'),(20,lambda x:mp.exp(1/x),1,2,10,3*mp.e,r'e^{1/x}',r'f^{\prime\prime}=e^{1/x}(2/x^3+1/x^4)\le3e')]:
 r=quad(f,a,c,N);et=K*(c-a)**3/(12*N*N);em=et/2;nt=need(K,c-a,mp.mpf('.0001'),'T');nm=need(K,c-a,mp.mpf('.0001'),'M')
 ma(n,r'I=\int_'+str(a)+'^'+str(c)+expr+r'dx,\quad n='+str(N),[form,Kwhy,'T_{'+str(N)+'}='+v(r['T'])+',\quad M_{'+str(N)+'}='+v(r['M']),r'|E_T|\le K(b-a)^3/(12n^2),\quad|E_M|\le K(b-a)^3/(24n^2)',r'|E_T|\le'+v(et)+r',\quad |E_M|\le'+v(em)],'T_{'+str(N)+'}='+v(r['T'])+',\ M_{'+str(N)+'}='+v(r['M'])+r';\quad n_T\ge'+str(nt)+r',\ n_M\ge'+str(nm)+r'\ (\varepsilon=10^{-4})',parts=list('abc'))
f=mp.sin;r=quad(f,0,pi,10);ans=[];steps=fs(form,sform,r'I=2,\quad |f^{\prime\prime}|\le1,\quad|f^{(4)}|\le1')
for k in ['T','M','S']:
 den,p=(12,2)if k=='T'else(24,2)if k=='M'else(180,4);eb=pi**(p+1)/(den*10**p);nn=need(1,pi,mp.mpf('.00001'),k);steps+=fs(k+'_{10}='+v(r[k])+',\quad E_'+k+'='+v(2-r[k],10)+r',\quad |E_'+k+r'|\le'+v(eb,10));ans.append('n_'+k+r'\ge'+str(nn))
ma(21,r'\int_0^\pi\sin xdx:\quad\text{approximations, actual errors, bounds, and mesh for }10^{-5}',[q[0][2:-2]for q in steps],',\quad '.join(ans),parts=list('abc'))
K=76*mp.e;nn=need(K,1,mp.mpf('.00001'),'S')
ma(22,r'\int_0^1e^{x^2}dx:\quad |E_S|<10^{-5}',[r'f^{(4)}=(16x^4+48x^2+12)e^{x^2}\le76e',r'|E_S|\le\frac{76e}{180n^4}<10^{-5}',r'n>\left(\frac{76e}{180\cdot10^{-5}}\right)^{1/4},\quad n\text{ even}'],r'n\ge'+str(nn))
b.save();print('7.7 authored',len(b.E))
for n,F,a,c,K2,K4,expr in [(23,s.exp(s.cos(x)),0,2*pi,mp.mpf(3),mp.mpf(11),r'e^{\cos x}'),(24,s.sqrt(4-x**3),-1,1,mp.mpf('2.2'),mp.mpf('18.1'),r'\sqrt{4-x^3}')]:
 f=s.lambdify(x,F,'mpmath');d2=s.diff(F,x,2);d4=s.diff(F,x,4);r=quad(f,a,c,10);I=mp.quad(f,[a,(a+c)/2,c]);L=c-a;ebm=K2*L**3/2400;ebs=K4*L**5/1800000;nn=need(K4,L,mp.mpf('.0001'),'S')
 steps=fs('f^{\prime\prime}(x)='+s.latex(s.factor(d2)),'f^{(4)}(x)='+s.latex(s.factor(d4)),r'K_2='+str(K2)+r',\quad K_4='+str(K4),'M_{10}='+v(r['M'],10),'I='+v(I,10),r'|E_M|\le K_2(b-a)^3/(24\cdot10^2)='+v(ebm,10),r'|I-M_{10}|='+v(abs(I-r['M']),14),'S_{10}='+v(r['S'],10),r'|E_S|\le K_4(b-a)^5/(180\cdot10^4)='+v(ebs,10),r'|I-S_{10}|='+v(abs(I-r['S']),14),r'n>\left(\frac{K_4(b-a)^5}{180\cdot10^{-4}}\right)^{1/4},\quad n\text{ even}')
 add(n,(M(r'I=\int_{'+str(a)+'}^{'+(r'2\pi'if n==23 else'1')+'}'+expr+'dx')+'(a) f″ 그래프에서 상한 K₂를 잡고 (b)M₁₀ (c)그 오차 한계 (d)고정밀 적분값 (e)실제 오차와 비교 (f)f⁽⁴⁾ 그래프의 K₄ (g)S₁₀ (h)오차 한계 (i)실제 오차 비교 (j)Simpson 오차 0.0001을 보장하는 n을 구하라. b,d,g는 소수10자리로 쓴다.',M(r'I=\int_{'+str(a)+'}^{'+(r'2\pi'if n==23 else'1')+'}'+expr+'dx')+'(a)Bound |f″| from its graph.(b)M₁₀.(c)Its error bound.(d)High-precision integral.(e)Compare actual error.(f)Bound |f⁽⁴⁾| graphically.(g)S₁₀.(h)Its error bound.(i)Compare actual error.(j)Find even n guaranteeing Simpson error below0.0001. Use10 decimal places in b,d,g.'),steps+[('실제 오차는 두 이론적 상한보다 작다. 상한은 그래프의 극값보다 조금 크게 잡았으므로 필요한 n은 충분조건이다.','Actual errors are smaller than both theoretical bounds. Constants slightly exceed the plotted extrema, so the mesh requirement is sufficient.')],same(M('M_{10}='+v(r['M'],10)+',\quad I='+v(I,10)+',\quad S_{10}='+v(r['S'],10)+r';\quad n\ge'+str(nn))),parts=list('abcdefghij'))
 panels=[]
 for der,K,lab in [(d2,K2,'second derivative'),(d4,K4,'fourth derivative')]:
  ff=s.lambdify(x,der,'math');panels.append((f'7.7.{n} {lab}',float(a),float(c),-float(K)*1.1,float(K)*1.1,[(lab,ff),('upper bound',lambda z,k=float(K):k),('lower bound',lambda z,k=float(K):-k)]))
 plots(b,n,panels);records.append({'number':n,'I':str(I),'M10':str(r['M']),'S10':str(r['S']),'K2':str(K2),'K4':str(K4),'n':nn})
for n,f,a,c,expr,I,ns,keys in [(25,lambda x:x*mp.exp(x),0,1,r'xe^x',mp.mpf(1),[5,10,20],['L','R','T','M']),(26,lambda x:x**-2,1,2,r'x^{-2}',mp.mpf('.5'),[5,10,20],['L','R','T','M']),(27,lambda x:x**4,0,2,r'x^4',mp.mpf(32)/5,[6,12],['T','M','S']),(28,lambda x:1/mp.sqrt(x),1,4,r'x^{-1/2}',mp.mpf(2),[6,12],['T','M','S'])]:
 rows=[]
 for N in ns:
  rr=quad(f,a,c,N)
  for k in keys:rows.append([N,k,v(rr[k]),v(I-rr[k])])
 add(n,(M(r'I=\int_'+str(a)+'^'+str(c)+expr+'dx')+'표시한 n='+str(ns)+'에 대해 '+','.join(keys)+' 근사와 E=I−근사를 계산하고 n을 두 배로 할 때 오차 변화를 설명하라.',M(r'I=\int_'+str(a)+'^'+str(c)+expr+'dx')+'For n='+str(ns)+', compute '+','.join(keys)+' estimates and signed errors E=I−estimate; describe the change when n doubles.'),fs(form,sform,'I='+str(I),table(rows,['n','Q','Q_n','E_Q']))+[('n을 두 배로 하면 끝점법의 오차는 대략1/2, 사다리꼴·중점법은 대략1/4로 감소한다. Simpson법은 대략1/16로 감소한다. 이 비율은 점근적이며, x⁴의 Simpson 오차에서는 정확히1/16이다.','Doubling n roughly halves endpoint errors, quarters trapezoidal/midpoint errors, and divides Simpson errors by16. These are asymptotic ratios; the Simpson ratio for x⁴ is exactly1/16.')],same(M(table(rows,['n','Q','Q_n','E_Q']))))
xs=[i/2 for i in range(13)];ys=[2,1.25,1,1.6,3,4.6,5,4.7,4,3.3,3,3.2,4];h=1;T=(ys[0]+ys[-1])/2+sum(ys[2:-1:2]);MM=sum(ys[1::2]);S=(ys[0]+ys[-1]+4*sum(ys[2:-1:4])+2*sum(ys[4:-1:4]))/3
ma(29,r'\text{Graph on }[0,6]:\quad n=6,\ T_6,M_6,S_6',[table(list(zip(xs,ys)),['x','f(x)\text{ approx}']),form,sform],f'T_6\\approx{v(T)},\\quad M_6\\approx{v(MM)},\\quad S_6\\approx{v(S)}',('0.5 간격의 눈금 판독값을 명시했다. 그래프 판독 오차 때문에 다른 가까운 답도 가능하다.','Explicit half-unit graph readings are used; nearby estimates may differ because the curve is read graphically.'),list('abc'));dataplot(29,xs,ys,'7.7.29 Read-off ordinates')
def simpson_data(ys,h):return mp.mpf(str(h))/3*(mp.mpf(str(ys[0]))+mp.mpf(str(ys[-1]))+4*sum(mp.mpf(str(y))for y in ys[1:-1:2])+2*sum(mp.mpf(str(y))for y in ys[2:-1:2]))
ys=[0,6.2,7.2,6.8,5.6,5,4.8,4.8,0];val=simpson_data(ys,2)
ma(30,r'\text{Pool widths at }x=0,2,\ldots,16\text{ m}:\quad'+str(ys),[r'\Delta x=2,\quad n=8,\quad A\approx S_8',sform,r'A\approx\frac23[4(6.2+6.8+5.0+4.8)+2(7.2+5.6+4.8)]'],r'A\approx'+v(val)+r'\ \mathrm{m}^2');dataplot(30,list(range(0,17,2)),ys,'7.7.30 Pool width samples (m)')
ys31=[2.4,2.9,3.3,3.6,3.8,4,4.1,3.9,3.5];val31=sum(ys31[1::2]);eb31=3*4**3/(24*4**2)
ma(31,r'\int_1^5f(x)dx,\quad -2\le f^{\prime\prime}\le3',[table(list(zip([1+i/2 for i in range(9)],ys31)),['x','f(x)']),r'(a)\quad M_4=1[f(1.5)+f(2.5)+f(3.5)+f(4.5)]=2.9+3.6+4.0+3.9',r'(b)\quad K_2=3,\quad |E_M|\le3(5-1)^3/(24\cdot4^2)'],r'M_4=14.4,\quad|E_M|\le0.5',parts=['a','b'])
ys32=[12.1,11.6,11.3,11.1,11.7,12.2,12.6,13,13.2];val32=simpson_data(ys32,'.2');eb32=5*mp.mpf('1.6')**5/(180*8**4)
ma(32,r'\int_0^{1.6}g(x)dx,\quad -5\le g^{(4)}\le2',[table(list(zip([i/5 for i in range(9)],ys32)),['x','g(x)']),sform,r'n=8,\quad h=0.2,\quad K_4=5',r'|E_S|\le5(1.6)^5/(180\cdot8^4)'],r'S_8\approx'+v(val32)+r',\quad |E_S|\le'+v(eb32,9),parts=['a','b'])
ys33=[67,65.5,64.5,61.5,67,72,75,77.5,79,75.5,75.5,71.5,68];val33=simpson_data(ys33,2)/24
ma(33,r'\text{Average daily temperature, Simpson }n=12',[table(list(zip(range(0,25,2),ys33)),['t\ (\mathrm{h})','T\ ({}^\circ F)']),r'T_{\rm avg}=\frac1{24}\int_0^{24}T(t)dt\approx S_{12}/24',sform],r'T_{\rm avg}\approx'+v(val33)+r'\ {}^\circ F',('2시간 간격으로 읽은 온도이며 그래프 판독에 따른 근삿값이다. 평균은 누적 온도를24시간으로 나눈 값이다.','Temperatures are approximate two-hour graph readings; divide the temperature integral by24hours.'));dataplot(33,list(range(0,25,2)),ys33,'7.7.33 Temperature readings (F)')
ys34=[0,4.67,7.34,8.86,9.73,10.22,10.51,10.67,10.76,10.81,10.81];val34=simpson_data(ys34,'.5')
ma(34,r'\text{Runner distance over }0\le t\le5\ \mathrm{s}',[table(list(zip([i/2 for i in range(11)],ys34)),['t\ (s)','v\ (m/s)']),r'd=\int_0^5v(t)dt,\quad h=0.5,\quad n=10',sform],r'd\approx'+v(val34)+r'\ \mathrm{m}')
ys35=[0,.6,4,10,13,9.5,0];val35=simpson_data(ys35,1)
ma(35,r'\text{Acceleration graph in ft/s}^2\text{: velocity increase over6s}',[table(list(zip(range(7),ys35)),['t\ (s)','a\ (ft/s^2)']),r'\Delta v=\int_0^6a(t)dt\approx S_6',sform],r'\Delta v\approx'+v(val35)+r'\ \mathrm{ft/s}',('1초 간격의 그래프 판독값으로 계산했다. 가속도의 적분은 속도 증가량이다.','Used one-second graph readings; integrating acceleration gives the increase in velocity.'));dataplot(35,list(range(7)),ys35,'7.7.35 Acceleration readings')
ys36=[4,3,2.4,1.9,1.5,1.15,1];val36=simpson_data(ys36,1)
ma(36,r'\text{Leak rate }r(t)\text{ L/h over first6h}',[table(list(zip(range(7),ys36)),['t\ (h)','r\ (L/h)']),r'V=\int_0^6r(t)dt\approx S_6',sform],r'V\approx'+v(val36)+r'\ \mathrm{L}',('본문의 L/h와6시간에 맞추어 t를 시간으로 해석했다. 원본 그래프의 seconds 표기는 본문과 모순되는 단위 오기이다.','Used hours, consistent with the stated L/h rate and six-hour interval. The source graph’s seconds label conflicts with the problem text.'));dataplot(36,list(range(7)),ys36,'7.7.36 Leak-rate samples, t in hours')
ys37=[1814,1735,1686,1646,1637,1609,1604,1611,1621,1666,1745,1886,2052];val37=simpson_data(ys37,'.5')
ma(37,r'\text{Energy consumed from midnight to6AM}',[table(list(zip([i/2 for i in range(13)],ys37)),['t\ (h)','P\ (MW)']),r'E=\int_0^6P(t)dt,\quad h=0.5,\quad n=12',sform],r'E\approx'+v(val37)+r'\ \mathrm{MWh}')
ys38=[.35,.31,.4,.49,.5,.56,.55,.82,.88];val38=simpson_data(ys38,1)*3600
ma(38,r'\text{Data transmitted over8h; }D\text{ in megabits/s}',[table(list(zip(range(9),ys38)),['t\ (h)','D\ (Mb/s)']),r'B=3600\int_0^8D(t)dt\approx3600S_8',sform],r'B\approx'+v(val38)+r'\ \mathrm{megabits}',('시간축은 시간, 전송률은 초당 메가비트이므로3600을 곱했다. 판독값의 근사 정확도만 의미가 있다.','The horizontal axis is hours but rates are megabits/second, requiring the factor3600. Accuracy is limited by graph readings.'));dataplot(38,list(range(9)),ys38,'7.7.38 Throughput readings (Mb/s)')
xs39=list(range(2,11));ys39=[0,1.5,1.9,2.2,3,3.8,4,3.1,0];Va=pi*simpson_data([y*y for y in ys39],1);Vb=2*pi*simpson_data([x*y for x,y in zip(xs39,ys39)],1)
ma(39,r'\text{Rotate the region }2\le x\le10\text{ about (a)x-axis (b)y-axis; }n=8',[table(list(zip(xs39,ys39)),['x','y\text{ approx}']),r'(a)V_x=\pi\int_2^{10}y^2dx\approx\pi S_8[y^2]',r'(b)V_y=2\pi\int_2^{10}xy\,dx\approx2\pi S_8[xy]',sform],r'V_x\approx'+v(Va)+r',\quad V_y\approx'+v(Vb),('同じ'.replace('同じ','')+'同'.replace('同','')+'같은 판독 높이를 제곱한 원판과 x를 곱한 껍질에 각각 사용했다.','Used the same read-off heights in squared disk radii and radius-weighted shells.'),['a','b']);dataplot(39,xs39,ys39,'7.7.39 Region height samples')
ys40=[9.8,9.1,8.5,8,7.7,7.5,7.4];val40=simpson_data(ys40,3)
ma(40,r'\text{Work for motion over18m}',[table(list(zip(range(0,19,3),ys40)),['x\ (m)','f\ (N)']),r'W=\int_0^{18}f(x)dx,\quad h=3,\quad n=6',sform],r'W\approx'+v(val40)+r'\ \mathrm{J}')
f=lambda x:1/(1+mp.exp(-x))**2;rr=quad(f,0,10,10)
ma(41,r'y=(1+e^{-x})^{-1},\quad0\le x\le10;\quad\text{rotate about x-axis}',[r'V=\pi\int_0^{10}\frac{dx}{(1+e^{-x})^2}',r'h=1,\quad n=10',sform],r'V\approx\pi S_{10}='+v(pi*rr['S']))
k=mp.sin(21*pi/180);f=lambda x:1/mp.sqrt(1-k*k*mp.sin(x)**2);rr=quad(f,0,pi/2,10);P=4/mp.sqrt(mp.mpf('9.8'))*rr['S']
ma(42,r'T=4\sqrt{L/g}\int_0^{\pi/2}\frac{dx}{\sqrt{1-k^2\sin^2x}},\quad k=\sin(\theta_0/2),\ L=1m,\ \theta_0=42^\circ',[r'g=9.8\ \mathrm{m/s^2},\quad k=\sin21^\circ,\quad h=\pi/20',sform,r'T\approx4S_{10}/\sqrt{9.8}'],r'T\approx'+v(P)+r'\ \mathrm{s}',('중력가속도9.8m/s²를 명시했다. 소진폭 주기2π/√g보다 조금 큰 결과인지 확인했다.','Explicitly used g=9.8m/s² and checked that the period slightly exceeds the small-amplitude value2π/√g.'))
N=10000;lam=mp.mpf('632.8e-9');d=mp.mpf('1e-4')
def light(th):
 k=pi*N*d*mp.sin(th)/lam
 return N*N*(mp.sin(k)/k)**2 if k else mp.mpf(N*N)
rr=quad(light,-mp.mpf('1e-6'),mp.mpf('1e-6'),10)
ma(43,r'I(\theta)=N^2(\sin k/k)^2,\ k=\pi Nd\sin\theta/\lambda,\ N=10^4,\ d=10^{-4}m,\ \lambda=632.8\cdot10^{-9}m',[r'h=2\cdot10^{-7},\quad \theta_j=-10^{-6}+(j+1/2)h,\quad j=0,\ldots,9',r'\int_{-10^{-6}}^{10^{-6}}I(\theta)d\theta\approx h\sum_{j=0}^9I(\theta_j)',r'I(0)=N^2\quad\text{by continuous extension}'],r'M_{10}\approx'+v(rr['M']),('각도는 라디안이다. 대칭 표본을 짝지어 동일 합을 독립적으로 확인했다.','Angles are radians; paired symmetric samples independently reproduce the weighted sum.'))
ma(44,r'\int_0^{20}\cos(\pi x)dx,\quad T_{10}',[r'h=2,\quad f(2j)=\cos(2j\pi)=1',r'T_{10}=2(1/2+9+1/2)=20',r'I=[\sin(\pi x)/\pi]_0^{20}=0'],r'T_{10}=20,\quad I=0,\quad E_T=-20',('모든 표본점이 진동의 꼭대기에 놓여 상쇄되는 음의 부분을 놓친다.','Every sample lands at an oscillation maximum, missing the negative portions that cancel the positive ones.'))
ma(45,r'\text{Find continuous }f\text{ on }[0,2]\text{ with }|E_T|<|E_M|\text{ for }n=2',[r'f(x)=2+\cos(2\pi x)-\cos(4\pi x)',r'I=4,\quad f(0)=f(1)=f(2)=2\Rightarrow T_2=4',r'f(1/2)=f(3/2)=0\Rightarrow M_2=0'],r'f(x)=2+\cos(2\pi x)-\cos(4\pi x);\quad |E_T|=0<4=|E_M|')
plots(b,45,[('7.7.45 Trapezoids can outperform midpoints',0,2,-.1,4.5,[('f',lambda x:2+math.cos(2*math.pi*x)-math.cos(4*math.pi*x))])])
ma(46,r'\text{Find continuous }f\text{ on }[0,2]\text{ with }|E_R|<|E_S|\text{ for }n=2',[r'f(x)=1+\cos(\pi x),\quad I=2',r'f(0)=2,\quad f(1)=0,\quad f(2)=2',r'R_2=0+2=2,\quad S_2=(2+4\cdot0+2)/3=4/3'],r'f(x)=1+\cos(\pi x);\quad |E_R|=0<2/3=|E_S|')
plots(b,46,[('7.7.46 Right endpoints can outperform Simpson',0,2,-.1,2.2,[('1+cos(pi x)',lambda x:1+math.cos(math.pi*x))])])
add(47,(M(r'f>0,\ f^{\prime\prime}<0\text{ on }[a,b]')+'Tₙ<∫f<Mₙ을 증명하라.',M(r'f>0,\ f^{\prime\prime}<0\text{ on }[a,b]')+'Prove Tₙ<∫f<Mₙ.'),[('각 소구간에서 엄격히 오목한 곡선은 양 끝을 잇는 현보다 위에 놓인다. 적분하면 해당 사다리꼴 넓이보다 크다.','On each subinterval a strictly concave curve lies above its endpoint chord, so its integral exceeds the trapezoid area.'),('중점 m에서의 접선은 곡선보다 위에 놓인다. f(x)≤f(m)+f′(m)(x−m)를 적분하면 홀함수 항이 사라져 구간 적분<hf(m)이다.','The tangent at midpoint m lies above the curve. Integrating f(x)≤f(m)+f′(m)(x−m) cancels the odd term and gives integral<hf(m).'),('모든 소구간의 엄격한 부등식을 더한다.','Sum the strict inequalities over all subintervals.')],same(M(r'T_n<\int_a^bf(x)dx<M_n')))
ma(48,r'\text{Simpson exactness for degree}\le3;\quad S_4\text{ for }\int_0^8(x^3-6x^2+4x)dx',[r'(a)\quad f(m+t)=A+Bt+Ct^2+Dt^3',r'\int_{-h}^hf(m+t)dt=2hA+\frac23Ch^3=\frac h3[f(m-h)+4f(m)+f(m+h)]',r'(b)\quad f(0),f(2),f(4),f(6),f(8)=0,-8,-16,24,160',r'S_4=\frac23[0+4(-8)+2(-16)+4(24)+160]=128',r'I=[x^4/4-2x^3+2x^2]_0^8=128',r'(c)\quad f^{(4)}=0\Rightarrow K_4=0\Rightarrow |E_S|\le0'],r'S_4=I=128;\quad\text{all polynomials of degree}\le3\text{ are exact}',parts=list('abc'))
ma(49,r'\tfrac12(T_n+M_n)=T_{2n}',[r'h=(b-a)/n,\quad x_j=a+jh,\quad m_j=(x_j+x_{j+1})/2',r'\frac{T_n+M_n}2=\frac h4[f(x_0)+2\sum_{j=1}^{n-1}f(x_j)+2\sum_{j=0}^{n-1}f(m_j)+f(x_n)]',r'\text{Refined mesh has spacing }h/2\text{ and nodes }x_0,m_0,x_1,m_1,\ldots,x_n'],r'\tfrac12(T_n+M_n)=T_{2n}')
ma(50,r'\tfrac13T_n+\tfrac23M_n=S_{2n}',[r'h=(b-a)/n,\quad x_j=a+jh,\quad m_j=(x_j+x_{j+1})/2',r'\frac13T_n+\frac23M_n=\frac h6[f(x_0)+2\sum_{j=1}^{n-1}f(x_j)+4\sum_{j=0}^{n-1}f(m_j)+f(x_n)]',r'S_{2n}\text{ uses spacing }h/2\text{ and factor }(h/2)/3=h/6'],r'\tfrac13T_n+\tfrac23M_n=S_{2n}')
# State all requested error tasks explicitly in the two mesh-bound exercises.
for n in [19,20]:
 for lang,txt in [('ko','(a)표시한 n의 사다리꼴·중점 근사 (b)각 오차 한계 (c)오차0.0001을 보장할 n을 구하라.'),('en','(a)Find trapezoidal/midpoint estimates at the specified n.(b)Bound their errors.(c)Choose n guaranteeing error below0.0001.')]:b.E[n]['statement'][lang]+=txt
(Path(__file__).parent/'calc1-s7-7-numeric-results.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
b.save();print('7.7 COMPLETE',len(b.E))
