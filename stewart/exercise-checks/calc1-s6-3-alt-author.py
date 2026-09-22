from calc1_alt_helpers import *
from calc1_plot_helpers import plots
x=s.symbols('x',real=True);R=s.Rational;b=AltBook('6.3*',[465,466,467])
def pg(n):return 465 if n<=60 else 466 if n<=80 else 467
def add(n,st,steps,ans,ck,parts=[]):
 b.add(n,pg(n),('자연지수함수','The natural exponential function'),st,steps,ans,parts=parts);b.verify(n,*ck);b.save()
def ma(n,eq,ss,ans,ck,parts=[]):add(n,(M(eq)+'계산하거나 증명하라.',M(eq)+'Evaluate or prove.'),fs(*ss),same(M(ans)),ck,parts)
# Every reused exercise was checked against all three alternative exercise pages.
for n in range(25,63):b.reuse(n,'6.2',n,pg(n))
for n in list(range(63,72))+list(range(73,103)):b.reuse(n,'6.2',n+2,pg(n))
for n,old in[(103,107),(104,108),(15,9),(16,12),(17,11)]:b.reuse(n,'6.2',old,pg(n))
for n,old in[(5,23),(8,26),(9,27),(11,29),(13,31),(14,32),(19,45),(20,46),(21,49),(22,52),(23,51),(24,54)]:b.reuse(n,'6.3',old,pg(n))
add(1,('f(x)=eˣ를 손으로 그리되 y축을 지나는 모양을 강조하고 근거를 설명하라.','Sketch f(x)=eˣ by hand, emphasizing how it crosses the y-axis and the fact that determines this.'),fs(r'f(0)=1,\quad f\prime(0)=e^0=1',r'\text{Tangent at }x=0:\quad y=1+x')+[('그래프는(0,1)을 기울기1로 지나며 항상 증가하고 위로 오목하다. 왼쪽 끝 수평점근선은 y=0이다.','The graph passes through(0,1) with slope1, is increasing and concave up, and has left horizontal asymptote y=0.')],('y축 교점(0,1), 접선 y=1+x이다.','Y-intercept(0,1), tangent y=1+x.'),('미분 공식(eˣ)′=eˣ를 원점에 대입하고 양의 이계도함수로 모양을 확인했다.','Substituted zero into(eˣ)′=eˣ and used the positive second derivative to check shape.'))
plots(b,1,[('Natural exponential and tangent',-2,2,-1,8,[('e^x',math.exp),('tangent',lambda q:1+q)])])
ma(2,r'(a)e^{\ln15};\quad(b)e^{3\ln2};\quad(c)e^{-2\ln5}',[r'(a)e^{\ln15}=15',r'(b)e^{\ln(2^3)}=8',r'(c)e^{\ln(5^{-2})}=1/25'],r'(a)15;\quad(b)8;\quad(c)1/25',('지수와 자연로그의 역관계 및 로그 거듭제곱 법칙을 적용했다.','Applied the inverse exponential/logarithm relation and logarithmic power law.'),list('abc'))
ma(3,r'(a)\ln(1/e^2);\quad(b)\ln\sqrt e;\quad(c)\ln(e^{\sin x})',[r'(a)\ln(e^{-2})=-2',r'(b)\ln(e^{1/2})=1/2',r'(c)\ln(e^{\sin x})=\sin x'],r'(a)-2;\quad(b)1/2;\quad(c)\sin x',('e의 지수가 실수인 모든 경우 ln(eᵘ)=u가 성립한다.','For every real exponent u, ln(eᵘ)=u.'),list('abc'))
ma(4,r'(a)\ln(\ln(e^{e^{50}}));\quad(b)e^{\ln(\ln e^3)};\quad(c)e^{x+\ln x}',[r'(a)\ln(\ln(e^{e^{50}}))=\ln(e^{50})=50',r'(b)e^{\ln(\ln e^3)}=\ln e^3=3',r'(c)e^{x+\ln x}=e^xe^{\ln x}=xe^x,\quad x>0'],r'(a)50;\quad(b)3;\quad(c)xe^x',('안쪽 합성부터 차례로 계산하고 c의 원 로그 조건 x>0을 보존했다.','Simplified from the innermost composition outward and preserved x>0 in part c.'),list('abc'))
va=s.sqrt(1+s.exp(3));vb=(s.log(19)-1)/4
ma(6,r'(a)\ln(x^2-1)=3;\quad(b)1+e^{4x+1}=20',[r'(a)x^2-1=e^3\Rightarrow x=\pm\sqrt{1+e^3}',r'(b)e^{4x+1}=19\Rightarrow x=(\ln19-1)/4'],fr'(a)\ x=\pm\sqrt{{1+e^3}}\approx\pm{float(va):.3f};\quad(b)\ x=(\ln19-1)/4\approx{float(vb):.3f}',('a의 두 근 모두 |x|>1로 원 로그 정의역에 속하며 b도 원 지수식에 대입해 확인했다.','Both roots in a satisfy |x|>1, and substitution verifies the exponential equation in b.'),['a','b'])
va=(1+s.sqrt(5))/2;vb=-s.log(s.E-1)/2
ma(7,r'(a)\ln x+\ln(x-1)=0;\quad(b)e-e^{-2x}=1',[r'(a)x>1,\quad\ln[x(x-1)]=0\Rightarrow x^2-x-1=0',r'x=(1+\sqrt5)/2\quad\text{(negative root excluded)}',r'(b)e^{-2x}=e-1\Rightarrow x=-\tfrac12\ln(e-1)'],fr'(a)\ (1+\sqrt5)/2\approx{float(va):.3f};\quad(b)\ -\tfrac12\ln(e-1)\approx{float(vb):.3f}',('a의 음의 근은 원 로그 정의역 밖이다. b의 로그 입력 e−1은 양수이다.','The negative quadratic root in a is outside the original logarithmic domain; e−1 in b is positive.'),['a','b'])
ma(10,r'(a)e^{3x+1}=k;\quad(b)\ln(2x+1)=2-\ln x',[r'(a)k>0\Rightarrow x=(\ln k-1)/3;\quad k\le0:\ \text{no real solution}',r'(b)x>0:\ \ln[x(2x+1)]=2\Rightarrow2x^2+x-e^2=0',r'x=(-1+\sqrt{1+8e^2})/4'],r'(a)\ x=(\ln k-1)/3\ (k>0);\quad(b)\ x=\frac{-1+\sqrt{1+8e^2}}4',('매개변수의 양수 조건과 이차방정식의 양의 가지를 모두 원식에서 확인했다.','Checked the positive parameter condition and the positive quadratic branch against the originals.'),['a','b'])
va=4+1/s.log(7);vb=1/(s.E**2-1)
ma(12,r'(a)e^{1/(x-4)}=7;\quad(b)\ln\frac{x+1}x=2',[r'(a)1/(x-4)=\ln7\Rightarrow x=4+1/\ln7',r'(b)(x+1)/x=e^2\Rightarrow x=1/(e^2-1)'],fr'(a)\ x\approx{float(va):.4f};\quad(b)\ x\approx{float(vb):.4f}',('a의 해는4가 아니고 b의 해는 양수여서 두 원식 모두 정의된다.','The solution in a differs from4 and the solution in b is positive, so both originals are defined.'),['a','b'])
add(18,('y=2(1−eˣ)의 개형을 변환으로 그려라.','Sketch y=2(1−eˣ) using transformations.'),fs(r'y=-2e^x+2,\quad y\prime=-2e^x<0,\quad y\prime\prime=-2e^x<0')+[('eˣ를 x축에 반사하고 세로2배 확대한 뒤 위로2 이동한다. 정의역 R, 치역(−∞,2), 절편(0,0), 왼쪽 수평점근선 y=2이다.','Reflect eˣ across the x-axis, stretch vertically by2, then shift up2. Domain R, range(−∞,2), intercept(0,0), left horizontal asymptote y=2.')],('항상 감소하고 아래로 오목한 그래프이다.','The graph is decreasing and concave down everywhere.'),('x=0의 값과 양끝 극한을 직접 대입하여 변환을 확인했다.','Checked the transformation using the value at zero and both end limits.'))
plots(b,18,[('Transformed exponential',-4,2,-13,3,[('2(1-e^x)',lambda q:2*(1-math.exp(q)))])])
add(72,('y=e²ˣ−eˣ의 정의역·절편·극한·증가감소·극값·오목성·변곡점을 조사하고 그려라.','Analyze and sketch y=e²ˣ−eˣ: domain, intercepts, limits, monotonicity, extrema, concavity and inflections.'),fs(r'y\prime=e^x(2e^x-1),\quad y\prime\prime=e^x(4e^x-1)',r'y\prime=0\iff x=-\ln2,\quad y\prime\prime=0\iff x=-\ln4',r'\lim_{x\to-\infty}y=0^-,\quad\lim_{x\to\infty}y=\infty')+[('정의역 R, 유일한 절편은 원점이다. −ln2까지 감소한 뒤 증가하며 절대최소는(−ln2,−1/4)이다. x<−ln4에서 아래로, x>−ln4에서 위로 오목하고 변곡점은(−ln4,−3/16)이다.','Domain R; the only intercept is the origin. Decreases to−ln2, then increases, with absolute minimum(−ln2,−1/4). Concave down for x<−ln4 and up for x>−ln4; inflection(−ln4,−3/16).')],same(M(r'\min y=-1/4\text{ at }x=-\ln2;\quad \mathrm{IP}=(-\ln4,-3/16)')),('eˣ가 항상 양수이므로 나머지 선형 인수로 두 도함수의 부호를 판정했다.','Since eˣ is positive, the remaining linear factors determine derivative signs.'))
plots(b,72,[('Difference of exponentials',-4,1,-.4,5,[('e^(2x)-e^x',lambda q:math.exp(2*q)-math.exp(q))])])
ma(105,r'e^{x-y}=e^x/e^y',[r'\ln(e^x/e^y)=\ln(e^x)-\ln(e^y)=x-y',r'\ln(e^{x-y})=x-y\Rightarrow e^{x-y}=e^x/e^y'],r'e^{x-y}=e^x/e^y',('자연로그가 일대일이고 모든 지수값은 양수이므로 로그의 동일성에서 원값의 동일성을 얻는다.','The natural logarithm is one-to-one and exponential values are positive, so equality of logarithms gives equality of values.'))
ma(106,r'(e^x)^r=e^{rx}',[r'\ln[(e^x)^r]=r\ln(e^x)=rx',r'\ln(e^{rx})=rx\Rightarrow(e^x)^r=e^{rx}'],r'(e^x)^r=e^{rx}',('밑 eˣ가 양수이므로 실수 r 거듭제곱에 대한 로그 법칙을 사용할 수 있다.','The positive base eˣ permits the logarithm power law for real r.'))
# Alternative31–50 are verbatim mathematical matches; no exercise-number references changed inside their formulas.
for n in[6,7,12]:
 b.E[n]['statement']['ko']=b.E[n]['statement']['ko'].replace('계산하거나 증명하라.','방정식을 풀고 지정 자릿수로 근사하라.');b.E[n]['statement']['en']=b.E[n]['statement']['en'].replace('Evaluate or prove.','Solve and round to the requested precision.')
b.save();print('6.3* COMPLETE',len(b.E))
for n in[19,20]:b.E[n]['subparts']=['a','b']
b.E[10]['answer']=pair(M(r'(a)\begin{cases}x=(\ln k-1)/3&k>0\\\text{no real solution}&k\le0\end{cases};\quad(b)\ x=\frac{-1+\sqrt{1+8e^2}}4'))
b.save()
