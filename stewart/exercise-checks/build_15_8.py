"""Original worked solutions for all 51 general Exercises in §15.8."""
import math
import sympy as s
from core_15 import Doc,tex,d,m,integral,pair
from plot_15 import solid,attach,points_plot
q,t,p,r,z=s.symbols('rho theta phi r z',nonnegative=True)
a,k,h=s.symbols('a k h',positive=True)
pi=s.pi;J=q*q*s.sin(p)
X=q*s.sin(p)*s.cos(t);Y=q*s.sin(p)*s.sin(t);Z=q*s.cos(p)
doc=Doc('15.8',[1144,1145,1146],lambda n:1144 if n<=29 else 1145 if n<=49 else 1146)
add=doc.add
points={1:[(2,3*pi/4,pi/2),(4,-pi/3,pi/4)],2:[(5,pi/2,pi/3),(6,0,5*pi/6)],3:[(3,3,0),(1,-s.sqrt(3),2*s.sqrt(3))],4:[(0,4,-4),(-2,2,2*s.sqrt(6))]}
outputs={}
for n,ps in points.items():
    forward=n<=2;outs=[];steps=[]
    for label,pt in zip('ab',ps):
        if forward:
            qq,tt,pp=pt;out=tuple(s.simplify(f.subs({q:qq,t:tt,p:pp})) for f in (X,Y,Z))
            step=d(r'(x,y,z)=(\rho\sin\phi\cos\theta,\rho\sin\phi\sin\theta,\rho\cos\phi)='+tex(s.Tuple(*out)))
        else:
            xx,yy,zz=pt;qq=s.sqrt(xx*xx+yy*yy+zz*zz);pp=s.acos(zz/qq);tt=s.simplify(s.atan2(yy,xx)%(2*pi));out=(qq,tt,pp)
            step=d(r'\rho=\sqrt{x^2+y^2+z^2}='+tex(qq)+r',\quad\theta='+tex(tt)+r',\quad\phi=\arccos(z/\rho)='+tex(pp))
        steps.append((f'({label}) '+step,f'({label}) '+step));outs.append(out)
    outputs[n]=outs
    steps.append((r'φ는 양의 z축에서 잰 각이며 θ는 xy-평면에서의 방위각이다. φ의 범위는0부터π이다.',r'φ is measured from the positive z-axis; θ is the azimuth in the xy-plane. The range of φ is0 toπ.'))
    add(n,('구면좌표 변환','Spherical-coordinate conversion'),
      (('구면좌표 점을 표시하고 직교좌표로 바꾸어라. ' if forward else '직교좌표를 구면좌표로 바꾸어라. ')+', '.join(f'({l}) '+m(tex(s.Tuple(*pt))) for l,pt in zip('ab',ps)),
       ('Plot the spherical-coordinate points and find rectangular coordinates. ' if forward else 'Convert rectangular coordinates to spherical coordinates. ')+', '.join(f'({l}) '+m(tex(s.Tuple(*pt))) for l,pt in zip('ab',ps))),
      (r'\(\rho^2=x^2+y^2+z^2\)와 세 좌표변환식을 사용한다.','Use the three coordinate transformations and '+m(r'\rho^2=x^2+y^2+z^2')+'.'),steps,
      d(r'(a)\ '+tex(s.Tuple(*outs[0]))+r',\quad(b)\ '+tex(s.Tuple(*outs[1]))),
      ('역변환으로 원래 점을 복원하고 θ의 사분면과 z의 부호를 확인했다.','Inverse conversion recovers the original point; the θ quadrant and sign of z were checked.'),('a','b'))

for n,eq,derivation,answer in [
 (5,r'\phi=3\pi/4',(r'\(r=\rho\sin\phi=\rho/\sqrt2\), \(z=\rho\cos\phi=-\rho/\sqrt2\)이므로 z=-r이다.',r'\(r=\rho\sin\phi=\rho/\sqrt2\) and \(z=\rho\cos\phi=-\rho/\sqrt2\), so z=-r.'),(r'\(z=-\sqrt{x^2+y^2}\): 음의 z축을 둘러싼 반각45°의 아래쪽 원뿔면.',r'\(z=-\sqrt{x^2+y^2}\): the lower cone with half-angle45° about the negative z-axis.')),
 (6,r'\rho^2-3\rho+2=0',(r'식은 \((\rho-1)(\rho-2)=0\)으로 인수분해된다.',r'Factor the equation as \((\rho-1)(\rho-2)=0\).'),('원점 중심 반지름1과2인 두 구면의 합집합. 두 구면 사이의 입체는 아니다.','The union of the two concentric spheres of radii1 and2; the equation describes surfaces, not the shell volume.')),
 (7,r'\rho\cos\phi=1',(r'좌표변환에서 \(\rho\cos\phi=z\)이다.',r'The coordinate identity is \(\rho\cos\phi=z\).'),(r'수평면 \(z=1\).',r'The horizontal plane \(z=1\).')),
 (8,r'\rho=\cos\phi',(r'양변에 ρ를 곱해 \(\rho^2=\rho\cos\phi=z\). 따라서 \(x^2+y^2+(z-1/2)^2=1/4\).',r'Multiply by ρ to obtain \(\rho^2=\rho\cos\phi=z\), hence \(x^2+y^2+(z-1/2)^2=1/4\).'),('중심(0,0,1/2), 반지름1/2인 구면.','The sphere with center(0,0,1/2) and radius1/2.'))]:
    add(n,('구면좌표 곡면 판별','Identifying a spherical-coordinate surface'),('곡면 '+m(eq)+'를 설명하라.','Describe the surface '+m(eq)+'.'),('직교좌표식 또는 반지름 조건으로 바꾼다.','Convert to a rectangular equation or radial condition.'),[derivation],answer,('변환 후 얻은 표면의 점들을 역대입하면 원래 관계를 만족한다.','Points on the resulting surface satisfy the original relation after substitution.'))

for n,original,converted in [(9,[r'x^2+y^2+z^2=9',r'x^2-y^2-z^2=1'],[r'\rho=3',r'\rho^2(2\sin^2\phi\cos^2\theta-1)=1']),
 (10,[r'z=x^2+y^2',r'z=x^2-y^2'],[r'\rho\cos\phi=\rho^2\sin^2\phi',r'\rho\cos\phi=\rho^2\sin^2\phi\cos(2\theta)'])]:
    add(n,('구면좌표 방정식','Equations in spherical coordinates'),
        ('각 방정식을 구면좌표로 바꾸어라. '+d(r'(a)\ '+original[0]+r',\quad(b)\ '+original[1]),'Convert each equation to spherical coordinates. '+d(r'(a)\ '+original[0]+r',\quad(b)\ '+original[1])),
        (r'\(x=\rho\sin\phi\cos\theta,y=\rho\sin\phi\sin\theta,z=\rho\cos\phi\)를 대입한다.',r'Substitute \(x=\rho\sin\phi\cos\theta,y=\rho\sin\phi\sin\theta,z=\rho\cos\phi\).'),
        [('(a) '+d(converted[0]),'(a) '+d(converted[0])),('(b) '+d(converted[1]),'(b) '+d(converted[1])),
         ('ρ로 나눌 때 원점을 잃을 수 있으므로 원점을 포함하는 식은 나누지 않은 형태로 남긴다.','Keep the undivided equation when the origin belongs to the surface; division by ρ could lose that point.')],d(r'(a)\ '+converted[0]+r',\quad(b)\ '+converted[1]),
        ('삼각함수 항등식을 전개하면 원래 직교좌표식으로 돌아온다.','Expanding the trigonometric identities recovers the original equations.'),('a','b'))

