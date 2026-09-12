"""Complete original bilingual solutions, source visually checked pp1138-1139."""
import math
import sympy as s
from core_15 import Doc,tex,d,m,integral,pair
from plot_15 import solid,attach
r,z,t=s.symbols('r z theta',nonnegative=True)
a,k,h,R,H=s.symbols('a k h R H',positive=True)
pi=s.pi
doc=Doc('15.7',[1138,1139],lambda n:1138 if n<=27 else 1139)
add=doc.add
points={1:[(5,pi/2,2),(6,-pi/4,-3)],2:[(2,5*pi/6,1),(8,-2*pi/3,5)],3:[(4,4,-3),(5*s.sqrt(3),-5,s.sqrt(3))],4:[(0,-2,9),(-1,s.sqrt(3),6)]}
for n,inputs in points.items():
    forward=n<=2; outputs=[];steps=[]
    for label,p in zip(('a','b'),inputs):
        if forward:
            rr,tt,zz=p;out=tuple(s.simplify(q) for q in (rr*s.cos(tt),rr*s.sin(tt),zz));eq=tex(s.Tuple(*out))
            steps.append((f'({label}) '+d(r'(x,y,z)=(r\cos\theta,r\sin\theta,z)='+eq),f'({label}) '+d(r'(x,y,z)=(r\cos\theta,r\sin\theta,z)='+eq)))
            steps.append((r'xy-평면에서 원점으로부터 '+m(tex(rr))+' 떨어진 점을 각도 '+m(tex(tt))+' 방향으로 잡고, 높이 '+m(tex(zz))+'로 옮긴다.',r'In the xy-plane, move a distance '+m(tex(rr))+' from the origin at angle '+m(tex(tt))+', then move to height '+m(tex(zz))+'.'))
        else:
            xx,yy,zz=p;rr=s.sqrt(xx*xx+yy*yy);tt=s.atan2(yy,xx)%(2*pi);out=(rr,s.simplify(tt),zz);eq=tex(s.Tuple(*out))
            steps.append((f'({label}) '+d(r'r=\sqrt{x^2+y^2}='+tex(rr)+r',\quad \theta='+tex(tt)+r',\quad z='+tex(zz)),f'({label}) '+d(r'r=\sqrt{x^2+y^2}='+tex(rr)+r',\quad \theta='+tex(tt)+r',\quad z='+tex(zz))))
        outputs.append(out)
    statement=(('원주좌표 점을 표시하고 직교좌표로 바꾸어라: ' if forward else '다음 직교좌표를 원주좌표로 바꾸어라: ')+', '.join(f'({c}) '+m(tex(s.Tuple(*p))) for c,p in zip('ab',inputs)),
               ('Plot the cylindrical-coordinate points and find their rectangular coordinates: ' if forward else 'Convert these rectangular coordinates to cylindrical coordinates: ')+', '.join(f'({c}) '+m(tex(s.Tuple(*p))) for c,p in zip('ab',inputs)))
    e=add(n,('원주좌표와 직교좌표','Cylindrical and rectangular coordinates'),statement,
      (r'\(x=r\cos\theta,y=r\sin\theta\)이며 z는 그대로이다. 각도의 사분면을 확인한다.',r'Use \(x=r\cos\theta,y=r\sin\theta\); z is unchanged. Check the angle quadrant.'),steps,
      d(r'(a)\ '+tex(s.Tuple(*outputs[0]))+r',\quad(b)\ '+tex(s.Tuple(*outputs[1]))),
      (r'두 변환을 연이어 적용하면 원래 점으로 돌아온다. 각도는 \(2\pi\)의 정수배 차이까지 동치이다.',r'Applying the inverse conversion recovers the original points. Angles differing by integer multiples of \(2\pi\) are equivalent.'),('a','b'))
    doc.checks.append({'number':n,'inputs':list(map(str,inputs)),'outputs':list(map(str,outputs))})

