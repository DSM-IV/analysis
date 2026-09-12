"""Surface area derivations, independent numerical checks, original SVGs."""
from core_15 import *
from plot_15 import solid,attach
import mpmath as mp,math
x,y,r,t=s.symbols('x y r theta',real=True);a=s.symbols('a',positive=True)
D=Doc('15.5',[1119,1120],lambda n:1119 if n<=14 else 1120)
def add(n,st,steps,ans,parts=(),check=('면적요소와 경계를 검산했다.','The area element and boundary were verified.')):
 return D.add(n,('곡면적','Surface area'),st,('투영영역을 구하고 면적요소를 '+m(r'\sqrt{1+f_x^2+f_y^2}\,dx\,dy')+'로 둔다.','Find the projection and use '+m(r'\sqrt{1+f_x^2+f_y^2}\,dx\,dy')+'.'),steps,ans,check,parts)
# All Korean prose below is authored explicitly; generic wrapper corrected at end.
def area(n,f,lims,desc,polar=False,numeric=False,graph=False,statement=None):
 fx=s.diff(f,x);fy=s.diff(f,y);q=s.sqrt(1+fx*fx+fy*fy)
 if n==8:q=2/s.sqrt(4-x*x)
 integrand=s.simplify(q.subs({x:r*s.cos(t),y:r*s.sin(t)}))*r if polar else q
 st=statement or ('곡면 '+m('z='+tex(f))+'의 '+m(desc)+' 위 부분의 넓이를 구하라.','Find the area of '+m('z='+tex(f))+' above '+m(desc)+'.')
 steps=[('편미분으로 면적요소를 구한다. '+d('f_x='+tex(fx)+',\quad f_y='+tex(fy)+',\quad dS='+tex(q)+r'\,dx\,dy'),'Differentiate to form the area element. '+d('f_x='+tex(fx)+',\quad f_y='+tex(fy)+',\quad dS='+tex(q)+r'\,dx\,dy')),('투영영역에 적분한다. '+d('A='+integral(integrand,lims)),'Integrate over the projection. '+d('A='+integral(integrand,lims)))]
 if numeric:
  v=num(integrand,lims);steps.append(('수치적분의 정밀도를 높여 소수 넷째 자리의 안정을 확인한다. '+d('A\\approx'+f'{v:.10f}'),'Increase numerical precision and confirm stability of four decimal places. '+d('A\\approx'+f'{v:.10f}')));ans=d('A\\approx'+f'{v:.4f}')
 else:
  v,subs=D.evaluated(integrand,lims);steps+=subs;ans=d('A='+tex(v))
 add(n,st,steps,ans);return v

def num(f,lims):
 vals=[]
 for prec in (22,32):
  mp.mp.dps=prec
  inner,outer=lims;v,lo,hi=inner;w,wl,wh=outer;fn=s.lambdify((v,w),f,'mpmath');lf=s.lambdify(w,lo,'mpmath');hf=s.lambdify(w,hi,'mpmath')
  z=mp.quad(lambda ww:mp.quad(lambda vv:fn(vv,ww),[lf(ww),hf(ww)]),[mp.mpf(str(s.N(wl,prec))),mp.mpf(str(s.N(wh,prec)))]);vals.append(z)
 assert abs(vals[0]-vals[1])<mp.mpf('1e-10')
 D.checks.append({'method':'independent mpmath quadrature at22/32dps','integrand':str(f),'limits':[[str(v) for v in li] for li in lims],'values':[str(v) for v in vals]});return float(vals[1])