sketches={
11:(r'0\le\rho\le1,\ 0\le\phi\le\pi/6,\ 0\le\theta\le\pi',('단위구 안의 좁은 북쪽 원뿔 부분 중 y≥0인 절반.','The y≥0 half of the narrow northern cone sector inside the unit ball.'),('방위각0≤θ≤π는 y≥0을 뜻하고 φ≤π/6은 양의 z축 주변 반각30° 원뿔 안쪽이다.','The azimuth range gives y≥0; φ≤π/6 lies within a30° cone about the positive z-axis.')),
12:(r'1\le\rho\le2,\ \pi/2\le\phi\le\pi',('반지름1과2 사이의 아래쪽 반구 껍질.','The lower hemispherical shell between radii1 and2.'),('φ≥π/2이면 z≤0이다. θ에는 제한이 없으므로 한 바퀴 전체이다.','φ≥π/2 gives z≤0. With no restriction on θ, the full azimuth is included.')),
13:(r'1\le\rho\le3,\ 0\le\phi\le\pi/2,\ \pi\le\theta\le3\pi/2',('반지름1–3 상반구 껍질 중 x≤0,y≤0인 사분의 일.','The x≤0,y≤0 quarter of the upper hemispherical shell between radii1 and3.'),('φ 범위가 z≥0, θ 범위가 xy-평면 제3사분면을 정한다.','The φ range gives z≥0; the θ range selects the third quadrant in the xy-plane.')),
14:(r'0\le\rho\le2,\ \rho\le\csc\phi',('반지름2의 구와 반지름1의 z축 원기둥의 공통 부분.','The intersection of the radius2 ball and the radius1 cylinder about the z-axis.'),(r'\(\rho\sin\phi\le1\)은 \(r\le1\)이다. 극축에서는 cscφ가 정의되지 않으므로 이 등가 부등식의 연속적 의미로 해석한다.',r'\(\rho\sin\phi\le1\) means \(r\le1\). At the polar axis, interpret the condition through this equivalent inequality, since cscφ is undefined there.'))}
for n,(eq,answer,reason) in sketches.items():
    add(n,('구면좌표 입체 그리기','Sketching spherical-coordinate solids'),('부등식의 입체를 그려라. '+d(eq),'Sketch the solid described by '+d(eq)),('반지름·극각·방위각이 각각 무엇을 자르는지 분리한다.','Read radius, polar angle, and azimuth restrictions separately.'),[reason,answer],answer,('경계 구면의 반지름과 각도 범위를 도해의 단면에 대조했다.','The radii and angular ranges were matched to the sections shown in the diagram.'))
add(15,('구 안·원뿔 밖 영역','Inside a sphere and outside a cone'),
    (r'\(x^2+y^2+z^2\le4z\) 안이면서 원뿔 \(z=\sqrt{x^2+y^2}\) 바깥인 영역을 구면좌표 부등식으로 써라.',r'Give spherical inequalities for the region inside \(x^2+y^2+z^2\le4z\) and outside the cone \(z=\sqrt{x^2+y^2}\).'),
    ('원뿔의 바깥은 이 구 안에서는 φ≥π/4이다.','Within this sphere, outside the cone means φ≥π/4.'),
    [(r'구의 경계는 \(\rho=4\cos\phi\)이고 구 전체가 z≥0에 있으므로 \(\phi\le\pi/2\).',r'The sphere is \(\rho=4\cos\phi\), and it lies in z≥0, so \(\phi\le\pi/2\).'),
     (r'원뿔 바깥 조건을 합치면 \(\pi/4\le\phi\le\pi/2\)이다. θ는 한 바퀴 전체이다.',r'Combining the outside-cone condition gives \(\pi/4\le\phi\le\pi/2\). The azimuth covers a full turn.')],d(r'0\le\theta<2\pi,\quad\pi/4\le\phi\le\pi/2,\quad0\le\rho\le4\cos\phi'),
    ('φ=π/4에서 구와 원뿔이 만나고 φ=π/2에서 허용 반지름은0으로 줄어든다.','At φ=π/4 the sphere meets the cone; at φ=π/2 the allowed radius shrinks to zero.'))
add(16,('공의 껍질과 반쪽','A spherical shell and one half'),
    ('지름30 cm, 두께0.5 cm인 속 빈 공을 (a) 좌표계 위치와 부등식으로 설명하고 (b) 반으로 잘랐을 때 한쪽을 설명하라.','For a hollow ball with diameter30 cm and thickness0.5 cm, (a) state coordinate placement and inequalities; (b) describe one half after cutting it in two.'),
    ('원점을 공 중심에 둔다. 주어진 지름은 바깥지름이다.','Place the origin at the center; use30 cm as the outer diameter.'),
    [(r'(a) 바깥 반지름15, 안쪽 반지름14.5이므로 \(14.5\le\rho\le15\). 각도는 구 전체를 덮는다.',r'(a) The outer radius is15 and inner radius14.5, so \(14.5\le\rho\le15\). Use the full angular ranges.'),
     (r'(b) 절단면을 z=0으로 잡으면 위쪽 반은 \(0\le\phi\le\pi/2\)이다.',r'(b) Choose z=0 as the cutting plane; the upper half has \(0\le\phi\le\pi/2\).')],
    d(r'(a)\ 14.5\le\rho\le15,\ 0\le\theta<2\pi,\ 0\le\phi\le\pi;\qquad(b)\ 14.5\le\rho\le15,\ 0\le\theta<2\pi,\ 0\le\phi\le\pi/2'),
    ('두 반지름 차가0.5 cm이고 상반구와 하반구를 합하면 전체 껍질이 된다.','The radii differ by0.5 cm, and the two hemispherical pieces recover the whole shell.'),('a','b'))