surfaces={
5:(r'r=2',r'x^2+y^2=4',('z축을 축으로 하는 반지름2의 무한 원기둥.','An infinite circular cylinder of radius2 centered on the z-axis.'),('z에 제한이 없으므로 모든 높이에서 같은 원이다.','No condition restricts z, so every horizontal section is the same circle.')),
6:(r'\theta=\pi/6',r'y=x/\sqrt3,\quad x\ge0,\quad z\in\mathbb R',('z축을 경계로 하고 양의 x축과30°를 이루는 수직 반평면.','A vertical half-plane bounded by the z-axis, at30° to the positive x-axis.'),('r≥0이므로 반직선 방향만 포함한다. 평면 전체로 확장하면 안 된다.','Because r≥0, only the forward radial direction is included, not the entire plane.')),
7:(r'r^2+z^2=4',r'x^2+y^2+z^2=4',('원점 중심 반지름2인 구면.','A sphere of radius2 centered at the origin.'),('r²=x²+y²를 대입하면 원점까지 거리제곱이4이다.','Substitute r²=x²+y² to obtain squared distance4 from the origin.')),
8:(r'r=2\sin\theta',r'x^2+(y-1)^2=1',('축이 직선 x=0,y=1인 반지름1의 원기둥.','A cylinder of radius1 with axis x=0,y=1.'),('양변에 r을 곱해 r²=2y로 만든 뒤 완전제곱한다.','Multiply by r to obtain r²=2y, then complete the square.'))}
for n,(original,eq,answer,reason) in surfaces.items():
    add(n,('원주좌표 곡면 판별','Identifying a cylindrical-coordinate surface'),
        ('곡면 '+m(original)+'를 설명하라.','Describe the surface '+m(original)+'.'),
        ('반지름·각도·높이 중 어떤 좌표가 고정되는지 본다.','Identify which of radius, angle, or height is constrained.'),
        [(reason[0],reason[1]),('직교좌표식은 '+d(eq),'In rectangular coordinates: '+d(eq))],answer,
        ('변환식을 역대입하면 원래 식과 같은 점집합을 얻는다.','Substitution back into cylindrical coordinates gives the original point set.'))
for n,original,converted in [(9,[r'x^2-x+y^2+z^2=1',r'z=x^2-y^2'],[r'r^2-r\cos\theta+z^2=1',r'z=r^2\cos(2\theta)']),
                              (10,[r'2x^2+2y^2-z^2=4',r'2x-y+z=1'],[r'2r^2-z^2=4',r'2r\cos\theta-r\sin\theta+z=1'])]:
    add(n,('원주좌표 방정식','Equations in cylindrical coordinates'),
        ('다음 식을 원주좌표로 바꾸어라. '+d(r'(a)\ '+original[0]+r',\qquad(b)\ '+original[1]),'Convert to cylindrical coordinates. '+d(r'(a)\ '+original[0]+r',\qquad(b)\ '+original[1])),
        (r'\(x^2+y^2=r^2\), \(x=r\cos\theta,y=r\sin\theta\)를 대입한다.',r'Substitute \(x^2+y^2=r^2\), \(x=r\cos\theta,y=r\sin\theta\).'),
        [('(a) '+d(converted[0]),'(a) '+d(converted[0])),('(b) '+d(converted[1]),'(b) '+d(converted[1]))],d(r'(a)\ '+converted[0]+r',\qquad(b)\ '+converted[1]),
        (r'\(\cos^2\theta-\sin^2\theta=\cos2\theta\)를 사용하고 원래 좌표에 역대입했다.',r'Use \(\cos^2\theta-\sin^2\theta=\cos2\theta\), then substitute back into the original coordinates.'),('a','b'))

for n,statement,steps,answer in [
 (11,r'r^2\le z\le8-r^2',[(r'두 경계가 만나는 곳은 \(r^2=8-r^2\), 즉 \(r=2,z=4\)이다.',r'The boundaries meet where \(r^2=8-r^2\), giving \(r=2,z=4\).'),(r'위아래 포물면 사이의 회전 렌즈형 입체이며 아래 꼭짓점은 원점, 위 꼭짓점은 \((0,0,8)\)이다.',r'This is a lens-shaped solid between two paraboloids, from the lower vertex at the origin to the upper vertex \((0,0,8)\).')],r'0\le\theta\le2\pi,\quad0\le r\le2,\quad r^2\le z\le8-r^2'),
 (12,r'0\le\theta\le\pi/2,\quad r\le z\le2',[(r'원뿔 \(z=r\) 위쪽, 평면 \(z=2\) 아래쪽이다.',r'The solid is above the cone \(z=r\) and below the plane \(z=2\).'),(r'각도가 제1사분면만 허용되므로 높이2, 반지름2의 원뿔을 축을 지나도록4등분한 한 조각이다.',r'The angular range retains the first-quadrant quarter of a cone with height2 and top radius2.')],r'0\le\theta\le\pi/2,\quad0\le r\le2,\quad r\le z\le2')]:
    add(n,('원주좌표 입체 그리기','Sketching a cylindrical-coordinate solid'),('다음 부등식의 입체를 그려라. '+d(statement),'Sketch the solid given by '+d(statement)),('교선을 구해 반지름의 최대값을 정한다.','Use the intersection to determine the maximum radius.'),steps,d(answer),('경계의 교선과 축 위 꼭짓점이 그림의 끝점과 일치한다.','The intersection curve and axial vertices agree with the endpoints in the diagram.'))
