import json,math,html
from pathlib import Path
from math import sin,cos,pi,sqrt,sinh,cosh
root=(Path(__file__).resolve().parents[1]/'exercise-content');d=json.loads((root/'s16-6.json').read_text())
plots={7:[(lambda u,v:(u*u,v*v,u+v),(-1,1),(-1,1),'u, v')],8:[(lambda u,v:(u,v**3,-v),(-2,2),(-2,2),'u, v')],9:[(lambda u,v:(u**3,u*sin(v),u*cos(v)),(-1,1),(0,2*pi),'u, v')],10:[(lambda u,v:(u,sin(u+v),sin(v)),(-pi,pi),(-pi,pi),'u, v')],11:[(lambda u,v:(sin(v),cos(u)*sin(4*v),sin(2*u)*sin(4*v)),(0,2*pi),(-pi/2,pi/2),'u, v')],12:[(lambda u,v:(cos(u),sin(u)*sin(v),cos(v)),(0,2*pi),(0,2*pi),'u, v')],13:[(lambda u,v:(u*cos(v),u*sin(v),v),(0,2),(0,4*pi),'IV')],14:[(lambda u,v:(u*v*v,u*u*v,u*u-v*v),(-1,1),(-1,1),'VI')],15:[(lambda u,v:(u**3-u,v*v,u*u),(-1.3,1.3),(0,1.5),'I')],16:[(lambda u,v:((1-u)*(3+cos(v))*cos(4*pi*u),(1-u)*(3+cos(v))*sin(4*pi*u),3*u+(1-u)*sin(v)),(0,1),(0,2*pi),'V')],17:[(lambda u,v:(cos(u)**3*cos(v)**3,sin(u)**3*cos(v)**3,sin(v)**3),(0,2*pi),(-pi/2,pi/2),'III')],18:[(lambda u,v:(sin(u),cos(u)*sin(v),sin(v)),(0,2*pi),(-pi/2,pi/2),'II')],27:[(lambda u,v:(u,-3*sin(v),3*cos(v)),(0,5),(0,pi),'Half-cylinder')],28:[(lambda u,v:(sin(u)*cos(v),sin(u)*sin(v),cos(u)),(pi/4,pi),(0,2*pi),'Truncated sphere')],29:[(lambda u,v:(u,cos(v)/(1+u*u),sin(v)/(1+u*u)),(-2,2),(0,2*pi),'Revolution about x')],30:[(lambda u,v:(cos(v)/u,u,sin(v)/u),(1,6),(0,2*pi),'Revolution about y')],31:[(lambda u,v:((2+sin(v))*sin(u),(2+sin(v))*cos(u),u+cos(v)),(0,4*pi),(0,2*pi),'(a) Reflected'),(lambda u,v:((2+sin(v))*cos(2*u),(2+sin(v))*sin(2*u),u+cos(v)),(0,4*pi),(0,2*pi),'(b) Double turns')],32:[(lambda u,v:(2*cos(v)+u*cos(v/2),2*sin(v)+u*cos(v/2),u*sin(v/2)),(-.5,.5),(0,2*pi),'View 1'),(lambda u,v:(2*cos(v)+u*cos(v/2),2*sin(v)+u*cos(v/2),u*sin(v/2)),(-.5,.5),(0,2*pi),'View 2')],37:[(lambda u,v:(u*u,2*u*sin(v),u*cos(v)),(0,1.5),(-pi,pi),'Surface'),(lambda u,v:(u,v,(u+1)/2),(0,2.25),(-2,2),'Tangent x - 2z = -1')],38:[(lambda u,v:(1-u*u-v*v,-v,-u),(-1.5,1.5),(-1.5,1.5),'Surface'),(lambda u,v:(3+2*u+2*v,u,v),(-1.5,.2),(-1.5,.2),'Tangent x - 2y - 2z = 3')],54:[(lambda u,v:(u*(1-abs(v)),v,(1+u*u*(1-abs(v))**2)/(1+v*v)),(-1,1),(-1,1),'Diamond domain')],58:[(lambda u,v:(2*u*cos(v),3*u*sin(v),u*u),(0,2),(0,2*pi),'a=2, b=3')],59:[(lambda u,v:(sin(u)*cos(v),2*sin(u)*sin(v),3*cos(u)),(0,pi),(0,2*pi),'a=1, b=2, c=3')],60:[(lambda u,v:(cosh(u)*cos(v),2*cosh(u)*sin(v),3*sinh(u)),(-math.asinh(1),math.asinh(1)),(0,2*pi),'a=1, b=2, c=3')],64:[]}
for a,b in[(.5,2),(1,2),(1.5,2)]:plots[64].append((lambda u,v,a=a,b=b:((b+a*cos(v))*cos(u),(b+a*cos(v))*sin(u),a*sin(v)),(0,2*pi),(0,2*pi),f'a={a}, b={b}'))
def svgplot(items,n):
 w=440;H=390;out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w*len(items)}" height="{H}" viewBox="0 0 {w*len(items)} {H}">',f'<rect width="100%" height="100%" fill="#f8fafc"/>']
 for idx,(f,ur,vr,label) in enumerate(items):
  ang=.75 if not(n==32 and idx==1) else 2.3
  def proj(p):
   x,y,z=p;return ((x*cos(ang)-y*sin(ang)),.35*(x*sin(ang)+y*cos(ang))-.94*z)
  lines=[]
  for fam in [0,1]:
   for i in range(13):
    pts=[]
    for j in range(81):
     t=i/12;s=j/80;u=ur[0]+(ur[1]-ur[0])*(t if fam==0 else s);v=vr[0]+(vr[1]-vr[0])*(s if fam==0 else t);pts.append(proj(f(u,v)))
    lines.append((fam,pts))
  allp=[p for _,pts in lines for p in pts];mx=[min(p[k] for p in allp) for k in [0,1]];M=[max(p[k] for p in allp) for k in[0,1]];sc=min(355/(M[0]-mx[0] or 1),270/(M[1]-mx[1] or 1))
  def xy(p):return idx*w+220+(p[0]-(mx[0]+M[0])/2)*sc,185+(p[1]-(mx[1]+M[1])/2)*sc
  out.append(f'<text x="{idx*w+220}" y="25" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#14243a">{html.escape(label)}</text>')
  for fam,pts in lines:
   ps=' '.join(f'{xy(p)[0]:.2f},{xy(p)[1]:.2f}'for p in pts);out.append(f'<polyline points="{ps}" fill="none" stroke="{["#0284c7","#9333ea"][fam]}" stroke-width="1" opacity=".75"/>')
  out.append(f'<text x="{idx*w+22}" y="357" font-family="sans-serif" font-size="13" fill="#0284c7">First parameter constant</text><text x="{idx*w+22}" y="377" font-family="sans-serif" font-size="13" fill="#9333ea">Second parameter constant</text>')

 for idx in range(len(items)):
  ang=.75 if not(n==32 and idx==1) else 2.3
  ox=idx*440+380;oy=355
  for name,dx,dy in [('x',28*cos(ang),10*sin(ang)),('y',-28*sin(ang),10*cos(ang)),('z',0,-24)]:
   out.append(f'<path d="M{ox},{oy}l{dx},{dy}" fill="none" stroke="#475569"/><text x="{ox+dx}" y="{oy+dy-3}" font-family="sans-serif" font-size="11" fill="#475569">{name}</text>')
 out.append('</svg>');return ''.join(out)
for ex in d['exercises']:
 n=ex['number']
 if n in plots:
  fn=f's16-6-{n}.svg';(root/'assets'/fn).write_text(svgplot(plots[n],n));ex['figure']={'src':'../exercise-content/assets/'+fn,'alt':{'ko':f'16.6 {n}번의 자체 제작 매개곡면 격자 그림','en':f'Original parametric wireframe for Exercise 16.6.{n}'},'caption':{'ko':'파랑: 첫 매개변수 일정, 보라: 둘째 매개변수 일정. 경계와 접힘을 확인하는 투영 그림.','en':'Blue: first parameter constant; purple: second parameter constant. Projected views show boundaries and folds.'}}
(root/'s16-6.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+chr(10))
