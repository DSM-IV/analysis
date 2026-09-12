"""All general §15.9 exercises: independently derived bilingual explanations."""
import math,html
import sympy as s
from core_15 import Doc,tex,d,m,integral,pair
from plot_15 import ASSETS,attach
u,v,w,r,t,p,q=s.symbols('u v w r theta p q',real=True)
a,b,c,k=s.symbols('a b c k',positive=True)
pi=s.pi
doc=Doc('15.9',[1154,1155],lambda n:1154 if n<=23 else 1155)
add=doc.add
trans=[(u+v,u-v),(u-v,u*v),(u*s.cos(v),u*s.sin(v)),(u-v,u+v*v),(u+v,2*v),(u*v,u**3-v**3)]
matching=['VI','I','IV','V','III','II']
reasons=[
 (r'(a) 정사각형 꼭짓점은 \((0,0),(1,1),(2,0),(1,-1)\)로 간다. 대각선이 좌표축에 평행한 마름모VI이다.',r'(a) The corners map to \((0,0),(1,1),(2,0),(1,-1)\), giving diamondVI.'),
 (r'(b) u=0 또는 v=0인 변은 y=0, u=1은 y=1-x, v=1은 y=1+x로 간다. 경계는 삼각형I이다.',r'(b) The edges u=0 or v=0 map to y=0; u=1 gives y=1-x and v=1 gives y=1+x. This is triangleI.'),
 (r'(c) u는 반지름, v는 각도이다. 0≤r≤1,0≤θ≤1 rad인 부채꼴IV이다.',r'(c) Here u is radius and v is angle:0≤r≤1,0≤θ≤1 rad, the sectorIV.'),
 (r'(d) u=0은 y=x², v=0은 y=x, u=1은 y=1+(1-x)², v=1은 y=x+2이다. 곡선 사각형V이다.',r'(d) The four edges become y=x²,y=x,y=1+(1-x)²,y=x+2, giving curved quadrilateralV.'),
 (r'(e) 꼭짓점은 \((0,0),(1,0),(2,2),(1,2)\)이다. 평행사변형III이다.',r'(e) The corners become \((0,0),(1,0),(2,2),(1,2)\), giving parallelogramIII.'),
 (r'(f) u=1은 y=1-x³, v=1은 y=x³-1이며 나머지 변은 x=0에 놓인다. 0≤x≤1인 곡선영역II이다.',r'(f) The edges u=1 and v=1 give y=1-x³ and y=x³-1; the other edges lie on x=0. This is curved regionII, with0≤x≤1.')]
add(1,('변환과 상의 모양 대응','Matching transformations to image regions'),
    (r'\(0\le u,v\le1\)인 정사각형의 상을 도해I–VI와 대응시키고 이유를 설명하라. '+d(r'\begin{aligned}(a)&\ (x,y)=(u+v,u-v)\\(b)&\ (x,y)=(u-v,uv)\\(c)&\ (x,y)=(u\cos v,u\sin v)\\(d)&\ (x,y)=(u-v,u+v^2)\\(e)&\ (x,y)=(u+v,2v)\\(f)&\ (x,y)=(uv,u^3-v^3)\end{aligned}'),
     r'Match the image of \(0\le u,v\le1\) under each map to diagramI–VI, explaining the choice. '+d(r'\begin{aligned}(a)&\ (x,y)=(u+v,u-v)\\(b)&\ (x,y)=(u-v,uv)\\(c)&\ (x,y)=(u\cos v,u\sin v)\\(d)&\ (x,y)=(u-v,u+v^2)\\(e)&\ (x,y)=(u+v,2v)\\(f)&\ (x,y)=(uv,u^3-v^3)\end{aligned}')),
    ('네 경계변의 상을 구한 뒤 꼭짓점과 곡률을 확인한다.','Map the four boundary edges, then check vertices and curvature.'),reasons,
    ('(a) VI, (b) I, (c) IV, (d) V, (e) III, (f) II.','(a) VI, (b) I, (c) IV, (d) V, (e) III, (f) II.'),
    ('각 변환의 경계 네 개를 직접 매개화하여 모든 도해의 선분·곡선과 대응시켰다.','Direct parametrization of all four edges verifies the segments and curves in each diagram.'),tuple('abcdef'))

