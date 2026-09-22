"""Original optimization plots and geometrical constraint diagrams."""
from calc1_core import panel,plot,samples
from pathlib import Path
import json,math
R=Path(__file__).resolve().parents[1]/'exercise-content';p=R/'s3-7.json';d=json.loads(p.read_text());E={e['number']:e for e in d['exercises']};count=0

def fig(n,panels,caption=None):
 global count
 name=f's3-7-{n}.svg';plot(name,panels);E[n]['figure']={'src':'../exercise-content/assets/'+name,'alt':{'ko':f'3.7 {n}번 자체 도해','en':f'Original diagram for Exercise3.7.{n}'},'caption':caption or {'ko':'조건과 목적함수에서 직접 만든 도해. 기하 도해의 치수는 표기된 값을 따르며 표시창 밖은 잘랐다.','en':'Original diagram from the constraints and objective.Geometric dimensions follow the indicated values; the display window clips unshown portions.'}};count+=1

def box(x,y):return[(0,0),(x,0),(x,y),(0,y),(0,0)]
def circle(r,c=(0,0)):return[(c[0]+r*math.cos(t*math.pi/300),c[1]+r*math.sin(t*math.pi/300))for t in range(601)]
def equal(title,curves,dots=(),xr=(-4,4),cy=0):
 h=(xr[1]-xr[0])*270/520;return panel(title,(xr[0],xr[1],cy-h/2,cy+h/2),curves,dots)
models={1:(lambda x:x*(23-x),0,23,11.5),2:(lambda x:x*(x+100),-110,10,-50),3:(lambda x:x+100/x,2,30,10),4:(lambda x:x*x+(16-x)**2,0,16,8),5:(lambda x:x+2-x*x,-1,2,.5),6:(lambda x:2*x*x-x+1,-1,1,.25),7:(lambda x:x*(50-x),0,50,25),8:(lambda x:2*x+2000/x,10,80,math.sqrt(1000)),9:(lambda x:x/(1+x*x),0,4,1),10:(lambda x:100*x/(x*x+x+4),0,8,2),11:(lambda x:375*x-2.5*x*x,0,150,75),12:(lambda x:x*(3-2*x)**2,0,1.5,.5),13:(lambda x:3*x+3000000/x,300,2500,1000),14:(lambda x:2*x*(1200-4*x),0,300,150),18:(lambda x:x*x+128000/x,15,100,40),19:(lambda x:(1200*x-x**3)/4,0,math.sqrt(1200),20),20:(lambda x:x*(4-2*x)*(3-3*x),0,1,1-1/math.sqrt(3)),21:(lambda x:20*x*x+180/x,.5,4,(4.5)**(1/3)),22:(lambda x:32*x*x+180/x,.5,4,(45/16)**(1/3)),23:(lambda x:x*x*(108-4*x),0,27,18),24:(lambda x:math.pi*x*x*(108-2*math.pi*x),0,54/math.pi,36/math.pi),36:(lambda x:2*x*(4-x*x),0,2,2/math.sqrt(3)),43:(lambda x:x*x/16+math.sqrt(3)*(10-x)**2/36,0,10,40*math.sqrt(3)/(9+4*math.sqrt(3))),44:(lambda x:x*x/16+(10-x)**2/(4*math.pi),0,10,40/(4+math.pi)),45:(lambda x:16*x-x*x,0,16,8),51:(lambda x:x/(x+1)**2,0,6,1),52:(lambda x:x**3/(x-1),1.05,4,1.5),53:(lambda x:-1.5/math.tan(x)+1.5*math.sqrt(3)/math.sin(x),.2,math.pi/2,math.acos(1/math.sqrt(3))),54:(lambda t:400*t*t+225*(t-1)**2,0,1,.36),55:(lambda x:math.sqrt(25+x*x)/6+(5-x)/8,0,5,5),56:(lambda t:2*math.cos(t)+t,0,math.pi/2,math.pi/2),57:(lambda x:.4*x+.8*math.sqrt((6-x)**2+4),0,6,6-2/math.sqrt(3)),59:(lambda x:1/x**2+3/(10-x)**2,1,9,10/(1+3**(1/3))),62:(lambda x:120*x*x-15*x**4,-3,3,2),65:(lambda x:16000/x+200+4*math.sqrt(x),60,1000,400),66:(lambda x:-16000+1200*x-5.4*x*x-.004*x**3,0,230,100),67:(lambda x:57000*x-3000*x*x,0,19,9.5),68:(lambda x:(x-6)*(40-2*x),6,20,13),70:(lambda x:(16+x)*(240-8*x),0,25,7),79:(lambda x:math.sqrt(x**3/(x-4)),4.1,8,6),81:(lambda x:math.atan(3*x)-math.atan(x),0,4,1/math.sqrt(3)),82:(lambda x:100*math.sin(x)*(1+math.cos(x)),0,math.pi/2,math.pi/3)}
for n,(f,lo,hi,c) in models.items():
 pts=samples(f,lo,hi,500);ys=[v for x,v in pts];gap=max(.02,(max(ys)-min(ys))*.1)
 title='Objective and optimizing point'
 if n==9:title='Yield divided by k'
 if n==51:title='Power: E=1 and internal resistance r=1'
 if n==52:title='Energy divided by a L u^2; horizontal variable v/u'
 if n==53:title='(S - 6 s h)/s^2 versus theta (radians)'
 if n==62:title='Tangent slope: both x=-2 and x=2 maximize'
 if n in[43,44]:title='Interior minimum; compare both endpoints for maximum'
 fig(n,[panel(title,(lo,hi,min(ys)-gap,max(ys)+gap),[pts],[(c,f(c))])])
