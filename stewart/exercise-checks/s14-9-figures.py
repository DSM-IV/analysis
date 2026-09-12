import math,json,sympy as S
from pathlib import Path
R=Path(__file__).resolve().parents[1];A=R/'exercise-content/assets';p=R/'exercise-content/s14-9.json';D=json.loads(p.read_text());x,y=S.symbols('x y')
def base(title):return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 600"><rect width="850" height="600" fill="white"/>',f'<text x="425" y="30" text-anchor="middle" font-family="sans-serif" font-size="17">{title}</text>']
def line(out,pts,col='#3574ad',width=1):out.append('<polyline points="'+' '.join(f'{a:.2f},{b:.2f}' for a,b in pts)+f'" fill="none" stroke="{col}" stroke-width="{width}"/>')
def save(n,out,ko,en):
 out.append('</svg>');name=f's14-9-{n}.svg';(A/name).write_text('\n'.join(out));next(e for e in D['exercises'] if e['number']==n)['figure']=dict(src='../exercise-content/assets/'+name,alt=dict(ko=ko,en=en),caption=dict(ko=ko,en=en))
out=base('Domain: y > −x − 1; dashed boundary excluded');proj=lambda x,y:(425+65*x,300-65*y);poly=[proj(-4,4),proj(4,4),proj(4,-4),proj(3,-4),proj(-4,3)];out.append('<polygon points="'+' '.join(f'{a},{b}' for a,b in poly)+'" fill="#d1e6f4"/>');out.append('<path d="M165 105 L685 625" fill="none" stroke="#3574ad" stroke-dasharray="7 5"/>');save(1,out,'열린 반평면. 점선 경계는 포함하지 않는다.','Open half-plane; the dashed boundary is excluded.')
out=base('Domain: x² + y² ≤ 4 and |x| ≤ 1');proj=lambda x,y:(425+110*x,300-110*y);pts=[proj(a,math.sqrt(4-a*a)) for a in [-1+i*.02 for i in range(101)]]+[proj(a,-math.sqrt(4-a*a)) for a in [1-i*.02 for i in range(101)]];out.append('<polygon points="'+' '.join(f'{a},{b}' for a,b in pts)+'" fill="#d1e6f4" stroke="#3574ad" stroke-width="3"/>');save(2,out,'반지름2 원판과 폭2 수직 띠의 교집합, 경계 포함.','Intersection of the radius2 disk and width2 vertical strip, boundaries included.')
plotdata=json.loads((R/'exercise-checks/s14-9-plot-data.json').read_text());plotdata['30']=dict(formula='x**2+y**4',box=[.3,1.7,.3,1.7])
for ns,data in plotdata.items():
 n=int(ns);F=S.sympify(data['formula']);fn=S.lambdify((x,y),F,'math');a,b,c,d=data['box'];segs=[];vals=[]
 for i in range(25):
  for sw in [False,True]:
   pts=[]
   for j in range(61):
    xx=a+(b-a)*(i/24 if sw else j/60);yy=c+(d-c)*(j/60 if sw else i/24);zz=fn(xx,yy);pts.append((xx,yy,zz));vals.append(zz)
   segs.append(pts)
 lo=min(vals);hi=max(vals);zs=280/max(1,hi-lo);project=lambda xx,yy,zz:(420+170*(xx-a)/(b-a)-155*(yy-c)/(d-c),410+50*(xx-a)/(b-a)+50*(yy-c)/(d-c)-zs*(zz-lo));out=base(f'Review {n}: computed surface'+(' with tangent plane and normal' if n==30 else ''))
 for pts in segs:line(out,[project(*q) for q in pts])
 if n==30:
  for i in range(11):
   xx=a+(b-a)*i/10;line(out,[project(xx,yy,2+2*(xx-1)+4*(yy-1)) for yy in [c,d]],'#dd8c39')
  line(out,[project(1+2*t,1+4*t,2-t) for t in [-.2,.2]],'#b33b37',3)
 out.append(f'<text x="425" y="555" text-anchor="middle">x ∈ [{a},{b}], y ∈ [{c},{d}]</text>');save(n,out,'함수에서 직접 계산한 곡면'+('과 접평면(주황)·법선(빨강).' if n==30 else '.'),'Surface sampled directly from the function'+(' with tangent plane(orange) and normal(red).' if n==30 else '.'))
out=base('Level ellipses of sqrt(4x²+y²)');proj=lambda x,y:(425+80*x,300-70*y)
for c in [1,2,3]:line(out,[proj(c*.5*math.cos(i*math.pi/100),c*math.sin(i*math.pi/100)) for i in range(201)],width=2)
save(5,out,'c=1,2,3의 타원 등위곡선.','Elliptical levels c=1,2,3.')
out=base('Level curves y = c − exp(x)');proj=lambda x,y:(400+90*x,300-45*y)
for c in [-2,0,2,4]:line(out,[proj(xx,c-math.exp(xx)) for xx in [-2+i*.04 for i in range(101)] if -5<=c-math.exp(xx)<=5],width=2)
save(6,out,'c=−2,0,2,4의 등위곡선.','Level curves c=−2,0,2,4.')
def contours(out,fn,levels,box,proj):
 a,b,c,d=box;N=100;dx=(b-a)/N;dy=(d-c)/N
 for lev in levels:
  for i in range(N):
   for j in range(N):
    corn=[(a+i*dx,c+j*dy),(a+(i+1)*dx,c+j*dy),(a+(i+1)*dx,c+(j+1)*dy),(a+i*dx,c+(j+1)*dy)];v=[fn(x,y)-lev for x,y in corn];hits=[]
    for k in range(4):
     l=(k+1)%4
     if v[k]*v[l]<0:
      t=v[k]/(v[k]-v[l]);hits.append(proj(corn[k][0]+t*(corn[l][0]-corn[k][0]),corn[k][1]+t*(corn[l][1]-corn[k][1])))
    for k in range(0,len(hits)-1,2):line(out,hits[k:k+2], '#b33b37' if lev<0 else '#3574ad')
