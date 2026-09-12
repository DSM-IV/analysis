"""Original geometric vector constructions."""
from pathlib import Path
import math,json,html
R=Path(__file__).resolve().parents[1];A=R/'exercise-content/assets';p=R/'exercise-content/s12-2.json';doc=json.loads(p.read_text())
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(a,t):return tuple(x*t for x in a)
def panels(n,plots,schematic=False):
 w,h=420,360;cols=min(2,len(plots));rows=math.ceil(len(plots)/cols)
 s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w*cols} {h*rows}"><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0L10,5L0,10Z" fill="context-stroke"/></marker></defs><rect width="100%" height="100%" fill="#f8fafc"/>']
 for i,(title,segments)in enumerate(plots):
  ox=(i%cols)*w;oy=(i//cols)*h
  def proj(a):return(a[0],-a[1])if len(a)==2 else(.8*a[0]-.6*a[1],.36*a[0]+.48*a[1]-.8*a[2])
  q=[proj(a)for start,end,label in segments for a in(start,end)];xs=[a[0]for a in q]+[0];ys=[a[1]for a in q]+[0];xmin,xmax=min(xs),max(xs);ymin,ymax=min(ys),max(ys);sc=min(280/max(xmax-xmin,1),240/max(ymax-ymin,1))
  def xy(a):x,y=proj(a);return(ox+210+(x-(xmax+xmin)/2)*sc,oy+185+(y-(ymax+ymin)/2)*sc)
  s.append(f'<text x="{ox+210}" y="{oy+24}" text-anchor="middle" font-family="sans-serif" font-size="22">{html.escape(title)}</text>')
  for j,(start,end,label)in enumerate(segments):
   x,y=xy(start);u,v=xy(end);color='#0f172a' if label=='result' else ['#0284c7','#9333ea','#c2410c','#0f172a'][min(j,3)];s.append(f'<path d="M{x:.2f},{y:.2f}L{u:.2f},{v:.2f}" stroke="{color}" stroke-width="2" marker-end="url(#arr)"/><text x="{(x+u)/2+5:.2f}" y="{(y+v)/2-6:.2f}" font-family="sans-serif" font-size="18" fill="{color}">{html.escape(label)}</text>')
  zero=xy((0,0));s.append(f'<circle cx="{zero[0]}" cy="{zero[1]}" r="2" fill="#334155"/>')
 s.append('</svg>');(A/f's12-2-{n}.svg').write_text(''.join(s));cap=('직접 제작한 벡터 작도. 원본의 방향 관계를 보존한 개략도이며 축척으로 수치를 읽는 그림은 아니다.','Original vector construction preserving the source direction relationships; the schematic is not intended for numerical measurement.')if schematic else('주어진 좌표로 직접 제작한 벡터 그림. 공간벡터는 사영하여 표시했다.','Original vector diagram constructed from the given coordinates; spatial vectors are shown in projection.')
 doc['exercises'][n-1]['figure']={'src':f'../exercise-content/assets/s12-2-{n}.svg','alt':{'ko':f'12.2 {n}번 벡터 작도','en':f'Vector construction for12.2.{n}'},'caption':dict(zip(('ko','en'),cap))}
def chain(vecs,names):
 start=(0,0);lines=[]
 for a,name in zip(vecs,names):end=plus(start,a);lines.append((start,end,name));start=end
 lines.append(((0,0),start,'result'));return lines
panels(2,[('Position vector', [((0,0),(4,7),'P=(4,7)')])])
D=(0,0);C=(4,0);AA=(1,3);B=(5,3);E=(2.5,1.5)
segments=[(AA,B,'AB'),(D,C,'DC'),(D,AA,'DA'),(C,B,'CB'),(D,E,'DE'),(E,B,'EB'),(C,E,'CE'),(E,AA,'EA')]
panels(3,[('Parallelogram and midpoint E',segments)],True)
a=(0,3);bb=(-2.3,0);c=(1.7,1.2)
plots=[]
for name,vecs,names in [('a+b',[a,bb],['a','b']),('b+c',[bb,c],['b','c']),('a+c',[a,c],['a','c']),('a-c',[a,scale(c,-1)],['a','-c']),('b+a+c',[bb,a,c],['b','a','c']),('a-b-c',[a,scale(bb,-1),scale(c,-1)],['a','-b','-c'])]:plots.append((name,chain(vecs,names)))
panels(5,plots,True)
u=(1,1.1);vv=(3,-1)
plots=[]
for name,vecs,names in [('u+v',[u,vv],['u','v']),('u-v',[u,scale(vv,-1)],['u','-v']),('2u',[scale(u,2)],['2u']),('-v/2',[scale(vv,-.5)],['-v/2']),('3u+v',[scale(u,3),vv],['3u','v']),('v-2u',[vv,scale(u,-2)],['v','-2u'])]:plots.append((name,chain(vecs,names)))
panels(6,plots,True)
for n,aa,bb in [(9,(-2,1),(1,2)),(10,(-5,-1),(-3,3)),(11,(3,-1),(2,3)),(12,(3,2),(1,0)),(13,(1,-2,4),(-2,3,0)),(14,(3,0,-2),(0,5,0))]:
 vec=plus(bb,scale(aa,-1));panels(n,[(f'A={aa}, B={bb}',[(aa,bb,'AB'),(tuple(0 for _ in aa),vec,str(vec))])])
for n,aa,bb in [(15,(-1,4),(6,-2)),(16,(3,-1),(-1,5)),(17,(3,0,1),(0,8,0)),(18,(1,3,-2),(0,0,6))]:
 zero=tuple(0 for _ in aa);cc=plus(aa,bb);panels(n,[('Head-to-tail addition',[(zero,aa,'a'),(aa,cc,'b'),(zero,cc,'a+b')])])
a=(3,2);bb=(2,-1);c=(7,1);sa=scale(a,9/7)
panels(45,[('a,b,c', [((0,0),a,'a'),((0,0),bb,'b'),((0,0),c,'c')]),('c=(9/7)a+(11/7)b',[((0,0),sa,'(9/7)a'),(sa,c,'(11/7)b'),((0,0),c,'c')])])
# Explicit sine curve and the four unit vectors at the requested point.
x0=math.pi/6;y0=1
s=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400"><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10Z" fill="context-stroke"/></marker></defs><rect width="640" height="400" fill="#f8fafc"/><text x="320" y="24" text-anchor="middle" font-family="sans-serif">Tangent and normal unit vectors at (pi/6,1)</text>']
def xy(x,y):return(200+100*x,285-100*y)
pts=[xy(-1+3.8*i/250,2*math.sin(-1+3.8*i/250))for i in range(251)]
s.append('<polyline points="'+' '.join(f'{x:.2f},{y:.2f}'for x,y in pts)+'" fill="none" stroke="#64748b" stroke-width="2"/>')
for name,(dx,dy)in [('T',(.5,math.sqrt(3)/2)),('-T',(-.5,-math.sqrt(3)/2)),('N',(-math.sqrt(3)/2,.5)),('-N',(math.sqrt(3)/2,-.5))]:
 x,y=xy(x0,y0);u,v=xy(x0+dx,y0+dy);color='#0284c7'if'T'in name else'#9333ea';s.append(f'<path d="M{x},{y}L{u},{v}" stroke="{color}" stroke-width="2" marker-end="url(#arr)"/><text x="{u+6}" y="{v}" font-family="sans-serif">{name}</text>')
s.append('</svg>');(A/'s12-2-42.svg').write_text(''.join(s));doc['exercises'][41]['figure']={'src':'../exercise-content/assets/s12-2-42.svg','alt':{'ko':'사인 곡선의 접선과 법선 단위벡터','en':'Unit tangent and normal vectors on the sine curve'},'caption':{'ko':'같은 축척으로 그린 곡선과 네 단위벡터.','en':'Curve and four unit vectors drawn at equal coordinate scales.'}}
p.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
