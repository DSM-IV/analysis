"""Small original SVG curve plots with arrows and coordinate orientation."""
import math,html
from pathlib import Path
def draw_curves(path,panels):
 cols=min(2,len(panels));rows=math.ceil(len(panels)/cols);W=500;H=410
 out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {cols*W} {rows*H}"><defs><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0L10,5L0,10Z" fill="context-stroke"/></marker></defs><rect width="100%" height="100%" fill="#f8fafc"/>']
 for i,(title,fn,ranges,labels)in enumerate(panels):
  ox=(i%cols)*W;oy=(i//cols)*H
  def project(p):return(p[0],-p[1])if len(p)==2 else(.8*p[0]-.6*p[1],.36*p[0]+.48*p[1]-.8*p[2])
  curves=[]
  for ri,(lo,hi) in enumerate(ranges):
   current=fn[ri] if isinstance(fn,list) else fn
   curves.append([tuple(current(lo+(hi-lo)*j/500))for j in range(501)])
  dim=len(curves[0][0]);points=[p for curve in curves for p in curve];mins=[min(0,min(p[k]for p in points))for k in range(dim)];maxs=[max(0,max(p[k]for p in points))for k in range(dim)]
  ends=[]
  for k in range(dim):
   for val in[mins[k],maxs[k]]:
    pt=[0]*dim;pt[k]=val;ends.append(pt)
  allp=[project(p)for p in points+ends];mn=[min(p[k]for p in allp)for k in[0,1]];mx=[max(p[k]for p in allp)for k in[0,1]];sc=min(370/max(mx[0]-mn[0],1),280/max(mx[1]-mn[1],1))
  def xy(p):a,b=project(p);return(ox+250+(a-(mn[0]+mx[0])/2)*sc,oy+205+(b-(mn[1]+mx[1])/2)*sc)
  out.append(f'<text x="{ox+250}" y="{oy+26}" text-anchor="middle" font-family="sans-serif" font-size="18">{html.escape(title)}</text>')
  for k in range(dim):
   a,b=xy(ends[2*k]),xy(ends[2*k+1]);out.append(f'<path d="M{a[0]},{a[1]}L{b[0]},{b[1]}" stroke="#94a3b8" stroke-dasharray="4 3"/><text x="{b[0]+7}" y="{b[1]-8}" font-family="sans-serif" font-size="15">{labels[k]}</text>')
  for ci,curve in enumerate(curves):
   color=['#0284c7','#a855f7','#ea580c','#16a34a'][ci%4];coords=[xy(p)for p in curve];out.append('<polyline points="'+' '.join(f'{a:.2f},{b:.2f}'for a,b in coords)+f'" fill="none" stroke="{color}" stroke-width="2.2"/>')
   for j in[100,300,450]:
    a,b=coords[j],coords[j+6];out.append(f'<path d="M{a[0]},{a[1]}L{b[0]},{b[1]}" stroke="{color}" stroke-width="2.2" marker-end="url(#arr)"/>')
  rng=', '.join(f'[{lo:.3g}, {hi:.3g}]'for lo,hi in ranges);out.append(f'<text x="{ox+250}" y="{oy+388}" text-anchor="middle" font-family="sans-serif" font-size="14">t in {html.escape(rng)}; arrows: increasing t</text>')
 out.append('</svg>');Path(path).write_text(''.join(out))
