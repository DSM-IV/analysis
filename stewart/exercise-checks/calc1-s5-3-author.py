from calc1_shell_helpers import *
x,y=s.symbols('x y',real=True);P=s.pi;R=s.Rational;b=CalcBook('5.3',[392,393,394,395])
# intervals, right/top, left/bottom, radius
records={
1:(r'y=x(x-1)^2,\ y=0,\ 0\le x\le1',[(0,1,x*(x-1)**2,0,x)],x,0),
2:(r'y=\sin(x^2),\ y=0,\ 0\le x\le\sqrt\pi',[(0,s.sqrt(P),s.sin(x*x),0,x)],x,0),
3:(r'y=\cos(x^2),\ y=0,\ 0\le x\le\sqrt{\pi/2}',[(0,s.sqrt(P/2),s.cos(x*x),0,x)],x,0),
4:(r'y=\sqrt x,\ y=2-x,\ y=0',[(0,1,2-y,y*y,y)],y,0),
5:(r'y=x^{1/4},\ y=0,\ x=2',[(0,2,x**R(1,4),0,x)],x,0),
6:(r'y=x^3,\ y=8,\ x=0',[(0,8,y**R(1,3),0,y)],y,0),
7:(r'y=\sqrt{x+4},\ y=0,\ x=0',[(0,2,0,y*y-4,3-y)],y,3),
8:(r'y=4x-x^2,\ y=x',[(0,3,4*x-x*x,x,7-x)],x,7),
9:(r'y=\sqrt x,\ y=0,\ x=4',[(0,4,s.sqrt(x),0,x)],x,0),
10:(r'y=x^3,\ y=0,\ x=1,2',[(1,2,x**3,0,x)],x,0),
11:(r'y=1/x,\ y=0,\ x=1,4',[(1,4,1/x,0,x)],x,0),
12:(r'y=x^2,\ y=4,\ x=0,\ 0\le x\le2',[(0,2,4,x*x,x)],x,0),
13:(r'y=\sqrt{5+x^2},\ y=0,\ x=0,2',[(0,2,s.sqrt(5+x*x),0,x)],x,0),
14:(r'y=4x-x^2,\ y=x',[(0,3,4*x-x*x,x,x)],x,0),
15:(r'xy=1,\ x=0,\ y=1,3',[(1,3,1/y,0,y)],y,0),
16:(r'y=\sqrt x,\ x=0,\ y=2',[(0,2,y*y,0,y)],y,0),
17:(r'y=x^{3/2},\ y=8,\ x=0',[(0,8,y**R(2,3),0,y)],y,0),
18:(r'x=-3y^2+12y-9,\ x=0',[(1,3,-3*y*y+12*y-9,0,y)],y,0),
19:(r'x=1+(y-2)^2,\ x=2',[(1,3,2,1+(y-2)**2,y)],y,0),
20:(r'x+y=4,\ x=y^2-4y+4',[(0,3,4-y,y*y-4*y+4,y)],y,0),
21:(r'y=x^2,\ y=8\sqrt x',[(0,4,8*s.sqrt(x),x*x,x)],x,0),
22:(r'y=x^3,\ y=4x^2',[(0,64,y**R(1,3),s.sqrt(y)/2,y)],y,0),
23:(r'y=4x-x^2,\ y=0',[(0,4,4*x-x*x,0,x+2)],x,-2),
24:(r'y=\sqrt x,\ y=x^3',[(0,1,y**R(1,3),y*y,y+1)],y,-1),
25:(r'y=x^3,\ y=8,\ x=0',[(0,2,8,x**3,3-x)],x,3),
26:(r'y=4-2x,\ y=0,\ x=0',[(0,2,4-2*x,0,x+1)],x,-1),
27:(r'y=4x-x^2,\ y=3',[(1,3,4*x-x*x,3,x-1)],x,1),
28:(r'y=\sqrt x,\ x=2y',[(0,4,s.sqrt(x),x/2,5-x)],x,5),
29:(r'x=2y^2,\ y\ge0,\ x=2',[(0,1,2,2*y*y,2-y)],y,2),
30:(r'x=2y^2,\ x=y^2+1',[(-1,1,y*y+1,2*y*y,y+2)],y,-2),
31:(r'y=\sin x,\ y=0,\ x=2\pi,3\pi',[(2*P,3*P,s.sin(x),0,x)],x,0),
32:(r'y=\tan x,\ y=0,\ x=\pi/4',[(0,P/4,s.tan(x),0,P/2-x)],x,P/2),
33:(r'y=\cos^4x,\ y=-\cos^4x,\ -\pi/2\le x\le\pi/2',[(-P/2,P/2,s.cos(x)**4,-s.cos(x)**4,P-x)],x,P),
34:(r'y=x,\ y=2x/(1+x^3)',[(0,1,2*x/(1+x**3),x,x+1)],x,-1),
35:(r'x=\sqrt{\sin y},\ x=0,\ 0\le y\le\pi',[(0,P,s.sqrt(s.sin(y)),0,4-y)],y,4),
36:(r'x^2-y^2=7,\ x=4',[(-3,3,4,s.sqrt(y*y+7),5-y)],y,5),
45:(r'y=\sin^2x,\ y=\sin^4x,\ 0\le x\le\pi',[(0,P/2,s.sin(x)**2,s.sin(x)**4,P/2-x)],x,P/2),
46:(r'y=x^3\sin x,\ y=0,\ 0\le x\le\pi',[(0,P,x**3*s.sin(x),0,x+1)],x,-1),
47:(r'y=1-\sqrt[3]x,\ y=x-1,\ x=0',[(0,1,1-x**R(1,3),x-1,x)],x,0),
50:(r'y=4x-x^2,\ y=x',[(0,3,4*x-x*x,x,x)],x,0),
51:(r'y=x^2,\ y=x^3,\ 0\le x\le1/2',[(0,R(1,2),x*x,x**3,x+2)],x,-2),
52:(r'x=3y-y^2,\ x=2',[(1,2,3*y-y*y,2,3-y)],y,3),
53:(r'y=-x^2+6x-8,\ y=0',[(2,4,-x*x+6*x-8,0,x)],x,0),
57:(r'x^2+(y-1)^2=1',[(0,1,1+s.sqrt(1-x*x),1-s.sqrt(1-x*x),x)],x,0),
58:(r'x=(y-3)^2,\ x=4',[(1,5,4,(y-3)**2,y-1)],y,1),
}
for n,(eq,ps,v,a)in records.items():
 axis=('x'if v==x else'y')+'='+tex(a);base=M(eq)+M(r'\text{axis: }'+axis)
 task=('원통껍질의 둘레·높이를 쓰고 부피를 계산하라.','State the shell circumference/height and compute the volume.')
 if 5<=n<=8:task=('원통껍질법 부피 적분만 세워라.','Set up, without evaluating, the shell volume integral.')
 if 31<=n<=36:task=('(a)부피 적분을 세우고 (b)소수 다섯 자리까지 계산하라.','(a)Set up the volume integral and(b)evaluate it to five decimal places.')
 if n in[21,22]:task=('x와 y를 각각 적분 변수로 사용해 두 가지 부피 적분과 값을 구하라.','Find the volume using both x and y as integration variables.')
 if n in[1,2]:task=(task[0]+' 와셔법과 편리함을 비교하라.',task[1]+' Compare its convenience with the washer method.')
 extra=[]
 if n==1:extra=[('와셔법은 y=x(x-1)²를 x에 대해 서로 다른 가지로 풀어야 한다. 수직 껍질은 원식을 그대로 쓸 수 있다.','Washers require different inverse branches of y=x(x-1)². Vertical shells use the given function directly.')]
 if n==2:extra=[('와셔법은 x²=arcsin y와 π-arcsin y 두 가지를 구해야 한다. 껍질은 u=x² 치환으로 바로 계산된다.','Washers require x²=arcsin y and π-arcsin y. Shells evaluate directly using u=x².')]
 if n==45:extra=[('회전축에 대칭인 양쪽 절반은 같은 입체를 생성한다. 왼쪽 절반만 적분하여 중복을 피한다.','The two halves symmetric about the axis generate the same solid. Integrate only the left half to avoid double counting.')]
 if n==57:extra=[('y축 양쪽 반원판이 같은 구를 생성하므로 오른쪽 반쪽만 껍질로 적분한다.','The two half-disks generate the same sphere, so integrate shells only over the right half.')]
 V=shell(b,n,392 if n<=2 else 393 if n<=36 else 394,(base+task[0],base+task[1]),ps,v,a,setup=5<=n<=8,numeric=31<=n<=36,extra=extra,parts=list('ab')if n in[3,4,21,22] or 31<=n<=36 or 47<=n<=52 else list('abc')if n in[23,24]else[])
 if n in[21,22]:
  wI=s.Integral(P*(y-(y/8)**4),(y,0,16))if n==21 else s.Integral(P*(16*x**4-x**6),(x,0,4));wV=s.simplify(wI.doit());assert s.simplify(wV-V)==0
  for lang in['ko','en']:b.E[n]['steps'][lang]+=[M(r'\text{Washer method: }'+s.latex(wI)+'='+tex(wV))]
 b.save()
