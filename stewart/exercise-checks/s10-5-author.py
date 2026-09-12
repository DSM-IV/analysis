import json,math,html,sys,ast,re
from pathlib import Path
import sympy as S
BASE=Path(__file__).resolve().parents[1];items=[];t=S.symbols('t',real=True)
def M(s):return r'\('+s+r'\)'
def bi(k,e=None):return {'ko':k,'en':k if e is None else e}
def add(n,sk,se,steps,ak,ae,ck,ce,sub=''):
 p=746 if n<=22 else 747 if n<=53 else 748 if n<=68 else 749
 items.append(dict(id=f'stewart9-exercise-10.5-{n}',number=n,subparts=list(sub),source=dict(printedPage=p,pdfPage=p+37),topic=bi('이차곡선','Conic sections'),statement=bi(sk,se),hint=bi('완전제곱으로 중심·축·반축 길이를 정하고 초점 거리 관계를 적용한다.','Complete squares to determine center, axes, and semiaxes, then use the focal-distance relation.'),steps={'ko':[a for a,b in steps],'en':[b for a,b in steps]},answer=bi(ak,ae),check=bi(ck,ce),conceptHref='../../calc1/index.html',status='math-verified'))
source=(BASE/'exercise-checks/s10-1-author.py').read_text()
for node in ast.parse(source).body:
 if isinstance(node,ast.FunctionDef) and node.name in ['sample','svg','multi']:exec(ast.get_source_segment(source,node).replace('s10-1-','s10-5-'))
def calc(n,eq,tk,te,lines,ans,k='',e='',sub=''):
 steps=[(M(x),M(x)) for x in lines]
 if k:steps.append((k,e))
 add(n,M(eq)+' '+tk,M(eq)+' '+te,steps,M(ans),M(ans),'표준형을 전개해 원래 식과 대조하고 초점·꼭짓점 관계를 검산했다.','The standard form was expanded against the original equation, and focus/vertex relations verified.',sub)
def L(x):return S.latex(S.sympify(x))
def pair(x,y):return rf'({L(x)},{L(y)})'
# p is signed; orientation is the opening axis.
def parab(n,eq,h,k,p,axis,taskk='꼭짓점·초점·준선을 구하고 그래프를 그려라.',taske='Find the vertex, focus, and directrix, and graph the parabola.'):
 h,k,p=map(S.sympify,(h,k,p));x,y=S.symbols('x y');std=rf'{L((y-k)**2)}={L(4*p*(x-h))}' if axis=='x' else rf'{L((x-h)**2)}={L(4*p*(y-k))}'
 F=(h+p,k) if axis=='x' else(h,k+p);direct=rf'x={L(h-p)}' if axis=='x' else rf'y={L(k-p)}'
 calc(n,eq,taskk,taske,[std,rf'p={L(p)}'],rf'{std};\quad V={pair(h,k)},\quad F={pair(*F)},\quad\text{{directrix }}{direct}')
 a=float(h);b=float(k);pp=float(p);span=max(2,abs(pp)*3)
 if axis=='x':curves=[('parabola',sample(lambda t:a+t*t/(4*pp),lambda t:b+t,-span*1.7,span*1.7)),('directrix',[(a-pp,b-2*span),(a-pp,b+2*span)])]
 else:curves=[('parabola',sample(lambda t:a+t,lambda t:b+t*t/(4*pp),-span*1.7,span*1.7)),('directrix',[(a-2*span,b-pp),(a+2*span,b-pp)])]
 svg(n,'Parabola and directrix',curves,arrows=False)
