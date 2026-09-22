"""§4.5: explicitly checked substitutions and antiderivatives."""
import json,sys,math,html
import sympy as s
import mpmath as mp
from early_helpers import Book,pair,same,fs,ROOT
x=s.symbols('x',real=True);u=s.symbols('u',positive=True);a=s.symbols('a',positive=True);aa,bb=s.symbols('a b',real=True);R=s.Rational
b=Book('4.5',[355,356]);checks=[];mp.mp.dps=40
M=lambda z:r'\('+z+r'\)'
def tex(z):return s.latex(z)
def add(n,eq,k,e,lines,ans,note=None):
 steps=fs(*lines)
 if note:steps.append(note)
 b.add(n,355 if n<=54 else 356,('치환적분','Integration by substitution'),(M(eq)+' '+k,M(eq)+' '+e),steps,same(M(ans)),check=('치환 전후 적분함수와 미분 인자를 대조하고 원시함수를 미분하여 확인했다. 정적분은 경계값 또는 대칭성을 사용했다.','Checked the integrand and differential under substitution, and differentiated the antiderivative. Definite integrals use endpoint values or symmetry.'))
 b.E[n]['conceptHref']='../../calc1/index.html'
def graph(n,funcs,lo,hi,shade=False,caption=None):
 data=[(label,[(lo+(hi-lo)*j/400,float(fn(lo+(hi-lo)*j/400)))for j in range(401)])for label,fn in funcs];vs=[y for _,p in data for _,y in p];y0=min(0,min(vs));y1=max(0,max(vs));pad=(y1-y0)*.1 or 1;y0-=pad;y1+=pad
 X=lambda v:60+510*(v-lo)/(hi-lo);Y=lambda v:315-260*(v-y0)/(y1-y0)
 out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 410"><rect width="640" height="410" fill="#f8fafc"/>',f'<text x="35" y="25" font-size="16">Exercise 4.5.{n}</text>',f'<path d="M60 {Y(0)}H580" stroke="#64748b"/>']
 if shade:
  pts=[(lo,0)]+data[0][1]+[(hi,0)];out.append('<polygon points="'+' '.join(f'{X(v):.3f},{Y(w):.3f}'for v,w in pts)+'" fill="#bfdbfe"/>')
 for j,(label,pts)in enumerate(data):
  color=['#2563eb','#dc2626'][j%2];out.append('<polyline points="'+' '.join(f'{X(v):.3f},{Y(w):.3f}'for v,w in pts)+f'" fill="none" stroke="{color}" stroke-width="2"/><text x="{60+j*260}" y="390" fill="{color}" font-size="14">{html.escape(label)}</text>')
 for j in range(5):
  v=lo+(hi-lo)*j/4;w=y0+(y1-y0)*j/4;out.append(f'<text x="{X(v)-10}" y="339" font-size="11">{v:.3g}</text><text x="5" y="{Y(w)+3}" font-size="11">{w:.3g}</text>')
 out.append('</svg>');name=f's4-5-{n}.svg';(ROOT/'assets'/name).write_text(''.join(out));b.E[n]['figure']={'src':'../exercise-content/assets/'+name,'alt':pair('주어진 식으로 계산한 자체 그래프','Original graph computed from the given formulas'),'caption':pair(*(caption or ('파랑·빨강은 표시된 함수의 그래프이다.','Blue and red show the labeled functions.')))}
