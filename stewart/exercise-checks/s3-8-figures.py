"""Newton tangent constructions and original qualitative diagrams."""
from calc1_core import panel,plot,samples
from pathlib import Path
import math,json,importlib.util
spec=importlib.util.spec_from_file_location('a38',Path(__file__).with_name('build_s3_8.py'));a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
s=a.s;x=a.x;R=Path(__file__).resolve().parents[1]/'exercise-content';p=R/'s3-8.json';d=json.loads(p.read_text());E={e['number']:e for e in d['exercises']};count=0

def fig(n,panels,schematic=False):
 global count
 name=f's3-8-{n}.svg';plot(name,panels);E[n]['figure']={'src':'../exercise-content/assets/'+name,'alt':{'ko':f'3.8 {n}번 자체 도해','en':f'Original diagram for Exercise3.8.{n}'},'caption':{'ko':'원본을 설명하는 자체 개형. 근사 접선은 원본에서 읽은 기울기이며 보간곡선의 정확한 근을 주장하지 않는다.'if schematic else'함수식과 뉴턴 반복으로 직접 계산한 도해. 파랑은 함수, 다른 색은 접선 또는 비교 곡선이며 표시창 밖은 잘랐다.','en':'Original schematic explaining the source graph.Estimated tangents use source readings,not claims about exact interpolation roots.'if schematic else'Plots computed from formulas and Newton iteration.Blue denotes the function;other colors denote tangents or comparison curves.The display window clips unshown portions.'}};count+=1

def herm(nodes):
 out=[]
 for (lo,y,u),(hi,z,v)in zip(nodes,nodes[1:]):
  for j in range(81):
   t=j/80;out.append((lo+(hi-lo)*t,(2*t**3-3*t*t+1)*y+(t**3-2*t*t+t)*(hi-lo)*u+(-2*t**3+3*t*t)*z+(t**3-t*t)*(hi-lo)*v))
 return out
curve=herm([(0,2.4,-.25),(1,1.85,-.8),(2.8,0,-.85),(5,-1,0),(6,-.75,.75/1.3),(7.3,.6,1.2),(8,3,3)])
fig(1,[panel('First two tangent steps from x1=6',(-.2,8.5,-1.5,4),[curve,[(6,-.75),(7.3,0)],[(7.3,.6),(6.8,0)]],[(6,-.75),(7.3,0),(7.3,.6),(6.8,0)],xticks=list(range(9)))],True)
fig(2,[panel('Tangent estimates from x1=1',(-.2,8.5,-1.5,4),[curve,[(1,1.85),(3.3125,0)],[(3.3125,-.38),(2.8,0)]],[(1,1.85),(3.3125,0),(2.8,0)],xticks=list(range(9)))],True)
fig(4,[panel('Horizontal tangents at1 and4; roots near2 and6',(-3,7,-2,3),[herm([(-3,.15,.02),(0,1,.8),(1,1.8,0),(2,0,-2),(4,-1.5,0),(6,0,1.5),(7,3,4)])],[(0,1),(1,1.8),(3,-1.1),(4,-1.5),(5,-1.1)],xticks=[0,1,2,3,4,5,6])],True)
f=lambda z:z*z/(1+z*z)
fig(5,[panel('Model of the source shape: a=-1,b=0.7,c=1.4,d=2.3',(-4,4,-.15,1.1),[samples(f,-4,4,900)],[(z,f(z))for z in[-1,.7,1.4,2.3]])],True)
# Explicit tangent geometry for the first iteration problems.
for n,f,seed,lo,hi in[(6,2*x**3-3*x*x+2,-1,-1.3,.2),(7,2/x-x*x+1,2,.8,2.5),(8,x**5-x*x-1,1,.6,1.6),(9,x**3+x+3,-1,-2,.5),(10,x**4-x-1,1,0,2)]:
 fn=s.lambdify(x,f,'math');df=s.lambdify(x,s.diff(f,x),'math');pts=samples(fn,lo,hi,600);v=[y for z,y in pts];curves=[pts];dots=[];c=float(seed)
 for j in range(2 if n<=8 else 1):
  nxt=c-fn(c)/df(c);curves.append([(c,fn(c)),(nxt,0)]);dots +=[(c,fn(c)),(nxt,0)];c=nxt
 fig(n,[panel('Newton tangents: intercepts are the next iterates',(lo,hi,min(v)-.3,max(v)+.3),curves,dots)])
