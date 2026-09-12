import json,math,html,sys,ast,re
from pathlib import Path
import sympy as S
import mpmath as mp
BASE=Path(__file__).resolve().parents[1];items=[];t=S.symbols('t',real=True)
def M(s):return r'\('+s+r'\)'
def bi(k,e=None):return {'ko':k,'en':k if e is None else e}
def add(n,sk,se,steps,ak,ae,ck,ce,sub=''):
 p=755 if n<=14 else 756
 items.append(dict(id=f'stewart9-exercise-10.6-{n}',number=n,subparts=list(sub),source=dict(printedPage=p,pdfPage=p+37),topic=bi('극좌표의 이차곡선','Conics in polar coordinates'),statement=bi(sk,se),hint=bi('분모 상수항을 일로 정규화한 뒤 이심률과 초점·준선 거리를 비교한다.','Normalize the denominator constant to one, then identify eccentricity and the focus-directrix distance.'),steps={'ko':[a for a,b in steps],'en':[b for a,b in steps]},answer=bi(ak,ae),check=bi(ck,ce),conceptHref='../../calc1/index.html',status='math-verified'))
for file,names in [('s10-1-author.py',['sample','svg','multi']),('s10-3-author.py',['polar'])]:
 source=(BASE/'exercise-checks'/file).read_text()
 for node in ast.parse(source).body:
  if isinstance(node,ast.FunctionDef) and node.name in names:exec(ast.get_source_segment(source,node).replace('s10-1-','s10-6-'))
def calc(n,eq,tk,te,lines,ans,k='',e='',sub=''):
 steps=[(M(x),M(x)) for x in lines]
 if k:steps.append((k,e))
 add(n,M(eq)+' '+tk,M(eq)+' '+te,steps,M(ans),M(ans),'초점에서의 거리 대 준선 거리의 비와 주어진 꼭짓점·궤도 자료를 대입해 확인했다.','Checked the ratio of focal distance to directrix distance and substitution of the given vertex or orbital data.',sub)
for n,eq,lines,ans in [(1,r'\text{parabola},\quad x=2',[r'e=1,\quad d=2,\quad r=e(d-r\cos\theta)'],r'r=\frac2{1+\cos\theta}'),(2,r'\text{ellipse},\quad e=1/3,\quad y=6',[r'ed=2,\quad r=e(6-r\sin\theta)'],r'r=\frac6{3+\sin\theta}'),(3,r'\text{hyperbola},\quad e=2,\quad y=-4',[r'ed=8,\quad r=e(4+r\sin\theta)'],r'r=\frac8{1-2\sin\theta}'),(4,r'\text{hyperbola},\quad e=5/2,\quad x=-3',[r'ed=15/2,\quad r=e(3+r\cos\theta)'],r'r=\frac{15}{2-5\cos\theta}'),(6,r'\text{ellipse},\quad e=0.6,\quad r=4\csc\theta\ \text{(directrix)}',[r'y=4,\quad ed=12/5'],r'r=\frac{12}{5+3\sin\theta}'),(7,r'\text{parabola},\quad V=(3,\pi/2)\ \text{(polar)}',[r'V=(0,3)\ \text{(Cartesian)},\quad\text{directrix }y=6'],r'r=\frac6{1+\sin\theta}'),(8,r'\text{hyperbola},\quad e=2,\quad r=-2\sec\theta\ \text{(directrix)}',[r'x=-2,\quad ed=4'],r'r=\frac4{1-2\cos\theta}')]:
 calc(n,eq,'초점이 원점인 이차곡선의 극좌표 방정식을 구하라.','Find a polar equation for the conic with a focus at the origin.',lines,ans)
