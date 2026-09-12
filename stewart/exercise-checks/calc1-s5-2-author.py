from calc1_volume_helpers import *
x,y=s.symbols('x y',real=True);P=s.pi;R=s.Rational;b=CalcBook('5.2',[384,385,386,387])
# (source boundary description, strip intervals/radii, integration variable, axis offset)
recs={
1:(r'y=x^2+5,\ y=0,\ x=0,3',[(0,3,x*x+5,0)],x,0),
2:(r'y=\sqrt x,\ y=x/2',[(0,4,s.sqrt(x),x/2)],x,0),
3:(r'y=x^3+1,\ x=0,\ y=9',[(1,9,(y-1)**R(1,3),0)],y,0),
4:(r'y=x/2,\ y=2/x,\ y=2',[(1,2,2*y,2/y)],y,0),
5:(r'y=1-1/x,\ y=0,\ x=3',[(1,3,1-1/x,0)],x,0),
6:(r'x=\sqrt{5-y},\ y=0,\ x=0',[(0,5,s.sqrt(5-y),0)],y,0),
7:(r'8y=x^2,\ y=\sqrt x',[(0,2,s.sqrt(8*y),y*y)],y,0),
8:(r'y=(x-2)^2,\ y=x+10',[(-1,6,x+10,(x-2)**2)],x,0),
9:(r'y=\sin x,\ y=0,\ 0\le x\le\pi',[(0,P,2+s.sin(x),2)],x,-2),
10:(r'y=\sqrt x,\ y=0,\ x=4',[(0,2,6-y*y,2)],y,6),
11:(r'y=x+1,\ y=0,\ x=0,2',[(0,2,x+1,0)],x,0),
12:(r'y=1/x,\ y=0,\ x=1,4',[(1,4,1/x,0)],x,0),
13:(r'y=\sqrt{x-1},\ y=0,\ x=5',[(1,5,s.sqrt(x-1),0)],x,0),
14:(r'y=\sqrt{25-x^2},\ y=0,\ x=2,4',[(2,4,s.sqrt(25-x*x),0)],x,0),
15:(r'x=2\sqrt y,\ x=0,\ y=9',[(0,9,2*s.sqrt(y),0)],y,0),
16:(r'2x=y^2,\ x=0,\ y=4',[(0,4,y*y/2,0)],y,0),
17:(r'y=x^2,\ y=2x',[(0,4,s.sqrt(y),y/2)],y,0),
18:(r'y=6-x^2,\ y=2',[(-2,2,6-x*x,2)],x,0),
19:(r'y=x^3,\ y=\sqrt x',[(0,1,s.sqrt(x),x**3)],x,0),
20:(r'x=2-y^2,\ x=y^4',[(-1,1,2-y*y,y**4)],y,0),
21:(r'y=x^2,\ x=y^2',[(0,1,1-x*x,1-s.sqrt(x))],x,1),
22:(r'y=x^3,\ y=1,\ x=2',[(1,2,x**3+3,4)],x,-3),
23:(r'y=3,\ y=1+\sec x,\ -\pi/3\le x\le\pi/3',[(-P/3,P/3,2,1/s.cos(x))],x,1),
24:(r'y=\sin x,\ y=\cos x,\ 0\le x\le\pi/4',[(0,P/4,1+s.cos(x),1+s.sin(x))],x,-1),
25:(r'y=x^3,\ y=0,\ x=1',[(0,1,2-y**R(1,3),1)],y,2),
26:(r'y=x^2,\ x=y^2',[(0,1,1+s.sqrt(y),1+y*y)],y,-1),
27:(r'x=y^2,\ x=1-y^2',[(-1/s.sqrt(2),1/s.sqrt(2),3-y*y,2+y*y)],y,3),
28:(r'y=x,\ y=0,\ x=2,4',[(0,2,3,1),(2,4,3,y-1)],y,1),
}
# Three regions partition the unit square by y=x and y=x^(1/4).
for k in range(29,41):
 region=(k-29)//4+1;axisname=['y=0','x=0','x=1','y=1'][(k-29)%4]
 if axisname.startswith('y'):
  up,dn={1:(x,0),2:(1,x**R(1,4)),3:(x**R(1,4),x)}[region];v=x
 else:up,dn={1:(1,y),2:(y**4,0),3:(y,y**4)}[region];v=y
 a=int(axisname[-1]);outer,inner=(up,dn)if a==0 else(1-dn,1-up)
 recs[k]=(r'\mathcal R_'+str(region)+r':\ '+{1:r'0\le y\le x\le1',2:r'0\le x\le1,\ x^{1/4}\le y\le1',3:r'0\le x\le1,\ x\le y\le x^{1/4}'}[region],[(0,1,outer,inner)],v,a)
for n,(eq,pieces,v,a)in recs.items():
 ax=('y'if v==x else'x')+'='+str(a)
 task=('회전한 입체와 대표 와셔를 그리고 부피 적분을 세운 뒤 계산하라.','Sketch the solid and a representative washer, then set up and evaluate its volume integral.')if not 5<=n<=10 else('회전한 입체의 부피 적분만 세워라.','Set up, without evaluating, the volume integral.')
 st=(M(eq)+M(r'\text{axis: }'+ax)+task[0],M(eq)+M(r'\text{axis: }'+ax)+task[1])
 volume(b,n,384,st,pieces,v,a,setup=5<=n<=10,parts=list('abc')if n<=4 else[])
 b.save()
