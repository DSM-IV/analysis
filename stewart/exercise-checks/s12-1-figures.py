from pathlib import Path
import json,math,html
from early_helpers import svg_surface
R=Path(__file__).resolve().parents[1];A=R/'exercise-content/assets';p=R/'exercise-content/s12-1.json';d=json.loads(p.read_text())
def attach(n,cap=('직접 제작한 좌표·곡면 그림. 무한 도형은 표시 범위로 잘랐다.','Original coordinate/surface diagram. Infinite objects are clipped to the display window.')):
 d['exercises'][n-1]['figure']={'src':f'../exercise-content/assets/s12-1-{n}.svg','alt':{'ko':f'12.1 {n}번 도해','en':f'Exercise12.1.{n} diagram'},'caption':{'ko':cap[0],'en':cap[1]}}
for n,items in {
 5:[(lambda u,v:(4,u,0),(-3,3),(0,0),'x=4 in the xy-plane'),(lambda u,v:(4,u,v),(-3,3),(-3,3),'x=4 in space')],
 6:[(lambda u,v:(u,3,v),(-3,3),(-1,6),'y=3'),(lambda u,v:(u,v,5),(-3,3),(-1,6),'z=5'),(lambda u,v:(u,3,5),(-3,3),(0,0),'Intersection: y=3, z=5')],
 7:[(lambda u,v:(u,2-u,v),(-2,4),(-3,3),'x+y=2')],
 8:[(lambda u,v:(3*math.cos(u),v,3*math.sin(u)),(0,2*math.pi),(-4,4),'x^2+z^2=9')],
 52:[([lambda u,v:(u*math.cos(v),u*math.sin(v),2*(1-abs(u*math.sin(v)))),lambda u,v:(u*math.cos(v),u*math.sin(v),0),lambda u,v:(math.cos(v),math.sin(v),2*u*(1-abs(math.sin(v))))],(0,1),(0,2*math.pi),'Disk footprint with a triangular roof')]
}.items():svg_surface(items,A/f's12-1-{n}.svg');attach(n)
def coord(n,points,lines,title):
 def xy(p):x,y,z=p;return(295+30*x-25*y,295+12*x+15*y-30*z)
 s=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 490"><rect width="640" height="490" fill="#f8fafc"/>',f'<text x="320" y="30" text-anchor="middle" font-family="sans-serif" font-size="17">{html.escape(title)}</text>']
 for end,label in [((5,0,0),'x'),((0,6,0),'y'),((0,0,7),'z')]:
  a,b=xy((0,0,0));c,e=xy(end);s.append(f'<path d="M{a},{b}L{c},{e}" stroke="#64748b"/><text x="{c+5}" y="{e}" font-family="sans-serif">{label}</text>')
 for a,b in lines:
  u,v=xy(a);w,z=xy(b);s.append(f'<path d="M{u},{v}L{w},{z}" stroke="#0284c7" fill="none"/>')
 for pt,label in points:
  x,y=xy(pt);s.append(f'<circle cx="{x}" cy="{y}" r="4" fill="#be123c"/><text x="{x+6}" y="{y-7}" font-family="sans-serif" font-size="12">{html.escape(label)}</text>')
 s.append('</svg>');(A/f's12-1-{n}.svg').write_text(''.join(s));attach(n)
pts=[(1,5,3),(0,2,-3),(-3,0,2),(2,-2,-1)]
coord(2,[(v,str(v))for v in pts],[(v,(v[0],v[1],0))for v in pts],'Four points in one coordinate system')
verts=[(x,y,z)for x in(0,2)for y in(0,3)for z in(0,5)]
lines=[(a,b)for i,a in enumerate(verts)for b in verts[i+1:]if sum(x!=y for x,y in zip(a,b))==1]
coord(4,[(v,str(v))for v in verts],lines+[((0,0,0),(2,3,5))],'Box vertices and diagonal')
# Schematic chosen to preserve P and the order of all plane crossings; no numerical A/B/C values are asserted.
coord(47,[((2,1,4),'P=(2,1,4)'),((.5,2.5,0),'A: z=0'),((0,3,-4/3),'B: x=0'),((3,0,20/3),'C: y=0')],[((0,3,-4/3),(3,0,20/3)),((0,3,0),(3,0,0)),((2,1,4),(2,1,0))],'Plane intersections (schematic)')
attach(47,('원본에서 읽은 P의 좌표와 평면 교점의 위치 관계를 나타낸 개략도. A·B·C의 수치 좌표를 제공하는 그림은 아니다.','Schematic preserving the source coordinate of P and the order of the plane crossings; it does not specify numerical coordinates for A,B,C.'))
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
