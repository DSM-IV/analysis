"""Independent distance, completed-square, and volume calculations."""
import sympy as s,json
from pathlib import Path
x,y,z,t=s.symbols('x y z t',real=True);P=s.Matrix([x,y,z]);A=s.Matrix([-1,5,3]);B=s.Matrix([6,2,-2]);checks=[]
def eq(name,a,b):assert s.simplify(a-b)==0,(name,a,b);checks.append(name)
eq('48 squared-distance locus',4*(P-B).dot(P-B)-(P-A).dot(P-A),3*(x*x+y*y+z*z)-50*x-6*y+22*z+141)
eq('48 completed square',(x-s.Rational(25,3))**2+(y-1)**2+(z+s.Rational(11,3))**2-s.Rational(332,9),(4*(P-B).dot(P-B)-(P-A).dot(P-A))/3)
eq('49 perpendicular bisector',(P-A).dot(P-A)-(P-B).dot(P-B),14*x-6*y-10*z-9)
eq('50 overlap volume',2*s.integrate(s.pi*(4-t*t),(t,s.Rational(3,2),2)),11*s.pi/12)
for n,pts,expected in [(9,[(3,5,-2),(-1,1,-4)],[36]),(10,[(-6,-3,0),(2,4,5)],[138]),(11,[(3,-2,-3),(7,0,1),(1,2,1)],[36,40,36]),(12,[(2,-1,0),(4,1,1),(4,-5,4)],[9,45,36])]:
 pairs=[(0,1)]if len(pts)==2 else[(0,1),(1,2),(2,0)]
 for (a,b),v in zip(pairs,expected):q=s.Matrix(pts[a])-s.Matrix(pts[b]);eq(f'{n} distance {a}-{b}',q.dot(q),v)
for n,raw,completed in [(19,x*x+y*y+z*z+8*x-2*z-8,(x+4)**2+y*y+(z-1)**2-25),(20,x*x+y*y+z*z-6*x+4*y+10*z,(x-3)**2+(y+2)**2+(z+5)**2-38),(21,x*x+y*y+z*z-x+2*y+s.Rational(1,2),(x-s.Rational(1,2))**2+(y+1)**2+z*z-s.Rational(3,4)),(22,x*x+y*y+z*z-4*x+s.Rational(3,2)*y+3,(x-2)**2+(y+s.Rational(3,4))**2+z*z-s.Rational(25,16))]:eq(f'{n} sphere',raw,completed)
eq('24 diameter squared radius',(s.Matrix([5,4,3])-s.Matrix([1,6,-9])).dot(s.Matrix([5,4,3])-s.Matrix([1,6,-9]))/4,41)
eq('51 second sphere',x*x+y*y+z*z-4*x-4*y-4*z+11,(x-2)**2+(y-2)**2+(z-2)**2-1)
(Path(__file__).parent/'s12-1-report.json').write_text(json.dumps({'section':'12.1','checks':checks,'passed':len(checks),'sourceVisualPages':[910,911],'oddAnswersCompared':'Appendix G A111, including Exercise47 point (2,1,4)'},indent=2)+'\n')
print('PASS:',len(checks),'independent calculations')