print('5.2 first forty',len(b.E))
import copy,xml.etree.ElementTree as ET
more={
41:(r'y=\tan x,\ y=0,\ x=\pi/4', [([(0,P/4,s.tan(x),0)],x,0), ([(0,P/4,1+s.tan(x),1)],x,-1)]),
42:(r'y=\cos^2x,\ y=0,\ -\pi/2\le x\le\pi/2',[([(-P/2,P/2,s.cos(x)**2,0)],x,0),([(-P/2,P/2,1,1-s.cos(x)**2)],x,1)]),
43:(r'x^2+4y^2=4',[([(-2,2,2+s.sqrt(1-x*x/4),2-s.sqrt(1-x*x/4))],x,2),([(-1,1,2+2*s.sqrt(1-y*y),2-2*s.sqrt(1-y*y))],y,2)]),
44:(r'y=x^2,\ x^2+y^2=1,\ y\ge0',[([(-s.sqrt((s.sqrt(5)-1)/2),s.sqrt((s.sqrt(5)-1)/2),s.sqrt(1-x*x),x*x)],x,0), ([(0,(s.sqrt(5)-1)/2,s.sqrt(y),0),((s.sqrt(5)-1)/2,1,s.sqrt(1-y*y),0)],y,0)])}
for n,(eq,cases)in more.items():
 es=[];svgs=[]
 for letter,(ps,v,a)in zip('ab',cases):
  ax=('y'if v==x else'x')+'='+str(a);st=(M(eq)+f'({letter}) '+M(ax)+'에 관해 회전한 부피를 적분으로 세우고 소수 다섯 자리로 구하라.',M(eq)+f'({letter}) Rotate about '+M(ax)+'; set up and evaluate the volume to five decimal places.')
  value=volume(b,n,384 if n<=43 else 385,st,ps,v,a)
  b.E[n]['answer']=pair(M(r'V\approx'+f'{float(value):.5f}'));es.append(copy.deepcopy(b.E[n]));svgs.append(ET.fromstring((ROOT/'assets'/f's5-2-{n}.svg').read_text()))
 e=es[0];e['subparts']=['a','b'];e['statement']={lang:' '.join(t['statement'][lang]for t in es)for lang in['ko','en']};e['steps']={lang:sum(([f'({let})']+t['steps'][lang]for let,t in zip('ab',es)),[])for lang in['ko','en']};e['answer']={lang:' '.join(f'({let}) '+t['answer'][lang]for let,t in zip('ab',es))for lang in['ko','en']};b.E[n]=e
 w=max(float(t.attrib['width'])for t in svgs);H=sum(float(t.attrib['height'])for t in svgs);out=ET.Element('svg',{'xmlns':'http://www.w3.org/2000/svg','viewBox':f'0 0 {w} {H}','width':str(w),'height':str(H)});offset=0
 for svg in svgs:
  grp=ET.SubElement(out,'g',{'transform':f'translate(0,{offset})'});grp.extend(list(svg));offset+=float(svg.attrib['height'])
 (ROOT/'assets'/f's5-2-{n}.svg').write_text(ET.tostring(out,encoding='unicode'));b.save()
for n,eq,f,g,seeds in[
(45,r'y=1+x^4,\ y=\sqrt{3-x^3}',s.sqrt(3-x**3),1+x**4,[-1.2,.8]),
(46,r'y=\sqrt[3]{2x-x^2},\ y=x^2/(x^2+1)',(2*x-x*x)**R(1,3),x*x/(x*x+1),[0,1.8])]:
 h=s.lambdify(x,f-g,'mpmath');roots=[mp.mpf(0)if q==0 else mp.findroot(h,q)for q in seeds];lo,hi=[s.Float(str(mp.re(z)),33)for z in roots]
 volume(b,n,385,(M(eq)+'의 유계영역을 x축에 관해 회전한다. 교점을 수치로 찾고 부피를 근사하라.',M(eq)+'Find numerical intersections and approximate the volume when the bounded region revolves about the x-axis.'),[(lo,hi,f,g)],x,numeric=True,extra=fs(r'x_1\approx'+f'{float(lo):.9f}'+r',\quad x_2\approx'+f'{float(hi):.9f}'))
 b.E[n]['answer']=pair(M(r'V\approx'+f'{float(mp.quad(s.lambdify(x,P*(f*f-g*g),"mpmath"),[float(lo),float(hi)])):.7f}'));b.save()
volume(b,47,385,(M(r'y=\sin^2x,\ y=0,\ 0\le x\le\pi')+'를 y=-1에 관해 회전한 정확한 부피를 구하라.',M(r'y=\sin^2x,\ y=0,\ 0\le x\le\pi')+'Find the exact volume on revolving about y=-1.'),[(0,P,1+s.sin(x)**2,1)],x,-1)
volume(b,48,385,(M(r'y=x^2-2x,\ y=x\cos(\pi x/4)')+'의 유계영역을 y=2에 관해 회전한 정확한 부피를 구하라.',M(r'y=x^2-2x,\ y=x\cos(\pi x/4)')+'Find the exact volume of the bounded region revolved about y=2.'),[(0,2,2-x*x+2*x,2-x*s.cos(P*x/4))],x,2,extra=fs(r'x(x-2-\cos(\pi x/4))=0\Rightarrow x=0,2'))
b.save();print('5.2 first 48',len(b.E))
def add(n,st,steps,ans,check,parts=[]):
 b.add(n,385 if n<=61 else 386 if n<=75 else 387,('단면적과 부피','Cross-sectional area and volume'),st,steps,ans,parts=parts);b.verify(n,*check)