out=base('Qualitative four-lobe contour pattern: illustrative sin(πx)sin(πy)');proj=lambda x,y:(180+220*x,510-220*y);contours(out,lambda x,y:math.sin(math.pi*x)*math.sin(math.pi*y),[-.8,-.5,-.2,.2,.5,.8],(0,2,0,2),proj);line(out,[proj(1,0),proj(1,2)],'#888',2);line(out,[proj(0,1),proj(2,1)],'#888',2);save(7,out,'정성적 대표 함수의 등고선: 파랑 양수, 빨강 음수, 회색0. 원문의 정확한 함수식으로 주장하지 않는다.','Qualitative representative contours: blue positive, red negative, gray zero; not a claimed exact source formula.')
out=base('Chain-rule dependency tree')
for label,cx,cy in [('w',425,70),('t',145,230),('u',425,230),('v',705,230)]:out.append(f'<text x="{cx}" y="{cy}" text-anchor="middle" font-size="24">{label}</text>')
for i,cx in enumerate([145,425,705]):
 line(out,[(425,80),(cx,200)])
 for j,label in enumerate(['p','q','r','s']):
  xx=50+i*280+j*63;line(out,[(cx,240),(xx,425)]);out.append(f'<text x="{xx}" y="455" text-anchor="middle" font-size="23">{label}</text>')
save(38,out,'w→t,u,v→p,q,r,s의 의존관계 나무.','Dependency tree w→t,u,v→p,q,r,s.')
out=base('Distance-sum ellipses (blue), constraint line (red)');proj=lambda x,y:(425+45*x,350-45*y)
for c in [7,8,9,10,11,12]:
 aa=c/2;bb=math.sqrt(aa*aa-9);line(out,[proj(aa*math.cos(i*math.pi/100),bb*math.sin(i*math.pi/100)) for i in range(201)])
line(out,[proj(xx,(100-16*xx)/15) for xx in [-1,8]],'#b33b37',3);px,py=proj(4,2.4);out.append(f'<circle cx="{px}" cy="{py}" r="5"/><text x="{px+10}" y="{py-12}">(4,12/5), minimum10</text>');save(64,out,'초점(±3,0)의 타원 등고선과 접하는 제약 직선.','Elliptical levels with foci(±3,0) and the tangent constraint line.')
out=base('Optimal pentagon: roof angle30°');ll=170;h=(1+math.sqrt(3))*ll/2;bb=math.sqrt(3)*ll;cx=425;bottom=530;pts=[(cx-bb/2,bottom),(cx+bb/2,bottom),(cx+bb/2,bottom-h),(cx,bottom-h-ll/2),(cx-bb/2,bottom-h),(cx-bb/2,bottom)];line(out,pts,'#278951',3);line(out,[pts[2],pts[4]],'#888');out.append('<text x="425" y="570" text-anchor="middle">l=P/(3+2√3), base=√3l, walls=(1+√3)l/2</text>');save(65,out,'최대넓이 오각형의 치수 비례 도해.','Proportional diagram of the maximum-area pentagon.')
p.write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n');print('Review figures',sum('figure' in e for e in D['exercises']))
# Problems Plus 2: exact gradient-path geometry.
p=R/'exercise-content/s14-10.json';D=json.loads(p.read_text());out=base('Concentration contours and steepest-ascent paths');proj=lambda x,y:(425+2*x,300-2*y)
for rr in [30,60,90,120]:line(out,[proj(rr*math.cos(i*math.pi/100),rr/math.sqrt(2)*math.sin(i*math.pi/100)) for i in range(201)])
for xx,yy in [(100,65),(-100,65),(100,-65),(-100,-65),(0,110)]:line(out,[proj(xx*math.exp(-t),yy*math.exp(-2*t)) for t in [i*.035 for i in range(201)]],'#b33b37',3)
out.append('<text x="425" y="570" text-anchor="middle">Red paths point toward origin: x=x₀e^(−s), y=y₀e^(−2s)</text></svg>');name='s14-10-2.svg';(A/name).write_text('\n'.join(out));D['exercises'][1]['figure']=dict(src='../exercise-content/assets/'+name,alt=dict(ko='농도 타원과 최급상승 포물선 경로',en='Concentration ellipses and steepest-ascent parabolic paths'),caption=dict(ko='빨간 경로는 파란 농도 등고선에 수직이며 원점 방향으로 진행한다.',en='Red paths are normal to blue concentration contours and proceed toward the origin.'));p.write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n');print('Problems Plus2 figure')