add(13,('원통 껍질의 좌표 설정','Coordinates for a cylindrical shell'),
    ('길이20 cm, 안쪽 반지름6 cm, 바깥 반지름7 cm인 원통 껍질을 좌표 부등식으로 쓰고 축의 위치를 설명하라.','Describe a cylindrical shell of length20 cm, inner radius6 cm, and outer radius7 cm with coordinate inequalities; explain the coordinate placement.'),
    ('원통의 축을 z축으로 둔다.','Align the cylinder axis with the z-axis.'),
    [('원점은 한쪽 끝면의 중심에 두고 z축을 반대쪽 끝면 방향으로 둔다.','Place the origin at the center of one end face and direct the positive z-axis toward the other end.'),
     (r'반지름은6에서7까지, 높이는0에서20까지이며 각도는 한 바퀴이다.',r'The radius runs from6 to7, height from0 to20, and angle through one full turn.')],d(r'6\le r\le7,\quad0\le\theta<2\pi,\quad0\le z\le20\quad(\mathrm{cm})'),
    (r'단면은 반지름6과7 사이의 원환이며 축 길이는20이다.',r'Every cross-section is an annulus between radii6 and7, and the axial length is20.'))
add(14,('두 포물면 사이 입체','A solid between two paraboloids'),
    (r'그래프 도구로 \(z=x^2+y^2\)와 \(z=5-x^2-y^2\) 사이 입체를 그려라.',r'Use graphing software to draw the solid between \(z=x^2+y^2\) and \(z=5-x^2-y^2\).'),
    ('두 곡면을 원주좌표로 나타내면 같은 원을 따라 만난다.','In cylindrical coordinates the surfaces meet along a circle.'),
    [(r'\(r^2=5-r^2\)에서 \(r=\sqrt{5/2},z=5/2\)이다.',r'Solving \(r^2=5-r^2\) gives \(r=\sqrt{5/2},z=5/2\).'),
     (r'\(0\le r\le\sqrt{5/2},0\le\theta<2\pi\)에서 두 표면 \((r\cos\theta,r\sin\theta,r^2)\), \((r\cos\theta,r\sin\theta,5-r^2)\)를 함께 그린다.',r'For \(0\le r\le\sqrt{5/2},0\le\theta<2\pi\), plot both surfaces \((r\cos\theta,r\sin\theta,r^2)\) and \((r\cos\theta,r\sin\theta,5-r^2)\).')],
    ('첨부 도해의 두 포물면으로 둘러싸인 입체.','The enclosed solid shown in the accompanying generated diagram.'),
    ('윗면과 아랫면은 z=5/2에 대해 대칭이고 교선의 높이·반지름이 일치한다.','The two surfaces are symmetric about z=5/2 and meet at the stated radius and height.'))