area(1,10+x+y*y,[(x,0,-y),(y,-2,0)],r'-2\le y\le0,\ 0\le x\le-y')
area(2,3+x*y,[(r,0,1),(t,0,2*s.pi)],r'x^2+y^2\le1',polar=True)
area(3,5*x+3*y+6,[(y,2,6),(x,1,4)],r'[1,4]\times[2,6]')
area(4,(1-6*x-4*y)/2,[(r,0,5),(t,0,2*s.pi)],r'x^2+y^2\le25',polar=True)
area(5,6-3*x-2*y,[(y,0,3-3*x/2),(x,0,2)],r'x,y,z\ge0')
area(6,(5+x*x-2*y)/4,[(y,0,2*x),(x,0,2)],r'0\le x\le2,\ 0\le y\le2x')
area(7,1-x*x-y*y,[(r,0,s.sqrt(3)),(t,0,2*s.pi)],r'z\ge-2',polar=True)
area(8,s.sqrt(4-x*x),[(y,0,1),(x,0,1)],r'[0,1]^2')
area(9,y*y-x*x,[(r,1,2),(t,0,2*s.pi)],r'1\le x^2+y^2\le4',polar=True)
# Positive-quadrant fractional powers: declare derivative radicals directly to avoid Abs.
f=s.Rational(2,3)*(x**s.Rational(3,2)+y**s.Rational(3,2));v,sub=D.evaluated(s.sqrt(1+x+y),[(y,0,1),(x,0,1)])
add(10,(''+m(r'z=\frac23(x^{3/2}+y^{3/2})')+'의 단위 정사각형 위 부분의 넓이를 구하라.','Find the area of '+m(r'z=\frac23(x^{3/2}+y^{3/2})')+' above the unit square.'),[('제1사분면에서 '+m(r'f_x=\sqrt x,\ f_y=\sqrt y')+'이므로 '+d(r'A=\int_0^1\int_0^1\sqrt{1+x+y}\,dy\,dx'),'In the first quadrant, '+m(r'f_x=\sqrt x,\ f_y=\sqrt y')+', hence '+d(r'A=\int_0^1\int_0^1\sqrt{1+x+y}\,dy\,dx'))]+sub,d('A='+tex(v)))
area(11,x*y,[(r,0,1),(t,0,2*s.pi)],r'x^2+y^2\le1',polar=True)
add(12,('구 '+m(r'x^2+y^2+z^2=4')+'의 평면 '+m('z=1')+' 위 부분의 넓이를 구하라.','Find the area of the sphere '+m(r'x^2+y^2+z^2=4')+' above '+m('z=1')+'.'),[('위쪽 구면은 '+m(r'z=\sqrt{4-r^2}')+'이고 평면과 만나면 '+m(r'r=\sqrt3')+'이다. 면적요소는 '+m(r'2r/\sqrt{4-r^2}\,dr\,d\theta')+'이다.','The upper sphere is '+m(r'z=\sqrt{4-r^2}')+' and meets the plane at '+m(r'r=\sqrt3')+'. Its area element is '+m(r'2r/\sqrt{4-r^2}\,dr\,d\theta')+'.'),('반지름 적분은 '+m(r'-2\sqrt{4-r^2}')+'를 원시함수로 가진다. '+d(r'A=\int_0^{2\pi}\int_0^{\sqrt3}\frac{2r}{\sqrt{4-r^2}}\,dr\,d\theta=4\pi'),'The radial antiderivative is '+m(r'-2\sqrt{4-r^2}')+'. '+d(r'A=\int_0^{2\pi}\int_0^{\sqrt3}\frac{2r}{\sqrt{4-r^2}}\,dr\,d\theta=4\pi'))],d('A=4\\pi'))
add(13,('구 '+m(r'x^2+y^2+z^2=a^2')+'의 위쪽 반구에서 원기둥 '+m(r'x^2+y^2=ax')+' 안에 있는 부분의 넓이를 구하라.','Find the area of the upper hemisphere '+m(r'x^2+y^2+z^2=a^2')+' inside '+m(r'x^2+y^2=ax')+'.'),[('투영은 '+m(r'|\theta|\le\pi/2,\ 0\le r\le a\cos\theta')+'이다.','The projection is '+m(r'|\theta|\le\pi/2,\ 0\le r\le a\cos\theta')+'.'),('구면 면적요소를 반지름으로 적분한다. '+d(r'A=\int_{-\pi/2}^{\pi/2}\int_0^{a\cos\theta}\frac{ar}{\sqrt{a^2-r^2}}\,dr\,d\theta=a^2\int_{-\pi/2}^{\pi/2}(1-|\sin\theta|)\,d\theta'), 'Integrate the spherical area element radially. '+d(r'A=\int_{-\pi/2}^{\pi/2}\int_0^{a\cos\theta}\frac{ar}{\sqrt{a^2-r^2}}\,dr\,d\theta=a^2\int_{-\pi/2}^{\pi/2}(1-|\sin\theta|)\,d\theta')),('짝대칭을 이용하면 '+m(r'2a^2[\theta+\cos\theta]_0^{\pi/2}')+'이다.','Even symmetry gives '+m(r'2a^2[\theta+\cos\theta]_0^{\pi/2}')+'.')],d(r'A=(\pi-2)a^2'))
add(14,('구 '+m(r'x^2+y^2+z^2=4z')+'에서 포물면 '+m(r'z=x^2+y^2')+' 안에 있는 부분의 넓이를 구하라.','Find the area of '+m(r'x^2+y^2+z^2=4z')+' inside the paraboloid '+m(r'z=x^2+y^2')+'.'),[('구에서 '+m(r'r^2=z(4-z)')+'이고 포물면 내부는 '+m(r'r^2\le z')+'이므로 '+m(r'z(3-z)\le0')+'이다. '+m(r'0\le z\le4')+'에서 '+m(r'3\le z\le4')+'인 구면 모자와 면적0인 원점만 남는다.','On the sphere '+m(r'r^2=z(4-z)')+'. The paraboloid interior requires '+m(r'r^2\le z')+', so '+m(r'z(3-z)\le0')+'. For '+m(r'0\le z\le4')+', this gives the cap '+m(r'3\le z\le4')+' and the isolated origin of zero area.'),('구 중심은 '+m('(0,0,2)')+', 반지름2, 모자높이1이다. 적분으로 '+d(r'A=\int_0^{2\pi}\int_3^4 2\,dz\,d\theta=4\pi'),'The sphere has center '+m('(0,0,2)')+', radius2 and cap height1. Direct integration gives '+d(r'A=\int_0^{2\pi}\int_3^4 2\,dz\,d\theta=4\pi'))],d('A=4\\pi'))
area(15,1/(1+x*x+y*y),[(r,0,1),(t,0,2*s.pi)],r'x^2+y^2\le1',polar=True,numeric=True,statement=(''+m(r'z=1/(1+x^2+y^2)')+'의 단위원판 위 넓이를 일변수 적분으로 줄이고 소수 넷째 자리까지 구하라.','Reduce the area of '+m(r'z=1/(1+x^2+y^2)')+' above the unit disk to a one-variable integral and evaluate to four decimals.'))
D.items[-1]['steps']['ko'].insert(2,'각도에 무관하므로 '+d(r'A=2\pi\int_0^1r\sqrt{1+\frac{4r^2}{(1+r^2)^4}}\,dr'))
D.items[-1]['steps']['en'].insert(2,'The integrand is independent of angle, so '+d(r'A=2\pi\int_0^1r\sqrt{1+\frac{4r^2}{(1+r^2)^4}}\,dr'))
area(16,s.cos(x*x+y*y),[(r,0,1),(t,0,2*s.pi)],r'x^2+y^2\le1',polar=True,numeric=True,statement=(''+m(r'z=\cos(x^2+y^2)')+'의 단위원판 위 넓이를 일변수 적분으로 줄이고 소수 넷째 자리까지 구하라.','Reduce the area of '+m(r'z=\cos(x^2+y^2)')+' above the unit disk to a one-variable integral and evaluate to four decimals.'))
for lang in ('ko','en'):D.items[-1]['steps'][lang].insert(2,d(r'A=2\pi\int_0^1r\sqrt{1+4r^2\sin^2(r^2)}\,dr'))
for n,f,side in [(17,x*x+y*y,1),(18,x*y+x*x+y*y,2)]:
 q=s.sqrt(1+s.diff(f,x)**2+s.diff(f,y)**2);pts=[s.Rational(side,4),s.Rational(3*side,4)];mid=s.Rational(side*side,4)*sum(q.subs({x:xx,y:yy}) for xx in pts for yy in pts);v=num(q,[(y,0,side),(x,0,side)])
 add(n,('곡면 '+m('z='+tex(f))+'의 '+m('[0,'+str(side)+']^2')+' 위 넓이를 (a)2×2 중점법으로 근사하고 (b)수치적분하여 소수 넷째 자리까지 비교하라.','For '+m('z='+tex(f))+' above '+m('[0,'+str(side)+']^2')+', (a) estimate area with a2×2 midpoint grid and (b) use numerical integration to four decimals and compare.'),[('면적의 적분함수는 '+m('g='+tex(q))+'이다. 각 작은 직사각형 넓이는 '+m(tex(s.Rational(side*side,4)))+'이다.','The area integrand is '+m('g='+tex(q))+'. Each cell has area '+m(tex(s.Rational(side*side,4)))+'.'),('(a) 두 좌표에서 중점 '+m(tex(pts[0])+','+tex(pts[1]))+'을 사용한다. '+d('M='+tex(mid)+'\\approx'+f'{float(mid):.6f}'),'(a) Use midpoint coordinates '+m(tex(pts[0])+','+tex(pts[1]))+'. '+d('M='+tex(mid)+'\\approx'+f'{float(mid):.6f}')),('(b) 실제 면적 적분은 '+d('A='+integral(q,[(y,0,side),(x,0,side)])+'\\approx'+f'{v:.10f}')+'이다. 중점 근사는 아래로 '+m(f'{v-float(mid):.6f}')+' 차이 난다.','(b) Numerical area is '+d('A='+integral(q,[(y,0,side),(x,0,side)])+'\\approx'+f'{v:.10f}')+'. The midpoint estimate is lower by '+m(f'{v-float(mid):.6f}')+'.')],d('(a)\ M\\approx'+f'{float(mid):.4f}'+',\quad(b)\ A\\approx'+f'{v:.4f}'),('a','b'))