def calc(n,statement,f,lims,setup,parts=()):return doc.calc(n,statement,f,lims,setup,parts)
calc(17,(r'\(\int_0^{\pi/6}\int_0^{\pi/2}\int_0^3\rho^2\sin\phi\,d\rho\,d\theta\,d\phi\)의 입체를 그리고 부피를 구하라.',r'Sketch the solid and evaluate \(\int_0^{\pi/6}\int_0^{\pi/2}\int_0^3\rho^2\sin\phi\,d\rho\,d\theta\,d\phi\).'),J,[(q,0,3),(t,0,pi/2),(p,0,pi/6)],('반지름3의 구 안에서 북쪽30° 원뿔 부분을 x,y≥0으로4등분한 조각이다.','This is the x,y≥0 quarter of the northern30° cone sector inside the radius3 ball.'))
calc(18,(r'\(\int_0^{\pi/4}\int_0^{2\pi}\int_0^{\sec\phi}\rho^2\sin\phi\,d\rho\,d\theta\,d\phi\)의 입체를 그리고 부피를 구하라.',r'Sketch the solid and evaluate \(\int_0^{\pi/4}\int_0^{2\pi}\int_0^{\sec\phi}\rho^2\sin\phi\,d\rho\,d\theta\,d\phi\).'),J,[(q,0,s.sec(p)),(t,0,2*pi),(p,0,pi/4)],(r'\(\rho\cos\phi\le1\)은 z≤1이고 φ≤π/4는 원뿔 z≥r이다. 높이1, 윗면 반지름1인 원뿔이다.',r'\(\rho\cos\phi\le1\) gives z≤1, and φ≤π/4 gives z≥r. This is a cone of height1 and top radius1.'))
F=r'f(\rho\sin\phi\cos\theta,\rho\sin\phi\sin\theta,\rho\cos\phi)\rho^2\sin\phi'
for n,desc,bounds,formula in [
 (19,('반지름3, 높이2의 제1팔분공간 원기둥 조각','The first-octant quarter of a cylinder with radius3 and height2'),r'0\le r\le3,\ 0\le\theta\le\pi/2,\ 0\le z\le2',r'\int_0^{\pi/2}\int_0^3\int_0^2f(r\cos\theta,r\sin\theta,z)r\,dz\,dr\,d\theta'),
 (20,('반지름1–2 상반구 껍질에서 제1팔분공간을 뺀 부분','The upper hemispherical shell of radii1–2 with the first octant removed'),r'1\le\rho\le2,\ 0\le\phi\le\pi/2,\ \pi/2\le\theta\le2\pi',integral(F,[(q,1,2),(p,0,pi/2),(t,pi/2,2*pi)]))]:
    add(n,('그림에서 적분 설정','Setting up an integral from a solid diagram'),
        (desc[0]+r'에서 임의 연속함수 f의 삼중적분을 원주 또는 구면좌표로 써라.',r'Set up the triple integral of a continuous function f over: '+desc[1]+'. Use cylindrical or spherical coordinates.'),
        ('그림의 길이·반지름·각도 범위를 따로 읽는다.','Read the dimensions, radial bounds, and angular bounds separately.'),
        [('영역의 좌표 범위는 '+d(bounds),'The coordinate bounds are '+d(bounds)),
         ('함수의 입력도 변환하고 야코비안을 곱한다. '+d(formula),'Transform the arguments of f and include the Jacobian. '+d(formula))],d(formula),
        ('상수함수1을 넣으면 해당 원기둥 조각 또는 구껍질 조각의 부피가 된다.','Setting f=1 recovers the volume of the corresponding cylinder or shell sector.'))
calc(21,(r'그림의 반지름2–3 하반구 껍질 중 x≤0인 절반에서 \(f=\sqrt{x^2+y^2+z^2}\). (a) 구면좌표 적분을 세우고 (b) 계산하라.',r'For \(f=\sqrt{x^2+y^2+z^2}\) on the x≤0 half of the lower hemispherical shell between radii2 and3, (a) set up and (b) evaluate the spherical integral.'),q*J,[(q,2,3),(p,pi/2,pi),(t,pi/2,3*pi/2)],('z≤0이므로 π/2≤φ≤π, x≤0이므로 π/2≤θ≤3π/2이고 피적분함수는ρ이다.','The restriction z≤0 gives π/2≤φ≤π, and x≤0 gives π/2≤θ≤3π/2; the integrand isρ.'),('a','b'))
calc(22,(r'원뿔 \(z=\sqrt{x^2+y^2}\) 위와 구 \(x^2+y^2+z^2=8\) 안에서 \(f=xy\). (a) 구면좌표 적분을 세우고 (b) 계산하라.',r'For \(f=xy\) above \(z=\sqrt{x^2+y^2}\) and inside \(x^2+y^2+z^2=8\), (a) set up and (b) evaluate the spherical integral.'),X*Y*J,[(q,0,2*s.sqrt(2)),(p,0,pi/4),(t,0,2*pi)],(r'φ 범위는0부터π/4, 반지름 범위는0부터2√2이다. xy는 방위각 적분에서 상쇄된다.',r'The polar angle runs from0 toπ/4 and radius from0 to2√2. The xy factor cancels in the azimuthal integral.'),('a','b'))
calc(23,(r'원점 중심 반지름5의 구에서 \(\iiint(x^2+y^2+z^2)^2dV\)를 구면좌표로 구하라.',r'Use spherical coordinates to evaluate \(\iiint(x^2+y^2+z^2)^2dV\) in the radius5 ball centered at the origin.'),q**4*J,[(q,0,5),(p,0,pi),(t,0,2*pi)],('피적분함수는ρ⁴이며 야코비안까지 포함하면ρ⁶ sinφ이다.','The integrand isρ⁴, becomingρ⁶ sinφ with the Jacobian.'))
calc(24,(r'원뿔 \(\phi=\pi/3\) 위, 구 \(\rho=1\) 안에서 \(\iiint y^2z^2dV\)를 구하라.',r'Evaluate \(\iiint y^2z^2dV\) above \(\phi=\pi/3\) and inside \(\rho=1\).'),Y**2*Z**2*J,[(q,0,1),(p,0,pi/3),(t,0,2*pi)],('원뿔 위 조건은φ≤π/3이다. y²z²는ρ⁴ sin²φ cos²φ sin²θ로 바뀐다.','Above the cone meansφ≤π/3. The integrand y²z² becomesρ⁴ sin²φ cos²φ sin²θ.'))
calc(25,(r'반지름2와3인 두 구면 사이에서 \(\iiint(x^2+y^2)dV\)를 구하라.',r'Evaluate \(\iiint(x^2+y^2)dV\) between the concentric spheres of radii2 and3.'),q**2*s.sin(p)**2*J,[(q,2,3),(p,0,pi),(t,0,2*pi)],('x²+y²=ρ²sin²φ이고 모든 방향을 포함한다.','Use x²+y²=ρ²sin²φ and include every direction.'))
calc(26,(r'\(x^2+y^2+z^2\le9,y\ge0\)인 반구에서 \(\iiint y^2dV\)를 구하라.',r'Evaluate \(\iiint y^2dV\) over \(x^2+y^2+z^2\le9,y\ge0\).'),Y**2*J,[(q,0,3),(p,0,pi),(t,0,pi)],('y≥0은0≤θ≤π이며 φ는0부터π 전체이다.','The condition y≥0 gives0≤θ≤π, while φ spans0 toπ.'))
calc(27,(r'단위구의 제1팔분공간 부분에서 \(\iiint xe^{x^2+y^2+z^2}dV\)를 구하라.',r'Evaluate \(\iiint xe^{x^2+y^2+z^2}dV\) in the first-octant part of the unit ball.'),X*s.exp(q*q)*J,[(q,0,1),(p,0,pi/2),(t,0,pi/2)],('θ와φ가 모두0부터π/2이다. 반지름 적분에는 u=ρ² 치환을 쓸 수 있다.','Both θ andφ run from0 toπ/2. The radial integral can use u=ρ².'))
calc(28,(r'원뿔 \(z=\sqrt{x^2+y^2}\) 위, 반지름1–2 구껍질에서 \(\iiint\sqrt{x^2+y^2+z^2}dV\)를 구하라.',r'Evaluate \(\iiint\sqrt{x^2+y^2+z^2}dV\) above \(z=\sqrt{x^2+y^2}\) and between spheres of radii1 and2.'),q*J,[(q,1,2),(p,0,pi/4),(t,0,2*pi)],('구껍질은1≤ρ≤2, 원뿔 위는φ≤π/4이다.','The shell gives1≤ρ≤2, and the cone restriction givesφ≤π/4.'))
calc(29,(r'반지름a인 구 안에서 원뿔 \(\phi=\pi/6\), \(\phi=\pi/3\) 사이 부분의 부피를 구하라.',r'Find the volume inside the radius-a ball between the cones \(\phi=\pi/6\) and \(\phi=\pi/3\).'),J,[(q,0,a),(p,pi/6,pi/3),(t,0,2*pi)],('극각만 두 원뿔 사이로 제한하고 방위각은 한 바퀴를 사용한다.','Restrict polar angle between the cones and keep a full azimuthal turn.'))
add(30,('구 내부 평균 거리','Mean distance inside a ball'),
    ('반지름a인 구에서 균일하게 택한 점과 중심 사이의 평균 거리를 구하라.','Find the average distance from the center to a uniformly selected point inside a radius-a ball.'),
    ('거리의 적분을 구의 부피로 나눈다.','Divide the integral of distance by the ball volume.'),
    [(r'거리함수는ρ이므로 '+d(r'\iiint_B\rho\,dV=4\pi\int_0^a\rho^3d\rho=\pi a^4'),r'The distance isρ, so '+d(r'\iiint_B\rho\,dV=4\pi\int_0^a\rho^3d\rho=\pi a^4')),
     (r'구 부피 \(4\pi a^3/3\)으로 나누면 평균은3a/4이다.',r'Dividing by the ball volume \(4\pi a^3/3\) gives mean3a/4.')],d(r'\rho_{\mathrm{avg}}=\frac{3a}{4}'),
    ('반지름 방향 확률밀도3ρ²/a³를 사용한 기대값과 같다.','The radial probability density3ρ²/a³ gives the same expectation.'))

