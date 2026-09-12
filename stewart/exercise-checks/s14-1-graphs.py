exec(compile(open(__file__.replace('-graphs.py','-author.py')).read(),__file__,'exec'))
from early_plots import *
import xml.etree.ElementTree as ET
X=lambda x,y:x;Y=lambda x,y:y
for n,f,lev,dom,xr,yr in[(3,lambda x,y:x+y,[0],lambda x,y:x+y>0,(-3,3),(-3,3)),(4,lambda x,y:y-x*x,[0],lambda x,y:y>=x*x,(-3,3),(-1,6)),(7,lambda x,y:min(x-2,y-1),[0],lambda x,y:x>=2 and y>=1,(-1,6),(-1,5)),(8,lambda x,y:x-3*y,[0],lambda x,y:x>=3*y,(-3,3),(-3,3)),(9,lambda x,y:4*x*x+y*y,[4],lambda x,y:x>=0 and 4*x*x+y*y<=4,(-2,2),(-3,3)),(10,lambda x,y:x*x+y*y,[9],lambda x,y:x*x+y*y>9,(-5,5),(-5,5)),(11,lambda x,y:x+y,[0],lambda x,y:True,(-3,3),(-3,3)),(12,lambda x,y:x*x+y*y,[1],lambda x,y:x<2,(-3,3),(-3,3)),(13,lambda x,y:x+1,[0],lambda x,y:x*y>=0,(-3,3),(-3,3)),(14,lambda x,y:x+y,[-1,1],lambda x,y:abs(x+y)<=1,(-3,3),(-3,3))]:attach(b,n,[{'f':f,'levels':lev,'domain':dom,'xr':xr,'yr':yr,'title':f'{n}: shaded domain; see boundary conditions'}])
b.plot(15,[([lambda u,v:(2,u*3,v),lambda u,v:(-2,u*3,v),lambda u,v:(2*u,3,v),lambda u,v:(2*u,-3,v),lambda u,v:(2*u,3*v,1),lambda u,v:(2*u,3*v,-1)],(-1,1),(-1,1),'Closed box: |x|≤2, |y|≤3, |z|≤1')])
b.plot(16,[(lambda u,v:(2*sin(u)*cos(v),2*sin(u)*sin(v),4*cos(u)),(0,pi),(0,2*pi),'Open ellipsoid interior; surface excluded')])
def surf(f,title,ran=(-2,2)):return(lambda x,y:(x,y,f(x,y)),ran,ran,title)
for n,(F,f,k,e)in surfdata.items():
 if n==31:b.plot(n,[(lambda u,v:(sin(u)*cos(v),2*sin(u)*sin(v),2*cos(u)),(0,pi/2),(0,2*pi),'Upper ellipsoid: 4x²+y²+z²=4')])
 else:b.plot(n,[surf(f,F.replace('\\',''))])
