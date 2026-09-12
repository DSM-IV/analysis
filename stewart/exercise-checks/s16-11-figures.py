import math,json
from pathlib import Path
R=Path(__file__).resolve().parents[1];out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 700"><rect width="1000" height="700" fill="#f8fafc"/><text x="25" y="30" font-size="19">(sin u, sin v, sin(u+v)): views and horizontal traces</text>']
for panel,angle in enumerate((.5,1.8,3.0)):
 cx=170+panel*330;cy=185
 def proj(x,y,z):return(cx+93*(math.cos(angle)*x-math.sin(angle)*y),cy+93*(.35*math.sin(angle)*x+.35*math.cos(angle)*y-.8*z))
 for k in range(29):
  for family in(0,1):
   pts=[]
   for j in range(97):
    u=2*math.pi*(k/28 if family==0 else j/96);v=2*math.pi*(j/96 if family==0 else k/28);x,y=proj(math.sin(u),math.sin(v),math.sin(u+v));pts.append(f'{x:.2f},{y:.2f}')
   color='#3b82a6'if family==0 else'#a36f9d';out.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-opacity=".55" stroke-width=".65"/>')
 out.append(f'<text x="{cx-28}" y="345" font-size="14">View {panel+1}</text>')
for j,c in enumerate((0,1,.5)):
 cx=170+j*330;cy=520;scale=105
 out.append(f'<path d="M{cx-125},{cy}H{cx+125} M{cx},{cy-125}V{cy+125}" stroke="#cbd5e1"/>')
 for w,col in [(math.asin(c),'#1d7e65'),(math.pi-math.asin(c),'#b56b3d')]:
  pts=[]
  for i in range(201):
   u=2*math.pi*i/200;x=math.sin(u);y=math.sin(w-u);pts.append(f'{cx+scale*x:.2f},{cy-scale*y:.2f}')
  out.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="2"/>')
 out.append(f'<text x="{cx-40}" y="668" font-size="17">z = '+('0'if c==0 else'±1'if c==1 else'±1/2')+'</text>')
out.append('</svg>');name='s16-11-4.svg';(R/'exercise-content/assets'/name).write_text('\n'.join(out))
p=R/'exercise-content/s16-11.json';d=json.loads(p.read_text());d['exercises'][3]['figure']={'src':'../exercise-content/assets/'+name,'alt':{'ko':'매개곡면의 세 시점과 세 높이의 자취','en':'Three views of the parametric surface and traces at three heights'},'caption':{'ko':'위: 자체 격자 도해. 아래: 높이별 선분, 원, 타원 두 개.','en':'Top: original wireframes. Bottom: diagonal segments, a circle, and a pair of ellipses.'}};p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print('Linked original three-view and trace diagram')
