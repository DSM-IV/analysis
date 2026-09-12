"""Source-checked, original worked solutions for Stewart ET 9e §15.6."""
import json
from pathlib import Path
import sympy as S
x,y,z,r,t=S.symbols('x y z r theta', real=True)
a,b,c,k,L,M=S.symbols('a b c k L M', positive=True)
pi=S.pi
ROOT=Path(__file__).resolve().parents[1]
items=[]; checks=[]
def tex(v): return S.latex(v)
def math(v): return r'\('+v+r'\)'
def disp(v): return r'\['+v+r'\]'
def pair(ko,en): return {'ko':ko,'en':en}
def integral(f,lims):
    return ''.join(r'\int_{'+tex(lo)+'}^{'+tex(hi)+'}' for v,lo,hi in reversed(lims))+r'\left('+ (f if isinstance(f,str) else tex(f))+r'\right)\,'+r'\,'.join('d'+tex(v) for v,lo,hi in lims)
def add(n,topic,statement,hint,steps,answer,check,parts=()):
    p=1130 if n<=10 else 1131 if n<=36 else 1132
    items.append({'id':f'stewart9-exercise-15.6-{n}','number':n,'subparts':list(parts),
      'source':{'printedPage':p,'pdfPage':p+37},'topic':pair(*topic),'statement':pair(*statement),
      'hint':pair(*hint),'steps':{'ko':[s[0] for s in steps],'en':[s[1] for s in steps]},
      'answer':pair(*answer) if isinstance(answer,tuple) else pair(answer,answer),'check':pair(*check),
      'conceptHref':'../s15-6.html','status':'math-verified'})
def calc(n,f,lims,region=None,note=None,parts=(),task=None):
    f=S.sympify(f); cur=f; steps=[]
    expression=integral(f,lims)
    if region:
        statement=(r'영역 \(E\): '+region+rf'. \(\iiint_E {tex(f)}\,dV\)를 계산하라.',
                   r'Region \(E\): '+region+rf'. Evaluate \(\iiint_E {tex(f)}\,dV\).')
        steps.append(('경계의 대소관계를 확인하고 다음 순서로 쓴다. '+disp(expression),
                      'The boundary inequalities give the following integration order. '+disp(expression)))
    else: statement=('반복적분을 계산하라. '+disp(expression),'Evaluate the iterated integral. '+disp(expression))
    if task: statement=task
    for v,lo,hi in lims:
        anti=S.integrate(cur,v)
        nxt=S.simplify(S.integrate(cur,(v,lo,hi)))
        assert not nxt.has(S.Integral), (n, v, nxt)
        if not anti.has(S.Integral):
            assert S.simplify(S.diff(anti,v)-cur)==0,(n,v,'antiderivative')
        eq=integral(cur,[(v,lo,hi)])+'='+tex(nxt)
        steps.append((math(tex(v))+'에 대해 적분하고 양 끝값을 대입한다. '+disp(eq),
                      'Integrate with respect to '+math(tex(v))+' and apply the limits. '+disp(eq)))
        cur=nxt
    if note: steps.insert(0,note)
    add(n,('삼중적분 계산','Evaluating a triple integral'),statement,
        ('안쪽 변수의 적분에서는 나머지 변수를 상수로 두고, 사영 영역의 경계를 유지한다.',
         'Hold the other variables fixed in the inner integral and preserve the projection bounds.'),steps,disp('I='+tex(cur)),
        ('각 단계의 원시함수를 미분하여 피적분함수를 복원하고 경계 대입을 기호 계산으로 확인했다.',
         'Differentiating each available antiderivative recovers its integrand; symbolic endpoint evaluation checks every stage.'),parts)
    checks.append({'number':n,'integrand':str(f),'limits':[[str(q) for q in li] for li in lims],'result':str(cur),'method':'antiderivative differentiation and endpoint substitution'})
    return cur

calc(1,x*y*z**2,[(y,-1,2),(z,0,3),(x,0,1)],
     task=(r'Example 1의 \(B=[0,1]\times[-1,2]\times[0,3]\), \(f=xyz^2\)에 대해 \(y\), \(z\), \(x\) 순서로 적분하라.',
           r'For the box \(B=[0,1]\times[-1,2]\times[0,3]\) and \(f=xyz^2\) from Example 1, integrate in the order \(y\), then \(z\), then \(x\).'))
calc(2,x*y+z**2,[(z,0,3),(y,0,1),(x,0,2)],r'\(0\le x\le2,\ 0\le y\le1,\ 0\le z\le3\)')
items[-1]['statement']['ko']+=' 서로 다른 세 적분 순서로 확인하라.'
items[-1]['statement']['en']+=' Verify the value using three different orders.'
for lang in ['ko','en']:
    items[-1]['steps'][lang].append(('다른 두 순서도 같은 직육면체를 나타낸다. ' if lang=='ko' else 'Two other orders describe the same box. ')+disp(integral(x*y+z**2,[(x,0,2),(z,0,3),(y,0,1)])+'='+integral(x*y+z**2,[(y,0,1),(x,0,2),(z,0,3)])+'=21'))
