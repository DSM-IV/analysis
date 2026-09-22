from calc1_helpers import *
from calc1_plot_helpers import plots
x,y,t,u=s.symbols('x y t u',real=True);a,c=s.symbols('a b',real=True,nonzero=True);Q=s.Rational;pi=s.pi
b=CalcBook('7.4',[553,554,555]);checks=[]
def pg(n):return 553 if n<=59 else 554 if n<=76 else 555
def add(n,st,steps,ans,ck,parts=[]):
 b.add(n,pg(n),('부분분수 적분','Integration by partial fractions'),st,steps,ans,parts=parts);b.verify(n,*ck);b.save()
def ma(n,eq,steps,ans,ck,parts=[]):add(n,(M(eq)+'계산하거나 증명하라.',M(eq)+'Evaluate or prove.'),fs(*steps),same(M(ans)),ck,parts)
forms={1:[(1/((x-3)*(x+5)),r'\frac A{x-3}+\frac B{x+5}'),((2*x+5)/((x-2)**2*(x*x+2)),r'\frac A{x-2}+\frac B{(x-2)^2}+\frac{Cx+D}{x^2+2}')],2:[((x-6)/(x*x+x-6),r'\frac A{x+3}+\frac B{x-2}'),(1/(x*x+x**4),r'\frac Ax+\frac B{x^2}+\frac{Cx+D}{x^2+1}')],3:[((x*x+4)/(x**3-3*x*x+2*x),r'\frac Ax+\frac B{x-1}+\frac C{x-2}'),((x**3+x)/(x*(2*x-1)**2*(x*x+3)**2),r'\frac Ax+\frac B{2x-1}+\frac C{(2x-1)^2}+\frac{Dx+E}{x^2+3}+\frac{Fx+G}{(x^2+3)^2}')],4:[(5/(x**4-1),r'\frac A{x-1}+\frac B{x+1}+\frac{Cx+D}{x^2+1}'),((x**4+x+1)/((x**3-1)*(x*x-1)),r'\frac A{x-1}+\frac B{(x-1)^2}+\frac C{x+1}+\frac{Dx+E}{x^2+x+1}')],5:[((x**5+1)/((x*x-x)*(x**4+2*x*x+1)),r'\frac Ax+\frac B{x-1}+\frac{Cx+D}{x^2+1}+\frac{Ex+F}{(x^2+1)^2}'),(x*x/(x*x+x-6),r'1+\frac A{x+3}+\frac B{x-2}')],6:[(x**6/(x*x-4),r'x^4+4x^2+16+\frac A{x-2}+\frac B{x+2}'),(x**4/((x*x-x+1)*(x*x+2)**2),r'\frac{Ax+B}{x^2-x+1}+\frac{Cx+D}{x^2+2}+\frac{Ex+F}{(x^2+2)^2}')]}
for n,items in forms.items():
 st=';\\quad'.join(f'({p})'+s.latex(f)for p,(f,F)in zip('ab',items));ans=';\\quad'.join(f'({p})'+F for p,(f,F)in zip('ab',items))
 add(n,(M(st)+'부분분수 분해의 형식만 쓰고 미정계수는 구하지 마라.',M(st)+'Write only the partial-fraction form without finding coefficients.'),[('분모를 실수 일차인수와 기약 이차인수로 분해한다. 가분수는 먼저 다항식 나눗셈을 한다.','Factor the denominator into real linear and irreducible quadratic factors; first divide if the fraction is improper.'),('반복 인수는1차부터 그 중복도까지 모두 포함하고, 이차인수 위에는1차 이하 분자를 둔다.','Include every power up to each multiplicity; an irreducible quadratic receives a numerator of degree at most one.')]+fs(ans),same(M(ans)),('분자 차수와 반복인수의 모든 항을 확인했다. 원 식에서 약분되는 인수의 계수는0이 될 수 있다.','Checked numerator degrees and all repeated-factor terms; a canceled factor may receive coefficient zero.'),['a','b'])
