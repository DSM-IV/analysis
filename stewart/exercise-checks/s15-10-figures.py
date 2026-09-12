"""Original diagrams for Chapter15 Review, based on stated bounds/readings."""
from pathlib import Path
import json,math,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from plot_15 import solid,attach
R=Path(__file__).resolve().parents[1];d=json.loads((R/'exercise-content/s15-10.json').read_text());items={e['number']:e for e in d['exercises']}
for n,vals in [(1,[[2.7,4.7,6.7],[4.5,6.5,8.5],[8,10,12]]),(2,[[1.1,3.1,5.1],[2.2,4.2,6.2],[5.2,7.2,9.2]])]:
 out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 440"><rect width="440" height="440" fill="#f8fafc"/><text x="35" y="30" font-size="16">Approximate contour readings</text>']
 for k in range(4):
  v=60+100*k;out.append(f'<path d="M60,{v}H360 M{v},60V360" stroke="#cbd5e1"/><text x="{v}" y="385" font-size="13">{k}</text><text x="35" y="{360-100*k}" font-size="13">{k}</text>')
 for j,row in enumerate(vals):
  for i,val in enumerate(row):
   xx=60+100*(i+(1 if n==1 else .5));yy=360-100*(j+(1 if n==1 else .5));out.append(f'<circle cx="{xx}" cy="{yy}" r="4" fill="#168264"/><text x="{xx+5}" y="{yy-7}" font-size="14">{val}</text>')
 out.append('<text x="50" y="418" font-size="12">Sample values only; not exact contour reconstruction.</text></svg>')
 name=f's15-10-{n}.svg';(R/'exercise-content/assets'/name).write_text('\n'.join(out));attach(items[n],name,('등고선 판독값을 표시한 표본점','Sample points with approximate contour readings'),('원본 등고선에서 읽은 표본값의 자체 도해','Original diagram of sample readings from the source contours'))
def mapping(a,b,c):
 th=math.pi*a/2;ph=math.pi*b/6;rr=2*c*math.cos(ph);return rr*math.sin(ph)*math.cos(th),rr*math.sin(ph)*math.sin(th),rr*math.cos(ph)
solid('s15-10-16.svg','Sphere sector inside a cone',mapping,axes=(1,1,2),subtitle='x,y >= 0; x²+y²+(z-1)² <= 1; phi <= pi/6')
attach(items[16],'s15-10-16.svg',('구와 원뿔이 제한하는 입체','Solid constrained by a sphere and cone'),('주어진 구면좌표 경계로 생성한 자체 도해','Original diagram generated from the spherical bounds'))
# Wireframe graph z=x sin y, with all gridlines in one projection.
def proj(x,y,z):return 300+46*(.8*x+.6*y),220+46*(.25*x-.3*y-.8*z)
out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 460"><rect width="600" height="460" fill="#f8fafc"/><text x="25" y="30" font-size="20">z = x sin y</text>']
for fixed in range(17):
 for family in (0,1):
  pts=[]
  for i in range(101):
   x=-3+6*(fixed/16 if family==0 else i/100);y=-math.pi+2*math.pi*(i/100 if family==0 else fixed/16);q=proj(x,y,x*math.sin(y));pts.append(f'{q[0]:.2f},{q[1]:.2f}')
  out.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="'+('#3b82a6'if family==0 else'#946bb3')+'" stroke-width="1"/>')
for j,l in enumerate('xyz'):
 v=[0,0,0];v[j]=3.4;ox,oy=proj(0,0,0);xx,yy=proj(*v);out.append(f'<path d="M{ox},{oy}L{xx},{yy}" stroke="#475569"/><text x="{xx}" y="{yy}" font-size="15">{l}</text>')
out.append('<text x="25" y="435" font-size="14">-3 ≤ x ≤ 3; -pi ≤ y ≤ pi</text></svg>')
name='s15-10-46.svg';(R/'exercise-content/assets'/name).write_text('\n'.join(out));attach(items[46],name,('z=x sin y의 곡면','Surface z=x sin y'),('고정 x와 고정 y의 격자선을 표시한 자체 그래프','Original graph with constant-x and constant-y grid curves'))
(R/'exercise-content/s15-10.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('Chapter15 Review:4 original SVG diagrams linked')