calc(5,r'\text{ellipse},\quad e=2/3,\quad V=(2,\pi)\ \text{(polar)}','초점이 원점인 타원의 가능한 극좌표 방정식을 구하라.','Find possible polar equations of the ellipse with a focus at the origin.',[r'r=\frac p{1-(2/3)\cos\theta},\quad r(\pi)=3p/5=2\Rightarrow p=10/3',r'r=\frac p{1+(2/3)\cos\theta},\quad r(\pi)=3p=2\Rightarrow p=2/3'],r'r=\frac{10}{3-2\cos\theta}\quad\text{or}\quad r=\frac2{3+2\cos\theta}','원문은 주어진 꼭짓점이 초점에서 가까운 쪽인지 먼 쪽인지 정하지 않는다. 두 방정식은 모두 조건을 만족한다.','The source does not specify whether the given vertex is the near or far one relative to the focus; both equations satisfy the data.')
matching=[(9,r'r=3/(1-\sin\theta)',lambda t:3/(1-math.sin(t)),'VI',r'x^2=6y+9','위로 열린 포물선이며 꼭짓점은 세로축의 음의 쪽이다.','An upward-opening parabola with vertex below the origin.',(-7,7,-3,8)),(10,r'r=9/(1+2\cos\theta)',lambda t:9/(1+2*math.cos(t)),'III',r'(x-6)^2/9-y^2/27=1','가로축 방향 쌍곡선이며 중심이 원점 오른쪽이다.','A horizontal hyperbola centered to the right of the origin.',(-3,15,-12,12)),(11,r'r=12/(8-7\cos\theta)',lambda t:12/(8-7*math.cos(t)),'II',r'e=7/8<1','가로로 긴 타원이며 오른쪽으로 뻗는다.','A horizontally elongated ellipse extending to the right.',(-2,13,-5,5)),(12,r'r=12/(4+3\sin\theta)',lambda t:12/(4+3*math.sin(t)),'V',r'e=3/4<1','세로로 긴 타원이며 아래쪽으로 뻗는다.','A vertically elongated ellipse extending downward.',(-6,6,-13,3)),(13,r'r=5/(2+3\sin\theta)',lambda t:5/(2+3*math.sin(t)),'IV',r'(y-3)^2/4-x^2/5=1','세로축 방향 쌍곡선이며 중심은 원점 위이다.','A vertical hyperbola centered above the origin.',(-7,7,-4,10)),(14,r'r=3/(2-2\cos\theta)',lambda t:3/(2-2*math.cos(t)),'I',r'y^2=3x+9/4','오른쪽으로 열린 포물선이며 꼭짓점은 원점 왼쪽이다.','A right-opening parabola with vertex left of the origin.',(-2,8,-6,6))]
for n,eq,f,label,ident,k,e,bounds in matching:
 calc(n,eq,'원문의 그래프 I–VI에 대응시키고 이유를 설명하라.','Match to source graph I–VI and explain.',[ident],rf'\text{{Graph {label}}}',k,e)
 svg(n,f'Graph {label}: original conic plot',[('conic',polar(f,.00001,2*math.pi-.00001,16000))],bounds,False)
classify=[(15,r'r=4/(5-4\sin\theta)',S.Rational(4,5),S.Rational(4,5),'sin',-1),(16,r'r=1/(2+\sin\theta)',S.Rational(1,2),S.Rational(1,2),'sin',1),(17,r'r=2/(3+3\sin\theta)',S.Rational(2,3),S.Integer(1),'sin',1),(18,r'r=5/(2-4\cos\theta)',S.Rational(5,2),S.Integer(2),'cos',-1),(19,r'r=9/(6+2\cos\theta)',S.Rational(3,2),S.Rational(1,3),'cos',1),(20,r'r=1/(3-3\sin\theta)',S.Rational(1,3),S.Integer(1),'sin',-1),(21,r'r=3/(4-8\cos\theta)',S.Rational(3,4),S.Integer(2),'cos',-1),(22,r'r=4/(2+3\cos\theta)',S.Integer(2),S.Rational(3,2),'cos',1)]
for n,eq,p,e,trig,sgn in classify:
 d=p/e;direct=rf'{"y" if trig=="sin" else "x"}={S.latex(sgn*d)}';kind='ellipse' if e<1 else'parabola' if e==1 else'hyperbola';ek={'ellipse':'타원','parabola':'포물선','hyperbola':'쌍곡선'}[kind]
 normalized=rf'r=\frac{{{S.latex(p)}}}{{1{"+" if sgn>0 else "-"}{S.latex(e)}\{trig}\theta}}'
 calc(n,eq,'(a) 이심률 (b) 곡선 종류 (c) 준선을 구하고 (d) 그래프를 그려라.','Find (a) eccentricity, (b) conic type, (c) directrix, and (d) a graph.',[normalized,rf'ed={S.latex(p)}\Rightarrow d={S.latex(d)}'],rf'\text{{(a)}}\ e={S.latex(e)};\quad\text{{(b)}}\ \text{{{kind}}};\quad\text{{(c)}}\ {direct}','이심률이 일보다 작으면 타원, 같으면 포물선, 크면 쌍곡선이다. 첨부 그림은 준선과 전체 곡선의 유한 표시창이다.','Eccentricity below, equal to, or above one gives an ellipse, parabola, or hyperbola. The figure shows the directrix and a finite window of the full conic.',sub='abcd')
 f=lambda t,p=float(p),e=float(e),sgn=sgn,trig=trig:p/(1+sgn*e*(math.sin(t) if trig=='sin' else math.cos(t)))
 extent=max(3,float(d)*2,float(p)*5);line=[(-extent,sgn*float(d)),(extent,sgn*float(d))] if trig=='sin' else[(sgn*float(d),-extent),(sgn*float(d),extent)]
 svg(n,'Conic and its directrix',[('conic',polar(f,.00001,2*math.pi-.00001,14000)),('directrix',line)],(-extent,extent,-extent,extent),False)