imagecases={
2:((u+v,-v),r'0\le u\le1,\ 0\le v\le2',r'-2\le y\le0,\quad0\le x+y\le1',
   (r'v=-y, u=x+y이므로 직사각형 조건을 그대로 바꾼다. 꼭짓점은(0,0),(1,0),(3,-2),(2,-2)이다.',r'Use v=-y and u=x+y. The corner images are(0,0),(1,0),(3,-2),(2,-2).')),
3:((2*u+3*v,u-v),r'0\le u\le3,\ 0\le v\le2',r'0\le x+3y\le15,\quad0\le x-2y\le10',
   (r'역변환은 u=(x+3y)/5, v=(x-2y)/5이다. 꼭짓점은(0,0),(6,3),(12,1),(6,-2)이다.',r'The inverse is u=(x+3y)/5,v=(x-2y)/5. The corners map to(0,0),(6,3),(12,1),(6,-2).')),
4:((v,u*(1+v*v)),r'0\le u,v\le1',r'0\le x\le1,\quad0\le y\le1+x^2',
   (r'x=v로0≤x≤1이며 각 v에서 u가0부터1까지 움직이면 y는0부터1+v²까지 채운다.',r'Since x=v,0≤x≤1; varying u from0 to1 fills0≤y≤1+v² at each v.')),
5:((u*u,v),r'0\le u\le v\le1',r'0\le y\le1,\quad0\le x\le y^2',
   (r'S는 꼭짓점(0,0),(1,1),(0,1)의 삼각형이다. u≥0이므로 u=√x이고 u≤v는 √x≤y이다.',r'S is the triangle with vertices(0,0),(1,1),(0,1). Since u≥0, u=√x and u≤v becomes√x≤y.')),
6:((a*u,b*v),r'u^2+v^2\le1',r'\frac{x^2}{a^2}+\frac{y^2}{b^2}\le1',
   (r'a,b>0을 반축 길이로 두면 u=x/a,v=y/b이다. 단위원판이 타원 내부로 늘어난다.',r'For positive semiaxes a,b, the inverse is u=x/a,v=y/b, so the unit disk stretches to the filled ellipse.'))}
for n,(mapping,domain,answer,reason) in imagecases.items():
    formula=r'x='+tex(mapping[0])+r',\ y='+tex(mapping[1])
    add(n,('변환의 상 구하기','Finding the image of a region'),
      ('영역 '+m(domain)+'를 '+m(formula)+'로 보냈을 때 상을 구하라.','Find the image of '+m(domain)+' under '+m(formula)+'.'),
      ('역변환 또는 각 경계변의 매개화를 사용한다.','Use the inverse map or parametrize each boundary edge.'),[reason,('따라서 상의 부등식은 '+d(answer),'The image inequalities are '+d(answer))],d(answer),
      ('상 영역의 임의 내부점에 역변환을 적용하면 원래 영역으로 돌아가므로 경계뿐 아니라 내부도 확인된다.','An interior point of the stated image maps back into the original domain, verifying the interior as well as the boundary.'))

maps={
7:(r'y=2x-1,\ y=2x+1,\ y=1-x,\ y=3-x',r'u=y-2x,\quad v=x+y',r'x=(v-u)/3,\quad y=(u+2v)/3',r'-1\le u\le1,\quad1\le v\le3'),
8:(r'(0,0),(4,3),(2,4),(-2,1)',r'(x,y)=u(4,3)+v(-2,1)',r'x=4u-2v,\quad y=3u+v',r'0\le u,v\le1'),
9:(r'1\le x^2+y^2\le2,\quad x,y\ge0',r'u=\sqrt{x^2+y^2},\quad v=\theta',r'x=u\cos v,\quad y=u\sin v',r'1\le u\le\sqrt2,\quad0\le v\le\pi/2'),
10:(r'1\le xy\le4,\quad1\le y/x\le4,\quad x,y>0',r'u=xy,\quad v=y/x',r'x=\sqrt{u/v},\quad y=\sqrt{uv}',r'1\le u\le4,\quad1\le v\le4')}
for n,(region,choice,inverse,domain) in maps.items():
    add(n,('직사각형에서 주어진 영역으로 변환','Mapping a rectangle onto the given region'),
      ('경계 또는 꼭짓점 '+m(region)+'인 R에 대해, 축에 평행한 직사각형 S를 R로 보내는 변환을 구하라.','Find a transformation from an axis-aligned rectangle S onto R with boundaries or vertices '+m(region)+'.'),
      ('두 가족의 경계곡선에서 각각 일정한 양을 새 변수로 선택한다.','Choose quantities constant along each family of boundary curves as the new coordinates.'),
      [('다음 변수를 선택한다. '+d(choice),'Choose the new coordinates '+d(choice)),('x,y에 대해 풀면 '+d(inverse),'Solve for x,y: '+d(inverse)),('새 영역은 직사각형 '+d(domain),'The new region is the rectangle '+d(domain))],d(inverse+r',\qquad '+domain),
      ('네 변을 대입하면 원래 네 경계 또는 꼭짓점에 정확히 도달한다.','Substituting the four rectangle edges recovers the original boundaries or vertices.'))

