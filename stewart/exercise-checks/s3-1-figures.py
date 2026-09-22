"""Original diagrams; dots preserve source endpoint and discontinuity distinctions."""
from calc1_core import panel,plot,samples
from pathlib import Path
import json,math as m,sympy as s
R=Path(__file__).resolve().parents[1]/'exercise-content';p=R/'s3-1.json';d=json.loads(p.read_text());E={e['number']:e for e in d['exercises']};pi=m.pi

def fig(n,panels,ko='자체 제작 그래프. 채운 점은 포함된 함수값, 빈 점은 제외된 점이다. 무한 정의역은 표시창으로 잘랐다.',en='Original plots. Filled points are included function values; open points are excluded. Infinite domains are clipped to a display window.'):
 name=f's3-1-{n}.svg';plot(name,panels);E[n]['figure']={'src':'../exercise-content/assets/'+name,'alt':{'ko':f'3.1 {n}번 자체 그래프','en':f'Original graphs for Exercise3.1.{n}'},'caption':{'ko':ko,'en':en}}
def smooth(points):
 out=[]
 for (a,c),(b,d)in zip(points,points[1:]):
  for j in range(51):
   u=j/50;v=3*u*u-2*u**3;out.append((a+(b-a)*u,c+(d-c)*v))
 return out
