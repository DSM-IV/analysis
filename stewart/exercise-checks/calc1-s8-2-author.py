from calc1_helpers import *
x,y,u=s.symbols('x y u',positive=True);Q=s.Rational;pi=s.pi;sq=s.sqrt;log=s.log;ex=s.exp
b=CalcBook('8.2',[611,612,613]);records=[]
def add(n,st,steps,ans,ck=None,parts=[]):
 b.add(n,611 if n<=26 else 612 if n<=42 else 613,('회전체의 겉넓이','Surface area of revolution'),st,steps,ans,parts=parts);b.verify(n,*(ck or('회전 반지름과 호의 길이 요소를 확인하고 독립 수치구적 또는 기호미분으로 검산했다.','Checked rotation radius and arc-length factor, then verified by independent quadrature or symbolic differentiation.')));b.save()
def ma(n,eq,steps,ans,ck=None,parts=[]):add(n,(M(eq)+'곡면 넓이를 구하거나 관계를 증명하라.',M(eq)+'Find the surface area or prove the relation.'),fs(*steps),same(M(ans)),ck,parts)
# Two equivalent surface integrals: independently track increasing inverse limits.
setups=[(1,x**Q(1,3),y**3,1,8,1,2,'x',r'y=\sqrt[3]x'),(2,2*log(x),ex(y/2),1,s.E,0,2,'x',r'x^2=e^y'),(3,(ex(x)-1)/2,log(2*y+1),0,log(3),0,1,'x',r'x=\ln(2y+1)'),(4,s.atan(x),s.tan(y),0,1,0,pi/4,'x',r'y=\arctan x'),(5,4/x,4/y,1,8,Q(1,2),4,'y',r'xy=4'),(6,(x+1)**4,y**Q(1,4)-1,0,2,1,81,'y',r'y=(x+1)^4'),(7,1+s.sin(x),s.asin(y-1),0,pi/2,1,2,'y',r'y=1+\sin x'),(8,log(x)/2,ex(2*y),1,ex(4),0,2,'y',r'x=e^{2y}')]
for n,f,g,a,c,d,e,axis,eq in setups:
 rx=f if axis=='x'else x;ry=y if axis=='x'else g;ix=s.Integral(2*pi*rx*sq(1+s.diff(f,x)**2),(x,a,c));iy=s.Integral(2*pi*ry*sq(1+s.diff(g,y)**2),(y,d,e))
 add(n,(M(eq+',\quad'+s.latex(a)+r'\le x\le '+s.latex(c)+',\quad'+s.latex(d)+r'\le y\le '+s.latex(e))+f'{axis}축 회전이다. (a)x (b)y에 대한 넓이 적분만 세우라.',M(eq+',\quad'+s.latex(a)+r'\le x\le '+s.latex(c)+',\quad'+s.latex(d)+r'\le y\le '+s.latex(e))+f'Rotate about the {axis}-axis. Set up, without evaluation, surface integrals in(a)x and(b)y.'),fs(r'dS=2\pi\rho\,ds,\quad\rho='+('y'if axis=='x'else'x'),r'y^\prime='+s.latex(s.diff(f,x))+r',\quad dx/dy='+s.latex(s.diff(g,y)),r'(a)S='+s.latex(ix),r'(b)S='+s.latex(iy)),same(M(r'(a)'+s.latex(ix)+r';\quad(b)'+s.latex(iy))),parts=['a','b'])
