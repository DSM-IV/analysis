import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));from build_exercises import require_string
d=json.loads((ROOT/'exercise-content/s6-5.json').read_text());E={e['number']:e for e in d['exercises']};assert list(E)==list(range(1,23))
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
def near(a,b,name,tol=mp.mpf('1e-35')):assert abs(a-b)<tol,(name,a,b);checks.append(name)
k=mp.log(mp.mpf('19.5'))/mp.mpf('1.5');near(50*mp.exp(mp.mpf('1.5')*k),975,'3 observed population');near(50*mp.exp(3*k),mp.mpf('19012.5'),'3 exact unrounded three-hour population')
k=mp.log(64)/4;near(50*mp.exp(2*k),400,'4 first observation');near(50*mp.exp(6*k),25600,'4 second observation')
frac=mp.power(2,-mp.mpf(68000000)/5730);logfrac=mp.log10(frac);assert -3573<logfrac<-3572;checks.append('12 tiny radiocarbon fraction independently computed at50digits')
near(mp.power(2,-(5730*mp.log(1000)/mp.log(2))/5730),mp.mpf('.001'),'12 detection threshold')
k=mp.log(mp.mpf(15)/22)/30;near(75+110*mp.exp(30*k),150,'15 cooling observation');near(75+110*mp.exp(k*mp.log(mp.mpf(25)/110)/k),100,'15 threshold')
k=mp.log(mp.mpf('10.3')/mp.mpf('12.5'));tau=mp.log(mp.mpf('12.5')/17)/k;near(20+17*mp.exp(k*tau),mp.mpf('32.5'),'16 first body-temperature observation');near(20+17*mp.exp(k*(tau+1)),mp.mpf('30.3'),'16 second body-temperature observation')
for P,r,t,ms in [(2500,mp.mpf('.045'),3,[1,4,12,52,365,8760]),(4000,mp.mpf('.0175'),5,[1,2,12,52,365])]:
 vals=[P*mp.power(1+r/m,m*t)for m in ms];assert vals==sorted(vals) and vals[-1]<P*mp.exp(r*t)
 checks.append(f'{P} high-precision compounding monotonicity and continuous limit')
for e in E.values():
 for key in ['statement','answer','check','steps']:
  for lang in ['ko','en']:
   vals=e[key][lang];vals=[vals]if isinstance(vals,str)else vals
   for v in vals:assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',v),(e['number'],key)
report={'section':'6.5','count':22,'sourcePDFPages':[521,522],'sourceVisualReview':'Both exercise pages visually inspected,including all demographic tables and compounding frequencies.','authorVerification':'Growth/decay initial and observed values substituted;time thresholds solved with unrounded logarithms;thermal models applied to temperature differences.','independentChecks':checks,'figureCount':sum('figure'in e for e in E.values()),'oddAnswerAppendix':'A86–A87 approximate results agree;3 uses unrounded k to give exact19012.5 and37650.003per hour instead of values obtained by prematurely rounding k.','sourceAssumptions':'8 explicitly follows the problem’s supplied28-day half-life;6 is a historical-table model forecast,not a current population claim.','browserVisualReview':'20 SVG checked in Chrome;three growth curves and their rate labels are visible.','status':'passed'}
(ROOT/'exercise-checks/calc1-s6-5-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report)
