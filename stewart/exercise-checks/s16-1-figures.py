"""Generate original SVG vector fields; no source artwork is copied."""
import math,json
from pathlib import Path
from html import escape
root=Path(__file__).resolve().parents[1]
assets=root/'exercise-content/assets';assets.mkdir(exist_ok=True)
sin,cos,sqrt,log=math.sin,math.cos,math.sqrt,math.log
fields={1:lambda x,y:(1,.5),2:lambda x,y:(2,-1),3:lambda x,y:(1,y/2),4:lambda x,y:(x,y/2),5:lambda x,y:(-.5,y-x),6:lambda x,y:(y,x+y),7:lambda x,y:(y/sqrt(x*x+y*y),x/sqrt(x*x+y*y)),8:lambda x,y:(y/sqrt(x*x+y*y),-x/sqrt(x*x+y*y)),13:lambda x,y:(x,-y),14:lambda x,y:(y,x-y),15:lambda x,y:(y,y+2),16:lambda x,y:(y,2*x),17:lambda x,y:(sin(y),cos(x)),18:lambda x,y:(cos(x+y),x),23:lambda x,y:((y-2*x)*y,(y-2*x)*3*x),24:lambda x,y:((x*x+y*y-2*sqrt(x*x+y*y))*x,(x*x+y*y-2*sqrt(x*x+y*y))*y),29:lambda x,y:(x-y,y-x),30:lambda x,y:(x,-y),31:lambda x,y:(2*x,2*y),32:lambda x,y:(2*x+y,x),33:lambda x,y:(2*(x+y),2*(x+y)),34:lambda x,y:(cos(sqrt(x*x+y*y))*x/sqrt(x*x+y*y),cos(sqrt(x*x+y*y))*y/sqrt(x*x+y*y)),35:lambda x,y:(2*x/(1+x*x+2*y*y),4*y/(1+x*x+2*y*y)),36:lambda x,y:(-sin(x),-2*cos(y)),39:lambda x,y:(x,-y),40:lambda x,y:(1,x)}
space={9:lambda x,y,z:(1,0,0),10:lambda x,y,z:(z,0,0),11:lambda x,y,z:(-y,0,0),12:lambda x,y,z:(1,0,1),19:lambda x,y,z:(1,2,3),20:lambda x,y,z:(1,2,z),21:lambda x,y,z:(x,y,3),22:lambda x,y,z:(x,y,z)}
def svg(n):
 s=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 620" role="img">',f'<title>Exercise 16.1.{n}: original vector field</title>','<rect width="600" height="620" fill="#fff"/>','<defs><marker id="a" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto"><path d="M0,0 L5,2.5 L0,5" fill="#176db1"/></marker><clipPath id="plot"><rect x="45" y="50" width="510" height="510"/></clipPath></defs>',f'<text x="300" y="28" text-anchor="middle" font-family="sans-serif" font-size="20">16.1 Exercise {n}</text>']
 def line(a,b,col='#176db1',arrow=False):s.append(f'<line x1="{a[0]:.3f}" y1="{a[1]:.3f}" x2="{b[0]:.3f}" y2="{b[1]:.3f}" stroke="{col}" stroke-width="1.5"'+(' marker-end="url(#a)"' if arrow else '')+'/>')
 if n in space:
  project=lambda x,y,z:(300+58*x-42*y,320+24*x+30*y-62*z)
  for xyz,label in [((2.8,0,0),'x'),((0,2.8,0),'y'),((0,0,2.8),'z')]:
   a=project(*xyz);line(project(0,0,0),a,'#777');s.append(f'<text x="{a[0]}" y="{a[1]}" font-family="sans-serif">{label}</text>')
  vals=[-1.6,-.8,0,.8,1.6]
  raw=[((x,y,z),space[n](x,y,z)) for z in vals for y in vals for x in vals]
  mx=max(sqrt(sum(a*a for a in v)) for _,v in raw);scale=.56/mx
  for (x,y,z),v in raw:line(project(x,y,z),project(x+scale*v[0],y+scale*v[1],z+scale*v[2]),arrow=True)
 else:
  span=4 if n in [31,32,33,34,35,36,39,40] else 3
  pt=lambda x,y:(300+250*x/span,305-250*y/span)
  for i in range(-span,span+1):
   line(pt(-span,i),pt(span,i),'#e5eaf0');line(pt(i,-span),pt(i,span),'#e5eaf0')
  line(pt(-span,0),pt(span,0),'#777');line(pt(0,-span),pt(0,span),'#777')
  s.append('<g clip-path="url(#plot)">')
  def curve(points):
   pts=' '.join(f'{pt(x,y)[0]:.2f},{pt(x,y)[1]:.2f}' for x,y in points if abs(x)<=span*1.1 and abs(y)<=span*1.1)
   s.append(f'<polyline points="{pts}" fill="none" stroke="#d16832" stroke-width="1.4"/>')
  if n==35:
   for a in [.6,1.2,1.8,2.4,3,3.6,4.2]:curve([(a*cos(t*math.pi/100),a/sqrt(2)*sin(t*math.pi/100)) for t in range(201)])
  if n==36:
   # Marching squares for exact scalar field, linear interpolation in each cell.
   fun=lambda x,y:cos(x)-2*sin(y)
   for lev in [-2.5,-1.5,-.5,.5,1.5,2.5]:
    for i in range(80):
     for j in range(80):
      x=-span+2*span*i/80;y=-span+2*span*j/80;h=2*span/80
      p=[(x,y),(x+h,y),(x+h,y+h),(x,y+h)];v=[fun(*a)-lev for a in p];cross=[]
      for k in range(4):
       q=(k+1)%4
       if v[k]*v[q]<0:
        t=v[k]/(v[k]-v[q]);cross.append((p[k][0]+t*(p[q][0]-p[k][0]),p[k][1]+t*(p[q][1]-p[k][1])))
      if len(cross)==2:curve(cross)
  if n==39:
   for c in [-4,-2,-1,1,2,4]:
    for sign in [-1,1]:curve([(sign*(.12+k*.035),c/(sign*(.12+k*.035))) for k in range(112)])
  if n==40:
   for c in [-4,-2,0,2]:curve([(-4+k*.025,(-4+k*.025)**2/2+c) for k in range(321)])
  vals=[-span+2*span*i/12 for i in range(13)];raw=[]
  for x in vals:
   for y in vals:
    try:v=fields[n](x,y)
    except ZeroDivisionError:continue
    raw.append(((x,y),v))
  mx=max(sqrt(sum(a*a for a in v)) for _,v in raw)
  for (x,y),(u,v) in raw:
   mag=sqrt(u*u+v*v)
   if mag<1e-9:s.append(f'<circle cx="{pt(x,y)[0]}" cy="{pt(x,y)[1]}" r="1.4" fill="#555"/>');continue
   scale=span*.12/mx
   line(pt(x,y),pt(x+scale*u,y+scale*v),arrow=True)
  s.append('</g>')
  s.append(f'<text x="555" y="325" font-family="sans-serif">x</text><text x="310" y="53" font-family="sans-serif">y</text><text x="45" y="580" font-family="sans-serif">Domain: [-{span}, {span}] × [-{span}, {span}]</text>')
 s.append('<text x="300" y="605" text-anchor="middle" font-size="13" font-family="sans-serif">Blue: vectors (one common scale). Orange: contours / streamlines.</text></svg>')
 return '\n'.join(s)
p=root/'exercise-content/s16-1.json';doc=json.loads(p.read_text())
for e in doc['exercises']:
 n=e['number']
 if n in fields or n in space:
  name=f's16-1-{n}.svg';(assets/name).write_text(svg(n));e['figure']={'src':'../exercise-content/assets/'+name,'alt':{'ko':f'16.1 {n}번의 자체 벡터장 그림','en':f'Original vector-field diagram for exercise 16.1.{n}'},'caption':{'ko':'파랑은 동일 축척의 벡터. 주황은 해당 문항의 등위선 또는 유선.','en':'Blue vectors use a common scale. Orange curves are contours or streamlines where applicable.'}}
p.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
print('Generated',len(fields)+len(space),'SVG figures')
