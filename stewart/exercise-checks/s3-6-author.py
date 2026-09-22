import json,math,html,sys,re
from pathlib import Path
import sympy as S
import mpmath as mp
BASE=Path(__file__).resolve().parents[1];items=[];mp.mp.dps=60;x=S.symbols('x',real=True)
def M(s):return r'\('+s+r'\)'
def bi(k,e=None):return {'ko':k,'en':k if e is None else e}
def calc(q,eq,tk,te,lines,ans,k='',e='',sub=''):
 p=263 if q<=10 else 264
 st=[M(t)for t in lines];items.append(dict(id=f'stewart9-exercise-3.6-{q}',number=q,subparts=list(sub),source=dict(printedPage=p,pdfPage=p+37),topic=bi('미적분과 기술을 이용한 그래프','Graphing with calculus and technology'),statement=bi(M(eq)+' '+tk,M(eq)+' '+te),hint=bi('최고차항과 한쪽 극한을 살피고 제곱근에서는 절댓값을 유지한다.','Inspect leading terms and one-sided limits; retain absolute values when extracting square roots.'),steps=bi(st+([k]if k else[]),st+([e]if e else[])),answer=bi(M(ans)),check=bi('극한의 방향·정의역·부호를 확인하고 식 또는 도형의 조건을 대조했다.','Limit direction, domain, and signs were checked against the formula or geometric conditions.'),conceptHref='../../calc1/index.html',status='math-verified'))
