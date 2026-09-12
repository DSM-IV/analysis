import math,json
from pathlib import Path
r=(Path(__file__).resolve().parents[1]/'exercise-content');d=json.loads((r/'s16-6.json').read_text())
for n in[37,38]:
 if n==37:
  surf=lambda u,v:(u*u,2*u*math.sin(v),u*math.cos(v));dom=(0,1.5,-math.pi,math.pi);plane=lambda u,v:(u,v,(u+1)/2);pd=(.1,2.1,-1.5,1.5);P=(1,0,1);title='x - 2z = -1'
 else:
  surf=lambda u,v:(1-u*u-v*v,-v,-u);dom=(-1.5,1.5,-1.5,1.5);plane=lambda u,v:(3+2*u+2*v,u,v);pd=(-1.5,-.5,-1.5,-.5);P=(-1,-1,-1);title='x - 2y - 2z = 3'
 def proj(p):
  x,y,z=p;return(.866*x-.5*y,.3*x+.52*y-.8*z)
 lines=[]
 for f,bounds,plane_flag in[(surf,dom,False),(plane,pd,True)]:
  for fam in[0,1]:
   for i in range(13 if not plane_flag else 7):
    pts=[];den=12 if not plane_flag else 6
    for j in range(81):
     a=i/den;b=j/80;u=bounds[0]+(bounds[1]-bounds[0])*(a if fam==0 else b);v=bounds[2]+(bounds[3]-bounds[2])*(b if fam==0 else a);pts.append(proj(f(u,v)))
    lines.append((['#0284c7','#9333ea'][fam] if not plane_flag else '#d97706',pts))
 allpts=[p for c,ps in lines for p in ps];mn=[min(p[k]for p in allpts)for k in[0,1]];mx=[max(p[k]for p in allpts)for k in[0,1]];sc=min(650/(mx[0]-mn[0]),310/(mx[1]-mn[1]))
 def xy(p):return(380+(p[0]-(mx[0]+mn[0])/2)*sc,215+(p[1]-(mx[1]+mn[1])/2)*sc)
 ss=['<svg xmlns="http://www.w3.org/2000/svg" width="760" height="460" viewBox="0 0 760 460"><rect width="100%" height="100%" fill="#f8fafc"/>',f'<text x="380" y="27" text-anchor="middle" font-family="sans-serif" font-size="18">Surface and tangent plane: {title}</text>']
 corners=[xy(proj(plane(u,v)))for u,v in[(pd[0],pd[2]),(pd[1],pd[2]),(pd[1],pd[3]),(pd[0],pd[3])]];ss.append('<polygon points="'+' '.join(f'{x:.2f},{y:.2f}'for x,y in corners)+'" fill="#fbbf24" opacity=".16"/>')
 for c,ps in lines:ss.append('<polyline points="'+' '.join(f'{xy(p)[0]:.2f},{xy(p)[1]:.2f}'for p in ps)+f'" fill="none" stroke="{c}" stroke-width="1" opacity=".7"/>')
 x,y=xy(proj(P));ss.append(f'<circle cx="{x}" cy="{y}" r="4.5" fill="#dc2626"/><text x="{x+8}" y="{y-8}" font-family="sans-serif" font-size="14" fill="#b91c1c">P{P}</text>')
 ss.append('<text x="25" y="417" fill="#0284c7" font-family="sans-serif" font-size="14">Surface: blue u constant, purple v constant</text><text x="25" y="441" fill="#d97706" font-family="sans-serif" font-size="14">Orange: tangent plane; red: point of contact</text>')
 for name,dx,dy in[('x',26,9),('y',-15,16),('z',0,-24)]:ss.append(f'<path d="M695,420l{dx},{dy}" stroke="#475569"/><text x="{695+dx}" y="{417+dy}" font-family="sans-serif" font-size="12">{name}</text>')
 ss.append('</svg>');(r/f'assets/s16-6-{n}.svg').write_text(''.join(ss));d['exercises'][n-1]['figure']['caption']={'ko':'곡면과 접평면을 같은 좌표계에 표시했다. 파랑·보라: 곡면 격자, 주황: 접평면, 빨강: 접점.','en':'Surface and tangent plane share one coordinate frame. Blue/purple: surface grid; orange: tangent plane; red: point of contact.'}
(r/'s16-6.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+chr(10))
