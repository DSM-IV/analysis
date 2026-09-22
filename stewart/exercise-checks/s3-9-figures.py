"""Computed antiderivative plots and original source-graph schematics."""
from calc1_core import panel,plot,samples
from pathlib import Path
import math,json,importlib.util
spec=importlib.util.spec_from_file_location('a39',Path(__file__).with_name('build_s3_9.py'));a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
R=Path(__file__).resolve().parents[1]/'exercise-content';p=R/'s3-9.json';d=json.loads(p.read_text());E={e['number']:e for e in d['exercises']};count=0

def fig(n,panels,schematic=False):
 global count
 name=f's3-9-{n}.svg';plot(name,panels);E[n]['figure']={'src':'../exercise-content/assets/'+name,'alt':{'ko':f'3.9 {n}번 자체 도해','en':f'Original diagram for Exercise3.9.{n}'},'caption':{'ko':'원본의 부호와 증감 관계를 설명하는 자체 개형. 눈금은 개형을 위한 좌표이며 원본의 추가 수치자료를 뜻하지 않는다.'if schematic else'해설의 함수식과 초기조건으로 직접 그린 그래프. 초등식이 없는 경우에는 수치 적분으로 원시함수를 그렸다.','en':'Original schematic illustrating the source signs and monotonicity. Coordinates organize the schematic and are not additional source data.'if schematic else'Graphs computed from the formulas and initial conditions. When no elementary form is used,the antiderivative is plotted by numerical integration.'}};count+=1

def auto(title,fn,lo,hi):
 pts=samples(fn,lo,hi,600);ys=[v for z,v in pts];gap=max(.2,(max(ys)-min(ys))*.12)
 return panel(title,(lo,hi,min(ys)-gap,max(ys)+gap),[pts])
def cumulative(pts,initial=0):
 result=[(pts[0][0],initial)];v=initial
 for (x,y),(z,w)in zip(pts,pts[1:]):v+=(z-x)*(y+w)/2;result.append((z,v))
 return result
for n,f,F,lo,hi in[(25,lambda z:5*z**4-2*z**5,lambda z:z**5-z**6/3+4,-1,3),(26,lambda z:z+2*math.sin(z),lambda z:z*z/2-2*math.cos(z)-4,-6,6),(56,lambda z:2*z-3*math.sqrt(z),lambda z:z*z-2*z**1.5+1,0,4)]:fig(n,[auto('Given function f',f,lo,hi),auto('Antiderivative F with the given initial value',F,lo,hi)])
fig(51,[panel('f (blue), a (red), b (green), c (purple)',(-.2,2,-1,2),[samples(lambda z:z*z-z,0,2),samples(lambda z:4*z-1,0,2),samples(lambda z:z**3/3-z*z/2,0,2),samples(lambda z:-z**3/3+z*z/2,0,2)])],True)
fig(52,[panel('f (blue), a (red), b (green), c (purple)',(0,5,-1.2,1.2),[samples(lambda z:(1-z)*math.exp(-z),0,5),samples(lambda z:z*math.exp(-z),0,5),samples(lambda z:-z*math.exp(-z),0,5),samples(lambda z:-(z-2)**2/8*math.exp(-z/4),0,5)])],True)
def herm(nodes):
 out=[]
 for (lo,y,u),(hi,z,v)in zip(nodes,nodes[1:]):
  for j in range(81):
   t=j/80;out.append((lo+(hi-lo)*t,(2*t**3-3*t*t+1)*y+(t**3-2*t*t+t)*(hi-lo)*u+(-2*t**3+3*t*t)*z+(t**3-t*t)*(hi-lo)*v))
 return out
f53=herm([(0,0,-2),(1,-1,0),(2,0,2),(2.5,.6,0),(3,0,-1.5),(3.5,-.4,0),(5,0,0)]);F53=cumulative(f53,1)
fig(53,[panel('Function f (schematic)',(0,5,-1.3,.8),[f53]),panel('Antiderivative starting at (0,1)',(0,5,-1,1.3),[F53],[(0,1)])],True)
v54=herm([(0,0,0),(1,2,0),(1.5,2,0),(2.5,0,0),(3,0,0),(3.5,-1,0),(4.2,0,0),(5,0,0)]);s54=cumulative(v54)
fig(54,[panel('Velocity: positive, zero, negative, zero',(0,5,-1.3,2.4),[v54],xlabel='schematic time'),panel('One position function',(0,5,-.3,4),[s54],xlabel='schematic time')],True)
fig(55,[panel('Derivative: constant on each open interval',(-.2,3.2,-1.5,2.5),[[(0,2),(1,2)],[(1,1),(2,1)],[(2,-1),(3,-1)]],[(0,2,'open'),(1,2,'open'),(1,1,'open'),(2,1,'open'),(2,-1,'open'),(3,-1,'open')],xticks=[0,1,2,3]),panel('Continuous antiderivative',(-.2,3.2,-1.5,2.5),[[(0,-1),(1,1),(2,2),(3,1)]],[(0,-1),(1,1),(2,2),(3,1)],xticks=[0,1,2,3])])
for n,fn,lo,hi in[(57,lambda z:math.sin(z)/(1+z*z),-2*math.pi,2*math.pi),(58,lambda z:math.sqrt(z**4-2*z*z+2)-2,-3,3)]:
 pts=samples(fn,lo,hi,2400);integ=cumulative(pts);base=integ[len(integ)//2][1];integ=[(z,v-base)for z,v in integ];ys=[v for z,v in integ]
 fig(n,[auto('Function f',fn,lo,hi),panel('Antiderivative through the origin',(lo,hi,min(ys)-.2,max(ys)+.2),[integ],[(0,0)])])
fig(65,[panel('Height: dropped (blue), thrown downward (red)',(0,10,0,470),[samples(lambda t:450-4.9*t*t,0,math.sqrt(450/4.9)),samples(lambda t:450-5*t-4.9*t*t,0,(-5+math.sqrt(8845))/9.8)],xlabel='t (s)',ylabel='height (m)')])
fig(70,[panel('Normalized board: m=rho=L=E=I=1; g=-1',(0,1,-.5,.05),[samples(lambda z:-(z*z/2-z**3/6+z*z/4-z**3/6+z**4/24),0,1)],[(0,0),(1,-11/24)],xlabel='distance along board',ylabel='vertical deflection')])
v78=lambda t:30*t*t if t<=3 else 270-32*(t-3)if t<=17 else-178+32*(t-17)if t<=22 else-18
s78=lambda t:10*t**3 if t<=3 else 270+270*(t-3)-16*(t-3)**2 if t<=17 else 914-178*(t-17)+16*(t-17)**2 if t<=22 else 424-18*(t-22)
fig(78,[panel('Rocket velocity: four flight phases',(0,46,-210,300),[samples(v78,0,410/9,1500)],[(3,270),(17,-178),(22,-18)],xticks=[0,3,11.4375,17,22,410/9],xlabel='t (s)',ylabel='v (ft/s)'),panel('Rocket height',(0,46,0,1500),[samples(s78,0,410/9,1500)],[(3,270),(183/16,22545/16),(17,914),(22,424),(410/9,0)],xticks=[0,3,11.4375,17,22,410/9],xlabel='t (s)',ylabel='height (ft)')])
fig(79,[panel('Rest-to-rest speed profile for a 20 min trip',(0,1200,0,290),[[(0,0),(110,264),(1090,264),(1200,0)]],[(0,0),(110,264),(1090,264),(1200,0)],xticks=[0,110,600,1090,1200],xlabel='t (s)',ylabel='v (ft/s)')])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print('3.9 original SVG:',count)