print('5.3 shell entries',len(b.E))
def add(n,st,steps,ans,check,parts=[]):
 b.add(n,394 if n<=61 else 395,('껍질과 부피 응용','Shells and volume applications'),st,steps,ans,parts=parts);b.verify(n,*check)
mids=[R(1,10),R(3,10),R(5,10),R(7,10),R(9,10)];vmid=sum(2*P*t*s.sqrt(1+t**3)for t in mids)/5
add(37,('y=√(1+x³),0≤x≤1 아래 영역을 y축에 관해 회전한다. n=5 중점법으로 부피를 추정하라.','Revolve the region under y=√(1+x³),0≤x≤1 about y. Estimate volume with n=5 midpoints.'),fs(r'\Delta x=.2,\quad x_i^*=.1,.3,.5,.7,.9',r'V\approx.2\sum_{i=1}^{5}2\pi x_i^*\sqrt{1+(x_i^*)^3}'),same(M(r'V\approx'+f'{float(vmid):.6f}')),('중점에서 높이만이 아니라 반지름과 높이의 곱을 평가했다.','Evaluated radius times height at each midpoint, not height alone.'))
add(38,('원본 영역은0≤x≤10이다. y축 회전 부피를 n=5 중점법으로 추정하라. x=1,3,5,7,9에서 위·아래 경계 차를 그림에서 읽으면 약2,4,3,2,2이다.','The source region spans0≤x≤10. Estimate its y-axis rotation volume using n=5 midpoints. At x=1,3,5,7,9 the graph gives approximate upper-minus-lower heights2,4,3,2,2.'),fs(r'\Delta x=2,\quad V\approx2\sum_{i=1}^{5}2\pi x_i^*h_i',r'V\approx4\pi(1\cdot2+3\cdot4+5\cdot3+7\cdot2+9\cdot2)=244\pi'),same(M(r'V\approx244\pi\approx766.55')),('자료의 높이는 곡선 값 자체가 아니라 두 곡선의 차이다. 다른 판독값은 가까운 추정값을 준다.','Heights are differences of the two curves, not individual function values; other readings give nearby estimates.'))
for n,eq,rh,desc in[
(39,r'\int_0^3 2\pi x^5dx',r'r=x,\ h=x^4',('y=x⁴ 아래0≤x≤3을 y축에 관해 회전한다.','Revolve the region under y=x⁴ on0≤x≤3 about y.')),
(40,r'\int_1^5 2\pi y\sqrt{y-1}\,dy',r'r=y,\ h=\sqrt{y-1}',('0≤x≤√(y-1),1≤y≤5를 x축에 관해 회전한다.','Revolve0≤x≤√(y-1),1≤y≤5 about x.')),
(41,r'2\pi\int_1^4\frac{y+2}{y^2}\,dy',r'r=y+2,\ h=1/y^2',('0≤x≤1/y²,1≤y≤4를 y=-2에 관해 회전한다.','Revolve0≤x≤1/y²,1≤y≤4 about y=-2.')),
(42,r'\int_0^{\pi/2}2\pi(x+1)(2x-\sin x)dx',r'r=x+1,\ h=2x-\sin x',('sin x≤y≤2x,0≤x≤π/2를 x=-1에 관해 회전한다.','Revolve sin x≤y≤2x,0≤x≤π/2 about x=-1.'))]:
 add(n,(M(eq)+'가 부피를 나타내는 회전체를 하나 설명하라.',M(eq)+'Describe one solid whose volume is represented by this integral.'),[desc]+fs(rh,r'dV=2\pi rh\,d'+('x'if n in[39,42]else'y')),desc,('반지름·껍질 높이·적분 범위를 각각 원 적분과 대조했다.','Matched the radius, shell height, and integration limits to the original integral.'))