for n,I,desc,rad in[
(49,r'\pi\int_0^{\pi/2}\sin^2x\,dx',('y=sin x 아래,0≤x≤π/2를 x축에 관해 회전한다.','Revolve the region under y=sin x on0≤x≤π/2 about the x-axis.'),r'R=\sin x,\ r=0'),
(50,r'\pi\int_0^\pi\sin x\,dx',('y=√(sin x) 아래,0≤x≤π를 x축에 관해 회전한다.','Revolve the region under y=√(sin x) on0≤x≤π about the x-axis.'),r'R=\sqrt{\sin x},\ r=0'),
(51,r'\pi\int_0^1(x^4-x^6)\,dx',('y=x²와 y=x³ 사이,0≤x≤1을 x축에 관해 회전한다.','Revolve the region between y=x² and y=x³ on0≤x≤1 about the x-axis.'),r'R=x^2,\ r=x^3'),
(52,r'\pi\int_{-1}^1(1-y^2)^2\,dy',('x=0과 x=1-y² 사이를 y축에 관해 회전한다.','Revolve the region between x=0 and x=1-y² about the y-axis.'),r'R=1-y^2,\ r=0'),
(53,r'\pi\int_0^4y\,dy',('x=0과 x=√y 사이,0≤y≤4를 y축에 관해 회전한다.','Revolve0≤x≤√y,0≤y≤4 about the y-axis.'),r'R=\sqrt y,\ r=0'),
(54,r'\pi\int_1^4[3^2-(3-\sqrt x)^2]\,dx',('y=0과 y=√x 사이,1≤x≤4를 y=3에 관해 회전한다.','Revolve0≤y≤√x,1≤x≤4 about y=3.'),r'R=3,\ r=3-\sqrt x')]:
 add(n,(M(I)+'로 표현되는 회전체를 하나 설명하라.',M(I)+'Describe one solid of revolution represented by this integral.'),[desc]+fs(rad,r'A=\pi(R^2-r^2)'),desc,('제시한 반지름을 와셔 공식에 대입하면 주어진 적분의 피적분함수를 얻는다.','Substitution of these radii into the washer formula reproduces the supplied integrand.'))