windows={11:(0,4),12:(1,3),13:(2,3),14:(3,4),15:(-2.5,-1.5),16:(0,3.2),17:(0,2.3),18:(-1,1),20:(0,2.5),21:(-1,1),22:(-3,2.5),23:(-2,1.6),24:(-1.5,3),25:(0,1),26:(-1,1)}
for n,(f,seeds,places,k,e,why,whye)in a.cases.items():
 lo,hi=windows[n];fn=s.lambdify(x,f,'math');pts=samples(fn,lo,hi,800);ys=sorted(v for z,v in pts);bot,top=ys[int(.05*len(ys))],ys[int(.95*len(ys))];gap=max(.1,(top-bot)*.15)
 rr=[float(rec['iterations'][-1])for rec in a.records if rec['exercise']==n]
 fig(n,[panel('Equation f(x)=0 and its real root(s)',(lo,hi,bot-gap,top+gap),[pts],[(z,0)for z in rr])])
fig(19,[panel('Substitution u=cube_root(x): u^4-u^3-1=0',(-1.2,1.7,-2,3),[samples(lambda u:u**4-u**3-1,-1.2,1.7)],xlabel='u')])
f30=lambda z:z**3-z-1;tangents=[]
for c in[1,.6,.57]:tangents.append(lambda z,c=c:f30(c)+(3*c*c-1)*(z-c))
fig(30,[panel('Function and the three first tangents',(0,1.6,-2,2),[samples(f30,0,1.6)]+[samples(fn,0,1.6)for fn in tangents],[(c,f30(c))for c in[1,.6,.57]]),panel('Wide view: small slopes give distant intercepts',(-60,20,-3,3),[samples(f30,-60,20,4000)]+[samples(fn,-60,20)for fn in tangents])])
cube=lambda z:math.copysign(abs(z)**(1/3),z)
fig(31,[panel('Real cube root: 1 -> -2 -> 4',(-3,5,-2,2),[samples(cube,-3,5,1000),[(1,1),(-2,0)],[(-2,cube(-2)),(4,0)]],[(1,1),(-2,0),(4,0)])])
sq=lambda z:math.copysign(math.sqrt(abs(z)),z)
fig(32,[panel('Two-cycle: 1 -> -1 -> 1',(-1.5,1.5,-1.5,1.5),[samples(sq,-1.5,1.5,1000),[(1,1),(-1,0)],[(-1,-1),(1,0)]],[(1,1),(-1,-1),(1,0),(-1,0)])])
f33=lambda z:z**6-z**4+3*z**3-2*z
fig(33,[panel('Three critical points; compare their heights',(-1.7,1.1,-2.5,5),[samples(f33,-1.7,1.1,1200)],[(float(r['iterations'][-1]),f33(float(r['iterations'][-1])))for r in a.records if r['exercise']==33])])
fig(34,[panel('Maximum of x cos x on[0,pi]',(0,math.pi,-3.4,1),[samples(lambda z:z*math.cos(z),0,math.pi)],[(float(r['iterations'][-1]),float(r['iterations'][-1])*math.cos(float(r['iterations'][-1])))for r in a.records if r['exercise']==34])])
fig(35,[panel('Inflection of x^2 sin x',(0,math.pi,-.2,4.5),[samples(lambda z:z*z*math.sin(z),0,math.pi)],[(float(r['iterations'][-1]),float(r['iterations'][-1])**2*math.sin(float(r['iterations'][-1])))for r in a.records if r['exercise']==35])])
c=next(float(r['iterations'][-1])for r in a.records if r['exercise']==36)
fig(36,[panel('Largest positive tangent slope through the origin',(-.2,7,-1.3,1.7),[samples(lambda z:-math.sin(z),-.2,7),samples(lambda z:-math.cos(c)*z,-.2,7)],[(0,0),(c,-math.sin(c))])])
c=next(float(r['iterations'][-1])for r in a.records if r['exercise']==37)
fig(37,[panel('Nearest point to the origin',(-1.5,3.5,-.1,2.5),[samples(lambda z:(z-1)**2,-.5,2),[(0,0),(c,(c-1)**2)]],[(0,0),(c,(c-1)**2)])])
th=next(float(r['iterations'][-1])for r in a.records if r['exercise']==38);rad=5/th;left=(-2,rad*math.cos(th/2));right=(2,left[1]);circle=[(rad*math.cos(t),rad*math.sin(t))for t in [2*math.pi*j/600 for j in range(601)]]
fig(38,[panel('Chord 4 cm; minor arc 5 cm',(-5.0074074074,5.0074074074,-2.6,2.6),[circle,[left,right],[(0,0),left],[(0,0),right]],[(0,0),left,right])])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print('3.8 original SVG:',count)
