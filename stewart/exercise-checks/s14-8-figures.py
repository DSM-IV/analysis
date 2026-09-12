import math,json
from pathlib import Path
R=Path(__file__).resolve().parents[1];A=R/'exercise-content/assets';p=R/'exercise-content/s14-8.json';D=json.loads(p.read_text())
def base(title):return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 600"><rect width="850" height="600" fill="white"/>',f'<text x="425" y="30" text-anchor="middle" font-family="sans-serif" font-size="18">{title}</text>']
def line(out,pts,color='#3574ad',width=1):out.append('<polyline points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+f'" fill="none" stroke="{color}" stroke-width="{width}"/>')
def save(n,out,ko,en):
 out.append('</svg>');name=f's14-8-{n}.svg';(A/name).write_text('\n'.join(out));next(e for e in D['exercises'] if e['number']==n)['figure']=dict(src='../exercise-content/assets/'+name,alt=dict(ko=ko,en=en),caption=dict(ko=ko,en=en))
out=base('Unit circle (red), level parabolas x² + y = c (blue)');proj=lambda x,y:(425+150*x,300-150*y)
line(out,[proj(math.cos(i*math.pi/100),math.sin(i*math.pi/100)) for i in range(201)],'#b33b37',3)
for c in [-1,-.5,0,.5,1,1.25]:
 pts=[proj(x,c-x*x) for x in [-1.25+i*.025 for i in range(101)] if -1.5<=c-x*x<=1.5];line(out,pts,'#3574ad',2 if c in [-1,1.25] else 1)
out.append('<text x="435" y="495">minimum c = −1</text><text x="470" y="88">maximum c = 5/4</text>');save(2,out,'단위원과 함수의 등위포물선. 접촉값은 최소−1, 최대5/4.','Unit circle and level parabolas; tangent values are minimum−1 and maximum5/4.')
out=base('Constraint √x + √y = 5 (red), objective lines 2x + 3y = c');proj=lambda x,y:(120+20*x,550-18*y)
line(out,[proj(t*t,(5-t)**2) for t in [i/40 for i in range(201)]],'#b33b37',3)
for c in [30,50,75]:line(out,[proj(x,(c-2*x)/3) for x in [i*.25 for i in range(101)] if 0<=(c-2*x)/3<=27],'#3574ad',2)
for x,y,txt in [(9,4,'min 30'),(0,25,'max 75')]:px,py=proj(x,y);out.append(f'<circle cx="{px}" cy="{py}" r="5" fill="#222"/><text x="{px+10}" y="{py-10}">{txt}</text>')
save(34,out,'제약곡선과 목적함수 직선. 정칙 접촉점은 최소이며 최대는 끝점이다.','Constraint and objective lines; regular tangency is a minimum, while the maximum is an endpoint.')
out=base('Cubic level curves (blue), constraint circle (red)');proj=lambda x,y:(90+75*x,535-75*y);f=lambda x,y:x**3+y**3+3*x*y
# Marching squares independently computes contours from the function.
for level in [3.67305217167,20,60,120,200,280,347.3269478283]:
 for i in range(100):
  for j in range(100):
   xx=i*.07;yy=j*.07;corn=[(xx,yy),(xx+.07,yy),(xx+.07,yy+.07),(xx,yy+.07)];vals=[f(a,b)-level for a,b in corn];hits=[]
   for k in range(4):
    l=(k+1)%4
    if vals[k]*vals[l]<0:
     q=vals[k]/(vals[k]-vals[l]);hits.append(proj(corn[k][0]+q*(corn[l][0]-corn[k][0]),corn[k][1]+q*(corn[l][1]-corn[k][1])))
   for k in range(0,len(hits)-1,2):line(out,hits[k:k+2])
line(out,[proj(3+3*math.cos(i*math.pi/100),3+3*math.sin(i*math.pi/100)) for i in range(201)],'#b33b37',3)
for a,txt in [(3-3/math.sqrt(2),'min 3.673'),(3+3/math.sqrt(2),'max 347.327')]:px,py=proj(a,a);out.append(f'<circle cx="{px}" cy="{py}" r="5"/><text x="{px+10}" y="{py-10}">{txt}</text>')
save(36,out,'함수에서 계산한 등고선과 제약 원. 두 접점의 극값을 수치 해설과 비교한다.','Computed function contours and constraint circle, with the two tangency extrema for numerical comparison.')
out=base('Cone (blue), plane (orange), ellipse (red)');proj=lambda x,y,z:(440+130*x-75*y,460+30*x+35*y-170*z)
for zz in [.25,.5,.75,1,1.25,1.5,1.75,2]:line(out,[proj(zz*math.cos(i*math.pi/70),zz*math.sin(i*math.pi/70),zz) for i in range(141)])
for i in range(20):th=i*math.pi/10;line(out,[proj(zz*math.cos(th),zz*math.sin(th),zz) for zz in [0,2]])
for yy in [-1,-.5,0,.5,1]:line(out,[proj(xx,yy,(5-4*xx+3*yy)/8) for xx in [-1.5,1.5]],'#dd8c39')
pts=[]
for i in range(241):th=i*math.pi/120;zz=5/(8+4*math.cos(th)-3*math.sin(th));pts.append(proj(zz*math.cos(th),zz*math.sin(th),zz))
line(out,pts,'#b33b37',3);save(58,out,'원뿔·평면과 직접 매개화한 타원 교선.','Cone, plane, and directly parametrized elliptical intersection.')
p.write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n');print('4 original figures')