add(55,('길이15 cm인 간의1.5 cm 간격 단면적은0,18,58,79,94,106,117,128,63,39,0 cm²이다. 중점법으로 부피를 추정하라.','A15-cm liver has cross-sectional areas0,18,58,79,94,106,117,128,63,39,0 cm² at1.5-cm spacing. Estimate volume by midpoints.'),[('너비3 cm의 다섯 구간을 선택하면 홀수 번째 측정 위치가 중점이다.','Five intervals of width3 cm use the odd-index measurements as midpoints.')]+fs(r'V\approx3(18+79+106+128+39)=1110\ \mathrm{cm^3}'),same(M(r'V\approx1110\ \mathrm{cm^3}')),('중점 단면적 합370 cm²와 두께3 cm를 따로 확인했다.','Checked the area sum370 cm² and width3 cm separately.'))
add(56,('길이10 m 통나무의 x=0,1,…,10 m 단면적은0.68,0.65,0.64,0.61,0.58,0.59,0.53,0.55,0.52,0.50,0.48 m²이다. n=5 중점법을 적용하라.','A10-m log has areas0.68,0.65,0.64,0.61,0.58,0.59,0.53,0.55,0.52,0.50,0.48 m² at x=0,1,…,10 m. Apply the Midpoint Rule with n=5.'),fs(r'\Delta x=2,\quad x_i^*=1,3,5,7,9',r'V\approx2(.65+.61+.59+.55+.50)=5.8\ \mathrm{m^3}'),same(M(r'V\approx5.8\ \mathrm{m^3}')),('총길이5·2=10이고 중점 면적 합은2.90이다.','Five widths total10 m; midpoint areas sum to2.90 m².'))
# Graphic estimates are given with their readings, so the approximation is reproducible.
xa=[2.18,3.0,5.5,6.5];xb=[9.95,9.7,9.3,8.65];va=2*math.pi*sum(q*q for q in[1.5,2.2,3.8,3.1]);vb=math.pi*sum(v*v-u*u for u,v in zip(xa,xb))
add(57,('원본의2≤x≤10,0≤y≤4 영역을 (a)x축,(b)y축에 관해 회전한 부피를 n=4 중점법으로 추정하라. 수직 중점 x=3,5,7,9의 높이는 약1.5,2.2,3.8,3.1이다. 수평 중점 y=.5,1.5,2.5,3.5에서 좌우 경계는 약(2.18,9.95),(3.0,9.7),(5.5,9.3),(6.5,8.65)이다.','Estimate the volume of the source region,2≤x≤10 and0≤y≤4, rotated about(a)the x-axis and(b)the y-axis, using n=4 midpoints. At x=3,5,7,9, heights are approximately1.5,2.2,3.8,3.1. At y=.5,1.5,2.5,3.5, left/right boundaries are approximately(2.18,9.95),(3.0,9.7),(5.5,9.3),(6.5,8.65).'),fs(r'(a)\ \Delta x=2,\quad V_x\approx2\pi(1.5^2+2.2^2+3.8^2+3.1^2)',r'(b)\ \Delta y=1,\quad V_y\approx\pi\sum_{i=1}^4(R_i^2-r_i^2)')+[('두 와셔 반지름을 모두 y축에서 경계까지의 거리로 측정한다.','Both washer radii are distances from the y-axis.')],same(M(r'V_x\approx'+f'{va:.1f}'+r',\quad V_y\approx'+f'{vb:.1f}')+' (graph estimates)'),('단면적을 먼저 제곱·차감하고 그 후 구간 폭을 곱했다. 원본 판독에 따른 근사 오차가 있다.','Squared and subtracted radii before multiplying by interval width. Values have graphical reading error.'),['a','b'])
# Egg: symbolic polynomial integration plus numerical species parameters.
a,c,bb,dd=s.symbols('a c b d',real=True);egg=(a*x**3+bb*x*x+c*x+dd)**2*(1-x*x);eggV=s.factor(s.integrate(P*egg,(x,-1,1)));numV=s.simplify(eggV.subs({a:-R(6,100),bb:R(4,100),c:R(1,10),dd:R(54,100)}));assert abs(float(numV)-float(mp.quad(s.lambdify(x,P*egg.subs({a:-R(6,100),bb:R(4,100),c:R(1,10),dd:R(54,100)}),'mpmath'),[-1,1])))<1e-12
f=(-R(6,100)*x**3+R(4,100)*x*x+R(1,10)*x+R(54,100))*s.sqrt(1-x*x)
volume(b,58,385,(M(r'f(x)=(ax^3+bx^2+cx+d)\sqrt{1-x^2}')+'의 -1≤x≤1 아래를 x축에 관해 회전한다. (a)일반 부피,(b)a=-.06,b=.04,c=.1,d=.54인 새알의 그래프와 부피를 구하라.',M(r'f(x)=(ax^3+bx^2+cx+d)\sqrt{1-x^2}')+'Revolve the region under f on-1≤x≤1 about the x-axis. Find(a)the general volume and(b)the graph and volume for a=-.06,b=.04,c=.1,d=.54.'),[(-1,1,f,0)],x,parts=['a','b'],extra=fs(r'(a)\quad V=\pi\int_{-1}^1(ax^3+bx^2+cx+d)^2(1-x^2)\,dx='+tex(eggV)))
b.E[58]['answer']=pair(M(r'(a)\ V='+tex(eggV))+M(r'(b)\ V='+tex(numV)+r'\approx'+f'{float(numV):.6f}'));b.save()
# Exact cross-section problems, with symbolic parameter checks.
r,h,Rr,aa,bb=s.symbols('r h R a b',positive=True)
sections={
59:(('밑면 반지름r, 높이h인 직각 원뿔의 부피를 구하라.','Find the volume of a right cone of base radius r and height h.'),x,0,h,P*r*r*(1-x/h)**2,('꼭짓점 쪽으로 갈수록 반지름이 선형으로 줄어든다.','The radius decreases linearly toward the vertex.')),
60:(('높이h, 아래·위 반지름R,r인 원뿔대의 부피를 구하라.','Find the volume of a conical frustum of height h and lower/upper radii R,r.'),x,0,h,P*(Rr+(r-Rr)*x/h)**2,('높이x에서 반지름은 R+(r-R)x/h이다.','At height x the radius is R+(r-R)x/h.')),
61:(('반지름r인 구에서 높이h인 구모자의 부피를 구하라(0≤h≤2r).','Find the volume of a spherical cap of height h cut from a sphere of radius r(0≤h≤2r).'),x,r-h,r,P*(r*r-x*x),('구 중심을 원점으로 놓으면 단면 반지름 제곱은 r²-x²이다.','With origin at the sphere center, squared section radius is r²-x².')),
62:(('높이h, 아래·위 정사각형 변b,a인 각뿔대의 부피를 구하라. a=b와 a=0도 해석하라.','Find the volume of a square-pyramid frustum of height h and bottom/top sides b,a. Interpret a=b and a=0.'),x,0,h,(bb+(aa-bb)*x/h)**2,('닮음으로 단면 변은 b+(a-b)x/h이다.','Similarity gives section side b+(a-b)x/h.')),
63:(('높이h, 밑면 변b,2b인 직사각뿔의 부피를 구하라.','Find the volume of a pyramid of height h and rectangular base b by2b.'),x,0,h,2*bb**2*(1-x/h)**2,('단면 두 변이 모두 같은 닮음비로 줄어든다.','Both section sides shrink by the same similarity ratio.')),
64:(('높이h, 밑면 변a인 정삼각형을 가진 사면체의 부피를 구하라.','Find the volume of a tetrahedron of height h with equilateral base of side a.'),x,0,h,s.sqrt(3)*aa**2/4*(1-x/h)**2,('밑면 넓이는 √3 a²/4이고 닮은 단면의 면적비는 길이비의 제곱이다.','Base area is √3 a²/4; similar section areas scale with the square of the length ratio.')),
65:(('한 꼭짓점에서 만나는 세 모서리가 서로 수직이고 길이가3,4,5 cm인 사면체의 부피를 구하라.','Find the volume of a tetrahedron with three mutually perpendicular edges of lengths3,4,5 cm at one vertex.'),x,0,5,6*(1-x/5)**2,('3·4/2=6 cm²인 직각삼각형을 밑면으로 하고 높이를5로 둔다.','Choose the right triangle of area3·4/2=6 cm² as base and height5 cm.')),
66:(('반지름r인 원판을 밑면으로 하고, 평행한 수직 단면이 정사각형인 입체의 부피를 구하라.','A solid has circular base of radius r and parallel square cross-sections perpendicular to the base. Find its volume.'),x,-r,r,4*(r*r-x*x),('원판의 현 길이2√(r²-x²)가 정사각형의 한 변이다.','The disk chord2√(r²-x²) is the square side.')),
67:(('밑면은9x²+4y²≤36이며 x축에 수직인 단면이 밑면의 현을 빗변으로 하는 직각이등변삼각형이다. 부피를 구하라.','The base is9x²+4y²≤36. Perpendicular-to-x cross-sections are isosceles right triangles with hypotenuse in the base. Find volume.'),x,-2,2,9*(1-x*x/4),('빗변은6√(1-x²/4), 삼각형 넓이는 빗변 제곱의1/4이다.','The hypotenuse is6√(1-x²/4); triangle area is one quarter its square.')),
68:(('밑면 꼭짓점은(0,0),(1,0),(0,1)이고 y축에 수직인 단면은 정삼각형이다. 부피를 구하라.','The base triangle has vertices(0,0),(1,0),(0,1); sections perpendicular to y are equilateral triangles. Find volume.'),y,0,1,s.sqrt(3)/4*(1-y)**2,('높이y에서 밑면의 현은1-y이다.','At height y the base chord is1-y.')),
69:(('밑면 꼭짓점은(0,0),(1,0),(0,1)이고 x축에 수직인 단면은 정사각형이다. 부피를 구하라.','The base triangle has vertices(0,0),(1,0),(0,1); sections perpendicular to x are squares. Find volume.'),x,0,1,(1-x)**2,('x에서 현 길이는1-x이다.','At x the chord length is1-x.')),
70:(('밑면은 y=1-x²와 x축 사이이며 y축에 수직인 단면이 정사각형이다. 부피를 구하라.','The base lies between y=1-x² and the x-axis; sections perpendicular to y are squares. Find volume.'),y,0,1,4*(1-y),('수평 현의 전체 길이는2√(1-y)이다.','The full horizontal chord length is2√(1-y).')),
71:(('밑면은 y=1-x²와 x축 사이이다. x축에 수직인 단면은 높이가 밑변과 같은 이등변삼각형이다. 부피를 구하라.','The base lies between y=1-x² and the x-axis. Sections perpendicular to x are isosceles triangles whose height equals their base. Find volume.'),x,-1,1,(1-x*x)**2/2,('밑변과 높이가 모두1-x²이므로 면적은(1-x²)²/2이다.','Both base and height equal1-x², giving area(1-x²)²/2.')),
72:(('밑면은 y=2-x²와 x축 사이이다. y축에 수직인 단면은 밑면의 현을 반지름으로 하는 사분원이다. 부피를 구하라.','The base lies between y=2-x² and the x-axis. Sections perpendicular to y are quarter-circles with the base chord as radius. Find volume.'),y,0,2,P*(2-y),('반지름은2√(2-y), 면적은 π·[2√(2-y)]²/4이다.','Radius is2√(2-y), and area is π·[2√(2-y)]²/4.')),
73:(('x축에 수직인 원들이 x축을 지나고 중심은 y=(1-x²)/2,-1≤x≤1에 놓인다. 이 입체의 부피를 구하라.','Circles perpendicular to the x-axis pass through that axis and have centers on y=(1-x²)/2,-1≤x≤1. Find the solid’s volume.'),x,-1,1,P*(1-x*x)**2/4,('중심에서 x축까지 거리(1-x²)/2가 원의 반지름이다.','The center-to-axis distance(1-x²)/2 is the circle radius.')),
74:(('0≤x≤4에서 x축에 수직인 원의 지름 양끝이 y=√x/2와 y=√x 위에 놓인다. 부피를 구하라.','For0≤x≤4, circular sections perpendicular to x have diameter endpoints on y=√x/2 and y=√x. Find volume.'),x,0,4,P*x/16,('지름은√x/2이고 반지름은√x/4이다.','The diameter is√x/2, so the radius is√x/4.')),
76:(('반지름r인 원판이 밑면이고 평행한 수직 단면이 높이h, 밑변이 원판의 현인 이등변삼각형이다. (a)부피 적분,(b)원의 넓이 해석으로 부피를 구하라.','A solid has circular base radius r and parallel isosceles-triangle sections of height h with chord bases. Find(a)a volume integral and(b)its value using a circle area.'),x,-r,r,h*s.sqrt(r*r-x*x),('단면적은 h·2√(r²-x²)/2이다. 적분은 반원의 넓이에h를 곱한 값이다.','Section area is h·2√(r²-x²)/2. The integral is h times a semicircle area.')),
77:(('반지름4 원기둥을 지름을 따라 만나며30°를 이루는 두 평면으로 잘라 쐐기를 만든다. 두 평면의 교선과 평행한 단면으로 부피를 구하라.','A wedge in a radius4 cylinder is cut by two planes meeting at30° along a diameter. Use cross-sections parallel to the planes’ intersection to find volume.'),y,0,4,2*y*s.sqrt(16-y*y)/s.sqrt(3),('교선에서 거리y인 단면은 너비2√(16-y²), 높이 y tan30°인 직사각형이다.','At distance y from the intersection line, the section is a rectangle of width2√(16-y²) and height y tan30°.')),
80:(('서로 수직으로 만나는 축을 가진 반지름r인 두 원기둥의 공통 부피를 구하라.','Find the intersection volume of two radius-r cylinders with perpendicular intersecting axes.'),x,-r,r,4*(r*r-x*x),('양쪽 원기둥 조건을 함께 적용하면 단면은 변2√(r²-x²)의 정사각형이다.','The two cylinder constraints give a square section of side2√(r²-x²).'))}
for n,(st,v,lo,hi,A,why)in sections.items():
 A=s.sympify(A);lo=s.sympify(lo);hi=s.sympify(hi);V=s.simplify(s.integrate(A,(v,lo,hi)));assert not V.has(s.Integral),(n,V)
 sub={r:3,h:2,Rr:5,aa:2,bb:4};aaN=A.subs(sub);aN=lo.subs(sub);bN=hi.subs(sub);q=mp.quad(s.lambdify(v,aaN,'mpmath'),[float(aN),float(bN)]);assert abs(float(V.subs(sub))-float(q))<1e-8,(n,V,q)
 steps=[why]+fs(r'A('+str(v)+')='+tex(A),r'V='+s.latex(s.Integral(A,(v,lo,hi)))+'='+tex(V));ans=same(M('V='+tex(V)))
 if n==62:steps+=[('a=b이면 부피b²h인 각기둥, a=0이면 부피b²h/3인 각뿔이 된다.','For a=b this is a prism of volume b²h; for a=0 it is a pyramid of volume b²h/3.')];ans=(ans[0]+'; a=b: b²h, a=0: b²h/3.',ans[1]+'; a=b: b²h, a=0: b²h/3.')
 add(n,st,steps,ans,('단면적의 기하학적 계수를 확인하고 양의 매개변수 예에서 정확 적분값과 수치구적을 대조했다.','Checked the geometric area factor and compared the exact integral against numerical quadrature for positive sample parameters.'),['a','b']if n==76 else[])
 b.save()
