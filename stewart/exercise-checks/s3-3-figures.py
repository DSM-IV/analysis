"""Original graphs from formulas, plus explicitly labelled qualitative reconstructions."""
from calc1_core import panel,plot,samples
from pathlib import Path
import json,math,importlib.util
spec=importlib.util.spec_from_file_location('author',Path(__file__).with_name('build_s3_3.py'));a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
s=a.s;x=a.x;R=Path(__file__).resolve().parents[1]/'exercise-content';p=R/'s3-3.json';d=json.loads(p.read_text());E={e['number']:e for e in d['exercises']};count=0

def fig(n,panels,schematic=False):
 global count
 name=f's3-3-{n}.svg';plot(name,panels);E[n]['figure']={'src':'../exercise-content/assets/'+name,'alt':{'ko':f'3.3 {n}번 자체 그래프','en':f'Original graphs for Exercise3.3.{n}'},'caption':{'ko':'원본의 증감과 오목성을 설명하는 자체 개형. 높이와 접선 위치의 근삿값은 원본 기준이며 보간곡선의 정확한 해를 뜻하지 않는다.'if schematic else'해설의 함수식으로 직접 계산한 그래프. 무한 정의역은 표시창으로 잘랐으며 곡선별 색을 구분했다.','en':'Original schematic illustrating source monotonicity and concavity. Numerical estimates refer to the source,not exact solutions of the interpolation.'if schematic else'Graphs computed directly from the solution formulas. Infinite domains are clipped to a display window;colors distinguish curves.'}};count+=1

def herm(nodes):
 out=[]
 for (lo,y,u),(hi,z,v)in zip(nodes,nodes[1:]):
  for j in range(81):
   t=j/80;out.append((lo+(hi-lo)*t,(2*t**3-3*t*t+1)*y+(t**3-2*t*t+t)*(hi-lo)*u+(-2*t**3+3*t*t)*z+(t**3-t*t)*(hi-lo)*v))
 return out

def pp(fn,lo,hi,n=450):
 out=[]
 for j in range(n+1):
  z=lo+(hi-lo)*j/n
  try:v=fn(z)
  except(ValueError,ZeroDivisionError,TypeError):continue
  if math.isfinite(v):out.append((z,v))
 return out