for n,eq,f,g,seeds in[
(43,r'y=x^2-2x,\ y=x/(x^2+1)',x/(x*x+1),x*x-2*x,[0,2.2]),
(44,r'y=3\sin x,\ y=x^2-4x+5',3*s.sin(x),x*x-4*x+5,[1,2.8])]:
 fn=s.lambdify(x,f-g,'mpmath');roots=[mp.mpf(0)if q==0 else mp.findroot(fn,q)for q in seeds];lo,hi=[s.Float(str(mp.re(z)),33)for z in roots]
 shell(b,n,394,(M(eq)+'의 교점을 그래프로 추정하고 유계영역을 y축에 관해 회전한 부피를 계산하라.',M(eq)+'Estimate the intersections graphically and compute the y-axis rotation volume of the bounded region.'),[(lo,hi,f,g,x)],x,numeric=True,extra=fs(r'x_1\approx'+f'{float(lo):.9f}'+r',\quad x_2\approx'+f'{float(hi):.9f}'));b.save()
washers={
48:(r'y=2-x^2,\ y=x^2,\ x=0',[(0,1,2-x*x,x*x)],x,0),
49:(r'y=\sqrt{\sin x},\ y=0,\ 0\le x\le\pi',[(0,P,s.sqrt(s.sin(x)),0)],x,0),
54:(r'y=-x^2+6x-8,\ y=0',[(2,4,-x*x+6*x-8,0)],x,0),
55:(r'y^2-x^2=1,\ y=2',[(-s.sqrt(3),s.sqrt(3),2,s.sqrt(1+x*x))],x,0),
56:(r'y^2-x^2=1,\ y=2',[(1,2,s.sqrt(y*y-1),0)],y,0),
59:(r'x=(y-1)^2,\ x-y=1',[(0,3,y+2,(y-1)**2+1)],y,-1)}
for n,(eq,ps,v,a)in washers.items():
 axis=('y'if v==x else'x')+'='+str(a)
 volume(b,n,394,(M(eq)+M(r'\text{axis: }'+axis)+'에 관해 회전하는 부피 적분을 세우고 계산하라.',M(eq)+M(r'\text{axis: }'+axis)+'Set up and evaluate the rotation-volume integral.'),ps,v,a,parts=['a','b']if n<=52 else[]);b.save()
