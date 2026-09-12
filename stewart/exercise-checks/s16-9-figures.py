"""Generate original vector plots using standard SVG geometry."""
from pathlib import Path
import math
A=Path(__file__).resolve().parents[1]/'exercise-content/assets';A.mkdir(exist_ok=True)
def base(title):return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 480"><rect width="640" height="480" fill="white"/><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10Z" fill="#2563eb"/></marker></defs>',f'<text x="25" y="30" font-family="sans-serif" font-size="19">{title}</text>']
def arrow(out,a,b):out.append(f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arrow)"/>')
for n in [22,23,24]:
 title={22:'F = (x, y²)',23:'F = (xy, x + y²)',24:'F = (x², y²)'}[n];out=base(title)
 p=lambda x,y:(320+90*x,255-90*y)
 for i in range(-5,6):
  for j in range(-5,6):
   x=i*.4;y=j*.4
   u,v=(x,y*y) if n==22 else (x*y,x+y*y) if n==23 else (x*x,y*y)
   norm=math.hypot(u,v);scale=.2/(1+norm*.5)
   if norm>1e-9:arrow(out,p(x,y),p(x+scale*u,y+scale*v))
 for a,b in [((-2.4,0),(2.4,0)),((0,-2.3),(0,2.3))]:
  x,y=p(*a);xx,yy=p(*b);out.append(f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" stroke="#64748b"/>')
 if n==22:
  for name,x,y in [('P1',-.6,1.5),('P2',-.6,-1)]:
   u,v=p(x,y);out.append(f'<circle cx="{u}" cy="{v}" r="5" fill="#e11d48"/><text x="{u+7}" y="{v-7}" font-family="sans-serif">{name}</text>')
 boundary=((-2.2,0),(2.2,0)) if n==23 else ((-2,2),(2,-2)) if n==24 else ((-2.2,-.5),(2.2,-.5))
 x,y=p(*boundary[0]);xx,yy=p(*boundary[1]);out.append(f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" stroke="#059669" stroke-dasharray="5 5"/><text x="24" y="462" font-family="sans-serif" font-size="13">Green dashed line: divergence = 0. Arrow lengths compressed for clarity.</text></svg>')
 (A/f's16-9-{n}.svg').write_text(''.join(out))
out=base('F = (sin x cos²y, sin³y cos⁴z, sin⁵z cos⁶x)')
p=lambda x,y,z:(315+125*(x-.7*y),350+125*(.25*x+.35*y-z))
for i in range(5):
 for j in range(5):
  for k in range(5):
   x,y,z=[q*math.pi/8 for q in (i,j,k)]
   u=math.sin(x)*math.cos(y)**2;v=math.sin(y)**3*math.cos(z)**4;w=math.sin(z)**5*math.cos(x)**6
   if u*u+v*v+w*w>1e-12:arrow(out,p(x,y,z),p(x+.22*u,y+.22*v,z+.22*w))
for e,label in [((1.9,0,0),'x'),((0,1.9,0),'y'),((0,0,1.9),'z')]:
 a=p(0,0,0);b=p(*e);out.append(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#334155"/><text x="{b[0]}" y="{b[1]-8}" font-family="sans-serif">{label}</text>')
out.append('<text x="24" y="460" font-family="sans-serif" font-size="14">0 ≤ x, y, z ≤ π/2; original sampled vector plot</text></svg>')
(A/'s16-9-18.svg').write_text(''.join(out))
