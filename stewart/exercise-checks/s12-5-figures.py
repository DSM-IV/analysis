"""Original intercept triangles, shown with labelled coordinate axes."""
from pathlib import Path
import json,html
R=Path(__file__).resolve().parents[1];p=R/'exercise-content/s12-5.json';doc=json.loads(p.read_text())
for n,coef,c in [(41,(2,5,1),10),(42,(3,1,2),6),(43,(6,-3,4),6),(44,(6,5,-3),15)]:
 intercepts=[c/a for a in coef];pts=[(intercepts[0],0,0),(0,intercepts[1],0),(0,0,intercepts[2])]
 def project(p):x,y,z=p;return(.8*x-.6*y,.36*x+.48*y-.8*z)
 ends=[]
 for i in range(3):
  for sign in [-1,1]:
   q=[0,0,0];q[i]=sign*max(abs(intercepts[i])*1.15,1.5);ends.append(tuple(q))
 projected=[project(q)for q in ends];mn=[min(q[i]for q in projected)for i in range(2)];mx=[max(q[i]for q in projected)for i in range(2)];sc=min(360/(mx[0]-mn[0]),285/(mx[1]-mn[1]))
 def xy(q):a,b=project(q);return(250+(a-(mn[0]+mx[0])/2)*sc,210+(b-(mn[1]+mx[1])/2)*sc)
 out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 440"><rect width="500" height="440" fill="#f8fafc"/>',f'<text x="250" y="28" text-anchor="middle" font-size="18" font-family="sans-serif">Exercise 12.5.{n}: plane intercepts</text>']
 out.append('<polygon points="'+' '.join('%g,%g'%xy(q)for q in pts)+'" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>')
 for i in range(3):
  a,b=xy(ends[2*i]),xy(ends[2*i+1]);out.append(f'<path d="M{a[0]},{a[1]}L{b[0]},{b[1]}" stroke="#64748b" stroke-dasharray="4 3"/><text x="{b[0]+5}" y="{b[1]-7}" font-family="sans-serif" font-size="17">{"xyz"[i]}</text>')
 for i,q in enumerate(pts):
  a,b=xy(q);label='('+', '.join(f'{v:g}'for v in q)+')';dx,dy=[(6,21),(-8,23),(7,-12)][i];anchor='end'if i==1 else'start';out.append(f'<circle cx="{a}" cy="{b}" r="3" fill="#0369a1"/><text x="{a+dx}" y="{b+dy}" text-anchor="{anchor}" font-family="sans-serif" font-size="15">{html.escape(label)}</text>')
 out.append('<text x="250" y="420" text-anchor="middle" font-family="sans-serif" font-size="14">The plane extends beyond the shaded triangle.</text></svg>');fn=f's12-5-{n}.svg';(R/'exercise-content/assets'/fn).write_text(''.join(out));doc['exercises'][n-1]['figure']={'src':'../exercise-content/assets/'+fn,'alt':{'ko':'좌표축 절편을 잇는 평면 도해','en':'Plane diagram joining its coordinate intercepts'},'caption':{'ko':'자체 제작 사영도. 음영 삼각형은 무한 평면의 일부이다.','en':'Original projected diagram. The shaded triangle is only part of the infinite plane.'}}
p.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
