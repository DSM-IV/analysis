"""Deterministic contour/domain SVGs using marching triangles, no dependencies."""
from early_helpers import *
def plots2d(panels,path):
 W,H=410,410;out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W*len(panels)}" height="{H}" viewBox="0 0 {W*len(panels)} {H}"><rect width="100%" height="100%" fill="#f8fafc"/>']
 for idx,p in enumerate(panels):
  f=p['f'];x0,x1=p.get('xr',(-3,3));y0,y1=p.get('yr',(-3,3));N=68;ox=idx*W
  def xy(x,y):return ox+45+320*(x-x0)/(x1-x0),350-300*(y-y0)/(y1-y0)
  def val(x,y):
   try:v=f(x,y);return v if math.isfinite(v)else None
   except(ValueError,ZeroDivisionError,OverflowError):return None
  for i in range(N):
   for j in range(N):
    if 'domain'in p:
     x=x0+(x1-x0)*(i+.5)/N;y=y0+(y1-y0)*(j+.5)/N
     if p['domain'](x,y):
      a,b=xy(x0+(x1-x0)*i/N,y0+(y1-y0)*(j+1)/N);out.append(f'<rect x="{a:.2f}" y="{b:.2f}" width="{320/N+.2:.2f}" height="{300/N+.2:.2f}" fill="#bae6fd"/>')
  for levelidx,k in enumerate(p.get('levels',[])):
   segs=[]
   for i in range(N):
    for j in range(N):
     q=[(x0+(x1-x0)*(i+di)/N,y0+(y1-y0)*(j+dj)/N)for di,dj in[(0,0),(1,0),(1,1),(0,1)]];v=[val(*a)for a in q]
     for tri in[(0,1,2),(0,2,3)]:
      pts=[]
      for a,b in zip(tri,tri[1:]+tri[:1]):
       if v[a]is None or v[b]is None or v[a]==v[b]:continue
       if(v[a]<=k<v[b])or(v[b]<=k<v[a]):
        t=(k-v[a])/(v[b]-v[a]);pts.append(xy(q[a][0]+t*(q[b][0]-q[a][0]),q[a][1]+t*(q[b][1]-q[a][1])))
      if len(pts)==2:segs.append(f'M{pts[0][0]:.2f},{pts[0][1]:.2f}L{pts[1][0]:.2f},{pts[1][1]:.2f}')
   color=['#0284c7','#9333ea','#059669','#e11d48','#d97706','#334155','#0891b2'][levelidx%7];out.append(f'<path d="{" ".join(segs)}" fill="none" stroke="{color}" stroke-width="1.1"/>');out.append(f'<text x="{ox+22+levelidx%4*97}" y="{378+levelidx//4*16}" font-family="sans-serif" font-size="11" fill="{color}">k={k:g}</text>')
  if x0<=0<=x1:a,c=xy(0,y0);_,d=xy(0,y1);out.append(f'<path d="M{a},{c}V{d}" stroke="#94a3b8"/>')
  if y0<=0<=y1:a,c=xy(x0,0);d,_=xy(x1,0);out.append(f'<path d="M{a},{c}H{d}" stroke="#94a3b8"/>')
  out.append(f'<rect x="{ox+45}" y="50" width="320" height="300" fill="none" stroke="#64748b"/>')
  for label,x,y in [(str(x0),ox+45,366),(str(x1),ox+345,366),(str(y0),ox+15,350),(str(y1),ox+15,55),('x',ox+378,352),('y',ox+42,40)]:out.append(f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="11">{html.escape(label)}</text>')
  out.append(f'<text x="{ox+205}" y="22" text-anchor="middle" font-family="sans-serif" font-size="13">{html.escape(p["title"])}</text>')
 out.append('</svg>');path.write_text(''.join(out))
def attach(b,n,panels,caption=None):
 fn=f's{b.section.replace(".","-")}-{n}.svg';plots2d(panels,ROOT/'assets'/fn);cap=caption or('자체 제작 등고선/정의역 그림. 선형 보간 격자로 그렸으며 열린 경계와 제외점은 본문의 정확한 조건을 따른다.','Original contour/domain diagram on an interpolated grid. Exact open boundaries and excluded points are specified in the text.');b.E[n]['figure']={'src':'../exercise-content/assets/'+fn,'alt':pair(f'{b.section}.{n} 자체 그래프',f'Original graph {b.section}.{n}'),'caption':pair(*cap)}