calc(3,2*x-y,[(x,0,y-z),(y,0,z**2),(z,0,2)])
calc(4,6*x*y,[(z,0,x+y),(x,y,2*y),(y,0,1)])
calc(5,x*S.exp(-y),[(y,0,S.log(x)),(x,0,2*z),(z,1,2)],note=(r'\(x=0\)에서 \(\ln x\)는 정의되지 않으므로 안쪽 적분은 \(x>0\)에서 계산한 뒤 끝점 극한으로 해석한다. 결과 \(x-1\)은 0까지 연속적으로 연장된다.',r'Because \(\ln x\) is undefined at \(x=0\), first evaluate for \(x>0\) and interpret the endpoint as a limit. The resulting \(x-1\) extends continuously to zero.'))
calc(6,S.cos(x-2*y+z),[(y,0,x+z),(z,0,2*x),(x,0,pi/2)])
calc(7,z/y,[(x,-y,z),(z,-1,2),(y,1,3)])
calc(8,x*y*S.exp(z),[(z,0,2-x**2-y**2),(y,0,1),(x,0,1)])
calc(9,x,[(y,0,2-z),(z,0,1-x**2),(x,0,1)],r'\(x,y,z\ge0,\ z\le1-x^2,\ y+z\le2\)',parts=('a','b'))
calc(10,x*y,[(z,0,4-y**2),(x,0,y),(y,0,2)],r'\(0\le x\le y,\ 0\le y\le2,\ 0\le z\le4-y^2\)',parts=('a','b'))
calc(11,x+y,[(y,0,x**2),(z,0,2-x),(x,0,2)],r'\(0\le x\le2,\ 0\le y\le x^2,\ 0\le z\le2-x\)',parts=('a','b'))
calc(12,2,[(x,z-4,4-z),(y,-S.sqrt(4-z),S.sqrt(4-z)),(z,0,4)],r'\(0\le z\le4,\ z-4\le x\le4-z,\ -\sqrt{4-z}\le y\le\sqrt{4-z}\)',parts=('a','b'))
for n in range(9,13):
    e=next(q for q in items if q['number']==n)
    e['statement']['ko']='그림의 입체를 다음 경계로 재서술한다. '+e['statement']['ko']+' (a) 반복적분을 세우고 (b) 값을 구하라.'
    e['statement']['en']='The pictured solid has the following boundary description. '+e['statement']['en']+' (a) Set up an iterated integral and (b) evaluate it.'
calc(13,y,[(z,x-y,x+y),(y,0,x),(x,0,3)],r'\(0\le x\le3,\ 0\le y\le x,\ x-y\le z\le x+y\)')
calc(14,S.exp(z/y),[(z,0,x*y),(x,y,1),(y,0,1)],r'\(0\le y\le1,\ y\le x\le1,\ 0\le z\le xy\)',note=(r'\(y=0\)인 경계에서는 식이 정의되지 않지만 이 경계는 부피 0이다. \(y>0\)에서 계산하며 \(0\le z/y\le x\le1\)이므로 적분함수는 유계이다.',r'The formula is undefined on the zero-volume boundary \(y=0\). Calculate for \(y>0\); since \(0\le z/y\le x\le1\), the integrand is bounded.'))
calc(15,x**-3,[(x,1,z+1),(z,0,y**2),(y,0,1)],r'\(0\le y\le1,\ 0\le z\le y^2,\ 1\le x\le z+1\)')
calc(16,S.sin(y),[(z,0,x),(x,0,pi-y),(y,0,pi)],r'\(x,y\ge0,\ x+y\le\pi,\ 0\le z\le x\)')
calc(17,6*x*y,[(z,0,1+x+y),(y,0,S.sqrt(x)),(x,0,1)],r'\(0\le x\le1,\ 0\le y\le\sqrt{x},\ 0\le z\le1+x+y\)')
calc(18,x-y,[(z,x**2-1,1-x**2),(y,0,2),(x,-1,1)],r'\(-1\le x\le1,\ 0\le y\le2,\ x^2-1\le z\le1-x^2\)')
calc(19,y**2,[(z,0,2-x-y),(y,0,2-x),(x,0,2)],r'\(x,y,z\ge0,\ x+y+z\le2\)')
calc(20,x*z,[(x,0,z-y),(y,0,z),(z,0,1)],r'\(x,y\ge0,\ x+y\le z\le1\)',note=(r'頂点 \((0,0,0),(1,0,1),(0,1,1),(0,0,1)\)を結ぶ斜面は \(z=x+y\) である。'.replace('頂点','꼭짓점').replace('を結ぶ斜面は','을 잇는 경사면은').replace('である。','이다.'),r'The sloping face through \((0,0,0),(1,0,1),(0,1,1)\) is \(z=x+y\); the fourth vertex is \((0,0,1)\).'))
calc(21,x*r,[(x,4*r**2,4),(r,0,1),(t,0,2*pi)],r'\(4y^2+4z^2\le x\le4\)',note=(r'\(yz\)-평면에서 \(y=r\cos\theta,z=r\sin\theta\)로 두면 \(dV=r\,dx\,dr\,d\theta\)이다. 아래 피적분함수는 야코비안까지 포함한다.',r'Use polar coordinates in the \(yz\)-plane: \(y=r\cos\theta,z=r\sin\theta\), so \(dV=r\,dx\,dr\,d\theta\). The integrand below includes the Jacobian.'))
items[-1]['statement']=pair(r'\(4y^2+4z^2\le x\le4\)인 입체에서 \(\iiint_E x\,dV\)를 구하라.',r'Evaluate \(\iiint_E x\,dV\) over \(4y^2+4z^2\le x\le4\).')
calc(22,z,[(x,0,y/3),(z,0,S.sqrt(9-y**2)),(y,0,3)],r'\(x,y,z\ge0,\ y^2+z^2\le9,\ 0\le x\le y/3\)')
calc(23,1,[(z,0,4-2*x-y),(y,0,4-2*x),(x,0,2)],r'\(x,y,z\ge0,\ 2x+y+z\le4\)')
calc(24,r,[(y,r**2,8-r**2),(r,0,2),(t,0,2*pi)],r'\(x^2+z^2\le y\le8-x^2-z^2\)',note=(r'\(xz\)-평면에 극좌표를 쓰면 교선은 \(r=2\), 높이는 \(8-2r^2\)이다. 야코비안 \(r\)을 곱한다.',r'Polar coordinates in the \(xz\)-plane give intersection radius \(r=2\) and thickness \(8-2r^2\). Include the Jacobian \(r\).'))
calc(25,1,[(z,0,1-y),(y,x**2,1),(x,-1,1)],r'\(x^2\le y\le1,\ 0\le z\le1-y\)')
calc(26,1,[(y,-1,4-z),(x,-S.sqrt(4-z**2),S.sqrt(4-z**2)),(z,-2,2)],r'\(x^2+z^2\le4,\ -1\le y\le4-z\)')
calc(27,1,[(x,y,1),(z,0,S.sqrt(1-y**2)),(y,0,1)],r'\(0\le y\le x\le1,\ 0\le z,\ y^2+z^2\le1\)',parts=('a','b'))
for n in range(23,28):
    e=next(q for q in items if q['number']==n)
    e['topic']=pair('입체의 부피','Volume of a solid')
    if n==24: e['statement']=pair(r'\(y=x^2+z^2\), \(y=8-x^2-z^2\) 사이 입체의 부피를 삼중적분으로 구하라.',r'Use a triple integral to find the volume between \(y=x^2+z^2\) and \(y=8-x^2-z^2\).')
    else:
        e['statement']['ko']+=' 이 적분은 입체의 부피이다.'
        e['statement']['en']+=' This integral gives the volume of the solid.'