fig(3,[panel('Schematic: a=0, b=1, c=2, d=3, r=4, s=5',(-.3,5.3,0,5),[smooth([(0,3),(1,1.5),(2,4),(3,3),(4,1),(5,4.5)])],[(0,3),(5,4.5)],xticks=list(range(6)))], '주어진 극값의 상대적 높이를 보존한 자체 개형. 가로 위치0,1,2,3,4,5는 각각a,b,c,d,r,s를 뜻하며 원본의 정확한 좌표값은 아니다.', 'Original schematic preserving the relative extrema. Horizontal positions0,1,2,3,4,5 denote a,b,c,d,r,s respectively,not exact source coordinates.')
fig(4,[panel('Schematic: a=0, b=1, c=2, d=3, r=4, s=5',(-.3,5.3,0,5),[smooth([(0,1),(1,3.5)]),smooth([(1,1.5),(2,4)]),smooth([(2,2),(3,1.3),(4,4.5),(5,1.5)])],[(0,1),(1,3.5),(1,1.5,'open'),(2,4,'open'),(2,2),(5,1.5)],xticks=list(range(6)))], '자체 개형. 가로 위치0,…,5는a,b,c,d,r,s이며 채운 점과 빈 점의 포함 관계를 보존했다.', 'Original schematic. Positions0,…,5 stand for a,b,c,d,r,s; filled/open point membership is preserved.')
fig(5,[panel('Values and open/filled points',(-.4,7.4,0,6),[smooth([(0,2),(1,4),(2,2),(4,5),(5,3),(6,4)]),smooth([(6,3),(7,1)])],[(0,2),(1,4,'open'),(1,3),(6,4),(6,3,'open'),(7,1,'open')],xticks=list(range(8)),yticks=list(range(7)))])
fig(6,[panel('Values and open/filled points',(-.4,7.4,0,6),[smooth([(0,5),(2,3),(3,4),(4,1),(6,3),(7,2)])],[(0,5,'open'),(2,3,'open'),(2,2),(7,2)],xticks=list(range(8)),yticks=list(range(7)))])
for n,pts in [(7,[(1,2),(2,0),(3,3),(4,1),(5,4)]),(8,[(1,1),(2,3),(3,2),(4,4),(5,0)]),(9,[(1,1),(2,3),(3,0),(4,4),(5,2)])]:fig(n,[panel('A continuous polygonal example',(.7,5.3,-.5,4.5),[pts],pts,xticks=[1,2,3,4,5],yticks=[0,1,2,3,4])])
fig(10,[panel('Maximum at2; stationary non-extremum at4',(.7,5.3,-2,9),[samples(lambda x:x+6,1,2),samples(lambda x:-(x-4)**3,2,5)],[(1,7),(2,8),(4,0),(5,-1)],xticks=[1,2,3,4,5])])
fig(11,[panel('(a) Differentiable maximum',(0,4,-4.5,1.5),[samples(lambda x:-(x-2)**2,0,4)],[(2,0)]),panel('(b) Continuous corner maximum',(0,4,-2.5,1.5),[[(0,-2),(2,0),(4,-2)]],[(2,0)]),panel('(c) Discontinuous maximum',(0,4,-4.5,1.5),[samples(lambda x:-(x-2)**2,0,4)],[(2,0,'open'),(2,1)])])
fig(12,[panel('(a) Endpoint absolute maximum',(-1.2,2.2,-1.5,2.5),[[(-1,-1),(2,2)]],[(-1,-1),(2,2)]),panel('(b) Local maximum at0; unbounded near2',(-1.2,2.2,-1.5,8),[samples(lambda x:-x*x,-1,1),samples(lambda x:1/(2-x),1,1.9)],[(-1,-1),(1,-1),(1,1,'open'),(2,0)],xticks=[-1,0,1,2])])
fig(13,[panel('(a) Maximum2; unattained infimum -1',(-1.2,2.2,-1.5,2.5),[[(-1,-1),(2,2)]],[(-1,-1,'open'),(-1,1),(2,2)]),panel('(b) Discontinuous with min0 and max1',(-1.2,2.2,-.3,1.3),[[(-1,0),(0,0)],[(0,1),(2,1)]],[(-1,0),(0,0,'open'),(0,1),(2,1)],xticks=[-1,0,1,2],yticks=[0,1])])
f14=lambda x:(x**10/10-23*x**8/8+175*x**6/6-477*x**4/4+162*x*x)/1000
fig(14,[panel('(a) Two maxima, one minimum, no absolute minimum',(-2,2,-5,.5),[samples(lambda x:-(x*x-1)**2,-2,2)],[(0,-1),(-1,0),(1,0)]),panel('(b) Seven critical numbers, five local extrema',(-3.5,3.5,-.04,.2),[samples(f14,-3.5,3.5,1400)],[(x,f14(x))for x in[-3,-2,-1,0,1,2,3]],xticks=list(range(-3,4)))])
fig(15,[panel('3 - 2x, x >= -1',(-1.4,4,-5,6),[samples(lambda x:3-2*x,-1,4)],[(-1,5)])])
fig(16,[panel('x^2, -1 <= x < 2',(-1.3,2.3,-.5,4.5),[samples(lambda x:x*x,-1,2)],[(-1,1),(2,4,'open'),(0,0)])])
fig(17,[panel('1/x, x >= 1',(.5,6,0,1.3),[samples(lambda x:1/x,1,6)],[(1,1)])])
fig(18,[panel('1/x, 1 < x < 3',(.7,3.3,0,1.3),[samples(lambda x:1/x,1,3)],[(1,1,'open'),(3,1/3,'open')])])
fig(19,[panel('sin x, 0 <= x < pi/2',(-.2,1.8,-.2,1.2),[samples(m.sin,0,pi/2)],[(0,0),(pi/2,1,'open')])])
fig(20,[panel('sin x, 0 < x <= pi/2',(-.2,1.8,-.2,1.2),[samples(m.sin,0,pi/2)],[(0,0,'open'),(pi/2,1)])])
fig(21,[panel('sin x, -pi/2 <= x <= pi/2',(-1.8,1.8,-1.2,1.2),[samples(m.sin,-pi/2,pi/2)],[(-pi/2,-1),(pi/2,1)])])
fig(22,[panel('cos t, -3pi/2 <= t <= 3pi/2',(-5,5,-1.3,1.3),[samples(m.cos,-1.5*pi,1.5*pi,500)],[(-1.5*pi,0),(1.5*pi,0)],xlabel='t')])
fig(23,[panel('1+(x+1)^2, -2 <= x < 5',(-2.4,5.4,-1,40),[samples(lambda x:1+(x+1)**2,-2,5)],[(-2,2),(-1,1),(5,37,'open')])])
fig(24,[panel('|x|',(-3,3,-.5,3.5),[[(-3,3),(0,0),(3,3)]],[(0,0)])])
fig(25,[panel('1-sqrt(x), x >= 0',(-.4,9,-2.5,1.5),[samples(lambda x:1-m.sqrt(x),0,9)],[(0,1)])])
fig(26,[panel('1-x^3: horizontal tangent without extremum',(-2,2,-7.5,9.5),[samples(lambda x:1-x**3,-2,2)],[(0,1)])])
fig(27,[panel('Piecewise: x^2 then 2-3x',(-1.2,1.2,-1.5,2.5),[samples(lambda x:x*x,-1,0),[(0,2),(1,-1)]],[(-1,1),(0,0),(0,2,'open'),(1,-1)])])
fig(28,[panel('Piecewise: 2x+1 then 4-2x',(-.2,3.2,-2.5,3.5),[[(0,1),(1,3)],[(1,2),(3,-2)]],[(0,1),(1,3,'open'),(1,2),(3,-2)])])
f47=lambda x:1+210*m.sin(x)/((x-3)**2+1);f48=lambda x:100*m.cos(x)**2/(10+x*x)-1
fig(47,[panel('Derivative: ten zero crossings (vertical clipping)',(-12,19,-8,8),[samples(f47,-12,19,5000)]),panel('Small final negative lobe, enlarged',(15.5,18.5,-.1,.5),[samples(f47,15.5,18.5,1200)])], '도함수의 자체 그래프. 위 패널은 세로범위를 잘랐고 아래는 놓치기 쉬운 마지막 두 영점을 확대한 것이다. 다른쪽 끝에는 추가 음의 사인반파가 없다.', 'Original derivative plots. The upper plot clips the vertical range; the lower enlarges the last two easily missed roots. There is no additional negative sine half-wave at the opposite endpoint.')
fig(48,[panel('Even derivative: fourteen zero crossings',(-10,10,-1.2,9.5),[samples(f48,-10,10,6000)]),panel('Last positive arch; two small crossings',(9,9.7,-.15,.03),[samples(f48,9,9.7,1400)])], '자체 도함수 그래프. 마지막 봉우리의 높이가 작으므로 별도 확대했다. 짝함수이므로 음수쪽에 같은 두 영점이 있다.', 'Original derivative plots. The last arch is very shallow and is enlarged separately. Even symmetry gives the matching two negative roots.')
fig(62,[panel('Corners and stationary points of |1+5x-x^3|',(-3,3,-.5,14),[samples(lambda x:abs(1+5*x-x**3),-3,3,1200)])])
for n,fn,lo,hi in [(63,lambda x:x**5-x**3+2,-1,1),(64,lambda x:x**4-3*x**3+3*x*x-x,0,2),(65,lambda x:x*m.sqrt(max(0,x-x*x)),0,1),(66,lambda x:x-2*m.cos(x),-2,0)]:
 pts=samples(fn,lo,hi,600);ys=[q[1]for q in pts];gap=max(max(ys)-min(ys),.1)*.12
 fig(n,[panel('Function on its full closed domain',(lo-(hi-lo)*.07,hi+(hi-lo)*.07,min(ys)-gap,max(ys)+gap),[pts],[(lo,fn(lo)),(hi,fn(hi))])])