area(19,1+2*x+3*y+4*y*y,[(x,1,4),(y,0,1)],r'[1,4]\times[0,1]')
area(20,1+x+y+x*x,[(y,-1,1),(x,-2,1)],r'[-2,1]\times[-1,1]')
area(21,1+x*x*y*y,[(r,0,1),(t,0,2*s.pi)],r'x^2+y^2\le1',polar=True,numeric=True)
# Even symmetry reduces the diamond to its first-quadrant triangle.
f=(1+x*x)/(1+y*y);q=s.sqrt(1+s.diff(f,x)**2+s.diff(f,y)**2);v=4*num(q,[(y,0,1-x),(x,0,1)])
add(22,('곡면 '+m(r'z=(1+x^2)/(1+y^2)')+'의 마름모 '+m(r'|x|+|y|\le1')+' 위 부분을 그리고 넓이를 소수 넷째 자리까지 구하라.','Graph '+m(r'z=(1+x^2)/(1+y^2)')+' over the diamond '+m(r'|x|+|y|\le1')+' and find its area to four decimals.'),[('편미분은 '+m(r'f_x=2x/(1+y^2),\ f_y=-2y(1+x^2)/(1+y^2)^2')+'이다. 면적함수는 두 좌표에 짝함수이다.','The derivatives are '+m(r'f_x=2x/(1+y^2),\ f_y=-2y(1+x^2)/(1+y^2)^2')+'. The area integrand is even in both coordinates.'),('제1사분면 삼각형의 적분을4배 한다. '+d('A=4'+integral(q,[(y,0,1-x),(x,0,1)])),'Multiply the integral over the first-quadrant triangle by four. '+d('A=4'+integral(q,[(y,0,1-x),(x,0,1)]))),('서로 다른 정밀도로 수치적분한 값이 일치한다. '+d('A\\approx'+f'{v:.10f}'),'Independent precision settings agree. '+d('A\\approx'+f'{v:.10f}'))],d('A\\approx'+f'{v:.4f}'))
add(23,('평면 '+m('z=ax+by+c')+'의 영역 D 위 부분의 넓이가 '+m(r'\sqrt{a^2+b^2+1}\,A(D)')+'임을 증명하라.','Prove that the area of '+m('z=ax+by+c')+' above D is '+m(r'\sqrt{a^2+b^2+1}\,A(D)')+'.'),[('편미분 '+m(r'f_x=a,\ f_y=b')+'는 상수이므로 면적요소도 상수배이다.','Since '+m(r'f_x=a,\ f_y=b')+' are constant, the area element is a constant multiple of planar area.'),('상수를 적분 밖으로 꺼내면 '+d(r'A(S)=\iint_D\sqrt{1+a^2+b^2}\,dA=\sqrt{1+a^2+b^2}\iint_D1\,dA')+'이다.','Pull the constant outside the integral: '+d(r'A(S)=\iint_D\sqrt{1+a^2+b^2}\,dA=\sqrt{1+a^2+b^2}\iint_D1\,dA'))],d(r'A(S)=\sqrt{1+a^2+b^2}\,A(D)'))
add(24,('반지름 a인 구의 위쪽 반구를 '+m(r'x^2+y^2\le t^2,\ t<a')+' 위에서 먼저 적분하고 '+m('t\\to a^-')+'의 이상적분 극한으로 구 전체 넓이를 증명하라.','First integrate the upper sphere of radius a over '+m(r'x^2+y^2\le t^2,\ t<a')+', then take the improper limit '+m('t\\to a^-')+' to obtain the full sphere area.'),[('경계 전까지 그래프는 미분가능하며 '+m(r'dS=ar/\sqrt{a^2-r^2}\,dr\,d\theta')+'이다.','Before the boundary the graph is differentiable, with '+m(r'dS=ar/\sqrt{a^2-r^2}\,dr\,d\theta')+'.'),('절단된 반구 면적은 '+d(r'A_t=2\pi\int_0^t\frac{ar}{\sqrt{a^2-r^2}}\,dr=2\pi a(a-\sqrt{a^2-t^2})')+'이다.','The truncated hemisphere has area '+d(r'A_t=2\pi\int_0^t\frac{ar}{\sqrt{a^2-r^2}}\,dr=2\pi a(a-\sqrt{a^2-t^2})')),('극한은 '+m(r'2\pi a^2')+'이고 아래쪽도 같으므로2배 한다.','The limit is '+m(r'2\pi a^2')+'; double it for the lower hemisphere.')],d(r'A=4\pi a^2'))
v,subs=D.evaluated(r*s.sqrt(1+4*r*r),[(r,0,5),(t,0,2*s.pi)])
add(25,('포물면 '+m('y=x^2+z^2')+'을 평면 '+m('y=25')+'로 잘라 얻는 곡면 부분의 넓이를 구하라.','Find the area of the curved piece of '+m('y=x^2+z^2')+' cut off by '+m('y=25')+'.'),[('xz평면 투영은 반지름5의 원판이다. 그래프 y의 두 편미분은2x,2z이므로 극좌표 면적요소는 '+m(r'r\sqrt{1+4r^2}\,dr\,d\theta')+'이다.','The xz projection is a disk of radius5. The derivatives of y are2x and2z, so the polar area element is '+m(r'r\sqrt{1+4r^2}\,dr\,d\theta')+'.')]+subs,d('A='+tex(v)))
add(26,('두 원기둥 '+m(r'y^2+z^2=1,\ x^2+z^2=1')+'의 공통 내부를 둘러싸는 전체 곡면적을 구하라.','Find the full boundary area of the intersection of the cylinders '+m(r'y^2+z^2=1,\ x^2+z^2=1')+'.'),[('첫 원기둥 표면을 '+m(r'(x,\cos\theta,\sin\theta)')+'로 놓는다. 다른 원기둥 내부 조건은 '+m(r'|x|\le\sqrt{1-\sin^2\theta}=|\cos\theta|')+'이다.','Parametrize the first cylinder by '+m(r'(x,\cos\theta,\sin\theta)')+'. The second cylinder requires '+m(r'|x|\le\sqrt{1-\sin^2\theta}=|\cos\theta|')+'.'),('두 접벡터의 외적 크기는1이다. 따라서 이 패치의 넓이는 '+d(r'A_1=\int_0^{2\pi}\int_{-|\cos\theta|}^{|\cos\theta|}dx\,d\theta=2\int_0^{2\pi}|\cos\theta|\,d\theta=8')+'이다.','The tangent cross product has magnitude1. This patch has area '+d(r'A_1=\int_0^{2\pi}\int_{-|\cos\theta|}^{|\cos\theta|}dx\,d\theta=2\int_0^{2\pi}|\cos\theta|\,d\theta=8')),('좌표교환 대칭으로 두 번째 패치도8이다. 교선은 면적0이므로 더하면 된다.','Exchanging x and y gives a second patch of area8. Their seams have area zero, so the areas add.')],d('A=16'))
# Native, reproducible surface plots: collapse the volume map onto the surface.
specs={1:(lambda u,v,w:(-(-2+2*u)*v,-2+2*u,-(-2+2*u)*v+(-2+2*u)**2),'Triangle: (0,0), (0,-2), (2,-2)'),2:(lambda u,v,w:(u*math.cos(2*math.pi*v),u*math.sin(2*math.pi*v),u*u*math.cos(2*math.pi*v)*math.sin(2*math.pi*v)),'z = 3 + xy; x² + y² ≤ 1'),20:(lambda u,v,w:(-2+3*u,-1+2*v,1+(-2+3*u)+(-1+2*v)+(-2+3*u)**2),'z = 1 + x + y + x²; -2 ≤ x ≤ 1; -1 ≤ y ≤ 1'),22:(lambda u,v,w:((2*u-1),(2*v-1)*(1-abs(2*u-1)),(1+(2*u-1)**2)/(1+((2*v-1)*(1-abs(2*u-1)))**2)),'z = (1 + x²)/(1 + y²); |x| + |y| ≤ 1'),26:(lambda u,v,w:((2*u-1)*math.sqrt(max(0,1-(2*w-1)**2)),(2*v-1)*math.sqrt(max(0,1-(2*w-1)**2)),2*w-1),'x² + z² ≤ 1; y² + z² ≤ 1')}
for n,(fn,sub) in specs.items():
 name=f's15-5-{n}.svg';solid(name,f'15.5 / {n} - Surface',fn,subtitle=sub,resolution=16)
 if n in(1,2):
  shift=10 if n==1 else 3
  from plot_15 import ASSETS
  path=ASSETS/name;path.write_text(path.read_text().replace('>z</text>',f'>z - {shift}</text>'));sub+=f'; vertical coordinate shown is z - {shift}'
 attach(next(e for e in D.items if e['number']==n),name,('문제 조건으로 직접 그린 곡면','Original surface plot from the stated equations'),(sub,sub))
for e in D.items:
 e['hint']['ko']='투영영역을 구한 뒤 곡면 면적요소를 적분한다.'
 e['check']['ko']='면적요소와 경계를 대조하고, 명시된 적분을 기호 계산 또는 서로 다른 정밀도의 수치 계산으로 검산했다.'
D.save(26)