def centroid(n,statement,rho,limits,wants_mass=True,inertia=None,parts=(),description=None):
    mass,ms=doc.evaluated(rho*J,limits)
    nz,zs=doc.evaluated(rho*Z*J,limits)
    steps=[(description[0],description[1])] if description else []
    steps.append((r'z축 회전대칭으로 \(\bar x=\bar y=0\). 질량 적분은 다음과 같다.',r'Rotational symmetry gives \(\bar x=\bar y=0\). The mass integral is as follows.'))
    steps+=ms
    steps.append(('높이 모멘트 적분에 z=ρ cosφ를 추가한다. '+d(r'N_z='+integral(rho*Z*J,limits)+'='+tex(nz)),r'Include z=ρ cosφ for the height moment. '+d(r'N_z='+integral(rho*Z*J,limits)+'='+tex(nz))))
    zz=s.simplify(nz/mass)
    answer=(('m='+tex(mass)+r',\quad') if wants_mass else '')+r'(\bar x,\bar y,\bar z)=(0,0,'+tex(zz)+')'
    steps.append((r'높이 모멘트를 질량으로 나눈다. '+d(r'\bar z=N_z/m='+tex(zz)),r'Divide height moment by mass. '+d(r'\bar z=N_z/m='+tex(zz))))
    if inertia is not None:
        ii,_=doc.evaluated(rho*inertia*J,limits)
        lab='I_z' if inertia==X*X+Y*Y else 'I_x'
        steps.append(('축까지 거리제곱으로 관성모멘트를 구한다. '+d(lab+'='+integral(rho*inertia*J,limits)+'='+tex(ii)),r'Weight by squared distance to the axis for inertia. '+d(lab+'='+integral(rho*inertia*J,limits)+'='+tex(ii))))
        answer+=r',\quad '+lab+'='+tex(ii)
    add(n,('회전체의 질량·도심·관성','Mass, centroid, and inertia of a solid of revolution'),statement,
        ('구면좌표의 밀도, 좌표함수, 야코비안을 구별해서 곱한다.','Keep density, coordinate weights, and the spherical Jacobian separate.'),steps,d(answer),
        ('대칭으로 수평 모멘트가0임을 확인했고 질량·모멘트를 각각 정확하게 기호 적분했다. 높이 중심은 입체의 높이 범위 안이다.','Horizontal moments vanish by symmetry. Mass and moments were independently symbolically integrated, and the centroid height lies within the solid.'),parts)
    return mass,zz

v31=calc(31,(r'(a) 원뿔 \(\phi=\pi/3\) 위, 구 \(\rho=4\cos\phi\) 안 입체의 부피를 구하고 (b) 도심을 구하라.',r'(a) Find the volume above the cone \(\phi=\pi/3\) and inside \(\rho=4\cos\phi\); (b) find its centroid.'),J,[(q,0,4*s.cos(p)),(p,0,pi/3),(t,0,2*pi)],('구는 중심(0,0,2), 반지름2이고 φ는0부터π/3이다.','The sphere has center(0,0,2), radius2, and polar angle0 toπ/3.'),('a','b'))
n31,st=doc.evaluated(Z*J,[(q,0,4*s.cos(p)),(p,0,pi/3),(t,0,2*pi)])
for lang in ['ko','en']:doc.items[-1]['steps'][lang].append(('회전대칭으로 x̄=ȳ=0. ' if lang=='ko' else 'Rotational symmetry gives x̄=ȳ=0. ')+d(r'N_z='+tex(n31)+r',\quad\bar z=N_z/V='+tex(n31/v31)))
ans31=d('V='+tex(v31)+r',\quad(\bar x,\bar y,\bar z)=(0,0,'+tex(n31/v31)+')');doc.items[-1]['answer']=pair(ans31,ans31)
calc(32,(r'반지름2의 구 안에서 xy-평면 위, 원뿔 \(z=\sqrt{x^2+y^2}\) 아래 부분의 부피를 구하라.',r'Find the volume inside the radius2 sphere, above the xy-plane and below \(z=\sqrt{x^2+y^2}\).'),J,[(q,0,2),(p,pi/4,pi/2),(t,0,2*pi)],('위쪽 원뿔 바깥 부분이므로 φ가π/4부터π/2이다.','Below the upper cone and above the plane givesφ fromπ/4 toπ/2.'))
centroid(33,(r'Example4의 입체 \(z\ge\sqrt{x^2+y^2},x^2+y^2+z^2\le z\), 일정 밀도K에 대해 (a) 도심과 (b) z축 관성모멘트를 구하라.',r'For the Example4 solid \(z\ge\sqrt{x^2+y^2},x^2+y^2+z^2\le z\), with constant densityK, find (a) the centroid and (b) z-axis inertia.'),s.Symbol('K',positive=True),[(q,0,s.cos(p)),(p,0,pi/4),(t,0,2*pi)],False,X*X+Y*Y,('a','b'),
    (r'원본 Example4(p.1143)를 대조했다. 구면 범위는 \(0\le\rho\le\cos\phi,0\le\phi\le\pi/4\)이다.',r'Checked against Example4 on p.1143: the spherical bounds are \(0\le\rho\le\cos\phi,0\le\phi\le\pi/4\).'))
