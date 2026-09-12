from early_helpers import *
from math import *
b=Book('14.3',[1007,1008,1009,1010,1011]);d=json.loads((ROOT/'s14-3.json').read_text());b.E={e['number']:e for e in d['exercises']}
def surface(f,title,ran=(-2,2)):return(lambda x,y:(x,y,f(x,y)),ran,ran,title)
b.plot(7,[surface(lambda x,y:16-4*x*x-y*y,'z = 16 - 4x² - y²'),([lambda t,v:(1+t,2,12-4*(1+t)**2),lambda t,v:(1,2+t,12-(2+t)**2),lambda t,v:(1+t,2,8-8*t),lambda t,v:(1,2+t,8-4*t)],(-.7,.7),(0,1),'Traces and tangent lines at (1,2,8)')])
b.plot(8,[(lambda a,t:(2*cos(a)*sin(t),sin(a)*sin(t),2*cos(t)),(0,2*pi),(0,pi/2),'z = sqrt(4 - x² - 4y²)'),([lambda t,v:(1+t,0,sqrt(3)-t/sqrt(3)),lambda t,v:(1,t,sqrt(3))],(-.6,.6),(0,1),'Tangent directions at (1,0,sqrt(3))')])
b.plot(70,[surface(lambda x,y:y/(1+x*x*y*y),'f = y/(1+x²y²)'),surface(lambda x,y:-2*x*y**3/(1+x*x*y*y)**2,'fx = -2xy³/(1+x²y²)²'),surface(lambda x,y:(1-x*x*y*y)/(1+x*x*y*y)**2,'fy = (1-x²y²)/(1+x²y²)²')])
b.plot(71,[surface(lambda x,y:x*x*y**3,'f = x²y³'),surface(lambda x,y:2*x*y**3,'fx = 2xy³'),surface(lambda x,y:3*x*x*y*y,'fy = 3x²y²')])
b.plot(90,[(lambda x,t:(x,t/20,10*exp(-.2*x)*sin(2*pi*t/365-.2*x)),(0,20),(0,365),'T = 10 exp(-0.2x) sin(2πt/365 - 0.2x)')],('자체 그래프. 수평축은 깊이 x와 시간 t/20으로 표시한 시간이다. 깊어질수록 진폭이 줄고 최대 온도 시점이 늦어진다.','Original plot. Horizontal coordinates are depth x and scaled time t/20. Amplitude decays with depth and peaks occur later.'))
b.plot(94,[([lambda x,y:(x,y,(6-x-x*x-2*y*y)/4),lambda t,v:(1,t,(4-2*t*t)/4),lambda t,v:(1,2+(t-2)/2,(-4-8*(t-2)/2)/4)],(0,3),(0,3),'Surface, trace, tangent; vertical coordinate z/4')],('청색 곡면, 주황 교선, 빨강 접선을 겹쳤다. 수직 표시 좌표는 z/4로 축척을 조정했다. 접점은 원래 좌표에서 (1,2,-4), 접선 방향은 (0,1,-8)이다.','Blue surface, orange section, and red tangent share a frame with vertical coordinate scaled to z/4. In original coordinates the contact point is (1,2,-4) and direction is (0,1,-8).'))
p94=ROOT/'assets'/'s14-3-94.svg';p94.write_text(p94.read_text().replace('>z</text>','>z/4</text>'))
def f(x,y):return (x**3*y-x*y**3)/(x*x+y*y) if x*x+y*y else 0
def mixed(x,y):return (x**6+9*x**4*y*y-9*x*x*y**4-y**6)/(x*x+y*y)**3 if x*x+y*y else float('nan')
b.plot(101,[surface(f,'f: continuous at origin'),surface(mixed,'fxy: origin value -1, punctured surface'),surface(mixed,'fyx: origin value +1, punctured surface')],('원점 밖에서는 혼합편도함수의 곡면이 같다. 원점의 별도 지정값은 fxy=-1, fyx=1이며 그 주변 곡면은 원점에서 극한이 없다.','The two mixed-partial surfaces coincide off the origin. Their separately defined origin values are fxy=-1 and fyx=1; the punctured surfaces have no limit there.'))
b.save()
from early_plots import *
for n in[4,5,72]:b.plot(n,[surface(lambda x,y:x*x*y-y**3,'Illustrative model: z = x²y - y³',(-2,2.5))],('원본 그림에서 읽은 국소 기울기·곡률 부호를 설명하는 자체 모형이다. 원본의 정확한 함수식은 주어지지 않았다.','An original model illustrating the local slope/curvature signs read from the source graph. The source does not specify an exact formula.'))
attach(b,6,[{'f':lambda x,y:4*x-2*y,'levels':[2,4,6,8,10],'xr':(0,4),'yr':(-1,3),'title':'Local contour interpolation: fx≈4, fy≈-2'}],('원본 등고선에서 읽은 점 부근의 변화율을 선형 모형으로 시각화했다. 정확한 원본 전체 지도가 아니다.','A local linear model visualizes the rates read from the source contours; it is not an exact reconstruction of the entire original map.'))
b.plot(69,[surface(lambda x,y:x*x*y-y**3,'c: illustrative f'),surface(lambda x,y:2*x*y,'b: corresponding fx'),surface(lambda x,y:x*x-3*y*y,'a: corresponding fy')],('원본의 대응 c=f,b=fx,a=fy를 설명하는 자체 미분 모형. 원본의 유일한 함수식을 추정한 것은 아니다.','An original derivative model illustrating the source matching c=f,b=fx,a=fy; no unique source formula is inferred.'))
attach(b,74,[{'f':lambda x,y:exp(y)/(x+2),'levels':[.2,.4,.6,.8,1,1.2],'xr':(0,3),'yr':(-1,2),'title':'Illustrative contour signs near P'}],('원본에서 판독한 fx<0,fy>0,fxx>0,fxy<0,fyy>0을 보여 주는 자체 모형. 원본 함수의 정확한 복원은 아니다.','An original model of the signs fx<0,fy>0,fxx>0,fxy<0,fyy>0 read from the source; not an exact recovery of its function.'))
b.save()
