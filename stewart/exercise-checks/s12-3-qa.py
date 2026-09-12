from pathlib import Path
import json,math,sympy as s
R=Path(__file__).resolve().parents[1];p=R/'exercise-content/s12-3.json';doc=json.loads(p.read_text());A=R/'exercise-content/assets'
def svg(n,title,lines,points=[]):
 def xy(v):return(100+70*v[0],330-70*v[1])
 out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400"><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10Z" fill="context-stroke"/></marker></defs><rect width="500" height="400" fill="#f8fafc"/>',f'<text x="250" y="26" text-anchor="middle" font-family="sans-serif" font-size="17">{title}</text>']
 for i,(start,end,label)in enumerate(lines):
  x,y=xy(start);u,v=xy(end);color=['#0284c7','#9333ea','#c2410c','#0f172a'][i%4];out.append(f'<path d="M{x},{y}L{u},{v}" stroke="{color}" stroke-width="2" marker-end="url(#arrow)"/><text x="{(x+u)/2+8}" y="{(y+v)/2-8}" font-family="sans-serif" font-size="16">{label}</text>')
 for point,label in points:
  x,y=xy(point);out.append(f'<circle cx="{x}" cy="{y}" r="3" fill="#334155"/><text x="{x+7}" y="{y+16}" font-family="sans-serif">{label}</text>')
 out.append('</svg>');(A/f's12-3-{n}.svg').write_text(''.join(out));doc['exercises'][n-1]['figure']={'src':f'../exercise-content/assets/s12-3-{n}.svg','alt':{'ko':f'12.3 {n}번 벡터 관계','en':f'Vector configuration for12.3.{n}'},'caption':{'ko':'조건에 따라 직접 제작한 벡터 작도. 정확한 길이와 각도는 본문의 식을 따른다.','en':'Original vector construction from the stated conditions; exact lengths and angles are given in the text.'}}
svg(11,'Equilateral triangle; |u|=1',[((1.5,1.5*math.sqrt(3)),(0,0),'u'),((1.5,1.5*math.sqrt(3)),(3,0),'v'),((0,0),(3,0),'w')])
svg(12,'Square; v ends at the center',[((0,3),(3,3),'u'),((0,3),(0,0),'w'),((0,3),(1.5,1.5),'v')],[((3,0),'fourth corner')])
svg(46,'Projection and perpendicular residual',[((0,0),(1,4),'a'),((0,0),(2,3),'b'),((0,0),(14/17,56/17),'proj'),((14/17,56/17),(2,3),'orth')])
p.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
checks=[]
x=s.symbols('x',real=True)
def eq(name,a,b):assert s.simplify(a-b)==0,(name,a,b);checks.append(name)
for val in[1+s.sqrt(6)/2,1-s.sqrt(6)/2]:eq('26 unsquared angle',((x+2)/s.sqrt(6*(1+x*x))).subs(x,val),s.sqrt(2)/2)
for sign in[-1,1]:
 u=s.Matrix([(3-sign*4*s.sqrt(3))/10,(4+sign*3*s.sqrt(3))/10]);eq('28 unit length',u.dot(u),1);eq('28 angle',u.dot(s.Matrix([3,4]))/5,s.Rational(1,2))
a=s.Matrix(s.symbols('a1:4',real=True));b=s.Matrix(s.symbols('b1:4',real=True));r=s.Matrix(s.symbols('x1:4',real=True))
eq('54 sphere completion',(r-a).dot(r-b),(r-(a+b)/2).dot(r-(a+b)/2)-(a-b).dot(a-b)/4)
eq('60 diagonal dot',(a+b).dot(a-b),a.dot(a)-b.dot(b))
eq('63 parallelogram',(a+b).dot(a+b)+(a-b).dot(a-b),2*a.dot(a)+2*b.dot(b))
xv=s.Matrix([1,4]);bv=s.Matrix([2,3]);proj=s.Rational(14,17)*xv;eq('46 residual perpendicular',(bv-proj).dot(xv),0)
eq('49 work',s.Matrix([8,-6,9]).dot(s.Matrix([6,2,12])),144)
eq('57 bond cosine',s.Matrix([1,-1,-1]).dot(s.Matrix([-1,1,-1]))/3,-s.Rational(1,3))
(R/'exercise-checks/s12-3-report.json').write_text(json.dumps({'passed':len(checks),'checks':checks,'sourceVisualPages':[927,928,929],'extraConditions':['24(c)zero-vector case','31 tangency angle0','38 both gamma values','45 projection requires nonzero a','54 zero-radius degeneracy']},indent=2)+'\n');print('PASS',len(checks),'independent checks')
