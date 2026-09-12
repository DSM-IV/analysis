"""Independent checks for worked vector, equilibrium and relative-motion answers."""
import sympy as s,math,json
from pathlib import Path
checks=[]
def near(name,a,b,tol=1e-10):assert abs(float(a-b))<tol,(name,a,b);checks.append(name)
a=s.Matrix([-3,4]);b=s.Matrix([9,-1]);near('19 norm difference',(a-b).norm(),13)
near('25 vector norm',s.Matrix([8,-1,4]).norm(),9)
near('26 scaled norm',(4*s.Matrix([6,2,-3])/7).norm(),4)
near('29 norm',s.Matrix([-2*s.sqrt(3),-2]).norm(),4)
near('29 smaller angle cosine',(-2*s.sqrt(3))/4,s.cos(5*s.pi/6))
near('34 vertical equilibrium',2*(500/s.sqrt(3))*s.sin(s.pi/3),500)
TL=350*math.cos(math.radians(38))/math.sin(math.radians(88));TR=350*math.cos(math.radians(50))/math.sin(math.radians(88))
near('35 horizontal equilibrium',-TL*math.cos(math.radians(50))+TR*math.cos(math.radians(38)),0)
near('35 vertical equilibrium',TL*math.sin(math.radians(50))+TR*math.sin(math.radians(38)),350)
t=s.symbols('t',positive=True);roots=s.solve(40*t*t-4800*t-2600000,t);T=roots[0]
near('38 speed condition',(1400/T)**2+(800/T+3)**2,49)
near('38 positive time',T,(4800+s.sqrt(4800**2+4*40*2600000))/80)
near('41 tangent normalization',(s.Matrix([1,4])/s.sqrt(17)).norm(),1)
near('42 orthogonality',s.Matrix([1,s.sqrt(3)]).dot(s.Matrix([-s.sqrt(3),1])),0)
near('45 x',s.Rational(9,7)*3+s.Rational(11,7)*2,7)
near('45 y',s.Rational(9,7)*2-s.Rational(11,7),1)
(Path(__file__).parent/'s12-2-report.json').write_text(json.dumps({'passed':len(checks),'checks':checks,'sourceVisualPdfPages':[918,919,920],'note':'Exercise29 uses the smaller angle with the positive x-axis, subject to quadrantIII.'},indent=2)+'\n');print('PASS',len(checks),'independent checks')
