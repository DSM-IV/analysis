"""Verified Calculus I content helpers; completion is explicit."""
from early_helpers import Book,pair,same,fs,ROOT
import json,math,html
from pathlib import Path
import sympy as s
import mpmath as mp
mp.mp.dps=35
class CalcBook(Book):
 def add(self,*args,**kwargs):
  args=tuple((a['ko'],a['en']) if isinstance(a,dict) and set(a)=={'ko','en'} else a for a in args)
  super().add(*args,**kwargs);self.E[args[0]]['status']='draft';self.E[args[0]]['conceptHref']='../../calc1/index.html'
 def verify(self,n,k,e):self.E[n]['check']=pair(k,e);self.E[n]['status']='math-verified'
 def save(self):
  super().save();p=ROOT/f's{self.section.replace(".","-")}.json';d=json.loads(p.read_text());d['source']['title']='Calculus';p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def tex(v):return s.latex(s.simplify(v))
def M(v):return fs(v)[0][0]
def area_svg(b,n,pieces,v,title):
 # Each tuple (a,b,upper,lower) is a verified vertical or horizontal strip.
 lines=[];polys=[]
 for lo,hi,up,dn in pieces:
  fu=s.lambdify(v,up,'math');fd=s.lambdify(v,dn,'math');us=[];ds=[]
  for i in range(181):
   t=float(lo)+(float(hi)-float(lo))*i/180
   try:u=float(fu(t));d=float(fd(t))
   except(ValueError,ZeroDivisionError):continue
   if not all(math.isfinite(a)for a in[u,d]):continue
   us.append((t,u)if str(v)=='x'else(u,t));ds.append((t,d)if str(v)=='x'else(d,t))
  lines.extend([('#0284c7',us),('#e11d48',ds)]);polys.append(us+ds[::-1])
 pts=[q for _,ls in lines for q in ls];mn=[min(p[k]for p in pts)for k in[0,1]];mx=[max(p[k]for p in pts)for k in[0,1]]
 for k in[0,1]:d=(mx[k]-mn[k]) or 1;mn[k]-=.1*d;mx[k]+=.1*d
 def xy(p):return(55+460*(p[0]-mn[0])/(mx[0]-mn[0]),320-260*(p[1]-mn[1])/(mx[1]-mn[1]))
 def pl(p):return' '.join(f'{xy(q)[0]:.3f},{xy(q)[1]:.3f}'for q in p)
 out=['<svg xmlns="http://www.w3.org/2000/svg" width="580" height="390" viewBox="0 0 580 390"><rect width="100%" height="100%" fill="#f8fafc"/>',f'<text x="290" y="26" text-anchor="middle" font-family="sans-serif" font-size="16">{html.escape(title)}</text>']
 for p in polys:out.append(f'<polygon points="{pl(p)}" fill="#dbeafe"/>')
 for color,ls in lines:out.append(f'<polyline points="{pl(ls)}" fill="none" stroke="{color}" stroke-width="2"/>')
 for k in[0,1]:
  if mn[k]<=0<=mx[k]:
   a=[mn[0],mn[1]];c=[mx[0],mx[1]];a[k]=c[k]=0;A=xy(a);C=xy(c);out.append(f'<path d="M{A[0]},{A[1]}L{C[0]},{C[1]}" stroke="#64748b"/>')
 lo,hi,up,dn=pieces[0];t=float(lo)+(float(hi)-float(lo))*.56;u=float(s.N(up.subs(v,t)));d=float(s.N(dn.subs(v,t)));A=xy((t,d)if str(v)=='x'else(d,t));B=xy((t,u)if str(v)=='x'else(u,t));out.append(f'<path d="M{A[0]},{A[1]}L{B[0]},{B[1]}" stroke="#059669" stroke-width="6" opacity=".65"/>')
 for label,x,y in [('x',535,325),('y',38,53),(f'x: {mn[0]:.3g} to {mx[0]:.3g}; y: {mn[1]:.3g} to {mx[1]:.3g}',55,353),('Blue/red: boundary curves. Green: a representative strip.',55,376)]:out.append(f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="12">{html.escape(label)}</text>')
 out.append('</svg>');fn=f's{b.section.replace(".","-")}-{n}.svg';(ROOT/'assets'/fn).write_text(''.join(out));b.E[n]['figure']={'src':'../exercise-content/assets/'+fn,'alt':pair('경계곡선과 대표 띠를 표시한 영역','Region with boundary curves and a representative strip'),'caption':pair('주어진 식으로 직접 그린 영역. 초록 띠의 길이는 두 경계값의 차, 두께는 적분 변수의 미소변화이다.','Region plotted directly from the given equations. The green strip has length equal to the boundary difference and infinitesimal thickness in the integration variable.')}
def area(b,n,page,st,pieces,v,setup_only=False,parts=[],numeric=False,extra=[]):
 pieces=[tuple(map(s.sympify,p))for p in pieces];ints=[];steps=list(extra);exact=0;nval=mp.mpf(0)
 for lo,hi,up,dn in pieces:
  diff=s.simplify(up-dn);assert float(diff.subs(v,(lo+hi)/2).evalf())>=-1e-8,(n,'negative strip')
  I=s.Integral(diff,(v,lo,hi));ints.append(I);num=mp.quad(s.lambdify(v,diff,'mpmath'),[mp.mpf(str(lo.evalf(34))),mp.mpf(str(hi.evalf(34)))]);nval+=num
  steps.append(('경계가 바뀌지 않는 구간에서 '+M(tex(lo)+r'\le '+str(v)+r'\le '+tex(hi))+(' 위−아래'if str(v)=='x'else' 오른쪽−왼쪽')+'를 적분한다.','On the interval '+M(tex(lo)+r'\le '+str(v)+r'\le '+tex(hi))+(' integrate top minus bottom.'if str(v)=='x'else' integrate right minus left.')))
  steps+=fs(s.latex(I))
  if not numeric:
   val=s.integrate(up,(v,lo,hi))-s.integrate(dn,(v,lo,hi));assert not val.has(s.Integral),(n,'unevaluated');exact+=val;assert abs(float(s.N(val,30))-float(num))<1e-7*max(1,abs(float(num))),(n,val,num)
   steps+=fs(s.latex(I)+'='+tex(val))
 if numeric:
  # Independent tanh-sinh vs Gauss-Legendre quadrature.
  n2=sum(mp.quadgl(s.lambdify(v,up-dn,'mpmath'),[float(lo),float(hi)],maxdegree=10)for lo,hi,up,dn in pieces);assert abs(n2-nval)<mp.mpf('1e-9'),(n,nval,n2)
  ans=M(r'A\approx'+f'{float(nval):.8f}')
 else:ans=M('A='+tex(exact))
 if setup_only:ans=M('A='+s.latex(s.Add(*ints,evaluate=False)));steps=[p for p in steps if not any('='in a and r'\int' in a for a in p)]
 b.add(n,page,('곡선 사이의 넓이','Area between curves'),st,steps,pair(ans),parts=parts)
 b.verify(n,f'각 구간의 경계 차가 음수가 아님을 확인하고, 독립 수치구적으로 총넓이 {float(nval):.10g}을 대조했다.',f'Checked the nonnegative strip differences and independently integrated them numerically: total area {float(nval):.10g}.')
 area_svg(b,n,pieces,v,f'{b.section}.{n}  Region and integration strip')
 return s.simplify(exact)if not numeric else nval