detmaps={11:((2*u+v,4*u-v),(u,v)),12:((u*u+u*v,u*v*v),(u,v)),13:((r*s.cos(t),r*s.sin(t)),(r,t)),14:((p*s.exp(q),q*s.exp(p)),(p,q)),15:((u*v,v*w,w*u),(u,v,w)),16:((u+v*w,v+w*u,w+u*v),(u,v,w))}
for n,(f,vars) in detmaps.items():
    mat=s.Matrix(f).jacobian(vars);det=s.trigsimp(s.factor(mat.det()))
    # Exercise13 uses source variable s rather than the radial helper r.
    replacement={r:s.Symbol('s'),t:s.Symbol('t')} if n==13 else {}
    mat=mat.subs(replacement);det=det.subs(replacement);f=tuple(expr.subs(replacement) for expr in f);vars=tuple(expr.subs(replacement) for expr in vars)
    maptex=r',\quad '.join(label+'='+tex(expr) for label,expr in zip('xyz',f))
    add(n,('야코비안 행렬식','Jacobian determinant'),
        ('변환 '+m(maptex)+'의 야코비안을 구하라.','Find the Jacobian determinant of '+m(maptex)+'.'),
        ('행은 출력좌표, 열은 새 변수를 같은 순서로 둔다.','Use output coordinates as rows and new variables as columns in the stated order.'),
        [('편도함수 행렬은 '+d('D T='+tex(mat)),'The derivative matrix is '+d('D T='+tex(mat))),
         ('행렬식을 전개하고 동류항을 정리한다. '+d('J='+tex(mat)+r'\quad\Longrightarrow\quad\det(DT)='+tex(det)),'Expand the determinant and collect terms. '+d('J='+tex(mat)+r'\quad\Longrightarrow\quad\det(DT)='+tex(det)))],d('J='+tex(det)),
        ('기호 미분으로 행렬을 구성한 뒤 행렬식을 독립 계산했다. 적분의 면적·부피요소에는 이 값의 절댓값을 사용한다.','The matrix was formed by symbolic differentiation and its determinant computed independently. Use the absolute value for an integration area or volume element.'))
    doc.checks.append({'number':n,'matrix':str(mat),'determinant':str(det)})

