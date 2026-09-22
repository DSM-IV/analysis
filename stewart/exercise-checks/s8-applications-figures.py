"""Native SVG diagrams for source-checked sections8.3–8.5."""
from calc1_core import panel,plot,samples
from pathlib import Path
import json,math,importlib.util
R=Path(__file__).resolve().parents[1]/'exercise-content';docs={sec:json.loads((R/f's{sec}.json').read_text())for sec in['8-3','8-4','8-5']};E={sec:{e['number']:e for e in d['exercises']}for sec,d in docs.items()};counts={sec:0 for sec in docs}
def fig(sec,n,panels,cap=None):
 name=f's{sec}-{n}.svg';plot(name,panels);E[sec][n]['figure']={'src':'../exercise-content/assets/'+name,'alt':{'ko':f'{sec} {n}번 자체 도해','en':f'Original diagram for{sec}.{n}'},'caption':cap or{'ko':'문제의 조건과 계산에서 직접 만든 도해. 색선은 경계·비교선이며 점은 도심 또는 주요 해이다.','en':'Original diagram from the problem conditions and calculations.Colored curves are boundaries/comparison lines; points indicate centroids or key solutions.'}};counts[sec]+=1

def equal(title,curves,dots=(),xr=(-4,4),cy=0):
 h=(xr[1]-xr[0])*270/520;return panel(title,(xr[0],xr[1],cy-h/2,cy+h/2),curves,dots)
def circle(r,c=(0,0),t0=0,t1=2*math.pi):return[(c[0]+r*math.cos(t0+(t1-t0)*i/400),c[1]+r*math.sin(t0+(t1-t0)*i/400))for i in range(401)]
# Water at y=0; geometric y points upward, depth is -y.
plates={3:([(-1,-3),(1,-3),(1,-11),(-1,-11),(-1,-3)],(-10,10),-5),4:([(0,-2),(0,-7),(10,-7),(0,-2)],(-3,15),-3.5),5:(circle(8,(0,-12)),(-21,21),-10),6:(circle(6,(0,-4),0,math.pi)+[(-6,-4),(6,-4)],(-9,9),-1),7:([(0,0),(-2,-6),(2,-6),(0,0)],(-7,7),-3),8:([(-3,-3),(3,-3),(0,-7),(-3,-3)],(-9,9),-3),9:([(-2,1),(2,1),(4,-2),(-4,-2),(-2,1)],(-6,6),-.5),10:([(0,0),(1,-1),(0,-2),(-1,-1),(0,0)],(-3,3),-1),11:([(-2,0),(2,0),(1,-2),(-1,-2),(-2,0)],(-3.5,3.5),-1),12:(circle(2,(0,-10),0,math.pi)+[(-2,-10),(2,-10)],(-12,12),-5)}
for n,(curve,xr,cy)in plates.items():fig('8-3',n,[equal('Horizontal strips: pressure uses vertical depth',[curve,[(xr[0],0),(xr[1],0)]],xr=xr,cy=cy)])
fig('8-3',14,[equal('Illustration only: bottom width b is not given in source', [[(0,0),(2,0),(1,-3),(0,-3),(0,0)],[(-1,0),(3,0)]],xr=(-3,5),cy=-1.5)],{'ko':'아래 폭 b는 원본 그림에 수치가 없다. 그림은 b=1인 예시일 뿐이며 해설은 b를 변수로 유지한다.','en':'The source omits bottom width b.This drawing illustrates b=1 only; the solution retains b as a parameter.'})
fig('8-3',16,[equal('Dam side view: actual slope70, vertical depth70cos30', [[(0,0),(35,-70*math.cos(math.pi/6))],[(0,0),(0,-70)]],xr=(-55,100),cy=-30)])
fig('8-3',17,[equal('Long side of pool: length40; depths3 and9',[[(0,0),(40,0),(40,-9),(0,-3),(0,0)]],xr=(-3,43),cy=-4)])
fig('8-3',19,[panel('Measured widths at known depths',(6.8,9.6,0,5),[list(zip([7,7.4,7.8,8.2,8.6,9,9.4],[1.2,1.8,2.9,3.8,3.6,4.2,4.4]))],xlabel='depth (ft)',ylabel='width (ft)')])
# Read exact centroid results from report, not rounded plot coordinates.
rep=json.loads(Path(__file__).with_name('s8-3-report.json').read_text());import sympy as s
coords={r['exercise']:tuple(float(s.sympify(z))for z in r['centroid'])for r in rep['exactIntegrationRecords']if 'centroid'in r}
regions={25:(lambda x:4-2*x,lambda x:0,0,2),26:(math.exp,lambda x:0,-1,1),27:(lambda x:x*x/2,lambda x:0,0,2),28:(lambda x:1/x,lambda x:0,1,2),29:(math.sqrt,lambda x:x,0,1),30:(lambda x:2-x*x,lambda x:x,-2,1),31:(lambda x:math.sin(2*x),math.sin,0,math.pi/3),32:(lambda x:x**3 if x<=1 else 2-x,lambda x:0,0,2),34:(lambda x:3-1.5*x,lambda x:0,0,2),35:(lambda x:math.sqrt(max(0,16-x*x)),lambda x:-2,0,4),37:(lambda x:x**3-x,lambda x:x*x-1,-1,1)}
for n,(f,g,lo,hi)in regions.items():
 top=samples(f,lo,hi,400);bot=samples(g,lo,hi,400);ys=[y for x,y in top+bot];cx,cy=coords[n];gap=max(.1,(max(ys)-min(ys))*.15)
 fig('8-3',n,[panel('Region boundaries and exact centroid',(lo-.15,hi+.15,min(ys)-gap,max(ys)+gap),[top,bot,[(lo,g(lo)),(lo,f(lo))],[(hi,g(hi)),(hi,f(hi))]],[(cx,cy)])])