def surface(n,f,q,a,c,axis,sp=None,G=None,extra=[]):
 a,c=s.sympify(a),s.sympify(c);d=s.diff(f,q);sp=sqrt(1+d*d)if sp is None else s.sympify(sp);rad=f if(axis=='x'and q==x)or(axis=='y'and q==y)else q;integrand=s.simplify(2*pi*rad*sp)
 diff=s.trigsimp(s.factor(sp**2-1-d*d));assert diff==0,(n,diff)
 if G is None:G=s.integrate(integrand,q)
 assert not G.has(s.Integral),(n,G)
 dd=s.simplify(s.trigsimp(s.diff(G,q)-integrand))
 if dd!=0:
  pt=mp.mpf(str(((a+c)/2).evalf(30)));gg=s.lambdify(q,G,'mpmath');ff=s.lambdify(q,integrand,'mpmath');assert abs(mp.diff(gg,pt)-ff(pt))<mp.mpf('1e-20'),(n,dd)
 val=s.simplify(s.limit(G,q,c,dir='-')-s.limit(G,q,a,dir='+'));num=mp.quad(s.lambdify(q,integrand,'mpmath'),[mp.mpf(str(a.evalf(30))),mp.mpf(str(c.evalf(30)))]);assert abs(complex(val.evalf())-complex(num))<1e-7*max(1,abs(complex(num))),(n,val,num)
 eq=('y='if q==x else'x=')+s.latex(f)+',\quad'+s.latex(a)+r'\le '+str(q)+r'\le '+s.latex(c)+r';\quad\text{about '+axis+'-axis}'
 add(n,(M(eq)+'정확한 넓이를 구하라.',M(eq)+'Find the exact surface area.'),list(extra)+fs(r'\rho='+s.latex(rad)+r',\quad ds='+s.latex(sp)+'d'+str(q),r'S='+s.latex(s.Integral(integrand,(q,a,c))),r'\int dS='+s.latex(G),r'S='+s.latex(val)),same(M('S='+s.latex(val))));records.append({'number':n,'exact':str(val),'numeric':str(num)})
 return val
# Exact elementary surface areas.
rows=[(9,x**3,x,0,2,'x',sq(1+9*x**4),pi*(1+9*x**4)**Q(3,2)/27),(10,5-y*y,y,0,sq(2),'x',sq(1+4*y*y),pi*(1+4*y*y)**Q(3,2)/6),(11,y*y-1,y,1,2,'x',sq(1+4*y*y),pi*(1+4*y*y)**Q(3,2)/6),(12,sq(1+ex(x)),x,0,1,'x',(ex(x)+2)/(2*sq(1+ex(x))),pi*(ex(x)+2*x)),(13,s.cos(x/2),x,0,pi,'x',sq(1+s.sin(x/2)**2/4),pi*s.sin(x/2)*sq(4+s.sin(x/2)**2)+4*pi*s.asinh(s.sin(x/2)/2)),(14,x**3/6+1/(2*x),x,Q(1,2),1,'x',(x*x+x**-2)/2,pi*(x**6/36+x*x/3-1/(4*x*x))),(15,(y*y+2)**Q(3,2)/3,y,1,2,'x',y*y+1,pi*(y**4/2+y*y)),(16,1+2*y*y,y,1,2,'x',sq(1+16*y*y),pi*(1+16*y*y)**Q(3,2)/24),(17,x**Q(3,2)/3,x,0,12,'y',sq(x+4)/2,pi*(Q(2,5)*(x+4)**Q(5,2)-Q(8,3)*(x+4)**Q(3,2))),(20,x*x/4-log(x)/2,x,1,2,'y',x/2+1/(2*x),pi*(x**3/3+x))]
for row in rows:surface(*row)
for n,eq in[(10,r'y=\sqrt{5-x},\quad3\le x\le5'),(11,r'y^2=x+1,\quad0\le x\le3')]:
 for lang in['ko','en']:b.E[n]['statement'][lang]=M(eq)+('x축 회전의 정확한 넓이를 구하라.'if lang=='ko'else'Find the exact surface area about the x-axis.')