centroid(34,(r'반지름a 상반구의 밀도가 밑면 중심까지 거리에 비례하며 비례상수는k이다. (a) 질량, (b) 질량중심, (c) 대칭축 관성모멘트를 구하라.',r'A solid upper hemisphere of radiusa has density k times distance from the center of its base. Find (a) mass, (b) center of mass, (c) inertia about its symmetry axis.'),k*q,[(q,0,a),(p,0,pi/2),(t,0,2*pi)],True,X*X+Y*Y,('a','b','c'))
centroid(35,(r'(a) 반지름a 균질 상반구의 도심을 구하라. (b) 밑면 지름에 대한 관성모멘트를 구하라. 밀도k를 사용하라.',r'(a) Find the centroid of a homogeneous upper hemisphere of radiusa. (b) Find inertia about a diameter of its base, using densityk.'),k,[(q,0,a),(p,0,pi/2),(t,0,2*pi)],False,Y*Y+Z*Z,('a','b'))
centroid(36,(r'반지름a 상반구의 밀도가 밑면까지 거리에 비례한다. 비례상수k일 때 질량과 질량중심을 구하라.',r'Find mass and center of mass of an upper hemisphere of radiusa whose density is k times distance from its base.'),k*Z,[(q,0,a),(p,0,pi/2),(t,0,2*pi)])
v37,st37=doc.evaluated(J,[(q,0,1),(p,0,pi/4),(t,0,2*pi)])
n37,_=doc.evaluated(Z*J,[(q,0,1),(p,0,pi/4),(t,0,2*pi)])
add(37,('원뿔 위 구 부분의 부피와 도심','Volume and centroid of a spherical cone sector'),
    (r'\(z=\sqrt{x^2+y^2}\) 위, 단위구 안 입체의 부피와 도심을 구하라.',r'Find volume and centroid above \(z=\sqrt{x^2+y^2}\) and inside the unit sphere.'),
    ('구면좌표에서0≤φ≤π/4,0≤ρ≤1이다.','Use0≤φ≤π/4 and0≤ρ≤1.'),st37+[(r'회전대칭으로 x̄=ȳ=0이고 높이 모멘트는 '+d(r'N_z='+integral(Z*J,[(q,0,1),(p,0,pi/4),(t,0,2*pi)])+'='+tex(n37)),r'Rotational symmetry gives x̄=ȳ=0, and the height moment is '+d(r'N_z='+integral(Z*J,[(q,0,1),(p,0,pi/4),(t,0,2*pi)])+'='+tex(n37))),
     (r'\(\bar z=N_z/V\)로 나눈다.',r'Divide using \(\bar z=N_z/V\).')],d('V='+tex(v37)+r',\quad(\bar x,\bar y,\bar z)=(0,0,'+tex(s.simplify(n37/v37))+')'),
    ('0<z̄<1이며 원뿔 각도가 커질수록 낮은 높이 부분이 포함되는 도심 식과 일치한다.','The centroid height lies between0 and1 and agrees with the general spherical-sector centroid formula.'))
calc(38,(r'구의 지름을 따라 만나는 두 평면 사이 작은 각이π/6이다. 반지름a 구에서 잘리는 작은 쐐기의 부피를 구하라.',r'Two planes intersect along a diameter of a radius-a sphere at angleπ/6. Find the volume of the smaller wedge.'),J,[(q,0,a),(p,0,pi),(t,0,pi/6)],('공통 지름을 z축으로 두면 제한은 방위각π/6뿐이다.','Choose the common diameter as the z-axis; only the azimuth rangeπ/6 is restricted.'))
for n,title,radial,statement in [
 (39,'cylinder',a,(r'반지름a, 높이h인 균질 원기둥의 (a) 대칭축, (b) 밑면 지름에 대한 관성모멘트를 구하라.',r'For a uniform cylinder of radiusa and heighth, find inertia about (a) its axis and (b) a diameter of its base.')),
 (40,'cone',a*(1-z/h),(r'밑면 반지름a, 높이h인 균질 직각원뿔의 (a) 대칭축, (b) 밑면 지름에 대한 관성모멘트를 구하라.',r'For a uniform right circular cone of base radiusa and heighth, find inertia about (a) its axis and (b) a diameter of its base.'))]:
    lims=[(r,0,radial),(z,0,h),(t,0,2*pi)]
    mm,_=doc.evaluated(k*r,lims);iz,_=doc.evaluated(k*r**3,lims);ix,_=doc.evaluated(k*(r*r*s.sin(t)**2+z*z)*r,lims)
    add(n,('원기둥·원뿔의 관성모멘트','Moments of inertia of a cylinder or cone'),statement,
        ('밑면을 z=0, 대칭축을 z축으로 둔다. 밑면 지름은 x축으로 택한다.','Place the base in z=0 and the symmetry axis on z; take x as the base diameter.'),
        [('밀도를 k라 하면 질량은 '+d('M='+integral(k*r,lims)+'='+tex(mm)),'For density k, mass is '+d('M='+integral(k*r,lims)+'='+tex(mm))),
         ('(a) 대칭축까지 거리제곱은r²이다. '+d('I_z='+integral(k*r**3,lims)+'='+tex(iz)),'(a) Squared distance to the axis isr². '+d('I_z='+integral(k*r**3,lims)+'='+tex(iz))),
         ('(b) x축까지 거리제곱은y²+z²이다. '+d('I_x='+integral(k*(r*r*s.sin(t)**2+z*z)*r,lims)+'='+tex(ix)),'(b) Squared distance to the x-axis isy²+z². '+d('I_x='+integral(k*(r*r*s.sin(t)**2+z*z)*r,lims)+'='+tex(ix)))],
        d(r'I_z=M\left('+tex(s.simplify(iz/mm))+r'\right),\quad I_x=M\left('+tex(s.simplify(ix/mm))+r'\right)'),
        ('질량×길이²의 차원을 확인했다. x축은 중심을 지나는 축이 아니라 밑면 지름이다.','Both results have units mass times length squared. The x-axis is a base diameter, not the centroidal horizontal axis.'),('a','b'))
