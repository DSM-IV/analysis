"""Original curve, curvature and osculating-circle illustrations."""
from curve_figures import draw_curves
from pathlib import Path
import math as m,json,sympy as s
R=Path(__file__).resolve().parents[1]/'exercise-content';p=R/'s13-3.json';d=json.loads(p.read_text());E={e['number']:e for e in d['exercises']};pi=m.pi
C=lambda u:m.cos(u);S=lambda u:m.sin(u)
def panel(title,fn,rg,labels='xyz'):return(title,fn,rg,labels)
def fig(n,panels,k='자체 제작 그래프. 파랑은 곡선이고, 같은 패널의 보라는 곡률 또는 첫 접촉원, 주황은 둘째 접촉원이다. 화살표는 각 매개변수의 증가 방향이다.',e='Original plots. Blue is the curve; purple on the same panel is curvature or the first osculating circle, and orange is the second circle. Arrows follow each plotted parameter.'):
 name=f's13-3-{n}.svg';draw_curves(R/'assets'/name,panels);E[n]['figure']={'src':'../exercise-content/assets/'+name,'alt':{'ko':f'13.3 {n}번의 자체 제작 그래프','en':f'Original graphs for Exercise13.3.{n}'},'caption':{'ko':k,'en':e}}
fig(12,[panel('Curve: one full period',lambda t:(S(t),S(2*t),S(3*t)),[(0,2*pi)])])
fig(30,[panel('Unit cylinder; z = sin(5t)',lambda t:(C(t),S(t),S(5*t)),[(0,2*pi)])])
# Schematic matching the estimated endpoint curvatures, not a digitization.
a=1.3/3;b=m.log(1.3/.7)/3
# Antiderivative of -a*x*(3-x)*exp(-b*x), normalized to f(0)=2.
def anti(x):return-a*m.exp(-b*x)*(x*x/b+(2/b**2-3/b)*x+2/b**3-3/b**2)
def f37(x):return 2+anti(x)-anti(0)
yq=f37(3)
fig(37,[panel('Schematic: P circle purple, Q orange',[lambda x:(x,f37(x)),lambda u:(S(u)/1.3,2-1/1.3+C(u)/1.3),lambda u:(3+S(u)/.7,yq+1/.7+C(u)/.7)],[(-.6,3.6),(0,2*pi),(0,2*pi)],'xy')], '원본을 그대로 복제한 그래프가 아닌 추정 반지름을 설명하는 개형이다. 파랑의 봉우리 P에서 보라 원의 반지름은 약0.77, 골짜기 Q에서 주황 원의 반지름은 약1.43이다.', 'This schematic illustrates the estimated radii; it is not a reproduction of the source graph. The purple circle at peak P has radius about0.77 and the orange circle at trough Q about1.43.')
fig(38,[panel('Blue: x^4 - 2x^2; purple: curvature',[lambda x:(x,x**4-2*x*x),lambda x:(x,abs(12*x*x-4)/(1+(4*x**3-4*x)**2)**1.5)],[(-1.8,1.8),(-1.8,1.8)],'xy')])
fig(39,[panel('Blue: x^-2; purple: curvature',[lambda x:(x,x**-2),lambda x:(x,x**-2),lambda x:(x,6*x**-4/(1+4*x**-6)**1.5),lambda x:(x,6*x**-4/(1+4*x**-6)**1.5)],[(-3,-.45),(.45,3),(-3,-.15),(.15,3)],'xy')], '자체 그래프. 파랑·보라는 y=x⁻²의 두 가지, 주황·초록은 곡률의 두 가지이다. x=0은 정의되지 않아 선을 연결하지 않았다.', 'Original plot. Blue/purple are the two branches of y=x⁻²; orange/green are the curvature branches. No line crosses the excluded point x=0.')
fig(40,[panel('Curve with stationary cusps',lambda t:(t-S(t),1-C(t),4*C(t/2)),[(0,8*pi)]),panel('Curvature; cusps excluded',lambda t:(t,1/(8*abs(S(t/2)))),[(2*pi*k+.12,2*pi*(k+1)-.12)for k in range(4)],'tk')], '정칙구간의 자체 그래프. t=2πk에서 곡률이 정의되지 않고 무한히 커지므로 곡률 그래프는 각 특이점으로부터0.12만큼 잘라 표시했다.', 'Original plots on regular intervals. Curvature is undefined and diverges at t=2πk, so the curvature display is clipped0.12 away from each singularity.')
f41=lambda t:(t*m.exp(t),m.exp(-t),m.sqrt(2)*t)
k41=lambda t:m.sqrt(2*(t+2)**2*m.exp(2*t)+(2*t+3)**2+2*m.exp(-2*t))/((t+1)**2*m.exp(2*t)+2+m.exp(-2*t))**1.5
fig(41,[panel('Curve, -5 <= t <= 5',f41,[(-5,5)]),panel('Curvature',lambda t:(t,k41(t)),[(-5,5)],'tk'),panel('Central bend, enlarged',f41,[(-2,1)])])
for n,scale,spread in [(42,1,1),(43,3,8)]:
 f=lambda x,A=scale,B=spread:A*m.exp(-x*x/B)
 k=lambda x,A=scale,B=spread:abs(A*m.exp(-x*x/B)*(4*x*x/B**2-2/B))/(1+(-2*x*A*m.exp(-x*x/B)/B)**2)**1.5
 fig(n,[panel('Schematic: blue f, purple curvature',[lambda x,f=f:(x,f(x)),lambda x,k=k:(x,k(x))],[(-3,3),(-3,3)]if n==42 else[(-7,7),(-7,7)],'xy')], '판별 이유를 보여 주는 자체 개형이다. 원본 a,b의 좌표를 복제하지 않았다. 이 그림의 파랑은 f, 보라는 κ이다. 원본의 기호 대응은 해설에 적었다.', 'Original schematic illustrating the identification logic, not a coordinate copy of source curves a,b. Here blue is f and purple is κ; the source-letter correspondence is given in the solution.')
