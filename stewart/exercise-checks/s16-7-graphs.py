import json,math
from pathlib import Path
from math import sin,cos,exp,pi,sqrt
root=(Path(__file__).resolve().parents[1]/'exercise-content')
W,H=760,500
# Orthographic projection, all arrows share a fixed scale .065.
def proj(p):
 x,y,z=p;return (380+65*(.866*x-.5*y),360+65*(.22*x+.381*y-.925*z))
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><defs><marker id="arrow" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto"><path d="M0 0L5 2.5L0 5Z" fill="#d97706"/></marker></defs><rect width="100%" height="100%" fill="#f8fafc"/><text x="380" y="30" text-anchor="middle" font-family="sans-serif" font-size="19">Elliptic cylinder and vector field</text>']
for typ in[0,1]:
 for i in range(17):
  pts=[]
  for j in range(81):
   x=-2+4*(i/16 if typ==0 else j/80);t=pi*(j/80 if typ==0 else i/16);pts.append(proj((x,cos(t),2*sin(t))))
  svg.append('<polyline points="'+' '.join(f'{x:.2f},{y:.2f}'for x,y in pts)+'" stroke="'+['#0284c7','#7c3aed'][typ]+'" fill="none" stroke-width=".9" opacity=".65"/>')
for x in[-1.6,-.8,0,.8,1.6]:
 for t in[.2*pi,.35*pi,.5*pi,.65*pi,.8*pi]:
  y=cos(t);z=2*sin(t);f=(sin(x*y*z),x*x*y,z*z*exp(x/5));P=proj((x,y,z));Q=proj((x+.065*f[0],y+.065*f[1],z+.065*f[2]));svg.append(f'<path d="M{P[0]:.2f},{P[1]:.2f}L{Q[0]:.2f},{Q[1]:.2f}" fill="none" stroke="#d97706" stroke-width="1.9" marker-end="url(#arrow)"/>')
O=proj((0,0,0))
for name,p in [('x',(2.8,0,0)),('y',(0,2,0)),('z',(0,0,3))]:
 q=proj(p);svg.append(f'<path d="M{O[0]},{O[1]}L{q[0]},{q[1]}" stroke="#475569" stroke-width="1"/><text x="{q[0]+5}" y="{q[1]}" font-family="sans-serif" font-size="16">{name}</text>')
svg.append('<text x="35" y="455" font-family="sans-serif" font-size="15" fill="#d97706">Orange arrows: F = (sin(xyz), x²y, z² exp(x/5)); common display scale 0.065</text><text x="35" y="480" font-family="sans-serif" font-size="14" fill="#475569">4y² + z² = 4; z ≥ 0; -2 ≤ x ≤ 2. Positive z selects the upward normal.</text></svg>')
(root/'assets/s16-7-36.svg').write_text(''.join(svg));d=json.loads((root/'s16-7.json').read_text());d['exercises'][35]['figure']={'src':'../exercise-content/assets/s16-7-36.svg','alt':{'ko':'위쪽 타원기둥과 동일 비율로 표시한 벡터장 화살표','en':'Upper elliptic cylinder with vector-field arrows using a common scale'},'caption':{'ko':'파랑·보라: 곡면 격자선. 주황: 모든 벡터에 동일한 0.065 배율을 적용한 벡터장.','en':'Blue/purple: surface grid. Orange: field vectors, each using the same display scale 0.065.'}};(root/'s16-7.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+chr(10))