add(60,('꼭짓점(0,0),(1,0),(1,2)인 삼각형을 x=a(a>1)에 관해 회전한 부피가V이다. a를 V로 나타내라.','A triangle with vertices(0,0),(1,0),(1,2) rotates about x=a(a>1) with volume V. Express a in terms of V.'),fs(r'0\le x\le1,\quad r=a-x,\quad h=2x',r'V=2\pi\int_0^1(a-x)2x\,dx=2\pi a-4\pi/3'),same(M(r'a=\frac{V}{2\pi}+\frac23,\qquad V>2\pi/3')),('삼각형 넓이1, 도심 x=2/3의 회전 거리2π(a-2/3)로도 같은 값을 얻는다.','The area1 triangle has centroid x=2/3; its travel distance2π(a-2/3) gives the same volume.'))
add(61,('반지름r인 구의 부피를 원통껍질법으로 구하라.','Use cylindrical shells to find the volume of a radius-r sphere.'),fs(r'0\le x\le r,\quad h(x)=2\sqrt{r^2-x^2}',r'V=4\pi\int_0^r x\sqrt{r^2-x^2}dx',r'u=r^2-x^2\Rightarrow V=2\pi\int_0^{r^2}u^{1/2}du=4\pi r^3/3'),same(M(r'V=4\pi r^3/3')),('반원 오른쪽만 회전해 중복을 피했고 원판법의 구 부피와 일치한다.','Rotated only the right half to avoid overlap; the result agrees with the disk-method sphere volume.'))
add(62,('관 반지름r, 중심 원 반지름R>r인 토러스의 부피를 원통껍질법으로 구하라.','Use cylindrical shells for a torus with tube radius r and central-circle radius R>r.'),fs(r'V=4\pi\int_{R-r}^{R+r}x\sqrt{r^2-(x-R)^2}dx',r'u=x-R\Rightarrow V=4\pi\int_{-r}^{r}(u+R)\sqrt{r^2-u^2}du')+[('u항은 홀함수라 적분0, 나머지는 R과 반원의 넓이의 곱이다.','The u term is odd and integrates to zero; the remaining term is R times a semicircle area.')]+fs(r'V=4\pi R(\pi r^2/2)=2\pi^2Rr^2'),same(M(r'V=2\pi^2Rr^2')),('와셔법5.2.75의 결과와 독립적으로 일치한다.','Independently agrees with the washer result in5.2.75.'))
add(63,('밑면 반지름r, 높이h인 직각 원뿔의 부피를 원통껍질법으로 구하라.','Use cylindrical shells to find the volume of a right cone of base radius r and height h.'),fs(r'H(x)=h(1-x/r),\quad0\le x\le r',r'V=2\pi h\int_0^r x(1-x/r)dx=2\pi h(r^2/2-r^2/3)=\pi r^2h/3'),same(M(r'V=\pi r^2h/3')),('껍질 높이가 축에서h, 밑면 가장자리에서0이며 원판법과 일치한다.','Shell height is h at the axis and0 at the base edge; the result agrees with disks.'))
add(64,('서로 다른 크기의 구에 중심 구멍을 뚫어 만든 두 냅킨 고리의 높이가 모두h이다. (a)어느 부피가 큰지 예측하고,(b)구 반지름R·구멍 반지름r의 껍질 적분으로 검증하여 h만의 식으로 나타내라.','Two napkin rings made from different spheres and central bore sizes have equal height h. (a)Predict which has more volume. (b)Verify with a shell integral for sphere radius R and bore radius r, then express the volume using h alone.'),[('같은 높이이면 부피도 같다. 껍질 반지름을 ρ로 두면 r≤ρ≤R이다.','Equal height gives equal volume. Shell radius ρ ranges from r to R.')]+fs(r'V=4\pi\int_r^R\rho\sqrt{R^2-\rho^2}d\rho=\frac{4\pi}{3}(R^2-r^2)^{3/2}',r'h=2\sqrt{R^2-r^2}\Rightarrow V=\pi h^3/6'),same(M(r'V_1=V_2=\pi h^3/6')),('남는 식에서 R,r이 따로 사라지며5.2.84의 와셔법과도 일치한다.','R and r disappear separately from the final formula, which also agrees with the washer result in5.2.84.'),['a','b'])
assert sorted(b.E)==list(range(1,65));b.save();print('5.3 COMPLETE',len(b.E))
def linear(table,t):
 for (u,a),(v,c)in zip(table,table[1:]):
  if u<=t<=v:return a+(c-a)*(t-u)/(v-u)
 return table[-1][1]
