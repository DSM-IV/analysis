from calc1_helpers import *
import textwrap

def planeplot(b,n,pts,reflect=False,title=None,caption=None,diagonal=False):
 lines=[('#0284c7',pts,'f')]
 if reflect:lines.append(('#e11d48',[(y,x)for x,y in pts],'inverse'))
 vs=[v for _,ps,_ in lines for p in ps for v in p];low=min(min(vs),0);high=max(max(vs),0);pad=(high-low)*.1 or 1;low-=pad;high+=pad
 def xy(p):return(75+370*(p[0]-low)/(high-low),425-370*(p[1]-low)/(high-low))
 def path(ps):return' '.join(f'{xy(p)[0]:.2f},{xy(p)[1]:.2f}'for p in ps)
 out=['<svg xmlns="http://www.w3.org/2000/svg" width="530" height="495" viewBox="0 0 530 495"><rect width="100%" height="100%" fill="#f8fafc"/>']
 for i,line in enumerate(textwrap.wrap(title or f'{b.section}.{n}  Function and inverse',62)):out.append(f'<text x="265" y="{20+16*i}" text-anchor="middle" font-family="sans-serif" font-size="14">{html.escape(line)}</text>')
 if reflect or diagonal:out.append(f'<polyline points="{path([(low,low),(high,high)])}" fill="none" stroke="#94a3b8" stroke-dasharray="6 5"/>')
 for i in range(5):
  t=low+(high-low)*i/4;xx,yy=xy((t,t));out.extend([f'<path d="M{xx},55V425M75,{yy}H445" stroke="#e2e8f0"/>',f'<text x="{xx}" y="444" text-anchor="middle" font-family="sans-serif" font-size="10">{t:.3g}</text>',f'<text x="66" y="{yy+4}" text-anchor="end" font-family="sans-serif" font-size="10">{t:.3g}</text>'])
 for ps in [[(low,0),(high,0)],[(0,low),(0,high)]]:out.append(f'<polyline points="{path(ps)}" fill="none" stroke="#64748b"/>')
 for color,ps,label in lines:out.append(f'<polyline points="{path(ps)}" fill="none" stroke="{color}" stroke-width="2.2"/>')
 for text_,X,Y,C in [('x',460,425,'#475569'),('y',70,49,'#475569'),('Blue: f',75,471,'#0284c7'),('Red: inverse'if reflect else'',175,471,'#e11d48'),('Dashed: y=x'if reflect or diagonal else'',320,471,'#64748b')]:out.append(f'<text x="{X}" y="{Y}" font-family="sans-serif" font-size="12" fill="{C}">{html.escape(text_)}</text>')
 out.append('</svg>');fn=f's{b.section.replace(".","-")}-{n}.svg';(ROOT/'assets'/fn).write_text(''.join(out));cap=caption or('같은 축척에서 좌표를 맞바꾸어 역함수를 직접 그렸다. 회색 대각선은 y=x이다.','Original inverse graph obtained by interchanging coordinates on equal-scale axes. The gray diagonal is y=x.')
 b.E[n]['figure']={'src':'../exercise-content/assets/'+fn,'alt':pair('함수의 자체 제작 평면 그래프','Original planar graph of the function'),'caption':pair(*cap)}
def points(fn,lo,hi,count=240):
 out=[]
 for i in range(count+1):
  t=lo+(hi-lo)*i/count
  try:z=fn(t)
  except(ValueError,ZeroDivisionError,OverflowError):continue
  if math.isfinite(z):out.append((t,z))
 return out