def calc(n,statement,f,lims,setup,parts=()):return doc.calc(n,statement,f,lims,setup,parts,topic=('변수변환으로 이중적분','Double integration by change of variables'))
calc(17,(r'꼭짓점(0,0),(2,1),(1,2)의 삼각형에서 \(\iint_R(x-3y)dA\)를 \(x=2u+v,y=u+2v\)로 계산하라.',r'Evaluate \(\iint_R(x-3y)dA\) on the triangle(0,0),(2,1),(1,2), using \(x=2u+v,y=u+2v\).'),3*(-u-5*v),[(v,0,1-u),(u,0,1)],(r'새 꼭짓점은(0,0),(1,0),(0,1)이다. \(|J|=3\), \(x-3y=-u-5v\).',r'The transformed vertices are(0,0),(1,0),(0,1). Here \(|J|=3\), and \(x-3y=-u-5v\).'))
calc(18,(r'꼭짓점(-1,3),(1,-3),(3,-1),(1,5)의 평행사변형에서 \(\iint_R(4x+8y)dA\)를 \(x=(u+v)/4,y=(v-3u)/4\)로 계산하라.',r'Evaluate \(\iint_R(4x+8y)dA\) over the parallelogram(-1,3),(1,-3),(3,-1),(1,5), using \(x=(u+v)/4,y=(v-3u)/4\).'),(-5*u+3*v)/4,[(u,-4,4),(v,0,8)],(r'역변환은 u=x-y,v=3x+y이다. 새 영역은[-4,4]×[0,8], \(|J|=1/4\), 피적분함수는-5u+3v이다.',r'The inverse is u=x-y,v=3x+y. The new rectangle is[-4,4]×[0,8], with \(|J|=1/4\) and integrand-5u+3v.'))
calc(19,(r'타원 \(9x^2+4y^2\le36\)에서 \(\iint x^2dA\)를 \(x=2u,y=3v\)로 계산하라.',r'Evaluate \(\iint x^2dA\) on \(9x^2+4y^2\le36\), using \(x=2u,y=3v\).'),24*r**3*s.cos(t)**2,[(r,0,1),(t,0,2*pi)],(r'타원은 단위원판u²+v²≤1이 된다. 첫 야코비안은6이며 u=r cosθ,v=r sinθ로 다시 바꾸면 r이 추가된다.',r'The ellipse becomes the unit disku²+v²≤1. The first Jacobian is6; the polar substitution u=r cosθ,v=r sinθ contributes another r.'))
calc(20,(r'\(x^2-xy+y^2\le2\)에서 \(\iint(x^2-xy+y^2)dA\)를 \(x=\sqrt2u-\sqrt{2/3}v,y=\sqrt2u+\sqrt{2/3}v\)로 계산하라.',r'Evaluate \(\iint(x^2-xy+y^2)dA\) on \(x^2-xy+y^2\le2\), using \(x=\sqrt2u-\sqrt{2/3}v,y=\sqrt2u+\sqrt{2/3}v\).'),8*r**3/s.sqrt(3),[(r,0,1),(t,0,2*pi)],(r'이차식은2(u²+v²), \(|J|=4/\sqrt3\)이다. 단위원판에서 극좌표를 쓰면 피적분함수는 \(8r^3/\sqrt3\)이다.',r'The quadratic becomes2(u²+v²), with \(|J|=4/\sqrt3\). Polar coordinates in the unit disk give transformed integrand \(8r^3/\sqrt3\).'))
calc(21,(r'제1사분면의 y=x,y=3x,xy=1,xy=3 경계에서 \(\iint_Rxy\,dA\)를 \(x=u/v,y=v\)로 계산하라.',r'Evaluate \(\iint_Rxy\,dA\) in the first-quadrant region bounded by y=x,y=3x,xy=1,xy=3, using \(x=u/v,y=v\).'),u/v,[(v,s.sqrt(u),s.sqrt(3*u)),(u,1,3)],(r'u=xy이므로1≤u≤3이다. y/x=v²/u가1에서3이므로√u≤v≤√(3u). \(|J|=1/v\)이다.',r'Since u=xy,1≤u≤3. The ratio y/x=v²/u lies between1 and3, so√u≤v≤√(3u). The absolute Jacobian is1/v.'))
calc(22,(r'xy=1,xy=2,xy²=1,xy²=2로 둘러싸인 R에서 \(\iint_R y^2dA\)를 \(u=xy,v=xy^2\)로 계산하고 R을 그래프로 그려라.',r'Evaluate \(\iint_Ry^2dA\) for the region bounded by xy=1,xy=2,xy²=1,xy²=2, using \(u=xy,v=xy^2\); graph R.'),v/u**2,[(u,1,2),(v,1,2)],(r'역변환은 y=v/u,x=u²/v이며 \(|J|=1/v\). 새 영역은[1,2]²이고 y²|J|=v/u²이다.',r'The inverse is y=v/u,x=u²/v, with \(|J|=1/v\). The new region is[1,2]² and y²|J|=v/u².'))