for n,fun,axes,dv in [(28,S.sqrt(x*x+y*y+z*z),[[1,3]]*3,8),
                     (29,S.cos(x*y*z),[[S.Rational(1,4),S.Rational(3,4)]]*3,S.Rational(1,8)),
                     (30,S.sqrt(x)*S.exp(x*y*z),[[1,3],[S.Rational(1,4),S.Rational(3,4)],[S.Rational(1,2),S.Rational(3,2)]],1)]:
    import itertools
    vals=[fun.subs({x:p[0],y:p[1],z:p[2]}) for p in itertools.product(*axes)]
    ans=S.simplify(dv*sum(vals))
    boxes={28:r'[0,4]^3',29:r'[0,1]^3',30:r'[0,4]\times[0,1]\times[0,2]'}
    coords=r',\quad '.join(tex(v)+r'\in\{'+','.join(tex(i) for i in ax)+r'\}' for v,ax in zip((x,y,z),axes))
    add(n,('삼중적분의 중점법','Midpoint rule in three dimensions'),
        (rf'\(B={boxes[n]}\)에서 \(f={tex(fun)}\)의 적분을 같은 크기 부분상자 8개의 중점법으로 근사하라.',rf'Estimate the integral of \(f={tex(fun)}\) on \(B={boxes[n]}\) using eight equal sub-boxes and their midpoints.'),
        ('각 축을 두 등분하고 중점 좌표의 모든 조합을 사용한다.','Bisect every coordinate interval and use all combinations of midpoint coordinates.'),
        [(r'중점 좌표는 '+disp(coords),'The midpoint coordinates are '+disp(coords)),
         (r'부분상자 부피는 '+math(r'\Delta V='+tex(dv))+r'이다. '+disp('Q='+tex(dv)+r'\left('+ '+'.join(tex(q) for q in vals)+r'\right)'),r'Each sub-box has volume '+math(r'\Delta V='+tex(dv))+'. '+disp('Q='+tex(dv)+r'\left('+ '+'.join(tex(q) for q in vals)+r'\right)')),
         ('8개 기여를 합하고 마지막에 반올림한다. '+disp(r'Q\approx '+str(S.N(ans,12))), 'Sum all eight contributions before rounding. '+disp(r'Q\approx '+str(S.N(ans,12))))],
        disp(r'Q\approx '+str(S.N(ans,12))),
        ('8개 중점의 중복·누락이 없고, 8배의 부분상자 부피가 전체 부피와 일치한다. 이는 정확한 적분값이 아니라 중점 근사이다.',
         'There are eight distinct midpoint triples and eight sub-box volumes sum to the box volume. This is a midpoint approximation, not the exact integral.'))
    checks.append({'number':n,'midpointValues':[str(q) for q in vals],'subboxVolume':str(dv),'approximation':str(S.N(ans,15))})

add(31,('적분 경계에서 입체 복원','Reconstructing a solid from its bounds'),
    (r'\(\int_0^1\int_0^{1-x}\int_0^{2-2z}dy\,dz\,dx\)의 부피 영역을 그려라.',r'Sketch the solid whose volume is \(\int_0^1\int_0^{1-x}\int_0^{2-2z}dy\,dz\,dx\).'),
    ('높이 z를 고정한 단면을 직사각형으로 읽는다.','Read the horizontal cross-section as a rectangle.'),
    [(r'부등식은 \(x,y,z\ge0,\ x+z\le1,\ y+2z\le2\)이다.',r'The inequalities are \(x,y,z\ge0,\ x+z\le1,\ y+2z\le2\).'),
     (r'\(z\) 단면은 \([0,1-z]\times[0,2(1-z)]\)이며 \(z=1\)에서 한 점으로 줄어든다.',r'At height \(z\), the section is \([0,1-z]\times[0,2(1-z)]\), shrinking to a point at \(z=1\).'),
     (r'밑면 꼭짓점은 \((0,0,0),(1,0,0),(1,2,0),(0,2,0)\), 꼭대기는 \((0,0,1)\)인 사각뿔이다.',r'This is a rectangular pyramid with base vertices \((0,0,0),(1,0,0),(1,2,0),(0,2,0)\) and apex \((0,0,1)\).')],
    ('밑면 1×2, 높이 1의 사각뿔.','A rectangular pyramid with a 1-by-2 base and height 1.'),
    (r'단면적 \(2(1-z)^2\)를 적분하면 부피 \(2/3\)이며 피라미드 공식과 일치한다.',r'The section area \(2(1-z)^2\) integrates to \(2/3\), agreeing with the pyramid formula.'))