def calc(n,ko,en,f,limits,setup,parts=()):return doc.calc(n,(ko,en),f,limits,setup,parts)
calc(15,r'그림의 \(0\le z\le2-x^2-y^2,x^2+y^2\le1\)에서 \(f=x^2+y^2\). (a) 원주좌표 적분을 세우고 (b) 계산하라.',r'For \(0\le z\le2-x^2-y^2,x^2+y^2\le1\) and \(f=x^2+y^2\), (a) set up a cylindrical integral and (b) evaluate it.',r**3,[(z,0,2-r*r),(r,0,1),(t,0,2*pi)],(r'\(f=r^2\), 원기둥 경계는 \(r=1\), \(dV=r\,dz\,dr\,d\theta\)이다.',r'Here \(f=r^2\), the cylinder is \(r=1\), and \(dV=r\,dz\,dr\,d\theta\).'),('a','b'))
calc(16,r'그림의 원뿔 \(z=\sqrt{x^2+y^2}\)와 포물면 \(z=6-x^2-y^2\) 사이에서 \(f=xy\). (a) 원주좌표 적분을 세우고 (b) 계산하라.',r'For \(f=xy\) between the cone \(z=\sqrt{x^2+y^2}\) and paraboloid \(z=6-x^2-y^2\), (a) set up a cylindrical integral and (b) evaluate it.',r**3*s.cos(t)*s.sin(t),[(z,r,6-r*r),(r,0,2),(t,0,2*pi)],(r'교선은 \(r=6-r^2\)에서 \(r=2\). \(xy=r^2\cos\theta\sin\theta\)이다.',r'The intersection \(r=6-r^2\) gives \(r=2\). Also \(xy=r^2\cos\theta\sin\theta\).'),('a','b'))
calc(17,r'\(\int_{\pi/2}^{3\pi/2}\int_0^3\int_{r^2}^9r\,dz\,dr\,d\theta\)의 입체를 그리고 부피를 구하라.',r'Sketch the solid and evaluate \(\int_{\pi/2}^{3\pi/2}\int_0^3\int_{r^2}^9r\,dz\,dr\,d\theta\).',r,[(z,r*r,9),(r,0,3),(t,pi/2,3*pi/2)],(r'포물면 \(z=r^2\) 위, 평면 \(z=9\) 아래의 입체 중 \(x\le0\)인 절반이다.',r'This is the \(x\le0\) half of the solid above \(z=r^2\) and below \(z=9\).'))
calc(18,r'\(\int_0^2\int_0^{2\pi}\int_0^r r\,dz\,d\theta\,dr\)의 입체를 그리고 부피를 구하라.',r'Sketch the solid and evaluate \(\int_0^2\int_0^{2\pi}\int_0^r r\,dz\,d\theta\,dr\).',r,[(z,0,r),(t,0,2*pi),(r,0,2)],(r'반지름2의 원기둥 안에서 \(z=0\) 위, 원뿔 \(z=r\) 아래인 입체이다.',r'The solid is inside the radius2 cylinder, above \(z=0\), and below the cone \(z=r\).'))
calc(19,r'\(x^2+y^2\le16,-5\le z\le4\)에서 \(\iiint\sqrt{x^2+y^2}\,dV\)를 원주좌표로 계산하라.',r'Use cylindrical coordinates to evaluate \(\iiint\sqrt{x^2+y^2}\,dV\) over \(x^2+y^2\le16,-5\le z\le4\).',r*r,[(z,-5,4),(r,0,4),(t,0,2*pi)],(r'반지름4, 높이9의 원기둥이다. 피적분함수는 r이고 야코비안을 포함하면 r²이다.',r'The cylinder has radius4 and height9. The integrand is r, becoming r² after including the Jacobian.'))
calc(20,r'\(z=x^2+y^2\)와 \(z=4\) 사이에서 \(\iiint z\,dV\)를 구하라.',r'Evaluate \(\iiint z\,dV\) between \(z=x^2+y^2\) and \(z=4\).',z*r,[(z,r*r,4),(r,0,2),(t,0,2*pi)],(r'교선에서 r²=4이므로 반지름 범위는0부터2이다.',r'The intersection has r²=4, giving radius range0 to2.'))
calc(21,r'제1팔분공간에서 \(z=4-x^2-y^2\) 아래 영역의 \(\iiint(x+y+z)dV\)를 구하라.',r'Evaluate \(\iiint(x+y+z)dV\) in the first octant below \(z=4-x^2-y^2\).',(r*s.cos(t)+r*s.sin(t)+z)*r,[(z,0,4-r*r),(r,0,2),(t,0,pi/2)],(r'제1팔분공간이므로 각도는0에서π/2이며 높이는0에서4-r²이다.',r'The first octant gives angles0 toπ/2 and height0 to4-r².'))
calc(22,r'\(1\le x^2+y^2\le16,0\le z\le y+4\)에서 \(\iiint(x-y)dV\)를 구하라.',r'Evaluate \(\iiint(x-y)dV\) over \(1\le x^2+y^2\le16,0\le z\le y+4\).',r*r*(s.cos(t)-s.sin(t)),[(z,0,r*s.sin(t)+4),(t,0,2*pi),(r,1,4)],(r'원환에서 높이는4+r sinθ로 음수가 아니다. 각도 적분을 먼저 하면 홀수 삼각항이 소거된다.',r'The annular region has nonnegative height4+r sinθ. Integrating angle before radius cancels odd trigonometric terms.'))
calc(23,r'\(x^2+y^2\le1\), z=0 위와 원뿔 \(z^2=4x^2+4y^2\)의 위쪽 가지 아래에서 \(\iiint x^2dV\)를 구하라.',r'Evaluate \(\iiint x^2dV\) inside \(x^2+y^2\le1\), above z=0 and below the upper branch of \(z^2=4x^2+4y^2\).',r**3*s.cos(t)**2,[(z,0,2*r),(r,0,1),(t,0,2*pi)],(r'z≥0 조건이 원뿔 가지 z=2r을 선택한다.',r'The condition z≥0 selects the cone branch z=2r.'))
calc(24,r'원기둥 \(x^2+y^2\le1\)과 구 \(x^2+y^2+z^2\le4\)의 공통 부분 부피를 구하라.',r'Find the volume common to \(x^2+y^2\le1\) and \(x^2+y^2+z^2\le4\).',r,[(z,-s.sqrt(4-r*r),s.sqrt(4-r*r)),(r,0,1),(t,0,2*pi)],(r'각 r에서 구의 아래·위 반구 사이 높이2√(4-r²)를 사용한다.',r'At each r the height between the lower and upper hemispheres is2√(4-r²).'))
calc(25,r'원뿔 \(z=\sqrt{x^2+y^2}\) 위와 구 \(x^2+y^2+z^2=2\) 아래 사이 입체의 부피를 구하라.',r'Find the volume above \(z=\sqrt{x^2+y^2}\) and inside the sphere \(x^2+y^2+z^2=2\).',r,[(z,r,s.sqrt(2-r*r)),(r,0,1),(t,0,2*pi)],(r'교선은 r²+r²=2이므로 r=1이다.',r'At the intersection, r²+r²=2, so r=1.'))
calc(26,r'포물면 \(z=x^2+y^2\) 위와 구 \(x^2+y^2+z^2=2\) 아래 사이 부피를 구하라.',r'Find the volume above \(z=x^2+y^2\) and inside \(x^2+y^2+z^2=2\).',r,[(z,r*r,s.sqrt(2-r*r)),(r,0,1),(t,0,2*pi)],(r'교선에서 r⁴+r²=2이므로 r²=1이다. 음의 대수적 근은 반지름제곱이 될 수 없다.',r'The intersection satisfies r⁴+r²=2, giving r²=1; the negative algebraic root is inadmissible.'))
V=calc(27,r'\(z=24-x^2-y^2\)와 \(z=2\sqrt{x^2+y^2}\) 사이 입체의 (a) 부피, (b) 도심을 구하라.',r'Find (a) the volume and (b) the centroid between \(z=24-x^2-y^2\) and \(z=2\sqrt{x^2+y^2}\).',r,[(z,2*r,24-r*r),(r,0,4),(t,0,2*pi)],(r'교선은 r²+2r-24=0의 양의 근 r=4이다. 회전대칭으로 x̄=ȳ=0이다.',r'The positive intersection root of r²+2r-24=0 is r=4. Rotational symmetry gives x̄=ȳ=0.'),('a','b'))
Nz,st=doc.evaluated(z*r,[(z,2*r,24-r*r),(r,0,4),(t,0,2*pi)])
for lang,idx in [('ko',0),('en',1)]:doc.items[-1]['steps'][lang]+=[q[idx] for q in st]+[d(r'\bar z=\frac{N_z}{V}='+tex(Nz/V))]
doc.items[-1]['answer']=pair(d('V='+tex(V)+r',\quad(\bar x,\bar y,\bar z)=(0,0,'+tex(Nz/V)+')'),d('V='+tex(V)+r',\quad(\bar x,\bar y,\bar z)=(0,0,'+tex(Nz/V)+')'))