upper=[(0,3),(1,4),(2,4.6),(3,5),(4,4.8),(5,4),(6,3.6),(7,4),(8,4.35),(9,4),(10,3)]
lower=[(0,3),(1,2),(2,1.6),(3,1),(4,.6),(5,1),(6,1.65),(7,2),(8,1.8),(9,2),(10,3)]
b.plot(38,[(lambda x,u:(x,linear(lower,x)+u*(linear(upper,x)-linear(lower,x)),0),(0,10),(0,1),'Approximate source region'),([lambda x,t:(x*math.cos(t),linear(upper,x),x*math.sin(t)),lambda x,t:(x*math.cos(t),linear(lower,x),x*math.sin(t))],(0,10),(0,2*math.pi),'Approximate y-axis rotation')],('원본 그래프 판독점을 선형 보간해 재구성한 근사도. 부피는 해설의 다섯 중점에서 계산한다.','Original approximation reconstructed by linear interpolation of source-graph readings. Volume uses the five stated midpoints.'))
for n in[21,22]:
 for lang in['ko','en']:
  b.E[n]['steps'][lang].insert(0,'(a) x — cylindrical shells'if n==21 else'(b) y — cylindrical shells');b.E[n]['steps'][lang][-1]='(b) y — '+b.E[n]['steps'][lang][-1]if n==21 else'(a) x — '+b.E[n]['steps'][lang][-1]
b.save()