for row in [(1,r'x^2=8y',0,0,2,'y'),(2,r'9x=y^2',0,0,S.Rational(9,4),'x'),(3,r'5x+3y^2=0',0,0,-S.Rational(5,12),'x'),(4,r'x^2+12y=0',0,0,-3,'y'),(5,r'(y+1)^2=16(x-3)',3,-1,4,'x'),(6,r'(x-3)^2=8(y+1)',3,-1,2,'y'),(7,r'y^2+6y+2x+1=0',4,-3,-S.Rational(1,2),'x'),(8,r'2x^2-16x-3y+38=0',4,2,S.Rational(3,8),'y')]:parab(*row)
parab(9,r'V=(0,0),\quad P=(-1,1),\quad\text{axis horizontal}',0,0,-S.Rational(1,4),'x','원문은 왼쪽으로 열린 그래프이다. 방정식·초점·준선을 구하라.','The source graph opens left. Find its equation, focus, and directrix.')
parab(10,r'V=(2,-2),\quad P=(0,0),\quad\text{axis vertical}',2,-2,S.Rational(1,2),'y','원문은 위로 열린 그래프이다. 방정식·초점·준선을 구하라.','The source graph opens upward. Find its equation, focus, and directrix.')
def ellipse(n,eq,h,k,A,B,tk='꼭짓점과 초점을 구하고 타원을 그려라.',te='Find vertices and foci and graph the ellipse.'):
 h,k,A,B=map(S.sympify,(h,k,A,B));x,y=S.symbols('x y');a=S.sqrt(max(A,B));c=S.sqrt(abs(A-B));axis='x' if A>=B else'y';vs=[(h-a,k),(h+a,k)] if axis=='x' else[(h,k-a),(h,k+a)];fs=[(h-c,k),(h+c,k)] if axis=='x' else[(h,k-c),(h,k+c)]
 std=rf'\frac{{{L((x-h)**2)}}}{{{L(A)}}}+\frac{{{L((y-k)**2)}}}{{{L(B)}}}=1';ans=std+r';\quad V='+','.join(pair(*p) for p in vs)+r';\quad F='+','.join(pair(*p) for p in fs)
 calc(n,eq,tk,te,[std,rf'a^2={L(max(A,B))},\quad b^2={L(min(A,B))},\quad c^2=a^2-b^2={L(abs(A-B))}'],ans)
 svg(n,'Ellipse with equal axis scale',[('ellipse',sample(lambda t:float(h)+math.sqrt(float(A))*math.cos(t),lambda t:float(k)+math.sqrt(float(B))*math.sin(t),0,2*math.pi))],arrows=False)
for row in [(11,r'x^2/16+y^2/25=1',0,0,16,25),(12,r'x^2/4+y^2/3=1',0,0,4,3),(13,r'x^2+3y^2=9',0,0,9,3),(14,r'x^2=4-2y^2',0,0,4,2),(15,r'4x^2+25y^2-50y=75',0,1,25,4),(16,r'9x^2-54x+y^2+2y+46=0',3,-1,4,36)]:ellipse(*row)
ellipse(17,r'C=(0,0),\quad x_{\rm ends}=\pm2,\quad y_{\rm ends}=\pm3',0,0,4,9,'원문 그래프의 축 끝값을 이용해 타원의 방정식과 초점을 구하라.','Use the source graph’s axis endpoints to find the ellipse equation and foci.')
ellipse(18,r'C=(2,1),\quad x_{\rm ends}=-1,5,\quad y_{\rm ends}=-1,3',2,1,9,4,'원문 그래프의 축 끝값을 이용해 타원의 방정식과 초점을 구하라.','Use the source graph’s axis endpoints to find the ellipse equation and foci.')
def hyper(n,eq,h,k,A,B,axis,tk='꼭짓점·초점·점근선을 구하고 쌍곡선을 그려라.',te='Find vertices, foci, and asymptotes and graph the hyperbola.'):
 h,k,A,B=map(S.sympify,(h,k,A,B));a=S.sqrt(A);b=S.sqrt(B);c=S.sqrt(A+B);x,y=S.symbols('x y')
 std=rf'\frac{{{L((x-h)**2)}}}{{{L(A)}}}-\frac{{{L((y-k)**2)}}}{{{L(B)}}}=1' if axis=='x' else rf'\frac{{{L((y-k)**2)}}}{{{L(A)}}}-\frac{{{L((x-h)**2)}}}{{{L(B)}}}=1'
 vs=[(h-a,k),(h+a,k)] if axis=='x' else[(h,k-a),(h,k+a)];fs=[(h-c,k),(h+c,k)] if axis=='x' else[(h,k-c),(h,k+c)];slope=b/a if axis=='x' else a/b
 calc(n,eq,tk,te,[std,rf'c^2=a^2+b^2={L(A+B)}'],std+r';\quad V='+','.join(pair(*p) for p in vs)+r';\quad F='+','.join(pair(*p) for p in fs)+rf';\quad y-({L(k)})=\pm{L(slope)}[x-({L(h)})]')
 curves=[]
 for sign in [-1,1]:
  if axis=='x':curves.append(('branch',sample(lambda t:float(h)+sign*float(a)*math.cosh(t),lambda t:float(k)+float(b)*math.sinh(t),-1.7,1.7)))
  else:curves.append(('branch',sample(lambda t:float(h)+float(b)*math.sinh(t),lambda t:float(k)+sign*float(a)*math.cosh(t),-1.7,1.7)))
 span=3*float(a+b)
 for sign in [-1,1]:curves.append(('asymptote',[(float(h)-span,float(k)-sign*float(slope)*span),(float(h)+span,float(k)+sign*float(slope)*span)]))
 svg(n,'Hyperbola and asymptotes',curves,arrows=False)