def real_logs(F):return F.replace(lambda z:z.func==s.log,lambda z:s.log(s.Abs(z.args[0])))
def rational(n,f,q=x,lo=None,hi=None,extra=[],sub=None,orig=None):
 f=s.cancel(f);A=s.apart(f,q,extension=s.sqrt(5)if n==38 else None);assert s.cancel(A-f)==0
 terms=s.Add.make_args(A);G=sum(s.integrate(term,q)for term in terms);assert not G.has(s.Integral),(n,G);assert s.simplify(s.diff(G,q)-f)==0,(n,'derivative');F=real_logs(G)
 steps=list(extra)+fs(s.latex(f)+'='+s.latex(A),r'\int '+s.latex(f)+r'\,d'+s.latex(q)+'='+s.latex(F)+'+C')
 if sub is not None:
  F=F.subs(q,sub);I=orig;outq=x
  steps+=fs('F(x)='+s.latex(F))
 else:I=s.Integral(f,q if lo is None else(q,lo,hi));outq=q
 if lo is None:ans=s.latex(F)+'+C'
 else:
  val=s.simplify(F.subs(outq,hi)-F.subs(outq,lo));ans=s.latex(val);steps+=fs(s.latex(I)+'=F('+s.latex(hi)+')-F('+s.latex(lo)+')='+ans)
  ff=s.lambdify(outq,(orig.function if sub is not None else f),'mpmath');num=mp.quad(ff,[float(lo),float(hi)]);assert abs(float(val)-float(num))<1e-7*max(1,abs(float(num))),(n,val,num)
 add(n,(M(s.latex(I))+'부분분수와 필요한 치환으로 적분하라.',M(s.latex(I))+'Integrate using partial fractions and an appropriate substitution.'),steps,same(M(ans)),('부분분수를 통분하여 원 유리함수와 기호적으로 일치함을 확인하고 원시함수를 미분했다. 로그 절댓값은 실수 정의역의 각 구간에서 적용한다.','Recombined the fractions symbolically and differentiated the primitive. Logarithmic absolute values apply on each component of the real domain.'));checks.append(n);return F
rows={7:5/((x-1)*(x+4)),8:(x-12)/(x*x-4*x),9:(5*x+1)/((2*x+1)*(x-1)),10:y/((y+4)*(2*y-1)),11:2/(2*x*x+3*x+1),12:(x-4)/(x*x-5*x+6),13:1/(x*(x-a)),14:1/((x+a)*(x+c)),15:x*x/(x-1),16:(3*t-2)/(t+1),17:(4*y*y-7*y-12)/(y*(y+2)*(y-3)),18:(3*x*x+6*x+2)/(x*x+3*x+2),19:(x*x+x+1)/((x+1)**2*(x+2)),20:x*(3-5*x)/((3*x-1)*(x-1)**2),21:1/(t*t-1)**2,22:(3*x*x+12*x-20)/(x**4-8*x*x+16),23:10/((x-1)*(x*x+9)),24:(3*x*x-x+8)/(x**3+4*x),25:(x**3-4*x+1)/(x*x-3*x+2),26:(x**3+4*x*x+x-1)/(x**3+x*x),27:4*x/(x**3+x*x+x+1),28:(x*x+x+1)/(x*x+1)**2,29:(x**3+4*x+3)/(x**4+5*x*x+4),30:(x**3+6*x-2)/(x**4+6*x*x),31:(x+4)/(x*x+2*x+5),32:x/(x*x+4*x+13),33:1/(x**3-1),34:(x**3-2*x*x+2*x-5)/(x**4+4*x*x+3),35:(x**3+2*x)/(x**4+4*x*x+3),36:(x**5+x-1)/(x**3+1),37:(5*x**4+7*x*x+x+2)/(x*(x*x+1)**2),38:(x**4+3*x*x+1)/(x**5+5*x**3+5*x),39:(x*x-3*x+7)/(x*x-4*x+6)**2,40:(x**3+2*x*x+3*x-2)/(x*x+2*x+2)**2}
bounds={11:(0,1),12:(0,1),17:(1,2),18:(1,2),19:(0,1),20:(2,3),25:(-1,0),26:(1,2),32:(0,1),35:(0,1)}
for n,f in rows.items():
 q=y if n in[10,17]else t if n in[16,21]else x
 lo,hi=bounds.get(n,(None,None));rational(n,f,q,lo,hi)
 if n==13:
  for lang in ['ko','en']:b.E[n]['answer'][lang]+=M(r'a=0:\quad-1/x+C')
 if n==14:
  for lang in ['ko','en']:b.E[n]['answer'][lang]+=M(r'a=b:\quad-1/(x+a)+C')
