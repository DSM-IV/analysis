import math,json
from pathlib import Path
R=Path(__file__).resolve().parents[1];A=R/'exercise-content/assets'
sin,cos,sqrt,exp=math.sin,math.cos,math.sqrt,math.exp

def draw(section,n,curve=None,field=None,span=4,samples=None,space=False,fence=False):
 W=640;project=(lambda x,y,z:(320+17*x-12*y,325+6*x+8*y-31*z)) if fence else (lambda x,y,z:(320+50*x-30*y,330+20*x+20*y-55*z))
 pt=(lambda a:project(*a)) if space else (lambda a:(320+250*a[0]/span,300-250*a[1]/span))
 s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 610"><title>Exercise {section}.{n}: original diagram</title><rect width="640" height="610" fill="white"/><defs><marker id="a" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto"><path d="M0,0L5,2.5L0,5" fill="#176db1"/></marker></defs>',f'<text x="320" y="30" text-anchor="middle" font-family="sans-serif" font-size="20">Exercise {section}.{n}</text>']
 def line(a,b,col='#176db1',arrow=False):
  a=pt(a);b=pt(b);s.append(f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" stroke="{col}" stroke-width="1.5"'+(' marker-end="url(#a)"' if arrow else '')+'/>')
 def poly(points,col='#d16832'):
  ps=' '.join(f'{pt(p)[0]:.2f},{pt(p)[1]:.2f}' for p in points);s.append(f'<polyline points="{ps}" fill="none" stroke="{col}" stroke-width="2.5"/>')
 if not space:
  line((-span,0),(span,0),'#999');line((0,-span),(0,span),'#999')
 if field:
  points=samples if samples is not None else [(i*span/6,j*span/6) for i in range(-6,7) for j in range(-6,7)]
  raw=[]
  for p in points:
   try:v=field(*p)
   except ZeroDivisionError:continue
   raw.append((p,v))
  mx=max(sqrt(sum(q*q for q in v)) for p,v in raw)
  scale=(.65 if space else span*.13)/mx if samples is None else .38
  for p,v in raw:line(p,tuple(a+scale*b for a,b in zip(p,v)),arrow=True)
 if curve:poly(curve)
 if fence:
  base=[(10*cos(t*math.pi/100),10*sin(t*math.pi/100),0) for t in range(201)];top=[(p[0],p[1],4+.01*(p[0]**2-p[1]**2)) for p in base]
  poly(base,'#777');poly(top)
  for i in range(0,201,8):line(base[i],top[i],'#8bacbf')
 s.append('<text x="320" y="587" text-anchor="middle" font-size="14" font-family="sans-serif">Orange: curve. Blue: field vectors (one common scale).</text></svg>')
 name=f's{section.replace(".","-")}-{n}.svg';(A/name).write_text('\n'.join(s))
 path=R/f'exercise-content/s{section.replace(".","-")}.json';d=json.loads(path.read_text());e=next(e for e in d['exercises'] if e['number']==n);e['figure']={'src':'../exercise-content/assets/'+name,'alt':{'ko':f'{section} {n}번 자체 도해','en':f'Original diagram for exercise {section}.{n}'},'caption':{'ko':'문제의 식에서 직접 생성한 도해. 벡터는 공통 축척이며 주황색은 경로이다.','en':'Diagram generated directly from the given equations. Vectors use a common scale; orange is the curve.'}};path.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
curve=lambda f,a,b:[f(a+(b-a)*i/300) for i in range(301)]
draw('16.2',29,curve(lambda t:(2*cos(t),2*sin(t)),0,1.5*math.pi),lambda x,y:(x-y,x*y),3)
draw('16.2',30,curve(lambda t:(t,1+t*t),-1,1),lambda x,y:(x/sqrt(x*x+y*y),y/sqrt(x*x+y*y)),3)
draw('16.2',31,curve(lambda t:(t*t,t**3),0,1),lambda x,y:(exp(x-1),x*y),1.5,samples=[(0,0),(.5,1/(2*sqrt(2))),(1,1)])
draw('16.2',32,curve(lambda t:(2*t,3*t,-t*t),-1,1),lambda x,y,z:(x,-z,y),samples=[(2*t,3*t,-t*t) for t in [-1,-.5,.5,1]],space=True)
draw('16.2',34,curve(lambda t:(2*cos(t),2*sin(t)),0,2*math.pi),lambda x,y:(x*x,x*y),3)
draw('16.2',50,space=True,fence=True)
draw('16.3',33,field=lambda x,y:(sin(y),1+x*cos(y)),span=3)
draw('16.4',24,curve(lambda t:(5*cos(t)-cos(5*t),5*sin(t)-sin(5*t)),0,2*math.pi),span=7)
print('Generated 8 additional original SVG diagrams')