for row in [(19,r'y^2/25-x^2/9=1',0,0,25,9,'y'),(20,r'x^2/36-y^2/64=1',0,0,36,64,'x'),(21,r'x^2-y^2=100',0,0,100,100,'x'),(22,r'y^2-16x^2=16',0,0,16,1,'y'),(23,r'x^2-y^2+2y=2',0,1,1,1,'x'),(24,r'9y^2-4x^2-36y-8x=4',-1,2,4,9,'y')]:hyper(*row)
hyper(25,r'V=(\pm3,0),\quad P=(5,4)',0,0,9,9,'x','원문 그래프의 꼭짓점과 표시점을 이용해 방정식·초점·점근선을 구하라.','Use the source graph’s vertices and marked point to find the equation, foci, and asymptotes.')
hyper(26,r'V=(0,\pm2),\quad P=(8,6)',0,0,4,8,'y','원문 격자 한 칸은 이 단위이다. 표시된 꼭짓점과 점으로 방정식·초점·점근선을 구하라.','One source grid square is two units; use the marked vertices and point to find the equation, foci, and asymptotes.')
hyper(27,r'4x^2=y^2+4',0,0,1,4,'x','곡선의 종류와 꼭짓점·초점을 구하라.','Identify the conic and find vertices and foci.')
parab(28,r'4x^2=y+4',0,-4,S.Rational(1,16),'y','곡선의 종류와 꼭짓점·초점을 구하라.','Identify the conic and find vertices and foci.')
ellipse(29,r'x^2=4y-2y^2',0,1,2,1,'곡선의 종류와 꼭짓점·초점을 구하라.','Identify the conic and find vertices and foci.')
hyper(30,r'y^2-2=x^2-2x',1,0,1,1,'y','곡선의 종류와 꼭짓점·초점을 구하라.','Identify the conic and find vertices and foci.')
parab(31,r'3x^2-6x-2y=1',1,-2,S.Rational(1,6),'y','곡선의 종류와 꼭짓점·초점을 구하라.','Identify the conic and find vertices and foci.')
ellipse(32,r'x^2-2x+2y^2-8y+7=0',1,2,2,1,'곡선의 종류와 꼭짓점·초점을 구하라.','Identify the conic and find vertices and foci.')
for n,eq,lines,ans in [(33,r'V=(0,0),\quad F=(1,0)',[r'p=1'],r'y^2=4x'),(34,r'F=(0,0),\quad\text{directrix }y=6',[r'V=(0,3),\quad p=-3'],r'x^2=-12(y-3)'),(35,r'F=(-4,0),\quad\text{directrix }x=2',[r'V=(-1,0),\quad p=-3'],r'y^2=-12(x+1)'),(36,r'F=(2,-1),\quad V=(2,3)',[r'p=-4,\quad\text{axis vertical}'],r'(x-2)^2=-16(y-3)'),(37,r'V=(3,-1),\quad\text{axis horizontal},\quad P=(-15,2)',[r'(y+1)^2=4p(x-3),\quad9=-72p\Rightarrow p=-1/8'],r'(y+1)^2=-(x-3)/2'),(38,r'\text{axis vertical},\quad P=(0,4),(1,3),(-2,-6)',[r'y=Ax^2+Bx+C,\quad C=4,\quad A+B=-1,\quad4A-2B=-10',r'A=-2,\quad B=1'],r'y=-2x^2+x+4')]:
 calc(n,eq,'조건을 만족하는 포물선 방정식을 구하라.','Find the parabola satisfying the conditions.',lines,ans)
for n,eq,lines,ans in [(39,r'F=(\pm2,0),\quad V=(\pm5,0)',[r'a=5,\ c=2,\ b^2=25-4=21'],r'x^2/25+y^2/21=1'),(40,r'F=(0,\pm\sqrt2),\quad V=(0,\pm2)',[r'a=2,\ c=\sqrt2,\ b^2=4-2=2'],r'x^2/2+y^2/4=1'),(41,r'F=(0,2),(0,6),\quad V=(0,0),(0,8)',[r'C=(0,4),\quad a=4,\ c=2,\ b^2=12'],r'x^2/12+(y-4)^2/16=1'),(42,r'F=(0,-1),(8,-1),\quad V=(9,-1)',[r'C=(4,-1),\quad a=5,\ c=4,\ b^2=9'],r'(x-4)^2/25+(y+1)^2/9=1'),(43,r'C=(-1,4),\quad V=(-1,0),\quad F=(-1,6)',[r'a=4,\ c=2,\ b^2=12'],r'(x+1)^2/12+(y-4)^2/16=1'),(44,r'F=(\pm4,0),\quad P=(-4,1.8)',[r'2a=9/5+\sqrt{8^2+(9/5)^2}=9/5+41/5=10',r'a=5,\quad b^2=25-16=9'],r'x^2/25+y^2/9=1')]:
 calc(n,eq,'조건을 만족하는 타원 방정식을 구하라.','Find the ellipse satisfying the conditions.',lines,ans)
