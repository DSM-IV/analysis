from pathlib import Path
import math,json,html
R=Path(__file__).resolve().parents[1];p=R/'exercise-content/s12-4.json';d=json.loads(p.read_text());A=R/'exercise-content/assets'
def draw(n,title,segments,points=[]):
 def proj(v):return(v[0],-v[1])if len(v)==2 else(.8*v[0]-.6*v[1],.36*v[0]+.48*v[1]-.8*v[2])
 ps=[proj(v)for a,b,l in segments for v in(a,b)];xx=[v[0]for v in ps];yy=[v[1]for v in ps];xmin,xmax=min(xx),max(xx);ymin,ymax=min(yy),max(yy);sc=min(350/max(xmax-xmin,1),250/max(ymax-ymin,1))
 def xy(v):x,y=proj(v);return(250+(x-(xmin+xmax)/2)*sc,205+(y-(ymin+ymax)/2)*sc)
 out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 390"><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10Z" fill="context-stroke"/></marker></defs><rect width="500" height="390" fill="#f8fafc"/>',f'<text x="250" y="28" text-anchor="middle" font-family="sans-serif" font-size="17">{html.escape(title)}</text>']
 for i,(a,b,l)in enumerate(segments):
  x,y=xy(a);u,v=xy(b);color=['#0284c7','#9333ea','#c2410c','#64748b'][i%4];out.append(f'<path d="M{x},{y}L{u},{v}" stroke="{color}" stroke-width="2" marker-end="url(#arr)"/><text x="{(x+u)/2+9}" y="{(y+v)/2-8}" fill="{color}" font-family="sans-serif" font-size="15">{html.escape(l)}</text>')
 for a,l in points:
  x,y=xy(a);out.append(f'<circle cx="{x}" cy="{y}" r="3" fill="#0f172a"/><text x="{x+6}" y="{y+17}" font-family="sans-serif">{html.escape(l)}</text>')
 out.append('</svg>');(A/f's12-4-{n}.svg').write_text(''.join(out));d['exercises'][n-1]['figure']={'src':f'../exercise-content/assets/s12-4-{n}.svg','alt':{'ko':f'12.4 {n}번 조건 도해','en':f'Exercise12.4.{n} configuration'},'caption':{'ko':'주어진 방향과 기하 조건에 따라 직접 제작한 도해. 공간벡터는 평면에 사영했다.','en':'Original illustration of the stated directions and geometry; spatial vectors are projected into the image plane.'}}
draw(8,'a, b, and their cross product',[((0,0,0),(1,0,-2),'a'),((0,0,0),(0,1,1),'b'),((0,0,0),(2,-1,1),'a x b')],[((0,0,0),'O')])
draw(14,'Cross product points into the page',[((0,0),(10*math.sin(math.pi/3),-5),'u:10'),((0,0),(0,-8),'v:8')])
draw(15,'Translate v to a common tail',[((0,0),(4,0),'u:4'),((4,0),(4+3*math.cos(math.pi/6),-1.5),'v:3'),((0,0),(3*math.cos(math.pi/6),-1.5),'translated v')])
draw(16,'a in xy, b along positive z',[((0,0,0),(3/math.sqrt(2),3/math.sqrt(2),0),'a'),((0,0,0),(0,0,2),'b'),((0,0,0),(3*math.sqrt(2),-3*math.sqrt(2),0),'a x b')])
foot=(1,1+3*math.tan(math.pi/18));pivot=(4,1);tip=(foot[0]-1.8*math.cos(math.radians(70)),foot[1]-1.8*math.sin(math.radians(70)))
draw(39,'Pedal arm and applied force',[((4,1),foot,'r:18cm'),(foot,tip,'F:60N')],[(pivot,'P')])
draw(40,'Horizontal force; lever arms are heights',[((0,0),(.6,.6),'elbow'),((.6,.6),(1,2),'handle'),((1,2),(2,2),'20lb'),((.6,.6),(1.6,.6),'20lb alternative')],[((0,0),'P'),((.6,.6),'height0.6ft'),((1,2),'height2ft')])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
