from calc1_helpers import *
def plots(b,n,panels,caption=None):
 """Panels: (title, xmin,xmax,ymin,ymax, [(label,function)], optional scatter)."""
 W=560;H=410;out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H*len(panels)}" viewBox="0 0 {W} {H*len(panels)}"><rect width="100%" height="100%" fill="#f8fafc"/>'];colors=['#0284c7','#dc2626','#16a34a','#a855f7','#d97706','#475569']
 for j,p in enumerate(panels):
  title,l,h,bot,top,curves,*other=p;yoff=H*j
  xy=lambda x,y:(65+450*(x-l)/(h-l),yoff+325-260*(y-bot)/(top-bot))
  out.append(f'<defs><clipPath id="p{j}"><rect x="65" y="{yoff+65}" width="450" height="260"/></clipPath></defs><text x="280" y="{yoff+25}" text-anchor="middle" font-family="sans-serif" font-size="15">{html.escape(title)}</text>')
  for i in range(5):
   xx=l+(h-l)*i/4; yy=bot+(top-bot)*i/4;X,Y=xy(xx,yy)
   out.append(f'<path d="M{X},{yoff+65}V{yoff+325}M65,{Y}H515" stroke="#dbe2ea"/><text x="{X}" y="{yoff+344}" text-anchor="middle" font-family="sans-serif" font-size="11">{xx:.3g}</text><text x="58" y="{Y+4}" text-anchor="end" font-family="sans-serif" font-size="11">{yy:.3g}</text>')
  X,Y=xy(0,0)
  if l<=0<=h:out.append(f'<path d="M{X},{yoff+65}V{yoff+325}" stroke="#475569"/>')
  if bot<=0<=top:out.append(f'<path d="M65,{Y}H515" stroke="#475569"/>')
  for k,(name,fn)in enumerate(curves):
   path=[];drawing=False
   for i in range(501):
    xx=l+(h-l)*i/500
    try:yy=float(fn(xx));valid=math.isfinite(yy)and abs(yy)<1e100
    except(ArithmeticError,ValueError):valid=False
    if not valid:drawing=False;continue
    X,Y=xy(xx,yy);path.append(('L'if drawing else'M')+f'{X:.2f},{Y:.2f}');drawing=True
   c=colors[k%len(colors)];out.append(f'<path d="{" ".join(path)}" fill="none" stroke="{c}" stroke-width="2" clip-path="url(#p{j})"/><text x="{65+225*(k%2)}" y="{yoff+366+17*(k//2)}" font-family="sans-serif" font-size="12" fill="{c}">{html.escape(name)}</text>')
  for xx,yy in(other[0]if other else[]):
   X,Y=xy(xx,yy);out.append(f'<circle cx="{X}" cy="{Y}" r="3.5" fill="#111827"/>')
 out.append('</svg>');fn=f's{b.section.replace(".","-").replace("*","-alt")}-{n}.svg';(ROOT/'assets'/fn).write_text(''.join(out));cap=caption or('주어진 식을 직접 계산해 그린 자체 그래프이다. 각 패널의 눈금을 사용한다.','Original graph computed from the stated formulas; use the scales shown in each panel.')
 b.E[n]['figure']={'src':'../exercise-content/assets/'+fn,'alt':pair('지수함수 자체 그래프','Original exponential-function graph'),'caption':pair(*cap)};b.save()
