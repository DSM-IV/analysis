from early_helpers import *
from math import *
def book(sec,pages):
 b=Book(sec,pages);d=json.loads((ROOT/f's{sec.replace(".","-")}.json').read_text());b.E={e['number']:e for e in d['exercises']};return b
b=book('12.7',[922,923,924])
items={28:(lambda u,v:(3,u,v),(-2,2),(-2,2),'x = 3'),29:(lambda u,v:(u,v,u),(-2,2),(-2,2),'x = z'),30:(lambda u,v:(u,v*v,v),(-2,2),(-2,2),'y = z²'),31:(lambda u,v:(u,u*cos(v),u*sin(v)/2),(-3,3),(0,2*pi),'x² = y² + 4z²'),32:(lambda u,v:(u,4*u+2*v-4,v),(-1,2),(-1,2),'4x - y + 2z = 4'),33:([lambda u,v:(sinh(u)*cos(v),2*cosh(u),sinh(u)*sin(v)),lambda u,v:(sinh(u)*cos(v),-2*cosh(u),sinh(u)*sin(v))],(0,1.3),(0,2*pi),'y²/4 - x² - z² = 1'),34:(lambda u,v:(u,sqrt(1+u*u)*cos(v),sqrt(1+u*u)*sin(v)),(-2,2),(0,2*pi),'y² + z² - x² = 1'),35:(lambda u,v:(sin(u)*cos(v),1+sin(u)*sin(v),2*cos(u)),(0,pi),(0,2*pi),'x²+(y-1)²+z²/4 = 1'),36:(lambda u,v:(u*u+v*v,1+u,2+v),(-2,2),(-2,2),'x = (y-1)² + (z-2)²'),37:(lambda u,v:(2*cos(u),4*sin(u)*cos(v),4*sin(u)*sin(v)),(0,pi),(0,2*pi),'4x² + y² + z² = 16'),38:(lambda u,v:(2/sqrt(3)*sin(u)*cos(v),-5/3+4/3*cos(u),2/sqrt(3)*sin(u)*sin(v)),(0,pi),(0,2*pi),'Ellipsoid centered at (0,-5/3,0)')}
for n,item in items.items():b.plot(n,[item])
fn='s12-7-2.svg';out=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="330" viewBox="0 0 1200 330"><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0L0,6L7,3Z" fill="context-stroke"/></marker></defs><rect width="100%" height="100%" fill="#f8fafc"/>']
for i,(title,vecs)in enumerate([('(a) a+b',[(100,-70),(30,60)]),('(b) a-b',[(100,-70),(-30,-60)]),('(c) -a/2',[(-50,35)]),('(d) 2a+b',[(70,-49),(70,-49),(21,42)])]):
 x=i*300+70;y=100;sx,sy=x,y
 for j,(dx,dy)in enumerate(vecs):out.append(f'<path d="M{x},{y}l{dx},{-dy}" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow)"/>');x+=dx;y-=dy
 out.append(f'<path d="M{sx},{sy}L{x},{y}" stroke="#e11d48" stroke-width="3" marker-end="url(#arrow)"/>');out.append(f'<text x="{i*300+110}" y="30" font-family="sans-serif" font-size="17">{title}</text>')
out.append('<text x="25" y="310" font-family="sans-serif" font-size="13">Blue: head-to-tail construction. Red: resultant. Lengths illustrate the source directions.</text></svg>');(ROOT/'assets'/fn).write_text(''.join(out));b.E[2]['figure']={'src':'../exercise-content/assets/'+fn,'alt':pair('벡터합 네 가지 작도','Four vector constructions'),'caption':pair('방향 관계를 보존한 자체 도식. 파랑은 이어 붙인 벡터, 빨강은 합벡터.','Original direction-preserving diagram: blue vectors are placed head-to-tail; red is the resultant.')}
def save(b,kind):
 b.save();p=ROOT/f's{b.section.replace(".","-")}.json';d=json.loads(p.read_text());d['scope']['kind']=kind
 for e in d['exercises']:e['conceptHref']='../s12-6.html'
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
save(b,'review')
b=book('12.8',[925,926]);r=sqrt(3)-1.5;centers=[(.5,.5,.5)]+[(x,y,z)for x in[r,1-r]for y in[r,1-r]for z in[r,1-r]]
b.plot(1,[([lambda u,v,c=c:(c[0]+r*sin(u)*cos(v),c[1]+r*sin(u)*sin(v),c[2]+r*cos(u))for c in centers],(0,pi),(0,2*pi),'Nine equal balls; radius sqrt(3)-1.5')])
b.plot(3,[(lambda u,v:(sqrt(1+u*u)*cos(v),sqrt(1+u*u)*sin(v),u),(0,1),(0,2*pi),'x²+y²-z²=1, 0≤z≤1')])
b.plot(6,[(lambda u,v:(5+3*sqrt(6)*sin(u)*cos(v),4+3*sqrt(6)*sin(u)*sin(v),1+3*sqrt(6)*cos(u)),(0,pi),(0,2*pi),'Largest sphere: center (5,4,1), R=3sqrt(6)')])
b.plot(8,[([lambda u,v:(v*cos(u)/2,v*sin(u)/2,1-abs(v*sin(u))),lambda u,v:(cos(u)/2,sin(u)/2,v*(1-abs(sin(u)))),lambda u,v:(v*cos(u)/2,v*sin(u)/2,0)],(0,2*pi),(0,1),'Maximal intersection of projection cylinders')])
save(b,'problems-plus')