for n,eq,lines,ans in [(45,r'V=(\pm3,0),\quad F=(\pm5,0)',[r'a=3,\ c=5,\ b^2=25-9=16'],r'x^2/9-y^2/16=1'),(46,r'V=(0,\pm2),\quad F=(0,\pm5)',[r'a=2,\ c=5,\ b^2=25-4=21'],r'y^2/4-x^2/21=1'),(47,r'V=(-3,-4),(-3,6),\quad F=(-3,-7),(-3,9)',[r'C=(-3,1),\quad a=5,\ c=8,\ b^2=39'],r'(y-1)^2/25-(x+3)^2/39=1'),(48,r'V=(-1,2),(7,2),\quad F=(-2,2),(8,2)',[r'C=(3,2),\quad a=4,\ c=5,\ b^2=9'],r'(x-3)^2/16-(y-2)^2/9=1'),(49,r'V=(\pm3,0),\quad\text{asymptotes }y=\pm2x',[r'a=3,\quad b/a=2\Rightarrow b=6'],r'x^2/9-y^2/36=1'),(50,r'F=(2,0),(2,8),\quad\text{asymptotes }y=3+x/2,\ y=5-x/2',[r'C=(2,4),\quad c=4,\quad a/b=1/2',r'a^2+b^2=16\Rightarrow a^2=16/5,\ b^2=64/5'],r'\frac{(y-4)^2}{16/5}-\frac{(x-2)^2}{64/5}=1')]:
 calc(n,eq,'조건을 만족하는 쌍곡선 방정식을 구하라.','Find the hyperbola satisfying the conditions.',lines,ans)
