"""Own diagrams for Rolle and MVT; graph readings retain approximate status."""
from calc1_core import panel,plot,samples
from pathlib import Path
import math,json
R=Path(__file__).resolve().parents[1]/'exercise-content';p=R/'s3-2.json';d=json.loads(p.read_text());E={e['number']:e for e in d['exercises']}
def fig(n,panels,schematic=False):
 name=f's3-2-{n}.svg';plot(name,panels);E[n]['figure']={'src':'../exercise-content/assets/'+name,'alt':{'ko':f'3.2 {n}번 자체 도해','en':f'Original diagram for Exercise3.2.{n}'},'caption':{'ko':'원본의 증감·매끄러움과 끝값을 보존한 자체 개형. 접선 위치의 수치는 원본에서 읽은 근삿값이며 이 보간곡선의 정확한 해가 아니다.'if schematic else'주어진 함수 또는 해설의 반례를 직접 계산한 그래프.','en':'Original schematic preserving source monotonicity,smoothness and endpoint heights. Tangency estimates are read from the source,not exact solutions of this interpolation.'if schematic else'Graphs computed from the given function or the counterexample in the solution.'}}
def herm(nodes):
 pts=[]
 for (a,y,u),(z,v,w)in zip(nodes,nodes[1:]):
  for j in range(101):
   t=j/100;pts.append((a+(z-a)*t,(2*t**3-3*t*t+1)*y+(t**3-2*t*t+t)*(z-a)*u+(-2*t**3+3*t*t)*v+(t**3-t*t)*(z-a)*w))
 return pts
fig(1,[panel('Rolle: horizontal tangents near 1 and 5',(-.2,8.2,0,5),[herm([(0,3,-3),(1,1,0),(5,4,0),(8,3,-.7)]),[(0,3),(8,3)]],[(0,3),(1,1),(5,4),(8,3)],xticks=list(range(9)))],True)
fig(2,[panel('Equal endpoints; corner at x=4',(-.2,8.2,-1.5,4),[[(0,3),(4,-1),(8,3)]],[(0,3),(4,-1),(8,3)],xticks=list(range(9)))])
g=herm([(0,1,1.3),(2,3,.5),(3,3.2,0),(6,1,0),(8,4,2)])
fig(3,[panel('Secant on [0,8]: slope 3/8',(-.2,8.2,0,5),[g,[(0,1),(8,4)]],[(0,1),(8,4)],xticks=list(range(9))),panel('Secant on [2,6]: slope about -1/2',(-.2,8.2,0,5),[g,[(2,3),(6,1)]],[(2,3),(6,1)],xticks=list(range(9)))],True)
fig(4,[panel('Continuous counterexample: slopes 0 and 3/4',(-.2,8.2,0,5),[[(0,1),(4,1),(8,4)],[(0,1),(8,4)]],[(0,1),(4,1),(8,4)],xticks=list(range(9)))])
fig(5,[panel('Interior corner: MVT hypotheses fail',(-.2,5.2,-.2,4.5),[[(0,0),(3,3.5),(5,2)]],[(0,0),(3,3.5),(5,2)],xticks=list(range(6)))],True)
fig(6,[panel('Equal heights: two horizontal tangents',(-.2,5.2,-.3,4.5),[herm([(0,1,-2),(1,0,0),(3,4,0),(5,1,-2)])],[(0,1),(1,0),(3,4),(5,1)],xticks=list(range(6)))],True)
# Endpoint vertical tangent and horizontal joining slope at x=3.
f7=lambda x:1 if x<=3 else 3-2*math.sqrt(max(0,1-((x-3)/2)**2))
fig(7,[panel('Endpoint vertical tangent is allowed',(-.2,5.2,0,3.5),[samples(f7,0,5,1200),[(0,1),(5,3)]],[(0,1),(5,3)],xticks=list(range(6)))],True)
fig(8,[panel('Interior cusp: differentiability fails',(-.2,5.2,0,5),[samples(lambda x:4-abs(x-4)**(2/3),0,5,800)],[(4,4)],xticks=list(range(6)))],True)
fig(19,[panel('sqrt(x): secant and tangent at c=1',(-.2,4.2,-.2,2.8),[samples(math.sqrt,0,4),[(0,0),(4,2)],[(0,.5),(4,2.5)]],[(0,0),(1,1),(4,2)],xticks=list(range(5)))])
c=2/math.sqrt(3)
fig(20,[panel('x^3-2x: two parallel tangents',(-2.2,2.2,-8,8),[samples(lambda x:x**3-2*x,-2,2),[(-2,-4),(2,4)],samples(lambda x:2*x-8*c/3,-2,2),samples(lambda x:2*x+8*c/3,-2,2)],[(-2,-4),(2,4),(c,c**3-2*c),(-c,-c**3+2*c)],xticks=[-2,-1,0,1,2])])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print('3.2:10 original SVG figures')
