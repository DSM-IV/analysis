"""Read-only final checks for the389 authored Chapter14 exercises."""
import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as S
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R));import build_exercises as builder
counts=[54,60,77,62,63,65,8];figs=0
for sec,count in zip(range(4,11),counts):
 p=R/f'exercise-content/s14-{sec}.json';d=json.loads(p.read_text());builder.validate_document(d,p);assert [e['number'] for e in d['exercises']]==list(range(1,count+1))
 for e in d['exercises']:
  for key in ['statement','hint','steps','answer','check']:
   value=e[key]['en'];text=' '.join(value) if isinstance(value,list) else value;assert not re.search('[가-힣]',text),(sec,e['number'],key)
  if 'figure' in e:
   asset=(R/'exercises'/e['figure']['src']).resolve();ET.parse(asset);figs+=1
 print(f'14.{sec}: {count} complete cards validated')
assert sum(counts)==389
# Critical independent calculations, distinct from the statement-generation routines.
x,y,z,t=S.symbols('x y z t',real=True)
assert S.expand((x*x+y*y-z).subs({x:-S.Rational(5,4),y:-S.Rational(5,4),z:S.Rational(25,8)}))==0
for p in [(S.Rational(19,3),S.Rational(14,3),S.Rational(19,3)),(-7,-2,-7)]:assert sum(a*a for a in p)==102
F=4*x*y*y-x*x*y*y-x*y**3;assert F.subs({x:1,y:2})==4 and F.subs({x:2,y:4})==-64
F=x**3*S.sqrt(y*y+z*z);G=S.Matrix([S.diff(F,j).subs({x:2,y:3,z:4}) for j in [x,y,z]]);assert G==S.Matrix([60,S.Rational(24,5),S.Rational(32,5)])
assert S.simplify(40+G.dot(S.Matrix([-S.Rational(2,100),S.Rational(1,100),-S.Rational(3,100)]))-S.Rational(38656,1000))==0
# Closest-point product constraint and distance.
p=[3**(-S.Rational(1,4)),S.sqrt(2)*3**(-S.Rational(1,4)),3**S.Rational(1,4)];assert S.simplify(p[0]*p[1]**2*p[2]**3)==2;assert S.simplify(sum(a*a for a in p)-2*S.sqrt(3))==0
# Ellipse enclosure: all boundary points of circle y in[0,2].
q=(2*y-y*y)/S.Rational(3,2)+y*y/S.Rational(9,2);assert S.simplify(q-(1-S.Rational(4,9)*(y-S.Rational(3,2))**2))==0
# Newton roots checked against original equations at the stored precision.
report=json.loads((R/'exercise-checks/s14-10-newton-report.json').read_text())
for a,b in report['roots']:assert abs(a**a+b**b-1000)<1e-9 and abs(a**b+b**a-100)<1e-9
print(f'389 cards; {figs} valid original SVG references; English-language scan clean; independent checks passed')