add(32,('포물기둥과 평면 사이 입체','A parabolic cylinder bounded by planes'),
    (r'\(\int_0^2\int_0^{2-y}\int_0^{4-y^2}dx\,dz\,dy\)의 부피 영역을 그려라.',r'Sketch the solid whose volume is \(\int_0^2\int_0^{2-y}\int_0^{4-y^2}dx\,dz\,dy\).'),
    ('y를 고정하면 xz-단면은 직사각형이다.','For fixed y, the xz-section is rectangular.'),
    [(r'영역은 \(0\le y\le2,\ 0\le x\le4-y^2,\ 0\le z\le2-y\)이다.',r'The region is \(0\le y\le2,\ 0\le x\le4-y^2,\ 0\le z\le2-y\).'),
     (r'곡면 \(x=4-y^2\), 평면 \(y+z=2\), 세 좌표평면으로 둘러싸인다. \(y=0\) 단면은 4×2 직사각형이다.',r'The boundary consists of \(x=4-y^2\), \(y+z=2\), and the three coordinate planes. The section at \(y=0\) is a 4-by-2 rectangle.'),
     (r'\(y\)가 증가하면 두 변의 길이가 \(4-y^2\), \(2-y\)로 줄고 \((0,2,0)\)에서 0이 된다.',r'As \(y\) increases, the side lengths \(4-y^2\) and \(2-y\) decrease to zero at \((0,2,0)\).')],
    (r'\(x,y,z\ge0,\ x+y^2\le4,\ y+z\le2\)인 곡면 쐐기.',r'The curved wedge \(x,y,z\ge0,\ x+y^2\le4,\ y+z\le2\).'),
    (r'\(\int_0^2(4-y^2)(2-y)dy=20/3\)으로 단면 부피를 독립 확인한다.',r'The cross-section check gives \(\int_0^2(4-y^2)(2-y)dy=20/3\).'))

orders={
33:[[(y,0,4-x*x-4*z*z),(x,-2*S.sqrt(1-z*z),2*S.sqrt(1-z*z)),(z,-1,1)],[(y,0,4-x*x-4*z*z),(z,-S.sqrt(1-x*x/4),S.sqrt(1-x*x/4)),(x,-2,2)],[(x,-S.sqrt(4-y-4*z*z),S.sqrt(4-y-4*z*z)),(y,0,4-4*z*z),(z,-1,1)],[(x,-S.sqrt(4-y-4*z*z),S.sqrt(4-y-4*z*z)),(z,-S.sqrt(1-y/4),S.sqrt(1-y/4)),(y,0,4)],[(z,-S.sqrt(4-y-x*x)/2,S.sqrt(4-y-x*x)/2),(x,-S.sqrt(4-y),S.sqrt(4-y)),(y,0,4)],[(z,-S.sqrt(4-y-x*x)/2,S.sqrt(4-y-x*x)/2),(y,0,4-x*x),(x,-2,2)]],
34:[[(x,-2,2),(y,-S.sqrt(9-z*z),S.sqrt(9-z*z)),(z,-3,3)],[(x,-2,2),(z,-S.sqrt(9-y*y),S.sqrt(9-y*y)),(y,-3,3)],[(y,-S.sqrt(9-z*z),S.sqrt(9-z*z)),(x,-2,2),(z,-3,3)],[(y,-S.sqrt(9-z*z),S.sqrt(9-z*z)),(z,-3,3),(x,-2,2)],[(z,-S.sqrt(9-y*y),S.sqrt(9-y*y)),(x,-2,2),(y,-3,3)],[(z,-S.sqrt(9-y*y),S.sqrt(9-y*y)),(y,-3,3),(x,-2,2)]],
35:[[(z,0,(4-y)/2),(y,x*x,4),(x,-2,2)],[(z,0,(4-y)/2),(x,-S.sqrt(y),S.sqrt(y)),(y,0,4)],[(x,-S.sqrt(y),S.sqrt(y)),(y,0,4-2*z),(z,0,2)],[(x,-S.sqrt(y),S.sqrt(y)),(z,0,(4-y)/2),(y,0,4)],[(y,x*x,4-2*z),(x,-S.sqrt(4-2*z),S.sqrt(4-2*z)),(z,0,2)],[(y,x*x,4-2*z),(z,0,(4-x*x)/2),(x,-2,2)]],
36:[[(z,0,(x+y-2)/2),(y,2-x,2),(x,0,2)],[(z,0,(x+y-2)/2),(x,2-y,2),(y,0,2)],[(y,2+2*z-x,2),(z,0,x/2),(x,0,2)],[(y,2+2*z-x,2),(x,2*z,2),(z,0,1)],[(x,2+2*z-y,2),(z,0,y/2),(y,0,2)],[(x,2+2*z-y,2),(y,2*z,2),(z,0,1)]],
37:[[(z,0,1-y),(y,S.sqrt(x),1),(x,0,1)],[(z,0,1-y),(x,0,y*y),(y,0,1)],[(x,0,y*y),(z,0,1-y),(y,0,1)],[(x,0,y*y),(y,0,1-z),(z,0,1)],[(y,S.sqrt(x),1-z),(z,0,1-S.sqrt(x)),(x,0,1)],[(y,S.sqrt(x),1-z),(x,0,(1-z)**2),(z,0,1)]],
38:[[(y,0,1-x),(z,0,1-x*x),(x,0,1)],[(z,0,1-x*x),(y,0,1-x),(x,0,1)],[(y,0,1-x),(x,0,S.sqrt(1-z)),(z,0,1)],[(z,0,1-x*x),(x,0,1-y),(y,0,1)],[(x,0,S.Min(1-y,S.sqrt(1-z))),(y,0,1),(z,0,1)],[(x,0,S.Min(1-y,S.sqrt(1-z))),(z,0,1),(y,0,1)]],
39:[[(z,0,y),(x,y,1),(y,0,1)],[(z,0,y),(y,0,x),(x,0,1)],[(y,z,x),(z,0,x),(x,0,1)],[(y,z,x),(x,z,1),(z,0,1)],[(x,y,1),(z,0,y),(y,0,1)],[(x,y,1),(y,z,1),(z,0,1)]],
40:[[(x,0,z),(z,y,1),(y,0,1)],[(y,0,z),(z,x,1),(x,0,1)],[(x,0,z),(y,0,z),(z,0,1)],[(y,0,z),(x,0,z),(z,0,1)],[(z,S.Max(x,y),1),(x,0,1),(y,0,1)],[(z,S.Max(x,y),1),(y,0,1),(x,0,1)]]}
regions={33:r'0\le y\le4-x^2-4z^2',34:r'-2\le x\le2,\ y^2+z^2\le9',35:r'x^2\le y,\ 0\le z,\ y+2z\le4',36:r'x\le2,\ y\le2,\ z\ge0,\ x+y\ge2+2z',37:r'0\le x\le y^2,\ y\ge0,\ z\ge0,\ y+z\le1',38:r'x,y,z\ge0,\ y\le1-x,\ z\le1-x^2',39:r'0\le z\le y\le x\le1',40:r'0\le x\le z\le1,\ 0\le y\le z'}
for n in range(33,41):
    other=n>=37
    stmt=(('주어진 적분과 같은 다른 다섯 순서를 구하라. ' if other else '다음 영역에서 연속함수 f의 삼중적분을 여섯 순서로 써라. ')+disp(integral('f(x,y,z)',orders[n][0]) if other else regions[n]),
          ('Write the five other equivalent orders for the given integral. ' if other else 'Write all six orders for the triple integral of a continuous function f over this region. ')+disp(integral('f(x,y,z)',orders[n][0]) if other else regions[n]))
    steps=[('먼저 적분 영역을 순서와 무관한 부등식으로 기록한다. '+disp(regions[n]),'First record the order-independent inequalities. '+disp(regions[n]))]
    for lims in orders[n][1 if other else 0:]:
        form=disp(integral('f(x,y,z)',lims))
        steps.append(('바깥 두 변수의 사영 범위를 정하고 안쪽 경계를 풀면 '+form,'Project onto the outer two variables and solve for the inner bounds: '+form))
    if n==38:
        steps.append((r'\(x\)를 먼저 적분할 때 두 상한을 동시에 만족시켜야 하므로 \(\min(1-y,\sqrt{1-z})\)를 쓴다. 분할식은 \(z=2y-y^2\)에서 두 상한을 나누면 된다.',r'Integrating \(x\) first requires both upper bounds, hence \(\min(1-y,\sqrt{1-z})\). To remove min, split the projection along \(z=2y-y^2\).'))
    if n==40:
        steps.append((r'\(z\ge x,y\)를 \(z\ge\max(x,y)\)로 합쳤다. max 없는 식은 단위 정사각형을 \(x=y\)로 나누면 얻는다.',r'The two lower bounds \(z\ge x,y\) combine as \(z\ge\max(x,y)\). Splitting the unit square along \(x=y\) removes max.'))
    add(n,('적분 순서 변경','Changing the order of integration'),stmt,
        ('각 순서에서 같은 입체를 기술해야 한다. 음의 제곱근 경계도 빠뜨리지 않는다.','Every order must describe the same solid. Retain both signs when a square root bounds a symmetric interval.'),steps,
        ('위 반복적분들이 요청한 모든 순서이다.','The iterated integrals above give all requested orders.'),
        ('각 순서의 경계를 공통 부등식으로 다시 바꾸면 같은 영역이 된다. 바깥 변수 범위와 경계면 교선도 대조했다.',
         'Converting every set of bounds back to the displayed common inequalities gives the same solid, including projection endpoints and intersecting boundaries.'))
    checks.append({'number':n,'region':regions[n],'orders':[[[str(q) for q in li] for li in order] for order in orders[n]],'method':'manual equivalent-inequality audit; six permutations present'})

