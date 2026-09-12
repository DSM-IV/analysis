from calc1_helpers import *
x,y=s.symbols('x y',real=True);b=CalcBook('5.1',[370,371,372,373]);P=s.pi;R=s.Rational
records={
1:(r'y=3x-x^2,\ y=x',[(0,2,3*x-x*x,x)],x),
2:(r'y=\sqrt x,\ y=1/x^2,\ x=4',[(1,4,s.sqrt(x),x**-2)],x),
3:(r'x=y^2-1,\ x=\sqrt y,\ y=0,1',[(0,1,s.sqrt(y),y*y-1)],y),
4:(r'x=y^2-4y,\ x=2y-y^2',[(0,3,2*y-y*y,y*y-4*y)],y),
5:(r'y=x^3-3x,\ y=x',[(-2,0,x**3-3*x,x),(0,2,x,x**3-3*x)],x),
6:(r'y=x^2,\ 3y=2x+16,\ y=-2x+8',[(-2,1,(2*x+16)/3,x*x),(1,2,-2*x+8,x*x)],x),
7:(r'y=1/x,\ y=1/x^2,\ x=2',[(1,2,1/x,1/x**2)],x),
8:(r'y=\tan x,\ y=\sin x,\ x=1',[(0,1,s.tan(x),s.sin(x))],x),
9:(r'y=2-x,\ y=2x-x^2',[(1,2,2*x-x*x,2-x)],x),
10:(r'x=y^4,\ x=2-y^2',[(-1,1,2-y*y,y**4)],y),
11:(r'y=x^2+2,\ y=-x-1,\ x=0,1',[(0,1,x*x+2,-x-1)],x),
12:(r'y=1+x^3,\ y=2-x,\ x=-1,0',[(-1,0,2-x,1+x**3)],x),
13:(r'y=(x-2)^2,\ y=x',[(1,4,x,(x-2)**2)],x),
14:(r'y=x^2-4x,\ y=2x',[(0,6,2*x,x*x-4*x)],x),
15:(r'y=\sqrt{x+3},\ y=(x+3)/2',[(-3,1,s.sqrt(x+3),(x+3)/2)],x),
16:(r'y=\sin x,\ y=2x/\pi,\ x\ge0',[(0,P/2,s.sin(x),2*x/P)],x),
17:(r'x=1-y^2,\ x=y^2-1',[(-1,1,1-y*y,y*y-1)],y),
18:(r'4x+y^2=12,\ x=y',[(-6,2,3-y*y/4,y)],y),
19:(r'y=12-x^2,\ y=x^2-6',[(-3,3,12-x*x,x*x-6)],x),
20:(r'y=x^2,\ y=4x-x^2',[(0,2,4*x-x*x,x*x)],x),
21:(r'x=2y^2,\ x=4+y^2',[(-2,2,4+y*y,2*y*y)],y),
22:(r'y=\sqrt{x-1},\ x-y=1',[(1,2,s.sqrt(x-1),x-1)],x),
23:(r'y=\sqrt[3]{2x},\ y=x/2',[(-2,0,y**3/2,2*y),(0,2,2*y,y**3/2)],y),
24:(r'y=x^3,\ y=x',[(-1,0,x**3,x),(0,1,x,x**3)],x),
25:(r'y=\sqrt x,\ y=x/3,\ 0\le x\le16',[(0,9,s.sqrt(x),x/3),(9,16,x/3,s.sqrt(x))],x),
26:(r'y=\cos x,\ y=2-\cos x,\ 0\le x\le2\pi',[(0,2*P,2-s.cos(x),s.cos(x))],x),
27:(r'y=\cos x,\ y=\sin2x,\ 0\le x\le\pi/2',[(0,P/6,s.cos(x),s.sin(2*x)),(P/6,P/2,s.sin(2*x),s.cos(x))],x),
28:(r'y=\cos x,\ y=1-\cos x,\ 0\le x\le\pi',[(0,P/3,s.cos(x),1-s.cos(x)),(P/3,P,1-s.cos(x),s.cos(x))],x),
29:(r'y=\sec^2x,\ y=8\cos x,\ -\pi/3\le x\le\pi/3',[(-P/3,P/3,8*s.cos(x),1/s.cos(x)**2)],x),
30:(r'y=x^4-3x^2,\ y=x^2',[(-2,2,x*x,x**4-3*x*x)],x),
31:(r'y=x^4,\ y=2-|x|',[(-1,0,2+x,x**4),(0,1,2-x,x**4)],x),
32:(r'y=1/x^2,\ y=x,\ y=x/8',[(0,1,x,x/8),(1,2,1/x**2,x/8)],x),
33:(r'y=\sin(\pi x/2),\ y=x^3',[(-1,0,x**3,s.sin(P*x/2)),(0,1,s.sin(P*x/2),x**3)],x),
34:(r'y=x^2/4,\ y=2x^2,\ x+y=3,\ x\ge0',[(0,1,2*x*x,x*x/4),(1,2,3-x,x*x/4)],x),
36:(r'y=x/\sqrt{1+x^2},\ y=x/\sqrt{9-x^2},\ x\ge0',[(0,2,x/s.sqrt(1+x*x),x/s.sqrt(9-x*x))],x),
37:(r'y=\cos^2x\sin x,\ y=\sin x,\ 0\le x\le\pi',[(0,P,s.sin(x),s.cos(x)**2*s.sin(x))],x),
38:(r'y=x\sqrt{x^2+1},\ y=x^2\sqrt{x^3+1}',[(0,1,x*s.sqrt(x*x+1),x*x*s.sqrt(x**3+1))],x),
39:(r'A=(0,0),\ B=(3,1),\ C=(1,2)',[(0,1,2*x,x/3),(1,3,(5-x)/2,x/3)],x),
40:(r'A=(2,0),\ B=(0,2),\ C=(-1,1)',[(-1,0,x+2,(2-x)/3),(0,2,2-x,(2-x)/3)],x),
41:(r'\int_0^{\pi/2}|\sin x-\cos2x|\,dx',[(0,P/6,s.cos(2*x),s.sin(x)),(P/6,P/2,s.sin(x),s.cos(2*x))],x),
42:(r'\int_0^4|\sqrt{x+2}-x|\,dx',[(0,2,s.sqrt(x+2),x),(2,4,x,s.sqrt(x+2))],x),
52:(r'x-2y^2\ge0,\ 1-x-|y|\ge0',[(-R(1,2),0,1+y,2*y*y),(0,R(1,2),1-y,2*y*y)],y),
61:(r'y^2=x^2(x+3)',[(-3,0,-x*s.sqrt(x+3),x*s.sqrt(x+3))],x),
62:(r'y=x^2,\ y=0,\ \text{tangent at }(1,1)',[(0,R(1,2),x*x,0),(R(1,2),1,x*x,2*x-1)],x),
68:(r'y=\sin x,\ y=e^x,\ x=0,\pi/2',[(0,P/2,s.exp(x),s.sin(x))],x),
69:(r'y=\tan x,\ y=2\sin x,\ -\pi/3\le x\le\pi/3',[(-P/3,0,s.tan(x),2*s.sin(x)),(0,P/3,2*s.sin(x),s.tan(x))],x),
70:(r'y=x^2,\ y=32/(x^2+4)',[(-2,2,32/(x*x+4),x*x)],x),
71:(r'y=1/x,\ y=x,\ y=x/4,\ x>0',[(0,1,x,x/4),(1,2,1/x,x/4)],x)}
for n,(F,pieces,v)in records.items():
 req=('(a) 넓이 적분을 세우고 (b) 값을 계산하라.','(a) Set up the area integral and (b) evaluate it.')if n<=4 else('넓이를 나타내는 적분을 세우되 계산하지 마라.','Set up, but do not evaluate, an area integral.')if 7<=n<=10 else('영역을 그리고 대표 근사 직사각형의 길이와 두께를 표시한 뒤 넓이를 구하라.','Sketch the region, label a typical strip’s length and thickness, and find its area.')if 11<=n<=18 else('영역을 그리고 넓이를 구하라.','Sketch the region and find its area.')
 if n in[41,42]:req=('적분을 계산하고 곡선 사이 영역의 넓이로 해석하여 그려라.','Evaluate the integral and interpret/sketch it as area between curves.')
 if n==61:req=('곡선의 닫힌 고리를 찾아 그 넓이를 구하라.','Locate the closed loop and find its enclosed area.')
 if n==62:req=('포물선, 지정한 점의 접선, x축이 둘러싼 넓이를 구하라.','Find the area enclosed by the parabola, its tangent at the specified point, and the x-axis.')
 area(b,n,370 if n<=6 else 371 if n<=51 else 372 if n<=65 else 373,(M(F)+req[0],M(F)+req[1]),pieces,v,setup_only=7<=n<=10,parts=['a','b']if n<=4 else[])
 b.save()
