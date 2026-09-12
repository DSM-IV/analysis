"""Original SVG wireframes from the stated equations; no source images copied."""
from pathlib import Path
import math
A=Path(__file__).resolve().parents[1]/'exercise-content/assets';A.mkdir(exist_ok=True)
def diagram(n):
 R=3 if n==15 else 1
 f=(lambda x,y:1-x-y) if n==15 else (lambda x,y:y*y-x*x)
 zlo,zhi=((1-3*math.sqrt(2),1+3*math.sqrt(2)) if n==15 else (-1,1))
 scale=57/R
 def p(x,y,z):return 340+scale*(x-.65*y),245+scale*(.35*x+.45*y-.65*z)
 lines=[]
 def line(points,color,width=1,opacity=.7):
  q=' '.join(f'{a:.2f},{b:.2f}' for a,b in [p(*q) for q in points]); lines.append(f'<polyline points="{q}" fill="none" stroke="{color}" stroke-width="{width}" opacity="{opacity}"/>')
 ts=[i*2*math.pi/120 for i in range(121)]
 for z in [zlo+(zhi-zlo)*i/5 for i in range(6)]:line([(R*math.cos(t),R*math.sin(t),z) for t in ts],'#9ca3af')
 for t in ts[::10]:line([(R*math.cos(t),R*math.sin(t),zlo),(R*math.cos(t),R*math.sin(t),zhi)],'#9ca3af')
 for i in range(-8,9):
  v=R*i/8; a=math.sqrt(max(0,R*R-v*v));us=[-a+2*a*j/60 for j in range(61)]
  line([(u,v,f(u,v)) for u in us],'#3975b8');line([(v,u,f(v,u)) for u in us],'#3975b8')
 line([(R*math.cos(t),R*math.sin(t),f(R*math.cos(t),R*math.sin(t))) for t in ts],'#059669',3,1)
 for end,label in [((R*1.6,0,0),'x'),((0,R*1.6,0),'y'),((0,0,zhi*1.3),'z')]:
  line([(0,0,0),end],'#334155',1,1);x,y=p(*end);lines.append(f'<text x="{x+7}" y="{y}" font-family="sans-serif" font-size="15">{label}</text>')
 eq='z = 1 - x - y; x² + y² = 9' if n==15 else 'z = y² - x²; x² + y² = 1'
 svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 460" role="img"><rect width="680" height="460" fill="white"/><text x="24" y="30" font-family="sans-serif" font-size="19">'+eq+'</text>'+''.join(lines)+'</svg>'
 (A/f's16-8-{n}.svg').write_text(svg)
for n in (15,16):diagram(n)