earth=s.Rational(4,3)*pi*6378**2*6356
add(23,('타원체의 부피와 관성모멘트','Volume and inertia of an ellipsoid'),
    (r'(a) \(x^2/a^2+y^2/b^2+z^2/c^2\le1\)의 부피를 \(x=au,y=bv,z=cw\)로 구하라. (b) a=b=6378 km,c=6356 km로 지구 부피를 추정하라. (c) 일정 밀도k에서 z축 관성모멘트를 구하라.',r'(a) Find the ellipsoid volume for \(x^2/a^2+y^2/b^2+z^2/c^2\le1\) using \(x=au,y=bv,z=cw\). (b) Estimate Earth’s volume for a=b=6378 km,c=6356 km. (c) Find z-axis inertia for constant densityk.'),
    ('세 반축을 나누어 단위구로 보낸다.','Scale the three semiaxes to the unit ball.'),
    [(r'(a) 새 영역은u²+v²+w²≤1이고 \(|J|=abc\)이다. '+d(r'V=abc\iiint_Bdu\,dv\,dw=\frac{4\pi abc}{3}'),r'(a) The new region isu²+v²+w²≤1 and \(|J|=abc\). '+d(r'V=abc\iiint_Bdu\,dv\,dw=\frac{4\pi abc}{3}')),
     ('(b) 주어진 반축 값을 대입하면 '+d('V='+tex(earth)+r'\ \mathrm{km}^3\approx '+tex(s.N(earth,12))+r'\ \mathrm{km}^3'),'(b) Substitute the given semiaxes: '+d('V='+tex(earth)+r'\ \mathrm{km}^3\approx '+tex(s.N(earth,12))+r'\ \mathrm{km}^3')),
     (r'(c) '+d(r'I_z=kabc\iiint_B(a^2u^2+b^2v^2)du\,dv\,dw'),r'(c) '+d(r'I_z=kabc\iiint_B(a^2u^2+b^2v^2)du\,dv\,dw')),
     (r'단위구의 대칭과 \(\int_B(u^2+v^2+w^2)dV=4\pi/5\)에서 각 제곱항 적분은4π/15이다.',r'By unit-ball symmetry and \(\int_B(u^2+v^2+w^2)dV=4\pi/5\), each squared-coordinate integral is4π/15.')],
    (r'(a) \(V=4\pi abc/3\). (b) '+m(tex(s.N(earth,12))+r'\ \mathrm{km}^3')+r'. (c) \(I_z=4\pi kabc(a^2+b^2)/15=M(a^2+b^2)/5\).',r'(a) \(V=4\pi abc/3\). (b) '+m(tex(s.N(earth,12))+r'\ \mathrm{km}^3')+r'. (c) \(I_z=4\pi kabc(a^2+b^2)/15=M(a^2+b^2)/5\).'),
    ('a=b=c이면 구의 부피와2Ma²/5 관성 공식으로 줄어든다.','Setting a=b=c recovers the sphere volume and inertia2Ma²/5.'),('a','b','c'))
add(24,('카르노 사이클의 일','Work of a Carnot cycle'),
    (r'양의 압력·부피 평면에서 xy=a,xy=b,xy^{1.4}=c,xy^{1.4}=d 사이 영역의 넓이로 일을 구하라. 0<a<b,0<c<d이다.',r'In the positive pressure-volume plane, find the work as the area bounded by xy=a,xy=b,xy^{1.4}=c,xy^{1.4}=d, where0<a<b and0<c<d.'),
    ('각 곡선에서 일정한 양을 u,v로 택한다.','Choose the quantities constant on the boundary curves as u,v.'),
    [(r'\(u=xy,v=xy^{7/5}\)이면 새 영역은[a,b]×[c,d]이다. 양의 사분면에서 \(y=(v/u)^{5/2},x=u^{7/2}/v^{5/2}\).',r'With \(u=xy,v=xy^{7/5}\), the new rectangle is[a,b]×[c,d]. In the positive quadrant, \(y=(v/u)^{5/2},x=u^{7/2}/v^{5/2}\).'),
     (r'순방향 행렬식은 \(\partial(u,v)/\partial(x,y)=\frac25xy^{7/5}=2v/5\), 따라서 역변환의 절댓값은5/(2v)이다.',r'The forward determinant is \(\partial(u,v)/\partial(x,y)=\frac25xy^{7/5}=2v/5\), so the inverse absolute Jacobian is5/(2v).'),
     (r'면적, 곧 일은 '+d(r'W=\int_a^b\int_c^d\frac5{2v}\,dv\,du=\frac52(b-a)\ln(d/c)'),r'The area, and hence work, is '+d(r'W=\int_a^b\int_c^d\frac5{2v}\,dv\,du=\frac52(b-a)\ln(d/c)'))],d(r'W=\frac52(b-a)\ln\frac dc'),
    ('두 인자가 양수이므로 일은 양수이며 d→c 또는 b→a에서0으로 수렴한다.','Both factors are positive; the work tends to zero as d→c or b→a.'))