report=json.loads((R.parent/'exercise-checks/s3-1-report.json').read_text());c=report['regression70'];vel=lambda t:sum(c[j]*t**j for j in range(4));acc=lambda t:c[1]+2*c[2]*t+3*c[3]*t*t;times=[0,10,15,20,32,59,62,125];ys=[0,185,319,447,742,1325,1445,4151]
fig(70,[panel('(a) Cubic regression and source data',(-5,130,-100,4400),[samples(vel,0,125)],list(zip(times,ys)),xlabel='t (s)',ylabel='v (ft/s)'),panel('(b) Acceleration model',(-5,130,15,80),[samples(acc,0,125)],xlabel='t (s)',ylabel='a (ft/s^2)')], '자체 최소제곱회귀 그래프. 채운 점은 문제의 속도 자료, 선은3차 적합곡선이다. 아래는 그 도함수인 가속도 모형이다.', 'Original least-squares fit. Filled points are supplied velocity data; the line is the fitted cubic. The lower panel shows its derivative,the acceleration model.')
fig(71,[panel('Normalized airflow model',(-.05,1.05,-.01,.17),[samples(lambda u:u*u*(1-u),0,1)],[(0,0),(.5,.125),(2/3,4/27),(1,0)],xticks=[0,.5,2/3,1],ylabel='v/(k r0^3)',xlabel='u = r/r0')])
fig(74,[panel('(a) Two critical numbers: x^3-3x',(-2.2,2.2,-5,5),[samples(lambda x:x**3-3*x,-2.2,2.2)],[(-1,2),(1,-2)]),panel('(a) One critical number: x^3',(-2,2,-8.5,8.5),[samples(lambda x:x**3,-2,2)],[(0,0)]),panel('(a) No critical numbers: x^3+x',(-2,2,-10.5,10.5),[samples(lambda x:x**3+x,-2,2)])])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print('3.1:',sum('figure'in e for e in E.values()),'original SVGs')