# Rationalizing substitutions. q=u is the rational integration variable; output variable remains x.
subs=[(41,1/(x*s.sqrt(x-1)),s.sqrt(x-1),2/(u*u+1),r'u=\sqrt{x-1},\quad x=u^2+1,\ dx=2u du'),(42,1/(2*s.sqrt(x+3)+x),s.sqrt(x+3),2*u/(u*u+2*u-3),r'u=\sqrt{x+3},\quad x=u^2-3,\ dx=2u du'),(43,1/(x*x+x*s.sqrt(x)),s.sqrt(x),2/(u*u*(u+1)),r'u=\sqrt x,\quad x=u^2,\ dx=2u du'),(44,1/(1+x**Q(1,3)),x**Q(1,3),3*u*u/(1+u),r'u=\sqrt[3]x,\quad x=u^3,\ dx=3u^2du'),(45,x**3/(x*x+1)**Q(1,3),(x*x+1)**Q(1,3),Q(3,2)*u*(u**3-1),r'u=\sqrt[3]{x^2+1},\quad x^2=u^3-1,\quad xdx=3u^2du/2'),(46,1/(1+s.sqrt(x))**2,s.sqrt(x),2*u/(1+u)**2,r'u=\sqrt x,\quad dx=2u du'),(47,1/(s.sqrt(x)-x**Q(1,3)),x**Q(1,6),6*u**3/(u-1),r'u=\sqrt[6]x,\quad x=u^6,\ dx=6u^5du'),(48,1/(x-x**Q(1,5)),s.real_root(x,5),5*u**3/(u**4-1),r'u=\sqrt[5]x\ \text{(real)},\quad x=u^5,\ dx=5u^4du'),(49,1/(x-3*s.sqrt(x)+2),s.sqrt(x),2*u/((u-1)*(u-2)),r'u=\sqrt x,\quad dx=2u du'),(50,s.sqrt(1+s.sqrt(x))/x,s.sqrt(1+s.sqrt(x)),4*u*u/(u*u-1),r'u=\sqrt{1+\sqrt x},\quad x=(u^2-1)^2,\ dx=4u(u^2-1)du'),(51,s.exp(2*x)/(s.exp(2*x)+3*s.exp(x)+2),s.exp(x),u/((u+1)*(u+2)),r'u=e^x,\quad dx=du/u'),(52,s.sin(x)/(s.cos(x)**2-3*s.cos(x)),s.cos(x),-1/(u*u-3*u),r'u=\cos x,\quad du=-\sin xdx'),(53,s.sec(x)**2/(s.tan(x)**2+3*s.tan(x)+2),s.tan(x),1/((u+1)*(u+2)),r'u=\tan x,\quad du=\sec^2xdx'),(54,s.exp(x)/((s.exp(x)-2)*(s.exp(2*x)+1)),s.exp(x),1/((u-2)*(u*u+1)),r'u=e^x,\quad du=e^xdx'),(55,1/(1+s.exp(x)),s.exp(x),1/(u*(1+u)),r'u=e^x,\quad dx=du/u'),(56,s.cosh(x)/(s.sinh(x)**2+s.sinh(x)**4),s.sinh(x),1/(u*u+u**4),r'u=\sinh x,\quad du=\cosh xdx')]
for n,f,U,rat,eq in subs:
 lo,hi=(s.S(0),s.S(1))if n==44 else(None,None)
 rational(n,rat,u,lo,hi,extra=fs(eq),sub=U,orig=s.Integral(f,x if lo is None else(x,lo,hi)))
 # Numerical back-substitution derivative check away from poles.
 F=s.integrate(rat,u);F=real_logs(F).subs(u,U);FF=s.lambdify(x,F,'mpmath');ff=s.lambdify(x,f,'mpmath')
 if n!=48:
  for pt in [mp.mpf('.3'),mp.mpf('.6')]:assert abs(mp.diff(FF,pt)-ff(pt))<mp.mpf('1e-22'),(n,pt)