# n, original integrand, u(x), transformed integrand (including dx factor).
rows=[
(1,s.cos(2*x),2*x,s.cos(u)/2),(2,x*(2*x*x+3)**4,2*x*x+3,u**4/4),(3,x*x*s.sqrt(x**3+1),x**3+1,s.sqrt(u)/3),
(4,s.sin(x)**2*s.cos(x),s.sin(x),u**2),(5,x**3/(x**4-5)**2,x**4-5,1/(4*u**2)),(6,s.sqrt(1+1/x)/x**2,1+1/x,-s.sqrt(u)),(7,s.cos(s.sqrt(x))/s.sqrt(x),s.sqrt(x),2*s.cos(u)),(8,x*s.sqrt(x-1),x-1,(u+1)*s.sqrt(u)),
(9,x*s.sqrt(1-x*x),1-x*x,-s.sqrt(u)/2),(10,(5-3*x)**10,5-3*x,-u**10/3),(11,x*x*s.cos(x**3),x**3,s.cos(u)/3),(12,s.sin(x)*s.sqrt(1+s.cos(x)),1+s.cos(x),-s.sqrt(u)),(13,s.sin(s.pi*x/3),s.pi*x/3,3*s.sin(u)/s.pi),(14,s.sec(2*x)**2,2*x,s.sec(u)**2/2),(15,s.sec(3*x)*s.tan(3*x),3*x,s.sec(u)*s.tan(u)/3),
(16,x*x*(4-x**3)**R(2,3),4-x**3,-u**R(2,3)/3),(17,s.cos(1+5*x),1+5*x,s.cos(u)/5),(18,s.sin(1/x)/x**2,1/x,-s.sin(u)),(19,s.cos(x)**3*s.sin(x),s.cos(x),-u**3),(20,s.sin(x)*s.sin(s.cos(x)),s.cos(x),-s.sin(u)),(21,(x-1/x**2)*(x*x+2/x)**5,x*x+2/x,u**5/2),(22,x*s.sqrt(x+2),x+2,(u-2)*s.sqrt(u)),(23,(aa+bb*x*x)/s.sqrt(3*aa*x+bb*x**3),3*aa*x+bb*x**3,1/(3*s.sqrt(u))),
(24,s.sec(x)**2/s.tan(x)**2,s.tan(x),u**-2),(25,x*x/(1+x**3)**R(1,3),1+x**3,u**-R(1,3)/3),(26,1/(s.cos(x)**2*s.sqrt(1+s.tan(x))),1+s.tan(x),u**-R(1,2)),(27,s.sqrt(s.cot(x))*s.csc(x)**2,s.cot(x),-s.sqrt(u)),(28,s.cos(s.pi/x)/x**2,s.pi/x,-s.cos(u)/s.pi),(29,s.sec(x)**3*s.tan(x),s.sec(x),u*u),(30,x*x*s.sqrt(2+x),2+x,(u-2)**2*s.sqrt(u)),(31,x*(2*x+5)**8,2*x+5,(u-5)*u**8/4),(32,x**3*s.sqrt(x*x+1),x*x+1,(u-1)*s.sqrt(u)/2),
(33,x*(x*x-1)**3,x*x-1,u**3/2),(34,s.tan(x)**2*s.sec(x)**2,s.tan(x),u*u),(35,s.sin(x)**3*s.cos(x),s.sin(x),u**3),(36,s.sin(x)*s.cos(x)**4,s.cos(x),-u**4),
(67,1/(4*x+7),4*x+7,1/(4*u)),(68,s.exp(-5*x),-5*x,-s.exp(u)/5),(69,s.log(x)**2/x,s.log(x),u*u),(70,1/(aa*x+bb),aa*x+bb,1/(aa*u)),(71,s.exp(x)*(2+3*s.exp(x))**R(3,2),2+3*s.exp(x),u**R(3,2)/3),(72,s.exp(s.cos(x))*s.sin(x),s.cos(x),-s.exp(u)),(73,s.atan(x)**2/(x*x+1),s.atan(x),u*u),(74,(x+1)/(3*x*x+6*x-5),3*x*x+6*x-5,1/(6*u)),(76,s.sin(s.log(x))/x,s.log(x),s.sin(u)),(77,s.sin(2*x)/(1+s.cos(x)**2),1+s.cos(x)**2,-1/u),(78,s.sin(x)/(1+s.cos(x)**2),s.cos(x),-1/(1+u*u)),(79,s.cot(x),s.sin(x),1/u),(80,x/(1+x**4),x*x,1/(2*(1+u*u))) ]
for n,f,g,q in rows:
 residual=s.trigsimp(s.simplify(q.subs(u,g)*s.diff(g,x)-f));assert residual==0,(n,residual)
 H=s.integrate(s.expand(q),u);assert not H.has(s.Integral),(n,H);assert s.trigsimp(s.simplify(s.diff(H,u)-q))==0,(n,H)
 F=H.subs(u,g)
 if n in [67,70,74,79]:F=F.replace(s.log,lambda z:s.log(s.Abs(z)))
 lines=['u='+tex(g)+r',\quad du=\left('+tex(s.diff(g,x))+r'\right)dx',r'I=\int\left('+tex(q)+r'\right)du',r'I='+tex(H)+r'+C',r'I='+tex(F)+r'+C']
 note=('실수 범위에서 함수가 정의되는 각 구간에 적용하며, 적분상수는 구간마다 다를 수 있다.','Use the formula on each real-domain interval; constants may differ between disconnected intervals.')
 if n in [16,25]:note=('분모가 영인 점을 제외하고 삼분의 일 거듭제곱은 실수 세제곱근으로 해석한다.','Interpret one-third powers as real cube roots, excluding zeros of denominators.')
 if n==70:note=('매개변수 a는 영이 아니며 분모가 영인 점을 제외한다.','The parameter a is nonzero; exclude zeros of the denominator.')
 k='치환적분으로 부정적분을 구하라.';e='Evaluate the indefinite integral by substitution.'
 if n<=8:k+=' 지정된 치환은 '+M('u='+tex(g))+'이다.';e+=' Use the specified substitution '+M('u='+tex(g))+'.'
 if n in [33,34,35,36]:k+=' 적분상수를 영으로 두고 원시함수와 도함수 그래프를 비교하라.';e+=' Set the integration constant to zero and compare graphs of the antiderivative and its derivative.'
 add(n,r'\int\left('+tex(f)+r'\right)dx',k,e,lines,tex(F)+r'+C',note);checks.append({'n':n,'substitution':str(g),'antiderivative':str(F),'chainRuleResidual':str(residual)})
 if n in [33,34,35,36]:
  lo,hi=(-1,1)if n==34 else(-2,2);graph(n,[('F(x), C=0',s.lambdify(x,F,'math')),('derivative = integrand',s.lambdify(x,f,'math'))],lo,hi)
