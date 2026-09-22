import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s8-1.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,54))
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   if key=='steps':assert len(vals)>=2,(e['number'],'steps')
   for v in vals:
    assert not re.search('[ぁ-ゟ゠-ヿ]',v),(e['number'],key,lang,v)
    if lang=='en':assert not re.search('[가-힣]',v),(e['number'],key,v)
    require_string(v,f'{e["number"]}.{key}.{lang}')
 assert e['status']=='math-verified'
 if 'figure'in e:ET.parse(ROOT/'exercise-content'/e['figure']['src'].split('../exercise-content/')[1])



mp.mp.dps=50;checks=[]
def near(a,b,name,tol=mp.mpf('1e-22')):
 assert abs(a-b)<tol,(name,a,b);checks.append(name)
rows=json.loads((ROOT/'exercise-checks/calc1-s8-1-numeric-results.json').read_text());nums={e['number']:mp.mpf(e['numeric'])for e in rows}
near(mp.quad(lambda t:mp.sqrt(1+(2*t+3*t*t)**2),[1,2]),nums[27],'27 direct slope quadrature')
near(mp.quad(lambda t:mp.sqrt(1+(1-mp.sin(t))**2),[0,mp.pi/2]),nums[28],'28 direct slope quadrature',mp.mpf('1e-14'))
near(mp.quad(lambda t:mp.sqrt(1+(t**(-mp.mpf(2)/3)/3)**2),[1,4]),nums[29],'29 cube-root slope')
near(mp.quad(lambda t:mp.sqrt(1+(mp.tan(t)+t/mp.cos(t)**2)**2),[0,1]),nums[30],'30 tangent slope')
near(mp.quad(lambda t:mp.sqrt(1+((1-t)*mp.exp(-t))**2),[1,2]),nums[31],'31 exponential slope')
near(mp.quad(lambda t:mp.sqrt(1+(2*t/(t*t+4))**2),[-2,0,2]),nums[32],'32 log slope')
near(mp.quad(lambda t:mp.sqrt(1+(mp.sin(t)+t*mp.cos(t))**2),[0,mp.pi/2,mp.pi,3*mp.pi/2,2*mp.pi]),nums[33],'33 oscillatory length quadrature',mp.mpf('1e-13'))
near(mp.quad(lambda t:mp.sqrt(1+4*t*t*mp.exp(-2*t*t)),[0,1,2]),nums[34],'34 Gaussian length')
near(mp.quad(lambda t:mp.sqrt(9*t**4+16*(1-t**3)**2),[0,.5,1,mp.root(4,3)]),nums[35],'35 regularized endpoint length')
near(mp.quad(lambda t:mp.sqrt(1+(1+mp.cos(t))**2),[0,mp.pi,2*mp.pi]),nums[36],'36 sinusoid length')
for n in [35,36]:
 vals=next(r['polygonal']for r in rows if r['number']==n);assert all(vals[i][1]<=vals[i+1][1]+1e-12 for i in range(2));assert vals[-1][1]<nums[n];checks.append(f'{n} polygonal monotonic lower approximations')
near(mp.quad(lambda t:mp.sqrt(1+mp.mpf(16)/9*t**(mp.mpf(2)/3)),[0,1]),mp.mpf(205)/128-mp.mpf(81)/512*mp.log(3),'38 exact substituted length')
near(4*mp.quad(lambda t:3*mp.sin(t)*mp.cos(t),[0,mp.pi/2]),6,'39 astroid symmetry')
near(mp.quad(lambda y:mp.sqrt(1+mp.mpf(9)/4*y),[0,1]),(13*mp.sqrt(13)-8)/27,'40 regular branch length')
near(mp.quad(lambda y:mp.sqrt(1+mp.mpf(9)/4*y),[0,1])+mp.quad(lambda y:mp.sqrt(1+mp.mpf(9)/4*y),[0,4]),(13*mp.sqrt(13)+80*mp.sqrt(10)-16)/27,'40 cusp splits two branches')
for z in map(mp.mpf,['-.9','0','.8']):near(mp.diff(lambda x:2*mp.sqrt(2)*(mp.sqrt(1+x)-1),z),mp.sqrt(1+((1-z)/mp.sqrt(1-z*z))**2),f'43 signed arc derivative {z}')
z=((mp.mpf('13.5')+5*mp.sqrt(5))**(mp.mpf(2)/3)-5)/3;near(mp.mpf(2)/9*((3*z+5)**mp.mpf('1.5')-5*mp.sqrt(5)),3,'44 inverse arc-length point')
a=mp.findroot(lambda a:2*a*mp.sinh(25/a)-51,(50,90));near(mp.quad(lambda x:mp.cosh(x/a),[-25,25]),51,'49 catenary cable length')
for z in map(mp.mpf,['-2','0','3']):
 f=mp.exp(z)/4+mp.exp(-z);df=mp.exp(z)/4-mp.exp(-z);near(f*f-df*df,1,f'51 length-area identity {z}')
for k in [1,2,5,20]:
 c=mp.mpf(2)**(-mp.mpf(1)/(2*k));assert 8*mp.sqrt((1-c)**2+c*c)<=8;checks.append(f'52 inscribed broken-line bound k={k}')
near(mp.quad(lambda x:x**mp.mpf('1.5'),[1,4]),mp.mpf(62)/5,'53 FTC cancellation')
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:
    assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
    assert not re.search(r'\\(?:quad|qquad)[A-Za-z]',v),(e['number'],key,v)
report={'section':'8.1','count':53,'sourcePDFPages':[640,641,642],'sourceVisualReview':'All three pages visually inspected, including omitted interval22, cube-root curve35, and full family52.','independentChecks':checks,'authorChecks':'Exact speed squares and primitive derivatives; exact values independently quadrature-checked.','figureCount':sum('figure'in e for e in E.values()),'status':'passed'}
(ROOT/'exercise-checks/calc1-s8-1-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('PASS',len(E),'exercises',len(checks),'independent checks')