calc(51,r'R_{\rm Moon}=1728\ \mathrm{km},\quad h_{\min}=110\ \mathrm{km},\quad h_{\max}=314\ \mathrm{km}','달 중심을 한 초점으로 하는 주어진 타원 궤도의 방정식을 구하라.','Find an equation for the specified elliptical orbit with the Moon’s center at one focus.',[r'a-c=1728+110=1838,\quad a+c=1728+314=2042',r'a=1940,\quad c=102,\quad b^2=a^2-c^2=3753196'],r'\frac{x^2}{3763600}+\frac{y^2}{3753196}=1,\quad F_{\rm Moon}=(102,0)','좌표 단위는 킬로미터이며 타원 중심을 원점, 장축을 가로축으로 선택했다. 제시된 고도는 달 표면 위 거리이므로 달 반지름을 더한다.','Coordinates are in kilometers, with the ellipse center at the origin and major axis horizontal. Add the Moon’s radius to the stated surface altitudes.')
calc(52,r'AB=10\ \mathrm{cm},\quad VF=p,\quad x_{CD}=11\ \mathrm{cm}','꼭짓점을 원점, 축을 양의 가로축으로 둔다. 초점에서 단면 폭이 주어진 포물선 반사경의 (a) 방정식 (b) 지정 위치의 개구 지름을 구하라.','Place the vertex at the origin and axis along the positive horizontal direction. Given the reflector width at the focus, find (a) its equation and (b) the aperture diameter at the specified position.',[r'y^2=4px,\quad(x,y)=(p,\pm5)\Rightarrow25=4p^2\Rightarrow p=5/2',r'x=11\Rightarrow y=\pm\sqrt{110}'],r'\text{(a)}\ y^2=10x;\quad\text{(b)}\ CD=2\sqrt{110}\ \mathrm{cm}\approx20.9762\ \mathrm{cm}',sub='ab')
calc(53,r'AB=400\ \mathrm{mi},\quad\Delta t=1200\ \mu\mathrm{s},\quad v=980\ \mathrm{ft}/\mu\mathrm{s}','동시에 보낸 신호 중 동쪽 관측소의 신호가 먼저 도착한다. (a) 배가 놓인 쌍곡선 방정식 (b) 배가 동쪽 관측소의 정북쪽일 때 해안까지 거리를 구하라.','The eastern station’s simultaneous signal arrives first. Find (a) the ship’s hyperbola and (b) its distance from shore if due north of the eastern station.',[r'A=(-200,0),\quad B=(200,0),\quad c=200',r'2a=980(1200)/5280=2450/11,\quad a=1225/11,\quad b^2=3339375/121',r'x=200=c\Rightarrow y=b^2/a=133575/539'],r'\text{(a)}\ \frac{x^2}{1500625/121}-\frac{y^2}{3339375/121}=1,\quad x>0;\quad\text{(b)}\ y=133575/539\ \mathrm{mi}\approx247.8200\ \mathrm{mi}','해안 중점을 원점으로 하고 가로축을 동쪽으로 둔다. 동쪽 신호가 먼저 도착하므로 동쪽 초점에 더 가까운 오른쪽 가지를 선택한다.','Use the coast midpoint as origin and east as positive horizontal direction; the earlier eastern signal selects the right branch, closer to the eastern focus.',sub='ab')
calc(54,r'F_1=(-c,0),\quad F_2=(c,0),\quad V=(\pm a,0),\quad c>a>0','거리 차의 정의로부터 쌍곡선 표준 방정식을 유도하라.','Derive the standard hyperbola equation from the distance-difference definition.',[r'd_1-d_2=2a\quad\text{on the right branch}',r'd_1^2-d_2^2=4cx=4a(d_2+a)\Rightarrow d_2=cx/a-a',r'(x-c)^2+y^2=(cx/a-a)^2',r'y^2=(c^2-a^2)(x^2/a^2-1)'],r'\frac{x^2}{a^2}-\frac{y^2}{b^2}=1,\quad b^2=c^2-a^2','왼쪽 가지는 대칭으로 얻는다. 제곱 후에는 각 가지에서 거리 차의 부호를 원래 정의와 대조해 외래 해를 배제한다.','Obtain the left branch by symmetry; after squaring, check the signed distance difference on each branch to exclude extraneous points.')
calc(55,r'y^2/a^2-x^2/b^2=1,\quad a,b>0','위쪽 가지의 함수가 위로 오목함을 증명하라.','Prove that the function on the upper branch is concave upward.',[r'y=\frac ab\sqrt{x^2+b^2}',r'y\prime=\frac{ax}{b\sqrt{x^2+b^2}}'],r'y\prime\prime=\frac{ab}{(x^2+b^2)^{3/2}}>0\quad(x\in\mathbb R)')
calc(56,r'F=(1,1),(-1,-1),\quad2a=4','회전된 타원의 방정식을 구하라.','Find the equation of the rotated ellipse.',[r'u=(x+y)/\sqrt2,\quad v=(x-y)/\sqrt2',r'a=2,\quad c=\sqrt2,\quad b^2=4-2=2',r'u^2/4+v^2/2=1'],r'\frac{(x+y)^2}{8}+\frac{(x-y)^2}{4}=1\quad\Longleftrightarrow\quad3x^2-2xy+3y^2=8')
calc(57,r'\frac{x^2}{k}+\frac{y^2}{k-16}=1','(a) 큰 양의 계수 (b) 작은 양의 계수 (c) 음의 계수에 따른 곡선 종류를 구하고 (d) 두 실수 곡선 족의 공통 초점을 보여라.','Classify the curve for (a) large positive, (b) small positive, and (c) negative coefficient; (d) show the two real families share their foci.',[r'\text{(a)}\ k>16:\quad a^2=k,\ b^2=k-16,\ c^2=16',r'\text{(b)}\ 0<k<16:\quad x^2/k-y^2/(16-k)=1,\ c^2=k+(16-k)=16',r'\text{(c)}\ k<0:\quad x^2/k+y^2/(k-16)\le0'],r'\text{(a)}\ k>16:\ \text{ellipse};\quad\text{(b)}\ 0<k<16:\ \text{hyperbola};\quad\text{(c)}\ k<0:\ \varnothing;\quad\text{(d)}\ F=(\pm4,0)','영과 십육은 원래 식의 분모가 영이 되는 제외값이다.','Zero and sixteen are excluded because an original denominator vanishes.',sub='abcd')
calc(58,r'y^2=4px,\quad P=(x_0,y_0),\quad p\ne0','(a) 지정점의 접선 공식을 증명하라. (b) 가로축 절편을 이용해 접선을 그리는 방법을 설명하라.','(a) Prove the tangent formula at the specified point. (b) Use its horizontal-axis intercept to explain how to draw the tangent.',[r'2y_0(y-y_0)=4p(x-x_0)',r'y_0^2=4px_0\Rightarrow y_0y=2p(x+x_0)',r'y=0\Rightarrow x=-x_0'],r'\text{(a)}\ y_0y=2p(x+x_0);\quad\text{(b)}\ (-x_0,0)','접점과 가로축 절편을 연결한다. 꼭짓점에서는 두 점이 일치하므로 공식을 직접 써서 수직 접선을 얻는다.','Join the contact point to the horizontal intercept; at the vertex the two points coincide, so use the formula directly to get the vertical tangent.',sub='ab')
svg(58,'Example p=1, P=(1,2)',[('parabola',sample(lambda t:t*t/4,lambda t:t,-3,4)),('tangent through (-1,0)',[(-2,-1),(4,5)])],arrows=False)
calc(59,r'x^2=4py,\quad p\ne0','준선 위 임의의 점에서 그은 두 접선이 수직임을 증명하라.','Prove that the two tangents drawn from any point on the directrix are perpendicular.',[r'\text{tangent of slope }m:\quad y=mx-pm^2',r'Q=(h,-p)\Rightarrow pm^2-hm-p=0',r'm_1m_2=-1,\quad\Delta=h^2+4p^2>0'],r'm_1m_2=-1\quad\Rightarrow\quad\text{perpendicular}')
calc(60,r'F_1,F_2','같은 두 초점을 가진 타원과 쌍곡선의 모든 교점에서 접선이 수직임을 증명하라.','Prove that confocal ellipse and hyperbola tangents are perpendicular at every intersection.',[r'd_i=|P-F_i|,\quad u_i=\nabla d_i=(P-F_i)/|P-F_i|',r'\nabla(d_1+d_2)=u_1+u_2,\quad\nabla(d_1-d_2)=u_1-u_2',r'(u_1+u_2)\cdot(u_1-u_2)=|u_1|^2-|u_2|^2=0'],r'\text{tangents intersect at }\pi/2','비퇴화 곡선의 교점에서는 두 법선이 영이 아니며, 두 직교 법선을 함께 직각 회전한 접선들도 직교한다.','At intersections of nondegenerate curves both normals are nonzero; rotating the perpendicular normals by a right angle gives perpendicular tangents.')
def simpson(a,b,n):
 h=math.pi/(2*n);f=lambda t:math.hypot(a*math.sin(t),b*math.cos(t));vals=[f(j*h) for j in range(n+1)];v=4*h/3*(vals[0]+vals[-1]+sum((4 if j%2 else 2)*vals[j] for j in range(1,n)));return v,vals
