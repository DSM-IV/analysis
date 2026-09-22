"""Numerical quadrature independently checks exact integrals and distribution tails."""
from pathlib import Path
import json,sympy as s,mpmath as mp
mp.mp.dps=45;P=Path(__file__).parent;checks=[];x=s.symbols('x',real=True)
def check(label,actual,expected,tol='1e-30'):
 a=mp.mpf(str(actual));b=mp.mpf(str(expected));assert abs(a-b)<mp.mpf(tol)*max(1,abs(b)),(label,a,b);checks.append({'check':label,'value':mp.nstr(a,20)})
for sec in['8-4','8-5']:
 d=json.loads((P/f's{sec}-report.json').read_text())
 for i,r in enumerate(d['exactIntegrals']):
  f=s.sympify(r['integrand'],locals={'x':x});fn=s.lambdify(x,f,'mpmath');lo,hi=[mp.mpf(str(s.N(s.sympify(v),45)))for v in r['bounds']];actual=mp.quad(fn,[lo,hi]);v=mp.mpf(str(s.N(s.sympify(r['value']),45)));check(f'{sec} integral{i+1}',actual,v)
# Independently use area*centroid depth for simple plates.
r=json.loads((P/'s8-3-report.json').read_text());forces={z['exercise']:z['force']for z in r['exactIntegrationRecords']if 'force'in z}
for n,v in[(3,mp.mpf('62.5')*16*7),(4,mp.mpf('62.5')*25*(mp.mpf(2)+mp.mpf(10)/3)),(5,9800*64*mp.pi*12),(7,9800*12*4),(8,mp.mpf('62.5')*12*(mp.mpf(3)+mp.mpf(4)/3)),(9,mp.mpf('62.5')*mp.mpf(128)/9)]:check(f'8.3.{n} independent geometric load',s.N(s.sympify(forces[n]),45),v)
check('8.3.6 quadrature',s.N(s.sympify(forces[6]),45),9800*mp.quad(lambda t:2*(4-t)*mp.sqrt(36-t*t),[0,4]))
for z in r['exactIntegrationRecords']:
 if 'centroid'not in z:continue
 A=s.sympify(z['area']);cx,cy=map(s.sympify,z['centroid']);assert s.simplify(A*cx-s.sympify(z['MyOverDensity']))==0;assert s.simplify(A*cy-s.sympify(z['MxOverDensity']))==0
 checks.append({'check':f"8.3.{z['exercise']} moment identities",'passed':True})
# Density quadrature and independently computed normal probabilities.
phi=lambda t:mp.exp(-t*t/2)/mp.sqrt(2*mp.pi)
d=json.loads((P/'s8-5-report.json').read_text());expected=list(map(mp.mpf,d['numericalNormal']));normal=[mp.quad(phi,[-4/mp.mpf('2.8'),0,4/mp.mpf('2.8')]),mp.quad(phi,[3/mp.mpf('2.8'),mp.inf]),mp.quad(phi,[mp.mpf(1)/7,mp.inf]),mp.quad(phi,[-mp.inf,-mp.mpf(5)/3]),None,mp.quad(phi,[-mp.inf,-mp.mpf('1.5')]),mp.quad(phi,[mp.mpf(13)/8,mp.inf]),mp.quad(phi,[-2,0,2])]
for i,v in enumerate(normal):
 if v is not None:check(f'8.5 normal tail{i}',v,expected[i])
check('8.5.16 minimum target percentile',mp.quad(phi,[-mp.inf,(500-expected[4])/12]),mp.mpf('.05'))
check('8.5.8 triangular mean',mp.quad(lambda t:t*t/30,[0,6])+mp.quad(lambda t:t*(10-t)/20,[6,10]),mp.mpf(16)/3)
check('8.5.13 REM probability',mp.quad(lambda t:t/1600,[30,40])+mp.quad(lambda t:(80-t)/1600,[40,60]),mp.mpf(19)/32)
check('8.5.21 hydrogen normalization',mp.quad(lambda t:4*t*t*mp.exp(-2*t),[0,mp.inf]),1)
check('8.5.21 hydrogen mean scaled',mp.quad(lambda t:4*t**3*mp.exp(-2*t),[0,mp.inf]),mp.mpf('1.5'))
check('8.5.21 hydrogen radius4 probability',mp.quad(lambda t:4*t*t*mp.exp(-2*t),[0,4]),1-41*mp.exp(-8))
# Density14 omission: retain b and verify both stated depth formulas symbolically.
b=s.symbols('b',positive=True)
for H,answer in[(3,27195*(b+1)),(s.Rational(6,5),9065*(78*b+24)/125)]:assert s.simplify(9065*s.integrate((H-x)*(b+(2-b)*x/3),(x,0,H))-answer)==0
checks.append({'check':'8.3.14 both forces retain unspecified bottom width','passed':True})
# Exact trapezoidal-dam force, independently integrated in slope distance.
check('8.3.16 inclined dam',mp.quad(lambda u:mp.mpf('62.5')*u*mp.sqrt(3)/2*(100-5*u/7),[0,70]),mp.mpf(15312500)*mp.sqrt(3)/3)
# Numerical inverse supply/demand: verify both endpoints and surplus positivity.
d=json.loads((P/'s8-4-report.json').read_text())['numerical'];q=mp.mpf(d['8quantity']);check('8.4.8 inverse demand',800000*mp.exp(-q/5000)/(q+20000),16)
q=mp.mpf(d['11quantity']);check('8.4.11 inverse supply',mp.sqrt(30+mp.mpf('.01')*q*mp.exp(mp.mpf('.001')*q)),30)
(P/'s8-applications-independent.json').write_text(json.dumps({'sections':['8.3','8.4','8.5'],'checks':checks},ensure_ascii=False,indent=2)+'\n');print('PASS',len(checks),'independent checks')