fig(1,[panel('Function: minimum at 1; cusp at 4',(-.2,6.2,0,6.5),[herm([(0,5,-5),(1,2,0),(2,3,2),(3,4,0),(4,1,-6)]),herm([(4,1,4),(6,6,1)])],xticks=list(range(7)),yticks=list(range(7)))],True)
fig(2,[panel('Function with flat inflection at x=5',(-.2,7.2,0,6.5),[herm([(0,0,7),(1,3,0),(2,2,-1.5),(3,1,0),(4,3,3),(5,4,0),(7,6,3)])],xticks=list(range(8)),yticks=list(range(7)))],True)
der5=herm([(0,.7,0),(1,0,-1.4),(2,-1.2,0),(3,0,2),(4,1.5,0),(5,0,-2.5),(6,-1.8,0)])
der6=herm([(0,-1.5,3),(1,0,.3),(2,.2,.4),(3,2,6)])+herm([(3,2,-5),(4,0,-.7),(4.5,-.15,0),(5,0,.6),(6,1,1.3)])
fig(5,[panel('Given derivative: f increases above the axis',(-.2,6.2,-2.2,2),[der5],xticks=list(range(7)))],True)
fig(6,[panel('A derivative peak is not a maximum of f',(-.2,6.2,-2,2.5),[der6],xticks=list(range(7)))],True)
curve7=pp(lambda z:-((z-4)**2-4)**2/16+1,0,8)
fig(7,[panel('Same curve: interpret as f, first or second derivative',(-.2,8.2,-2,1.5),[curve7],xticks=list(range(9)))],True)
fig(8,[panel('Derivative signs versus derivative monotonicity',(-.2,9.2,-2,2),[herm([(0,.5,1.5),(1,1.5,0),(2,.7,0),(3,1.2,0),(4,0,-2),(5,-1,0),(6,0,1.3),(7,.9,0),(8,0,-1.5),(9,-2,-2)])],xticks=list(range(10)))],True)
windows={9:(-1,6),10:(-10,13),11:(-1,3),12:(-2,3),13:(0,10),14:(-4,5),15:(-3,5),16:(-1,4),18:(0,8),19:(-2,2),20:(-4,4),23:(-1,2),24:(-3,5),39:(-2,4),40:(-4,5),41:(-3,3),42:(-8,2),43:(-1,3),44:(-1.6,1.6),45:(-2,2.7),46:(-2.8,2.8),47:(-2,6),48:(-2,4),49:(-5,4),50:(0,1.2)}
for n,data in a.D.items():
 f,cuts,ips,*rest=data;excluded=rest[0]if rest else[];lo,hi=windows.get(n,(0,2*math.pi if n!=17 else math.pi))
 if n==52:hi=4*math.pi
 fn=lambda z,f=f:a.realval(f,z)
 edges=[lo]+[float(v)for v in excluded if lo<float(v)<hi]+[hi];curves=[]
 for j,(l,h)in enumerate(zip(edges,edges[1:])):curves.append(pp(fn,l+(.01 if j else 0),h-(.01 if j<len(edges)-2 else 0)))
 vals=sorted(v for pts in curves for z,v in pts);bot,top=(vals[int(len(vals)*.025)],vals[int(len(vals)*.975)])if excluded else(min(vals),max(vals));gap=max(.2,(top-bot)*.12)
 dots=[]
 for c in cuts+ips:
  if c not in excluded and lo<=float(c)<=hi:dots.append((float(c),fn(c)))
 fig(n,[panel('Function and critical/inflection candidates',(lo,hi,bot-gap,top+gap),curves,dots)])
for n,functions in[(28,[lambda z:-math.exp(z),math.exp]),(29,[lambda z:-math.exp(-z),lambda z:math.exp(-z)])]:
 fig(n,[panel('(a) Example',(-2,2,-8,8),[pp(functions[0],-2,2)]),panel('(b) Example',(-2,2,-8,8),[pp(functions[1],-2,2)])])
funcs={30:lambda z:z+4/z if z<0 else 1/z,31:lambda z:2/math.pi-math.pi*z*z/4 if z<0 else 2/math.pi*math.cos(math.pi*z/2)if z<=4 else 2/math.pi-math.pi*(z-4)**2/4,32:lambda z:-math.log(1-z)if z<1 else math.log(z-1)+(z-1)**2/8,33:lambda z:1-math.exp(z-2)if z<2 else-6/math.pi*math.cos(math.pi*(z-5)/6)if z<=8 else 1-math.exp(8-z),34:lambda z:z+1 if z<=-1 else-math.log(2-z)-z/2+math.log(3)-.5 if z<2 else-math.log(z-2)+(z-2)/2 if z<=4 else 1-math.log(2)-(z-4)**2,35:lambda z:2/math.pi*(1-math.cos(math.pi*z/2))if abs(z)<=6 else 4/math.pi-math.pi/4*(abs(z)-6)**2}
for n,bounds,ranges in[(30,(-6,4,-10,10),[(-6,-.03),(.03,4)]),(31,(-2,6,-3,1),[(-2,6)]),(32,(-3,7,-4,7),[(-3,.97),(1.03,7)]),(33,(-1,11,-2.2,1.2),[(-1,11)]),(34,(-3,6,-4,5),[(-3,1.98),(2.02,6)]),(35,(-8,8,-2,1.5),[(-8,8)])]:fig(n,[panel('Example satisfying all stated conditions',bounds,[pp(funcs[n],lo,hi,900)for lo,hi in ranges])])
# Labelled source schematic for36.
points=[(.5,1.5),(3,1.3),(5,3.7),(6,4),(7.5,3.5)]
fig(36,[panel('A, B, C, D, E: marked points from left to right',(0,8.2,0,4.5),[herm([(0,2,-1.3),(.5,1.5,-.9),(2,.8,0),(3,1.3,1),(4,2.6,1.5),(5,3.7,.6),(6,4,0),(7.5,3.5,-.6),(8.2,3,-.9)])],points)],True)
d37a=herm([(0,3,0),(2,0,-1.5),(3,-1,0),(4,0,1.5),(6,3,0)]);d37b=pp(lambda z:(z-6)**2/4+(z-6)/2-2,6,9)
d38=herm([(0,-2.5,2.5),(1,0,2.5),(2,1.7,0),(3,1.1,0),(5,3,0),(6,0,-4),(7,-1.5,0),(8,0,2.5),(9,2.5,2.5)])
for n,derivs in[(37,[d37a,d37b]),(38,[d38])]:
 accum=[];total=0;prior=None
 for pts in derivs:
  for z,v in pts:
   if prior is not None:total+=(z-prior[0])*(v+prior[1])/2
   accum.append((z,total));prior=(z,v)
 vals=[v for z,v in accum];fig(n,[panel('Given derivative (schematic)',(0,9,-3,4),derivs,[(6,3,'open'),(6,-2,'open')]if n==37 else[],xticks=list(range(10))),panel('One corresponding function with f(0)=0',(0,9,min(vals)-1,max(vals)+1),[accum],[(0,0)],xticks=list(range(10)))],True)
