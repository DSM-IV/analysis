"""Calculus I authoring and native SVG figures; numerical data remain explicit."""
from core_15 import *
import math,html
class CalcDoc(Doc):
 def add(self,*args,**kwargs):
  e=super().add(*args,**kwargs);e['conceptHref']='../../calc1/index.html';return e
 def fig(self,n,panels,caption=('직접 계산하거나 조건에 따라 그린 도해.','Diagram drawn directly from the calculations or stated conditions.')):
  name='s'+self.section.replace('.','-')+'-'+str(n)+'.svg'
  plot(name,panels)
  e=next(e for e in self.items if e['number']==n)
  e['figure']={'src':'../exercise-content/assets/'+name,'alt':pair('문항 '+str(n)+' 도해','Diagram for exercise '+str(n)),'caption':pair(*caption)}
def samples(f,a,b,n=160):return [(a+(b-a)*i/n,float(f(a+(b-a)*i/n))) for i in range(n+1)]
def panel(title,bounds,curves=(),dots=(),xticks=None,yticks=None,xlabel='x',ylabel='y'):
 return dict(title=title,bounds=bounds,curves=curves,dots=dots,xticks=xticks,yticks=yticks,xlabel=xlabel,ylabel=ylabel)
def plot(name,panels):
 width=640;height=370*len(panels);out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img">','<rect width="100%" height="100%" fill="white"/>','<g font-family="Arial,sans-serif" font-size="13">']
 colors=['#1d4ed8','#dc2626','#15803d','#9333ea']
 for j,p in enumerate(panels):
  a,b,c,d=p['bounds'];ox,oy=66,50+j*370;w,h=520,270
  X=lambda x:ox+w*(x-a)/(b-a);Y=lambda y:oy+h*(d-y)/(d-c)
  esc=html.escape
  out.append(f'<text x="30" y="{28+j*370}" font-size="17">{esc(p["title"])}</text><defs><clipPath id="clip{j}"><rect x="{ox}" y="{oy}" width="{w}" height="{h}"/></clipPath></defs>')
  xt=p['xticks'] if p['xticks'] is not None else [a+(b-a)*k/4 for k in range(5)]
  yt=p['yticks'] if p['yticks'] is not None else [c+(d-c)*k/4 for k in range(5)]
  for x in xt:
   out.append(f'<path d="M{X(x):.2f},{oy}v{h}" stroke="#e2e8f0"/><text x="{X(x):.2f}" y="{oy+h+19}" text-anchor="middle">{x:g}</text>')
  for y in yt:
   out.append(f'<path d="M{ox},{Y(y):.2f}h{w}" stroke="#e2e8f0"/><text x="{ox-8}" y="{Y(y)+4:.2f}" text-anchor="end">{y:g}</text>')
  ax=X(max(a,min(b,0)));ay=Y(max(c,min(d,0)))
  out.append(f'<path d="M{ox},{ay:.2f}h{w} M{ax:.2f},{oy}v{h}" stroke="#475569"/><text x="{ox+w}" y="{oy+h+40}" text-anchor="end">{esc(p["xlabel"])}</text><text x="{ox-30}" y="{oy-8}">{esc(p["ylabel"])}</text><g clip-path="url(#clip{j})">')
  for k,curve in enumerate(p['curves']):
   pts=curve['points'] if isinstance(curve,dict) else curve;color=curve.get('color',colors[k%4]) if isinstance(curve,dict) else colors[k%4]
   q=' '.join(f'{X(x):.2f},{Y(y):.2f}' for x,y in pts if math.isfinite(x) and math.isfinite(y))
   out.append(f'<polyline points="{q}" fill="none" stroke="{color}" stroke-width="2.2"/>')
  for dot in p['dots']:
   x,y,*other=dot;opened=other and other[0]=='open';out.append(f'<circle cx="{X(x):.2f}" cy="{Y(y):.2f}" r="4" fill="{"white" if opened else "#1d4ed8"}" stroke="#1d4ed8" stroke-width="1.7"/>')
  out.append('</g>')
 out.append('</g></svg>');(ROOT/'exercise-content/assets'/name).write_text('\n'.join(out))

def normalize_prose_inequalities(doc):
    """Keep literal comparison signs from being mistaken for HTML tags."""
    def rec(value):
        if isinstance(value,str):
            chunks=re.split(r'(\\\(.*?\\\)|\\\[.*?\\\])',value,flags=re.S)
            return ''.join(z if i%2 else z.replace('<',r'\(\lt\)') for i,z in enumerate(chunks))
        if isinstance(value,list):return [rec(z)for z in value]
        if isinstance(value,dict):return {k:rec(v)for k,v in value.items()}
        return value
    doc.items=rec(doc.items)