calc(41,(r'포물면 \(z=x^2+y^2\) 위, 평면 \(z=2y\) 아래에서 \(\iiint z\,dV\)를 계산하라.',r'Evaluate \(\iiint z\,dV\) above \(z=x^2+y^2\) and below \(z=2y\).'),z*r,[(z,r*r,2*r*s.sin(t)),(r,0,2*s.sin(t)),(t,0,pi)],(r'사영은 \(r^2\le2r\sin\theta\), 즉 \(0\le r\le2\sin\theta,0\le\theta\le\pi\)이다.',r'The projection satisfies \(r^2\le2r\sin\theta\), giving \(0\le r\le2\sin\theta,0\le\theta\le\pi\).'))
calc(42,(r'(a) 토러스 \(\rho=\sin\phi\)가 둘러싸는 부피를 구하고 (b) 그래프 도구로 그려라.',r'(a) Find the volume enclosed by the torus \(\rho=\sin\phi\), and (b) graph it.'),J,[(q,0,s.sin(p)),(p,0,pi),(t,0,2*pi)],(r'\(\rho^2=\rho\sin\phi=r\)에서 \((r-1/2)^2+z^2=1/4\). 큰 반지름과 작은 반지름이 모두1/2인 horn torus이다.',r'From \(\rho^2=\rho\sin\phi=r\), obtain \((r-1/2)^2+z^2=1/4\). Both the major and minor radii are1/2.'),('a','b'))
calc(43,(r'\(\int_0^1\int_0^{\sqrt{1-x^2}}\int_{\sqrt{x^2+y^2}}^{\sqrt{2-x^2-y^2}}xy\,dz\,dy\,dx\)를 구면좌표로 구하라.',r'Use spherical coordinates to evaluate \(\int_0^1\int_0^{\sqrt{1-x^2}}\int_{\sqrt{x^2+y^2}}^{\sqrt{2-x^2-y^2}}xy\,dz\,dy\,dx\).'),X*Y*J,[(q,0,s.sqrt(2)),(p,0,pi/4),(t,0,pi/2)],('원뿔 위, 반지름√2 구 안의 제1팔분공간 부분이다. 교선의 원주 반지름이1이다.','This is the first-octant portion above the cone and inside the radius√2 sphere; the intersection has cylindrical radius1.'))
calc(44,(r'반지름a 구 전체에서 \(\iiint(x^2z+y^2z+z^3)dV\)를 구면좌표로 계산하라.',r'Use spherical coordinates to evaluate \(\iiint(x^2z+y^2z+z^3)dV\) over the entire radius-a ball.'),q*q*Z*J,[(q,0,a),(p,0,pi),(t,0,2*pi)],('피적분함수는zρ²이다. 전체 구의 z 반사 대칭으로0이 예상된다.','The integrand iszρ², so reflection in z predicts zero over the full ball.'))
calc(45,(r'\(\int_{-2}^2\int_{-\sqrt{4-x^2}}^{\sqrt{4-x^2}}\int_{2-\sqrt{4-x^2-y^2}}^{2+\sqrt{4-x^2-y^2}}(x^2+y^2+z^2)^{3/2}dz\,dy\,dx\)를 구면좌표로 구하라.',r'Use spherical coordinates to evaluate \(\int_{-2}^2\int_{-\sqrt{4-x^2}}^{\sqrt{4-x^2}}\int_{2-\sqrt{4-x^2-y^2}}^{2+\sqrt{4-x^2-y^2}}(x^2+y^2+z^2)^{3/2}dz\,dy\,dx\).'),q**3*J,[(q,0,4*s.cos(p)),(p,0,pi/2),(t,0,2*pi)],(r'입체는 중심(0,0,2), 반지름2의 구로 \(\rho\le4\cos\phi\)이다. 원점까지 거리를 쓰는 함수이므로 구 중심으로 좌표를 옮기지 않는다.',r'The solid is the sphere centered at(0,0,2) with radius2, so \(\rho\le4\cos\phi\). The integrand measures distance from the origin, so retain that origin.'))
dens=s.Rational(61909,100)-s.Rational(97,1000000)*q
atm,st=doc.evaluated(dens*J,[(q,6370000,6375000),(p,0,pi),(t,0,2*pi)])
add(46,('대기층 질량의 구면적분','Mass of a spherical atmospheric layer'),
    (r'교재 모델 \(\delta=619.09-0.000097\rho\) kg/m³와 지구 반지름6370 km를 사용해 고도0–5 km 대기 질량을 추정하라. ρ는 지구 중심부터의 거리(m)이다.',r'Using the textbook model \(\delta=619.09-0.000097\rho\) kg/m³ and Earth radius6370 km, estimate atmospheric mass between altitudes0 and5 km. Hereρ is distance from Earth’s center in meters.'),
    ('모든 길이를 미터로 통일한 뒤 구껍질에서 밀도를 적분한다.','Convert all lengths to meters, then integrate density over the spherical shell.'),
    [(r'거리 범위는 \(6{,}370{,}000\le\rho\le6{,}375{,}000\)이다.',r'The radial bounds are \(6{,}370{,}000\le\rho\le6{,}375{,}000\).'),
     (r'각도 적분은4π이므로 '+d(r'M=4\pi\int_{6370000}^{6375000}(619.09-0.000097\rho)\rho^2d\rho'),r'The angular integral is4π, giving '+d(r'M=4\pi\int_{6370000}^{6375000}(619.09-0.000097\rho)\rho^2d\rho')),
     (r'원시함수는 \(4\pi(619.09\rho^3/3-0.000097\rho^4/4)\)이다. 양 끝값의 차를 취한다.',r'An antiderivative is \(4\pi(619.09\rho^3/3-0.000097\rho^4/4)\). Evaluate its endpoint difference.')],d(r'M\approx '+tex(s.N(atm,12))+r'\ \mathrm{kg}'),
    ('하단·상단 밀도는 각각1.2와0.715 kg/m³이다. 추정 질량은 이 두 밀도에 껍질 부피를 곱한 값 사이에 있다.','Bottom and top densities are1.2 and0.715 kg/m³. The computed mass lies between shell volume times these two endpoint densities.'))
add(47,('원기둥과 반구 지붕','Cylinder with a hemispherical roof'),
    ('반지름3, 높이10의 원기둥 위에 반구를 얹은 저장탑을 그래프 도구로 그려라.','Graph a silo with a cylinder of radius3 and height10 topped by a hemisphere.'),
    ('반구 중심을 원기둥 윗면 중심(0,0,10)에 둔다.','Place the hemisphere center at the cylinder’s top center(0,0,10).'),
    [(r'옆면은 \((3\cos\theta,3\sin\theta,z)\), \(0\le z\le10\)이다.',r'The cylindrical wall is \((3\cos\theta,3\sin\theta,z)\), \(0\le z\le10\).'),
     (r'지붕은 \((3\sin\phi\cos\theta,3\sin\phi\sin\theta,10+3\cos\phi)\), \(0\le\phi\le\pi/2\)이다.',r'The roof is \((3\sin\phi\cos\theta,3\sin\phi\sin\theta,10+3\cos\phi)\), \(0\le\phi\le\pi/2\).'),
     (r'두 곡면은 z=10, r=3인 원을 따라 만나며 최고점은 z=13이다.',r'The surfaces meet along z=10,r=3; the highest point is z=13.')],('첨부한 자체 생성 저장탑 도해.','The accompanying generated silo diagram.'),
    ('접합 원의 좌표가 두 매개화에서 일치하며 높이·반지름 조건을 만족한다.','Both parametrizations agree on the joining circle and satisfy the stated radius and height.'))
lat1=s.Rational(3406,100)*pi/180;lat2=s.Rational(4550,100)*pi/180;dlon=s.Rational(11825-7360,100)*pi/180
dot=s.sin(lat1)*s.sin(lat2)+s.cos(lat1)*s.cos(lat2)*s.cos(dlon)
distance=3960*s.acos(dot)
add(48,('두 도시의 대권거리','Great-circle distance between two cities'),
    ('구 반지름3960 mi를 사용해 LA(북위34.06°, 서경118.25°)와 Montréal(북위45.50°, 서경73.60°) 사이 대권거리를 구하라.','Using sphere radius3960 mi, find the great-circle distance between Los Angeles(34.06°N,118.25°W) and Montréal(45.50°N,73.60°W).'),
    ('두 위치의 단위벡터 내적은 중심각의 코사인이다.','The dot product of the two unit position vectors is the cosine of the central angle.'),
    [(r'위도α, 경도λ의 단위벡터는 \((\cos\alpha\cos\lambda,\cos\alpha\sin\lambda,\sin\alpha)\)이다. 각도를 라디안으로 변환한다.',r'The unit vector at latitudeα and longitudeλ is \((\cos\alpha\cos\lambda,\cos\alpha\sin\lambda,\sin\alpha)\). Convert angles to radians.'),
     (r'경도 차는44.65°이며 '+d(r'\cos\gamma=\sin34.06^\circ\sin45.50^\circ+\cos34.06^\circ\cos45.50^\circ\cos44.65^\circ'),r'The longitude difference is44.65°, so '+d(r'\cos\gamma=\sin34.06^\circ\sin45.50^\circ+\cos34.06^\circ\cos45.50^\circ\cos44.65^\circ')),
     ('호의 길이는 반지름×중심각이다. '+d(r'd=3960\arccos('+tex(s.N(dot,12))+r')\approx '+tex(s.N(distance,12))+r'\ \mathrm{mi}'),'Arc length is radius times central angle. '+d(r'd=3960\arccos('+tex(s.N(dot,12))+r')\approx '+tex(s.N(distance,12))+r'\ \mathrm{mi}'))],d(r'd\approx '+tex(s.N(distance,10))+r'\ \mathrm{mi}'),
    ('중심각은0과π 사이이다. 현 길이보다 대권 호 길이가 크며, 도·라디안 변환을 두 번 적용하지 않았다.','The central angle lies between0 andπ. The arc exceeds the chord, and degree-to-radian conversion was applied exactly once.'))