for lang,txt in[('ko','y²=x+1의 두 부호 가지는 x축 회전으로 같은 곡면을 생성한다. 양의 가지만 한 번 계산한다.'),('en','The two signed branches of y²=x+1 generate the same surface about the x-axis; use the positive branch once.')]:b.E[11]['steps'][lang].insert(0,txt)
ma(18,r'x^{2/3}+y^{2/3}=1,\quad0\le y\le1;\quad\text{about y-axis}',[r'x=(1-y^{2/3})^{3/2},\quad ds=y^{-1/3}dy',r'S=2\pi\int_0^1(1-y^{2/3})^{3/2}y^{-1/3}dy',r'u=y^{2/3}\Rightarrow S=3\pi\int_0^1(1-u)^{3/2}du=6\pi/5',r'\text{The negative-x branch generates the same surface; do not double count}'],r'S=6\pi/5')
ma(19,r'x=\sqrt{a^2-y^2},\quad0\le y\le a/2,\quad a>0;\quad\text{about y-axis}',[r'dx/dy=-y/\sqrt{a^2-y^2},\quad ds=a\,dy/\sqrt{a^2-y^2}',r'S=2\pi\int_0^{a/2}\sqrt{a^2-y^2}\frac a{\sqrt{a^2-y^2}}dy=2\pi a(a/2)'],r'S=\pi a^2')
for n,f,q,a,c,axis in[(21,ex(-x*x),x,-1,1,'x'),(22,y-1/y,y,1,3,'x'),(23,y+y**3,y,0,1,'y'),(24,x+s.sin(x),x,0,2*pi/3,'y'),(25,log(y)+y*y,y,1,4,'x'),(26,s.cos(y)**2,y,0,pi/2,'y')]:
 d=s.diff(f,q);rad=f if(axis=='x'and q==x)or(axis=='y'and q==y)else q;integ=2*pi*rad*sq(1+d*d);val=mp.quad(s.lambdify(q,integ,'mpmath'),[float(a),float(c)]);eq=('y='if q==x else'x=')+s.latex(f)+',\quad'+s.latex(a)+r'\le '+str(q)+r'\le '+s.latex(c)+r';\quad\text{about '+axis+'-axis}'
 add(n,(M(eq)+'넓이 적분을 세우고 소수4자리까지 계산하라.',M(eq)+'Set up the surface integral and evaluate to4decimal places.'),fs(r'\rho='+s.latex(rad)+r',\quad d'+('y/dx'if q==x else'x/dy')+'='+s.latex(d),r'S='+s.latex(s.Integral(integ,(q,a,c))),r'S\approx'+f'{float(val):.4f}'),same(M(r'S\approx'+f'{float(val):.4f}')));records.append({'number':n,'numeric':str(val)})
H=lambda u:sq(1+u*u)+log(u/(1+sq(1+u*u)))
surface(27,1/x,x,1,2,'x',sq(1+x**-4),-pi*H(x**-2),fs(r'u=x^{-2}\Rightarrow S=\pi\int_{1/4}^1\frac{\sqrt{1+u^2}}u du'))
surface(28,sq(x*x+1),x,0,3,'x',sq(1+2*x*x)/sq(1+x*x),pi*(x*sq(1+2*x*x)+s.asinh(sq(2)*x)/sq(2)))
surface(29,x**3,x,0,1,'y',sq(1+9*x**4),pi*(x*x*sq(1+9*x**4)+s.asinh(3*x*x)/3)/2,fs(r'u=x^2\Rightarrow S=\pi\int_0^1\sqrt{1+9u^2}du'))
G30=2*pi*((u*sq(1+u*u)+s.asinh(u))/2-H(u));surface(30,log(x+1),x,0,1,'y',sq(1+(x+1)**-2),G30.subs(u,x+1),fs(r'u=x+1\Rightarrow S=2\pi\int_1^2(1-u^{-1})\sqrt{1+u^2}du'))
for n,f,a,c in[(31,x**5/5,0,5),(32,x*log(x),1,2)]:
 integ=2*pi*f*sq(1+s.diff(f,x)**2);ff=s.lambdify(x,integ,'mpmath');h=mp.mpf(c-a)/10;S=h/3*(ff(a)+ff(c)+4*sum(ff(a+j*h)for j in[1,3,5,7,9])+2*sum(ff(a+j*h)for j in[2,4,6,8]));I=mp.quad(ff,[a,c]);ma(n,'y='+s.latex(f)+',\quad'+str(a)+r'\le x\le '+str(c)+r';\quad\text{about x-axis, Simpson }n=10',[r'S='+s.latex(s.Integral(integ,(x,a,c))),r'Q_{10}=\frac h3[g_0+4g_1+2g_2+\cdots+4g_9+g_{10}],\quad g=2\pi y\sqrt{1+(y^\prime)^2}',r'Q_{10}\approx'+f'{float(S):.8f}'+r',\quad S\approx'+f'{float(I):.8f}',r'S-Q_{10}\approx'+f'{float(I-S):.8f}'],r'Q_{10}\approx'+f'{float(S):.8f}'+r',\quad S\approx'+f'{float(I):.8f}');records.append({'number':n,'numeric':str(I),'simpson':str(S)})
