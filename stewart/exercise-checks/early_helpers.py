"""Content and original SVG helpers for early Stewart exercise sections."""
import json,math,html,textwrap
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'exercise-content'
def pair(k,e=None):return {'ko':k,'en':k if e is None else e}
def same(s):return(s,s)
def fs(*s):return[same(r'\['+x+r'\]') for x in s]
class Book:
 def __init__(self,section,pages):self.section=section;self.pages=pages;self.E={}
 def add(self,n,pg,topic,statement,steps,answer,parts=[],hint=None,check=None):
  self.E[n]={'id':f'stewart9-exercise-{self.section}-{n}','number':n,'subparts':parts,'source':{'printedPage':pg,'pdfPage':pg+37},'topic':pair(*topic),'statement':pair(*statement),'hint':pair(*(hint or ('정의와 주어진 조건을 식으로 옮겨 단계별로 계산한다.','Translate the definitions and conditions into equations, then work through them.'))),'steps':{'ko':[k for k,e in steps],'en':[e for k,e in steps]},'answer':pair(*answer),'check':pair(*(check or ('결과를 원래 식과 경계 조건에 대입해 확인한다.','Substitute the result into the original equation and check the boundary conditions.'))),'conceptHref':f'../s{self.section.replace(".","-")}.html','status':'math-verified'}
 def save(self):
  ns=sorted(self.E);d={'section':self.section,'source':{'title':'Calculus','edition':9,'language':'en','printedPages':self.pages,'pdfPages':[x+37 for x in self.pages]},'scope':{'kind':'exercise','numbers':ns,'total':len(ns),'note':pair('원본을 대조한 문제·해설·검산.','Source-checked exercises, worked solutions, and verification.')},'exercises':[self.E[n]for n in ns]};(ROOT/f's{self.section.replace(".","-")}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+chr(10))
 def plot(self,n,items,caption=None):
  fn=f's{self.section.replace(".","-")}-{n}.svg';svg_surface(items,ROOT/'assets'/fn)
  cap=caption or ('자체 제작 그래프. 파랑·보라 선은 서로 다른 매개변수를 고정한 곡선이다. 무한곡면은 표시 범위로 잘랐다.','Original graph. Blue/purple lines fix the two parameters respectively. Unbounded surfaces are clipped to a display window.')
  self.E[n]['figure']={'src':'../exercise-content/assets/'+fn,'alt':pair(f'{self.section} {n}번의 자체 제작 그래프',f'Original graph for Exercise {self.section}.{n}'),'caption':pair(*cap)}
def svg_surface(items,path):
 # items=(function,(u0,u1),(v0,v1),title), multiple functions may share a panel via list.
 w,H=430,365;out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w*len(items)}" height="{H}" viewBox="0 0 {w*len(items)} {H}"><rect width="100%" height="100%" fill="#f8fafc"/>']
 for idx,(f,ur,vr,title)in enumerate(items):
  funcs=f if isinstance(f,list)else[f];lines=[]
  def project(p):
   x,y,z=p;return(.8*x-.6*y,.36*x+.48*y-.8*z)
  for fi,ff in enumerate(funcs):
   for fam in[0,1]:
    for i in range(13):
     pts=[]
     for j in range(81):
      a=i/12;b=j/80;u=ur[0]+(ur[1]-ur[0])*(a if fam==0 else b);v=vr[0]+(vr[1]-vr[0])*(b if fam==0 else a)
      try:p=project(ff(u,v));assert all(math.isfinite(t)for t in p)
      except (ValueError,ZeroDivisionError,OverflowError,AssertionError):continue
      pts.append(p)
     if pts:lines.append((['#0284c7','#9333ea','#d97706','#059669','#e11d48','#e11d48','#64748b','#64748b'][(fam+2*fi)%8],pts))
  ps=[p for c,l in lines for p in l];mn=[min(p[k]for p in ps)for k in[0,1]];mx=[max(p[k]for p in ps)for k in[0,1]];scale=min(350/(mx[0]-mn[0] or 1),250/(mx[1]-mn[1] or 1))
  def xy(p):return(idx*w+215+(p[0]-(mx[0]+mn[0])/2)*scale,168+(p[1]-(mx[1]+mn[1])/2)*scale)
  for ti,line in enumerate(textwrap.wrap(title,48)or['']):out.append(f'<text x="{idx*w+215}" y="{18+15*ti}" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#172b46">{html.escape(line)}</text>')
  for color,pts in lines:out.append('<polyline points="'+' '.join(f'{xy(p)[0]:.2f},{xy(p)[1]:.2f}'for p in pts)+f'" fill="none" stroke="{color}" stroke-width="1" opacity=".7"/>')
  ox=idx*w+375;oy=333
  for name,dx,dy in[('x',24,11),('y',-18,14),('z',0,-24)]:out.append(f'<path d="M{ox},{oy}l{dx},{dy}" stroke="#475569"/><text x="{ox+dx}" y="{oy+dy-3}" font-family="sans-serif" font-size="11">{name}</text>')
  out.append(f'<text x="{idx*w+15}" y="335" font-family="sans-serif" font-size="12" fill="#0284c7">First parameter fixed</text><text x="{idx*w+15}" y="352" font-family="sans-serif" font-size="12" fill="#9333ea">Second parameter fixed</text>')
 out.append('</svg>');path.write_text(''.join(out))