k44=lambda t:m.sqrt(72*S(t)**2*(8*S(t)**4-10*S(t)**2+5)**2)/(18*C(3*t)**2+4*C(2*t)**2)**1.5
fig(44,[panel('Planar curve in z = x',lambda t:(S(3*t),S(2*t),S(3*t)),[(0,2*pi)]),panel('Six curvature maxima per period',lambda t:(t,k44(t)),[(0,2*pi)],'tk'),panel('View in its plane (equal units)',lambda t:(m.sqrt(2)*S(3*t),S(2*t)),[(0,2*pi)],['sqrt(2)x','y'])])
k45=lambda t:m.sqrt((36*C(t)**2-108*C(t)+117)/16)/(17/4-3*C(t))**1.5
fig(45,[panel('Rising trochoid',lambda t:(t-1.5*S(t),1-1.5*C(t),t),[(-2*pi,2*pi)]),panel('Maxima at t = 2 pi k',lambda t:(t,k45(t)),[(-2*pi,2*pi)],'tk')])
fig(55,[panel('Ellipse and both osculating circles',[lambda t:(2*C(t),3*S(t)),lambda t:(-2.5+4.5*C(t),4.5*S(t)),lambda t:((4/3)*C(t),5/3+(4/3)*S(t))],[(0,2*pi)]*3,'xy')])
fig(56,[panel('Parabola and osculating circles',[lambda x:(x,x*x/2),lambda t:(C(t),1+S(t)),lambda t:(-1+2*m.sqrt(2)*C(t),2.5+2*m.sqrt(2)*S(t))],[(-2.8,2.8),(0,2*pi),(0,2*pi)],'xy')])
fig(78,[panel('Smooth railway transition',lambda x:(x,0 if x<=0 else 1 if x>=1 else 6*x**5-15*x**4+10*x**3),[(-.5,1.5)],'xy')])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print('13.3:',sum('figure'in e for e in E.values()),'original SVGs')