add(28,('구와 치우친 원기둥의 교집합','Intersection of a sphere and an offset cylinder'),
    (r'(a) 원점 중심 반지름a의 구에서 원기둥 \(r=a\cos\theta\) 내부가 잘라내는 부피를 구하라. (b) 두 곡면을 함께 그려라.',r'(a) Find the volume inside both the radius-a sphere centered at the origin and the cylinder \(r=a\cos\theta\). (b) Plot the sphere and cylinder together.'),
    (r'원기둥은 \((x-a/2)^2+y^2=(a/2)^2\)이며 각도는 -π/2에서π/2이다.',r'The cylinder is \((x-a/2)^2+y^2=(a/2)^2\), with angles from-π/2 toπ/2.'),
    [(r'위·아래 구면 사이에 놓인 높이를 적분한다. '+d(r'V=\int_{-\pi/2}^{\pi/2}\int_0^{a\cos\theta}2r\sqrt{a^2-r^2}\,dr\,d\theta'),r'Integrate the height between the two hemispheres. '+d(r'V=\int_{-\pi/2}^{\pi/2}\int_0^{a\cos\theta}2r\sqrt{a^2-r^2}\,dr\,d\theta')),
     (r'r 적분은 \(\frac{2a^3}{3}(1-|\sin\theta|^3)\)이다. θ의 대칭으로0부터π/2 적분의2배를 쓴다.',r'The r-integral is \(\frac{2a^3}{3}(1-|\sin\theta|^3)\). Use twice the angular integral from0 toπ/2.'),
     (r'\(\int_0^{\pi/2}\sin^3\theta\,d\theta=2/3\)이므로 '+d(r'V=\frac{4a^3}{3}\left(\frac\pi2-\frac23\right)'),r'Since \(\int_0^{\pi/2}\sin^3\theta\,d\theta=2/3\), '+d(r'V=\frac{4a^3}{3}\left(\frac\pi2-\frac23\right)')),
     (r'(b) 그림은 a=1로 정규화했다. 모든 좌표를 a배 하면 일반 경우를 얻는다.',r'(b) The diagram is normalized to a=1; multiply all coordinates by a for the general case.')],d(r'V=\frac{2a^3}{9}(3\pi-4)'),
    ('부피가 a³에 비례하며 반구 부피보다 작다. 절댓값을 빠뜨리지 않도록 각도 구간을 대칭으로 나누었다.','The volume scales as a³ and is smaller than a hemisphere. The angular symmetry split preserves the absolute value.'),('a','b'))