for n in [53,56]:
 for key in ['statement','steps','answer']:
  for lang in ['ko','en']:
   vv=b.E[n][key][lang]
   if isinstance(vv,list):b.E[n][key][lang]=[v.replace('x','t')for v in vv]
   else:b.E[n][key][lang]=vv.replace('x','t')
# Avoid a CAS piecewise sign form for the real fifth root.
b.E[48]['statement']=pair(M(r'\int\frac{dx}{x-\sqrt[5]x}')+'실수 다섯제곱근을 사용하라.',M(r'\int\frac{dx}{x-\sqrt[5]x}')+'Use the real fifth root.')
for lang in ['ko','en']:
 b.E[48]['steps'][lang]=[M(r'u=\sqrt[5]x,\quad dx=5u^4du'),M(r'\int\frac{5u^3}{u^4-1}du=\frac54\ln|u^4-1|'),M(r'F(x)=\frac54\ln|x^{4/5}-1|')];b.E[48]['answer'][lang]=M(r'\frac54\ln|x^{4/5}-1|+C')
b.save();print('7.4 authored',len(b.E))
D=x*x-x+2;F57=(x-Q(1,2))*s.log(D)-2*x+s.sqrt(7)*s.atan((2*x-1)/s.sqrt(7));assert s.simplify(s.diff(F57,x)-s.log(D))==0
ma(57,s.latex(s.Integral(s.log(D),x)),[r'u=\ln(x^2-x+2),\quad dv=dx',r'\int\ln Ddx=x\ln D-\int\frac{x(2x-1)}Ddx',r'\frac{x(2x-1)}D=2+\frac{x-4}D=2+\frac{D\prime/2-7/2}D',r'D=(x-1/2)^2+7/4'],s.latex(F57)+'+C',('D는 모든 실수에서 양수이며 최종식을 기호적으로 미분해 확인했다.','D is positive for all real x; symbolic differentiation verifies the result.'))
ma(58,r'\int x\arctan xdx',[r'u=\arctan x,\quad dv=xdx',r'\int x\arctan xdx=\tfrac12x^2\arctan x-\tfrac12\int\frac{x^2}{1+x^2}dx',r'\frac{x^2}{1+x^2}=1-\frac1{1+x^2}'],r'\tfrac12(x^2+1)\arctan x-x/2+C',('곱의 미분과 arctan의 미분을 합하면 x arctan x로 돌아간다.','The product and arctangent derivative terms combine to recover x arctan x.'))
f59=1/(x*x-2*x-3);rational(59,f59,x,s.S(0),s.S(2),extra=[('0≤x≤2에서 분모는 음수이다. 그래프는 약−0.3 높이로 폭2를 가지므로 적분은 대략−0.6이고 음수이다.','The denominator is negative on0≤x≤2. The graph has height roughly−0.3 over width2, suggesting a negative integral near−0.6.')]);plots(b,59,[('Negative signed area on [0,2]',0,2,-.4,0,[('f',s.lambdify(x,f59,'math'))])])
ma(60,r'\int\frac{dx}{x^2+k},\quad k\in\mathbb R',[r'k>0:\quad x=\sqrt k\,u\Rightarrow\frac1{\sqrt k}\int\frac{du}{1+u^2}',r'k=0:\quad\int x^{-2}dx=-1/x',r'k<0:\quad a=\sqrt{-k},\quad\frac1{x^2-a^2}=\frac1{2a}\left(\frac1{x-a}-\frac1{x+a}\right)'],r'\begin{cases}\frac1{\sqrt k}\arctan(x/\sqrt k)+C&k>0,\\-1/x+C&k=0,\\\frac1{2\sqrt{-k}}\ln\left|\frac{x-\sqrt{-k}}{x+\sqrt{-k}}\right|+C&k<0.\end{cases}',('k의 부호에 따라 실수 극점의 개수가 달라진다. 세 원시함수를 각각 미분하여 확인했다.','The sign of k changes the number of real poles; each primitive differentiates to the integrand.'))
rational(61,1/(x*x-2*x),extra=fs(r'x^2-2x=(x-1)^2-1'))
rational(62,(2*x+1)/(4*x*x+12*x-7),extra=fs(r'4x^2+12x-7=(2x+3)^2-16',r'2x+1=\tfrac14(8x+12)-2'))
ma(63,r't=\tan(x/2),\quad-\pi<x<\pi',[r'(a)1+t^2=\sec^2(x/2),\quad\cos(x/2)>0',r'\cos(x/2)=\frac1{\sqrt{1+t^2}},\quad\sin(x/2)=\frac{t}{\sqrt{1+t^2}}',r'(b)\cos x=\cos^2(x/2)-\sin^2(x/2)=\frac{1-t^2}{1+t^2}',r'\sin x=2\sin(x/2)\cos(x/2)=\frac{2t}{1+t^2}',r'(c)dt=\tfrac12\sec^2(x/2)dx\Rightarrow dx=\frac2{1+t^2}dt'],r'\cos(x/2)=\frac1{\sqrt{1+t^2}},\quad\sin(x/2)=\frac{t}{\sqrt{1+t^2}},\quad\cos x=\frac{1-t^2}{1+t^2},\quad\sin x=\frac{2t}{1+t^2},\quad dx=\frac2{1+t^2}dt',('반각 범위에서 코사인이 양수이므로 제곱근의 부호가 결정된다. 음수 t도 사인의 부호에 반영된다.','Cosine is positive on the half-angle interval, fixing the square-root sign; negative t preserves the sine sign.'),list('abc'))
for n,f,rat,lo,hi in[(64,1/(1-s.cos(x)),1/u**2,None,None),(65,1/(3*s.sin(x)-4*s.cos(x)),1/(2*u*u+3*u-2),None,None),(66,1/(1+s.sin(x)-s.cos(x)),1/(u*(u+1)),pi/3,pi/2),(67,s.sin(2*x)/(2+s.cos(x)),8*u*(1-u*u)/((1+u*u)**2*(3+u*u)),s.S(0),pi/2)]:
 rational(n,rat,u,lo,hi,extra=fs(r'u=\tan(x/2),\quad\sin x=2u/(1+u^2),\quad\cos x=(1-u^2)/(1+u^2),\quad dx=2du/(1+u^2)'),sub=s.tan(x/2),orig=s.Integral(f,x if lo is None else(x,lo,hi)))
