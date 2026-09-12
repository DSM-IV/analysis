"""Original planar diagrams, no external plotting dependencies."""
import math,html
from plot_15 import ASSETS,attach
def planar(name,title,polygons,labels=(),curves=()):
 pts=[p for poly in polygons for p in poly]+[p for line in curves for p in line]+[(0,0)];xmin=min(x for x,y in pts);xmax=max(x for x,y in pts);ymin=min(y for x,y in pts);ymax=max(y for x,y in pts);scale=min(420/max(.1,xmax-xmin),260/max(.1,ymax-ymin))
 def xy(p):return(300+(p[0]-(xmin+xmax)/2)*scale,245-(p[1]-(ymin+ymax)/2)*scale)
 out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 450" role="img"><title>{html.escape(title)}</title><rect width="600" height="450" fill="#fbfcff"/><text x="25" y="30" font-family="sans-serif" font-size="20">{html.escape(title)}</text>']
 for poly in polygons:out.append('<polygon points="'+' '.join(f'{a:.2f},{b:.2f}' for a,b in map(xy,poly))+'" fill="#91b7e5" fill-opacity=".65" stroke="#27598c" stroke-width="2"/>')
 for line in curves:out.append('<polyline points="'+' '.join(f'{a:.2f},{b:.2f}' for a,b in map(xy,line))+'" fill="none" stroke="#a44841" stroke-width="2"/>')
 for line,label in [([(xmin-.15,0),(xmax+.15,0)],'x'),([(0,ymin-.15),(0,ymax+.15)],'y')]:
  aa,bb=map(xy,line);out.append(f'<path d="M{aa[0]},{aa[1]}L{bb[0]},{bb[1]}" stroke="#253956"/><text x="{bb[0]+6}" y="{bb[1]-5}" font-family="sans-serif" font-size="16">{label}</text>')
 for xx,yy,label in labels:
  aa,bb=xy((xx,yy));out.append(f'<text x="{aa+6:.2f}" y="{bb-7:.2f}" font-family="sans-serif" font-size="14">{html.escape(label)}</text>')
 out.append('</svg>');(ASSETS/name).write_text('\n'.join(out))
def polar_polygon(lo,hi,rlo,rhi,N=100):
 ts=[lo+(hi-lo)*i/N for i in range(N+1)]
 return[(rhi(t)*math.cos(t),rhi(t)*math.sin(t)) for t in ts]+[(rlo(t)*math.cos(t),rlo(t)*math.sin(t)) for t in reversed(ts)]
def strip_polygon(lo,hi,bottom,top,N=100):
 xs=[lo+(hi-lo)*i/N for i in range(N+1)]
 return[(x,bottom(x)) for x in xs]+[(x,top(x)) for x in reversed(xs)]
