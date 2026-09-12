from calc1_helpers import *
from early_helpers import svg_surface

def volume(b,n,page,st,pieces,v,axis=0,setup=False,parts=[],extra=[],numeric=False):
 pieces=[tuple(map(s.sympify,p))for p in pieces]; steps=list(extra);values=[];ints=[];plots=[]
 for lo,hi,outer,inner in pieces:
  assert float((outer-inner).subs(v,(lo+hi)/2))>=0 and float(inner.subs(v,(lo+hi)/2))>=0
  expr=s.pi*(outer**2-inner**2);I=s.Integral(expr,(v,lo,hi));ints.append(I)
  steps.append(('회전축까지 거리로 바깥·안쪽 반지름을 잡는다.','Measure both radii as distances from the axis.'))
  steps+=fs(str(v)+r'\in['+tex(lo)+','+tex(hi)+r'],\quad R='+tex(outer)+r',\quad r='+tex(inner),r'A('+str(v)+r')=\pi(R^2-r^2)='+tex(expr))
  numerical=mp.quad(s.lambdify(v,expr,'mpmath'),[float(lo),float(hi)])
  val=s.Float(str(numerical),30)if numeric else s.integrate(s.expand(expr),(v,lo,hi));assert not val.has(s.Integral),(n,val)
  if numeric:
   alt=mp.quadgl(s.lambdify(v,expr,'mpmath'),[float(lo),float(hi)],maxdegree=10);assert abs(alt-numerical)<1e-7
  assert abs(float(val)-float(numerical))<1e-7*max(1,abs(float(numerical))),(n,val,numerical)
  values.append(val);steps+=fs(s.latex(I)+(((r'\approx'if numeric else'=')+tex(val))if not setup else''))
  fo=s.lambdify(v,outer,'math');fi=s.lambdify(v,inner,'math');mid=float((lo+hi)/2)
  if str(v)=='x':
   fun=lambda t,a,fo=fo:(t,float(axis)+fo(t)*math.cos(a),fo(t)*math.sin(a))
   fin=lambda t,a,fi=fi:(t,float(axis)+fi(t)*math.cos(a),fi(t)*math.sin(a))
   wash=lambda u,a,fo=fo,fi=fi,mid=mid:(mid,float(axis)+(fi(mid)+u*(fo(mid)-fi(mid)))*math.cos(a),(fi(mid)+u*(fo(mid)-fi(mid)))*math.sin(a))
  else:
   fun=lambda t,a,fo=fo:(float(axis)+fo(t)*math.cos(a),t,fo(t)*math.sin(a))
   fin=lambda t,a,fi=fi:(float(axis)+fi(t)*math.cos(a),t,fi(t)*math.sin(a))
   wash=lambda u,a,fo=fo,fi=fi,mid=mid:(float(axis)+(fi(mid)+u*(fo(mid)-fi(mid)))*math.cos(a),mid,(fi(mid)+u*(fo(mid)-fi(mid)))*math.sin(a))
  sign=-1 if float(axis)>0 else 1
  profile=(lambda t,u,fo=fo,fi=fi:(t,float(axis)+sign*(fi(t)+u*(fo(t)-fi(t))),0))if str(v)=='x'else(lambda t,u,fo=fo,fi=fi:(float(axis)+sign*(fi(t)+u*(fo(t)-fi(t))),t,0))
  plots.extend([(profile,(float(lo),float(hi)),(0,1),'Original plane region, z=0'),([fun,fin],(float(lo),float(hi)),(0,2*math.pi),f'{b.section}.{n}: solid, {v} from {float(lo):.3g} to {float(hi):.3g}'),(wash,(0,1),(0,2*math.pi),'Representative washer (separate view)')])
 ans=M('V='+s.latex(s.Add(*ints,evaluate=False)))if setup else M('V='+tex(sum(values)))
 b.add(n,page,('원판·와셔와 부피','Disks, washers, and volume'),st,steps,same(ans),parts=parts)
 b.verify(n,'반지름 순서와 비음성을 확인하고 각 와셔 적분을 독립 수치구적으로 대조했다.','Checked nonnegative ordered radii and compared every washer integral with independent numerical quadrature.')
 b.plot(n,plots,('주어진 반지름으로 직접 구성한 회전체와 대표 와셔. 와셔는 보기 쉽게 별도 패널에 표시했다.','Solid and a representative washer constructed from the given radii. The washer is shown separately for clarity.'))
 return s.simplify(sum(values))