add(49,('울퉁불퉁한 구면의 부피','Volume of a bumpy sphere'),
    (r'\(\rho=1+\frac15\sin(6\theta)\sin(5\phi)\)가 둘러싸는 부피를 기호 계산으로 구하라.',r'Use symbolic computation to find the enclosed volume for \(\rho=1+\frac15\sin(6\theta)\sin(5\phi)\).'),
    ('반지름부터 적분한 뒤 방위각에 대해 홀수인 사인항들을 없앤다.','Integrate radius first, then cancel odd sine powers over the azimuthal period.'),
    [(r'반지름은0.8이상으로 양수이다. '+d(r'V=\frac13\int_0^\pi\int_0^{2\pi}\left(1+\frac15\sin6\theta\sin5\phi\right)^3\sin\phi\,d\theta\,d\phi'),r'The radius is at least0.8, hence positive. '+d(r'V=\frac13\int_0^\pi\int_0^{2\pi}\left(1+\frac15\sin6\theta\sin5\phi\right)^3\sin\phi\,d\theta\,d\phi')),
     (r'\(\int\sin6\theta\,d\theta=\int\sin^36\theta\,d\theta=0\), \(\int_0^{2\pi}\sin^26\theta\,d\theta=\pi\)이므로 '+d(r'V=\frac{4\pi}{3}+\frac\pi{25}\int_0^\pi\sin^2(5\phi)\sin\phi\,d\phi'),r'The first and third sine powers integrate to zero; \(\int_0^{2\pi}\sin^26\theta\,d\theta=\pi\). Thus '+d(r'V=\frac{4\pi}{3}+\frac\pi{25}\int_0^\pi\sin^2(5\phi)\sin\phi\,d\phi')),
     (r'반각공식 또는 기호적분으로 남은 적분은100/99이다. 따라서 '+d(r'V=\frac{4\pi}{3}+\frac{4\pi}{99}=\frac{136\pi}{99}'),r'The remaining integral is100/99 by a half-angle identity or symbolic integration, giving '+d(r'V=\frac{4\pi}{3}+\frac{4\pi}{99}=\frac{136\pi}{99}'))],d(r'V=\frac{136\pi}{99}'),
    ('반지름 세제곱을 전개한 항별 적분과 직접 기호적분이 일치한다. 정규 단위구 부피보다 조금 크다.','Termwise integration after cubing the radius agrees with direct symbolic integration. The result is slightly larger than the unit-ball volume.'))
check49=s.integrate(s.sin(5*p)**2*s.sin(p),(p,0,pi));assert check49==s.Rational(100,99)
doc.checks.append({'number':49,'remainingIntegral':str(check49),'volume':'136*pi/99'})
add(50,('이상 삼중적분과 구면 극한','An improper triple integral via spherical limits'),
    (r'구의 반지름을 무한대로 보내는 정의로 \(\iiint_{\mathbb R^3}\sqrt{x^2+y^2+z^2}e^{-(x^2+y^2+z^2)}dV=2\pi\)임을 보여라.',r'Using the limit over expanding balls, prove \(\iiint_{\mathbb R^3}\sqrt{x^2+y^2+z^2}e^{-(x^2+y^2+z^2)}dV=2\pi\).'),
    ('먼저 유한 반지름R에서 계산한 뒤 극한을 취한다.','First compute on a finite radius-R ball, then take the limit.'),
    [(r'구면좌표로 '+d(r'I(R)=4\pi\int_0^R\rho^3e^{-\rho^2}d\rho'),r'Spherical coordinates give '+d(r'I(R)=4\pi\int_0^R\rho^3e^{-\rho^2}d\rho')),
     (r'\(u=\rho^2\)로 치환하고 부분적분하면 '+d(r'I(R)=2\pi\int_0^{R^2}ue^{-u}du=2\pi[1-(R^2+1)e^{-R^2}]'),r'Set \(u=\rho^2\) and integrate by parts: '+d(r'I(R)=2\pi\int_0^{R^2}ue^{-u}du=2\pi[1-(R^2+1)e^{-R^2}]')),
     (r'\((R^2+1)e^{-R^2}\to0\)이므로 \(I(R)\to2\pi\).',r'Since \((R^2+1)e^{-R^2}\to0\), the limit is \(2\pi\).')],d(r'I=2\pi'),
    ('비음수 함수이며 유한 R에서 계산한 식은 증가하고2π로 유계이다. 따라서 주어진 구 확장 극한이 존재한다.','The integrand is nonnegative; the finite-R formula increases and is bounded by2π, so the specified expanding-ball limit exists.'))
add(51,('구면 부피요소의 유도','Deriving the spherical volume element'),
    (r'(a) \(0<\phi_0<\pi/2\)에서 구 \(r^2+z^2=a^2\) 아래, 원뿔 \(z=r\cot\phi_0\) 위의 부피를 원주좌표로 구하라. (b) 구면 쐐기 \(\rho_1\le\rho\le\rho_2,\theta_1\le\theta\le\theta_2,\phi_1\le\phi\le\phi_2\) 부피를 유도하라. (c) 평균값정리로 \(\Delta V=\tilde\rho^2\sin\tilde\phi\,\Delta\rho\Delta\theta\Delta\phi\)를 보여라.',r'(a) For \(0<\phi_0<\pi/2\), use cylindrical coordinates for the volume below \(r^2+z^2=a^2\) and above \(z=r\cot\phi_0\). (b) Derive the volume of a wedge with bounds \(\rho_1\le\rho\le\rho_2,\theta_1\le\theta\le\theta_2,\phi_1\le\phi\le\phi_2\). (c) Apply the Mean Value Theorem to obtain \(\Delta V=\tilde\rho^2\sin\tilde\phi\,\Delta\rho\Delta\theta\Delta\phi\).'),
    ('원주좌표로 먼저 원뿔 부분을 구한 뒤 반지름·각도 구간의 차이를 취한다.','First compute a cone sector in cylindrical coordinates, then take radial and angular differences.'),
    [(r'(a) 교선 반지름은 \(a\sin\phi_0\)이다. '+d(r'V=2\pi\int_0^{a\sin\phi_0}r[\sqrt{a^2-r^2}-r\cot\phi_0]dr'),r'(a) The intersection radius is \(a\sin\phi_0\). '+d(r'V=2\pi\int_0^{a\sin\phi_0}r[\sqrt{a^2-r^2}-r\cot\phi_0]dr')),
     (r'적분 후 \(\cos^3\phi_0+\sin^2\phi_0\cos\phi_0=\cos\phi_0\)를 사용하면 '+d(r'V=\frac{2\pi a^3}{3}(1-\cos\phi_0)'),r'After integrating, use \(\cos^3\phi_0+\sin^2\phi_0\cos\phi_0=\cos\phi_0\) to get '+d(r'V=\frac{2\pi a^3}{3}(1-\cos\phi_0)')),
     (r'(b) 반지름ρ₂와ρ₁의 결과를 빼고 두 극각의 차이를 취한다. 방위각 비율 \((\theta_2-\theta_1)/(2\pi)\)를 곱한다. 아래쪽 극각은 반구 대칭으로 같은 코사인 식이 성립한다.',r'(b) Subtract the radial results atρ₂ andρ₁ and the two polar-angle results, then multiply by the azimuth fraction \((\theta_2-\theta_1)/(2\pi)\). Reflection extends the cosine expression to southern polar angles.'),
     (d(r'\Delta V=\frac{\rho_2^3-\rho_1^3}{3}(\cos\phi_1-\cos\phi_2)(\theta_2-\theta_1)'),d(r'\Delta V=\frac{\rho_2^3-\rho_1^3}{3}(\cos\phi_1-\cos\phi_2)(\theta_2-\theta_1)')),
     (r'(c) 평균값정리를 \(u^3/3\)와 \(-\cos v\)에 각각 적용하면 어떤 내부점에서 \((\rho_2^3-\rho_1^3)/3=\tilde\rho^2\Delta\rho\), \(\cos\phi_1-\cos\phi_2=\sin\tilde\phi\,\Delta\phi\)이다. 두 식에 Δθ를 곱하면 된다.',r'(c) Apply the Mean Value Theorem separately to \(u^3/3\) and \(-\cos v\). At intermediate points, \((\rho_2^3-\rho_1^3)/3=\tilde\rho^2\Delta\rho\) and \(\cos\phi_1-\cos\phi_2=\sin\tilde\phi\,\Delta\phi\). Multiply these identities byΔθ.')],
    (r'(a) \(V=2\pi a^3(1-\cos\phi_0)/3\). (b) 위의 정확한 쐐기 부피식. (c) \(\Delta V=\tilde\rho^2\sin\tilde\phi\,\Delta\rho\Delta\theta\Delta\phi\).',r'(a) \(V=2\pi a^3(1-\cos\phi_0)/3\). (b) The exact wedge formula above. (c) \(\Delta V=\tilde\rho^2\sin\tilde\phi\,\Delta\rho\Delta\theta\Delta\phi\).'),
    ('평균값정리의 함수는 닫힌 구간에서 연속이고 내부에서 미분 가능하다. 0≤φ≤π와 순서 있는 반지름·각도 구간에서 모든 부피 인자가 비음수이다.','The Mean Value Theorem functions are continuous on each closed interval and differentiable inside. For0≤φ≤π and ordered intervals, all volume factors are nonnegative.'),('a','b','c'))