# Definite substitutions; the transformed limits retain their orientation.
drows=[(37,s.cos(s.pi*x/2),0,1,s.pi*x/2,2*s.cos(u)/s.pi),(38,(3*x-1)**50,0,1,3*x-1,u**50/3),(39,(1+7*x)**R(1,3),0,1,1+7*x,u**R(1,3)/7),(40,s.csc(x/2)**2,s.pi/3,2*s.pi/3,x/2,2*s.csc(u)**2),(41,s.sin(x)/s.cos(x)**2,0,s.pi/6,s.cos(x),-u**-2),(42,s.sqrt(2+s.sqrt(x))/s.sqrt(x),1,4,2+s.sqrt(x),2*s.sqrt(u)),(44,s.cos(x)*s.sin(s.sin(x)),0,s.pi/2,s.sin(x),s.sin(u)),(45,(1+2*x)**-R(2,3),0,13,1+2*x,u**-R(2,3)/2),(47,x*s.sqrt(x*x+a*a),0,a,x*x+a*a,s.sqrt(u)/2),(49,x*s.sqrt(x-1),1,2,x-1,(u+1)*s.sqrt(u)),(50,x/s.sqrt(1+2*x),0,4,1+2*x,(u-1)/(4*s.sqrt(u))),(51,s.cos(x**-2)/x**3,R(1,2),1,x**-2,-s.cos(u)/2),(52,1/(1+s.sqrt(x))**4,0,1,1+s.sqrt(x),2*(u-1)/u**4),(81,1/(x*s.sqrt(s.log(x))),s.E,s.exp(4),s.log(x),u**-R(1,2)),(82,s.exp(x)/(1+s.exp(2*x)),0,1,s.exp(x),1/(1+u*u)),(83,(s.exp(x)+1)/(s.exp(x)+x),0,1,s.exp(x)+x,1/u),(84,(x-1)*s.exp((x-1)**2),0,2,(x-1)**2,s.exp(u)/2)]
for n,f,lo,hi,g,q in drows:
 residual=s.trigsimp(s.simplify(q.subs(u,g)*s.diff(g,x)-f));assert residual==0,(n,residual)
 H=s.integrate(s.expand(q),u);assert not H.has(s.Integral);assert s.trigsimp(s.simplify(s.diff(H,u)-q))==0
 L=s.simplify(g.subs(x,lo));U=s.simplify(g.subs(x,hi));val=s.simplify(H.subs(u,U)-H.subs(u,L));lines=['u='+tex(g)+r',\quad du=\left('+tex(s.diff(g,x))+r'\right)dx',r'x='+tex(lo)+r'\Rightarrow u='+tex(L)+r',\quad x='+tex(hi)+r'\Rightarrow u='+tex(U),r'I=\int_{'+tex(L)+'}^{'+tex(U)+r'}\left('+tex(q)+r'\right)du',r'I=\left['+tex(H)+r'\right]_{'+tex(L)+'}^{'+tex(U)+'}='+tex(val)]
 note=None
 if n==47:note=('매개변수 a는 양수이다.','The parameter a is positive.')
 if n==84:note=('치환함수가 일대일이 아니어도 원시함수의 합성에 대한 연쇄법칙으로 정적분 공식이 성립한다. 중앙에서 나누면 두 적분이 상쇄된다.','The substitution need not be one-to-one: the chain rule for the composed antiderivative still gives the endpoint formula. Splitting at the midpoint yields cancelling integrals.')
 add(n,r'\int_{'+tex(lo)+'}^{'+tex(hi)+r'}\left('+tex(f)+r'\right)dx','정적분을 계산하라.','Evaluate the definite integral.',lines,tex(val),note)
 # Separate numerical quadrature checks, using a=2 for the parameterized exercise.
 numf=f.subs(a,2);A=lo.subs(a,2)if hasattr(lo,'subs')else lo;B=hi.subs(a,2)if hasattr(hi,'subs')else hi;target=val.subs(a,2)
 numeric=mp.quad(s.lambdify(x,numf,'mpmath'),[mp.mpf(str(s.N(A,38))),mp.mpf(str(s.N(B,38)))]);assert abs(numeric-mp.mpf(str(s.N(target,38))))<mp.mpf('1e-25')*max(1,abs(numeric)),(n,numeric,target)
 checks.append({'n':n,'answer':str(val),'numeric':str(numeric)})