ma(33,r'y=1/x,\quad x\ge1;\quad\text{about x-axis}',[r'S=2\pi\int_1^\infty\frac1x\sqrt{1+x^{-4}}dx',r'S\ge2\pi\int_1^\infty dx/x=\infty',r'V=\pi\int_1^\infty x^{-2}dx=\pi'],r'S=\infty\quad\text{while }V=\pi')
ma(34,r'y=e^{-x},\quad x\ge0;\quad\text{about x-axis}',[r'S=2\pi\int_0^\infty e^{-x}\sqrt{1+e^{-2x}}dx',r'u=e^{-x}\Rightarrow S=2\pi\int_0^1\sqrt{1+u^2}du',r'S=\pi[u\sqrt{1+u^2}+\operatorname{arsinh}u]_0^1'],r'S=\pi[\sqrt2+\ln(1+\sqrt2)]')
ma(35,r'3ay^2=x(a-x)^2,\quad a>0:\quad\text{rotate the loop about (a)x-axis (b)y-axis}',[r'0\le x\le a,\quad y_\pm=\pm(a-x)\sqrt{x/(3a)}',r'|y^\prime|=\frac{|a-3x|}{2\sqrt{3ax}},\quad ds=\frac{a+3x}{2\sqrt{3ax}}dx',r'(a)\text{Both branches generate the same surface: use the upper branch once}',r'S_x=\frac\pi{3a}\int_0^a(a-x)(a+3x)dx=\pi a^2/3',r'(b)\text{Upper/lower branches generate distinct surface halves}',r'S_y=4\pi\int_0^ax\frac{a+3x}{2\sqrt{3ax}}dx=\frac{2\pi}{\sqrt{3a}}\left[\frac{2a}3x^{3/2}+\frac65x^{5/2}\right]_0^a'],r'(a)S_x=\frac{\pi a^2}3;\quad(b)S_y=\frac{56\pi a^2}{15\sqrt3}',parts=['a','b'])
ma(36,r'y=ax^2\text{ rotated about y-axis: diameter10ft, depth2ft}',[r'y(5)=2\Rightarrow a=2/25\ \mathrm{ft}^{-1}',r'S=2\pi\int_0^5x\sqrt{1+(4x/25)^2}dx',r'S=\frac{625\pi}{24}\left[(1+16x^2/625)^{3/2}\right]_0^5'],r'a=2/25,\quad S=\frac\pi{24}(205\sqrt{41}-625)\ \mathrm{ft}^2')
ma(37,r'x^2/a^2+y^2/b^2=1,\quad a>b>0:\quad(a)\text{x-axis};\ (b)\text{y-axis}',[r'e=\sqrt{1-b^2/a^2},\quad0<e<1',r'(a)y=b\sqrt{1-x^2/a^2}:\quad S_x=\frac{2\pi b}a\int_{-a}^a\sqrt{a^2-e^2x^2}dx',r'\int\sqrt{a^2-e^2x^2}dx=\tfrac x2\sqrt{a^2-e^2x^2}+\tfrac{a^2}{2e}\arcsin(ex/a)',r'S_x=2\pi b^2+\frac{2\pi ab}e\arcsin e',r'(b)x=a\sqrt{1-y^2/b^2}:\quad S_y=\frac{2\pi a}b\int_{-b}^b\sqrt{b^2+\frac{a^2-b^2}{b^2}y^2}dy',r'S_y=2\pi a^2+\frac{2\pi b^2}e\operatorname{artanh}e'],r'(a)2\pi b^2\left(1+\frac a{be}\arcsin e\right);\quad(b)2\pi a^2\left(1+\frac{1-e^2}e\operatorname{artanh}e\right)',parts=['a','b'])
ma(38,r'\text{Torus: central radius }R,\text{ tube radius }r,\quad R>r>0',[r'\rho(\theta)=R+r\cos\theta,\quad ds=r\,d\theta,\quad0\le\theta\le2\pi',r'S=\int_0^{2\pi}2\pi(R+r\cos\theta)r\,d\theta',r'S=2\pi r[2\pi R+0]'],r'S=4\pi^2Rr')
I39=mp.quad(lambda y:2*mp.pi*(4-y)*mp.sqrt(1+4*y*y),[0,2])
ma(39,r'(a)y=f(x)\le c,\ a\le x\le b:\text{ rotate about }y=c;\quad(b)y=\sqrt x,\ 0\le x\le4,\ c=4',[r'(a)\rho=c-f(x),\quad ds=\sqrt{1+[f^\prime(x)]^2}dx',r'S=2\pi\int_a^b[c-f(x)]\sqrt{1+[f^\prime(x)]^2}dx',r'(b)S=2\pi\int_0^4(4-\sqrt x)\sqrt{1+1/(4x)}dx',r'x=y^2\Rightarrow S=2\pi\int_0^2(4-y)\sqrt{1+4y^2}dy'],r'(a)2\pi\int_a^b[c-f(x)]\sqrt{1+[f^\prime(x)]^2}dx;\quad(b)S\approx'+f'{float(I39):.4f}',parts=['a','b'])
vals40=[];steps=[]
for lab,rad,axis in[('a',x+1,'x=-1'),('b',4-x,'x=4'),('c',x**3-Q(1,2),'y=1/2'),('d',10-x**3,'y=10')]:
 integ=2*pi*rad*sq(1+9*x**4);I=mp.quad(s.lambdify(x,integ,'mpmath'),[1,2]);steps+=fs('('+lab+r')\quad\rho='+s.latex(rad)+r',\quad S='+s.latex(s.Integral(integ,(x,1,2)))+r'\approx'+f'{float(I):.2f}');vals40.append('('+lab+')'+f'{float(I):.2f}')
