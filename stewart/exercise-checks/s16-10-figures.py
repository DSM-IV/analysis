from pathlib import Path
import math
A=Path(__file__).resolve().parents[1]/'exercise-content/assets';A.mkdir(exist_ok=True)
def svg(n):
 out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 480"><rect width="720" height="480" fill="white"/>']
 p=(lambda x,y,z:(350+100*(x-.6*y),270+35*x+40*y-80*z)) if n==24 else (lambda x,y,z:(315+20*(x-.6*y),300+10*x+7*y-20*z))
 def line(pts,col='#2563eb',w=1):
  q=' '.join(f'{a:.2f},{b:.2f}' for a,b in [p(*pt) for pt in pts]);out.append(f'<polyline points="{q}" fill="none" stroke="{col}" stroke-width="{w}"/>')
 if n==24:
  out.append('<text x="24" y="30" font-family="sans-serif" font-size="19">Review 24: z = y, x² + y² = 1</text>')
  for u in [-1,-.5,0,.5,1]:line([(u,-1,-1),(u,1,1)],'#cbd5e1');line([(-1,u,u),(1,u,u)],'#cbd5e1')
  line([(math.cos(t*math.pi/90),math.sin(t*math.pi/90),math.sin(t*math.pi/90)) for t in range(181)],'#059669',3)
  ends=[((1.6,0,0),'x'),((0,1.6,0),'y'),((0,0,1.6),'z')]
 else:
  out.append('<text x="24" y="30" font-family="sans-serif" font-size="19">Review 26: r(u,v) = (v², -uv, u²)</text>')
  for i in range(13):
   u=i/4;line([(v*v,-u*v,u*u) for v in [-3+j/20 for j in range(121)]])
  for i in range(25):
   v=-3+i/4;line([(v*v,-u*v,u*u) for u in [j/30 for j in range(91)]])
  for xx in [0,2,4,6,8]:line([(xx,-xx/4-zz,zz) for zz in [i/10 for i in range(31)]],'#d97706')
  for zz in [0,1,2,3]:line([(xx,-xx/4-zz,zz) for xx in [i/10 for i in range(81)]],'#d97706')
  x,y=p(4,-2,1);out.append(f'<circle cx="{x}" cy="{y}" r="5" fill="#dc2626"/><text x="{x+7}" y="{y-9}" font-family="sans-serif">(4,-2,1)</text>')
  out.append('<text x="24" y="458" font-family="sans-serif" font-size="14">Blue: surface. Orange: tangent plane x + 4y + 4z = 0.</text>')
  ends=[((12,0,0),'x'),((0,12,0),'y'),((0,0,12),'z')]
 for e,label in ends:
  line([(0,0,0),e],'#64748b');x,y=p(*e);out.append(f'<text x="{x+6}" y="{y-5}" font-family="sans-serif">{label}</text>')
 out.append('</svg>');(A/f's16-10-{n}.svg').write_text(''.join(out))
for n in [24,26]:svg(n)