v,vals=simpson(3,2,8)
calc(61,r'9x^2+4y^2=36,\quad n=8','매개식과 심프슨 법칙으로 둘레를 근사하라.','Use parametric equations and Simpson’s rule to approximate the perimeter.',[r'x=2\sin t,\quad y=3\cos t,\quad L=4\int_0^{\pi/2}\sqrt{4\cos^2t+9\sin^2t}\,dt',r'h=\pi/16,\quad f_j=\sqrt{4\cos^2(jh)+9\sin^2(jh)}',r'L\approx\frac{4h}{3}[f_0+4f_1+2f_2+4f_3+2f_4+4f_5+2f_6+4f_7+f_8]'],rf'L\approx{v:.8f}','대칭으로 사분면 길이에 팔 분할 심프슨 법칙을 적용한 다음 네 배 했다.','Apply eight Simpson subintervals to one quadrant and multiply by four.')
v2,vals2=simpson(5.9e9,5.7e9,10)
calc(62,r'2a=1.18\times10^{10}\ \mathrm{km},\quad2b=1.14\times10^{10}\ \mathrm{km},\quad n=10','주어진 명왕성 타원 궤도를 한 바퀴 도는 거리를 심프슨 법칙으로 근사하라.','Use Simpson’s rule to approximate the distance traveled in one full orbit of the specified Pluto ellipse.',[r'a=5.9\times10^9,\quad b=5.7\times10^9,\quad L=4\int_0^{\pi/2}\sqrt{a^2\sin^2t+b^2\cos^2t}\,dt',r'h=\pi/20,\quad f_j=\sqrt{a^2\sin^2(jh)+b^2\cos^2(jh)}',r'L\approx\frac{4h}{3}[f_0+4f_1+2f_2+4f_3+2f_4+4f_5+2f_6+4f_7+2f_8+4f_9+f_{10}]'],rf'L\approx{v2:.2f}\ \mathrm{{km}}\approx3.64451831\times10^{{10}}\ \mathrm{{km}}','책에서 주어진 두 축 길이의 절반을 반축으로 사용하며, 한 사분면을 열 등분했다.','Use half the source axis lengths as semiaxes and ten subintervals for one quadrant.')
calc(63,r'x^2/a^2-y^2/b^2=1,\quad a,b>0','초점을 지나는 수직선과 쌍곡선이 둘러싸는 넓이를 구하라.','Find the area enclosed by the hyperbola and a vertical line through a focus.',[r'c=\sqrt{a^2+b^2},\quad y=\pm\frac ba\sqrt{x^2-a^2}',r'A=\frac{2b}{a}\int_a^c\sqrt{x^2-a^2}\,dx',r'\int\sqrt{x^2-a^2}\,dx=\frac12[x\sqrt{x^2-a^2}-a^2\ln(x+\sqrt{x^2-a^2})]'],r'A=\frac{b^2c}{a}-ab\ln\frac{c+b}{a},\quad c=\sqrt{a^2+b^2}','어느 초점을 골라도 대칭으로 넓이가 같다.','Either focus gives the same area by symmetry.')
calc(64,r'x^2/a^2+y^2/b^2=1,\quad a>b>0','타원을 (a) 장축 (b) 단축 둘레로 회전한 입체의 부피를 구하라.','Find volumes obtained by rotating the ellipse about (a) its major axis and (b) its minor axis.',[r'\text{(a)}\ V=\pi\int_{-a}^ab^2(1-x^2/a^2)\,dx',r'\text{(b)}\ V=\pi\int_{-b}^ba^2(1-y^2/b^2)\,dy'],r'\text{(a)}\ V=4\pi ab^2/3;\quad\text{(b)}\ V=4\pi a^2b/3',sub='ab')
calc(65,r'9x^2+4y^2=36,\quad y\ge0','타원 윗부분과 가로축이 둘러싸는 영역의 도심을 구하라.','Find the centroid of the region between the upper ellipse and the horizontal axis.',[r'y=3\sqrt{1-x^2/4},\quad-2\le x\le2,\quad A=3\pi',r'\bar x=0,\quad M_x=\frac12\int_{-2}^2 9(1-x^2/4)\,dx=12'],r'(\bar x,\bar y)=(0,4/\pi)')
calc(66,r'x^2/a^2+y^2/b^2=1,\quad a>b>0','타원을 (a) 장축 (b) 단축 둘레로 회전해 얻는 타원체의 겉넓이를 구하라.','Find the ellipsoid surface area obtained by rotation about (a) the major axis and (b) the minor axis.',[r'c=\sqrt{a^2-b^2},\quad e=c/a',r'\text{(a)}\ S=4\pi b\int_0^1\sqrt{a^2-c^2u^2}\,du',r'\text{(b)}\ S=4\pi a\int_0^1\sqrt{b^2+c^2u^2}\,du',r'\operatorname{asinh}(c/b)=\operatorname{artanh}(e)'],r'\text{(a)}\ S=2\pi b^2+\frac{2\pi ab}{e}\arcsin e;\quad\text{(b)}\ S=2\pi a^2+\frac{2\pi b^2}{e}\operatorname{artanh}e,\quad e=\sqrt{1-b^2/a^2}','이심률이 영으로 가는 극한에서는 두 식 모두 구의 겉넓이를 준다.','As eccentricity tends to zero, both formulas tend to the sphere surface area.',sub='ab')
calc(67,r'x^2/a^2+y^2/b^2=1,\quad F_1,F_2,\quad P=(x_1,y_1)','두 초점으로 연결한 선분이 접선과 이루는 두 각도가 같음을 증명하라.','Prove that the two focal segments make equal angles with the tangent.',[r'u_i=(P-F_i)/|P-F_i|,\quad n\parallel u_1+u_2',r'\tau\cdot(u_1+u_2)=0\Rightarrow\tau\cdot u_1=-\tau\cdot u_2',r'|\tau\cdot u_1|=|\tau\cdot u_2|'],r'\alpha=\beta','단위 접선과 두 단위 초점 방향의 내적 절댓값이 같아 접선과 이루는 각이 같다. 합벡터 방향의 법선으로 입사 방향을 반사하면 다른 초점을 향하는 방향이 된다.','Equal absolute dot products with the unit tangent give equal line angles. Reflection in the normal along the sum sends the incoming direction toward the other focus.')
calc(68,r'x^2/a^2-y^2/b^2=1,\quad F_1,F_2,\quad P=(x_1,y_1)','두 초점 방향과 접선 사이의 반사각이 같음을 증명하라.','Prove equality of the reflection angles between the focal directions and tangent.',[r'u_i=(P-F_i)/|P-F_i|,\quad n\parallel u_1-u_2',r'\tau\cdot(u_1-u_2)=0\Rightarrow\tau\cdot u_1=\tau\cdot u_2',r'\widehat n=(u_1-u_2)/|u_1-u_2|,\quad -u_2-2[(-u_2)\cdot\widehat n]\widehat n=-u_1'],r'\alpha=\beta','초점 거리 차의 수준곡선이므로 법선은 두 단위 초점 방향의 차이다. 다른 초점으로 향하던 빛은 반사 후 첫 초점으로 향한다.','The distance-difference level curve has normal equal to the difference of the unit focal directions. A ray aimed at the second focus is reflected toward the first.')
calc(69,r'C_1=(-1,0),\ R_1=3;\quad C_2=(1,0),\ R_2=5','그림처럼 큰 원 내부이면서 작은 원 외부에서 두 원에 접하는 양의 반지름 원들을 생각하라. 그 중심들이 놓이는 타원 방정식을 구하고 원문의 모든 접원이라는 표현의 범위를 설명하라.','Consider positive-radius circles tangent to both given circles while lying inside the larger and outside the smaller, as illustrated. Find the ellipse containing their centers and clarify the source phrase “all tangent circles.”',[r'P=(x,y),\quad\rho>0,\quad |P-C_1|=3+\rho,\quad|P-C_2|=5-\rho',r'|P-C_1|+|P-C_2|=8\Rightarrow a=4,\quad c=1,\quad b^2=15',r'P=(-4,0)\Rightarrow\rho=0'],r'x^2/16+y^2/15=1,\quad P\ne(-4,0)','원문 그림의 두 원 사이 접원 조건이 필요하다. 이를 빼면 중심 음육·영, 반지름 이인 원도 양쪽 원에 외접하지만 타원 위에 있지 않아 문자 그대로 모든 접원이라는 주장은 성립하지 않는다. 왼쪽 끝점은 반지름 영인 퇴화 경우라 양의 반지름 중심 집합에서는 제외한다.','The between-circles condition shown in the source figure is necessary. Without it, a circle centered at (-6,0) with radius two is externally tangent to both but its center is not on the ellipse, disproving the unrestricted “all circles” wording. Exclude the left endpoint because it corresponds to zero radius.')
curves=[('inner given circle',sample(lambda t:-1+3*math.cos(t),lambda t:3*math.sin(t),0,2*math.pi)),('outer given circle',sample(lambda t:1+5*math.cos(t),lambda t:5*math.sin(t),0,2*math.pi)),('center ellipse',sample(lambda t:4*math.cos(t),lambda t:math.sqrt(15)*math.sin(t),0,2*math.pi))]
for ang in [0,1.1,2.2]:
 px=4*math.cos(ang);py=math.sqrt(15)*math.sin(ang);rho=math.hypot(px+1,py)-3
 assert abs(math.hypot(px-1,py)+rho-5)<1e-12
 curves.append(('sample tangent circle',sample(lambda t,px=px,rho=rho:px+rho*math.cos(t),lambda t,py=py,rho=rho:py+rho*math.sin(t),0,2*math.pi)))