add(41,('대칭으로 적분 소거','Cancellation by symmetry'),
    (r'\(C:\ x^2+y^2\le4,-2\le z\le2\)에서 \(\iiint_C(4+5x^2yz^2)dV\)를 기하·대칭만으로 구하라.',r'Use only geometry and symmetry to evaluate \(\iiint_C(4+5x^2yz^2)dV\) on \(C:\ x^2+y^2\le4,-2\le z\le2\).'),
    ('y를 -y로 반사하라.','Reflect y to -y.'),
    [(r'영역은 \(y\mapsto-y\)에 불변이지만 \(5x^2yz^2\)는 부호가 바뀌므로 그 적분은 0이다.',r'The region is invariant under \(y\mapsto-y\), while \(5x^2yz^2\) changes sign, so its integral vanishes.'),
     (r'원기둥의 반지름은 2, 높이는 4이므로 \(V=16\pi\)이다.',r'The cylinder has radius 2 and height 4, so \(V=16\pi\).'),
     (r'상수항의 적분은 \(4V=64\pi\)이다.',r'The constant term integrates to \(4V=64\pi\).')],disp(r'64\pi'),
    ('대칭 반사가 영역과 부피요소를 보존하며 홀수항만 제거한다.','The reflection preserves the region and volume element and cancels only the odd term.'))
add(42,('구의 대칭','Symmetry of a ball'),
    (r'단위구 \(B\)에서 \(\iiint_B(z^3+\sin y+3)dV\)를 기하·대칭만으로 구하라.',r'Use geometry and symmetry to evaluate \(\iiint_B(z^3+\sin y+3)dV\) over the unit ball.'),
    ('각 홀수항에 알맞은 좌표 반사를 사용한다.','Use the appropriate coordinate reflection for each odd term.'),
    [(r'\(z^3\)는 z에 홀수이고 \(\sin y\)는 y에 홀수이므로 구 위 적분은 각각 0이다.',r'The terms \(z^3\) and \(\sin y\) are odd in z and y respectively, so both integrate to zero over the ball.'),
     (r'남은 적분은 상수 3과 단위구 부피 \(4\pi/3\)의 곱이다.',r'The remaining integral is 3 times the unit-ball volume \(4\pi/3\).')],disp(r'4\pi'),
    ('두 반사는 모두 단위구를 보존한다.','Both reflections preserve the unit ball.'))