V29,st29=doc.evaluated(r,[(z,4*r*r,a),(r,0,s.sqrt(a)/2),(t,0,2*pi)])
Nz29,stz29=doc.evaluated(z*r,[(z,4*r*r,a),(r,0,s.sqrt(a)/2),(t,0,2*pi)])
add(29,('포물면 입체의 질량중심','Centroid of a paraboloid solid'),
    (r'\(z=4x^2+4y^2\)와 \(z=a\), a>0 사이 입체의 일정 밀도가 K일 때 질량과 질량중심을 구하라.',r'Find mass and center of mass between \(z=4x^2+4y^2\) and \(z=a\), a>0, for constant density K.'),
    ('부피를 구해 K를 곱하고, z모멘트를 질량으로 나눈다.','Multiply volume by K for mass and divide the z-moment by mass.'),
    [(r'범위는 \(0\le r\le\sqrt a/2,4r^2\le z\le a\)이다. 회전대칭으로 x̄=ȳ=0.',r'The bounds are \(0\le r\le\sqrt a/2,4r^2\le z\le a\). Rotational symmetry gives x̄=ȳ=0.'),*st29,
     (r'질량은 \(K V\), 높이 모멘트는 '+d(r'N_z=K\int_0^{2\pi}\int_0^{\sqrt a/2}\int_{4r^2}^a zr\,dz\,dr\,d\theta=K'+tex(Nz29)),r'The mass is \(KV\), and the height moment is '+d(r'N_z=K\int_0^{2\pi}\int_0^{\sqrt a/2}\int_{4r^2}^a zr\,dz\,dr\,d\theta=K'+tex(Nz29)))],d(r'm=\frac{K\pi a^2}{8},\quad(\bar x,\bar y,\bar z)=(0,0,2a/3)'),
    ('높이 z의 원판 단면적은 πz/4이므로 1변수 질량·모멘트 적분으로도 같은 값을 얻는다.','The horizontal disk area is πz/4, yielding the same mass and moment by one-variable integration.'))
add(30,('구의 거리 가중 질량','Distance-weighted mass of a ball'),
    (r'반지름a의 원점 중심 구에서 밀도가 z축까지 거리에 비례한다. 비례상수 k>0일 때 질량을 구하라.',r'Find the mass of a radius-a ball when density is k times distance from the z-axis.'),
    (r'밀도 kr과 원주좌표 야코비안 r을 모두 곱한다.',r'Include both the density kr and the cylindrical Jacobian r.'),
    [(r'각 r의 높이는 두 반구 사이 거리이므로 '+d(r'M=4\pi k\int_0^a r^2\sqrt{a^2-r^2}dr'),r'The height at each radius is the distance between the two hemispheres: '+d(r'M=4\pi k\int_0^a r^2\sqrt{a^2-r^2}dr')),
     (r'\(r=a\sin u\), \(0\le u\le\pi/2\)로 치환하면 '+d(r'M=4\pi k a^4\int_0^{\pi/2}\sin^2u\cos^2u\,du'),r'Substitute \(r=a\sin u\), \(0\le u\le\pi/2\): '+d(r'M=4\pi k a^4\int_0^{\pi/2}\sin^2u\cos^2u\,du')),
     (r'\(\sin^2u\cos^2u=(1-\cos4u)/8\)의 적분은 \(\pi/16\)이다.',r'The identity \(\sin^2u\cos^2u=(1-\cos4u)/8\) gives integral \(\pi/16\).')],d(r'M=\frac{\pi^2ka^4}{4}'),
    (r'구면좌표에서 밀도 \(k\rho\sin\phi\)를 적분해도 같은 값이다.',r'Spherical integration of density \(k\rho\sin\phi\) gives the same result.'))