fig('8-3',33,[equal('Region between x=y^2 and x=2-y', [[(y*y,y)for y in[-2+3*j/400 for j in range(401)]],[(4,-2),(1,1)]],[(1.6,-.5)],xr=(-1,6),cy=-.5)])
ys=[0,2,2.6,2.3,2.2,3.3,4,3.2,0];sim=lambda a:sum((1 if i in[0,8]else 4 if i%2 else 2)*v for i,v in enumerate(a))/3;area=sim(ys);cx=sim([i*v for i,v in enumerate(ys)])/area;cy=sim([v*v/2 for v in ys])/area
fig('8-3',36,[panel('Sampled graphical heights; Simpson centroid',(0,8,0,4.5),[list(enumerate(ys))],[(cx,cy)],xlabel='x',ylabel='height')],{'ko':'원본에서 읽은 정수점 근사 높이를 선분으로 이은 도해이다. 도심은 이 선분 영역이 아니라 해당 표본의 Simpson 합으로 계산했다.','en':'Segments connect approximate integer-point readings.The centroid uses Simpson sums of those samples, not the polygonal interpolant.'})
r=rep['numerical38'];lo,hi=map(float,r['intersections']);cx,cy=map(float,r['centroid']);fig('8-3',38,[panel('Exponential and parabola; numerical centroid',(-1.6,.8,0,2.4),[samples(math.exp,lo,hi),samples(lambda x:2-x*x,lo,hi)],[(cx,cy)])])
fig('8-3',40,[equal('Rectangle plus triangle; combined centroid',[[(-1,0),(2,0),(0,2),(-1,2),(-1,0)],[(0,0),(0,2)]],[(1/12,5/6)],xr=(-2,3),cy=1)])
fig('8-3',41,[equal('Two triangles above a rectangle; symmetry x=0',[[(-2,-1),(2,-1),(2,0),(1,2),(0,0),(-1,2),(-2,0),(-2,-1)],[(-2,0),(2,0)]],[(0,1/12)],xr=(-4,4),cy=.5)])
fig('8-3',42,[panel('Normalized rectangle: R1 below parabola,R2 above',(-.1,1.1,-.1,1.1),[[(0,0),(1,0),(1,1),(0,1),(0,0)],samples(lambda x:x*x,0,1)],[(.75,.3),(.375,.6)])])
fig('8-3',46,[equal('Generating triangle; centroid travels at radius4', [[(2,3),(2,5),(5,4),(2,3)],[(-1,0),(7,0)]],[(3,4)],xr=(-2,10),cy=2.5)])
fig('8-3',47,[equal('Quarter-circle WIRE, not filled quarter-disk',[circle(4,t0=0,t1=math.pi/2)],[(8/math.pi,8/math.pi)],xr=(-2,7),cy=2)])
fig('8-3',50,[panel('n=3,m=4: centroid lies above upper boundary x^3',(-.05,1.05,-.05,1.05),[samples(lambda x:x**3,0,1),samples(lambda x:x**4,0,1)],[(2/3,20/63)])])
# Surplus areas: boundary lines plus vertical shading strokes.
eco={4:(lambda x:2000-46*math.sqrt(x),400,'consumer'),5:(lambda x:870*math.exp(-.03*x),45,'consumer'),6:(lambda x:6-x/3500,11200,'consumer'),7:(lambda x:25-x/30,300,'consumer'),9:(lambda x:3+.01*x*x,10,'producer'),10:(lambda x:125+.002*x*x,500,'producer')}
r84=json.loads(Path(__file__).with_name('s8-4-report.json').read_text())['numerical'];eco[8]=(lambda x:800000*math.exp(-x/5000)/(x+20000),float(r84['8quantity']),'consumer');eco[11]=(lambda x:math.sqrt(30+.01*x*math.exp(.001*x)),float(r84['11quantity']),'producer')
for n,(f,q,kind)in eco.items():
 P=f(q);curves=[samples(f,0,q),[(0,P),(q,P)]]+[{'points':[(q*j/30,P),(q*j/30,f(q*j/30))],'color':'#a5b4fc'}for j in range(31)];vals=[f(0),P];gap=max(1,(max(vals)-min(vals))*.15)
 fig('8-4',n,[panel(f'{kind.title()} surplus: shaded strips between price and curve',(0,q*1.08,min(vals)-gap,max(vals)+gap),curves,[(q,P)],xlabel='quantity (thousands)' if n==5 else 'quantity',ylabel='price')])
