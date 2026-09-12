from curve_figures import draw_curves
from pathlib import Path
import math,json,html
R=Path(__file__).resolve().parents[1];p=R/'exercise-content/s13-2.json';d=json.loads(p.read_text());pi=math.pi;sin=math.sin;cos=math.cos;exp=math.exp
figs={}
def segment(p,v):return lambda u:tuple(a+u*b for a,b in zip(p,v))
def tangent(n,fn,at,vel,span):
 point=fn(at);zero=tuple(0 for _ in point)
 figs[n]=[('Blue curve; purple r; orange tangent',[fn,segment(zero,point),segment(point,vel)],[span,(0,1),(0,1)],'xy')]
tangent(3,lambda t:(t-2,t*t+1),-1,(1,-2),(-2.3,1.2));tangent(4,lambda t:(t*t,t**3),1,(2,3),(-1.2,1.6));tangent(5,lambda t:(exp(2*t),exp(t)),0,(2,1),(-1.5,1));tangent(6,lambda t:(exp(t),2*t),0,(1,2),(-1.2,1.4));tangent(7,lambda t:(4*sin(t),-2*cos(t)),3*pi/4,(-2*math.sqrt(2),math.sqrt(2)),(0,2*pi));tangent(8,lambda t:(cos(t)+1,sin(t)-1),-pi/3,(math.sqrt(3)/2,.5),(-pi,pi))
figs[2]=[('Blue curve; purple r(1); orange r(1.1)',[lambda t:(t*t,t),segment((0,0),(1,1)),segment((0,0),(1.21,1.1)),segment((1,1),(.21,.1))],[(0,2),(0,1),(0,1),(0,1)],'xy'),('Blue curve; purple derivative; orange quotient',[lambda t:(t*t,t),segment((1,1),(2,1)),segment((1,1),(2.1,1))],[(0,2),(0,1),(0,1)],'xy')]
figs[31]=[('Blue curve; purple tangent',[lambda t:(t,exp(-t),2*t-t*t),segment((0,1,0),(1,-1,2))],[(-1.2,2.2),(-1,1)],'xyz')]
figs[32]=[('Blue curve; purple tangent',[lambda t:(2*cos(t),2*sin(t),4*cos(2*t)),segment((math.sqrt(3),1,2),(-1,math.sqrt(3),-4*math.sqrt(3)))],[(0,2*pi),(-.5,.5)],'xyz')]
figs[33]=[('Blue curve; purple tangent',[lambda t:(t*cos(t),t,t*sin(t)),segment((-pi,pi,0),(-1,1,-pi))],[(0,2*pi),(-1.5,1.5)],'xyz')]
figs[34]=[('Blue ellipse; purple/orange tangents',[lambda t:(sin(pi*t),2*sin(pi*t),cos(pi*t)),segment((0,0,1),(1,2,0)),segment((1,2,0),(0,0,1))],[(0,2),(-1.4,1.5),(-1.4,1.5)],'xyz')]
for n,panels in figs.items():
 fn=f's13-2-{n}.svg';draw_curves(R/'exercise-content/assets'/fn,panels);d['exercises'][n-1]['figure']={'src':'../exercise-content/assets/'+fn,'alt':{'ko':f'13.2 {n}번 곡선과 벡터','en':f'Curve and vectors for13.2.{n}'},'caption':{'ko':'주어진 식으로 직접 제작했다. 파랑은 곡선이고 다른 색은 제목에 표시한 벡터 또는 접선이다.','en':'Original calculation from the given equations. Blue is the curve; other colors show the vectors or tangent lines identified in the title.'}}
# Exercise1 gives only a schematic; no numeric coordinates are inferred.
P=(190,500);Q=(205,435);RR=(177,365)
out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 660"><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0L10,5L0,10Z" fill="context-stroke"/></marker></defs><rect width="1000" height="660" fill="#f8fafc"/>']
for idx,title in enumerate(['Displacements from P','Scaled secants from P']):
 dx=500*idx;out.append(f'<text x="{dx+250}" y="30" text-anchor="middle" font-family="sans-serif" font-size="18">{title}</text><path d="M{dx+70},565C{dx+140},580 {dx+175},560 {dx+190},500C{dx+198},468 {dx+207},455 {dx+205},435C{dx+205},405 {dx+190},380 {dx+177},365C{dx+165},352 {dx+150},345 {dx+140},340" fill="none" stroke="#94a3b8" stroke-width="2"/>')
 for point,label in [(P,'P=r(4)'),(Q,'Q=r(4.2)'),(RR,'R=r(4.5)')]:out.append(f'<circle cx="{dx+point[0]}" cy="{point[1]}" r="3" fill="#0f172a"/><text x="{dx+point[0]+10}" y="{point[1]+6}" font-family="sans-serif" font-size="15">{label}</text>')
 for end,fac,col,label in [(Q,5 if idx else 1,'#0284c7','5 PQ'if idx else'PQ'),(RR,2 if idx else 1,'#a855f7','2 PR'if idx else'PR')]:
  # Common geometry preserves the exact factors5 and2.
  factor=fac;ex=P[0]+factor*(end[0]-P[0]);ey=P[1]+factor*(end[1]-P[1]);out.append(f'<path d="M{dx+P[0]},{P[1]}L{dx+ex},{ey}" stroke="{col}" stroke-width="2" marker-end="url(#arr)"/><text x="{dx+ex-50}" y="{ey-10}" font-family="sans-serif" fill="{col}" font-size="15">{label}</text>')
 out.append(f'<text x="{dx+250}" y="635" text-anchor="middle" font-family="sans-serif" font-size="14">Schematic only; no numerical curve data.</text>')
out.append('<path d="M190,500L224,355" stroke="#ea580c" stroke-width="2" marker-end="url(#arr)"/><text x="235" y="340" fill="#ea580c" font-family="sans-serif" font-size="15">T(4), unit length</text></svg>');fn='s13-2-1.svg';(R/'exercise-content/assets'/fn).write_text(''.join(out));d['exercises'][0]['figure']={'src':'../exercise-content/assets/'+fn,'alt':{'ko':'P에서 시작하는 변위와 할선벡터 도해','en':'Schematic displacement and secant vectors from P'},'caption':{'ko':'개형을 설명하는 자체 도해이며 수치 좌표를 부여한 답이 아니다. P에서의 단위접선은 두 할선의 극한 방향으로 길이1을 잡는다.','en':'Original schematic, not an answer assigning numerical coordinates. The unit tangent at P has length1 in the limiting direction of the secants.'}}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(len(figs)+1,'original figures')