calc(31,r'\(\int_{-2}^2\int_{-\sqrt{4-y^2}}^{\sqrt{4-y^2}}\int_{\sqrt{x^2+y^2}}^2xz\,dz\,dx\,dy\)를 원주좌표로 계산하라.',r'Convert and evaluate \(\int_{-2}^2\int_{-\sqrt{4-y^2}}^{\sqrt{4-y^2}}\int_{\sqrt{x^2+y^2}}^2xz\,dz\,dx\,dy\).',r*r*z*s.cos(t),[(z,r,2),(r,0,2),(t,0,2*pi)],(r'밑면은 반지름2의 원판이며 r≤z≤2이다. xz와 야코비안의 곱은 r²z cosθ이다.',r'The base is the radius2 disk and r≤z≤2. The transformed integrand including the Jacobian is r²z cosθ.'))
calc(32,r'\(\int_{-3}^3\int_0^{\sqrt{9-x^2}}\int_0^{9-x^2-y^2}\sqrt{x^2+y^2}\,dz\,dy\,dx\)를 원주좌표로 계산하라.',r'Convert and evaluate \(\int_{-3}^3\int_0^{\sqrt{9-x^2}}\int_0^{9-x^2-y^2}\sqrt{x^2+y^2}\,dz\,dy\,dx\).',r*r,[(z,0,9-r*r),(r,0,3),(t,0,pi)],(r'밑면은 y≥0인 반원판이므로 각도는0부터π이다.',r'The base is the half-disk y≥0, so the angle runs from0 toπ.'))
num=s.Rational(200,12)*pi*62000**2*12400**2
add(33,('산을 형성하는 일','Work required to form a mountain'),
    (r'해수면에서 원뿔 모양 산을 만든다. (a) 점 P의 무게밀도 g(P), 높이 h(P)를 써서 일을 적분으로 표현하라. (b) 반지름62000 ft, 높이12400 ft, 일정 무게밀도200 lb/ft³인 산의 일을 구하라.',r'A conical mountain is raised from sea level. (a) Express the work using weight density g(P) and height h(P). (b) Calculate it for radius62000 ft, height12400 ft, and constant weight density200 lb/ft³.'),
    ('작은 부피의 무게에 들어 올리는 높이를 곱한다.','Multiply the weight of a small volume by its lifting height.'),
    [(r'(a) \(dW=g(P)h(P)dV\)이므로 \(W=\iiint_E g(P)h(P)dV\). 원뿔 밑면을 z=0에 두면 h(P)=z이다.',r'(a) \(dW=g(P)h(P)dV\), so \(W=\iiint_E g(P)h(P)dV\). With the base in z=0, h(P)=z.'),
     (r'반지름R, 높이H에 대해 높이z 단면의 반지름은 R(1-z/H)이다. '+d(r'W=\int_0^H\int_0^{2\pi}\int_0^{R(1-z/H)}g(r\cos\theta,r\sin\theta,z)\,zr\,dr\,d\theta\,dz'),r'The cross-section radius at height z is R(1-z/H). '+d(r'W=\int_0^H\int_0^{2\pi}\int_0^{R(1-z/H)}g(r\cos\theta,r\sin\theta,z)\,zr\,dr\,d\theta\,dz')),
     (r'(b) 일정 무게밀도 w이면 '+d(r'W=w\pi R^2\int_0^H z(1-z/H)^2dz=\frac{w\pi R^2H^2}{12}'),r'(b) For constant weight density w, '+d(r'W=w\pi R^2\int_0^H z(1-z/H)^2dz=\frac{w\pi R^2H^2}{12}')),
     ('주어진 값을 대입하면 '+d('W='+tex(num)+r'\ \mathrm{ft\cdot lb}\approx '+str(s.N(num,12))+r'\ \mathrm{ft\cdot lb}'),'Substitution gives '+d('W='+tex(num)+r'\ \mathrm{ft\cdot lb}\approx '+str(s.N(num,12))+r'\ \mathrm{ft\cdot lb}'))],
    (r'(a) \(W=\iiint_E gh\,dV\). (b) '+d(r'W\approx '+str(s.N(num,12))+r'\ \mathrm{ft\cdot lb}'),r'(a) \(W=\iiint_E gh\,dV\). (b) '+d(r'W\approx '+str(s.N(num,12))+r'\ \mathrm{ft\cdot lb}')),
    ('균질 원뿔의 무게 wπR²H/3에 도심 높이H/4를 곱한 독립 계산과 같다. 무게밀도이므로 중력가속도를 다시 곱하지 않는다.','Independently, multiply cone weight wπR²H/3 by centroid heightH/4. Because this is weight density, do not multiply by gravitational acceleration again.'),('a','b'))