# Add geometry above objective plots where geometry is essential.
def prepend(n,panels):
 old=E[n].get('figure');new=[]
 if n in models:
  f,lo,hi,c=models[n];pts=samples(f,lo,hi);ys=[v for x,v in pts];gap=max(.05,(max(ys)-min(ys))*.1);new=[panel('Objective versus the chosen variable',(lo,hi,min(ys)-gap,max(ys)+gap),[pts],[(c,f(c))])]
 # Replacing the same artifact does not add another figure.
 global count
 if old:count-=1
 fig(n,panels+new)
prepend(11,[equal('Four pens: five fences of length x; two of length y',[box(187.5,75)]+[[(187.5*k/4,0),(187.5*k/4,75)]for k in[1,2,3]],xr=(-10,205),cy=37.5)])
prepend(12,[equal('3 ft sheet: red corners are cut; blue center becomes base',[box(3,3),[(.5,0),(.5,3)],[(2.5,0),(2.5,3)],[(0,.5),(3,.5)],[(0,2.5),(3,2.5)]],xr=(-1.5,4.5),cy=1.5)])
prepend(14,[equal('River is the slanted upper boundary; fence lengths 3x,x,y',[[(0,0),(600,0),(600,150)],[(0,0),(0,450)],[(0,450),(600,150)]],xr=(-170,770),cy=225)])
prepend(20,[equal('4 by3 sheet: one double fold removes3x from the width',[box(4,3),[(.42,0),(.42,3)],[(3.58,0),(3.58,3)],[(0,.42),(4,.42)],[(0,2.16),(4,2.16)],[(0,2.58),(4,2.58)]],xr=(-1.5,5.5),cy=1.5)])
for n,curve,pt,target in[(25,samples(lambda x:2*x+3,-3,1),(-1.2,.6),(0,0)),(26,[(x,math.sqrt(x))for x in [j/100 for j in range(601)]],(2.5,math.sqrt(2.5)),(3,0)),(27,[(math.cos(t*math.pi/300),2*math.sin(t*math.pi/300))for t in range(601)],(-1/3,4*math.sqrt(2)/3),(1,0))]:
 fig(n,[equal('Curve and extremizing distance segment',[curve,[target,pt]],[target,pt],xr=(-4,5),cy=1)])
r28=2.65
import mpmath as mp
r28=float(mp.findroot(lambda t:t-4+(mp.sin(t)-2)*mp.cos(t),2.7))
fig(28,[equal('Nearest point on sine curve',[samples(math.sin,0,7),[(4,2),(r28,math.sin(r28))]],[(4,2),(r28,math.sin(r28))],xr=(-.5,7.5),cy=.7)])
for n in[29,30,33]:
 r=1;cur=[circle(r)];pts=[]
 if n==30:cur=[[(2*x,y)for x,y in circle(1)]];a=math.sqrt(2);bb=1/math.sqrt(2);cur.append([(-a,-bb),(a,-bb),(a,bb),(-a,bb),(-a,-bb)])
 elif n==29:a=1/math.sqrt(2);cur.append([(-a,-a),(a,-a),(a,a),(-a,a),(-a,-a)])
 else:cur.append([(0,1),(-math.sqrt(3)/2,-.5),(math.sqrt(3)/2,-.5),(0,1)])
 fig(n,[equal('Optimal inscribed shape (normalized dimensions)',cur,xr=(-2.7,2.7))])