def mass(n,rho,lims,coords,statement,polar=False,inertia=False,decimal=False):
    weights=[S.Integer(1),*coords]+([coords[0]**2+coords[1]**2] if inertia else [])
    values=[]; steps=[]
    if polar: steps.append((r'원주좌표 \(x=r\cos\theta,y=r\sin\theta\)를 사용하고 부피요소의 \(r\)은 아래 밀도식에 이미 곱했다.',r'Use cylindrical coordinates \(x=r\cos\theta,y=r\sin\theta\); the Jacobian \(r\) is already included in the integrand below.'))
    labels=['m','N_x','N_y','N_z']+(['I_z'] if inertia else [])
    for label,w in zip(labels,weights):
        value=S.simplify(S.integrate(S.expand_trig(rho*w),*lims))
        assert not value.has(S.Integral),(n,label,value)
        values.append(value)
        eq=disp(label+'='+integral(S.expand_trig(rho*w),lims)+'='+tex(value))
        steps.append((('질량' if label=='m' else '모멘트')+' 적분을 계산한다. '+eq,('Evaluate the mass integral. ' if label=='m' else 'Evaluate this moment integral. ')+eq))
    cm=[S.simplify(q/values[0]) for q in values[1:4]]
    result='m='+tex(values[0])+r',\qquad(\bar x,\bar y,\bar z)='+tex(S.Tuple(*cm))
    if inertia: result+=r',\qquad I_z='+tex(values[4])
    steps.append((r'\(\bar x=N_x/m,\bar y=N_y/m,\bar z=N_z/m\)으로 나눈다. '+disp(result),r'Divide by mass: \(\bar x=N_x/m,\bar y=N_y/m,\bar z=N_z/m\). '+disp(result)))
    if decimal:
        result=r'm\approx'+f'{float(values[0]):.3f}'+r',\quad(\bar x,\bar y,\bar z)\approx('+','.join(f'{float(q):.3f}' for q in cm)+')'+r',\quad I_z\approx'+f'{float(values[4]):.3f}'
    add(n,('질량과 질량중심'+('·관성모멘트' if inertia else ''),'Mass, center of mass'+(', and inertia' if inertia else '')),
        statement,('질량은 밀도의 적분, 좌표 모멘트는 좌표×밀도의 적분이다.','Integrate density for mass and coordinate times density for first moments.'),steps,disp(result),
        ('기호 적분으로 모든 모멘트를 계산했다. 질량은 양수이고, 질량중심이 입체의 좌표 범위 안에 있는지 확인했다. 대칭으로 0이 되는 좌표도 대조했다.',
         'All moments were symbolically integrated. Mass is positive, centroid coordinates lie within the solid’s coordinate ranges, and symmetry-imposed zero coordinates were checked.'),('a','b','c') if inertia else ())
    checks.append({'number':n,'densityTimesJacobian':str(rho),'limits':[[str(q) for q in li] for li in lims],'moments':dict(zip(labels,map(str,values))),'centroid':list(map(str,cm))})

mass(43,3*r,[(z,0,1-r*r),(r,0,1),(t,0,2*pi)],(r*S.cos(t),r*S.sin(t),z),
     (r'\(0\le z\le1-x^2-y^2\)인 입체의 밀도가 3이다. 질량과 질량중심을 구하라.',r'Find the mass and center of mass for \(0\le z\le1-x^2-y^2\) with density 3.'),polar=True)
mass(44,4,[(x,0,1-z),(z,0,1-y*y),(y,-1,1)],(x,y,z),
     (r'\(z=1-y^2,x+z=1,x=0,z=0\)으로 둘러싸인 입체의 밀도는 4이다. 질량과 질량중심을 구하라.',r'Find the mass and center of mass of the solid bounded by \(z=1-y^2,x+z=1,x=0,z=0\), with density 4.'))
mass(45,x*x+y*y+z*z,[(x,0,a),(y,0,a),(z,0,a)],(x,y,z),
     (r'\(a>0\), \([0,a]^3\)에서 밀도 \(x^2+y^2+z^2\)의 질량과 질량중심을 구하라.',r'For \(a>0\), find the mass and center of mass on \([0,a]^3\) with density \(x^2+y^2+z^2\).'))
mass(46,y,[(z,0,1-x-y),(y,0,1-x),(x,0,1)],(x,y,z),
     (r'\(x,y,z\ge0,x+y+z\le1\)인 사면체에서 밀도가 y일 때 질량과 질량중심을 구하라.',r'Find the mass and center of mass of \(x,y,z\ge0,x+y+z\le1\) with density y.'))

add(47,('정육면체의 관성모멘트','Moments of inertia of a cube'),
    (r'원점에서 뻗는 세 모서리가 좌표축에 놓인 한 변 L의 정육면체, 일정 밀도 k의 세 좌표축 관성모멘트를 구하라.',r'A cube of side L has one vertex at the origin and three edges on the coordinate axes. Find its three moments of inertia for constant density k.'),
    (r'\(I_x=\iiint k(y^2+z^2)dV\)를 쓰고 대칭을 이용한다.',r'Use \(I_x=\iiint k(y^2+z^2)dV\), then symmetry.'),
    [(r'영역은 \([0,L]^3\)이다. '+disp(r'I_x=k\int_0^L\int_0^L\int_0^L(y^2+z^2)dx\,dy\,dz'),r'The region is \([0,L]^3\). '+disp(r'I_x=k\int_0^L\int_0^L\int_0^L(y^2+z^2)dx\,dy\,dz')),
     (r'두 항의 적분은 각각 \(kL^5/3\)이다. 좌표축 순환 대칭으로 세 값은 같다.',r'Each term contributes \(kL^5/3\). Permuting the coordinate axes leaves the cube unchanged.')],disp(r'I_x=I_y=I_z=\frac{2kL^5}{3}=\frac{2ML^2}{3},\quad M=kL^3'),
    ('차원은 질량×길이²이고 중심축 값에 평행축 정리를 적용해도 같다.','The units are mass times length squared; the parallel-axis theorem applied to the centroidal axes gives the same result.'))