print('5.1 exact-area entries',len(b.E))
# Numerical intersections are refined at35 digits; all bounded components are included.
numeric={43:(x*s.sin(x*x),x**4,[0,mp.findroot(lambda q:mp.sin(q*q)-q**3,.9)]),44:(x/(x*x+1)**2,x**5-x,[0,mp.findroot(lambda q:1/(q*q+1)**2-q**4+1,1.05)]),45:(3*x*x-2*x,x**3-3*x+4,[mp.findroot(lambda q:q**3-3*q*q-q+4,a)for a in[-1.1,1.25,2.86]]),46:(x-s.cos(x),2-x*x,[mp.findroot(lambda q:q*q+q-mp.cos(q)-2,a)for a in[-1.9,1.1]]),47:(2/(1+x**4),x*x,[-1,1]),48:(x**6,s.sqrt(2-x**4),[-1,1]),49:(s.tan(x)**2,s.sqrt(x),[0,mp.findroot(lambda q:mp.tan(q)**2-mp.sqrt(q),.75)]),50:(s.cos(x),x+2*s.sin(x)**4,[mp.findroot(lambda q:mp.cos(q)-q-2*mp.sin(q)**4,a)for a in[-1.91,-1.22,.608]])}
for n,(f,g,roots)in numeric.items():
 rs=[s.Float(str(q),33)for q in roots];ps=[]
 for l,h in zip(rs,rs[1:]):
  up,dn=(f,g)if float((f-g).subs(x,(l+h)/2))>0 else(g,f);ps.append((l,h,up,dn))
 F=M('y='+tex(f)+r',\quad y='+tex(g));st=(F+'교점을 수치적으로 찾고 영역을 그린 뒤 넓이를 구하라.','Numerically locate the intersections, plot the region, and find its area. '+F)
 extra=[('교점 방정식을 풀고 부호가 바뀌는 곳에서 적분을 나눈다. 교점 x좌표: '+', '.join(f'{float(q):.10f}'for q in roots),'Solve the intersection equation and split where the boundary order changes. Intersection x-values: '+', '.join(f'{float(q):.10f}'for q in roots))]
 if n==49:
  st=(F+'원점에 인접한 영역(0≤x<π/2)을 그리고 넓이를 소수점 아래5자리까지 구하라.',F+'Plot the region adjacent to the origin (0≤x<π/2) and find its area to five decimal places.')
  extra.append(('tan²x는 주기함수이므로 다른 가지에도 영역이 생긴다. 이 답은 교재 그래프에서 다루는 원점 옆 첫 영역이다.','Because tan²x is periodic, other branches also enclose regions. This answer specifies the first region adjacent to the origin.'))
 val=area(b,n,371,st,ps,x,numeric=True,extra=extra)
 if n>=47:b.E[n]['answer']=pair(M(r'A\approx'+f'{float(val):.5f}'))
 b.save()
