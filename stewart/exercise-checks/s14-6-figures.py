import json,math
from pathlib import Path
R=Path(__file__).resolve().parents[1];A=R/'exercise-content/assets';p=R/'exercise-content/s14-6.json';D=json.loads(p.read_text())
def base(title):return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 560"><defs><marker id="a" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6" fill="#bf342e"/></marker></defs><rect width="800" height="560" fill="white"/>',f'<text x="400" y="30" text-anchor="middle" font-family="sans-serif" font-size="18">{title}</text>']
def path(out,pts,col='#3875ad',width=1):out.append('<polyline points="'+' '.join(f'{a:.2f},{b:.2f}' for a,b in pts)+f'" fill="none" stroke="{col}" stroke-width="{width}"/>')
def arrow(out,a,b):out.append(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#bf342e" stroke-width="3" marker-end="url(#a)"/>')
def save(n,out,ko,en):
 out.append('</svg>');name=f's14-6-{n}.svg';(A/name).write_text('\n'.join(out));next(e for e in D['exercises'] if e['number']==n)['figure']=dict(src='../exercise-content/assets/'+name,alt=dict(ko=ko,en=en),caption=dict(ko=ko,en=en))
for n,labels in [(26,[('P',180,260,-65,-65),('Q',400,260,65,65),('R',620,260,-65,-65)]),(44,[('(4,6)',400,260,45,90)])]:
 out=base('Gradient directions: schematic local contours')
 for label,cx,cy,dx,dy in labels:
  for k in [-2,-1,0,1,2]:path(out,[(cx-dy*.7+k*dx/4,cy+dx*.7+k*dy/4),(cx+dy*.7+k*dx/4,cy-dx*.7+k*dy/4)])
  arrow(out,(cx,cy),(cx+dx,cy+dy));out.append(f'<text x="{cx+8}" y="{cy-8}" font-size="18">{label}</text>')
 save(n,out,'국소 등고선에 수직이고 값이 증가하는 방향의 기울기 화살표 개략도.','Schematic gradient arrows normal to local contours toward increasing values.')
out=base('Steepest descent: perpendicular contour crossings')
for center in [(260,300),(610,290)]:
 for rr in [55,90,125,160]:
  out.append(f'<ellipse cx="{center[0]}" cy="{center[1]}" rx="{rr}" ry="{rr*.8}" fill="none" stroke="#84936b"/>')
path(out,[(195,260),(170,230),(158,200),(165,163),(196,132)],'#bf342e',3);arrow(out,(165,163),(196,132));out.append('<ellipse cx="206" cy="112" rx="45" ry="20" fill="#add8ef"/><text x="174" y="116">Mud Lake</text><text x="195" y="280">A</text>')
path(out,[(540,325),(512,347),(480,370),(440,395)],'#bf342e',3);arrow(out,(480,370),(440,395));out.append('<text x="545" y="322">B</text><text x="395" y="430">Lower valley</text>');save(42,out,'최급하강 경로의 개략도. 지리적 지도 재구성이 아닌 방향 원리 도해.','Schematic descent paths illustrating the principle, not a geographic reconstruction.')
for n in [53,54,76]:
 out=base('Surface (blue), tangent plane (orange), normal (red)' if n!=76 else 'Real cube-root surface z = cbrt(xy)')
 if n==53:bx,by,bz=1,1,1;fn=lambda x,y:(3-x*y)/(x+y);pn=lambda x,y:3-x-y;N=(1,1,1);sc=.65
 elif n==54:bx,by,bz=1,2,3;fn=lambda x,y:6/(x*y);pn=lambda x,y:(18-6*x-3*y)/2;N=(6,3,2);sc=.6
 else:bx=by=bz=0;fn=lambda x,y:math.copysign(abs(x*y)**(1/3),x*y);pn=None;sc=1
 project=lambda x,y,z:(400+130*(x-bx)/sc-90*(y-by)/sc,290+40*(x-bx)/sc+40*(y-by)/sc-70*(z-bz))
 for fun,col in [(fn,'#3875ad')]+([(pn,'#df9138')] if pn else []):
  for i in range(21):
   c=-sc+2*sc*i/20
   for sw in [False,True]:
    pts=[]
    for j in range(61):
     d=-sc+2*sc*j/60;xx=bx+(c if sw else d);yy=by+(d if sw else c);pts.append(project(xx,yy,fun(xx,yy)))
    path(out,pts,col)
 if pn:nn=math.sqrt(sum(a*a for a in N));path(out,[project(bx+k*N[0]/nn,by+k*N[1]/nn,bz+k*N[2]/nn) for k in [-.7,.7]],'#bf342e',3)
 save(n,out,'함수에서 직접 계산한 곡면 도해'+('와 접평면·법선.' if pn else '.'),'Surface computed directly from the function'+(' with tangent plane and normal.' if pn else '.'))
for n in [55,56]:
 out=base('Level curve (blue), tangent (orange), gradient (red)');proj=lambda x,y:(160+100*x,440-100*y)
 if n==55:
  path(out,[proj(xx,6/xx) for xx in [1.6+i*.05 for i in range(69)]]);P=(3,2);G=(2,3);T=(-3,2)
 else:
  path(out,[proj(2+math.sqrt(5)*math.cos(i*math.pi/100),math.sqrt(5)*math.sin(i*math.pi/100)) for i in range(201)]);P=(1,2);G=(-2,4);T=(2,1)
 path(out,[proj(P[0]+a*T[0],P[1]+a*T[1]) for a in [-.5,.5]],'#df9138',2);arrow(out,proj(*P),proj(P[0]+.35*G[0],P[1]+.35*G[1]));save(n,out,'등위곡선, 그 접선, 기준점의 기울기를 동일 좌표에 표시.','Level curve, tangent, and base-point gradient in the same coordinates.')
out=base('Cylinder (blue), plane (orange), intersection (green), tangent (red)');proj=lambda x,y,z:(400+60*x-45*y,370+20*x+20*y-65*z)
for zz in [-1,0,1,2,3,4,5]:path(out,[proj(math.sqrt(5)*math.cos(i*math.pi/60),math.sqrt(5)*math.sin(i*math.pi/60),zz) for i in range(121)])
for i in range(16):th=i*math.pi/8;path(out,[proj(math.sqrt(5)*math.cos(th),math.sqrt(5)*math.sin(th),zz) for zz in [-1,5]])
for yy in [-2,-1,0,1,2]:path(out,[proj(xx,yy,3-yy) for xx in [-3,3]],'#df9138')
path(out,[proj(math.sqrt(5)*math.cos(i*math.pi/100),math.sqrt(5)*math.sin(i*math.pi/100),3-math.sqrt(5)*math.sin(i*math.pi/100)) for i in range(201)],'#278951',3);path(out,[proj(1+2*t,2-t,1+t) for t in [-1,1]],'#bf342e',3);save(70,out,'원기둥·평면·교선과 (1,2,1)의 접선.','Cylinder, plane, intersection, and tangent at (1,2,1).')
p.write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n');print('10 original SVG figures written')
