"""Reproducible structural/math checks and original schematic for 5.1.59."""
import json,math,xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1];p=ROOT/'exercise-content/s5-1.json';d=json.loads(p.read_text());E={e['number']:e for e in d['exercises']}
assert list(E)==list(range(1,73))
for e in E.values():
 assert e['status']=='math-verified'
 for lang in['ko','en']:
  assert len(e['answer'][lang])>2 and e['answer'][lang]not in['ko','en']
  assert len(e['steps'][lang])>=2 and len(e['check'][lang])>15
# Source graphic has no numeric velocity scale: retain only relative heights.
im=Image.open('/tmp/calc1-ch5/s5-1-0409.png').convert('RGB')
curves=[]
for kind in['A','B']:
 points=[(0,0)]
 for x in range(817,1154):
  ys=[]
  for y in range(548,747):
   r,g,b=im.getpixel((x,y));match=r>180 and g<130 and b<130 if kind=='A'else b>110 and r<90 and g<170
   if match:ys.append(y)
  if ys:points.append(((x-815)/113,746-sum(ys)/len(ys)))
 curves.append(points)
def interp(ps,t):
 for a,b in zip(ps,ps[1:]):
  if a[0]<=t<=b[0]:return a[1]+(b[1]-a[1])*(t-a[0])/(b[0]-a[0])
 return ps[-1][1]
acc=0;at2=None;catch=None
for i in range(1,3001):
 t=i/1000;prev=acc;acc+=(interp(curves[0],t-.0005)-interp(curves[1],t-.0005))*.001
 if i==2000:at2=acc
 if t>1 and prev>0>=acc and catch is None:catch=t
assert at2>0 and 2.15<catch<2.4,(at2,catch)
# Independently redraw the digitized curves as sparse polylines, with clear approximation caption.
W,H=600,380
xy=lambda t,v:(55+480*t/3,320-245*v/200)
path=lambda pts:' '.join(f'{xy(t,v)[0]:.2f},{xy(t,v)[1]:.2f}'for t,v in pts)
out=['<svg xmlns="http://www.w3.org/2000/svg" width="600" height="380" viewBox="0 0 600 380"><rect width="100%" height="100%" fill="#f8fafc"/><text x="300" y="25" text-anchor="middle" font-family="sans-serif" font-size="16">5.1.59  Relative velocities (graph estimate)</text>']
poly=[(t/50,interp(curves[0],t/50))for t in range(51)]+[(t/50,interp(curves[1],t/50))for t in range(50,-1,-1)]
out.append(f'<polygon points="{path(poly)}" fill="#bfdbfe"/>')
for i,c in enumerate(['#e11d48','#0284c7']):
 pts=[(j/20,interp(curves[i],j/20))for j in range(61)];out.append(f'<polyline points="{path(pts)}" fill="none" stroke="{c}" stroke-width="2"/>')
out.append('<path d="M55,55V320H555" fill="none" stroke="#475569"/>')
for t in range(4):
 x=55+160*t;out.append(f'<text x="{x}" y="340" text-anchor="middle" font-family="sans-serif">{t}</text>')
out.append('<text x="555" y="362" text-anchor="end" font-family="sans-serif">t (min)</text><text x="80" y="63" font-family="sans-serif" fill="#e11d48">A</text><text x="110" y="63" font-family="sans-serif" fill="#0284c7">B</text><text x="55" y="365" font-family="sans-serif" font-size="11">Velocity: relative scale; shaded area is A’s first-minute lead.</text></svg>')
asset=ROOT/'exercise-content/assets/s5-1-59.svg';asset.write_text(''.join(out));E[59]['figure']={'src':'../exercise-content/assets/s5-1-59.svg','alt':{'ko':'두 차의 상대 속도 곡선과 첫1분 넓이','en':'Relative velocity curves and the first-minute area'},'caption':{'ko':'원본 곡선을 독립적으로 수치 판독해 다시 그린 근사도. 세로축은 상대 척도이며, 추월 시간은 누적 넓이가 같아지는 약2.25분이다.','en':'Original approximate redraw from independently digitized source curves. The vertical scale is relative; accumulated areas balance at about2.25 minutes.'}}
# Arithmetic/application checks independent of the symbolic area author.
assert abs(2/3600*sum([22-20,52-46,71-62,86-75,98-86])-1/45)<1e-14
assert abs(4*sum([6.2,6.8,5,4.8])-91.2)<1e-12
assert abs(40*sum([20.3,29,27.3,20.5,8.7])-4232)<1e-9
assert abs(8/3*6**3-576)<1e-12
for e in E.values():
 if 'figure'in e:ET.parse(ROOT/'exercise-content'/e['figure']['src'].split('../exercise-content/')[1])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
report={'section':'5.1','count':72,'sourcePDFPages':[407,408,409,410],'visualSourceReview':'all four exercise pages inspected','mathVerification':'calc1-s5-1-author.py: ordered strips; symbolic integrals versus independent quadrature; numerical areas use tanh-sinh versus Gauss-Legendre maxdegree10. Application arithmetic checked here.','graph59':{'accumulatedRelativeLeadAtTwoMinutes':at2,'estimatedCatchUpMinutes':catch},'figures':sum('figure'in e for e in E.values()),'status':'passed','limitations':['Graph-reading answers are approximate. Exercise49 identifies the intended first tangent branch; further tangent branches also create bounded components.']}
(ROOT/'exercise-checks/calc1-s5-1-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report)