calc(23,r'r=1/(1-2\sin\theta)','(a) 이심률·준선을 구하고 함께 그려라. (b) 원점 주위 반시계로 사분의 삼 파이만큼 회전한 방정식과 그래프를 구하라.','(a) Find eccentricity and directrix and graph both. (b) Rotate counterclockwise by three quarters pi about the pole and give the equation and graph.',[r'e=2,\quad ed=1\Rightarrow d=1/2,\quad\text{directrix }y=-1/2',r'\theta\mapsto\theta-3\pi/4'],r'\text{(a)}\ e=2,\ y=-1/2;\quad\text{(b)}\ r=\frac1{1-2\sin(\theta-3\pi/4)}',sub='ab')
multi(23,[('Original hyperbola',[('conic',polar(lambda t:1/(1-2*math.sin(t)),.0001,2*math.pi-.0001,15000)),('directrix',[(-4,-.5),(4,-.5)])],(-4,4,-4,4)),('Rotation by 3pi/4',[('rotated conic',polar(lambda t:1/(1-2*math.sin(t-3*math.pi/4)),.0001,2*math.pi-.0001,15000)),('rotated directrix',[(-3,3+1/math.sqrt(2)),(3,-3+1/math.sqrt(2))])],(-4,4,-4,4))])
calc(24,r'r=4/(5+6\cos\theta)','곡선과 준선을 그린 뒤 원점 주위 반시계로 삼분의 파이만큼 회전한 곡선을 그려라.','Graph the conic and its directrix, then the curve rotated counterclockwise by one third pi about the pole.',[r'e=6/5,\quad ed=4/5\Rightarrow d=2/3',r'\theta\mapsto\theta-\pi/3'],r'\text{directrix }x=2/3;\quad r_{\rm rotated}=\frac4{5+6\cos(\theta-\pi/3)}')
multi(24,[('Original hyperbola',[('conic',polar(lambda t:4/(5+6*math.cos(t)),.0001,2*math.pi-.0001,15000)),('directrix',[(2/3,-5),(2/3,5)])],(-5,5,-5,5)),('Rotation by pi/3',[('rotated conic',polar(lambda t:4/(5+6*math.cos(t-math.pi/3)),.0001,2*math.pi-.0001,15000))],(-5,5,-5,5))])
calc(25,r'r=e/(1-e\cos\theta),\quad e=0.4,0.6,0.8,1.0','같은 화면에 곡선을 그리고 이심률의 효과를 설명하라.','Plot the curves on common axes and explain the effect of eccentricity.',[r'\text{directrix }x=-1',r'0<e<1:\quad a=e/(1-e^2),\quad C=(e^2/(1-e^2),0)',r'e=1:\quad y^2=2x+1'],r'e=0.4,0.6,0.8:\ \text{ellipses};\quad e=1:\ \text{parabola}','이심률이 커질수록 타원이 가로로 길어지고 오른쪽 끝이 멀어진다. 일에서는 오른쪽으로 열린 포물선이 된다. 초점과 준선은 고정이다.','Increasing eccentricity elongates the ellipses horizontally and pushes the right end outward; at one the curve becomes a right-opening parabola. Focus and directrix stay fixed.')
svg(25,'Common focus and directrix',[(f'e={e}',polar(lambda t,e=e:e/(1-e*math.cos(t)),.0001,2*math.pi-.0001,12000)) for e in [.4,.6,.8,1]]+[('directrix',[(-1,-4),(-1,4)])],(-1.5,6,-4,4),False)
calc(26,r'r=ed/(1+e\sin\theta),\quad d>0,\ e>0','(a) 이심률을 일로 두고 준선 거리 변화에 따른 그림과 효과를 설명하라. (b) 준선 거리를 일로 두고 이심률 변화에 따른 그림과 효과를 설명하라.','(a) Set eccentricity to one and graph/explain changes with directrix distance. (b) Set directrix distance to one and graph/explain changes with eccentricity.',[r'\text{(a)}\ e=1:\quad x^2=d^2-2dy,\quad V=(0,d/2)',r'\text{(b)}\ d=1:\quad0<e<1\ \text{ellipse},\ e=1\ \text{parabola},\ e>1\ \text{hyperbola}'],r'\text{(a)}\ d\text{ scales the curve from the pole};\quad\text{(b)}\ e<1,=1,>1:\ \text{ellipse, parabola, hyperbola}','거리 배율은 원점 중심 확대이고 모두 아래로 열린 포물선이다. 고정된 준선에서는 이심률이 곡선 종류를 바꾼다.','Changing distance scales the curve about the pole; all curves in (a) are downward-opening parabolas. With a fixed directrix, eccentricity changes the conic type.',sub='ab')
multi(26,[('a: e=1, varying d',[(f'd={d}',polar(lambda t,d=d:d/(1+math.sin(t)),.0001,2*math.pi-.0001,12000)) for d in [.5,1,2]],(-6,6,-6,3)),('b: d=1, varying e',[(f'e={e}',polar(lambda t,e=e:e/(1+e*math.sin(t)),.0001,2*math.pi-.0001,14000)) for e in [.5,.8,1,1.5,2]],(-6,6,-6,6))])
for n,eq,line,relation,ans in [(27,r'e>0,\ d>0,\quad\text{directrix }x=-d',r'\text{distance to directrix}=|x+d|',r'r=e(d+r\cos\theta)',r'r=\frac{ed}{1-e\cos\theta}'),(28,r'e>0,\ d>0,\quad\text{directrix }y=d',r'\text{distance to directrix}=|d-y|',r'r=e(d-r\sin\theta)',r'r=\frac{ed}{1+e\sin\theta}'),(29,r'e>0,\ d>0,\quad\text{directrix }y=-d',r'\text{distance to directrix}=|y+d|',r'r=e(d+r\sin\theta)',r'r=\frac{ed}{1-e\sin\theta}')]:
 calc(n,eq,'초점이 원점인 이차곡선의 극좌표 방정식을 유도하라.','Derive the polar equation of the conic with focus at the origin.',[line,relation],ans,'초점이 있는 쪽에서 양의 반지름으로 유도한 뒤 정리한다. 쌍곡선의 반대 가지는 부호 있는 반지름 표현으로 포함되며, 거리의 절댓값 관계도 만족한다.','Derive on the focus side using positive radius, then rearrange. For a hyperbola, signed radii include the other branch and still satisfy the absolute-distance relation.')