add(48,('직육면체 중심축 관성모멘트','Centroidal inertia of a rectangular brick'),
    (r'중심이 원점이고 변이 좌표축과 평행한 크기 \(a\times b\times c\), 질량 M의 균질 직육면체의 관성모멘트를 구하라. a,b,c는 x,y,z 방향 길이로 둔다.',r'Find the coordinate-axis moments of inertia of a uniform brick centered at the origin, with mass M and dimensions a,b,c along x,y,z.'),
    (r'밀도는 \(M/(abc)\), 각 좌표 범위는 길이의 절반씩이다.',r'The density is \(M/(abc)\), and each coordinate runs between half-length endpoints.'),
    [(r'\(\int_{-b/2}^{b/2}y^2dy=b^3/12\), \(\int_{-c/2}^{c/2}z^2dz=c^3/12\)이다.',r'\(\int_{-b/2}^{b/2}y^2dy=b^3/12\) and \(\int_{-c/2}^{c/2}z^2dz=c^3/12\).'),
     (r'따라서 \(I_x=\frac{M}{abc}a(cb^3+bc^3)/12\). 다른 두 축은 변수 이름을 순환시킨다.',r'Thus \(I_x=\frac{M}{abc}a(cb^3+bc^3)/12\). Cycle the variables for the other axes.')],disp(r'I_x=\frac M{12}(b^2+c^2),\quad I_y=\frac M{12}(a^2+c^2),\quad I_z=\frac M{12}(a^2+b^2)'),
    ('a=b=c로 두면 정육면체 중심축 공식으로 줄어든다.','Setting a=b=c recovers the centroidal formula for a cube.'))
for n,lim,statement,answer in [(49,[(r,0,a),(z,0,S.Symbol('h',positive=True)),(t,0,2*pi)],
    (r'일정 밀도 k, \(x^2+y^2\le a^2,0\le z\le h\)인 원기둥의 z축 관성모멘트를 구하라.',r'Find the z-axis moment of inertia for constant density k on \(x^2+y^2\le a^2,0\le z\le h\).'),r'I_z=\frac{k\pi h a^4}{2}'),
    (50,[(r,0,z),(z,0,S.Symbol('h',positive=True)),(t,0,2*pi)],
    (r'일정 밀도 k, \(\sqrt{x^2+y^2}\le z\le h\)인 원뿔의 z축 관성모멘트를 구하라.',r'Find the z-axis moment of inertia for constant density k on \(\sqrt{x^2+y^2}\le z\le h\).'),r'I_z=\frac{k\pi h^5}{10}')]:
    eq=integral(k*r**3,lim)
    val=S.integrate(k*r**3,*lim)
    add(n,('회전체의 관성모멘트','Axial inertia of a solid of revolution'),statement,
        (r'z축 거리제곱은 \(r^2\), 부피요소는 \(r\,dr\,dz\,d\theta\)이다.',r'The squared distance to the z-axis is \(r^2\) and \(dV=r\,dr\,dz\,d\theta\).'),
        [('밀도와 거리제곱, 야코비안을 곱하면 '+disp(eq),'Multiply density, squared distance, and the Jacobian: '+disp(eq)),
         (r'안쪽 적분은 \(k r^4/4\)의 끝값 차이다. 나머지 높이·각도 적분을 계산하면 '+disp('I_z='+tex(val)),r'The inner integral uses \(kr^4/4\). Integrate the resulting expression over height and angle: '+disp('I_z='+tex(val)))],disp(answer),
        ('원판 단면의 관성모멘트를 높이에 대해 적분하는 방법과 일치한다.','Integrating the inertia of horizontal disk slices gives the same result.'))
    checks.append({'number':n,'integral':eq,'result':str(val)})

for n,domain,rho,lims in [(51,r'x^2\le y\le1,\ 0\le z\le1-y',S.sqrt(x*x+y*y),[(z,0,1-y),(y,x*x,1),(x,-1,1)]),
                          (52,r'x^2+y^2+z^2\le1,\ z\ge0',S.sqrt(x*x+y*y+z*z),[(z,0,S.sqrt(1-x*x-y*y)),(y,-S.sqrt(1-x*x),S.sqrt(1-x*x)),(x,-1,1)])]:
    op=integral(r'\rho(x,y,z)\,q(x,y,z)',lims)
    add(n,('질량·중심·관성 적분 설정','Setting up mass, centroid, and inertia'),
        (r'영역 '+math(domain)+', 밀도 '+math(r'\rho='+tex(rho))+r'에 대해 (a) 질량, (b) 질량중심, (c) z축 관성모멘트의 적분식만 세워라.',r'For '+math(domain)+' with density '+math(r'\rho='+tex(rho))+r', set up but do not evaluate integrals for (a) mass, (b) center of mass, (c) z-axis inertia.'),
        ('밀도를 포함한 적분 연산자를 정의하면 모든 양의 식을 간결하게 쓸 수 있다.','Define a density-weighted integral operator to write each quantity clearly.'),
        [('다음 연산자는 원래 영역과 밀도를 모두 포함한다. '+disp(r'J[q]='+op), 'This operator includes the original domain and density. '+disp(r'J[q]='+op)),
         (r'(a) 질량은 \(m=J[1]\)이다. (b) 좌표 모멘트는 \(J[x],J[y],J[z]\)이다.',r'(a) The mass is \(m=J[1]\). (b) The first moments are \(J[x],J[y],J[z]\).'),
         (r'(c) z축의 거리제곱을 곱하므로 \(I_z=J[x^2+y^2]\)이다.',r'(c) Weight by squared distance to the z-axis: \(I_z=J[x^2+y^2]\).')],
        disp(r'm=J[1],\quad(\bar x,\bar y,\bar z)=\frac{(J[x],J[y],J[z])}{J[1]},\quad I_z=J[x^2+y^2]'),
        ('경계를 대입하면 원래 곡면으로 돌아온다. 요청대로 적분값은 계산하지 않았다.','Substitution of each endpoint recovers the boundary surfaces. The integrals are left unevaluated as requested.'),('a','b','c'))