svg(69,'Tangent circles and the locus of centers',curves,arrows=False)
# Structure, equation and quadrature checks.
for n,k,e in [(27,'쌍곡선','Hyperbola'),(28,'포물선','Parabola'),(29,'타원','Ellipse'),(30,'쌍곡선','Hyperbola'),(31,'포물선','Parabola'),(32,'타원','Ellipse')]:
 ex=next(z for z in items if z['number']==n);ex['answer']['ko']=k+'. '+ex['answer']['ko'];ex['answer']['en']=e+'. '+ex['answer']['en']
items.sort(key=lambda e:e['number']);assert [e['number'] for e in items]==list(range(1,70))
raw={'section':'10.5','source':{'title':'Calculus','edition':'9','language':'en','printedPages':[746,747,748,749],'pdfPages':[783,784,785,786]},'scope':{'kind':'exercise','numbers':list(range(1,70)),'total':69,'note':bi('일반 연습문제 전체. 그림의 좌표와 접하는 방향을 명시했다.','All ordinary exercises; graph coordinates and tangency directions are made explicit.')},'exercises':items}
import xml.etree.ElementTree as ET
for ex in items:
 for field in ['statement','answer']:
  assert re.findall(r'\\\((.*?)\\\)',ex[field]['ko'])==re.findall(r'\\\((.*?)\\\)',ex[field]['en']),(ex['number'],field)
 if 'figure' in ex:ET.parse(BASE/'exercise-content'/ex['figure']['src'].replace('../exercise-content/',''))