ma(40,r'y=x^3,\quad1\le x\le2;\quad(a)x=-1,\ (b)x=4,\ (c)y=1/2,\ (d)y=10',[r'ds=\sqrt{1+9x^4}dx']+[t[0][2:-2]for t in steps],r';\quad '.join(vals40),parts=list('abcd'))
ma(41,r'x^2+y^2=r^2\text{ rotated about }y=r',[r'x=r\cos\theta,\ y=r\sin\theta,\quad ds=r\,d\theta',r'\rho=r-y=r(1-\sin\theta)\ge0',r'S=\int_0^{2\pi}2\pi r^2(1-\sin\theta)d\theta=4\pi^2r^2'],r'S=4\pi^2r^2')
ma(42,r'\text{Sphere radius }R\text{ between parallel planes separated by }h',[r'y=\sqrt{R^2-x^2},\quad ds=R\,dx/\sqrt{R^2-x^2}',r'\text{Planes }x=a,b,\quad b-a=h',r'S=\int_a^b2\pi y\,ds=\int_a^b2\pi R\,dx=2\pi Rh'],r'S=2\pi Rh')
ma(43,r'\text{Cylinder radius }R\text{ and zone height }h',[r'\text{Unroll the curved zone into a rectangle}',r'\text{Width}=2\pi R,\quad\text{height}=h\Rightarrow S=(2\pi R)h',r'\text{This equals the spherical-zone formula; end disks are not part of the zone}'],r'S=2\pi Rh')
ma(44,r'g(x)=f(x)+c,\quad f>0,c>0,\quad L=\int_a^b\sqrt{1+(f^\prime)^2}dx',[r'g^\prime=f^\prime',r'S_g=\int_a^b2\pi(f+c)\sqrt{1+(f^\prime)^2}dx',r'=\int_a^b2\pi f\sqrt{1+(f^\prime)^2}dx+2\pi c\int_a^b\sqrt{1+(f^\prime)^2}dx'],r'S_g=S_f+2\pi cL')
ma(45,r'y=e^{x/2}+e^{-x/2},\quad a\le x\le b;\quad\text{about x-axis}',[r'y^\prime=\tfrac12(e^{x/2}-e^{-x/2})',r'1+(y^\prime)^2=\tfrac14(e^{x/2}+e^{-x/2})^2=y^2/4',r'y>0\Rightarrow ds=(y/2)dx',r'S=\int_a^b2\pi y(y/2)dx=\pi\int_a^by^2dx=V'],r'S=V')
ma(46,r'y=f(x)\text{ may have either sign; rotate about x-axis}',[r'\rho(x)=\text{distance to x-axis}=|f(x)|',r'ds=\sqrt{1+[f^\prime(x)]^2}\,dx',r'dS=2\pi\rho\,ds=2\pi|f(x)|\sqrt{1+[f^\prime(x)]^2}\,dx'],r'S=\int_a^b2\pi|f(x)|\sqrt{1+[f^\prime(x)]^2}\,dx')
(Path(__file__).parent/'calc1-s8-2-numeric-results.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n');b.save();print('8.2 COMPLETE',len(b.E))