fig(31,[equal('Triangle L=2: optimal rectangle has half base and half height',[[(0,0),(2,0),(1,math.sqrt(3)),(0,0)],[(.5,0),(1.5,0),(1.5,math.sqrt(3)/2),(.5,math.sqrt(3)/2),(.5,0)]],xr=(-1,3),cy=.8)])
fig(32,[equal('Trapezoid in unit semicircle',[circle(1),[(-1,0),(1,0),(.5,math.sqrt(3)/2),(-.5,math.sqrt(3)/2),(-1,0)]],xr=(-2.2,2.2))])
prepend(36,[equal('Optimal rectangle below y=4-x^2',[samples(lambda x:4-x*x,-2,2),[(-2/math.sqrt(3),0),(2/math.sqrt(3),0),(2/math.sqrt(3),8/3),(-2/math.sqrt(3),8/3),(-2/math.sqrt(3),0)]],xr=(-4.5,4.5),cy=2)])
fig(37,[equal('Axial section of sphere and volume-maximizing cylinder',[circle(1),[(-math.sqrt(2/3),-1/math.sqrt(3)),(math.sqrt(2/3),-1/math.sqrt(3)),(math.sqrt(2/3),1/math.sqrt(3)),(-math.sqrt(2/3),1/math.sqrt(3)),(-math.sqrt(2/3),-1/math.sqrt(3))]],xr=(-2.2,2.2))])
fig(38,[equal('Axial section: cylinder height h/3, radius2r/3',[[(-1,0),(1,0),(0,2),(-1,0)],[(-2/3,0),(2/3,0),(2/3,2/3),(-2/3,2/3),(-2/3,0)]],xr=(-2.4,2.4),cy=1)])
rr=30/(4+math.pi)
fig(40,[equal('Norman window: rectangle height equals semicircle radius',[[(0,0),(2*rr,0),(2*rr,rr)],[(0,0),(0,rr)],[(rr+rr*math.cos(t*math.pi/300),rr+rr*math.sin(t*math.pi/300))for t in range(301)]],xr=(-5,14),cy=rr)])
prepend(55,[equal('Width5, downstream5: direct rowing is fastest',[[(-1,0),(7,0)],[(-1,5),(7,5)],[(0,0),(5,5)]],[(0,0),(5,5)],xr=(-3,9),cy=2.5)])
prepend(56,[equal('Opposite endpoints: fastest route is semicircular walking',[circle(2),[(-2,0),(2,0)],[(2*math.cos(t*math.pi/200),2*math.sin(t*math.pi/200))for t in range(201)]],xr=(-4.4,4.4))])
for n in[57,58]:
 x=6-2/math.sqrt(3) if n==57 else float(mp.findroot(lambda x:x/mp.sqrt(x*x+1)-2*(6-x)/mp.sqrt((6-x)**2+4),4.9));start=(0,0 if n==57 else 1)
 pan=equal('Land then underwater: optimized crossing point',[[(-1,0),(7,0)],[(-1,-2),(7,-2)],[start,(x,0),(6,-2)]],[start,(x,0),(6,-2)],xr=(-1,7),cy=-.5)
 if n==57:prepend(n,[pan])
 else:fig(n,[pan])