def clean(x):
 if isinstance(x,str):assert not any(ord(c)<32 and c!='\n' for c in x),repr(x)
 elif isinstance(x,dict):
  for v in x.values():clean(v)
 elif isinstance(x,list):
  for v in x:clean(v)
clean(raw)
x,y=S.symbols('x y')
assert S.expand(9*(x-3)**2+(y+1)**2-36)==9*x*x-54*x+y*y+2*y+46
assert S.expand(9*(y-2)**2-4*(x+1)**2-36)==9*y*y-4*x*x-36*y-8*x-4
assert S.Rational(25,9)-S.Rational(16,9)==1
assert S.Rational(36,4)-S.Rational(64,8)==1
assert S.simplify(S.sqrt(400**2+S.Rational(133575,539)**2)-S.Rational(133575,539)-S.Rational(2450,11))==0
import mpmath as mp
mp.mp.dps=35
assert abs(v-4*mp.quad(lambda t:mp.sqrt(4*mp.cos(t)**2+9*mp.sin(t)**2),[0,mp.pi/2]))<1e-5
assert abs(v2-4*mp.quad(lambda t:mp.sqrt(mp.mpf('5.9e9')**2*mp.sin(t)**2+mp.mpf('5.7e9')**2*mp.cos(t)**2),[0,mp.pi/2]))<1
path=BASE/'exercise-content/s10-5.json';sys.path.insert(0,str(BASE));import build_exercises as build
build.validate_document(raw,path);path.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
print('10.5:',len(items),'cards;',sum('figure' in e for e in items),'SVG; completed squares, graph coordinates, distance conditions, quadrature, bilingual math and XML checked')
