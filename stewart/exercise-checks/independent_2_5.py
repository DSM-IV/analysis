import json,ast,math
from pathlib import Path
import sympy as s
import mpmath as m
m.mp.dps=45
x=s.symbols('x',real=True);R,N,P=s.symbols('r n p',real=True)
# Re-enter the source functions independently of the author's SymPy expressions.
f={1:lambda t:(5-t**4)**3,2:lambda t:m.sqrt(t**3+2),3:lambda t:m.sin(m.cos(t)),4:lambda t:m.tan(t*t),5:lambda t:m.sqrt(m.sin(t)),6:lambda t:m.sin(m.sqrt(t)),7:lambda t:(2*t**3-5*t*t+4)**5,8:lambda t:(t**5+3*t*t-t)**50,9:lambda t:m.sqrt(5*t+1),10:lambda t:1/m.root(t*t-1,3),11:lambda t:1/(2*t+1)**2,12:lambda t:1/(2*t+1)**4,13:lambda t:1/(m.cos(t)+m.tan(t))**2,14:lambda t:(2-m.sin(t))**m.mpf('1.5'),15:lambda t:m.cos(t*t),16:lambda t:m.cos(t)**2,17:lambda t:t*m.root(1+t*t,3),18:lambda t:t*m.sin(m.pi*t),19:lambda t:(4*t+5)**3*(t*t-2*t+5)**4,20:lambda t:(1-4*t)**2*m.sqrt(t*t+1),21:lambda t:m.root(t+1,3)**2*(2*t*t-1)**3,22:lambda t:(3*t-1)**4/(2*t+1)**3,23:lambda t:m.sqrt(t/(t+1)),24:lambda t:(t+1/t)**5,25:lambda t:((t**3-1)/(t**3+1))**8,26:lambda t:m.sqrt((1+m.sin(t))/(1+m.cos(t))),27:lambda t:(t*t-1)**3/(2*t+1)**5,28:lambda t:t*t/m.sqrt(t**3+1),29:lambda t:m.cos(1/m.cos(4*t)),30:lambda t:m.tan(2*t)**2,31:lambda t:m.cos(t)/m.sqrt(1+m.sin(t)),32:lambda t:m.tan(t*t*m.sin(t)),33:lambda t:((1-m.cos(2*t))/(1+m.cos(2*t)))**4,34:lambda t:t*m.sin(1/t),35:lambda t:m.sin(t)*m.cos(1-t*t),36:lambda t:m.sin(t+m.cos(m.sqrt(t))),37:lambda t:m.tan(m.sqrt(1+t*t)),38:lambda t:(1+m.cos(t)**2)**3,39:lambda t:m.sin(t*t+1)**2,40:lambda t:((t*t-1)**6-3*t)**4,41:lambda t:m.cos(m.sin(t)**3)**4,42:lambda t:m.sin(m.cos(t*t))**3,43:lambda t:m.tan(1/m.cos(m.cos(t))),44:lambda t:m.sqrt(t+m.sqrt(t+m.sqrt(t))),45:lambda t:(6*m.sin(3*t)+2)**4,46:lambda t:m.sin(t+m.tan(t+m.cos(t))),47:lambda t:m.cos(m.sqrt(m.sin(m.tan(m.pi*t)))),48:lambda t:(t+(t+m.sin(t)**2)**3)**4}
checks=[]
def close(n,a,b,method):
 err=abs(a-b)/max(1,abs(a),abs(b));assert err<m.mpf('1e-32'),(n,a,b,err)
 checks.append({'number':n,'method':method,'relativeResidual':str(err)})
# Load the formula assignment, not the authoring script's execution or its answers.
tree=ast.parse(Path(__file__).with_name('build_2_5.py').read_text());node=next(z.value for z in tree.body if isinstance(z,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='forms'for t in z.targets));forms=eval(compile(ast.Expression(node),'<author formula data>','eval'),{'s':s,'x':x,'R':R,'N':N,'P':P})
forms.update({1:(5-x**4)**3,2:s.sqrt(x**3+2),3:s.sin(s.cos(x)),4:s.tan(x*x),5:s.sqrt(s.sin(x)),6:s.sin(s.sqrt(x))})
for n,fn in f.items():
 expr=forms[n].subs({R:3,N:2,P:4});de=s.lambdify(x,s.diff(expr,x),'mpmath')
 for val in (['1.3','1.7']if n==10 else ['0.13','0.21']):
  t=m.mpf(val);close(n,m.diff(fn,t),de(t),'45-digit numerical differentiation of independently transcribed source at '+val)