calc(25,(r'x-2y=0,4 및3x-y=1,8로 둘러싸인 평행사변형에서 \(\iint_R\frac{x-2y}{3x-y}dA\)를 구하라.',r'Evaluate \(\iint_R\frac{x-2y}{3x-y}dA\) on the parallelogram bounded by x-2y=0,4 and3x-y=1,8.'),u/(5*v),[(u,0,4),(v,1,8)],(r'u=x-2y,v=3x-y이면 x=(2v-u)/5,y=(v-3u)/5, \(|J|=1/5\). 분모는v≥1이므로 특이점이 없다.',r'Let u=x-2y,v=3x-y. Then x=(2v-u)/5,y=(v-3u)/5, with \(|J|=1/5\). Since v≥1, the denominator has no singularity.'))
calc(26,(r'x-y=0,2 및x+y=0,3으로 둘러싸인 직사각형에서 \(\iint_R(x+y)e^{x^2-y^2}dA\)를 구하라.',r'Evaluate \(\iint_R(x+y)e^{x^2-y^2}dA\) in the rectangle bounded by x-y=0,2 andx+y=0,3.'),v*s.exp(u*v)/2,[(u,0,2),(v,0,3)],(r'u=x-y,v=x+y이면 x=(u+v)/2,y=(v-u)/2, \(|J|=1/2\). 지수는uv이고 앞의 인자는v이다.',r'Set u=x-y,v=x+y, so x=(u+v)/2,y=(v-u)/2 and \(|J|=1/2\). The exponent isuv and the leading factor isv.'))
calc(27,(r'꼭짓점(1,0),(2,0),(0,2),(0,1)의 사다리꼴에서 \(\iint_R\cos\frac{y-x}{y+x}dA\)를 구하라.',r'Evaluate \(\iint_R\cos\frac{y-x}{y+x}dA\) over the trapezoid(1,0),(2,0),(0,2),(0,1).'),u*s.cos(v)/2,[(v,-1,1),(u,1,2)],(r'u=x+y,v=(y-x)/(y+x)이면1≤u≤2,-1≤v≤1이다. 역변환 x=u(1-v)/2,y=u(1+v)/2의 \(|J|=u/2\).',r'Use u=x+y,v=(y-x)/(y+x), giving1≤u≤2,-1≤v≤1. The inverse x=u(1-v)/2,y=u(1+v)/2 has \(|J|=u/2\).'))
calc(28,(r'제1사분면의 \(9x^2+4y^2\le1\)에서 \(\iint\sin(9x^2+4y^2)dA\)를 구하라.',r'Evaluate \(\iint\sin(9x^2+4y^2)dA\) in the first-quadrant part of \(9x^2+4y^2\le1\).'),r*s.sin(r*r)/6,[(r,0,1),(t,0,pi/2)],(r'u=3x,v=2y로 단위원판의 사분면이 되며 첫 야코비안은1/6이다. u=r cosθ,v=r sinθ로 바꾸면 지수 내부는r²이다.',r'Let u=3x,v=2y to obtain the quarter unit disk, with first Jacobian1/6. Then u=r cosθ,v=r sinθ makes the sine argument r².'))
calc(29,(r'\(|x|+|y|\le1\)인 마름모에서 \(\iint e^{x+y}dA\)를 구하라.',r'Evaluate \(\iint e^{x+y}dA\) on the diamond \(|x|+|y|\le1\).'),s.exp(u)/2,[(v,-1,1),(u,-1,1)],(r'u=x+y,v=x-y로 놓으면 \(|x|+|y|=\max(|u|,|v|)\)이다. 따라서[-1,1]²이며 \(|J|=1/2\).',r'With u=x+y,v=x-y, the identity \(|x|+|y|=\max(|u|,|v|)\) gives[-1,1]², and \(|J|=1/2\).'))
calc(30,(r'x+y=1,3 및y=2x,y=x/2로 둘러싸인 영역에서 \(\iint_R(y/x)dA\)를 구하라.',r'Evaluate \(\iint_R(y/x)dA\) on the region bounded by x+y=1,3 andy=2x,y=x/2.'),u*v/(1+v)**2,[(v,s.Rational(1,2),2),(u,1,3)],(r'u=x+y,v=y/x로1≤u≤3,1/2≤v≤2이다. x=u/(1+v),y=uv/(1+v), \(|J|=u/(1+v)^2\).',r'Set u=x+y,v=y/x, giving1≤u≤3,1/2≤v≤2. The inverse is x=u/(1+v),y=uv/(1+v), with \(|J|=u/(1+v)^2\).'))
add(31,('합에 의존하는 함수의 적분','Integrating a function of the coordinate sum'),
    (r'f가[0,1]에서 연속이고 R은(0,0),(1,0),(0,1)의 삼각형일 때 \(\iint_Rf(x+y)dA=\int_0^1uf(u)du\)를 보여라.',r'For f continuous on[0,1] and R the triangle(0,0),(1,0),(0,1), prove \(\iint_Rf(x+y)dA=\int_0^1uf(u)du\).'),
    ('함수의 입력 x+y 자체를 새 변수로 둔다.','Use the argument x+y as a new variable.'),
    [(r'u=x+y,v=x이면 역변환 x=v,y=u-v이며 \(|J|=1\)이다.',r'Let u=x+y,v=x. Then x=v,y=u-v and \(|J|=1\).'),
     (r'삼각형의 조건은0≤v≤u≤1로 바뀐다. 따라서 '+d(r'\iint_Rf(x+y)dA=\int_0^1\int_0^uf(u)\,dv\,du'),r'The triangle becomes0≤v≤u≤1, so '+d(r'\iint_Rf(x+y)dA=\int_0^1\int_0^uf(u)\,dv\,du')),
     (r'f(u)는 v에 무관하므로 안쪽 적분은 u f(u)이다.',r'Since f(u) is independent of v, the inner integral equalsu f(u).')],d(r'\iint_Rf(x+y)dA=\int_0^1uf(u)du'),
    ('f≡1이면 양변은 삼각형 넓이1/2이다. 연속성으로 적분과 변수변환의 가정이 충족된다.','For f≡1 both sides give triangle area1/2. Continuity supplies the integrability needed for the change of variables.'))