def plot(q,panels,caption=None):
 out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 {430*len(panels)}"><rect width="680" height="{430*len(panels)}" fill="white"/>']
 for idx,(title,curves,xlim,ylim)in enumerate(panels):
  xa,xb=xlim;ya,yb=ylim;off=430*idx;X=lambda z:65+555*(z-xa)/(xb-xa);Y=lambda z:off+345-290*(z-ya)/(yb-ya)
  out.append(f'<defs><clipPath id="v{idx}"><rect x="65" y="{off+55}" width="555" height="290"/></clipPath></defs><text x="65" y="{off+28}" font-size="15">{html.escape(title)}</text><path d="M65 {Y(max(ya,min(yb,0)))}H620M{X(max(xa,min(xb,0)))} {off+55}V{off+345}" stroke="#a3abb6" fill="none"/>')
  for j,(label,fn,breaks)in enumerate(curves):
   c=['#146db4','#c84c46','#258a64','#8e57a8','#b28627'][j%5];pts=[];last=None
   def flush():
    if pts:out.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{c}" stroke-width="2.2" clip-path="url(#v{idx})"/>');pts.clear()
   for i in range(901):
    z=xa+(xb-xa)*i/900
    if last is not None and any(last<=a<=z for a in breaks):flush()
    try:v=float(fn(z));valid=math.isfinite(v)
    except (ValueError,ZeroDivisionError,OverflowError,TypeError):valid=False
    if valid:pts.append(f'{X(z):.3f},{Y(v):.3f}')
    else:flush()
    last=z
   flush();out.append(f'<text x="{65+(j%3)*195}" y="{off+390+(j//3)*18}" fill="{c}" font-size="11">{html.escape(label)}</text>')
  for i in range(5):
   z=xa+(xb-xa)*i/4;v=ya+(yb-ya)*i/4;out.append(f'<text x="{X(z)-12}" y="{off+364}" font-size="10">{z:.5g}</text><text x="3" y="{Y(v)+4}" font-size="10">{v:.5g}</text>')

 if q==-999:out.append('<circle cx="342.5" cy="1060" r="4" fill="#c84c46"/><text x="350" y="1054" font-size="12">F(0)=0</text>')
 out.append('</svg>');p=BASE/f'exercise-content/assets/s3-6-{q}.svg';p.write_text(''.join(out));ex=next(e for e in items if e['number']==q);ex['figure']={'src':f'../exercise-content/assets/{p.name}','alt':bi('함수와 극한 또는 점근선의 자체 도해','Original plot illustrating functions, limits, or asymptotes'),'caption':caption or bi('풀이의 식에서 직접 계산한 자체 그래프.','Original plots computed directly from the solution formulas.')}
def roots_poly(expr):
 num=S.fraction(S.cancel(expr))[0];p=S.Poly(num,x)
 return [mp.mpf(str(S.N((a+b)/2,60)))for (a,b),m in p.intervals(eps=S.Rational(1,10**30))]
def show(v):
 if v==mp.inf:return r'\infty'
 if v==-mp.inf:return r'-\infty'
 return f'{float(v):.8f}'
def ivs(rows):return r'\cup'.join('('+show(a)+','+show(b)+')'for a,b in rows)or r'\varnothing'
def scanroot(fn,a,b,N=5000):
 found=[];prev=mp.mpf(a);pv=fn(prev)
 for j in range(1,N+1):
  z=mp.mpf(a)+(mp.mpf(b)-a)*j/N;v=fn(z)
  if v==0:r=z
  elif pv*v<0:
   lo,hi=prev,z;vlo=pv
   for k in range(130):
    m=(lo+hi)/2;vm=fn(m)
    if vlo*vm<=0:hi=m
    else:lo=m;vlo=vm
   r=(lo+hi)/2
  else:prev=z;pv=v;continue
  if not found or abs(r-found[-1])>mp.mpf('1e-15'):found.append(r)
  prev=z;pv=v
 return found
def analyze(q,eq,fn,d1,d2,crit,infzeros,domains,breaks,fexpr=None,extra=None,windows=None,derivative=True):
 pos=[];neg=[];cu=[];cd=[];ext=[];infl=[]
 for a,b in domains:
  for der,zeros,pp,nn,isfirst in [(d1,crit,pos,neg,True),(d2,infzeros,cu,cd,False)]:
   inside=sorted(z for z in zeros if a<z<b);cuts=[a]+inside+[b]
   signs=[]
   for lo,hi in zip(cuts,cuts[1:]):
    z=hi-1 if lo==-mp.inf else lo+1 if hi==mp.inf else(lo+hi)/2;sgn=mp.sign(der(z));signs.append(sgn);(pp if sgn>0 else nn).append((lo,hi))
   for j,z in enumerate(inside):
    if signs[j]*signs[j+1]<0:
     if isfirst:ext.append((z,'max'if signs[j]>0 else'min'))
     else:infl.append(z)
 lines=[]
 if fexpr is not None:lines=[r'f^{\prime}='+S.latex(S.factor(S.diff(fexpr,x))),r'f^{\prime\prime}='+S.latex(S.factor(S.diff(fexpr,x,2)))]
 lines+=[r'\text{Domain interiors: }'+ivs(domains),r'\text{Increasing: }'+ivs(pos)+r';\quad\text{decreasing: }'+ivs(neg),r'\text{Concave up: }'+ivs(cu)+r';\quad\text{concave down: }'+ivs(cd),r'\text{Local extrema: }'+(r';\quad '.join(r'\text{'+kind+'}('+show(z)+','+show(fn(z))+')'for z,kind in ext)or r'\text{none}'),r'\text{Inflections: }'+(r',\quad '.join('('+show(z)+','+show(fn(z))+')'for z in infl)or r'\text{none}')]
 if not derivative:
  lines=[line for line in lines if 'Local extrema' in line]
 if extra:lines+=extra
 calc(q,eq,'함수와 두 도함수의 그래프를 사용하여 중요한 세부 구간을 확대하고 증가·감소, 극값, 오목성, 변곡점을 구하라.'if derivative else'점근선과 교점으로 먼저 손 개형을 예상한 뒤 수치 그래프로 확대하여 극값을 추정하라.','Graph the function and its first two derivatives, zoom into important details, and find monotonicity, extrema, concavity, and inflections.'if derivative else'Use asymptotes and intercepts for an initial hand sketch, then zoom with numerical plots to estimate extrema.',lines,r'\text{The intervals, extrema, and inflection coordinates listed above determine the plotted curve.}','수치 좌표는 근삿값이다. 분모가 영인 곳과 정의역의 틈을 가로질러 그래프를 연결하지 않는다.','Numerical coordinates are estimates. Plots are split at poles and gaps in the domain.')
 if windows is None:
  allz=[float(z)for z in crit+infzeros+breaks if mp.isfinite(z)];lo=min(allz+[0])-2;hi=max(allz+[0])+2;vv=[]
  for j in range(401):
   z=lo+(hi-lo)*j/400
   try:v=float(fn(z))
   except:continue
   if math.isfinite(v):vv.append(v)
  vv.sort();yl=vv[len(vv)//20];yh=vv[len(vv)*19//20];pad=max(.1,(yh-yl)*.12);windows=[('Function overview',[lo,hi],[yl-pad,yh+pad])]
 panels=[(title,[('f',fn,[float(z)for z in breaks])],xl,yl)for title,xl,yl in windows]
 if derivative:
  xl=[min(win[1][0]for win in windows),max(win[1][1]for win in windows)]
  for title,df in [("First derivative",d1),("Second derivative",d2)]:
   vals=[]
   for j in range(401):
    z=xl[0]+(xl[1]-xl[0])*j/400
    try:v=float(df(z))
    except:continue
    if math.isfinite(v):vals.append(v)
   vals.sort();yl=vals[len(vals)//10];yh=vals[len(vals)*9//10];pad=max(.1,(yh-yl)*.1);panels.append((title,[(title,df,[float(z)for z in breaks])],xl,[min(-pad,yl-pad),max(pad,yh+pad)]))
 plot(q,panels)
 return ext,infl
records={}
functions={1:x**5-5*x**4-x**3+28*x*x-2*x,2:-2*x**6+5*x**5+140*x**3-110*x*x,3:x**6-5*x**5+25*x**3-6*x*x-48*x,4:(x**4-x**3-8)/(x*x-x-6),5:x/(x**3+x*x+1),9:1+1/x+8/x**2+1/x**3,10:x**-8-2*10**8*x**-4,11:(x+4)*(x-3)**2/(x**4*(x-1)),12:(2*x+3)**2*(x-2)**5/(x**3*(x-5)**2),13:x*x*(x+1)**3/((x-2)**2*(x-4)**4),14:(2*x+3)**2*(x-2)**5/(x**3*(x-5)**2),15:(x**3+5*x*x+1)/(x**4+x**3-x*x+2)}
windows={1:[('Overview',[-2.5,5],[-20,70]),('Small minimum near zero',[-.12,.2],[-.06,.7]),('Close positive extrema',[2.5,3],[56.6,56.95])],2:[('Overview',[-2,5],[-800,1400]),('Small turning points',[0,.9],[-15,12])],3:[('Overview',[-2,4.2],[-55,50]),('Close right extrema',[2.35,2.9],[-11.5,-10.9])],4:[('All branches',[-6,7],[-20,65]),('Three central turns',[-1.4,1.4],[1.2,1.8])],5:[('Overview',[-5,4],[-2,2]),('Positive peak',[0,2],[0,.5])],9:[('Wide tail',[-25,5],[-.2,3]),('Features near zero',[-1,.2],[-1,70])],10:[('Narrow scale',[-.035,.035],[-1.1e16,1e16]),('Outer approach to zero',[-.2,.2],[-1e14,1e14])],11:[('Left small maximum',[-12,-2],[-.02,.025]),('Negative middle maximum',[.2,.98],[-2000,-250]),('Right zero and maximum',[1.5,10],[-.003,.04])],12:[('Overview',[-5,8],[-500,500]),('Flat zero at x=-1.5',[-2,-1],[-.1,1]),('Flat zero at x=2',[1,3],[-1,1]),('Positive branch minimum',[6,12],[550,1200])],13:[('Far left minimum',[-100,1],[-.03,.005]),('Tiny left maximum',[-1.3,.3],[-.00003,.00003]),('Central minimum',[2.1,3.9],[0,1200])],14:[('Overview',[-5,8],[-500,800]),('Flat left feature',[-2,-1],[-.1,1]),('Positive branch minimum',[6,12],[550,1200])],15:[('Overview',[-4,4],[-1,8]),('Far left minimum',[-25,-4],[-.065,.02])]}
for q,f in functions.items():
 d=S.diff(f,x);dd=S.diff(f,x,2);fn=S.lambdify(x,f,'mpmath');d1=S.lambdify(x,d,'mpmath');d2=S.lambdify(x,dd,'mpmath');crit=roots_poly(d);infl=roots_poly(dd);poles=roots_poly(S.denom(S.cancel(f)));bs=[-mp.inf]+poles+[mp.inf];domains=list(zip(bs,bs[1:]));extra=[]
 if q==3:extra.append(r'\text{Repeated stationary roots are included even when no extremum occurs.}')
 if q in [9,10]:
  extra +=[r'\text{Exact critical inputs: }'+S.latex(S.solve(S.fraction(S.factor(d))[0],x)),r'\text{Exact second-derivative zeros: }'+S.latex(S.solve(S.fraction(S.factor(dd))[0],x))]
 if q==9:extra +=[r'a=-8-\sqrt{61},\quad b=-8+\sqrt{61},\quad u=-12-\sqrt{138},\quad v=-12+\sqrt{138}',r'\text{Increasing }(a,b);\quad\text{decreasing }(-\infty,a),(b,0),(0,\infty)',r'\text{Concave up }(u,v),(0,\infty);\quad\text{concave down }(-\infty,u),(v,0)']
 if q==10:extra +=[r'a=1/100,\quad b=(9/(5\cdot10^8))^{1/4}',r'\text{Increasing }(-a,0),(a,\infty);\quad\text{decreasing }(-\infty,-a),(0,a)',r'\text{Concave up }(-b,0),(0,b);\quad\text{concave down }(-\infty,-b),(b,\infty)']
 if q in [11,12]:
  extra=[r'\text{Zeros with multiplicities: }'+S.latex(S.roots(S.numer(S.factor(f)),x)),r'\text{Vertical asymptotes: }'+','.join('x='+show(z)for z in poles),rf'\lim_{{x\to-\infty}}f={S.latex(S.limit(f,x,-S.oo))},\quad\lim_{{x\to\infty}}f={S.latex(S.limit(f,x,S.oo))}']
 if q==13:extra.append(r'\text{The tiny left maximum requires its own vertical scale.}')
 ext,inf=analyze(q,'f(x)='+S.latex(f),fn,d1,d2,crit,infl,domains,poles,f,extra,windows[q],q not in[11,12]);records[q]={'critical':[str(v)for v in crit],'inflections':[str(v)for v in inf],'poles':[str(v)for v in poles]}
for q,f,lo,hi,poles,win in [(6,6*S.sin(x)-x*x,-5,3,[],[('Full interval',[-5,3],[-22,4]),('Two close left extrema',[-3.1,-2.5],[-10.2,-9.8])]),(7,6*S.sin(x)+S.cot(x),-mp.pi,mp.pi,[0],[('All branches',[-math.pi+.001,math.pi-.001],[-12,12])]),(8,S.sin(x)/x,-2*mp.pi,2*mp.pi,[0],[('Sinc function',[-2*math.pi,2*math.pi],[-.3,1.1])])]:
 fn=S.lambdify(x,f,'mpmath');d1=S.lambdify(x,S.diff(f,x),'mpmath');d2=S.lambdify(x,S.diff(f,x,2),'mpmath');cuts=[mp.mpf(lo)]+[mp.mpf(z)for z in poles]+[mp.mpf(hi)];domains=list(zip(cuts,cuts[1:]));cr=[];ir=[]
 for a,b in domains:
  delta=mp.mpf('1e-8');cr+=scanroot(d1,a+delta,b-delta,3000);ir+=scanroot(d2,a+delta,b-delta,3000)
 extra=[r'\text{The stated finite-domain endpoints are included wherever the formula is defined.}']
 if q==6:extra +=[rf'f(-5)={show(fn(-5))},\quad f(3)={show(fn(3))};\quad\text{{absolute minimum at }}x=-5,\quad\text{{absolute maximum at }}x={show(cr[-1])}']
 if q==8:extra+=[r'x=0\notin D,\quad\lim_{x\to0}\sin x/x=1\text{ is a removable hole, not a maximum of this domain};\quad f(\pm2\pi)=0;\quad\sup f=1\text{ is not attained}']
 if q==7:extra+=[r'\text{Vertical poles at }x=-\pi,0,\pi;\quad\text{all excluded}']
 ext,inf=analyze(q,'f(x)='+S.latex(f)+r',\quad '+(r'-5\le x\le3'if q==6 else r'-\pi\le x\le\pi'if q==7 else r'-2\pi\le x\le2\pi'),fn,d1,d2,cr,ir,domains,poles,f,extra,win);records[q]={'critical':[str(z)for z in cr],'inflections':[str(z)for z in inf]}
# Fractional-power function: rational logarithmic derivatives avoid complex-root branches.
D=1+x+x**4;g=S.Rational(2,3)/x-S.diff(D,x)/D;g2=S.factor(g*g+S.diff(g,x));f16=lambda z:abs(z)**(mp.mpf(2)/3)/(1+z+z**4);d16=lambda z:f16(z)*S.lambdify(x,g,'mpmath')(z);dd16=lambda z:f16(z)*S.lambdify(x,g2,'mpmath')(z);cr=roots_poly(g);ir=roots_poly(g2)
ext,inf=analyze(16,r'f(x)=x^{2/3}/(1+x+x^4)',f16,d16,dd16,cr,ir,[(-mp.inf,0),(0,mp.inf)],[0],None,[r'D=\mathbb R,\quad f(0)=0\text{ is a cusp minimum}',r'f^{\prime}=f\left[\frac2{3x}-\frac{1+4x^3}{1+x+x^4}\right]\quad(x\ne0)',r'f^{\prime\prime}=f\left[\left(\frac2{3x}-\frac{1+4x^3}{1+x+x^4}\right)^2-\frac2{3x^2}-\frac{12x^2(1+x+x^4)-(1+4x^3)^2}{(1+x+x^4)^2}\right]',r'1+x+x^4>0\text{ for all }x;\quad\lim_{x\to\pm\infty}f=0'],[('Fractional-power curve',[-3,3],[-.05,1.8])]);records[16]={'critical':[str(z)for z in cr]+['0'],'inflections':[str(z)for z in inf]}
# Real square-root domain is not simply [0,20]: include the small negative component.
grad=lambda z:z+5*mp.sin(z);gprime=lambda z:1+5*mp.cos(z);gsecond=lambda z:-5*mp.sin(z)
zr=scanroot(grad,mp.mpf(-5),mp.mpf(20),6000)
if not any(abs(z)<mp.mpf('1e-20')for z in zr):zr.append(mp.mpf(0))
zr=sorted(zr);cuts=[mp.mpf(-5)]+zr+[mp.mpf(20)];domains=[(a,b)for a,b in zip(cuts,cuts[1:])if grad((a+b)/2)>0]
f17=lambda z:mp.sqrt(grad(z));d17=lambda z:gprime(z)/(2*mp.sqrt(grad(z)));n17=lambda z:2*grad(z)*gsecond(z)-gprime(z)**2;dd17=lambda z:n17(z)/(4*grad(z)**mp.mpf('1.5'));cr=[];ir=[]
for a,b in domains:cr+=scanroot(gprime,a+mp.mpf('1e-10'),b-mp.mpf('1e-10'),2500);ir+=scanroot(n17,a+mp.mpf('1e-10'),b-mp.mpf('1e-10'),2500)
ext,inf=analyze(17,r'f(x)=\sqrt{x+5\sin x},\quad x\le20',f17,d17,dd17,cr,ir,domains,zr,None,[r'D=\{x\le20:x+5\sin x\ge0\};\quad\text{include the zero-radicand endpoints of the listed domain intervals}',r'f^{\prime}=\frac{1+5\cos x}{2\sqrt{x+5\sin x}}',r'f^{\prime\prime}=\frac{-10(x+5\sin x)\sin x-(1+5\cos x)^2}{4(x+5\sin x)^{3/2}}',r'\text{Every zero-radicand endpoint is a one-sided minimum with }f=0;\quad\text{absolute maximum at }x=20,\quad f(20)\approx'+show(f17(20))],[('All real-domain components',[-5,20],[-.2,5.5]),('Small negative-domain component',[-5,-4],[0,.7])]);records[17]={'domain':[[str(a),str(b)]for a,b in domains],'critical':[str(z)for z in cr],'inflections':[str(z)for z in inf]}
D=x**4+x+1;f18=(2*x-1)/D**S.Rational(1,4);d=S.factor(S.diff(f18,x));dd=S.factor(S.diff(f18,x,2));cr=roots_poly(S.fraction(d)[0]);ir=roots_poly(S.fraction(dd)[0]);fn=S.lambdify(x,f18,'mpmath');d1=S.lambdify(x,d,'mpmath');d2=S.lambdify(x,dd,'mpmath')
ext,inf=analyze(18,'f(x)='+S.latex(f18),fn,d1,d2,cr,ir,[(-mp.inf,mp.inf)],[],f18,[r'x^4+x+1>0;\quad\lim_{x\to-\infty}f=-2,\quad\lim_{x\to\infty}f=2'],[('Fourth-root denominator',[-7,7],[-4,3])]);records[18]={'critical':[str(z)for z in cr],'inflections':[str(z)for z in inf]}
f19=S.sin(x+S.sin(3*x));fn=S.lambdify(x,f19,'mpmath');d1=S.lambdify(x,S.diff(f19,x),'mpmath');d2=S.lambdify(x,S.diff(f19,x,2),'mpmath');cr=scanroot(d1,mp.mpf(0),mp.pi,12000);ir=scanroot(d2,mp.mpf('1e-9'),mp.pi-mp.mpf('1e-9'),12000)
ext,inf=analyze(19,r'f(x)=\sin(x+\sin3x)',fn,d1,d2,cr,ir,[(mp.mpf(0),mp.pi)],[],f19,[r'f(-x)=-f(x),\quad f(x+2\pi)=f(x)',r'\text{On }[0,\pi]\text{ there are three local maxima, including two very close peaks near }x=0.6',r'g=x+\sin3x:\quad f^{\prime}=\cos g(1+3\cos3x)',r'\text{Partition at }1+3\cos3x=0\text{ and solve }g=\pi/2\text{ on each monotone piece.}'],[('Requested window',[0,math.pi],[-1.2,1.2]),('Two close peaks and a hidden minimum',[.54,.74],[.99994,1.00001]),('Odd symmetry and two periods',[-2*math.pi,2*math.pi],[-1.2,1.2])]);records[19]={'critical':[str(z)for z in cr],'inflections':[str(z)for z in inf]}
calc(20,r'f_c(x)=x^3+cx,\quad c\in\mathbb R','여러 매개변수 그래프와 도함수로 극값·변곡점의 이동과 모양 전환값을 조사하라.','Use several parameter plots and derivatives to study moving extrema, inflections, and shape transitions.',[r'f_c^{\prime}=3x^2+c,\quad f_c^{\prime\prime}=6x',r'c<0:\quad a=\sqrt{-c/3},\quad\max(-a,2a^3),\quad\min(a,-2a^3)',r'c\ge0:\quad\text{increasing, no extrema};\quad c=0\text{ has a stationary inflection}',r'\text{Every member has inflection }(0,0)'],r'\text{Transition }c=0;\quad c\uparrow0\text{ merges the two extrema at the origin}','매개변수가 음의 큰 값이면 극값이 원점에서 멀어지고 높이의 절댓값이 커진다. 모든 곡선은 홀함수이다.','Large negative parameters move the extrema farther from the origin and increase their absolute heights. Every curve is odd.');plot(20,[('Cubic family',[(f'c={c}',lambda z,c=c:z**3+c*z,[])for c in [-3,-1,0,1,3]],[-2.5,2.5],[-8,8])])
calc(21,r'f_c(x)=x^2+6x+c/x,\quad x\ne0','뉴턴 삼지창 함수족의 극값·변곡점·점근선과 모양 전환값을 조사하라.','Investigate extrema, inflections, asymptotes, and shape transitions of the trident family.',[r'f_c^{\prime}=(2x^3+6x^2-c)/x^2,\quad f_c^{\prime\prime}=2+2c/x^3',r'H(x)=2x^2(x+3),\quad H^{\prime}=6x(x+2),\quad H(-2)=8,\ H(0)=0',r'c<0:\ \text{one minimum at }x<-3;\quad c=0:\ \min(-3,-9),\ \text{hole at }(0,0)',r'0<c<8:\quad\text{min at }r_1\in(-3,-2),\ \max\text{ at }r_2\in(-2,0),\ \min\text{ at }r_3>0',r'c=8:\quad f^{\prime}=2(x+2)^2(x-1)/x^2;\quad\min(1,15),\quad\text{stationary inflection }(-2,-12)',r'c>8:\quad\text{one minimum at }x>1',r'c\ne0:\quad\text{inflection input }x=-\sqrt[3]c;\quad x=0\text{ vertical asymptote}',r'f_c(x)-(x^2+6x)=c/x\to0\quad(x\to\pm\infty)'],r'\text{Transitions }c=0,8;\quad\text{critical inputs solve }2x^2(x+3)=c','정의역에서 원점은 모든 매개변수에 대해 제외했다. 영 매개변수에서는 수직 점근선 대신 제거 가능한 구멍이 남는다.','The origin remains excluded for every parameter. At zero parameter, the vertical asymptote is replaced by a removable hole.');plot(21,[('Trident transition family',[(f'c={c}',lambda z,c=c:z*z+6*z+c/z,[0])for c in [-4,0,4,8,12]],[-6,3],[-25,25])])
calc(22,r'f_c(x)=x\sqrt{c^2-x^2},\quad c\in\mathbb R','함수족의 정의역·극값·변곡점과 매개변수 변화에 따른 크기를 조사하라.','Investigate domains, extrema, inflections, and scaling across the family.',[r'r=|c|>0:\quad D=[-r,r],\quad f_c(ru)=r^2u\sqrt{1-u^2}',r'f_c^{\prime}=(r^2-2x^2)/\sqrt{r^2-x^2}',r'f_c^{\prime\prime}=x(2x^2-3r^2)/(r^2-x^2)^{3/2}',r'\min(-r/\sqrt2,-r^2/2),\quad\max(r/\sqrt2,r^2/2),\quad\text{inflection }(0,0)',r'c=0:\quad D=\{0\},\quad f(0)=0'],r'c\text{ and }-c\text{ give identical graphs; transition at }c=0','매개변수 절댓값이 커지면 가로 크기는 그 값에, 세로 크기는 그 제곱에 비례한다. 퇴화한 한 점에서는 통상적인 내부 변곡점을 정의하지 않는다.','Horizontal scale grows with the absolute parameter and vertical scale with its square. The collapsed one-point domain has no ordinary interior inflection point.');plot(22,[('Scaling of the radical family',[(f'|c|={c}',lambda z,c=c:z*math.sqrt(c*c-z*z),[-c,c])for c in [.5,1,2,3]],[-3,3],[-5,5])])
calc(23,r'f_c(x)=cx/(1+c^2x^2)','극값과 변곡점의 이동, 대칭, 전환값을 조사하라.','Investigate moving extrema and inflections, symmetry, and transitions.',[r'f_c(x)=h(cx),\quad h(t)=t/(1+t^2)',r'f_c^{\prime}=c(1-c^2x^2)/(1+c^2x^2)^2',r'f_c^{\prime\prime}=2c^3x(c^2x^2-3)/(1+c^2x^2)^3',r'c\ne0:\quad\max(1/c,1/2),\quad\min(-1/c,-1/2)',r'\text{Inflections: }(0,0),(\sqrt3/c,\sqrt3/4),(-\sqrt3/c,-\sqrt3/4)',r'c=0:\quad f\equiv0;\quad c\ne0:\quad y=0\text{ horizontal asymptote}'],r'\text{Transition }c=0;\quad|c|\text{ controls horizontal compression, sign controls reflection}');plot(23,[('Rational family',[(f'c={c}',lambda z,c=c:c*z/(1+c*c*z*z),[])for c in [-2,-.5,0,.5,2]],[-5,5],[-.6,.6])])
calc(24,r'f_c(x)=\sin x/(c+\cos x)','점근선·극값·변곡점 개수가 변하는 매개변수를 찾고 여러 곡선을 비교하라.','Find parameter transitions in asymptotes, extrema, and inflections, and compare several curves.',[r'f_c^{\prime}=\frac{1+c\cos x}{(c+\cos x)^2},\quad f_c^{\prime\prime}=\frac{\sin x(2-c^2+c\cos x)}{(c+\cos x)^3}',r'|c|<1:\quad\cos x=-c\text{ gives two vertical poles per period};\quad f_c^{\prime}>0\text{ on each branch}',r'c=1:\ f=\tan(x/2);\quad c=-1:\ f=-\cot(x/2);\quad\text{one vertical pole per period}',r'|c|>1:\quad\text{no poles};\quad\cos x=-1/c\text{ gives extrema of heights }\pm1/\sqrt{c^2-1}',r'\text{Inflections at }\sin x=0\text{ whenever defined}',r'1<|c|<2:\quad\cos x=c-2/c\text{ adds two inflections per period}',r'|c|=2:\quad\text{the additional pair merges into a sine-zero inflection};\quad |c|>2:\text{ no additional pair}',r'f_{-c}(x)=f_c(x+\pi),\quad f_c(x+2\pi)=f_c(x)'],r'\text{Shape transitions at }c=-2,-1,1,2','모든 영 분모는 정의역에서 제외한다. 절댓값 일이하에서는 각 가지가 증가하지만 절댓값 일을 넘으면 파형 극값이 생긴다. 추가 변곡점은 절댓값 일과 이 사이에서만 따로 존재한다.','All zero denominators are excluded. Branches increase when the absolute parameter is at most one; beyond one, smooth wave extrema appear. Extra inflections occur separately only between absolute parameters one and two.');plot(24,[(f'Parameter c={c}',[(f'c={c}',lambda z,c=c:math.sin(z)/(c+math.cos(z)),[a for a in [-math.acos(-c),math.acos(-c)]if abs(c)<=1]if abs(c)<=1 else[])],[-math.pi,math.pi],[-3,3])for c in [0,1,1.3,2,3]])
calc(25,r'f_c(x)=cx+\sin x','매개변수에 따라 단조성과 극값·변곡점이 어떻게 바뀌는지 조사하라.','Investigate parameter changes in monotonicity, extrema, and inflections.',[r'f_c^{\prime}=c+\cos x,\quad f_c^{\prime\prime}=-\sin x',r'c\ge1:\quad\text{increasing};\quad c\le-1:\quad\text{decreasing};\quad\text{no extrema in either case}',r'-1<c<1:\quad\alpha=\arccos(-c)',r'\max\text{ at }x=\alpha+2k\pi,\quad\min\text{ at }x=-\alpha+2k\pi',r'f(\alpha+2k\pi)=c\alpha+\sin\alpha+2k\pi c',r'f(-\alpha+2k\pi)=-c\alpha-\sin\alpha+2k\pi c',r'\text{Inflections }(k\pi,ck\pi)\text{ for every }c;\quad c=\pm1\text{ makes alternate ones stationary}'],r'\text{Extremum transitions }c=\pm1;\quad c=0\text{ is the periodic member}','영이 아닌 매개변수에서는 물결이 직선 경향 위에서 이동한다. 직선과의 차이는 사인이므로 그 직선은 엄밀한 점근선은 아니다.','For nonzero parameter, the wave follows a linear trend. Its difference from that line is sine, so the line is not a strict asymptote.');plot(25,[('Linear trend plus sine',[(f'c={c}',lambda z,c=c:c*z+math.sin(z),[])for c in [-1.5,-1,0,1,1.5]],[-7,7],[-10,10])])
calc(26,r'f_c(x)=cx^4-4x^2+1','(a) 최소점이 있는 매개변수 (b) 모든 극값점이 놓이는 포물선을 증명하고 함수족과 함께 그려라.','(a) Find parameters with minima and (b) prove the parabolic locus of all extrema, illustrating it with the family.',[r'f_c^{\prime}=4x(cx^2-2),\quad f_c^{\prime\prime}=12cx^2-8',r'x=0:\quad f=1,\ f^{\prime\prime}=-8<0\text{ for every }c',r'c>0:\quad x=\pm\sqrt{2/c},\quad f^{\prime\prime}=16>0,\quad f=1-4/c',r'cx^2=2:\quad cx^4-4x^2+1=1-2x^2',r'x=0:\quad f=1=1-2x^2'],r'\text{(a)}\ c>0;\quad\text{(b)}\ y=1-2x^2',sub='ab');plot(26,[('Extrema lie on the parabola',[(f'c={c}',lambda z,c=c:c*z**4-4*z*z+1,[])for c in [-1,0,1,2,4]]+[('locus 1-2x^2',lambda z:1-2*z*z,[])],[-2.5,2.5],[-9,5])])
calc(27,r'f_c(x)=x^4+cx^2+x','변곡점 개수의 전환값을 먼저 구하고, 그래프로 임계수 개수의 다른 전환값을 찾아 증명하라.','First determine the inflection-count transition, then discover and prove the separate transition in critical-point counts.',[r'f_c^{\prime}=4x^3+2cx+1,\quad f_c^{\prime\prime}=12x^2+2c',r'c<0:\quad\text{two inflections at }x=\pm\sqrt{-c/6};\quad c\ge0:\text{ no inflections}',r'\text{A multiple critical root satisfies }4x^3+2cx+1=0,\quad12x^2+2c=0',r'c=-6x^2\Rightarrow1-8x^3=0\Rightarrow x=1/2,\ c=-3/2',r'c<-3/2:\quad\text{three critical points: min, max, min}',r'c=-3/2:\quad f^{\prime}=(x+1)(2x-1)^2;\quad\min\text{ at }x=-1,\ \text{stationary inflection at }x=1/2',r'c>-3/2:\quad\text{one critical point, a global minimum}'],r'\text{Inflection transition }c=0;\quad\text{critical-count transition }c=-3/2','임계수 개수는 전환점에서 서로 다른 두 개이며, 그중 하나는 극값이 아닌 수평 변곡점이다.','At the critical transition there are two distinct critical numbers, one of which is a stationary inflection rather than an extremum.');plot(27,[('Quartic transition family',[(f'c={c}',lambda z,c=c:z**4+c*z*z+z,[])for c in [-3,-1.5,-.5,0,2]],[-2,2],[-5,6])])
calc(28,r'f_c(x)=2x^3+cx^2+2x','(a) 함수족을 조사하고 극대·극소가 생기는 매개변수를 구하라. (b) 모든 극값점이 놓이는 곡선을 증명하고 함께 그려라.','(a) Investigate the family and parameters producing maxima and minima. (b) Prove the locus of all extrema and plot it with the family.',[r'f_c^{\prime}=6x^2+2cx+2,\quad f_c^{\prime\prime}=12x+2c',r'\Delta=4(c^2-12)>0\Longleftrightarrow |c|>2\sqrt3',r'x_- =(-c-\sqrt{c^2-12})/6\text{ is a local maximum};\quad x_+=(-c+\sqrt{c^2-12})/6\text{ is a local minimum}',r'|c|<2\sqrt3:\quad\text{increasing, no extrema};\quad |c|=2\sqrt3:\text{ stationary inflection only}',r'\text{Every curve has inflection input }x=-c/6',r'f_c^{\prime}=0\Rightarrow cx=-3x^2-1\Rightarrow f_c=2x^3+x(cx)+2x=x-x^3'],r'\text{(a)}\ |c|>2\sqrt3;\quad\text{(b)}\ y=x-x^3',sub='ab');plot(28,[('Extrema locus and cubic family',[(f'c={c}',lambda z,c=c:2*z**3+c*z*z+2*z,[])for c in [-5,-2*math.sqrt(3),0,2*math.sqrt(3),5]]+[('locus x-x^3',lambda z:z-z**3,[])],[-2.2,2.2],[-8,8])])
items.sort(key=lambda e:e['number']);assert[e['number']for e in items]==list(range(1,29))
raw={'section':'3.6','source':{'title':'Calculus','edition':'9','language':'en','printedPages':[263,264],'pdfPages':[300,301]},'scope':{'kind':'exercise','numbers':list(range(1,29)),'total':28,'note':bi('일반 Exercises의 모든 주번호와 소문항.','All main-numbered ordinary Exercises and their subparts.')},'exercises':items}
sys.path.insert(0,str(BASE));from build_exercises import validate_document
validate_document(raw,BASE/'exercise-content/s3-6.json')
import xml.etree.ElementTree as ET
for ex in items:
 ET.parse(BASE/'exercise-content/assets'/Path(ex['figure']['src']).name)
 for key in ['statement','answer']:assert re.findall(r'\\\((.*?)\\\)',ex[key]['ko'])==re.findall(r'\\\((.*?)\\\)',ex[key]['en'])
# Independent derivative evaluation at a regular point for every rational function.
for q,f in functions.items():
 fn=S.lambdify(x,f,'mpmath');d=S.lambdify(x,S.diff(f,x),'mpmath');dd=S.lambdify(x,S.diff(f,x,2),'mpmath');z=mp.mpf('1.371')
 assert abs(mp.diff(fn,z)-d(z))<mp.mpf('1e-40');assert abs(mp.diff(fn,z,2)-dd(z))<mp.mpf('1e-40')
for z in [-mp.mpf('1.37'),mp.mpf('.73')]:
 assert abs(mp.diff(f16,z)-d16(z))<mp.mpf('1e-45');assert abs(mp.diff(f16,z,2)-dd16(z))<mp.mpf('1e-45')
assert len(records[19]['critical'])==6;assert len(records[17]['domain'])==3
c=S.symbols('c',real=True);assert S.factor(4*x**3-3*x+1)==(x+1)*(2*x-1)**2
assert S.simplify((2*x**3+c*x*x+2*x).subs(c,(-3*x*x-1)/x)-(x-x**3))==0
(BASE/'exercise-content/s3-6.json').write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
(BASE/'exercise-checks/s3-6-independent.json').write_text(json.dumps(records,indent=2)+'\n')
print('3.6: 28 cards, 28 multi-panel SVG; exact polynomial root isolation, high-precision root refinement, independent derivatives, domain components and family transition identities verified')