funs32=[lambda x,y:1/(1+x*x+y*y),lambda x,y:1/(1+x*x*y*y),lambda x,y:log(x*x+y*y),lambda x,y:cos(hypot(x,y)),lambda x,y:abs(x*y),lambda x,y:cos(x*y)]
b.plot(32,[surf(f,title)for f,title in zip(funs32,['(a) III: circular peak','(b) I: cross ridges','(c) IV: logarithmic funnel','(d) V: circular ripples','(e) VI: absolute product','(f) II: hyperbolic ripples'])])
attach(b,36,[{'f':lambda x,y:x*x+y*y,'levels':[1,2,3,4,5,6],'title':'I: paraboloid / decreasing radial gaps'},{'f':lambda x,y:hypot(x,y),'levels':[.5,1,1.5,2,2.5,3],'title':'II: cone / constant radial gaps'}])
peaks=lambda x,y:sum(a*exp(-5*((x-u)**2+(y-v)**2))for u,v,a in[(-1,-1,1.3),(-1,1,1.5),(1,-1,.8),(1,1,1.0)])
attach(b,38,[{'f':peaks,'levels':[.05,.2,.5,.8,1.1,1.4],'title':'Four peaks: an illustrative contour model'}],('원본 곡면의 네 봉우리 배치를 설명하기 위한 자체 모형이다. 원본의 유일한 함수식을 추정한 것은 아니다.','An original illustrative model of the four-peak arrangement; it does not claim to recover a unique source formula.'))
attach(b,39,[{'f':lambda m,h:m/h**2,'levels':[18.5,25,30,40],'domain':lambda m,h:18.5<=m/h**2<=25,'xr':(0,150),'yr':(.5,2.5),'title':'x = mass (kg), y = height (m); shaded 18.5–25'}])
attach(b,40,[{'f':lambda m,h:m/h**2,'levels':[20],'xr':(0,100),'yr':(.5,2.2),'title':'B = 20: (45,1.5), (64.8,1.8), (80,2)'}])
for n,f in [(41,lambda x,y:log(max(hypot(x,y),.03))),(42,lambda x,y:exp((x*x-y)/3)),(43,lambda x,y:abs(x-y)*sqrt(max(x*y,0))),(44,lambda x,y:4-abs(x)-abs(y))]:b.plot(n,[surf(f,f'{n}: illustrative surface from contours',(0,3)if n==43 else(-2,2))],('원본 등고선의 모양과 높이 증가 방향을 만족하는 자체 설명용 모형. 그림만으로 원래 함수는 유일하게 정해지지 않는다.','An original model matching the qualitative contour shape and direction of increasing height. The source function is not uniquely determined by its diagram.'))
contours={45:(lambda x,y:x*x-y*y,[-4,-2,0,2,4]),46:(lambda x,y:x*y,[-4,-2,-1,0,1,2,4]),47:(lambda x,y:sqrt(x)+y,[-2,-1,0,1,2,3]),48:(lambda x,y:log(x*x+4*y*y),[-2,-1,0,1,2,3]),49:(lambda x,y:y*exp(x),[-3,-2,-1,0,1,2,3]),50:(lambda x,y:y-atan(x),[-2,-1,0,1,2]),51:(lambda x,y:(x*x+y*y)**(1/3),[.5,1,1.5,2]),52:(lambda x,y:y/(x*x+y*y),[-2,-1,-.5,0,.5,1,2]),53:(lambda x,y:x*x+9*y*y,[1,4,9,16,25]),54:(lambda x,y:sqrt(36-9*x*x-4*y*y),[0,1,2,3,4,5,6]),55:(lambda x,y:100/(1+x*x+2*y*y),[20,25,50,75]),56:(lambda x,y:1/sqrt(1-x*x-y*y),[1.1,1.25,1.5,2,3])}
for n,(f,ls)in contours.items():attach(b,n,[{'f':f,'levels':ls,'xr':(0,4)if n==47 else(-1.1,1.1)if n==56 else(-3,3),'yr':(-1.1,1.1)if n==56 else(-3,3),'title':f'Exercise {n}: level curves'+(' (c=r=1)'if n==56 else'')}])
def combine(n,items):
 path=ROOT/'assets'/f's14-1-{n}.svg';old=ET.fromstring(path.read_text())if path.exists()else None
 b.plot(n,items);new=ET.fromstring(path.read_text())
 if old is not None:
  w=max(int(new.attrib['width']),int(old.attrib['width']));h=int(new.attrib['height'])+int(old.attrib['height']);root=ET.Element('svg',{'xmlns':'http://www.w3.org/2000/svg','width':str(w),'height':str(h),'viewBox':f'0 0 {w} {h}'})
  g=ET.SubElement(root,'g');g.extend(list(new));g=ET.SubElement(root,'g',{'transform':'translate(0,365)'});g.extend(list(old));path.write_text(ET.tostring(root,encoding='unicode'))
combine(53,[(lambda r,t:(r*cos(t),r*sin(t)/3,r*r),(0,2),(0,2*pi),'z = x² + 9y²; 0≤z≤4')]);combine(54,[(lambda u,v:(2*sin(u)*cos(v),3*sin(u)*sin(v),6*cos(u)),(0,pi/2),(0,2*pi),'Upper ellipsoid: semiaxes 2,3,6')])
cf={57:lambda x,y:x*y*y-x**3,58:lambda x,y:x*y**3-y*x**3,59:lambda x,y:exp(-(x*x+y*y)/3)*(sin(x*x)+cos(y*y)),60:lambda x,y:cos(x)*cos(y),61:lambda x,y:sin(x*y),62:lambda x,y:exp(x)*cos(y),63:lambda x,y:sin(x-y),64:lambda x,y:sin(x)-sin(y),65:lambda x,y:(1-x*x)*(1-y*y),66:lambda x,y:(x-y)/(1+x*x+y*y),73:lambda x,y:3*x-x**4-4*y*y-10*x*y,74:lambda x,y:x*y*exp(-x*x-y*y),75:lambda x,y:(x+y)/(x*x+y*y),76:lambda x,y:x*y/(x*x+y*y)}
for n,f in cf.items():
 ls=[-1,-.5,0,.5,1]if n not in[57,58,65,73,74]else[-4,-2,0,2,4]if n!=74 else[-.15,-.1,0,.1,.15]
 attach(b,n,[{'f':f,'levels':ls,'xr':(-3,3),'yr':(-3,3),'title':f'{n}: contour map'}]);combine(n,[surf(f,f'{n}: central window',(-2,2)),surf(f,f'{n}: wider window',(-3,3))])
b.plot(77,[surf(lambda x,y,c=c:exp(c*x*x+y*y),f'c = {c}',(-1.2,1.2))for c in[-1,0,1,2]])
b.plot(78,[surf(lambda x,y,a=a,d=d:(a*x*x+d*y*y)*exp(-x*x-y*y),f'a = {a}, b = {d}')for a,d in[(1,1),(2,1),(-1,-1),(1,-1),(1,0),(0,0)]])
b.plot(79,[surf(lambda x,y,c=c:x*x+y*y+c*x*y,f'c = {c}')for c in[-3,-2,0,2,3]])
b.plot(80,[(lambda r,t,f=f:(r*cos(t),r*sin(t),f(r)),(.08,3)if i in[2,4]else(0,3),(0,2*pi),title)for i,(f,title)in enumerate([(lambda r:r,'z = r'),(exp,'z = exp(r)'),(log,'z = ln(r)'),(sin,'z = sin(r)'),(lambda r:1/r,'z = 1/r')])])
b.save()