fig(74,[equal('Maximum-area kite: top and bottom angles are90 degrees',[[(-1,0),(0,1),(1,0),(0,-1),(-1,0)],[(-1,0),(1,0)],[(0,-1),(0,1)]],xr=(-2.2,2.2))])
y=float(mp.findroot(lambda y:y/mp.sqrt(y*y+4)+y/mp.sqrt(y*y+9)-1,1.4));L=lambda x:x+math.sqrt((5-x)**2+4)+math.sqrt((5-x)**2+9);der=lambda x:1-(5-x)/math.sqrt((5-x)**2+4)-(5-x)/math.sqrt((5-x)**2+9)
fig(75,[equal('Cable junction: A=(0,5),B=(-2,0),C=(3,0)',[[(0,5),(0,y),(-2,0)],[(0,y),(3,0)],[(-2,0),(3,0)]],[(0,5),(0,y),(-2,0),(3,0)],xr=(-5,6),cy=2.5),panel('Cable length L(x), x=AP',(0,5,7,11),[samples(L,0,5)],[(5-y,L(5-y))]),panel('Derivative dL/dx: zero at the minimum',(0,5,-1.2,1.2),[samples(der,0,5)],[(5-y,0)])])
# Qualitative source-compatible hourly curve: tangent-from-origin explains the method.
f=lambda v:1+(v-30)**2/1600;c=50
fig(76,[panel('Schematic hourly consumption; tangent from origin',(0,85,0,3),[samples(f,0,80),[(0,0),(80,80*f(c)/c)]],[(c,f(c))],xlabel='speed (mph)',ylabel='relative hourly use')],{'ko':'원본 개형과 접선 원리를 설명하는 자체 모형이다. 정확한 차량 데이터가 아니며 약50mph는 원본 그래프에서 추정한다.','en':'Original qualitative model explaining the source shape and tangent method.It is not measured car data; about50mph is estimated from the source graph.'})
fig(77,[equal('Least-time refraction; angles measured from vertical normal',[[(-1,0),(6,0)],[(0,2),(2,0),(5,-1)],[(2,-1.5),(2,2)]],xr=(-1,7),cy=.2)])
fig(78,[equal('Rope and reflected straight path', [[(0,0),(0,2)],[(5,0),(5,3)],[(0,2),(2,0),(5,3)],[(0,-2),(5,3)],[(-1,0),(6,0)]],xr=(-3,9),cy=.5)])
prepend(79,[equal('Folded corner and shortest crease: x=6 inches',[box(12,8),[(12,2),(12-6*math.sqrt(2),8)],[(12,8),(12-4*math.sqrt(2),0)],[(12,2),(12-4*math.sqrt(2),0)]],xr=(-3,15),cy=4)])
fig(80,[equal('Right-angle corridor: narrowest orientation limits pipe length',[[(-12,0),(0,0),(0,18)],[(-12,9),(-6,9),(-6,18)],[(-11,0),(0,16.5)]],xr=(-24,16),cy=9)])
prepend(81,[equal('Observer one unit from track; runners at x and3x',[[(-1,0),(3,0)],[(0,-1),(1/math.sqrt(3),0)],[(0,-1),(math.sqrt(3),0)]],[(0,-1),(1/math.sqrt(3),0),(math.sqrt(3),0)],xr=(-1.5,3.5),cy=-.3)])
prepend(82,[equal('Optimal gutter: base10, side10, angle60 degrees',[[(-5,0),(5,0),(10,5*math.sqrt(3))],[(-5,0),(-10,5*math.sqrt(3))],[(-10,5*math.sqrt(3)),(10,5*math.sqrt(3))]],xr=(-13,13),cy=4.3)])
L0,W=3,1;pts=[((x-y)/math.sqrt(2),(x+y)/math.sqrt(2))for x,y in[(-L0/2,-W/2),(L0/2,-W/2),(L0/2,W/2),(-L0/2,W/2),(-L0/2,-W/2)]];z=(L0+W)/(2*math.sqrt(2))
fig(83,[equal('45-degree rotation makes the outer rectangle a square',[pts,[(-z,-z),(z,-z),(z,z),(-z,z),(-z,-z)]],xr=(-3,3))])
fig(84,[equal('Parent vessel then branch; angle with parent direction', [[(0,0),(4,0)],[(2,0),(3,2)],[(3,0),(3,2)]] ,xr=(-1,5),cy=1)])
xx=25/math.sqrt(24)
fig(85,[equal('Island to C on shore, then along shore to D',[[(-1,0),(14,0)],[(0,5),(xx,0),(13,0)],[(0,5),(0,0)]],[(0,5),(xx,0),(13,0)],xr=(-2,15),cy=2.5)])
pans=[]
for dist in[5,math.sqrt(50),10]:
 fn=lambda x:1/(x*x+dist*dist)+1/((10-x)**2+dist*dist);pts=samples(fn,0,10);ys=[v for x,v in pts];gap=(max(ys)-min(ys))*.15 or .001
 pans.append(panel(f'Illumination/k on bounded segment: d={dist:.5g}',(0,10,min(ys)-gap,max(ys)+gap),[pts],[(x,fn(x))for x in[0,5,10]]))
fig(86,pans)

# Explicit comparative constructions for parts(a),(b) of11 and12.
pens=[]
for a,c in[(50,250),(75,187.5),(100,125)]:
 pens.append(equal(f'Pen sides x={a}, y={c}; total area={a*c:g} ft^2',[box(c,a)]+[[(c*k/4,0),(c*k/4,a)]for k in[1,2,3]],xr=(-20,270),cy=55))
prepend(11,pens)
boxes=[]
for cut in[.25,.5,.75]:
 base=3-2*cut
 # Oblique elevation, horizontal base and vertical height share their actual scale.
 vertices=[(0,0),(base,0),(base+.45,.3),(.45,.3),(0,0)]
 curves=[vertices,[(0,0),(0,cut),(base,cut),(base,0)],[(base,cut),(base+.45,cut+.3),(base+.45,.3)],[(0,cut),(.45,cut+.3),(base+.45,cut+.3)]]
 boxes.append(panel(f'Cut x={cut}; square base y={base}; volume={cut*base*base:g}',(-.2,3.2,-.2,1.6),curves,xlabel='base direction',ylabel='height'))
prepend(12,boxes)
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print('3.7 SVG:',count)