f=x**5-6*x**3+4*x;g=x;rr=[-s.sqrt(3+s.sqrt(6)),-s.sqrt(3-s.sqrt(6)),s.Integer(0),s.sqrt(3-s.sqrt(6)),s.sqrt(3+s.sqrt(6))];ps=[]
for lo,hi in zip(rr,rr[1:]):
 up,dn=(f,g)if float((f-g).subs(x,(lo+hi)/2))>0 else(g,f);ps.append((lo,hi,up,dn))
area(b,51,371,(M(r'y=x^5-6x^3+4x,\quad y=x')+'사이 모든 유계영역의 정확한 넓이를 구하라.',M(r'y=x^5-6x^3+4x,\quad y=x')+'Find the exact total area of all bounded components.'),ps,x,extra=fs(r'x^5-6x^3+3x=x(x^4-6x^2+3)=0',r'x=0,\quad x=\pm\sqrt{3-\sqrt6},\ \pm\sqrt{3+\sqrt6}'))
def add(n,st,steps,ans,check,parts=[]):
 b.add(n,371 if n<=51 else 372 if n<=65 else 373,('넓이와 누적 변화','Area and accumulated change'),st,steps,pair(*ans),parts=parts);b.verify(n,*check)
add(35,('0≤x≤5에서 f와 g가 x=2에 교차한다. 왼쪽에서는 g가 위에 있고 넓이12, 오른쪽에서는 f가 위에 있고 넓이27이다. (a)총넓이,(b)∫₀⁵(f-g)dx를 구하라.','On0≤x≤5 the graphs intersect at x=2. Left of2, g is above f with area12; right of2, f is above g with area27. Find(a)total area,(b)∫₀⁵(f-g)dx.'),[('기하학적 넓이는 두 영역을 더하지만 부호 있는 적분은 f<g인 영역을 뺀다.','Geometric area adds both regions, while the signed integral subtracts the region where f<g.')]+fs(r'A=12+27=39,\qquad\int_0^5(f-g)\,dx=-12+27=15'),same('(a)39; (b)15.'),('각 구간에서 f-g의 부호를 원본과 대조했다.','Checked the sign of f-g on each interval against the source.'),['a','b'])
vc=[0,20,32,46,54,62,69,75,81,86,90];vk=[0,22,37,52,61,71,80,86,93,98,102];tab=M(r'\begin{array}{c|rrrrrrrrrrr}t\ (s)&0&1&2&3&4&5&6&7&8&9&10\\v_C&0&20&32&46&54&62&69&75&81&86&90\\v_K&0&22&37&52&61&71&80&86&93&98&102\end{array}')
add(53,('함께 출발한 두 차의 mph 속도표를 이용해 첫10초 동안 Kelly가 Chris보다 더 간 거리를 중점법으로 추정하라.'+tab,'Using the mph velocity table for two cars starting together, estimate Kelly’s extra distance during the first10 seconds with the Midpoint Rule.'+tab),fs(r'\Delta t=2/3600\ \mathrm h,\quad t_i^*=1,3,5,7,9\ \mathrm s',r'\Delta d\approx\frac2{3600}[(22-20)+(52-46)+(71-62)+(86-75)+(98-86)]=\frac1{45}\ \mathrm{mi}'),same(M(r'\Delta d\approx1/45\ \mathrm{mi}\approx117.33\ \mathrm{ft}')),('중점 속도차의 합은40 mph이고 초를 시간으로 바꾸었다.','The midpoint speed differences sum to40 mph; seconds were converted to hours.'))
add(54,('길이16 m인 수영장의 x=2,4,6,8,10,12,14 m에서 폭이 각각6.2,7.2,6.8,5.6,5.0,4.8,4.8 m이다. 중점법으로 넓이를 추정하라.','A16-m-long pool has widths6.2,7.2,6.8,5.6,5.0,4.8,4.8 m at x=2,4,6,8,10,12,14 m. Estimate area by the Midpoint Rule.'),[('간격4 m인 네 구간의 중점2,6,10,14 m를 선택한다.','Use four4-m intervals with midpoints2,6,10,14 m.')]+fs(r'A\approx4(6.2+6.8+5.0+4.8)=91.2\ \mathrm{m^2}'),same(M(r'A\approx91.2\ \mathrm{m^2}')),('16 m 전체를 겹침 없이 네 구간으로 덮고 중점 자료만 사용했다.','The four intervals cover the full16 m without overlap and use only midpoint data.'))
add(55,('날개 단면의 x=0,20,…,200 cm에서 두께가5.8,20.3,26.7,29.0,27.6,27.3,23.8,20.5,15.1,8.7,2.8 cm이다. 중점법으로 단면적을 추정하라.','At x=0,20,…,200 cm, wing thicknesses are5.8,20.3,26.7,29.0,27.6,27.3,23.8,20.5,15.1,8.7,2.8 cm. Estimate cross-sectional area using midpoints.'),fs(r'\Delta x=40\ \mathrm{cm},\quad x_i^*=20,60,100,140,180',r'A\approx40(20.3+29.0+27.3+20.5+8.7)=4232\ \mathrm{cm^2}'),same(M(r'A\approx4232\ \mathrm{cm^2}')),('중점 두께의 합105.8 cm에40 cm를 곱했다.','The midpoint thicknesses sum to105.8 cm, multiplied by40 cm.'))
area(b,56,372,('출생률 b(t)=2200+52.3t+0.74t², 사망률 d(t)=1460+28.8t(명/년)이다. 첫10년의 두 곡선 사이 넓이와 뜻을 구하라.','Birth rate is b(t)=2200+52.3t+0.74t² and death rate d(t)=1460+28.8t (people/year). Find and interpret the area between them during the first10 years.'),[(0,10,2200+R(523,10)*x+R(74,100)*x*x,1460+R(288,10)*x)],x,extra=[('출생률이 더 크므로 차의 적분은 출생·사망에 의한 인구 순증가를 나타낸다.','Birth rate exceeds death rate, so the difference integrates to the population’s net increase from births and deaths.')])
b.save()
g=lambda t:-mp.mpf('.9')*t*(t-21)*(t+1);t1=mp.findroot(lambda t:g(t)-1210,11);t2=mp.findroot(lambda t:g(t)-1210+23*(t-t1),17);inf=mp.quad(lambda t:g(t)-1210+23*(t-t1),[t1,t2])
add(57,('교재 모형 f(t)=-t(t-21)(t+1)에 면역 효과를 적용해 g(t)=0.9f(t)로 둔다. (a)감염 전파가 시작되는 농도1210에 처음 도달하는 날,(b)그 점에서 끝점으로 이은 직선의 기울기가 -23일 때 끝나는 날,(c)그 직선과 g 사이의 넓이를 구하라.','Use the textbook model f(t)=-t(t-21)(t+1) with immunity adjustment g(t)=0.9f(t). Find(a)the first day concentration reaches1210,(b)the ending day when the joining chord has slope-23,(c)the area between g and that chord.'),fs(r'-0.9t_1(t_1-21)(t_1+1)=1210',r'g(t_2)=1210-23(t_2-t_1),\quad t_2>t_1',r'I=\int_{t_1}^{t_2}[g(t)-1210+23(t-t_1)]\,dt')+[(f'시작은 증가하는 가지에서 t1≈{float(t1):.8f}, 끝은 그 뒤 교점 t2≈{float(t2):.8f}을 선택한다.',f'Choose t1≈{float(t1):.8f} on the increasing branch and the subsequent intersection t2≈{float(t2):.8f}.')],same(M(r'(a)\ t_1\approx'+f'{float(t1):.6f}'+r';\quad(b)\ t_2\approx'+f'{float(t2):.6f}'+r';\quad(c)\ I\approx'+f'{float(inf):.6f}')),('두 끝점에서 g와 직선이 같고 그 사이 g가 더 큼을 확인했다. 면적 단위는 (cells/mL)·days.','Verified equality at both endpoints and g above the chord between them. Area units are(cells/mL)·days.'),['a','b','c'])
area_svg(b,57,[(s.Float(str(t1)),s.Float(str(t2)),-R(9,10)*x*(x-21)*(x+1),1210-23*(x-s.Float(str(t1))))],x,'5.1.57  Adjusted pathogenesis model')
area(b,58,372,('강우율 f(t)=0.73t³-2t²+t+0.6, g(t)=0.17t²-0.5t+1.1 (in/h)이 주어진다. 0≤t≤2에서 곡선 사이 넓이를 구하고 해석하라.','Rain rates are f(t)=0.73t³-2t²+t+0.6 and g(t)=0.17t²-0.5t+1.1 (in/h). Find and interpret the area between them on0≤t≤2.'),[(0,2,R(17,100)*x*x-x/2+R(11,10),R(73,100)*x**3-2*x*x+x+R(6,10))],x,extra=[('두 시간 동안 g>f이므로 넓이는 g지역에 더 내린 총 강우량(in)이다.','Since g>f throughout the two hours, the area is the extra total rainfall in inches at location g.')])
add(59,('원본 속도 그래프에서 두 차 A,B는 정지 상태에서 같이 출발한다. A는0<t<1분에 더 빠르고 그 뒤 B가 더 빠르다. (a)1분 후 선두,(b)0–1분 두 곡선 사이 넓이의 뜻,(c)2분 후 선두,(d)다시 나란해지는 시간을 그림으로 추정하라.','In the source velocity graph, cars A and B start together from rest. A is faster for0<t<1 minute, B thereafter. Determine(a)the leader at1 minute,(b)the meaning of the area between curves on0–1,(c)the leader at2 minutes,(d)an estimate of their next side-by-side time.'),[('변위 차는 속도 차의 누적 적분이다. 1분까지 A가 얻은 양의 넓이에서 이후 B가 얻는 넓이를 빼야 한다.','Position difference is the accumulated velocity difference. Subtract B’s later gain from A’s positive area during the first minute.'),('원본 격자를 세면2분에도 처음의 넓이가 조금 남는다. 이후 약0.25분이 더 지나야 두 넓이가 같아진다.','Counting source-grid areas leaves a small positive balance at2 minutes. Roughly another0.25 minute makes the two areas equal.')],('(a)A; (b)1분 후 A가 앞선 거리; (c)A; (d)약2.25분(그림 판독값).','(a)A; (b)A’s distance advantage at1 minute; (c)A; (d)about2.25 minutes, a graphical estimate.'),('원본 곡선의 색상 좌표를 수치 판독하여 누적 면적의 영점이 약2.26분임을 별도로 확인했다.','Independent digitization of the source curves placed the zero of accumulated area at about2.26 minutes.'),list('abcd'))
add(60,('원본 한계수익 R′와 한계비용 C′ 그래프에서 음영은50≤x≤100이다. R,C 단위는 천 달러이다. 음영의 뜻을 설명하고 중점법으로 추정하라. 중점55,65,75,85,95에서 그래프로 읽은 R′-C′는 약1.6,1.4,1.1,0.7,0.3이다.','The source marginal-revenue/cost graph shades50≤x≤100; R,C are in thousands of dollars. Explain and estimate the area with the Midpoint Rule. Approximate graph readings of R′-C′ at55,65,75,85,95 are1.6,1.4,1.1,0.7,0.3.'),fs(r'\int_{50}^{100}(R\prime-C\prime)\,dx=[R(100)-C(100)]-[R(50)-C(50)]',r'\Delta\mathrm{Profit}\approx10(1.6+1.4+1.1+.7+.3)=51'),('생산량을50개에서100개로 늘릴 때 이익 증가량, 약51,000달러. 판독·분할 방식에 따라 가까운 추정값이 가능하다.','The increase in profit when output rises from50 to100 units, about$51,000; nearby estimates depend on graphical readings and partition choice.'),('원본을 별도로 수치 판독한 중점 차이의 합은 약51.1천 달러이다.','Independent midpoint digitization gives about51.1 thousand dollars.'))
add(63,(M(r'y=x^2,\quad y=4')+'사이 넓이를 y=b가 반으로 나누게 하는 b를 구하라.',M(r'y=x^2,\quad y=4')+'Find b so that y=b bisects the enclosed area.'),fs(r'A=\int_0^4 2\sqrt y\,dy=32/3',r'\int_0^b2\sqrt y\,dy=\frac43b^{3/2}=16/3'),same(M(r'b=4^{2/3}=2^{4/3}')),('0<b<4이고 아래쪽 넓이가 정확히16/3이다.','Checked0<b<4 and lower area exactly16/3.'))
add(64,('곡선 y=1/x² 아래,1≤x≤4인 넓이를 (a)x=a,(b)y=b가 각각 이등분하게 하는 a,b를 구하라.','Bisect the area under y=1/x² on1≤x≤4 by(a)x=a and(b)y=b.'),fs(r'A=\int_1^4x^{-2}\,dx=3/4',r'(a)\ \int_1^a x^{-2}\,dx=1-1/a=3/8\Rightarrow a=8/5',r'(b)\ \int_b^1(y^{-1/2}-1)\,dy=(1-\sqrt b)^2=3/8'),same(M(r'a=8/5,\qquad b=(1-\sqrt{3/8})^2')),('b≈0.150255는1/16과1 사이이므로 수평 띠 폭 y^(-1/2)-1 공식이 해당 구간에서 유효하다.','b≈0.150255 lies between1/16 and1, validating the horizontal-strip formula on that interval.'),['a','b'])
add(65,('포물선 y=x²-c²와 y=c²-x² 사이 넓이가576이 되게 하는 c를 구하라.','Find c for which the area between y=x²-c² and y=c²-x² is576.'),fs(r'x=\pm|c|,\quad A=\int_{-|c|}^{|c|}2(c^2-x^2)\,dx=\frac83|c|^3=576'),same(M(r'c=\pm6')),('c²만 나타나므로 양수·음수 해를 모두 보존했다.','Both signs are retained because only c² occurs.'))
add(66,('0<c<π/2이다. cos x와 cos(x-c),x=0 사이 넓이가 cos(x-c),x=π,y=0 사이 넓이와 같게 하는 c를 구하라.','For0<c<π/2, equate the area bounded by cos x,cos(x-c),x=0 to that bounded by cos(x-c),x=π,y=0; find c.'),fs(r'A_1=\int_0^{c/2}[\cos x-\cos(x-c)]dx=2\sin(c/2)-\sin c',r'A_2=-\int_{c+\pi/2}^\pi\cos(x-c)\,dx=1-\sin c',r'A_1=A_2\Rightarrow\sin(c/2)=1/2'),same(M(r'c=\pi/3')),('c/2∈(0,π/4)이므로 조건에 맞는 해는 유일하며 두 넓이는1-√3/2이다.','Since c/2∈(0,π/4), the admissible root is unique; both areas equal1-√3/2.'))
add(67,('y=8x-27x³의 양의 봉우리를 수평선 y=c가 두 번 가로지른다. y축부터 두 번째 교점까지, 곡선 아래·직선 위 넓이와 직선 아래·곡선 위 넓이가 같게 하는 c를 구하라.','A horizontal line y=c crosses the positive hump of y=8x-27x³ twice. Between the y-axis and the second intersection, make the areas above and below the horizontal line equal; find c.'),fs(r'c=8b-27b^3,\quad\int_0^b(8x-27x^3-c)\,dx=0',r'4b^2-\frac{27}4b^4-b(8b-27b^3)=0',r'b>0\Rightarrow b=4/9,\quad c=8(4/9)-27(4/9)^3=32/27'),same(M(r'c=32/27')),('b=4/9를 두 조건에 대입하면 곡선 교점 조건과 부호 있는 넓이0을 모두 만족한다.','Substituting b=4/9 satisfies both the intersection condition and zero signed area.'))
add(72,(M(r'y=mx,\quad y=\frac{x}{1+x^2}')+'가 유계영역을 둘러싸는 m의 범위와 넓이를 구하라.',M(r'y=mx,\quad y=\frac{x}{1+x^2}')+'Find the values of m enclosing bounded regions and compute their area.'),fs(r'x\left(\frac1{1+x^2}-m\right)=0\Rightarrow x=0,\quad x=\pm\sqrt{1/m-1}',r'0<m<1\Rightarrow a=\sqrt{1/m-1}>0',r'A_{right}=\int_0^a\left(\frac{x}{1+x^2}-mx\right)dx=\frac12(m-1-\ln m)')+[('두 함수는 홀함수라 좌우 영역의 넓이가 같다. m≤0 또는 m≥1이면 서로 다른 유한 교점 세 개가 없어 양의 유계넓이를 만들지 않는다.','Both functions are odd, so the left/right areas are equal. For m≤0 or m≥1 there are no three distinct finite intersections enclosing positive area.')],(M(r'0<m<1,\quad A_{each}=\tfrac12(m-1-\ln m),\quad A_{total}=m-1-\ln m'),M(r'0<m<1,\quad A_{each}=\tfrac12(m-1-\ln m),\quad A_{total}=m-1-\ln m')),('ln m≤m-1로 넓이가 음이 아님을 확인하고 m→1에서는0으로 간다.','The inequality ln m≤m-1 checks nonnegativity, and the area tends to0 as m→1.'))
b.E[65]['steps']['ko'].append('따라서 |c|의 세제곱은216, |c|=6이며 c=±6이다.')
b.E[65]['steps']['en'].append('Thus |c| cubed equals216, so |c|=6 and c=±6.')
b.save();print('5.1 COMPLETE',len(b.E))