def eq(n,a,b,method):
 z=s.trigsimp(s.simplify(a-b));assert z==0,(n,z);checks.append({'number':n,'method':method,'residual':'0'})
for n,fn,second in[(49,s.cos(s.sin(3*x)),9*s.sin(s.sin(3*x))*s.sin(3*x)-9*s.cos(s.sin(3*x))*s.cos(3*x)**2),(50,(1+s.sqrt(x))**3,s.Rational(3,4)*(x-1)/x**s.Rational(3,2)),(51,s.sqrt(s.cos(x)),-(1+s.cos(x)**2)/(4*s.cos(x)**s.Rational(3,2))),(52,4*x/s.sqrt(x+1),-(x+4)/(x+1)**s.Rational(5,2))]:eq(n,s.diff(fn,x,2),second,'independently derived second derivative')
for n,fn,at,slope in[(53,(3*x-1)**-6,0,18),(54,s.sqrt(1+x**3),2,2),(55,s.sin(s.sin(x)),s.pi,-1),(56,s.sin(x)**2*s.cos(x),s.pi/2,-1),(57,s.tan(s.pi*x*x/4),1,s.pi),(58,x/s.sqrt(2-x*x),1,2)]:eq(n,s.diff(fn,x).subs(x,at),slope,'tangent slope substitution')
eq(59,s.diff(x*s.sqrt(2-x*x),x),2*(1-x*x)/s.sqrt(2-x*x),'product and chain derivative');eq(60,s.diff(s.sin(x+s.sin(2*x)),x),s.cos(x+s.sin(2*x))*(1+2*s.cos(2*x)),'nested trigonometric derivative')
for t in[s.pi/2,3*s.pi/2]:eq(61,s.diff(2*s.sin(x)+s.sin(x)**2,x).subs(x,t),0,'stationary point')
eq(62,s.diff(s.sqrt(1+2*x),x).subs(x,4),s.Rational(1,3),'perpendicular slope');eq(64,3*4/(2*s.sqrt(4+3*7)),s.Rational(6,5),'composed square root')
eq(69,(-s.Rational(2,3))/(2*s.sqrt(2)),-s.sqrt(2)/6,'tangent slope divided by radical chain factor')
g=s.Function('g');eq(72,s.diff(x*g(x*x),x,2),6*x*s.Subs(s.diff(g(x),x),x,x*x)+4*x**3*s.Subs(s.diff(g(x),x,2),x,x*x),'general second derivative')
eq(75,s.diff(s.cos(2*x),x,103),2**103*s.sin(2*x),'103rd derivative');eq(76,s.diff(x*s.sin(s.pi*x),x,35),-s.pi**35*x*s.cos(s.pi*x)-35*s.pi**34*s.sin(s.pi*x),'35th product derivative')
for n,result,expected in[(63,4*6,24),(65,5*6,30),(65,9*4,36),(66,4*5,20),(66,7*9,63),(67,-s.Rational(1,4)*-1,s.Rational(1,4)),(67,-1*2,-2),(67,s.Rational(1,2)*-1,-s.Rational(1,2)),(68,-1*-1,1),(68,4*2,8),(71,6*5*4,120),(73,2*3*2*4*2,96),(74,6*(3+5*(2+4)),198)]:eq(n,s.sympify(result),s.sympify(expected),'independent chain-factor arithmetic; graph68 approximate inputs')
F,G=s.Function('F'),s.Function('G');eq(84,s.diff(F(x)/G(x),x),(G(x)*s.diff(F(x),x)-F(x)*s.diff(G(x),x))/G(x)**2,'general quotient identity');eq(88,s.diff(F(G(x)),x,2),s.Subs(s.diff(F(x),x,2),x,G(x))*s.diff(G(x),x)**2+s.Subs(s.diff(F(x),x),x,G(x))*s.diff(G(x),x,2),'general second-order chain identity')
Path(__file__).with_name('s2-5-independent.json').write_text(json.dumps({'section':'2.5','passed':len(checks),'checks':checks},indent=2)+'\n');print(len(checks),'independent checks passed')