for n,f,c in [(43,x**3+x**4*s.tan(x),s.pi/4),(48,x**4*s.sin(x),s.pi/3)]:
 assert s.simplify(f.subs(x,-x)+f)==0
 add(n,r'\int_{-'+tex(c)+'}^{'+tex(c)+r'}\left('+tex(f)+r'\right)dx','대칭성을 이용하여 정적분을 계산하라.','Evaluate using symmetry.',[r'f(-x)=-f(x)',r'\int_{-c}^cf(x)\,dx=0'],r'0')
add(46,r'\int_0^a x\sqrt{a^2-x^2}\,dx','매개변수 a가 실수일 때 정적분을 계산하라.','Evaluate for a real parameter a.',[r'u=a^2-x^2,\quad du=-2x\,dx',r'I=-\tfrac12\int_{a^2}^0u^{1/2}\,du=\tfrac13(a^2)^{3/2}'],r'|a|^3/3',('a가 양수이면 a³/3이고 영이면 적분도 영이다. 음수여도 적분 방향을 유지하면 같은 절댓값 식을 얻는다.','For positive a this is a³/3; for zero it is zero. For negative a the oriented integral gives the same absolute-value expression.'))
add(75,r'\int\frac{1+x}{1+x^2}\,dx','두 항으로 나누어 부정적분을 계산하라.','Split into two terms and integrate.',[r'I=\int\frac{dx}{1+x^2}+\int\frac{x\,dx}{1+x^2}',r'u=1+x^2,\quad du=2x\,dx'],r'\arctan x+\tfrac12\ln(1+x^2)+C')
for n,f,hi,F in [(53,s.sqrt(2*x+1),1,(2*x+1)**R(3,2)/3),(54,2*s.sin(x)-s.sin(2*x),s.pi,-2*s.cos(x)+s.cos(2*x)/2)]:
 val=s.simplify(F.subs(x,hi)-F.subs(x,0));assert s.trigsimp(s.diff(F,x)-f)==0
 approx=round(float(val),1);add(n,'y='+tex(f)+r',\quad0\le x\le'+tex(hi),'그래프로 곡선 아래 넓이를 대략 추정하고 정확한 값을 구하라.','Estimate the area under the curve graphically, then find the exact value.',[r'A\approx'+str(approx)+r'\quad\text{(rough graph estimate)}',r'A=\int_0^{'+tex(hi)+'}('+tex(f)+r')dx=\left['+tex(F)+r'\right]_0^{'+tex(hi)+'}',r'A='+tex(val)],tex(val));graph(n,[('integrand',s.lambdify(x,f,'math'))],0,float(hi),True)