for n,fn in[(53,lambda z,c:z**4-c*z),(54,lambda z,c:z**3-3*c*c*z+2*c**3)]:fig(n,[panel('Parameter c=0.5 (blue), 1 (red), 2 (green)',(-3,3,-10,25),[pp(lambda z,c=c:fn(z,c),-3,3)for c in[.5,1,2]])])
for n,fn,lo,hi in[(55,lambda z:(z+1)/math.sqrt(z*z+1),-5,5),(56,lambda z:z+2*math.cos(z),0,2*math.pi),(57,lambda z:math.sin(2*z)+math.sin(4*z),0,math.pi),(58,lambda z:(z-1)**2*(z+1)**3,-1.5,1.5),(59,lambda z:(z**4+z**3+1)/math.sqrt(z*z+z+1),-2,2),(60,lambda z:(z+1)**2*(z*z+5)/((z*z-z+1)*(z*z+4)),-4,4)]:
 pts=pp(fn,lo,hi,900);v=[t[1]for t in pts];panels=[panel('Function',(lo,hi,min(v)-.2*(max(v)-min(v)),max(v)+.2*(max(v)-min(v))),[pts], [(-1,0,'open')]if n==60 else[])]
 if n>=57:
  sf={57:s.sin(2*x)+s.sin(4*x),58:(x-1)**2*(x+1)**3,59:(x**4+x**3+1)/s.sqrt(x*x+x+1),60:(x+1)**2*(x*x+5)/((x*x-x+1)*(x*x+4))}[n];dd=s.diff(sf,x,2);q=pp(lambda z:a.realval(dd,z),lo,hi,1000);ys=[t[1]for t in q];panels.append(panel('Second derivative: sign-changing zeros',(lo,hi,min(ys)*1.1-.1,max(ys)*1.1+.1),[q]))
 fig(n,panels)
fig(61,[panel('Population schematic: fastest growth around 8 h',(0,18,0,700),[herm([(0,0,12),(4,70,25),(6,140,55),(8,350,110),(10,520,55),(14,640,13),(18,675,5)])],xticks=list(range(0,19,2)),)],True)
fig(66,[panel('Depth vs time: narrowest cross-section near t=1',(0,2,0,2),[pp(lambda z:1+math.atan(3*(z-1))/math.atan(3),0,2)],[(1,1)],xlabel='normalized time',ylabel='depth')],True)
fig(74,[panel('c=-2 (blue), -1 (red), 0 (green), 2 (purple)',(-2,2,-3,10),[pp(lambda z,c=c:z**4+c*z**3+z*z,-2,2,900)for c in[-2,-1,0,2]])])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print('3.3 original SVG:',count)