def figures():
    outline=[]
    for fn in trans:
        lamb=s.lambdify((u,v),fn,'math')
        pts=[]
        for side in range(4):
            for j in range(41):
                s0=j/40
                uv=[(s0,0),(1,s0),(1-s0,1),(0,1-s0)][side]
                pts.append(lamb(*uv))
        outline.append(pts)
    order=[1,5,4,2,3,0]
    out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 570" role="img"><title>Six image regions for Exercise15.9.1</title><rect width="900" height="570" fill="#fbfcff"/><text x="26" y="32" font-size="21" font-family="sans-serif">15.9 / 1 · Image regions I–VI</text>']
    for j,(roman,idx) in enumerate(zip(['I','II','III','IV','V','VI'],order)):
        left=25+(j%3)*295;top=55+(j//3)*250
        pts=outline[idx];lowx=min(q[0] for q in pts);hix=max(q[0] for q in pts);lowy=min(q[1] for q in pts);hiy=max(q[1] for q in pts)
        sc=min(190/max(hix-lowx,1),155/max(hiy-lowy,1))
        def xy(x,y):return (left+135+sc*(x-(lowx+hix)/2),top+120-sc*(y-(lowy+hiy)/2))
        coords=' '.join(f'{a:.2f},{b:.2f}' for a,b in [xy(*pt) for pt in pts])
        out.append(f'<rect x="{left}" y="{top}" width="270" height="230" rx="8" fill="#fff" stroke="#d8e0ee"/><text x="{left+13}" y="{top+24}" font-size="19" font-family="sans-serif">{roman}</text><polygon points="{coords}" fill="#c9dcf4" stroke="#2f65a8" stroke-width="1.7"/>')
        axis0=xy(0,0);xr=xy(hix+.22,0);xl=xy(lowx-.16,0);yt=xy(0,hiy+.15);yb=xy(0,lowy-.15)
        out.append(f'<path d="M{xl[0]},{xl[1]}L{xr[0]},{xr[1]}M{yb[0]},{yb[1]}L{yt[0]},{yt[1]}" stroke="#67758a" stroke-width=".9"/><text x="{xr[0]+3}" y="{xr[1]-3}" font-family="sans-serif" font-size="12">x</text><text x="{yt[0]+3}" y="{yt[1]-3}" font-family="sans-serif" font-size="12">y</text>')
        for tick in range(math.ceil(lowx),math.floor(hix)+1):
            loc=xy(tick,0);out.append(f'<text x="{loc[0]-4}" y="{loc[1]+15}" font-family="sans-serif" font-size="11">{tick}</text>')
        for tick in range(math.ceil(lowy),math.floor(hiy)+1):
            if tick==0:continue
            loc=xy(0,tick);out.append(f'<text x="{loc[0]-16}" y="{loc[1]+4}" font-family="sans-serif" font-size="11">{tick}</text>')
    out.append('</svg>');name='s15-9-1.svg';(ASSETS/name).write_text('\n'.join(out))
    attach(doc.items[0],name,('정사각형의 여섯 변환 상 I–VI를 직접 재구성한 비교 도해','Original reconstruction of the six transformed-square images I–VI'),('경계곡선을 변환식에서 계산해 원래 도형 라벨을 보존했다.','Boundary curves are computed from the maps, preserving the original diagram labels.'))
    def xy(x,y):return (70+100*x,325-130*y)
    pts=[]
    for side in range(4):
        for j in range(65):
            a0=j/64
            uu,vv=[(1+a0,1),(2,1+a0),(2-a0,2),(1,2-a0)][side]
            pts.append((uu*uu/vv,vv/uu))
    coords=' '.join(f'{a0:.2f},{b0:.2f}' for a0,b0 in map(lambda p:xy(*p),pts))
    out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 610 440" role="img"><title>15.9.22 region under the inverse transformation</title><rect width="610" height="440" fill="#fbfcff"/><text x="25" y="31" font-family="sans-serif" font-size="20">15.9 / 22 · Curvilinear region R</text>',f'<polygon points="{coords}" fill="#c9dcf4" stroke="#2e649f" stroke-width="2"/>','<path d="M55,325H510M70,340V42" fill="none" stroke="#3b4c65"/><text x="520" y="330" font-family="sans-serif">x</text><text x="57" y="48" font-family="sans-serif">y</text>']
    for i in range(5):
        a0,b0=xy(i,0);out.append(f'<text x="{a0-3}" y="{b0+19}" font-family="sans-serif" font-size="12">{i}</text>')
    for i in (1,2):
        a0,b0=xy(0,i);out.append(f'<text x="{a0-18}" y="{b0+4}" font-family="sans-serif" font-size="12">{i}</text>')
    for pt,label,dx,dy in [((1,1),'(1,1)',-35,17),((4,.5),'(4,1/2)',6,4),((2,1),'(2,1)',8,-7),((.5,2),'(1/2,2)',8,-8)]:
        a0,b0=xy(*pt);out.append(f'<circle cx="{a0}" cy="{b0}" r="3" fill="#224e87"/><text x="{a0+dx}" y="{b0+dy}" font-family="sans-serif" font-size="12">{label}</text>')
    out+=['<text x="25" y="385" font-family="sans-serif" font-size="14">Boundaries: xy = 1, xy = 2, xy² = 1, xy² = 2</text>','<text x="25" y="413" font-family="sans-serif" font-size="14">Inverse map: x = u²/v, y = v/u; 1 ≤ u,v ≤ 2</text>','</svg>']
    name='s15-9-22.svg';(ASSETS/name).write_text('\n'.join(out))
    attach(next(e for e in doc.items if e['number']==22),name,('네 곡선 xy=1,2와 xy²=1,2로 둘러싸인 제1사분면 영역','First-quadrant region bounded by xy=1,2 and xy²=1,2'),('꼭짓점과 경계는 역변환에서 직접 계산했다.','Vertices and boundary curves are computed directly from the inverse map.'))
figures();doc.save(31)