calc(30,r'r=c/(1+\cos\theta),\quad r=d/(1-\cos\theta),\quad c,d>0','두 포물선이 직각으로 교차함을 증명하라.','Prove the two parabolas intersect at right angles.',[r'y^2=c^2-2cx,\quad y^2=d^2+2dx',r'x=(c-d)/2,\quad y^2=cd',r'm_1=-c/y,\quad m_2=d/y\Rightarrow m_1m_2=-cd/y^2=-1'],r'\text{intersection angle}=\pi/2')
for n,eq,a,e in [(31,r'e=0.093,\quad a=2.28\times10^8\ \mathrm{km}',S.Integer(228000000),S.Rational(93,1000)),(32,r'e=0.048,\quad2a=1.56\times10^9\ \mathrm{km}',S.Integer(780000000),S.Rational(48,1000)),(33,r'e=0.97,\quad2a=36.18\ \mathrm{AU}',S.Rational(1809,100),S.Rational(97,100)),(34,r'e=0.9951,\quad2a=356.5\ \mathrm{AU}',S.Rational(713,4),S.Rational(9951,10000))]:
 p=a*(1-e*e);unit=r'\mathrm{km}' if n<=32 else r'\mathrm{AU}';ans=rf'r=\frac{{{S.latex(p)}}}{{1+{S.latex(e)}\cos\theta}}\ {unit}'
 lines=[r'r=\frac{a(1-e^2)}{1+e\cos\theta}',rf'a={S.latex(a)},\quad a(1-e^2)={S.latex(p)}']
 if n==33:ans+=rf';\quad r_{{\max}}=a(1+e)={float(a*(1+e)):.4f}\ \mathrm{{AU}}'
 if n==34:ans+=rf';\quad r_{{\min}}=a(1-e)={float(a*(1-e)):.6f}\ \mathrm{{AU}}'
 tk='주어진 궤도 자료로 극방정식을 구하라.'+(' 태양에서의 최대 거리를 구하라.' if n==33 else ' 태양에 가장 가까운 거리를 구하라.' if n==34 else '')
 te='Find a polar orbit equation from the given data.'+(' Find maximum solar distance.' if n==33 else ' Find minimum solar distance.' if n==34 else '')
 calc(n,eq,tk,te,lines,ans,'태양을 원점에 놓고 가장 가까운 점을 양의 극축 방향으로 택했다. 수치는 책에서 주어진 궤도 모형의 값이다.','Place the Sun at the pole and perihelion on the positive polar axis; numerical data are the orbital model values supplied in the book.')
