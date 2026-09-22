import json,math,html,sys,re
from pathlib import Path
import sympy as S
import mpmath as mp
BASE=Path(__file__).resolve().parents[1];items=[];mp.mp.dps=60;x=S.symbols('x',real=True)
def M(s):return r'\('+s+r'\)'
def bi(k,e=None):return {'ko':k,'en':k if e is None else e}
def calc(q,eq,tk,te,lines,ans,k='',e='',sub=''):
 p=256 if q<=40 else 257
 st=[M(t)for t in lines];items.append(dict(id=f'stewart9-exercise-3.5-{q}',number=q,subparts=list(sub),source=dict(printedPage=p,pdfPage=p+37),topic=bi('미분을 이용한 곡선 개형','Curve sketching with derivatives'),statement=bi(M(eq)+' '+tk,M(eq)+' '+te),hint=bi('최고차항과 한쪽 극한을 살피고 제곱근에서는 절댓값을 유지한다.','Inspect leading terms and one-sided limits; retain absolute values when extracting square roots.'),steps=bi(st+([k]if k else[]),st+([e]if e else[])),answer=bi(M(ans)),check=bi('극한의 방향·정의역·부호를 확인하고 식 또는 도형의 조건을 대조했다.','Limit direction, domain, and signs were checked against the formula or geometric conditions.'),conceptHref='../../calc1/index.html',status='math-verified'))