for n,f in[(68,1/(x**3+x)),(69,(x*x+1)/(3*x-x*x))]:
 rational(n,f,x,s.S(1),s.S(2),extra=[('주어진 구간에서 함수가 양수이므로 정적분이 넓이이다.','The function is positive on the interval, so its definite integral is the area.')]);area_svg(b,n,[(s.S(1),s.S(2),f,s.S(0))],x,f'7.4.{n} Area under the rational curve')
va=s.simplify(pi*s.integrate(1/(x*x+3*x+2)**2,(x,0,1)));vb=s.simplify(2*pi*s.integrate(x/(x*x+3*x+2),(x,0,1)))
ma(70,r'y=1/(x^2+3x+2),\quad0\le x\le1:\ (a)x\text{-axis};\ (b)y\text{-axis}',[r'(a)V_x=\pi\int_0^1\frac{dx}{(x+1)^2(x+2)^2}',s.latex(s.apart(1/((x+1)**2*(x+2)**2),x)),r'(b)V_y=2\pi\int_0^1\frac{x\,dx}{(x+1)(x+2)}',r'\frac{x}{(x+1)(x+2)}=-\frac1{x+1}+\frac2{x+2}'],r'(a)'+s.latex(va)+r';\quad(b)'+s.latex(vb),('x축에는 원판, y축에는 껍질을 사용했다. 두 정적분을 독립 수치구적으로 확인했다.','Used disks about the x-axis and shells about the y-axis; independent quadrature verifies both integrals.'),['a','b'])
add(71,('암컷 개체수 P, 불임 수컷 수 S, 번식률 r에 대해 t=∫(P+S)/(P[(r−1)P−S])dP이다. P(0)=10000,r=1.1,S=900일 때 t와 P의 관계를 구하라.','The population model is t=∫(P+S)/(P[(r−1)P−S])dP, where P is female population,S sterile-male count and r reproduction rate. Find the relation between t and P for P(0)=10000,r=1.1,S=900.'),fs(r'\frac{P+900}{P(0.1P-900)}=\frac{10P+9000}{P(P-9000)}=-\frac1P+\frac{11}{P-9000}',r't=-\ln P+11\ln(P-9000)+C\quad(P>9000)',r'0=-\ln10000+11\ln1000+C'),same(M(r't=\ln\frac{10000}{P}+11\ln\frac{P-9000}{1000}\quad(P>9000)')),('P=10000을 대입하면 t=0이고 P로 미분하면 주어진 유리함수를 회복한다.','P=10000 gives t=0; differentiation with respect to P recovers the given rational function.'))
F72=s.log((x*x+s.sqrt(2)*x+1)/(x*x-s.sqrt(2)*x+1))/(4*s.sqrt(2))+(s.atan(s.sqrt(2)*x+1)+s.atan(s.sqrt(2)*x-1))/(2*s.sqrt(2));assert s.simplify(s.diff(F72,x)-1/(x**4+1))==0
ma(72,r'\int\frac{dx}{x^4+1}',[r'x^4+1=(x^2+1)^2-2x^2=(x^2+\sqrt2x+1)(x^2-\sqrt2x+1)',r'\frac1{x^4+1}=\frac{x/(2\sqrt2)+1/2}{x^2+\sqrt2x+1}+\frac{-x/(2\sqrt2)+1/2}{x^2-\sqrt2x+1}',r'x^2\pm\sqrt2x+1=(x\pm1/\sqrt2)^2+1/2'],s.latex(F72)+'+C',('두 이차인수는 모든 실수에서 양수이다. arctan 합 형태는 실수축 전체에서 연속이고 미분 검산이 일치한다.','Both quadratics are positive on the real line; the sum-of-arctangents form is globally continuous and differentiates correctly.'))
f73=(4*x**3-27*x*x+5*x-32)/(30*x**5-13*x**4+50*x**3-286*x*x-299*x-70)
f74=(12*x**5-7*x**3-13*x*x+8)/(100*x**6-80*x**5+116*x**4-80*x**3+41*x*x-20*x+4)
for n,f in [(73,f73),(74,f74)]:
 F=rational(n,f)
 b.E[n]['subparts']=list('ab'if n==73 else'abc')
 for lang in ['ko','en']:
  b.E[n]['statement'][lang]+= ('(a)CAS로 분해하고 (b)분해식의 각 항을 직접 적분하여 CAS의 원 식 직접 적분과 비교하라.'if lang=='ko'else'(a)Use a CAS to decompose.(b)Integrate the terms and compare against direct CAS integration.')
  b.E[n]['answer'][lang]=M('(a)'+s.latex(s.apart(f,x)))+b.E[n]['answer'][lang]
 G=s.integrate(f,x);assert s.simplify(s.diff(G,x)-f)==0
 if n==73:
  b.E[n]['steps']['ko'].append('CAS의 직접 적분과 항별 적분은 로그의 합치기·상수·복소 로그 가지 때문에 다르게 보일 수 있다. 두 결과의 도함수 차는0이다. 실수 해설은 절댓값 로그로 각 극점 사이 구간에 적용한다.')
  b.E[n]['steps']['en'].append('Direct CAS and termwise forms may look different due to logarithm combinations, constants, or complex logarithm branches. Their derivative difference is zero; the real absolute-value form applies between poles.')
 else:
  ko='(c)F′=f이다. F는 x≈−0.778246,1에서 극소, x≈0.802942에서 극대이다. x=0.4에서 F는 왼쪽에서+∞, 오른쪽에서−∞로 발산한다. F의 변곡점 x는 약−1.636031,0.877151,1.835954이다. |x|→∞이면 F는 (3/25)ln|x|처럼 증가한다.'
  en='(c)F′=f. F has local minima at x≈−0.778246 and1, and a local maximum at x≈0.802942. At x=0.4,F tends to+∞ from the left and−∞ from the right. Inflection x-values are approximately−1.636031,0.877151,1.835954. As |x|→∞,F grows like(3/25)ln|x|.'
  b.E[n]['steps']['ko'].append(ko);b.E[n]['steps']['en'].append(en);b.E[n]['answer']['ko']+=ko;b.E[n]['answer']['en']+=en
  b.E[n]['statement']['ko']+='f와 원시함수를 함께 그리고 (c)f에서 원시함수 그래프의 주요 성질을 읽어라.';b.E[n]['statement']['en']+='Plot f with its primitive and(c)infer the primitive’s main features from f.'
  plots(b,n,[('Left of the pole',-3,.35,-8,12,[('f',s.lambdify(x,f,'math')),('F',s.lambdify(x,F,'math'))]),('Right of the pole',.45,3,-12,8,[('f',s.lambdify(x,f,'math')),('F',s.lambdify(x,F,'math'))])])