print('5.2 sections/application subtotal',len(b.E))
add(75,('중심 원의 반지름R, 관의 반지름r(R>r)인 토러스에 대해 (a)와셔 부피 적분,(b)원의 넓이를 이용한 값을 구하라.','For a torus with central-circle radius R and tube radius r(R>r), find(a)a washer integral and(b)its value using a circle area.'),fs(r'R_{out}(y)=R+\sqrt{r^2-y^2},\quad R_{in}(y)=R-\sqrt{r^2-y^2}',r'V=\pi\int_{-r}^{r}[(R+\sqrt{r^2-y^2})^2-(R-\sqrt{r^2-y^2})^2]dy',r'V=4\pi R\int_{-r}^{r}\sqrt{r^2-y^2}\,dy=4\pi R\frac{\pi r^2}{2}=2\pi^2Rr^2'),same(M(r'V=2\pi^2Rr^2')),('남은 적분이 반지름r인 반원의 넓이임을 확인했고 차원은 길이의 세제곱이다.','The remaining integral is a radius-r semicircle area, and dimensions are length cubed.'),['a','b'])
add(78,('Cavalieri 원리를 (a)단면적 적분으로 증명하고 (b)밑면 반지름r, 수직 높이h인 비스듬한 원기둥의 부피에 적용하라.','(a)Prove Cavalieri’s principle using cross-sectional integrals. (b)Apply it to an oblique cylinder with base radius r and perpendicular height h.'),fs(r'A_1(t)=A_2(t)\ (a\le t\le b)\Rightarrow V_1=\int_a^bA_1(t)dt=\int_a^bA_2(t)dt=V_2')+[('밑면에 평행한 단면은 위치가 옮겨져도 반지름r인 원판이므로 모두 넓이가 πr²이다.','Every section parallel to the base is a translated radius-r disk, so all have area πr².')]+fs(r'V=\int_0^h\pi r^2\,dt=\pi r^2h'),same(M(r'(a)\ V_1=V_2;\qquad(b)\ V=\pi r^2h')),('h는 옆 모서리 길이가 아니라 평행 밑면 사이의 수직 거리로 사용했다.','Used perpendicular distance between base planes for h, rather than a slanted side length.'),['a','b'])
add(79,('반지름r인 반구와, 같은 반지름·높이r인 원기둥에서 꼭짓점이 아래인 원뿔을 뺀 입체가 같은 부피임을 Cavalieri 원리로 보여라.','Use Cavalieri’s principle to equate a radius-r hemisphere with a cylinder of radius/height r minus a cone with vertex at the bottom.'),fs(r'A_{hem}(y)=\pi(r^2-y^2),\quad0\le y\le r',r'A_{cyl-cone}(y)=\pi r^2-\pi y^2=A_{hem}(y)',r'V=\pi r^3-\frac13\pi r^3=\frac23\pi r^3'),same(M(r'V=\frac23\pi r^3')),('같은 높이에서 두 단면적을 직접 비교했으며 반구 부피 공식을 가정하지 않았다.','Compared cross-sectional areas at equal heights without assuming the hemisphere volume formula.'))
add(81,('반지름r인 두 구의 중심 사이 거리가r일 때 공통 부피를 구하라.','Two radius-r spheres have centers distance r apart. Find their intersection volume.'),[('공통영역은 높이r/2인 동일한 구모자 두 개이다. 중심을 잇는 축에서 수직이등분면으로 나눈다.','The intersection consists of two congruent spherical caps of height r/2, split by the perpendicular bisector plane.')]+fs(r'V=2\pi\int_{r/2}^{r}(r^2-x^2)dx=\frac{5\pi r^3}{12}'),same(M(r'V=5\pi r^3/12')),('구모자 공식2π(r/2)²(r-r/6)으로 독립 대조했다.','Independently checked with the two-cap formula2π(r/2)²(r-r/6).'))
add(82,('지름30 cm인 반구형 그릇 바닥에 지름10 cm의 무거운 구가 놓여 있다. 바닥에서 수면까지 깊이가h cm(0≤h≤15)일 때 물의 부피를 구하라.','A heavy diameter10-cm ball rests at the bottom of a hemispherical bowl of diameter30 cm. Find water volume at depth h cm above the bottom(0≤h≤15).'),[('그릇에 찬 구모자의 부피에서 잠긴 공의 부피를 뺀다. 공의 중심 높이는5 cm이고 꼭대기는10 cm이다.','Subtract submerged ball volume from the bowl’s spherical cap. The ball center is5 cm high and its top is10 cm high.')]+fs(r'V_{bowl}(h)=\pi h^2(15-h/3)',r'0\le h\le10:\quad V_{ball}(h)=\pi h^2(5-h/3)',r'10\le h\le15:\quad V_{ball}=\frac43\pi5^3=500\pi/3'),same(M(r'V(h)=\begin{cases}10\pi h^2,&0\le h\le10,\\\pi h^2(15-h/3)-500\pi/3,&10\le h\le15.\end{cases}\ \mathrm{cm^3}')),('h=10에서 양쪽 식이1000π로 이어지고, h=0에서0이며 증가율은 물이 차는 수평 단면적이다.','Both formulas give1000π at h=10, vanish at h=0, and their derivatives equal the available horizontal water area.'))
add(83,('반지름R인 원기둥의 중심을 지나며 원래 축에 수직인 반지름r<R의 원기둥 구멍을 뚫는다. 제거된 부피 적분만 세워라.','A radius-r bore with r<R passes through the center of a radius-R cylinder perpendicular to its axis. Set up an integral for the removed volume.'),[('두 축 모두에 수직인 좌표를x로 잡으면 공통 단면은 변2√(R²-x²),2√(r²-x²)인 직사각형이다.','Choose x perpendicular to both axes. The shared section is a rectangle with sides2√(R²-x²) and2√(r²-x²).')]+fs(r'-r\le x\le r,\quad A(x)=4\sqrt{R^2-x^2}\sqrt{r^2-x^2}'),same(M(r'V=4\int_{-r}^{r}\sqrt{R^2-x^2}\sqrt{r^2-x^2}\,dx')),('r=R이면 같은 반지름 교차 원기둥의 정사각형 단면으로 줄어드는지 확인했다.','For r=R the section reduces to the square section of equal-radius intersecting cylinders.'))
add(84,('반지름R인 구의 중심을 관통하는 반지름r<R 원기둥 구멍을 뚫었다. 남은 입체의 부피를 구하라.','A cylindrical hole of radius r<R is bored through the center of a sphere of radius R. Find remaining volume.'),fs(r'a=\sqrt{R^2-r^2},\quad-a\le x\le a',r'A(x)=\pi[(R^2-x^2)-r^2]=\pi(a^2-x^2)',r'V=\pi\int_{-a}^{a}(a^2-x^2)dx=\frac43\pi a^3'),same(M(r'V=\frac43\pi(R^2-r^2)^{3/2}')),('r=0이면 구 전체 부피가 되고 r→R이면0이다. 남은 높이H=2a만으로 쓰면 πH³/6이다.','At r=0 this is the full sphere, and it tends to0 as r→R. In terms of remaining height H=2a, it is πH³/6.'))
add(85,('술통은 y=R-cx²,-h/2≤x≤h/2를 x축에 관해 회전해 만든다(c>0). (a)d=ch²/4일 때 양끝 반지름r=R-d임을 보이고,(b)V=πh(2R²+r²-2d²/5)/3을 증명하라.','A barrel is generated by revolving y=R-cx²,-h/2≤x≤h/2 about x(c>0). (a)With d=ch²/4 show end radius r=R-d. (b)Prove V=πh(2R²+r²-2d²/5)/3.'),fs(r'(a)\ y(\pm h/2)=R-ch^2/4=R-d',r'(b)\ V=\pi\int_{-h/2}^{h/2}(R-cx^2)^2dx=\pi(R^2h-Rch^3/6+c^2h^5/80)',r'c=4d/h^2\Rightarrow V=\pi h(R^2-2Rd/3+d^2/5)',r'r=R-d\Rightarrow 2R^2+r^2-2d^2/5=3R^2-2Rd+3d^2/5'),same(M(r'r=R-d,\qquad V=\frac{\pi h}{3}(2R^2+r^2-\frac25d^2)')),('d=0이면 원기둥 πR²h로 줄며 두 최종 다항식이 전개 후 일치한다.','At d=0 the volume reduces to πR²h, and expansion confirms equality of the two final polynomials.'),['a','b'])
add(86,('x축 위쪽의 영역은 넓이A이다. x축에 관해 회전한 부피가V1일 때 y=-k(k>0)에 관해 회전한 부피V2를 V1,k,A로 나타내라.','A region above the x-axis has area A. Its volume on rotation about x is V1. Express its volume V2 on rotation about y=-k(k>0) in terms of V1,k,A.'),fs(r'\pi[(f+k)^2-(g+k)^2]=\pi(f^2-g^2)+2\pi k(f-g)',r'V_2=V_1+2\pi k\int(f-g)dx=V_1+2\pi kA')+[('수직 단면이 여러 구간이면 각 구간에 같은 항등식을 적용해 합한다.','If a vertical section has multiple intervals, apply the identity to each and sum.')],same(M(r'V_2=V_1+2\pi kA')),('추가 항은 양수이고 부피 차원의 kA에2π를 곱한 값이다.','The additional term is positive and2π times the volume-dimensional product kA.'))
cc=(s.Integer(25000)/(93*P))**R(1,3)
add(87,('영역R1은0≤x≤y^(1/3),1≤y≤8(cm)이다. (a)y축 회전 부피V1,(b)(x,y)→(cx,cy)로 변환된 R2의 경계,(c)V2=c³V1 증명,(d)부피5000 cm³가 되는 양의c를 구하라.','R1 is0≤x≤y^(1/3),1≤y≤8(cm). Find(a)its y-axis rotation volume V1,(b)the boundary of R2 after(x,y)→(cx,cy),(c)a proof that V2=c³V1,(d)positive c giving5000 cm³.'),fs(r'(a)\ V_1=\pi\int_1^8y^{2/3}dy=93\pi/5',r'(b)\ X=cx,\ Y=cy:\quad Y=X^3/c^2,\quad Y=c,8c,\quad X=0',r'(c)\ V_2=\pi\int_c^{8c}(c^2Y)^{2/3}dY=\pi c^3\int_1^8y^{2/3}dy=c^3V_1',r'(d)\ c^3\frac{93\pi}{5}=5000\Rightarrow c=\left(\frac{25000}{93\pi}\right)^{1/3}'),same(M(r'V_1=93\pi/5;\quad V_2=c^3V_1;\quad c='+tex(cc)+r'\approx'+f'{float(cc):.6f}')),('선형 크기를c배 하면 단면적c²배, 두께c배이므로 부피가c³배가 되는지 독립 확인했다.','Independently checked that scaling lengths by c scales section area by c² and thickness by c, hence volume by c³.'),list('abcd'))
b.plot(75,[(lambda u,v:((3+math.cos(v))*math.cos(u),(3+math.cos(v))*math.sin(u),math.sin(v)),(0,2*math.pi),(0,2*math.pi),'Torus: R=3, r=1 (illustrative parameters)')])
b.plot(84,[(lambda x,t:(x,math.sqrt(4-x*x)*math.cos(t),math.sqrt(4-x*x)*math.sin(t)),(-math.sqrt(3),math.sqrt(3)),(0,2*math.pi),'Outer sphere: R=2, bore radius=1'),(lambda x,t:(x,math.cos(t),math.sin(t)),(-math.sqrt(3),math.sqrt(3)),(0,2*math.pi),'Inner bore surface (same scale parameters)')])
assert sorted(b.E)==list(range(1,88));b.save();print('5.2 COMPLETE',len(b.E))
def linear(table,t):
 for (u,a),(v,c)in zip(table,table[1:]):
  if u<=t<=v:return a+(c-a)*(t-u)/(v-u)
 return table[-1][1]
profile=[(2,0),(3,1.5),(4,1.9),(5,2.2),(6,3),(7,3.8),(8,4),(9,3.1),(10,0)]
b.plot(57,[(lambda x,t:(x,linear(profile,x)*math.cos(t),linear(profile,x)*math.sin(t)),(2,10),(0,2*math.pi),'Approximate source profile revolved about x'),(lambda x,t:(x*math.cos(t),linear(profile,x),x*math.sin(t)),(2,10),(0,2*math.pi),'Approximate source profile revolved about y')],('원본 그래프 판독점의 선형 보간으로 직접 그린 근사 회전체이다. 부피값은 해설에 적은 네 중점 자료로 계산한다.','Original approximate solids from linear interpolation of source-graph readings. Volume estimates use the four midpoint readings stated in the solution.'))
b.E[57]['answer']['ko']=b.E[57]['answer']['ko'].replace('(graph estimates)','(그래프 추정값)')
b.E[65]['answer']=pair(M(r'V=10\ \mathrm{cm^3}'))
b.save()