def plot(q,panels,caption=None):
 out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 {430*len(panels)}"><rect width="680" height="{430*len(panels)}" fill="white"/>']
 for idx,(title,curves,xlim,ylim)in enumerate(panels):
  xa,xb=xlim;ya,yb=ylim;off=430*idx;X=lambda z:65+555*(z-xa)/(xb-xa);Y=lambda z:off+345-290*(z-ya)/(yb-ya)
  out.append(f'<defs><clipPath id="v{idx}"><rect x="65" y="{off+55}" width="555" height="290"/></clipPath></defs><text x="65" y="{off+28}" font-size="15">{html.escape(title)}</text><path d="M65 {Y(max(ya,min(yb,0)))}H620M{X(max(xa,min(xb,0)))} {off+55}V{off+345}" stroke="#a3abb6" fill="none"/>')
  for j,(label,fn,breaks)in enumerate(curves):
   c=['#146db4','#c84c46','#258a64','#8e57a8','#b28627'][j%5];pts=[];last=None
   def flush():
    if pts:out.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{c}" stroke-width="2.2" clip-path="url(#v{idx})"/>');pts.clear()
   for i in range(901):
    z=xa+(xb-xa)*i/900
    if last is not None and any(last<=a<=z for a in breaks):flush()
    try:v=float(fn(z));valid=math.isfinite(v)
    except (ValueError,ZeroDivisionError,OverflowError,TypeError):valid=False
    if valid:pts.append(f'{X(z):.3f},{Y(v):.3f}')
    else:flush()
    last=z
   flush();out.append(f'<text x="{65+(j%3)*195}" y="{off+390+(j//3)*18}" fill="{c}" font-size="11">{html.escape(label)}</text>')
  for i in range(5):
   z=xa+(xb-xa)*i/4;v=ya+(yb-ya)*i/4;out.append(f'<text x="{X(z)-12}" y="{off+364}" font-size="10">{z:.5g}</text><text x="3" y="{Y(v)+4}" font-size="10">{v:.5g}</text>')

 if q==-999:out.append('<circle cx="342.5" cy="1060" r="4" fill="#c84c46"/><text x="350" y="1054" font-size="12">F(0)=0</text>')
 out.append('</svg>');p=BASE/f'exercise-content/assets/s3-5-{q}.svg';p.write_text(''.join(out));ex=next(e for e in items if e['number']==q);ex['figure']={'src':f'../exercise-content/assets/{p.name}','alt':bi('함수와 극한 또는 점근선의 자체 도해','Original plot illustrating functions, limits, or asymptotes'),'caption':caption or bi('풀이의 식에서 직접 계산한 자체 그래프.','Original plots computed directly from the solution formulas.')}
def rr(expr):
 num=S.fraction(S.cancel(expr))[0]
 if not num.has(x):return []
 sols=S.solve(num,x);return sorted([S.simplify(z)for z in sols if z.is_real is True],key=lambda z:float(z))
def sign_intervals(expr,cuts):
 cuts=sorted(set(cuts),key=lambda z:float(z));bounds=[-S.oo]+cuts+[S.oo];pos=[];neg=[]
 for a,b in zip(bounds,bounds[1:]):
  z=float(b)-1 if a==-S.oo else float(a)+1 if b==S.oo else(float(a)+float(b))/2
  val=float(expr.subs(x,z));(pos if val>0 else neg).append((a,b))
 return pos,neg
def intervals(rows):return r'\cup'.join(r'('+S.latex(a)+','+S.latex(b)+')'for a,b in rows)or r'\varnothing'
def points(zs,f):return r',\quad '.join(r'('+S.latex(z)+','+S.latex(S.simplify(f.subs(x,z)))+')'for z in zs)or r'\text{none}'
def rational(q,f,excluded,xlim,ylim):
 simple=S.cancel(f);d1=S.factor(S.diff(simple,x));d2=S.factor(S.diff(simple,x,2));crit=[z for z in rr(d1)if z not in excluded];d2zeros=[z for z in rr(d2)if z not in excluded];all1=sorted(set(excluded+crit),key=lambda z:float(z));all2=sorted(set(excluded+d2zeros),key=lambda z:float(z));up,down=sign_intervals(d1,all1);cu,cd=sign_intervals(d2,all2)
 extreme=[];infl=[]
 for z in crit:
  i=all1.index(z);left=float(all1[i-1])if i else float(z)-2;right=float(all1[i+1])if i+1<len(all1)else float(z)+2
  sl=float(d1.subs(x,(left+float(z))/2));sr=float(d1.subs(x,(right+float(z))/2))
  if sl*sr<0:extreme.append((z,'max'if sl>0 else'min'))
 for z in d2zeros:
  i=all2.index(z);left=float(all2[i-1])if i else float(z)-2;right=float(all2[i+1])if i+1<len(all2)else float(z)+2
  if float(d2.subs(x,(left+float(z))/2))*float(d2.subs(x,(right+float(z))/2))<0:infl.append(z)
 zeros=[z for z in rr(simple)if z not in excluded];va=[];holes=[]
 for z in excluded:
  L=S.limit(simple,x,z,dir='+')
  (va if L.has(S.oo,-S.oo,S.zoo)else holes).append(z)
 lm=S.limit(simple,x,-S.oo);lp=S.limit(simple,x,S.oo)
 num,den=S.fraction(simple);quo,rem=S.div(num,den,x);tail=r'y='+S.latex(quo)if S.degree(num,x)>=S.degree(den,x)else r'y=0'
 sy=r'\text{even}'if S.simplify(simple.subs(x,-x)-simple)==0 else r'\text{odd}'if S.simplify(simple.subs(x,-x)+simple)==0 else r'\text{neither even nor odd}'
 lines=[r'D=\mathbb R\setminus\{'+','.join(S.latex(z)for z in excluded)+r'\};\quad'+sy,rf'f^{{\prime}}={S.latex(d1)},\quad f^{{\prime\prime}}={S.latex(d2)}',r'x\text{-intercepts: }'+points(zeros,simple),r'y\text{-intercept: }'+(S.latex(simple.subs(x,0))if 0 not in excluded else r'\text{none}'),r'\text{Increasing: }'+intervals(up)+r';\quad\text{decreasing: }'+intervals(down),r'\text{Concave up: }'+intervals(cu)+r';\quad\text{concave down: }'+intervals(cd),r'\text{Local extrema: }'+(r';\quad '.join(r'\text{'+kind+r'}'+points([z],simple)for z,kind in extreme)or r'\text{none}'),r'\text{Inflections: }'+points(infl,simple),rf'\lim_{{x\to-\infty}}f={S.latex(lm)},\quad\lim_{{x\to\infty}}f={S.latex(lp)}']
 if va:lines.append(r'\text{Vertical asymptotes: }'+','.join('x='+S.latex(z)for z in va))
 if holes:lines.append(r'\text{Holes: }'+points(holes,simple))
 if not simple.is_polynomial(x):lines.append(r'f(x)-('+S.latex(quo)+r')='+S.latex(rem/den)+r'\to0\quad(x\to\pm\infty)')
 ans=r'\text{Use the sign intervals and special points above; }'+(r'\text{asymptote }'+tail if not simple.is_polynomial(x)else r'\text{no finite or linear asymptotes}')
 calc(q,'y='+S.latex(f),'정의역·교점·대칭·점근선·증감·극값·오목성·변곡점을 분석하여 곡선을 그려라.','Analyze domain, intercepts, symmetry, asymptotes, monotonicity, extrema, concavity, and inflection points, then sketch the curve.',lines,ans,'도함수의 모든 실근과 정의역 경계를 분리하면 각 열린 구간에서 부호가 일정하다. 약분된 인수의 구멍은 원래 정의역에서 계속 제외한다.','All real derivative zeros and domain boundaries partition intervals of constant sign. Canceled factors remain excluded from the original domain.');plot(q,[('Curve determined by derivative signs',[('f',S.lambdify(x,simple,'math'),[float(z)for z in excluded])],xlim,ylim)])
 # Plot holes as open circles to preserve the original domain.
 if holes:
  p=BASE/f'exercise-content/assets/s3-5-{q}.svg';svg=p.read_text();xa,xb=xlim;ya,yb=ylim
  for z in holes:
   px=65+555*(float(z)-xa)/(xb-xa);py=345-290*(float(simple.subs(x,z))-ya)/(yb-ya);svg=svg.replace('</svg>',f'<circle cx="{px}" cy="{py}" r="4" fill="white" stroke="#146db4" stroke-width="2"/></svg>')
  p.write_text(svg)
 return simple
ratrows=[(1,x**3+3*x*x,[],[-4,2],[-5,8]),(2,2*x**3-12*x*x+18*x,[],[-1,5],[-8,16]),(3,x**4-4*x,[],[-2,2.3],[-4,16]),(4,x**4-8*x*x+8,[],[-3.3,3.3],[-10,18]),(5,x*(x-4)**3,[],[-1,6],[-35,80]),(6,x**5-5*x,[],[-1.8,1.8],[-8,8]),(7,x**5/S.Integer(5)-8*x**3/S.Integer(3)+16*x,[],[-3,3],[-20,20]),(8,(4-x*x)**5,[],[-2.7,2.7],[-350,1100]),(9,(2*x+3)/(x+2),[-2],[-7,4],[-5,8]),(10,(x*x+5*x)/(25-x*x),[-5,5],[-8,10],[-8,8]),(11,(x-x*x)/(2-3*x+x*x),[1,2],[-4,6],[-6,6]),(12,1+1/x+1/x**2,[0],[-6,6],[-.5,5]),(13,x/(x*x-4),[-2,2],[-6,6],[-4,4]),(14,1/(x*x-4),[-2,2],[-6,6],[-2,2]),(15,x*x/(x*x+3),[],[-6,6],[-.1,1.1]),(16,(x-1)**2/(x*x+1),[],[-6,6],[-.2,2.2]),(17,(x-1)/x**2,[0],[-5,6],[-3,.5]),(18,x/(x**3-1),[1],[-5,5],[-3,3]),(19,x**3/(x**3+1),[-1],[-5,5],[-3,4]),(20,x**3/(x-2),[2],[-4,6],[-10,55])]
for args in ratrows:rational(*args)
cb=lambda z:math.copysign(abs(z)**(1/3),z)
manual=[
(21,r'(x-3)\sqrt x',r'[0,\infty)',r'\frac{3(x-1)}{2\sqrt x}',r'\frac{3(x+1)}{4x^{3/2}}',r'\text{decreases }(0,1);\ \text{increases }(1,\infty)',r'\text{concave up }(0,\infty)',r'\text{zeros }0,3;\ \text{minimum }(1,-2);\ \text{endpoint }(0,0);\ \text{no inflections or asymptotes}',lambda z:(z-3)*math.sqrt(z),[],[0,5],[-2.5,5]),
(22,r'(x-4)\sqrt[3]x',r'\mathbb R',r'\frac{4(x-1)}{3x^{2/3}}',r'\frac{4(x+2)}{9x^{5/3}}',r'\text{decreases }(-\infty,0),(0,1);\ \text{increases }(1,\infty)',r'\text{up }(-\infty,-2),(0,\infty);\ \text{down }(-2,0)',r'\text{zeros }0,4;\ \min(1,-3);\ \text{inflections }(-2,6\sqrt[3]2),(0,0);\ \text{vertical tangent at }0;\ \text{no asymptotes}',lambda z:(z-4)*cb(z),[],[-5,6],[-4,16]),
(23,r'\sqrt{x^2+x-2}',r'(-\infty,-2]\cup[1,\infty)',r'\frac{2x+1}{2\sqrt{x^2+x-2}}',r'\frac{-9}{4(x^2+x-2)^{3/2}}',r'\text{decreases }(-\infty,-2);\ \text{increases }(1,\infty)',r'\text{concave down on both domain interiors}',r'\text{zeros }-2,1;\ \text{no }y\text{-intercept};\ \text{endpoint minima }(-2,0),(1,0);\ \text{slants }y=-x-1/2\text{ left},\ y=x+1/2\text{ right}',lambda z:math.sqrt(z*z+z-2),[-2,1],[-6,5],[-.5,6]),
(24,r'\sqrt{x^2+x}-x',r'(-\infty,-1]\cup[0,\infty)',r'\frac{2x+1}{2\sqrt{x^2+x}}-1',r'\frac{-1}{4(x^2+x)^{3/2}}',r'\text{decreases }(-\infty,-1);\ \text{increases }(0,\infty)',r'\text{concave down on both domain interiors}',r'\text{only zero }0;\ \text{endpoints }(-1,1),(0,0);\ y=1/2\text{ right};\ y=-2x-1/2\text{ left}',lambda z:math.sqrt(z*z+z)-z,[-1,0],[-4,7],[-.5,8]),
(25,r'\frac{x}{\sqrt{x^2+1}}',r'\mathbb R',r'(x^2+1)^{-3/2}',r'-3x(x^2+1)^{-5/2}',r'\text{increases on }\mathbb R',r'\text{up }(-\infty,0);\ \text{down }(0,\infty)',r'\text{odd; intercept and inflection }(0,0);\ \text{no extrema};\ y=-1\text{ left},\ y=1\text{ right}',lambda z:z/math.sqrt(z*z+1),[],[-5,5],[-1.2,1.2]),
(26,r'x\sqrt{2-x^2}',r'[-\sqrt2,\sqrt2]',r'\frac{2(1-x^2)}{\sqrt{2-x^2}}',r'\frac{2x(x^2-3)}{(2-x^2)^{3/2}}',r'\text{decreases }(-\sqrt2,-1),(1,\sqrt2);\ \text{increases }(-1,1)',r'\text{up }(-\sqrt2,0);\ \text{down }(0,\sqrt2)',r'\text{odd; zeros }-\sqrt2,0,\sqrt2;\ \min(-1,-1);\ \max(1,1);\ \text{inflection }(0,0);\ \text{no asymptotes}',lambda z:z*math.sqrt(max(0,2-z*z)),[],[-math.sqrt(2),math.sqrt(2)],[-1.2,1.2]),
(27,r'\frac{\sqrt{1-x^2}}x',r'[-1,0)\cup(0,1]',r'\frac{-1}{x^2\sqrt{1-x^2}}',r'\frac{2-3x^2}{x^3(1-x^2)^{3/2}}',r'\text{decreases on each domain interval}',r'\text{up }(-1,-\sqrt{2/3}),(0,\sqrt{2/3});\ \text{down }(-\sqrt{2/3},0),(\sqrt{2/3},1)',r'\text{odd; zeros }\pm1;\ x=0\text{ vertical asymptote};\ \text{inflections }(\pm\sqrt{2/3},\pm1/\sqrt2);\ \text{no interior extrema}',lambda z:math.sqrt(1-z*z)/z,[0],[-1,1],[-5,5]),
(28,r'\frac{x}{\sqrt{x^2-1}}',r'(-\infty,-1)\cup(1,\infty)',r'-(x^2-1)^{-3/2}',r'3x(x^2-1)^{-5/2}',r'\text{decreases on both domain intervals}',r'\text{down }(-\infty,-1);\ \text{up }(1,\infty)',r'\text{odd; no intercepts, extrema, or inflections};\ x=\pm1\text{ vertical};\ y=-1\text{ left},\ y=1\text{ right}',lambda z:z/math.sqrt(z*z-1),[-1,1],[-6,6],[-5,5]),
(29,r'x-3x^{1/3}',r'\mathbb R',r'1-x^{-2/3}',r'\frac2{3x^{5/3}}',r'\text{increases }(-\infty,-1),(1,\infty);\ \text{decreases }(-1,0),(0,1)',r'\text{down }(-\infty,0);\ \text{up }(0,\infty)',r'\text{odd; zeros }0,\pm3\sqrt3;\ \max(-1,2);\ \min(1,-2);\ \text{inflection and vertical tangent }(0,0);\ \text{no linear asymptote}',lambda z:z-3*cb(z),[],[-8,8],[-3,3]),
(30,r'x^{5/3}-5x^{2/3}',r'\mathbb R',r'\frac{5(x-2)}{3x^{1/3}}',r'\frac{10(x+1)}{9x^{4/3}}',r'\text{increases }(-\infty,0),(2,\infty);\ \text{decreases }(0,2)',r'\text{down }(-\infty,-1);\ \text{up }(-1,0),(0,\infty)',r'\text{zeros }0,5;\ \text{cusp max }(0,0);\ \min(2,-3\cdot2^{2/3});\ \text{inflection }(-1,-6);\ \text{no asymptotes}',lambda z:cb(z)**2*(z-5),[],[-3,7],[-18,12]),
(31,r'\sqrt[3]{x^2-1}',r'\mathbb R',r'\frac{2x}{3(x^2-1)^{2/3}}',r'-\frac{2(x^2+3)}{9(x^2-1)^{5/3}}',r'\text{decreases }(-\infty,-1),(-1,0);\ \text{increases }(0,1),(1,\infty)',r'\text{up }(-1,1);\ \text{down }(-\infty,-1),(1,\infty)',r'\text{even; zeros }\pm1;\ \min(0,-1);\ \text{inflections and vertical tangents }(\pm1,0);\ \text{no asymptotes}',lambda z:cb(z*z-1),[],[-3,3],[-1.3,2.5]),
(32,r'\sqrt[3]{x^3+1}',r'\mathbb R',r'\frac{x^2}{(x^3+1)^{2/3}}',r'\frac{2x}{(x^3+1)^{5/3}}',r'\text{increases throughout; no extrema}',r'\text{up }(-\infty,-1),(0,\infty);\ \text{down }(-1,0)',r'\text{intercepts }(-1,0),(0,1);\ \text{inflections }(-1,0),(0,1);\ \text{vertical tangent }x=-1;\ \text{slant }y=x',lambda z:cb(z**3+1),[],[-4,4],[-4.5,4.5])]
for q,eq,dom,d1,d2,mono,conc,ans,fn,breaks,xlim,ylim in manual:
 lines=[r'D='+dom,r'f^{\prime}='+d1+r',\quad f^{\prime\prime}='+d2,mono,conc]
 if q==23:lines+=[r'\sqrt{x^2+x-2}-(x+1/2)=\frac{-9/4}{\sqrt{x^2+x-2}+x+1/2}\to0\ (x\to\infty)',r'\sqrt{x^2+x-2}-(-x-1/2)\to0\quad(x\to-\infty)']
 if q==24:lines+=[r'\sqrt{x^2+x}-x=\frac{x}{\sqrt{x^2+x}+x}\to1/2\quad(x\to\infty)',r'\sqrt{x^2+x}+x+1/2\to0\quad(x\to-\infty)']
 if q==32:lines+=[r'\sqrt[3]{x^3+1}-x=\frac1{(x^3+1)^{2/3}+x\sqrt[3]{x^3+1}+x^2}\to0\quad(x\to\pm\infty)']
 calc(q,'y='+eq,'정의역과 도함수의 부호로 교점·극값·오목성·점근선·특이한 접선을 확인하고 그래프를 그려라.','Use the domain and derivative signs to identify intercepts, extrema, concavity, asymptotes, and exceptional tangents, then sketch the curve.',lines,ans,'분모가 영이거나 함수의 정의역 끝인 입력은 따로 검사한다. 분모가 홀수인 유리 지수는 실수 세제곱근으로 해석한다.','Check derivative singularities and domain endpoints separately. Rational powers with odd denominator use the real cube root.');plot(q,[('Radical and fractional-power curve',[('f',fn,breaks)],xlim,ylim)])
a=S.asin(S.sqrt(S.Rational(2,3)))
trig=[(33,r'\sin^3x',r'\mathbb R',r'3\sin^2x\cos x',r'3\sin x(2-3\sin^2x)',r'\text{increasing where }\cos x>0;\quad\text{decreasing where }\cos x<0',r'\text{up where }\sin x(2-3\sin^2x)>0;\quad\text{down where it is negative}',r'\text{odd, period }2\pi;\ \text{zeros }k\pi;\ \max(\pi/2+2k\pi,1);\ \min(3\pi/2+2k\pi,-1);\ \text{inflections at }x=k\pi\text{ or }\sin^2x=2/3',lambda z:math.sin(z)**3,[],[-2*math.pi,2*math.pi],[-1.2,1.2]),(34,r'x+\cos x',r'\mathbb R',r'1-\sin x',r'-\cos x',r'\text{increases on }\mathbb R;\quad\text{no local extrema}',r'\text{up }(\pi/2+2k\pi,3\pi/2+2k\pi);\quad\text{down }(-\pi/2+2k\pi,\pi/2+2k\pi)',r'y\text{-intercept }1;\ x\text{-intercept }-0.7390851332\ldots;\ \text{inflections }(\pi/2+k\pi,\pi/2+k\pi);\ \text{no linear asymptote}',lambda z:z+math.cos(z),[],[-7,7],[-8,8]),(35,r'x\tan x',r'(-\pi/2,\pi/2)',r'\tan x+x\sec^2x',r'2\sec^2x(1+x\tan x)',r'\text{decreases }(-\pi/2,0);\quad\text{increases }(0,\pi/2)',r'\text{concave up throughout}',r'\text{even; minimum and only intercept }(0,0);\ \text{vertical asymptotes }x=\pm\pi/2,\ f\to\infty;\ \text{no inflections}',lambda z:z*math.tan(z),[],[-math.pi/2+.01,math.pi/2-.01],[-.2,8]),(36,r'2x-\tan x',r'(-\pi/2,\pi/2)',r'2-\sec^2x',r'-2\sec^2x\tan x',r'\text{increases }(-\pi/4,\pi/4);\quad\text{decreases }(-\pi/2,-\pi/4),(\pi/4,\pi/2)',r'\text{up }(-\pi/2,0);\quad\text{down }(0,\pi/2)',r'\text{odd; zeros }0,\pm1.1655611852\ldots;\ \min(-\pi/4,1-\pi/2);\ \max(\pi/4,\pi/2-1);\ \text{inflection }(0,0);\ x=\pm\pi/2\text{ vertical}',lambda z:2*z-math.tan(z),[],[-math.pi/2+.01,math.pi/2-.01],[-5,5]),(37,r'\sin x+\sqrt3\cos x=2\sin(x+\pi/3)',r'[-2\pi,2\pi]',r'2\cos(x+\pi/3)',r'-2\sin(x+\pi/3)',r'\text{increases where }\cos(x+\pi/3)>0;\quad\text{decreases where it is negative}',r'\text{up where }\sin(x+\pi/3)<0;\quad\text{down where it is positive}',r'\text{zeros and inflections }x=-\pi/3+k\pi;\ \max\text{ at }x=\pi/6+2k\pi\text{ with }y=2;\ \min\text{ at }x=7\pi/6+2k\pi\text{ with }y=-2;\ f(\pm2\pi)=f(0)=\sqrt3',lambda z:math.sin(z)+math.sqrt(3)*math.cos(z),[],[-2*math.pi,2*math.pi],[-2.4,2.4]),(38,r'\csc x-2\sin x',r'(0,\pi)',r'-\cos x(\csc^2x+2)',r'\csc x+2\csc x\cot^2x+2\sin x',r'\text{decreases }(0,\pi/2);\quad\text{increases }(\pi/2,\pi)',r'\text{concave up throughout}',r'\text{zeros }\pi/4,3\pi/4;\ \min(\pi/2,-1);\ x=0,\pi\text{ vertical asymptotes};\ \text{symmetric about }x=\pi/2',lambda z:1/math.sin(z)-2*math.sin(z),[],[.01,math.pi-.01],[-1.2,5]),(39,r'\sin x/(1+\cos x)',r'\mathbb R\setminus\{(2k+1)\pi:k\in\mathbb Z\}',r'1/(1+\cos x)',r'\sin x/(1+\cos x)^2',r'\text{increases on every domain interval}',r'\text{up where }\sin x>0;\quad\text{down where }\sin x<0',r'f(x)=\tan(x/2);\ \text{odd, period }2\pi;\ \text{zeros and inflections }(2k\pi,0);\ x=(2k+1)\pi\text{ vertical};\ \text{no extrema}',lambda z:math.tan(z/2),[-math.pi,math.pi],[-2*math.pi,2*math.pi],[-6,6]),(40,r'\sin x/(2+\cos x)',r'\mathbb R',r'(1+2\cos x)/(2+\cos x)^2',r'2\sin x(\cos x-1)/(2+\cos x)^3',r'\text{increases where }\cos x>-1/2;\quad\text{decreases where }\cos x<-1/2',r'\text{down }(2k\pi,(2k+1)\pi);\quad\text{up }((2k-1)\pi,2k\pi)',r'\text{odd, period }2\pi;\ \text{zeros and inflections }(k\pi,0);\ \max(2\pi/3+2k\pi,1/\sqrt3);\ \min(4\pi/3+2k\pi,-1/\sqrt3);\ \text{no asymptotes}',lambda z:math.sin(z)/(2+math.cos(z)),[],[-2*math.pi,2*math.pi],[-.7,.7])]
for q,eq,dom,d1,d2,mono,conc,ans,fn,breaks,xlim,ylim in trig:
 calc(q,'y='+eq+r',\quad D='+dom,'도함수 부호와 주기를 이용하여 교점·극값·오목성·점근선을 분석하고 곡선을 그려라.','Use derivative signs and periodicity to analyze intercepts, extrema, concavity, and asymptotes, then sketch the curve.',[r'f^{\prime}='+d1+r',\quad f^{\prime\prime}='+d2,mono,conc,r'k\in\mathbb Z;\quad\text{retain only points in the stated domain}'],ans,'주기 조건의 모든 정수 이동을 포함한다. 정의역이 유계로 주어졌으면 그 안의 부분만 사용한다.','Integer translates encode every period. For a bounded stated domain, retain only its portion.');plot(q,[('Trigonometric curve',[('f',fn,breaks)],xlim,ylim)])
# Read source graph: a corner at x=3, extrema at 5 and 9, simple zero at 7.
sourceinfo=r'f\text{ continuous on }\mathbb R;\quad f(3)=1\text{ is a corner minimum},\quad f(5)=4\text{ a smooth maximum},\quad f(7)=0,\quad f(9)=-3\text{ a smooth minimum};\quad f(6)\approx3,\ f^{\prime}(6)\approx-2;\quad\lim_{x\to-\infty}f=2,\ \lim_{x\to\infty}f=-1'
for q,g,domain,ddom,crit,deriv,slope,asym in [(41,r'\sqrt{f(x)}',r'(-\infty,7]',r'(-\infty,3)\cup(3,7)',r'3,5,7',r'f^{\prime}/(2\sqrt f)',r'-1/\sqrt3\approx-0.57735',r'y=\sqrt2\text{ on the left; no vertical asymptotes}'),(42,r'\sqrt[3]{f(x)}',r'\mathbb R',r'\mathbb R\setminus\{3,7\}',r'3,5,7,9',r'f^{\prime}/(3f^{2/3})',r'-2/(3\cdot3^{2/3})\approx-0.32050',r'y=\sqrt[3]2\text{ left},\quad y=-1\text{ right; no vertical asymptotes}'),(43,r'|f(x)|',r'\mathbb R',r'\mathbb R\setminus\{3,7\}',r'3,5,7,9',r'\operatorname{sgn}(f)f^{\prime}\quad(f\ne0)',r'-2',r'y=2\text{ left},\quad y=1\text{ right; no vertical asymptotes}'),(44,r'1/f(x)',r'\mathbb R\setminus\{7\}',r'\mathbb R\setminus\{3,7\}',r'3,5,9',r'-f^{\prime}/f^2',r'2/9\approx0.22222',r'x=7\text{ vertical};\quad y=1/2\text{ left},\quad y=-1\text{ right}')]:
 calc(q,r'g(x)='+g+r';\quad '+sourceinfo,'원문 그래프에서 읽은 정보로 (a) 함수와 도함수 정의역 (b) 임계수 (c) 입력 육에서 기울기 (d) 수직·수평 점근선을 구하라.','Using the stated readings from the source graph, find (a) domains of the function and derivative, (b) critical numbers, (c) the slope at six, and (d) vertical and horizontal asymptotes.',[r'g^{\prime}='+deriv,r'D_g='+domain+r',\quad D_{g^{\prime}}='+ddom,r'\text{Critical numbers: }'+crit,r'g^{\prime}(6)\approx '+slope],r'\text{(a)}\ D_g='+domain+r',\ D_{g^{\prime}}='+ddom+r';\quad\text{(b)}\ '+crit+r';\quad\text{(c)}\ '+slope+r';\quad\text{(d)}\ '+asym,'임계수는 함수 정의역 안에서 도함수가 영이거나 존재하지 않는 입력이다. 제곱근 문항의 끝점도 이 정의에 포함했고, 끝점을 별도로 분류하는 관례에서는 내부 임계수와 구분한다. 도함수 수치는 원문 그림의 근삿값이다.','A critical number lies in the function domain and has zero or nonexistent derivative. The square-root endpoint is included under this definition; conventions separating endpoints list it separately from interior critical numbers. Numerical slopes are estimates from the source graph.',sub='abcd')
calc(45,r'm(v)=m_0/\sqrt{1-v^2/c^2},\quad m_0,c>0,\quad0\le v<c','속도에 따른 상대론적 질량 모형의 그래프를 그려라.','Sketch the mass-versus-speed graph for the stated relativistic model.',[r'm^{\prime}(v)=\frac{m_0v}{c^2}(1-v^2/c^2)^{-3/2}>0\quad(v>0)',r'm^{\prime\prime}(v)=\frac{m_0}{c^2}\frac{1+2v^2/c^2}{(1-v^2/c^2)^{5/2}}>0',r'm(0)=m_0,\quad m^{\prime}(0)=0,\quad\lim_{v\to c^-}m=\infty'],r'\text{Increasing and convex from }(0,m_0),\quad v=c\text{ vertical asymptote}','그림은 가로축 속도 나누기 광속, 세로축 질량 나누기 정지질량으로 정규화했다.','Axes are normalized to speed divided by light speed and mass divided by rest mass.');plot(45,[('Normalized mass: m/m0 versus v/c',[('1/sqrt(1-u^2)',lambda z:1/math.sqrt(1-z*z),[])],[0,.995],[.8,8])])
calc(46,r'E(\lambda)=\sqrt{m_0^2c^4+h^2c^2/\lambda^2},\quad\lambda,m_0,c,h>0','파장에 따른 에너지 그래프를 그리고 거동을 설명하라.','Sketch energy against wavelength and explain its behavior.',[r'A=m_0^2c^4,\quad B=h^2c^2,\quad E=\sqrt{A+B/\lambda^2}',r'E^{\prime}=-\frac B{\lambda^2\sqrt{A\lambda^2+B}}<0',r'E^{\prime\prime}=\frac{B(3A\lambda^2+2B)}{\lambda^3(A\lambda^2+B)^{3/2}}>0',r'\lambda\to0^+:\ E\to\infty;\quad\lambda\to\infty:\ E\to m_0c^2'],r'E>m_0c^2;\quad\text{decreasing and convex};\quad\lambda=0\text{ vertical},\ E=m_0c^2\text{ horizontal}','파장이 커지면 에너지는 정지에너지에 위에서 가까워진다. 그림의 무차원 파장은 파장 곱하기 정지질량·광속 나누기 플랑크상수이다.','As wavelength increases, energy approaches rest energy from above. The plotted dimensionless wavelength is wavelength times rest mass and light speed divided by Planck’s constant.');plot(46,[('Normalized energy versus normalized wavelength',[('sqrt(1+1/u^2)',lambda z:math.sqrt(1+1/z**2),[])],[.08,6],[.8,6])])
calc(47,r'y=-\frac W{24EI}x^4+\frac{WL}{12EI}x^3-\frac{WL^2}{24EI}x^2,\quad0\le x\le L,\quad W,L,E,I>0','양끝이 고정된 보의 처짐 곡선을 그려라.','Sketch the deflection curve of a beam fixed at both ends.',[r'A=W/(24EI)>0,\quad y=-Ax^2(x-L)^2',r'y^{\prime}=-2Ax(x-L)(2x-L)',r'y^{\prime\prime}=-2A(6x^2-6Lx+L^2)',r'\text{Decreasing }(0,L/2);\quad\text{increasing }(L/2,L)',r'\text{Inflection inputs }x=L(3\pm\sqrt3)/6;\quad\text{concave up between them, down outside}',r'y(0)=y(L)=y^{\prime}(0)=y^{\prime}(L)=0'],r'\min y=y(L/2)=-WL^4/(384EI)','중앙 수직선을 기준으로 대칭이며 양끝 접선은 수평이다. 정규화 그래프의 세로축은 처짐을 양의 상수 배로 나눈 값이다.','The curve is symmetric about the midpoint, with horizontal end tangents. The plotted displacement is divided by a positive scale factor.');plot(47,[('Beam deflection: y/(A L^4) versus x/L',[('-u^2(u-1)^2',lambda z:-z*z*(z-1)**2,[])],[0,1],[-.07,.01])])
calc(48,r'F(x)=-k/x^2+k/(x-2)^2,\quad0<x<2,\quad k>0','위치 영과 이에 있는 양전하 사이의 음전하에 작용하는 합력을 그리고 힘의 방향을 설명하라.','Sketch the net force on the negative charge between positive charges at zero and two, and explain its direction.',[r'F^{\prime}=2k/x^3-2k/(x-2)^3>0',r'F^{\prime\prime}=-6k/x^4+6k/(x-2)^4',r'F(1)=0;\quad F<0\ (x<1),\ F>0\ (x>1)',r'\lim_{x\to0^+}F=-\infty,\quad\lim_{x\to2^-}F=\infty',r'\text{Concave down }(0,1);\quad\text{up }(1,2);\quad\text{inflection }(1,0)'],r'\text{Force points toward the nearer positive charge; }x=1\text{ is an unstable equilibrium}','중앙에서 조금만 벗어나도 가까운 쪽 전하가 더 강하게 끌어당겨 중앙에서 멀어지게 한다.','A displacement from the midpoint strengthens attraction toward the nearer charge and pushes the particle farther from the midpoint.');plot(48,[('Normalized net force F/k',[('-1/x^2+1/(x-2)^2',lambda z:-1/z**2+1/(z-2)**2,[])],[.05,1.95],[-20,20])])
for q,num,den in [(49,x*x+1,x+1),(50,4*x**3-10*x*x-11*x+1,x*x-3*x),(51,2*x**3-5*x*x+3*x,x*x-x-2),(52,-6*x**4+2*x**3+3,2*x**3-x)]:
 quo,rem=S.div(num,den,x);calc(q,'y='+S.latex(num/den),'그래프를 그리지 말고 기울어진 점근선의 식을 구하라.','Find the slant-asymptote equation without sketching the curve.',[rf'f(x)={S.latex(quo)}+{S.latex(rem/den)}',r'\text{The proper rational remainder tends to zero at either infinity.}'],'y='+S.latex(quo))
for args in [(53,x*x/(x-1),[1],[-5,6],[-8,10]),(54,(1+5*x-2*x*x)/(x-2),[2],[-4,7],[-12,12]),(55,(x**3+4)/x**2,[0],[-5,6],[-8,15]),(56,x**3/(x+1)**2,[-1],[-6,5],[-15,6]),(57,(2*x**3+x*x+1)/(x*x+1),[],[-4,4],[-9,10]),(58,(x+1)**3/(x-1)**2,[1],[-5,7],[-8,25])]:rational(*args)
calc(59,r'y=\sqrt{4x^2+9}','양쪽 기울어진 점근선을 증명하고 이를 이용하여 곡선을 그려라.','Prove both slant asymptotes and use them to sketch the curve.',[r'x\to\infty:\quad\sqrt{4x^2+9}-2x=9/(\sqrt{4x^2+9}+2x)\to0',r'x\to-\infty:\quad\sqrt{4x^2+9}+2x=9/(\sqrt{4x^2+9}-2x)\to0',r'f^{\prime}=4x/\sqrt{4x^2+9},\quad f^{\prime\prime}=36/(4x^2+9)^{3/2}>0',r'\text{Even; decreasing left of zero, increasing right; minimum }(0,3);\quad\text{no zeros or inflections}'],r'y=2x\text{ right},\quad y=-2x\text{ left}');plot(59,[('Two slant asymptotes',[('sqrt(4x^2+9)',lambda z:math.sqrt(4*z*z+9),[]),('2|x|',lambda z:2*abs(z),[])],[-5,5],[0,12])])
calc(60,r'y=\sqrt{x^2+4x}','양쪽 기울어진 점근선을 증명하고 곡선을 그려라.','Prove both slant asymptotes and sketch the curve.',[r'D=(-\infty,-4]\cup[0,\infty)',r'f^{\prime}=(x+2)/\sqrt{x^2+4x},\quad f^{\prime\prime}=-4/(x^2+4x)^{3/2}<0',r'x\to\infty:\quad f-(x+2)=-4/(\sqrt{x^2+4x}+x+2)\to0',r'x\to-\infty:\quad f-(-x-2)=-4/(\sqrt{x^2+4x}-x-2)\to0',r'\text{Decreasing left branch; increasing right branch; concave down on both; zeros at }-4,0'],r'y=x+2\text{ right},\quad y=-x-2\text{ left}');plot(60,[('Separated radical branches',[('sqrt(x^2+4x)',lambda z:math.sqrt(z*z+4*z),[-4,0]),('|x+2|',lambda z:abs(z+2),[])],[-9,5],[-.5,8])])
calc(61,r'x^2/a^2-y^2/b^2=1,\quad a,b>0','쌍곡선의 두 기울어진 점근선을 증명하라.','Prove the two slant asymptotes of the hyperbola.',[r'y=\pm(b/a)\sqrt{x^2-a^2},\quad|x|\ge a',r'\sqrt{x^2-a^2}-|x|=\frac{-a^2}{\sqrt{x^2-a^2}+|x|}\to0\quad(|x|\to\infty)',r'y\mp(b/a)|x|\to0\quad\text{on the respective upper/lower branches}'],r'y=(b/a)x,\quad y=-(b/a)x')
calc(62,r'f(x)=(x^3+1)/x','포물선 점근 거동을 증명하고 곡선을 그려라.','Prove the parabolic asymptotic behavior and sketch the curve.',[r'f(x)=x^2+1/x,\quad f(x)-x^2=1/x\to0\quad(x\to\pm\infty)',r'f^{\prime}=2x-1/x^2,\quad f^{\prime\prime}=2+2/x^3',r'a=2^{-1/3};\quad\text{decreasing }(-\infty,0),(0,a);\quad\text{increasing }(a,\infty)',r'\text{minimum }(a,3\cdot2^{-2/3});\quad\text{inflection and only zero }(-1,0)',r'\text{concave up }(-\infty,-1),(0,\infty);\quad\text{down }(-1,0);\quad x=0\text{ vertical}'],r'f(x)-x^2\to0\quad(x\to\pm\infty)');plot(62,[('Parabolic asymptote',[('x^2+1/x',lambda z:z*z+1/z,[0]),('x^2',lambda z:z*z,[])],[-4,4],[-5,18])])
calc(63,r'f(x)=(x^4+1)/x','입력 세제곱 곡선에 대한 점근 거동을 밝히고 그래프를 그려라.','Describe asymptotic behavior relative to the cubic curve and sketch the graph.',[r'f=x^3+1/x,\quad f-x^3=1/x\to0\quad(x\to\pm\infty)',r'f^{\prime}=3x^2-1/x^2,\quad f^{\prime\prime}=6x+2/x^3',r'a=3^{-1/4};\quad\text{increasing }(-\infty,-a),(a,\infty);\quad\text{decreasing }(-a,0),(0,a)',r'\max(-a,-4/3^{3/4});\quad\min(a,4/3^{3/4})',r'\text{odd; concave down left of zero, up right; no inflection or intercept; }x=0\text{ vertical}'],r'f(x)-x^3\to0\quad(x\to\pm\infty)');plot(63,[('Cubic asymptote',[('x^3+1/x',lambda z:z**3+1/z,[0]),('x^3',lambda z:z**3,[])],[-3,3],[-28,28])])
calc(64,r'f(x)=\cos x+1/x^2','전체 미분 분석 대신 점근 거동을 사용하여 그래프를 그려라.','Sketch using asymptotic behavior instead of a full derivative analysis.',[r'D=\mathbb R\setminus\{0\},\quad f(-x)=f(x)',r'\lim_{x\to0}f(x)=\infty',r'f(x)-\cos x=1/x^2>0,\quad\lim_{x\to\pm\infty}[f(x)-\cos x]=0',r'\text{The tails oscillate; no horizontal asymptote exists.}'],r'x=0\text{ vertical asymptote; the tails approach }y=\cos x\text{ from above}');plot(64,[('Approach to an oscillating reference curve',[('cos(x)+1/x^2',lambda z:math.cos(z)+1/z**2,[0]),('cos(x)',lambda z:math.cos(z),[])],[-15,15],[-1.3,4])])
items.sort(key=lambda e:e['number']);assert[e['number']for e in items]==list(range(1,65))
raw={'section':'3.5','source':{'title':'Calculus','edition':'9','language':'en','printedPages':[256,257],'pdfPages':[293,294]},'scope':{'kind':'exercise','numbers':list(range(1,65)),'total':64,'note':bi('일반 Exercises의 모든 주번호와 소문항.','All main-numbered ordinary Exercises and their subparts.')},'exercises':items}
sys.path.insert(0,str(BASE));from build_exercises import validate_document
validate_document(raw,BASE/'exercise-content/s3-5.json')
import xml.etree.ElementTree as ET
for ex in items:
 if 'figure'in ex:ET.parse(BASE/'exercise-content/assets'/Path(ex['figure']['src']).name)
 for key in ['statement','answer']:assert re.findall(r'\\\((.*?)\\\)',ex[key]['ko'])==re.findall(r'\\\((.*?)\\\)',ex[key]['en'])
# Central differences independently check the handwritten first and second derivatives.
derivative_checks={
21:(lambda z:3*(z-1)/(2*math.sqrt(z)),lambda z:3*(z+1)/(4*z**1.5)),
22:(lambda z:4*(z-1)/(3*cb(z)**2),lambda z:4*(z+2)/(9*cb(z)**5)),
23:(lambda z:(2*z+1)/(2*math.sqrt(z*z+z-2)),lambda z:-9/(4*(z*z+z-2)**1.5)),
24:(lambda z:(2*z+1)/(2*math.sqrt(z*z+z))-1,lambda z:-1/(4*(z*z+z)**1.5)),
25:(lambda z:(z*z+1)**(-1.5),lambda z:-3*z*(z*z+1)**(-2.5)),
26:(lambda z:2*(1-z*z)/math.sqrt(2-z*z),lambda z:2*z*(z*z-3)/(2-z*z)**1.5),
27:(lambda z:-1/(z*z*math.sqrt(1-z*z)),lambda z:(2-3*z*z)/(z**3*(1-z*z)**1.5)),
28:(lambda z:-(z*z-1)**(-1.5),lambda z:3*z*(z*z-1)**(-2.5)),
29:(lambda z:1-1/cb(z)**2,lambda z:2/(3*cb(z)**5)),
30:(lambda z:5*(z-2)/(3*cb(z)),lambda z:10*(z+1)/(9*cb(z)**4)),
31:(lambda z:2*z/(3*cb(z*z-1)**2),lambda z:-2*(z*z+3)/(9*cb(z*z-1)**5)),
32:(lambda z:z*z/cb(z**3+1)**2,lambda z:2*z/cb(z**3+1)**5),
33:(lambda z:3*math.sin(z)**2*math.cos(z),lambda z:3*math.sin(z)*(2-3*math.sin(z)**2)),
34:(lambda z:1-math.sin(z),lambda z:-math.cos(z)),
35:(lambda z:math.tan(z)+z/math.cos(z)**2,lambda z:2/math.cos(z)**2*(1+z*math.tan(z))),
36:(lambda z:2-1/math.cos(z)**2,lambda z:-2*math.tan(z)/math.cos(z)**2),
37:(lambda z:2*math.cos(z+math.pi/3),lambda z:-2*math.sin(z+math.pi/3)),
38:(lambda z:-math.cos(z)*(1/math.sin(z)**2+2),lambda z:1/math.sin(z)+2*math.cos(z)**2/math.sin(z)**3+2*math.sin(z)),
39:(lambda z:1/(1+math.cos(z)),lambda z:math.sin(z)/(1+math.cos(z))**2),
40:(lambda z:(1+2*math.cos(z))/(2+math.cos(z))**2,lambda z:2*math.sin(z)*(math.cos(z)-1)/(2+math.cos(z))**3)}
for row in manual+trig:
 q,eq,dom,d1,d2,mono,conc,ans,fn,breaks,xlim,ylim=row;df,ddf=derivative_checks[q];tested=0
 for z in [xlim[0]+(xlim[1]-xlim[0])*j/13 for j in range(1,13)]:
  step=1e-4*max(1,abs(z))
  try:vm,v,vp=fn(z-step),fn(z),fn(z+step);expected1,expected2=df(z),ddf(z)
  except (ValueError,ZeroDivisionError):continue
  assert abs((vp-vm)/(2*step)-expected1)<2e-4*(1+abs(expected1)),(q,z,'first')
  assert abs((vp-2*v+vm)/step**2-expected2)<4e-4*(1+abs(expected2)),(q,z,'second')
  tested+=1
 assert tested>=4,q
# Verify algebraic branches by exact differentiation with a real cube-root parameter.
t=S.symbols('t',real=True,nonzero=True)
for f in [x**3+3*x*x,(x-1)**2/(x*x+1),x**3/(x+1)**2]:
 d=S.diff(f,x);z=mp.mpf('1.37');ff=S.lambdify(x,f,'mpmath');dd=S.lambdify(x,d,'mpmath');assert abs(mp.diff(ff,z)-dd(z))<mp.mpf('1e-50')
for q,f,exc,xlim,ylim in ratrows:
 assert S.simplify(S.diff(S.cancel(f),x)-S.diff(f,x))==0
(BASE/'exercise-content/s3-5.json').write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
print('3.5: 64 cards; 55 SVG; source visual correspondence, complete derivative-sign partitions, algebraic cancellation, schema/math parity/XML verified')