q=mp.mpf('4.6e7');ecc=mp.mpf('.206');far=q*(1+ecc)/(1-ecc)
calc(35,r'e=0.206,\quad r_{\min}=4.6\times10^7\ \mathrm{km}','주어진 수성 궤도의 최대 태양 거리를 구하라.','Find maximum solar distance for the specified Mercury orbit.',[r'r_{\min}=a(1-e),\quad r_{\max}=a(1+e)',r'r_{\max}=r_{\min}\frac{1+e}{1-e}'],rf'r_{{\max}}=4.6\times10^7\frac{{1.206}}{{0.794}}\ \mathrm{{km}}\approx{float(far):.4f}\ \mathrm{{km}}')
calc(36,r'r_{\min}=4.43\times10^9\ \mathrm{km},\quad r_{\max}=7.37\times10^9\ \mathrm{km}','명왕성 궤도의 이심률을 구하라.','Find eccentricity of the specified Pluto orbit.',[r'a=(r_{\max}+r_{\min})/2,\quad ae=(r_{\max}-r_{\min})/2'],r'e=\frac{7.37-4.43}{7.37+4.43}=\frac{147}{590}\approx0.249153')
mp.mp.dps=45;ecc=mp.mpf('.206');a=mp.mpf('4.6e7')/(1-ecc);b=a*mp.sqrt(1-ecc*ecc);per=4*mp.quad(lambda u:mp.sqrt(a*a*mp.sin(u)**2+b*b*mp.cos(u)**2),[0,mp.pi/2])
with mp.workdps(60):per2=4*mp.quad(lambda u:mp.sqrt(a*a*mp.sin(u)**2+b*b*mp.cos(u)**2),[0,mp.pi/4,mp.pi/2])
assert abs(per-per2)<mp.mpf('1e-30')
calc(37,r'e=0.206,\quad r_{\min}=4.6\times10^7\ \mathrm{km}','수성이 주어진 타원 궤도를 한 번 도는 이동거리를 수치 적분으로 구하라.','Use numerical integration to find the distance Mercury travels in one complete orbit of the given ellipse.',[r'a=\frac{4.6\times10^7}{1-0.206},\quad b=a\sqrt{1-0.206^2}',r'L=4\int_0^{\pi/2}\sqrt{a^2\sin^2t+b^2\cos^2t}\,dt'],rf'L\approx{float(per):.4f}\ \mathrm{{km}}\approx{float(per)/1e8:.8f}\times10^8\ \mathrm{{km}}','반축을 먼저 구해 타원의 호 길이를 적분했다. 정밀도를 높이고 적분 구간을 나누어 같은 결과를 확인했다.','Compute the semiaxes first and integrate ellipse arc length; increased precision and interval splitting confirm the result.')
items.sort(key=lambda e:e['number']);assert [e['number'] for e in items]==list(range(1,38))
raw={'section':'10.6','source':{'title':'Calculus','edition':'9','language':'en','printedPages':[755,756],'pdfPages':[792,793]},'scope':{'kind':'exercise','numbers':list(range(1,38)),'total':37,'note':bi('일반 연습문제 전체. 이차곡선은 부호 있는 반지름까지 포함한다.','All ordinary exercises; conic plots include signed radii.')},'exercises':items}
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
for n,eq,p,e,trig,sgn in classify:
 for theta in [.2,.7,1.4,2.3,3.7,5.1]:
  rr=float(p)/(1+sgn*float(e)*(math.sin(theta) if trig=='sin' else math.cos(theta)));coord=rr*(math.sin(theta) if trig=='sin' else math.cos(theta));distance=abs(coord-sgn*float(p/e));assert abs(abs(rr)-float(e)*distance)<1e-9
assert 10/(3-2*math.cos(math.pi))==2 and 2/(3+2*math.cos(math.pi))==2
path=BASE/'exercise-content/s10-6.json';sys.path.insert(0,str(BASE));import build_exercises as build
build.validate_document(raw,path);path.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
print('10.6:',len(items),'cards;',sum('figure' in e for e in items),'SVG; focus/directrix identities, orbit quadrature, bilingual math and XML checked')