mass(53,r*(1+r*S.cos(t)+r*S.sin(t)+z),[(z,0,r*S.sin(t)),(r,0,1),(t,0,pi/2)],(r*S.cos(t),r*S.sin(t),z),
     (r'제1팔분공간의 \(x^2+y^2\le1,0\le z\le y\)에서 밀도 \(1+x+y+z\)의 (a) 질량, (b) 질량중심, (c) z축 관성모멘트를 정확히 구하라.',r'In the first octant, let \(x^2+y^2\le1,0\le z\le y\) and density \(1+x+y+z\). Find exact values for (a) mass, (b) center of mass, (c) z-axis inertia.'),polar=True,inertia=True)
mass(54,(x*x+r*r*S.cos(t)**2)*r,[(x,0,r*S.cos(t)/3),(r,0,3),(t,0,pi/2)],(x,r*S.cos(t),r*S.sin(t)),
     (r'22번 영역 \(y,z\ge0,y^2+z^2\le9,0\le x\le y/3\), 밀도 \(x^2+y^2\)의 (a) 질량, (b) 질량중심, (c) z축 관성모멘트를 소수 셋째 자리까지 구하라.',r'For the region of Exercise 22, \(y,z\ge0,y^2+z^2\le9,0\le x\le y/3\), with density \(x^2+y^2\), find (a) mass, (b) center of mass, (c) z-axis inertia to three decimal places.'),inertia=True,decimal=True)
items[-1]['steps']['ko'].insert(0,r'\(yz\)-평면에 \(y=r\cos\theta,z=r\sin\theta\)를 쓴다. \(0\le r\le3,0\le\theta\le\pi/2\)이고 야코비안 r을 밀도에 곱한다.')
items[-1]['steps']['en'].insert(0,r'Use \(y=r\cos\theta,z=r\sin\theta\) in the yz-plane. Then \(0\le r\le3,0\le\theta\le\pi/2\), and multiply the density by the Jacobian r.')

add(55,('결합확률밀도 정규화','Normalizing a joint density'),
    (r'\([0,2]^3\)에서 \(f=Cxyz\), 바깥에서는 0이다. (a) C, (b) \(P(X\le1,Y\le1,Z\le1)\), (c) \(P(X+Y+Z\le1)\)을 구하라.',r'Let \(f=Cxyz\) on \([0,2]^3\) and zero elsewhere. Find (a) C, (b) \(P(X\le1,Y\le1,Z\le1)\), (c) \(P(X+Y+Z\le1)\).'),
    ('전체 확률을 1로 정규화한 뒤 각 사건의 영역에서 적분한다.','Normalize total probability to 1, then integrate over each event region.'),
    [(r'(a) \(1=C(\int_0^2x\,dx)^3=8C\)이므로 \(C=1/8\).',r'(a) \(1=C(\int_0^2x\,dx)^3=8C\), hence \(C=1/8\).'),
     (r'(b) \(P=\frac18(\int_0^1x\,dx)^3=1/64\).',r'(b) \(P=\frac18(\int_0^1x\,dx)^3=1/64\).'),
     (r'(c) 사건은 제1팔분공간의 단위 사면체이다. '+disp(r'P=\frac18\int_0^1\int_0^{1-x}\int_0^{1-x-y}xyz\,dz\,dy\,dx=\frac1{16}\int_0^1\int_0^{1-x}xy(1-x-y)^2dy\,dx'),r'(c) The event is the unit simplex in the first octant. '+disp(r'P=\frac18\int_0^1\int_0^{1-x}\int_0^{1-x-y}xyz\,dz\,dy\,dx=\frac1{16}\int_0^1\int_0^{1-x}xy(1-x-y)^2dy\,dx')),
     (r'y를 먼저 적분하면 \(\frac1{192}\int_0^1x(1-x)^4dx=1/5760\)이다.',r'The y-integral gives \(\frac1{192}\int_0^1x(1-x)^4dx=1/5760\).')],disp(r'C=\frac18,\quad P_b=\frac1{64},\quad P_c=\frac1{5760}'),
    (r'단체의 단항식 공식 \(\int xyz\,dV=1!1!1!/6!=1/720\)로 (c)를 독립 검산한다. 작은 사건의 확률이 더 작다.',r'The simplex monomial identity \(\int xyz\,dV=1!1!1!/6!=1/720\) independently verifies (c). The smaller event has the smaller probability.'),('a','b','c'))
assert S.integrate(x*y*z/8,(z,0,1-x-y),(y,0,1-x),(x,0,1))==S.Rational(1,5760)

def save():
    from plot_15 import section156
    section156(items)
    assert [e['number'] for e in items]==list(range(1,56))
    for e in items:
        for lang in ['ko','en']:
            for text in [e['statement'][lang],e['hint'][lang],*e['steps'][lang],e['answer'][lang],e['check'][lang]]:
                assert not any(ord(c)<32 and c!='\n' for c in text),(e['number'],'control character')
                assert text.count(r'\(')==text.count(r'\)'),(e['number'],'inline delimiters')
                assert text.count(r'\[')==text.count(r'\]'),(e['number'],'display delimiters')
    payload={'section':'15.6','source':{'title':'Calculus: Early Transcendentals','edition':9,'language':'en','printedPages':[1130,1131,1132],'pdfPages':[1167,1168,1169]},'scope':{'kind':'exercise','numbers':[e['number'] for e in items],'total':len(items),'note':pair('§15.6 일반 연습문제.','General exercises for §15.6.')},'exercises':items}
    (ROOT/'exercise-content/s15-6.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'exercise-checks/s15-6-report.json').write_text(json.dumps({'sourceVisualCheck':[1167,1168,1169],'checks':checks},ensure_ascii=False,indent=2)+'\n')
    print('Saved',len(items),'exercises')

if __name__=='__main__': save()