add(55,r'\int_{-2}^2(x+3)\sqrt{4-x^2}\,dx','두 적분으로 나누고 원의 넓이를 이용하여 계산하라.','Split the integral and use a circular area.',[r'I=\int_{-2}^2x\sqrt{4-x^2}\,dx+3\int_{-2}^2\sqrt{4-x^2}\,dx',r'\text{first integrand odd}\Rightarrow\text{first integral}=0',r'\text{second integral}=\tfrac12\pi(2)^2=2\pi'],r'6\pi')
add(56,r'\int_0^1x\sqrt{1-x^4}\,dx','치환 뒤 원의 넓이로 해석하여 계산하라.','Substitute and interpret the result as a circular area.',[r'u=x^2,\quad du=2x\,dx',r'I=\tfrac12\int_0^1\sqrt{1-u^2}\,du',r'\int_0^1\sqrt{1-u^2}\,du=\pi/4'],r'\pi/8')
add(57,r'f(t)=\tfrac12\sin(2\pi t/5)\ \mathrm{L/s}','주기 오 초인 호흡 모형에서 들숨 시작 이후 폐 안 공기의 부피 변화를 시간의 함수로 구하라.','For a five-second breathing cycle, find the lung-volume change from the start of inhalation as a function of time.',[r'V(t)-V(0)=\int_0^t\tfrac12\sin(2\pi s/5)\,ds',r'V(t)-V(0)=\left[-\frac5{4\pi}\cos(2\pi s/5)\right]_0^t'],r'V(t)-V(0)=\frac5{4\pi}[1-\cos(2\pi t/5)]\ \mathrm L',('이는 시작 시점 대비 순부피 변화다. 첫 들숨 구간은 영부터 이점오 초이고, 날숨에서는 감소한다. 원래 폐에 있던 부피는 초기값으로 더한다.','This is net volume relative to the initial level. The first inhalation lasts from zero to 2.5 seconds; volume decreases during exhalation. Add the initial lung volume if needed.'))
add(58,r'R(t)=85-0.18\cos(\pi t/12)\ \mathrm{kcal/h}','오전 다섯 시부터 잰 시간 t에 대한 모형으로 하루의 총 기초대사량을 구하라.','Time t is measured in hours from five in the morning. Find total basal metabolism over a full day.',[r'\int_0^{24}R(t)\,dt=\left[85t-\frac{2.16}{\pi}\sin(\pi t/12)\right]_0^{24}',r'\sin0=\sin2\pi=0'],r'2040\ \mathrm{kcal}')
add(59,r'\int_0^4f(x)\,dx=10','연속함수 f에 대해 영부터 이까지 f(2x)의 적분을 구하라.','For continuous f, find the integral of f(2x) from zero to two.',[r'u=2x,\quad dx=du/2',r'\int_0^2f(2x)\,dx=\tfrac12\int_0^4f(u)\,du'],r'5')
add(60,r'\int_0^9f(x)\,dx=4','연속함수 f에 대해 영부터 삼까지 xf(x²)의 적분을 구하라.','For continuous f, integrate xf(x²) from zero to three.',[r'u=x^2,\quad du=2x\,dx',r'\int_0^3xf(x^2)\,dx=\tfrac12\int_0^9f(u)\,du'],r'2')
add(61,r'\int_a^bf(-x)\,dx=\int_{-b}^{-a}f(x)\,dx','실수 전체에서 연속인 f에 대해 증명하라. f가 음이 아니고 0<a<b일 때 넓이의 대칭 도식도 제시하라.','Prove the identity for continuous f on the real line. For nonnegative f and 0<a<b, illustrate equality of reflected areas.',[r'u=-x,\quad dx=-du,\quad x=a\Rightarrow u=-a,\ x=b\Rightarrow u=-b',r'\int_a^bf(-x)\,dx=-\int_{-a}^{-b}f(u)\,du=\int_{-b}^{-a}f(u)\,du'],r'\int_a^bf(-x)\,dx=\int_{-b}^{-a}f(x)\,dx',('y축 대칭은 높이와 가로 길이를 보존하므로 두 영역의 넓이가 같다.','Reflection across the vertical axis preserves heights and horizontal lengths, hence area.'))
add(62,r'\int_a^bf(x+c)\,dx=\int_{a+c}^{b+c}f(x)\,dx','실수 전체에서 연속인 f에 대해 증명하고 f가 음이 아닐 때 넓이의 평행이동 도식을 제시하라.','Prove for continuous f on the real line and illustrate the area-preserving translation when f is nonnegative.',[r'u=x+c,\quad du=dx',r'x=a\Rightarrow u=a+c,\quad x=b\Rightarrow u=b+c',r'\int_a^bf(x+c)\,dx=\int_{a+c}^{b+c}f(u)\,du'],r'\int_a^bf(x+c)\,dx=\int_{a+c}^{b+c}f(x)\,dx',('좌표를 가로 방향으로 c만큼 이동시키면 높이와 밑변 길이가 보존된다.','Translating horizontal coordinates by c preserves heights and base lengths.'))
add(63,r'a,b>0','영부터 일까지 xᵃ(1−x)ᵇ의 적분은 a와 b를 바꾸어도 같음을 증명하라.','Prove that the integral of xᵃ(1−x)ᵇ from zero to one is unchanged when a and b are exchanged.',[r'u=1-x,\quad dx=-du',r'\int_0^1x^a(1-x)^b\,dx=-\int_1^0(1-u)^au^b\,du',r'=\int_0^1u^b(1-u)^a\,du'],r'\int_0^1x^a(1-x)^b\,dx=\int_0^1x^b(1-x)^a\,dx')
add(64,r'I=\int_0^\pi xf(\sin x)\,dx','f가 [0,π]에서 연속일 때 치환 u=π−x로 I의 대칭 공식을 증명하라.','For f continuous on [0,π], derive the symmetry formula for I using u=π−x.',[r'\sin(\pi-u)=\sin u',r'I=\int_0^\pi(\pi-u)f(\sin u)\,du',r'I=\pi\int_0^\pi f(\sin u)\,du-I'],r'I=\frac\pi2\int_0^\pi f(\sin x)\,dx')
add(65,r'\int_0^{\pi/2}f(\cos x)\,dx=\int_0^{\pi/2}f(\sin x)\,dx','연속함수 f에 대해 여각 치환으로 증명하라.','Prove the identity for continuous f using a complementary-angle substitution.',[r'u=\pi/2-x,\quad dx=-du,\quad\cos x=\sin u',r'\int_0^{\pi/2}f(\cos x)\,dx=-\int_{\pi/2}^0f(\sin u)\,du'],r'\int_0^{\pi/2}f(\cos x)\,dx=\int_0^{\pi/2}f(\sin x)\,dx')
add(66,r'A=\int_0^{\pi/2}\cos^2x\,dx,\quad B=\int_0^{\pi/2}\sin^2x\,dx','앞 문항의 대칭성을 이용하여 두 적분을 계산하라.','Use the preceding symmetry identity to evaluate both integrals.',[r'A=B\quad\text{by complementary-angle substitution}',r'A+B=\int_0^{\pi/2}(\cos^2x+\sin^2x)\,dx=\pi/2'],r'A=B=\pi/4')
add(85,r'I=\int_0^\pi\frac{x\sin x}{1+\cos^2x}\,dx','육십사 번의 대칭 공식을 이용하여 계산하라.','Evaluate using the symmetry formula from Exercise 64.',[r'\frac{\sin x}{1+\cos^2x}=\frac{\sin x}{2-\sin^2x}',r'I=\frac\pi2\int_0^\pi\frac{\sin x}{1+\cos^2x}\,dx',r'u=\cos x,\quad\int_0^\pi\frac{\sin x}{1+\cos^2x}\,dx=\int_{-1}^1\frac{du}{1+u^2}=\pi/2'],r'\pi^2/4',('대칭 공식은 합성에 실제 쓰이는 값 범위 [0,1]에서의 연속성만으로 충분하다. 여기서는 그 범위에서 분모가 양수다.','The symmetry proof only needs continuity on the actual argument range [0,1], where this denominator is positive.'))
# Area illustrations for the two general identities: explicitly labeled examples, not extra assumptions.
for n,lo,hi in [(61,1,3),(62,0,2)]:
 name=f's4-5-{n}.svg';shift=3 if n==62 else 0
 label1='f(-x), 1 ≤ x ≤ 3'if n==61 else'f(x+3), 0 ≤ x ≤ 2';label2='f(x), -3 ≤ x ≤ -1'if n==61 else'f(x), 3 ≤ x ≤ 5'
 out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 300"><rect width="660" height="300" fill="#f8fafc"/>']
 for j,label in enumerate([label1,label2]):
  pts=[]
  for k in range(101):
   t=k/100;y=1+(t if n==62 or j==0 else 1-t)**2;pts.append((45+j*330+230*t,230-65*y))
  p=[(45+j*330,230)]+pts+[(275+j*330,230)];out.append('<polygon points="'+' '.join(f'{x:.2f},{y:.2f}'for x,y in p)+'" fill="#bfdbfe" stroke="#2563eb"/><text x="'+str(35+j*330)+'" y="265" font-size="15">'+html.escape(label)+'</text>')
 out.append('<text x="35" y="28" font-size="16">Equal shaded areas: '+('reflection'if n==61 else'translation')+'</text></svg>');(ROOT/'assets'/name).write_text(''.join(out));b.E[n]['figure']={'src':'../exercise-content/assets/'+name,'alt':pair('대칭 또는 평행이동으로 넓이가 보존되는 자체 예시 도식','Original example showing area preservation under reflection or translation'),'caption':pair('일반 증명의 기하적 의미를 보여 주는 비음수 함수의 예시다.','A nonnegative-function example illustrating the geometry of the general proof.')}
from final_sections_helpers import localize
localize(b)
assert sorted(b.E)==list(range(1,86));b.save()
sys.path.insert(0,str(ROOT.parent));from build_exercises import validate_document
validate_document(json.loads((ROOT/'s4-5.json').read_text()),ROOT/'s4-5.json')
(ROOT.parent/'exercise-checks/s4-5-report.json').write_text(json.dumps({'section':'4.5','sourceVisualPages':[392,393],'checks':checks,'notes':['46 covers either sign of a','57 distinguishes net volume and initial volume','84 explains non-injective substitution','85 uses continuity on actual argument range']},ensure_ascii=False,indent=2)+'\n')
print('4.5: 85 exercises; substitutions, antiderivatives and numerical quadrature checked')
