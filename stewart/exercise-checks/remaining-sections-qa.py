"""Independent numerical checks for the final three sections; no author imports."""
import json,re
from pathlib import Path
import mpmath as m
m.mp.dps=45
R=Path(__file__).resolve().parents[1];reports=[]
docs={sec:json.loads((R/f'exercise-content/s{sec}.json').read_text())for sec in ['2-8','2-9','4-5']}
# Catch malformed TeX spacing that MathJax's noUndefined extension renders red.
for sec,document in docs.items():
 text=json.dumps(document,ensure_ascii=False)
 assert not re.search(r'\\[0-9-]',text),(sec,'invalid TeX control symbol')
 assert not re.search(r'\\(?:H|S|s|x|z)(?![A-Za-z])',text),(sec,'stray variable command')

def check(sec,n,fn,t,expected,token):
 e=docs[sec]['exercises'][n-1];assert e['number']==n
 assert token in e['answer']['en'],(sec,n,'answer changed',token)
 value=m.diff(fn,m.mpf(t));assert m.almosteq(value,expected,rel_eps=m.mpf('1e-30'),abs_eps=m.mpf('1e-30')),(sec,n,value,expected)
 reports.append({'section':sec,'number':n,'numericDerivative':str(value),'expected':str(expected)})
def ck(n,fn,t,v,token):check('2-8',n,fn,t,v,token)
p=m.pi;q=m.sqrt
ck(1,lambda t:(15+4*t)**3,0,2700,'2700')
ck(2,lambda t:p*(30+2*t)**2,0,120*p,r'120\pi')
ck(3,lambda t:(4+6*t)**2,0,48,'48')
ck(4,lambda t:4*p*(40+4*t)**3/3,0,25600*p,r'25600\pi')
ck(5,lambda t:4*p*(8+2*t)**2,0,128*p,r'128\pi')
ck(6,lambda t:(20+8*t)*(10+3*t),0,140,'140')
ck(7,lambda t:(10+3*t)/(25*p),0,3/(25*p),r'3/(25\pi)')
ck(8,lambda t:(2+m.mpf('2.5')*t)*(3+m.mpf('1.5')*t)*m.sin(p/3+t/5)/2,0,21*q(3)/8+m.mpf('.3'),r'\frac{21\sqrt3}8')
ck(9,lambda t:q((25-9*(1+t/3)**2)/4),0,-m.mpf(3)/8,'-3/8')
ck(9,lambda t:q((25-4*(-2+3*t)**2)/9),0,m.mpf(8)/3,'8/3')
ck(10,lambda t:q(9-(2+5*t)**2-(2+4*t)**2),0,-18,'-18')
ck(11,lambda t:130*(3960/(4000+12*t))**2,0,-m.mpf('.764478'),'-0.764478')
ck(12,lambda t:8/(2-3*t),0,6,'6')
ck(13,lambda t:q((q(3)+500*t)**2+1),0,250*q(3),r'250\sqrt3')
ck(14,lambda t:q((100*p-t)/p),0,-1/(20*p),'-1/(20')
ck(15,lambda t:(40+5*t)*m.mpf(5)/3,0,m.mpf(25)/3,'25/3')
ck(16,lambda t:q((150-35*t)**2+(25*t)**2),4,215/q(101),r'215/\sqrt{101}')
ck(17,lambda t:q((60*t)**2+(25*t)**2),2,65,'65')
ck(18,lambda t:24/(8+m.mpf('1.6')*t),0,-m.mpf('.6'),'-0.6')
ck(19,lambda t:q(500**2+(4*(t+300)+5*t)**2),900,837/q(8674),r'837/\sqrt{8674}')
ck(20,lambda t:q((90-(45+24*t))**2+90**2),0,-24/q(5),r'-24/\sqrt5')
ck(20,lambda t:q((45+24*t)**2+90**2),0,24/q(5),r'24/\sqrt5')
ck(21,lambda t:2*(100+2*t)/(10+t),0,-m.mpf(8)/5,'-8/5')
ck(22,lambda t:q((q(65)-t)**2-1),0,-q(65)/8,r'\sqrt{65}/8')
ck(23,lambda t:m.mpf('4.9')*(t*t-(t-1)**2),2,m.mpf('9.8'),'9.8')
ck(24,lambda t:q(100+(m.mpf('4.9')*(t*t-(t-1)**2))**2),2,m.mpf('144.06')/q(m.mpf('316.09')),'144.06')
ck(25,lambda t:p*(200+20*t)**3/27+10000*t,0,10000+800000*p/9,'800000')
ck(26,lambda t:q((m.mpf(1)/3+q(10)*t)**2+(2*m.sin(p*(m.mpf(1)/3+q(10)*t)/2))**2),0,1+3*p*q(3)/2,r'3\pi\sqrt3/2')
# Inverse-function rates use derivative of volume vs height, independently.
for n,V,h,Q,target,token in [(27,lambda h:10*(m.mpf('.3')*h+h*h/2),m.mpf('.3'),m.mpf('.2'),m.mpf(1)/30,'1/30'),(28,lambda h:15*h*h,m.mpf('.5'),12,m.mpf(4)/5,'4/5'),(29,lambda h:p*h**3/12,10,30,6/(5*p),r'6/(5\pi)'),(30,lambda h:20*(12*h+m.mpf(11)*h*h/6),5,m.mpf('.8'),m.mpf(3)/2275,'3/2275')]:
 actual=Q/m.diff(V,h);assert m.almosteq(actual,target);assert token in docs['2-8']['exercises'][n-1]['answer']['en'];reports.append({'section':'2-8','number':n,'inverseVolumeRate':str(actual)})