add(75,('다항식 F,G와 영다항식이 아닌 Q에 대해 Q(x)≠0인 모든 x에서 F(x)/Q(x)=G(x)/Q(x)이다. 모든 실수 x에서 F(x)=G(x)임을 증명하라.','For polynomials F,G and nonzero polynomial Q, suppose F(x)/Q(x)=G(x)/Q(x) whenever Q(x)≠0. Prove F(x)=G(x) for every real x.'),[('Q(x)≠0인 점에서는 양변에 Q(x)를 곱해 F(x)=G(x)를 얻는다.','At points where Q(x)≠0, multiply by Q(x) to obtain F(x)=G(x).'),('Q는 영다항식이 아니므로 영점이 유한하다. 영점 c마다 그 밖의 점들 xₙ→c를 고를 수 있다.','A nonzero polynomial has finitely many zeros. At each zero c, choose points xₙ→c outside that finite set.'),('F,G의 연속성으로 F(c)=lim F(xₙ)=lim G(xₙ)=G(c)이다. 따라서 영점에서도 성립한다.','Continuity gives F(c)=lim F(xₙ)=lim G(xₙ)=G(c), so the identity also holds at zeros.')],same(M(r'F(x)=G(x)\quad\text{for all }x\in\mathbb R')),('Q가 영다항식이면 원래 조건이 공허해 결론을 보장하지 못하므로 유리함수 분모의 통상 조건 Q≢0을 명시했다.','If Q were identically zero, the condition would be vacuous; stated the usual nonzero-denominator-polynomial assumption.'))
add(76,('a≠0이라 하고 Iₙ=∫dx/(x²+a²)ⁿ이라 하자.(a)부분적분으로 감소공식을 유도하고(b)a=1일 때 I₂,I₃를 구하라. 원문의 식에 n−1이 분모로 있으므로 재귀는 n≥2에 적용한다.','Let a≠0 and Iₙ=∫dx/(x²+a²)ⁿ.(a)Derive the reduction formula by parts.(b)Find I₂,I₃ for a=1. The printed recurrence contains n−1 in a denominator, so it applies for n≥2.'),fs(r'I_{n-1}=\frac{x}{(x^2+a^2)^{n-1}}+2(n-1)\int\frac{x^2}{(x^2+a^2)^n}dx',r'\int\frac{x^2}{(x^2+a^2)^n}dx=I_{n-1}-a^2I_n',r'I_n=\frac{x}{2a^2(n-1)(x^2+a^2)^{n-1}}+\frac{2n-3}{2a^2(n-1)}I_{n-1}',r'a=1:\ I_1=\arctan x,\quad I_2=\frac{x}{2(x^2+1)}+\frac12\arctan x',r'I_3=\frac{x}{4(x^2+1)^2}+\frac{3x}{8(x^2+1)}+\frac38\arctan x'),same(M(r'(b)I_2=\frac{x}{2(x^2+1)}+\frac12\arctan x+C;\quad I_3=\frac{x}{4(x^2+1)^2}+\frac{3x}{8(x^2+1)}+\frac38\arctan x+C')),('n=1은 별도 초기값이며 재귀식에 직접 넣을 수 없다. 두 최종 원시함수를 미분해 확인했다.','n=1 is a separate base case and cannot be inserted into the recurrence; differentiated both final primitives.'),['a','b'])
ma(77,r'\frac1{x^n(x-a)},\quad a\ne0,\ n\in\mathbb N',[r'A=\left.\frac1{x^n}\right|_{x=a}=a^{-n}',r'\frac1{x^n(x-a)}-\frac1{a^n(x-a)}=\frac{a^n-x^n}{a^nx^n(x-a)}',r'a^n-x^n=-(x-a)\sum_{j=0}^{n-1}x^{n-1-j}a^j'],r'\frac1{a^n(x-a)}-\sum_{k=1}^n\frac1{a^{n-k+1}x^k}',('유한 등비합으로 통분하면 분자가1로 돌아온다. n=1에서 기본 두 일차분수 분해와 일치한다.','Recombination using a finite geometric sum recovers numerator1; n=1 matches the elementary two-linear-factor decomposition.'))
ma(78,r'f(x)=Ax^2+Bx+1,\quad\int\frac{f(x)}{x^2(x+1)^3}dx\ \text{rational}',[r'\frac{Ax^2+Bx+1}{x^2(x+1)^3}=\frac{B-3}x+\frac1{x^2}-\frac{B-3}{x+1}-\frac{B-2}{(x+1)^2}+\frac{A-B+1}{(x+1)^3}',r'\int=(B-3)\ln\left|\frac{x}{x+1}\right|-\frac1x+\frac{B-2}{x+1}-\frac{A-B+1}{2(x+1)^2}+C',r'\text{No logarithmic term}\Rightarrow B-3=0'],r'f\prime(0)=B=3',('유리함수의 도함수에는 단순극의 잔여항이 없으므로 두 로그 계수는0이어야 한다. B=3이면 나머지 원시함수는 유리함수이다.','A derivative of a rational function has no simple-pole residue, so the logarithmic coefficients must vanish. For B=3 the remaining primitive is rational.'))
# Compact equivalent primitive for the logarithmic derivative in38.
for lang in ['ko','en']:
 b.E[38]['answer'][lang]=M(r'\frac15\ln|x^5+5x^3+5x|+C')
 b.E[38]['steps'][lang].append(M(r'(x^5+5x^3+5x)\prime=5(x^4+3x^2+1)'))
b.save();print('7.4 COMPLETE',len(b.E))
# Zooms make the shallow extrema visible without changing the primitive constant.
F74=real_logs(sum(s.integrate(term,x)for term in s.Add.make_args(s.apart(f74,x))))
plots(b,74,[('Left of the pole',-3,.35,-8,12,[('f',s.lambdify(x,f74,'math')),('F',s.lambdify(x,F74,'math'))]),('Right of the pole',.45,3,-12,8,[('f',s.lambdify(x,f74,'math')),('F',s.lambdify(x,F74,'math'))]),('Primitive: shallow left minimum',-1.6,-.5,-6.785,-6.755,[('F',s.lambdify(x,F74,'math'))]),('Primitive: nearby maximum and minimum',.75,1.15,-6.727,-6.7235,[('F',s.lambdify(x,F74,'math'))])])
b.E[59]['statement']['ko']+='그래프로 부호와 근삿값을 추측한 뒤 정확한 값을 구하라.';b.E[59]['statement']['en']+='Guess the sign and approximate value from the graph, then find the exact value.'
b.save()