fig('8-4',12,[panel('Equilibrium and the two surplus regions',(0,240,15,55),[samples(lambda x:50-x/20,0,240),samples(lambda x:20+x/10,0,240),[(0,40),(200,40)]],[(200,40)],xlabel='quantity',ylabel='price')])
for n,ts,ys in[(24,list(range(0,17,2)),[0,4.1,8.9,8.5,6.7,4.3,2.5,1.2,.2]),(25,list(range(0,17,2)),[0,6,7.4,6.7,5.4,4.1,3,2.2,1.5])]:
 fig('8-4',n,[panel('Concentration samples for Simpson integration',(0,16,0,10),[list(zip(ts,ys))],list(zip(ts,ys)),xlabel='time (s)',ylabel='concentration (mg/L)')],{'ko':'제시된 표 또는 원본 그래프의 근사 표본을 이은 도해. 적분은 Simpson 가중합으로 계산한다.','en':'Diagram joining tabulated or graph-estimated samples.Integration uses Simpson weights.'})
prob={3:(lambda x:30*x*x*(1-x)**2,0,1),4:(lambda x:math.exp(3-x)/(1+math.exp(3-x))**2,-3,9),6:(lambda x:2/9*(3*x-x*x),0,3),7:(lambda x:.1,0,10),8:(lambda x:x/30 if x<=6 else(10-x)/20,0,10),10:(lambda x:math.exp(-x/1000)/1000,0,4000),11:(lambda x:math.exp(-x/1.6)/1.6,0,8),13:(lambda x:x/1600 if x<=40 else(80-x)/1600,0,80),18:(lambda x:math.exp(-x*x/2)/math.sqrt(2*math.pi),-4,4),21:(lambda x:4*x*x*math.exp(-2*x),0,5)}
for n,(f,lo,hi)in prob.items():
 pts=samples(f,lo,hi,600);top=max(y for x,y in pts)*1.15
 fig('8-5',n,[panel('Probability density'+('; horizontal r/a0, vertical a0*p(r)'if n==21 else''),(lo,hi,0,top),[pts],[(1,f(1))]if n==21 else[(3,f(3))]if n==4 else[])])
for sec,d in docs.items():(R/f's{sec}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(counts)