ck(31,lambda t:q(3)*(30+10*t)**2/4,0,150*q(3),r'150\sqrt3')
ck(32,lambda t:m.atan(100/(100*q(3)+8*t)),0,-m.mpf('.02'),'-0.02')
ck(33,lambda t:q((20*t)**2+(6*t)**2+625),5,436/q(461),r'436/\sqrt{461}')
ck(34,lambda t:7**2*(2*p*t/60)/2,0,49*p/60,r'\pi r^2/60')
ck(35,lambda t:m.acos((6+4*t)/10),0,-m.mpf('.5'),'-1/2')
ck(37,lambda t:150*600/(150+20*t),0,-80,'-80')
h=m.findroot(lambda h:p*(30*h*h-h**3/3)-9000*p,20);v=2000/(p*(60*h-h*h));assert f'{float(v):.10f}' in docs['2-8']['exercises'][37]['answer']['en'];reports.append({'section':'2-8','number':38,'halfVolumeDepth':str(h),'riseRate':str(v)})
ck(39,lambda t:1/(1/(80+m.mpf('.3')*t)+1/(100+m.mpf('.2')*t)),0,m.mpf(107)/810,'107/810')
ck(40,lambda t:400*(80/(80-10*t))**(m.mpf(5)/7),0,m.mpf(250)/7,'250/7')
ck(41,lambda t:q((40*t)**2+(60*t)**2-2*40*60*t*t*m.cos(p/3)),m.mpf('.5'),20*q(7),r'20\sqrt7')
v=m.diff(lambda t:m.mpf('.007')*(m.mpf('.12')*(18+t/m.mpf(2000000))**m.mpf('2.53'))**(m.mpf(2)/3),0);assert f'{float(v):.10g}' in docs['2-8']['exercises'][41]['answer']['en'];reports.append({'section':'2-8','number':42,'brainRate':str(v)})
ck(43,lambda t:q(144+225-360*m.cos(p/3+p*t/90)),0,p/(3*q(7)),r'\pi/(3\sqrt7)')
ck(44,lambda t:q((39-q((5+2*t)**2+144))**2-144),0,-10/q(133),r'10/\sqrt{133}')
ck(45,lambda t:q(4000**2+(3000+600*t)**2),0,360,'360')
ck(45,lambda t:m.atan((3000+600*t)/4000),0,m.mpf('.096'),'0.096')
ck(46,lambda t:3*m.tan(m.atan(m.mpf(1)/3)+8*p*t),0,80*p/3,r'80\pi/3')
ck(47,lambda t:5/m.tan(p/3-p*t/6),0,10*p/9,r'10\pi/9')
ck(48,lambda t:10+10*m.sin(m.asin(m.mpf('.6'))+p*t),0,8*p,r'8\pi')
ck(49,lambda t:q((300*m.cos(p/6)*t)**2+(1+300*m.sin(p/6)*t)**2),m.mpf(1)/60,1650/q(31),r'1650/\sqrt{31}')
ck(50,lambda t:q((3*t-q(2)*t)**2+(q(2)*t)**2),m.mpf(1)/4,q(13-6*q(2)),r'13-6\sqrt2')
ck(51,lambda t:q(50000-40000*m.cos(m.acos(m.mpf(1)/4)+m.mpf('.07')*t)),0,7*q(15)/4,r'7\sqrt{15}/4')
ck(52,lambda t:q(80-64*m.cos(p/6-11*p*t/360)),0,-11*p/(90*q(5-2*q(3))),r'90\sqrt{5-2\sqrt3}')
# Hand-derived error propagation: compare independent differentiation against published values.
for n,fn,t,v,token in [(39,lambda t:(30+m.mpf('.1')*t)**3,0,270,'270'),(40,lambda t:p*(24+m.mpf('.2')*t)**2,0,m.mpf('9.6')*p,'9.6'),(41,lambda t:(84+m.mpf('.5')*t)**3/(6*p*p),0,1764/(p*p),'1764'),(42,lambda t:2*p*(25+m.mpf('.0005')*t)**3/3,0,m.mpf('.625')*p,'0.625'),(44,lambda t:20/m.sin(p/6+p*t/180),0,-2*p*q(3)/9,r'2\pi\sqrt3/9')]:check('2-9',n,fn,t,v,token)
# Check the independently derived integral answers in the manual part of 4.5.
for n,fn,lo,hi,target,token in [(46,lambda z:z*q(4-z*z),0,-2,m.mpf(8)/3,'|a|^3/3'),(53,lambda z:q(2*z+1),0,1,(3*q(3)-1)/3,'3'),(54,lambda z:2*m.sin(z)-m.sin(2*z),0,p,4,'4'),(55,lambda z:(z+3)*q(4-z*z),-2,2,6*p,r'6\pi'),(56,lambda z:z*q(1-z**4),0,1,p/8,r'\pi/8'),(58,lambda z:85-m.mpf('.18')*m.cos(p*z/12),0,24,2040,'2040'),(85,lambda z:z*m.sin(z)/(1+m.cos(z)**2),0,p,p*p/4,r'\pi^2/4')]:
 value=m.quad(fn,[lo,hi]);assert m.almosteq(value,target);assert token in docs['4-5']['exercises'][n-1]['answer']['en'];reports.append({'section':'4-5','number':n,'quadrature':str(value)})
(R/'exercise-checks/remaining-sections-independent.json').write_text(json.dumps({'passed':len(reports),'checks':reports},indent=2)+'\n');print('PASS:',len(reports),'independent derivative, inverse-rate and quadrature checks')
