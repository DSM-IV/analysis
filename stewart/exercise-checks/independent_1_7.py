import json
from pathlib import Path
import mpmath as m
import sympy as s
m.mp.dps=70
checks=[]
def ck(n,method,detail):checks.append({'number':n,'method':method,'detail':detail})
for n,fn,a,L,e,delta in [(3,m.sqrt,4,2,m.mpf('.4'),m.mpf('1.44')),(4,lambda x:x*x,1,1,m.mpf('.5'),m.sqrt(m.mpf('1.5'))-1),(5,lambda x:m.sqrt(x*x+5),2,3,m.mpf('.3'),m.sqrt(m.mpf('5.89'))-2),(6,lambda x:m.cos(x)**2,m.pi/6,m.mpf('.75'),m.mpf('.1'),m.acos(m.sqrt(m.mpf('.65')))-m.pi/6)]:
 assert max(abs(fn(a-delta)-L),abs(fn(a+delta)-L))<e+m.mpf('1e-60')
 for k in range(-99,100):assert abs(fn(a+delta*k/100)-L)<e
 ck(n,'70-digit endpoint and interior bound check',str(delta))
for n,fn,L,es,ds in [(7,lambda x:x**3-3*x+4,6,['.2','.1'],['.021901','.011029']),(8,lambda x:(4*x+1)/(3*x-4),m.mpf('4.5'),['.5','.1'],['.090909','.020408'])]:
 for e,de in zip(map(m.mpf,es),map(m.mpf,ds)):
  assert max(abs(fn(2-de)-L),abs(fn(2+de)-L))<e
  ck(n,'independent rounded-delta endpoint bounds',str(de))
for M in [500,1000]:
 de=m.asin(1/m.sqrt(M));assert abs(1/m.sin(de)**2-M)<m.mpf('1e-60')
 for k in range(1,100):assert 1/m.sin(de*k/100)**2>M
 ck(10,'70-digit reciprocal-sine boundary check',str(de))
for area in [995,1000,1005]:
 r=m.sqrt(area/m.pi);assert abs(m.pi*r*r-area)<m.mpf('1e-60')
 ck(11,'area recovered from independently computed radius',str(area))
for temp in [199,200,201]:
 w=(-m.mpf('2.155')+m.sqrt(m.mpf('2.155')**2+m.mpf('.4')*(temp-20)))/m.mpf('.2')
 assert abs(m.mpf('.1')*w*w+m.mpf('2.155')*w+20-temp)<m.mpf('1e-60')
 ck(12,'temperature recovered from independent quadratic root',str(temp))
for n,fn,a,L,delfun in [(25,lambda x:x*x,0,0,lambda e:m.sqrt(e)),(26,lambda x:x**3,0,0,lambda e:m.root(e,3)),(29,lambda x:x*x-4*x+5,2,1,lambda e:m.sqrt(e)),(30,lambda x:x*x+2*x-7,2,1,lambda e:min(1,e/7)),(31,lambda x:x*x-1,-2,3,lambda e:min(1,e/5)),(32,lambda x:x**3,2,8,lambda e:min(1,e/19)),(33,lambda x:x*x,3,9,lambda e:min(2,e/8)),(34,lambda x:x*x,3,9,lambda e:m.sqrt(9+e)-3),(36,lambda x:1/x,2,m.mpf('.5'),lambda e:min(1,2*e))]:
 for ep in ['.000001','.01','.4','1','10','100']:
  e=m.mpf(ep);de=delfun(e)
  for k in [-99,-70,-10,10,70,99]:assert abs(fn(a+de*k/100)-L)<e,(n,ep,k)
 ck(n,'70-digit sampling supplements the written uniform proof','6 epsilon scales; 6 interior offsets each')
for e in map(m.mpf,['.00001','.4','1','10','100']):
 A=1+e/2;B=m.sqrt(A*A+m.mpf(1)/27);b=m.root(A+B,3)-m.root(B-A,3);de=b-1
 assert abs(b**3+b-(2+e))<m.mpf('1e-55')
 assert abs((1-de)**3+(1-de)+1-3)<e
 ck(35,'independent real-Cardano root and opposite-boundary test',str(e))
x,d=s.symbols('x d',real=True)
assert s.expand((1+d)**3+(1+d)+1-3)==d**3+3*d*d+4*d
assert s.expand(3-((1-d)**3+(1-d)+1))==d**3-3*d*d+4*d
ck(35,'symbolic asymmetric-error identities','right error minus left error = 6d²')
p=Path(__file__).with_name('s1-7-independent.json');p.write_text(json.dumps({'section':'1.7','passed':len(checks),'checks':checks},indent=2)+'\n');print(len(checks),'checks passed')
