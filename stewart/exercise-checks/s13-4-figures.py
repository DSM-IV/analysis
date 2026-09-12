from curve_figures import draw_curves
from pathlib import Path
import math as m,json,sympy as s
R=Path(__file__).resolve().parents[1]/'exercise-content';p=R/'s13-4.json';d=json.loads(p.read_text());E={e['number']:e for e in d['exercises']};pi=m.pi
C=m.cos;S=m.sin
panel=lambda title,fn,ranges,labels='xyz':(title,fn,ranges,labels)
def fig(n,panels,ko='자체 제작 그래프. 같은 패널에서 파랑은 경로, 보라는 속도, 주황은 가속도 벡터이다. 두 벡터의 시작점은 입자의 위치이다.',en='Original plots. Within each panel blue is the path, purple velocity and orange acceleration. Both vectors start at the particle position.'):
 fn=f's13-4-{n}.svg';draw_curves(R/'assets'/fn,panels);E[n]['figure']={'src':'../exercise-content/assets/'+fn,'alt':{'ko':f'13.4 {n}번 자체 도해','en':f'Original illustration for Exercise13.4.{n}'},'caption':{'ko':ko,'en':en}}
def line(P,D):return lambda u:tuple(a+u*b for a,b in zip(P,D))
t=s.symbols('t');co=s.symbols('a:4');pol=sum(co[i]*t**i for i in range(4));ff=[]
for values,der in [([4,3.4,2.4],-2),([2,3.2,3.5],1.6)]:
 sol=s.solve([pol.subs(t,1.5)-values[0],pol.subs(t,2)-values[1],pol.subs(t,2.4)-values[2],s.diff(pol,t).subs(t,2)-der],co);ff.append(s.lambdify(t,pol.subs(sol),'math'))
r=lambda u:(ff[0](u),ff[1](u));P=r(2);L=r(1.5);Q=r(2.4);D1=tuple((Q[i]-P[i])/.4 for i in range(2));D2=tuple((P[i]-L[i])/.5 for i in range(2))
fig(2,[panel('Schematic secant velocities',[r,line(P,D1),line(L,D2)],[(1.3,2.7),(0,1),(0,1)],'xy'),panel('Estimated instantaneous velocity',[r,line(P,(-2,1.6))],[(1.3,2.7),(0,1)],'xy')], '원본을 근사해 벡터 구성을 설명한 개형이다. 왼쪽의 보라는 [2,2.4], 주황은 [1.5,2]의 평균속도이고, 오른쪽 보라는 순간속도 추정이다. 이 그림에 사용한 보간식은 주어진 물리 법칙이 아니다.', 'Schematic explaining the vector construction from approximate source readings. Left: purple is the[2,2.4]average velocity and orange the[1.5,2]average. Right: purple is the estimated instantaneous velocity. The interpolating curve is illustrative, not a supplied motion law.')
rows=[(3,[-t*t/2,t],2,(-1,3)),(4,[t*t,t**-2],1,(.55,2)),(5,[3*s.cos(t),2*s.sin(t)],s.pi/3,(0,2*pi)),(6,[s.exp(t),s.exp(2*t)],0,(-1.5,.8)),(7,[t,t*t,2],1,(-1.5,2)),(8,[t,2*s.cos(t),s.sin(t)],0,(-pi,pi))]
for n,ff,at,rg in rows:
 rr=s.Matrix(ff);dd=rr.diff(t);aa=dd.diff(t);P=tuple(float(z.subs(t,at))for z in rr);D=tuple(float(z.subs(t,at))for z in dd);A=tuple(float(z.subs(t,at))for z in aa);fun=s.lambdify(t,ff,'math')
 fig(n,[panel('Path, velocity and acceleration',[fun,line(P,D),line(P,A)],[rg,(0,1),(0,1)],'xy'if len(ff)==2 else'xyz')])
fig(17,[panel('Integrated trajectory',lambda t:(t**3/3+t,t-S(t)+1,(1-C(2*t))/4),[(-3,3)])], '초기조건을 만족하는 자체 경로그래프. 무한 경로 중 −3≤t≤3을 표시했다.', 'Original trajectory satisfying the initial conditions, displayed for−3≤t≤3.')
fig(18,[panel('Integrated trajectory',lambda t:(t**3/6,m.exp(t)-t,m.exp(-t)+2*t),[(-2,2)])], '초기조건을 만족하는 자체 경로그래프. 무한 경로 중 −2≤t≤2을 표시했다.', 'Original trajectory satisfying the initial conditions, displayed for−2≤t≤2.')
fig(33,[panel('(a) Perpendicular heading: drift 16 m',lambda x:(x,(60*x*x-x**3)/2000),[(0,40)],'xy'),panel('(b) Heading 23.58 deg upstream',lambda x:(x,(.15*x*x-x**3/400-2*x)/m.sqrt(21)),[(0,40)],'xy')], 'x는 서쪽 둑에서 동쪽으로의 거리(m), y는 하류(북쪽) 변위(m)이다. (b)의 선수각은 일정하지만 실제 경로의 방향은 유속에 따라 변한다.', 'x is eastward distance from the west bank(m); y is downstream displacement north(m). In(b)the heading is constant while the actual path direction changes with current speed.')
P=(4,2);T=(1/m.sqrt(2),1/m.sqrt(2));N=(-1/m.sqrt(2),1/m.sqrt(2));at=10/m.sqrt(5);an=20/m.sqrt(5);av=tuple(at*T[i]+an*N[i]for i in range(2));ta=tuple(at*T[i]for i in range(2));na=tuple(an*N[i]for i in range(2));tip=tuple(P[i]+ta[i]for i in range(2))
fig(43,[panel('Schematic acceleration decomposition',[lambda x:(x,x*x/8),line(P,av),line(P,ta),line(tip,na)],[(0,7),(0,1),(0,1),(0,1)],'xy')], '자체 개형: 파랑 경로, 보라 가속도 a, 주황 접선성분 a_TT, 초록 법선성분 a_NN이다. 성분합을 보여 주기 위해 초록 벡터의 시작점만 주황 끝점으로 옮겼다. 원본의 각도는 근사적으로 읽었다.', 'Original schematic: blue path, purple acceleration a, orange tangential component a_TT and green normal component a_NN. The green vector is translated to the orange tip to show vector addition. The source angle is only estimated.')
asset=R/'assets/s13-4-33.svg';asset.write_text(asset.read_text().replace('t in [','x in [').replace('increasing t','increasing x'))
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print('13.4:',sum('figure'in e for e in E.values()),'original SVGs')