def figures():
    specs={11:('Between two paraboloids',lambda u,v,w:(2*u*math.cos(2*math.pi*v),2*u*math.sin(2*math.pi*v),4*u*u+w*(8-8*u*u)),(2.3,2.3,8.3),'r² ≤ z ≤ 8 - r²; 0 ≤ r ≤ 2'),
           12:('Quarter cone',lambda u,v,w:(2*u*w*math.cos(math.pi*v/2),2*u*w*math.sin(math.pi*v/2),2*w),(2.2,2.2,2.2),'0 ≤ θ ≤ π/2; r ≤ z ≤ 2'),
           14:('Two paraboloids',lambda u,v,w:(math.sqrt(2.5)*u*math.cos(2*math.pi*v),math.sqrt(2.5)*u*math.sin(2*math.pi*v),2.5*u*u+w*(5-5*u*u)),(1.8,1.8,5.2),'z = r² and z = 5 - r²; intersection r = √(5/2)'),
           15:('Cylinder under a paraboloid',lambda u,v,w:(u*math.cos(2*math.pi*v),u*math.sin(2*math.pi*v),w*(2-u*u)),(1.2,1.2,2.2),'r ≤ 1; 0 ≤ z ≤ 2 - r²'),
           16:('Cone and paraboloid',lambda u,v,w:(2*u*math.cos(2*math.pi*v),2*u*math.sin(2*math.pi*v),2*u+w*(6-4*u*u-2*u)),(2.2,2.2,6.2),'r ≤ z ≤ 6 - r²; intersection r = 2'),
           17:('Half of a paraboloid cap',lambda u,v,w:(3*u*math.cos(math.pi/2+math.pi*v),3*u*math.sin(math.pi/2+math.pi*v),9*u*u+w*(9-9*u*u)),(3.2,3.2,9.2),'x ≤ 0; r² ≤ z ≤ 9'),
           18:('Below a cone, inside a cylinder',lambda u,v,w:(2*u*math.cos(2*math.pi*v),2*u*math.sin(2*math.pi*v),2*u*w),(2.2,2.2,2.2),'r ≤ 2; 0 ≤ z ≤ r'),
           28:('Sphere cut by an offset cylinder (a = 1)',lambda u,v,w:(u*math.cos(-math.pi/2+math.pi*v)**2,u*math.cos(-math.pi/2+math.pi*v)*math.sin(-math.pi/2+math.pi*v),(2*w-1)*math.sqrt(max(0,1-(u*math.cos(-math.pi/2+math.pi*v))**2))),(1.2,.7,1.2),'Sphere: x²+y²+z²=1; cylinder: (x-1/2)²+y²=1/4')}
    for n,(title,fn,axes,subtitle) in specs.items():
        name=f's15-7-{n}.svg';solid(name,f'15.7 / {n} · {title}',fn,axes,subtitle)
        attach(next(e for e in doc.items if e['number']==n),name,('경계식에서 생성한 입체 도해','Solid generated directly from the boundary equations'),(subtitle,subtitle))
    # Point plots are separate from surface plots to keep both labels visible.
    from plot_15 import points_plot
    for n in (1,2):
        out=[(float(rr*s.cos(tt)),float(rr*s.sin(tt)),float(zz)) for rr,tt,zz in points[n]]
        name=f's15-7-{n}.svg';points_plot(name,f'15.7 / {n} · Cylindrical points',out)
        attach(next(e for e in doc.items if e['number']==n),name,('원주좌표를 직교좌표로 변환한 두 점 a,b','Points a,b after converting cylindrical to rectangular coordinates'),('점선은 xy-평면의 사영과 높이를 나타낸다.','Dashed lines show xy-projections and vertical height.'))
figures()
from plot_15 import sphere_cylinder
sphere_cylinder('s15-7-28.svg')
for e in doc.items:
    for field in ['statement','hint','answer','check']:
        e[field]['en']=e[field]['en'].replace('radius2','radius 2').replace('radius1','radius 1').replace('at30','at 30').replace('length20','length 20').replace('radius6','radius 6').replace('radius7','radius 7').replace('radius62000','radius 62000').replace('height12400','height 12400').replace('density200','density 200')
doc.save(33)