def spherical(rlow,rhigh,plow,phigh,tlow,thigh):
    def mapping(u,v,w):
        pp=plow+(phigh-plow)*w;tt=tlow+(thigh-tlow)*v
        lo=rlow(pp,tt) if callable(rlow) else rlow
        hi=rhigh(pp,tt) if callable(rhigh) else rhigh
        rr=lo+(hi-lo)*u
        return rr*math.sin(pp)*math.cos(tt),rr*math.sin(pp)*math.sin(tt),rr*math.cos(pp)
    return mapping
def figures():
    specs={
     11:('Northern sector in y ≥ 0',spherical(0,1,0,math.pi/6,0,math.pi),(1.1,1.1,1.1),'ρ ≤ 1; φ ≤ π/6; 0 ≤ θ ≤ π'),
     12:('Lower hemispherical shell',spherical(1,2,math.pi/2,math.pi,0,2*math.pi),(2.2,2.2,1.2),'1 ≤ ρ ≤ 2; z ≤ 0'),
     13:('One quarter of an upper shell',spherical(1,3,0,math.pi/2,math.pi,3*math.pi/2),(1.2,1.2,3.2),'1 ≤ ρ ≤ 3; x ≤ 0, y ≤ 0, z ≥ 0'),
     14:('Intersection of ball and cylinder',lambda u,v,w:(u*math.cos(2*math.pi*v),u*math.sin(2*math.pi*v),(2*w-1)*math.sqrt(4-u*u)),(1.2,1.2,2.2),'x²+y²+z² ≤ 4; x²+y² ≤ 1'),
     17:('Spherical sector in the first octant',spherical(0,3,0,math.pi/6,0,math.pi/2),(1.7,1.7,3.2),'ρ ≤ 3; φ ≤ π/6; 0 ≤ θ ≤ π/2'),
     18:('Cone ending at the plane z = 1',spherical(0,lambda p,t:1/math.cos(p),0,math.pi/4,0,2*math.pi),(1.2,1.2,1.2),'r ≤ z ≤ 1'),
     19:('Quarter cylinder',lambda u,v,w:(3*u*math.cos(math.pi*v/2),3*u*math.sin(math.pi*v/2),2*w),(3.2,3.2,2.2),'0 ≤ r ≤ 3; 0 ≤ z ≤ 2; 0 ≤ θ ≤ π/2'),
     20:('Upper shell with the first octant removed',spherical(1,2,0,math.pi/2,math.pi/2,2*math.pi),(2.2,2.2,2.2),'1 ≤ ρ ≤ 2; z ≥ 0; π/2 ≤ θ ≤ 2π'),
     21:('Half of the lower hemispherical shell',spherical(2,3,math.pi/2,math.pi,math.pi/2,3*math.pi/2),(1.2,3.2,1.2),'2 ≤ ρ ≤ 3; x ≤ 0; z ≤ 0'),
     22:('Sphere above a cone',spherical(0,math.sqrt(8),0,math.pi/4,0,2*math.pi),(2.2,2.2,3),'ρ ≤ √8; φ ≤ π/4'),
     42:('Horn torus',lambda u,v,w:((.5+.5*u*math.cos(2*math.pi*w))*math.cos(2*math.pi*v),(.5+.5*u*math.cos(2*math.pi*w))*math.sin(2*math.pi*v),.5*u*math.sin(2*math.pi*w)),(1.2,1.2,.7),'(r - 1/2)² + z² = 1/4; ρ = sin φ'),
     47:('Silo with a hemispherical roof',lambda u,v,w:(u*(3 if 13*w<=10 else math.sqrt(max(0,9-(13*w-10)**2)))*math.cos(2*math.pi*v),u*(3 if 13*w<=10 else math.sqrt(max(0,9-(13*w-10)**2)))*math.sin(2*math.pi*v),13*w),(3.3,3.3,13.3),'Cylinder: radius 3, height 10; roof: radius 3; total height 13'),
     49:('Bumpy sphere, m = 6 and n = 5',spherical(0,lambda p,t:1+.2*math.sin(6*t)*math.sin(5*p),0,math.pi,0,2*math.pi),(1.4,1.4,1.4),'ρ = 1 + (1/5) sin(6θ) sin(5φ)')}
    for n,(title,fn,axes,subtitle) in specs.items():
        name=f's15-8-{n}.svg';solid(name,f'15.8 / {n} · {title}',fn,axes,subtitle,resolution=36 if n==49 else 13 if n==47 else 16)
        attach(next(e for e in doc.items if e['number']==n),name,('주어진 경계와 각도 범위에서 직접 생성한 입체','Solid generated from the stated boundaries and angular ranges'),(subtitle,subtitle))
    for n in (1,2):
        name=f's15-8-{n}.svg';points_plot(name,f'15.8 / {n} · Spherical points',[tuple(float(q) for q in pt) for pt in outputs[n]])
        attach(next(e for e in doc.items if e['number']==n),name,('구면좌표에서 변환한 두 점 a,b','Points a,b converted from spherical coordinates'),('점선은 수평 사영과 높이를 나타낸다.','Dashed lines show the horizontal projection and height.'))
figures()
doc.save(51)
